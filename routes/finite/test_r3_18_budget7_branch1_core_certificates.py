"""Regressions for deterministic branch-1 generalized-core certificate export."""

from __future__ import annotations

import copy
import gzip
import itertools
import json
import math
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path

from .bounded_deletion_sat_cegar import build_variables
from .budget8_next import deterministic_gzip_text, sha256
from .r3_18_budget5_branch import EXPECTED_INPUT_SHA256
from .r3_18_budget7_branch import (
    EXPECTED_BUDGET6_SUMMARY_SHA256,
    load_universal_bank,
)
from .r3_18_budget7_branch1_assumption_cores import CommonFormula, build_common_formula
from .r3_18_budget7_branch1_core_certificates import (
    DEFAULT_CORES,
    EXPECTED_CADICAL_COMMIT,
    EXPECTED_DRAT_TRIM_COMMIT,
    EXPECTED_FORMULA_FINGERPRINT,
    _load_candidate_specs,
    _public_tool_result,
    _validate_toolchain,
    candidate_artifact_paths,
    classify_external_result,
    main as certificate_main,
    full_dimacs_lines,
    require_complete_proof_artifact,
    validate_candidate,
    validate_export_targets,
    validate_pilot,
)
from .verify_ramsey import read_matrix


HERE = Path(__file__).resolve().parent
SEED = HERE / "certificates" / "r3_18_n100_nearmiss.txt"
BUDGET6 = HERE / "r3_18_budget6_summary.json"
BANK = HERE / "r3_18_budget6_branch_0_universal_union.cuts.json"
PILOT = HERE / "r3_18_budget7_branch1_assumption_core_pilot.json"
PROOF_SUMMARY = HERE / "r3_18_budget7_branch1_core_proof_summary.json"


