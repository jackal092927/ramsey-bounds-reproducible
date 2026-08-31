"""Regressions for the independent PySAT-free generalized-core CNF checker."""

from __future__ import annotations

import copy
import gzip
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from .check_r3_18_budget7_branch1_core_cnf import (
    AuditError,
    CnfAudit,
    FormulaSpec,
    _canonical_clause_line,
    build_reconstruction_plan,
    compare_gzip_dimacs,
    iter_expected_clauses,
    load_ordered_bank,
    main,
    read_seed_matrix,
    validate_core,
    validate_manifest,
    validate_result,
)


def _complete_rows(order: int) -> list[int]:
    full = (1 << order) - 1
    return [full & ~(1 << vertex) for vertex in range(order)]


def _remove_edge(rows: list[int], edge: tuple[int, int]) -> list[int]:
    result = rows.copy()
    u, v = edge
    result[u] &= ~(1 << v)
    result[v] &= ~(1 << u)
    return result


def _write_toy_cnf(
    path: Path,
    plan,
    masks: list[int],
    units: tuple[int, ...],
    *,
    replacement: tuple[int, list[int]] | None = None,
    header_clause_delta: int = 0,
    append_clause: list[int] | None = None,
) -> None:
    clauses = [
        clause for _, clause in iter_expected_clauses(plan, masks, units)
    ]
    if replacement is not None:
        index, clause = replacement
        clauses[index] = clause
    declared = len(clauses) + header_clause_delta
    with path.open("wb") as raw:
        with gzip.GzipFile(
            filename="", mode="wb", fileobj=raw, mtime=0
        ) as sink:
            sink.write(f"p cnf {plan.maximum_variable} {declared}\n".encode("ascii"))
            for clause in clauses:
                sink.write(_canonical_clause_line(clause))
            if append_clause is not None:
                sink.write(_canonical_clause_line(append_clause))


class IndependentCoreCnfCheckerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.spec = FormulaSpec(
            order=6,
            fixed_edge=(4, 5),
            residual_deletions=2,
            degree_cap=3,
            bank_set_size=3,
        )
        self.rows = _complete_rows(self.spec.order)
        self.masks = [0b000111, 0b111000]
        self.plan = build_reconstruction_plan(self.rows, self.spec)
        _, self.units, _ = validate_core("toy", ((0, 1),), self.plan)

    def test_toy_formula_is_reconstructed_clause_for_clause(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "toy.cnf.gz"
            _write_toy_cnf(path, self.plan, self.masks, self.units)
            audit = compare_gzip_dimacs(
                path, self.plan, self.masks, self.units
            )
            self.assertEqual(audit.variables, self.plan.maximum_variable)
            self.assertEqual(
                audit.clauses,
                self.plan.common_clause_count_without_bank
                + len(self.masks)
                + len(self.units),
            )
            self.assertEqual(audit.lines, audit.clauses + 1)
            self.assertEqual(len(audit.uncompressed_sha256), 64)
            self.assertEqual(len(audit.gzip_sha256), 64)

    def test_clause_mutation_fails_at_the_exact_block(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "mutated.cnf.gz"
            _write_toy_cnf(
                path,
                self.plan,
                self.masks,
                self.units,
                replacement=(0, [-1]),
            )
            with self.assertRaisesRegex(AuditError, "index 1 in triangles"):
                compare_gzip_dimacs(path, self.plan, self.masks, self.units)

    def test_wrong_trailing_core_unit_is_rejected(self) -> None:
        expected_clause_count = (
            self.plan.common_clause_count_without_bank + len(self.masks)
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "wrong-unit.cnf.gz"
            _write_toy_cnf(
                path,
                self.plan,
                self.masks,
                self.units,
                replacement=(expected_clause_count, [-2]),
            )
            with self.assertRaisesRegex(AuditError, "candidate_units"):
                compare_gzip_dimacs(path, self.plan, self.masks, self.units)

    def test_header_and_extra_clause_are_both_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            wrong_header = root / "wrong-header.cnf.gz"
            _write_toy_cnf(
                wrong_header,
                self.plan,
                self.masks,
                self.units,
                header_clause_delta=1,
            )
            with self.assertRaisesRegex(AuditError, "header mismatch"):
                compare_gzip_dimacs(
                    wrong_header, self.plan, self.masks, self.units
                )
            extra = root / "extra.cnf.gz"
            _write_toy_cnf(
                extra,
                self.plan,
                self.masks,
                self.units,
                append_clause=[1],
            )
            with self.assertRaisesRegex(AuditError, "extra clauses"):
                compare_gzip_dimacs(extra, self.plan, self.masks, self.units)

    def test_original_nonedge_is_excluded_from_counter_and_core(self) -> None:
        rows = _remove_edge(self.rows, (0, 1))
        plan = build_reconstruction_plan(rows, self.spec)
        self.assertNotIn((0, 1), plan.residual_edges)
        with self.assertRaisesRegex(AuditError, "non-residual"):
            validate_core("toy", ((0, 1),), plan)

    def test_matrix_parser_rejects_asymmetry(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "matrix.txt"
            path.write_text("0 1\n0 0\n", encoding="ascii")
            with self.assertRaisesRegex(AuditError, "symmetric"):
                read_seed_matrix(path)

    def test_bank_parser_preserves_order_and_rejects_duplicates(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bank.json"
            path.write_text(
                json.dumps({"masks": ["7", "38"]}), encoding="utf-8"
            )
            masks, digest = load_ordered_bank(
                path, order=6, set_size=3
            )
            self.assertEqual(masks, self.masks)
            self.assertEqual(len(digest), 64)
            path.write_text(
                json.dumps({"masks": ["7", "7"]}), encoding="utf-8"
            )
            with self.assertRaisesRegex(AuditError, "duplicate"):
                load_ordered_bank(path, order=6, set_size=3)

    def test_manifest_rejects_pilot_subset_transfer_and_order_tampering(self) -> None:
        audit = CnfAudit(
            variables=154190,
            clauses=718454,
            lines=718455,
            uncompressed_bytes=123,
            uncompressed_sha256="1" * 64,
            gzip_bytes=45,
            gzip_sha256="2" * 64,
            structural_clauses_sha256="3" * 64,
            degree_clauses_sha256="4" * 64,
        )
        candidate_sha256 = "5" * 64
        formula_fingerprint = "6" * 64
        matrix_sha256 = "7" * 64
        bank_sha256 = "8" * 64
        ordered_sha256 = "9" * 64
        payload = {
            "schema": (
                "ramsey-r3-18-n100-exact-budget7-branch1-core-cnf-manifest-v1"
            ),
            "status": "FROZEN_DIMACS_EXPORTED_UNCHECKED",
            "candidate": {
                "label": "K_ab",
                "deletion_edges": [[11, 62], [18, 61]],
                "size": 2,
                "assumption_units": [-1085, -1672],
                "candidate_sha256": candidate_sha256,
                "unit_semantics": "d_e=true is the DIMACS unit -x_e",
                "minimality_claim": False,
                "pilot_anchor_proves_candidate_UNSAT": False,
            },
            "common_formula": {
                "schema": (
                    "ramsey-r3-18-n100-exact-budget7-branch1-common-formula-v1"
                ),
                "formula_fingerprint_sha256": formula_fingerprint,
                "maximum_variable": 154190,
                "materialized_structural_and_degree_clauses": 466681,
                "materialized_universal_I18_clauses": 251771,
                "common_clause_count": 718452,
                "formula_is_relaxation_of_target": True,
                "learned_core_clauses_installed": 0,
                "clause_order": [
                    "structural clauses including exact-six and fixed branch unit",
                    "degree-cap clauses",
                    "universal I18 clauses in ordered-bank order",
                    "candidate deletion units in lexicographic edge order",
                ],
            },
            "dimacs": {
                "variables": 154190,
                "clauses": 718454,
                "header_and_clause_lines": 718455,
                "uncompressed_sha256": "1" * 64,
                "gzip_sha256": "2" * 64,
                "uncompressed_bytes": 123,
                "gzip_bytes": 45,
            },
            "inputs": {
                "matrix": {"sha256": matrix_sha256},
                "universal_bank": {
                    "sha256": bank_sha256,
                    "ordered_masks_sha256": ordered_sha256,
                    "masks": 251771,
                },
            },
            "global_ramsey_implication": None,
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "manifest.json"
            for field, mutation, pattern in (
                (
                    "pilot",
                    lambda value: value["candidate"].__setitem__(
                        "pilot_anchor_proves_candidate_UNSAT", True
                    ),
                    "transfers pilot UNSAT",
                ),
                (
                    "order",
                    lambda value: value["common_formula"].__setitem__(
                        "clause_order", list(reversed(value["common_formula"]["clause_order"]))
                    ),
                    "clause-order",
                ),
            ):
                with self.subTest(field=field):
                    broken = copy.deepcopy(payload)
                    mutation(broken)
                    path.write_text(json.dumps(broken), encoding="utf-8")
                    with self.assertRaisesRegex(AuditError, pattern):
                        validate_manifest(
                            path,
                            label="K_ab",
                            edges=((11, 62), (18, 61)),
                            units=(-1085, -1672),
                            candidate_sha256=candidate_sha256,
                            formula_fingerprint=formula_fingerprint,
                            matrix_sha256=matrix_sha256,
                            bank_sha256=bank_sha256,
                            ordered_masks_sha256=ordered_sha256,
                            masks=range(251771),
                            audit=audit,
                        )

    def test_result_claim_bits_and_checker_transcript_are_fail_closed(self) -> None:
        manifest = {"candidate": {"label": "K"}, "dimacs": {"clauses": 1}}
        with tempfile.TemporaryDirectory() as directory:
            manifest_path = Path(directory) / "manifest.json"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            manifest_hash = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
            result_path = Path(directory) / "result.json"
            valid = {
                "schema": (
                    "ramsey-r3-18-n100-exact-budget7-branch1-core-proof-result-v1"
                ),
                "status": "UNSAT_PROOF_VERIFIED_LOCAL_BRANCH1_EXACT_SIX_CORE",
                "candidate": manifest["candidate"],
                "dimacs": manifest["dimacs"],
                "manifest": {"sha256": manifest_hash},
                "minimality_claim": False,
                "global_ramsey_implication": None,
                "proof_verified": True,
                "local_branch1_exact_six_superset_exclusion_proved": True,
                "external_proof": {
                    "status": "UNSAT_PROOF_WRITTEN",
                    "exitcode": 20,
                },
                "drat_check": {
                    "status": "VERIFIED",
                    "exitcode": 0,
                    "stdout_tail": "c checker output\ns VERIFIED\n",
                },
            }
            result_path.write_text(json.dumps(valid), encoding="utf-8")
            self.assertEqual(
                validate_result(
                    result_path,
                    manifest_path=manifest_path,
                    manifest=manifest,
                )["proof_verified"],
                True,
            )
            mutations = (
                (
                    "nonboolean",
                    lambda value: value.__setitem__("proof_verified", "true"),
                    "not Boolean",
                ),
                (
                    "exitcode",
                    lambda value: value["drat_check"].__setitem__("exitcode", 1),
                    "nonzero checker",
                ),
                (
                    "solver-exitcode",
                    lambda value: value["external_proof"].__setitem__(
                        "exitcode", 10
                    ),
                    "non-UNSAT solver",
                ),
                (
                    "transcript",
                    lambda value: value["drat_check"].__setitem__(
                        "stdout_tail", "s VERIFIED-ish\n"
                    ),
                    "exact s VERIFIED",
                ),
                (
                    "false-verified-status",
                    lambda value: value.__setitem__("proof_verified", False),
                    "unverified result uses",
                ),
            )
            for name, mutation, pattern in mutations:
                with self.subTest(name=name):
                    broken = copy.deepcopy(valid)
                    mutation(broken)
                    result_path.write_text(json.dumps(broken), encoding="utf-8")
                    with self.assertRaisesRegex(AuditError, pattern):
                        validate_result(
                            result_path,
                            manifest_path=manifest_path,
                            manifest=manifest,
                        )

    def test_json_output_symlink_cannot_overwrite_checker_sources(self) -> None:
        finite = Path(__file__).resolve().parent
        for source_name in (
            "check_r3_18_budget7_branch1_core_cnf.py",
            "independent_seqcounter.py",
        ):
            with (
                self.subTest(source=source_name),
                tempfile.TemporaryDirectory() as directory,
            ):
                root = Path(directory)
                source = finite / source_name
                source_before = source.read_bytes()
                output_alias = root / "audit.json"
                output_alias.symlink_to(source)
                argv = [
                    "check_r3_18_budget7_branch1_core_cnf.py",
                    "--cnf",
                    str(root / "unused.cnf.gz"),
                    "--matrix",
                    str(root / "unused-matrix.txt"),
                    "--universal-bank",
                    str(root / "unused-bank.json"),
                    "--expected-label",
                    "K_ab",
                    "--core",
                    "11-62,18-61",
                    "--json-output",
                    str(output_alias),
                    "--overwrite",
                ]
                with mock.patch("sys.argv", argv):
                    with self.assertRaisesRegex(ValueError, "collides"):
                        main()
                self.assertTrue(output_alias.is_symlink())
                self.assertEqual(source.read_bytes(), source_before)


if __name__ == "__main__":
    unittest.main()