class Branch1CoreCertificateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rows = read_matrix(SEED)
        masks, info = load_universal_bank(BANK)
        cls.formula = build_common_formula(
            cls.rows, sha256(SEED), masks, info
        )
        cls.pilot = json.loads(PILOT.read_text(encoding="utf-8"))
        cls.anchors = validate_pilot(cls.pilot, cls.formula)

    def test_pinned_inputs_and_rebuilt_formula_are_strictly_validated(self) -> None:
        self.assertEqual(sha256(SEED), EXPECTED_INPUT_SHA256)
        self.assertEqual(sha256(BUDGET6), EXPECTED_BUDGET6_SUMMARY_SHA256)
        self.assertEqual(
            self.formula.metadata["formula_fingerprint_sha256"],
            EXPECTED_FORMULA_FINGERPRINT,
        )
        self.assertEqual(len(self.anchors), 2)
        broken = copy.deepcopy(self.pilot)
        broken["common_formula"]["formula_fingerprint_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "formula fingerprint"):
            validate_pilot(broken, self.formula)
        broken = copy.deepcopy(self.pilot)
        broken["records"][0]["record_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "record digest"):
            validate_pilot(broken, self.formula)

    def test_default_size_two_candidates_have_negative_units_and_anchors(self) -> None:
        candidates = [
            validate_candidate(label, edges, self.formula, self.anchors)
            for label, edges in DEFAULT_CORES
        ]
        self.assertEqual([candidate.label for candidate in candidates], [
            "K_ab", "K_ac", "K_ad", "K_bd"
        ])
        self.assertEqual(
            candidates[0].edges,
            ((11, 62), (18, 61)),
        )
        self.assertEqual(candidates[0].assumption_units, (-1085, -1672))
        self.assertEqual(candidates[1].assumption_units, (-1085, -1675))
        self.assertEqual(candidates[2].assumption_units, (-1085, -1680))
        self.assertEqual(candidates[3].assumption_units, (-1672, -1680))
        self.assertEqual(
            [candidate.candidate_sha256 for candidate in candidates],
            [
                "cba54b472f5de7cd2987ee512f9dd8346348c52a252531537afb6a00f23f02af",
                "012e7789196da1797128350c2f8d85769e7ead59e516d629e8c47e8aef4d4bd6",
                "a1441cdbaeb5c0d10d33bad4082a6b61bf643fecef6e6cc6c14b718a269f51ac",
                "6409c5bdf4c2b65524384699fda070ebf8a38f303bd01b02ebf49ada49a4d063",
            ],
        )
        self.assertTrue(all(candidate.anchor_records for candidate in candidates))
        self.assertTrue(
            all(unit < 0 for candidate in candidates for unit in candidate.assumption_units)
        )

    def test_explicit_size_three_and_unanchored_residual_candidates_are_accepted(self) -> None:
        size_three = validate_candidate(
            "K1_size3",
            ((11, 62), (18, 61), (18, 64)),
            self.formula,
            self.anchors,
        )
        self.assertEqual(size_three.assumption_units, (-1085, -1672, -1675))
        self.assertTrue(size_three.anchor_records)
        unanchored = validate_candidate(
            "unanchored", ((1, 97),), self.formula, self.anchors
        )
        self.assertEqual(unanchored.assumption_units, (-195,))
        self.assertFalse(unanchored.anchor_records)

    def test_candidate_validation_rejects_ambiguous_or_nonresidual_sets(self) -> None:
        bad = (
            ("reverse", ((62, 11), (18, 61), (18, 64))),
            ("unsorted", ((18, 61), (11, 62), (18, 64))),
            ("duplicate", ((11, 62), (11, 62))),
            ("fixed", ((97, 99),)),
            ("nonedge", ((0, 1),)),
        )
        for label, edges in bad:
            with self.subTest(label=label), self.assertRaises(ValueError):
                validate_candidate(label, edges, self.formula, self.anchors)
        with self.assertRaisesRegex(ValueError, "safe artifact"):
            validate_candidate(
                "../K", DEFAULT_CORES[0][1], self.formula, self.anchors
            )

    def test_full_dimacs_materializes_bank_before_core_units(self) -> None:
        variables, pairs = build_variables(18)
        mask = (1 << 18) - 1
        formula = CommonFormula(
            clauses=[[1, 2], [-3]],
            variables=variables,
            pairs=pairs,
            original_edges=set(pairs),
            residual_edges=set(pairs),
            universal_masks=[mask],
            metadata={
                "total_clauses": 3,
                "maximum_variable": max(variables.values()),
            },
        )
        lines = list(full_dimacs_lines(formula, (-1, -2)))
        self.assertEqual(lines[0], "p cnf 153 5\n")
        self.assertEqual(lines[1:3], ["1 2 0\n", "-3 0\n"])
        universal = [int(value) for value in lines[3].split()[:-1]]
        self.assertEqual(len(universal), 153)
        self.assertEqual(lines[-2:], ["-1 0\n", "-2 0\n"])

    def test_deterministic_gzip_hashes_match_for_identical_export(self) -> None:
        variables, pairs = build_variables(18)
        formula = CommonFormula(
            clauses=[[1, -2]],
            variables=variables,
            pairs=pairs,
            original_edges=set(pairs),
            residual_edges=set(pairs),
            universal_masks=[(1 << 18) - 1],
            metadata={"total_clauses": 2, "maximum_variable": 153},
        )
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first.cnf.gz"
            second = Path(directory) / "second.cnf.gz"
            one = deterministic_gzip_text(first, full_dimacs_lines(formula, (-1,)))
            two = deterministic_gzip_text(second, full_dimacs_lines(formula, (-1,)))
            self.assertEqual(one, two)
            self.assertEqual(first.read_bytes(), second.read_bytes())
            with gzip.open(first, "rt", encoding="ascii") as source:
                exported = source.readlines()
            self.assertEqual(exported[0], "p cnf 153 3\n")
            self.assertEqual(exported[-1], "-1 0\n")

    def test_candidate_json_binds_formula_fingerprint(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "cores.json"
            payload = {
                "schema": (
                    "ramsey-r3-18-n100-exact-budget7-branch1-core-candidates-v1"
                ),
                "formula_fingerprint_sha256": EXPECTED_FORMULA_FINGERPRINT,
                "cores": [{"label": "K1", "edges": [[11, 62], [18, 61], [18, 64]]}],
            }
            path.write_text(json.dumps(payload), encoding="utf-8")
            specs, source = _load_candidate_specs([], path)
            self.assertEqual(specs[0][0], "K1")
            self.assertEqual(source["sha256"], sha256(path))
            payload["formula_fingerprint_sha256"] = "0" * 64
            path.write_text(json.dumps(payload), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "fingerprint"):
                _load_candidate_specs([], path)

    def test_external_status_classification_is_fail_closed(self) -> None:
        for proof in (
            {"status": "TIME_LIMIT"},
            {"status": "ERROR"},
            {"status": "UNKNOWN"},
        ):
            with self.subTest(proof=proof):
                status, verified = classify_external_result(proof, None)
                self.assertEqual(status, "UNKNOWN_EXTERNAL_PROOF_NOT_COMPLETED")
                self.assertFalse(verified)
        self.assertEqual(
            classify_external_result({"status": "SAT"}, None),
            ("QUARANTINED_EXTERNAL_SAT_MISMATCH", False),
        )
        self.assertEqual(
            classify_external_result(
                {"status": "UNSAT_PROOF_WRITTEN"}, {"status": "TIME_LIMIT"}
            ),
            ("UNKNOWN_PROOF_UNVERIFIED", False),
        )
        self.assertEqual(
            classify_external_result(
                {"status": "UNSAT_PROOF_WRITTEN"}, {"status": "VERIFIED"}
            ),
            ("UNSAT_PROOF_VERIFIED_LOCAL_BRANCH1_EXACT_SIX_CORE", True),
        )

    def test_exit_twenty_without_a_trace_is_downgraded(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing.drat.gz"
            raw = {
                "status": "UNSAT_PROOF_WRITTEN",
                "proof": {"gzip_sha256": "0" * 64},
            }
            downgraded = require_complete_proof_artifact(raw, missing)
            self.assertEqual(
                downgraded["status"], "ERROR_UNSAT_WITHOUT_PROOF_ARTIFACT"
            )
            self.assertFalse(classify_external_result(downgraded, None)[1])
            present = Path(directory) / "present.drat.gz"
            present.write_bytes(b"not the recorded trace")
            mismatch = require_complete_proof_artifact(raw, present)
            self.assertEqual(
                mismatch["status"], "ERROR_PROOF_ARTIFACT_DIGEST_MISMATCH"
            )

    def test_public_tool_result_redacts_absolute_paths(self) -> None:
        executable = Path("/bin/sh")
        raw = {
            "status": "ERROR",
            "stdout_tail": f"tool={executable.resolve()} repo={HERE.resolve()}",
        }
        public = _public_tool_result(raw, executable, "commit")
        rendered = json.dumps(public)
        self.assertNotIn(str(HERE.resolve()), rendered)
        self.assertNotIn(str(executable.resolve()), rendered)
        self.assertEqual(public["tool_basename"], "sh")

    def test_summary_collision_with_every_candidate_artifact_is_rejected(self) -> None:
        candidate = validate_candidate(
            DEFAULT_CORES[0][0], DEFAULT_CORES[0][1], self.formula, self.anchors
        )
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "artifacts"
            paths = candidate_artifact_paths(output, candidate)
            for kind, summary in (
                ("cnf", paths.cnf),
                ("manifest", paths.manifest),
                ("result", paths.result),
                ("drat", paths.drat),
            ):
                with self.subTest(kind=kind):
                    with self.assertRaisesRegex(ValueError, "target collision"):
                        validate_export_targets(summary, output, [candidate])
            self.assertFalse(output.exists())

    def test_every_resolved_collision_between_candidate_targets_is_rejected(self) -> None:
        candidate = validate_candidate(
            DEFAULT_CORES[0][0], DEFAULT_CORES[0][1], self.formula, self.anchors
        )
        for source_name, target_name in itertools.combinations(
            ("cnf", "manifest", "result", "drat"), 2
        ):
            with self.subTest(source=source_name, target=target_name):
                with tempfile.TemporaryDirectory() as directory:
                    output = Path(directory) / "artifacts"
                    output.mkdir()
                    paths = candidate_artifact_paths(output, candidate)
                    source = getattr(paths, source_name)
                    target = getattr(paths, target_name)
                    source.symlink_to(target.name)
                    with self.assertRaisesRegex(ValueError, "target collision"):
                        validate_export_targets(
                            Path(directory) / "summary.json", output, [candidate]
                        )

    def test_toolchain_is_bound_to_adjacent_source_commit_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cadical_dir = root / "cadical"
            drat_dir = root / "drat"
            cadical_dir.mkdir()
            drat_dir.mkdir()
            cadical = cadical_dir / "cadical"
            drat = drat_dir / "drat-trim"
            for executable in (cadical, drat):
                executable.write_text("#!/bin/sh\nexit 0\n", encoding="ascii")
                executable.chmod(0o755)
            (cadical_dir / "SOURCE_COMMIT").write_text(
                EXPECTED_CADICAL_COMMIT + "\n", encoding="ascii"
            )
            (drat_dir / "SOURCE_COMMIT").write_text(
                EXPECTED_DRAT_TRIM_COMMIT + "\n", encoding="ascii"
            )
            self.assertTrue(
                _validate_toolchain(
                    cadical,
                    EXPECTED_CADICAL_COMMIT,
                    drat,
                    EXPECTED_DRAT_TRIM_COMMIT,
                )
            )
            (drat_dir / "SOURCE_COMMIT").write_text("wrong\n", encoding="ascii")
            with self.assertRaisesRegex(ValueError, "SOURCE_COMMIT mismatch"):
                _validate_toolchain(
                    cadical,
                    EXPECTED_CADICAL_COMMIT,
                    drat,
                    EXPECTED_DRAT_TRIM_COMMIT,
                )

    def test_proof_summary_is_claim_bounded_and_counts_exactly(self) -> None:
        payload = json.loads(PROOF_SUMMARY.read_text(encoding="utf-8"))
        self.assertEqual(
            payload["status"],
            "FOUR_SINGLETON_NO_GOODS_PROOF_VERIFIED_EXACT_SEVEN_UNKNOWN",
        )
        self.assertIsNone(payload["global_ramsey_implication"])
        self.assertIsNone(payload["exact_seven_repair_exists"])
        self.assertFalse(payload["minimality_claim"])
        records = payload["records"]
        self.assertEqual(
            [record["label"] for record in records],
            ["K_a", "K_b", "K_c", "K_d"],
        )
        self.assertEqual(
            [record["assumption_units"] for record in records],
            [[-1085], [-1672], [-1675], [-1680]],
        )
        asset_names = {
            record[field]
            for record in records
            for field in ("cnf_asset", "proof_asset")
        }
        self.assertEqual(len(asset_names), 2 * len(records))
        self.assertTrue(
            all("/" not in name and "\\" not in name for name in asset_names)
        )
        self.assertTrue(all(record["proof_verified"] for record in records))
        coverage = payload["coverage"]
        raw = math.comb(826, 6)
        degree = math.comb(808, 6)
        singleton_union = raw - math.comb(822, 6)
        overlap = degree - math.comb(804, 6)
        additional = singleton_union - overlap
        self.assertEqual(coverage["raw_exact_six_supports"], raw)
        self.assertEqual(coverage["degree_cap_excluded"], degree)
        self.assertEqual(coverage["singleton_union_excluded"], singleton_union)
        self.assertEqual(coverage["singleton_union_overlap_with_degree_cap"], overlap)
        self.assertEqual(coverage["additional_excluded_beyond_degree_cap"], additional)
        self.assertEqual(
            coverage["combined_degree_and_singleton_excluded"], degree + additional
        )
        self.assertEqual(
            coverage["remaining_after_two_filters"], raw - degree - additional
        )

    def test_cli_collision_fails_before_creating_output_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "artifacts"
            colliding_summary = output / "branch1_core_K_ab_size2.cnf.gz"
            argv = [
                "core-certificates",
                "--core",
                "K_ab:11-62,18-61",
                "--output-dir",
                str(output),
                "--summary-json",
                str(colliding_summary),
            ]
            with mock.patch.object(sys, "argv", argv):
                with self.assertRaisesRegex(ValueError, "target collision"):
                    certificate_main()
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
