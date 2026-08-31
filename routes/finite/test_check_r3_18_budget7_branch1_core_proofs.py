"""Small and mocked regressions for generalized-core proof replay."""

from __future__ import annotations

import copy
import gzip
import hashlib
import io
import json
import os
import subprocess
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

import reproduce

from .check_r3_18_budget7_branch1_core_cnf import (
    EXPECTED_FORMULA_FINGERPRINT,
    PRODUCTION_COMMON_CLAUSES,
    PRODUCTION_MAXIMUM_VARIABLE,
    PRODUCTION_ORDER,
    lexicographic_edge_variables,
)
from .check_r3_18_budget7_branch1_core_proofs import (
    AuditError,
    CNF_AUDIT_STATUS,
    EXPECTED_SUMMARY_SHA256,
    EXPECTED_SUMMARY_STATUS,
    PINNED_DRAT_TRIM_COMMIT,
    SUMMARY_SCHEMA,
    _expected_candidate_identity,
    _load_frozen_summary,
    _read_strict_json,
    audit_core_proofs,
    main,
    protected_replay_inputs,
    replay_drat,
    validate_summary,
)


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _gzip_bytes(data: bytes) -> bytes:
    buffer = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=buffer, mtime=0) as sink:
        sink.write(data)
    return buffer.getvalue()


def _write_executable(path: Path, body: str) -> None:
    path.write_text("#!/bin/sh\n" + body, encoding="ascii")
    path.chmod(0o755)


def _record(
    label: str,
    edges: tuple[tuple[int, int], ...],
    cnf_asset: str,
    proof_asset: str,
    cnf_gzip: bytes,
    proof_gzip: bytes,
    cnf_raw: bytes,
) -> dict:
    variables, _ = lexicographic_edge_variables(PRODUCTION_ORDER)
    units, candidate = _expected_candidate_identity(edges, variables)
    return {
        "label": label,
        "deletion_edges": [list(edge) for edge in edges],
        "assumption_units": list(units),
        "candidate_sha256": candidate,
        "cnf_asset": cnf_asset,
        "cnf_gzip_bytes": len(cnf_gzip),
        "cnf_gzip_sha256": _sha256(cnf_gzip),
        "cnf_uncompressed_sha256": _sha256(cnf_raw),
        "proof_asset": proof_asset,
        "proof_gzip_bytes": len(proof_gzip),
        "proof_gzip_sha256": _sha256(proof_gzip),
        "independent_cnf_audit_sha256": "a" * 64,
        "proof_verified": True,
    }


def _summary(records: list[dict]) -> dict:
    semantic_checker = Path(__file__).with_name(
        "check_r3_18_budget7_branch1_core_cnf.py"
    )
    return {
        "schema": SUMMARY_SCHEMA,
        "status": EXPECTED_SUMMARY_STATUS,
        "claim_boundary": "local branch only",
        "minimality_claim": False,
        "global_ramsey_implication": None,
        "common_formula": {
            "formula_fingerprint_sha256": EXPECTED_FORMULA_FINGERPRINT,
            "maximum_variable": PRODUCTION_MAXIMUM_VARIABLE,
            "clauses_before_candidate_units": PRODUCTION_COMMON_CLAUSES,
            "original_nonedge_variables_in_deletion_counter": 0,
        },
        "external_toolchains": {
            "drat_trim": {
                "source_commit": PINNED_DRAT_TRIM_COMMIT,
                "binary_sha256": "b" * 64,
            },
            "independent_arm64_drat_trim": {
                "source_commit": PINNED_DRAT_TRIM_COMMIT,
                "binary_sha256": "c" * 64,
            },
        },
        "independent_cnf_checker": {
            "script": "routes/finite/check_r3_18_budget7_branch1_core_cnf.py",
            "script_sha256": hashlib.sha256(semantic_checker.read_bytes()).hexdigest(),
            "pysat_imported": False,
            "production_formula_builder_imported": False,
        },
        "records": records,
    }


def _semantic_result(record: dict) -> dict:
    return {
        "status": CNF_AUDIT_STATUS,
        "candidate": {
            "label": record["label"],
            "deletion_edges": record["deletion_edges"],
            "assumption_units": record["assumption_units"],
            "candidate_sha256": record["candidate_sha256"],
        },
        "cnf": {
            "basename": record["cnf_asset"],
            "bytes": record["cnf_gzip_bytes"],
            "sha256": record["cnf_gzip_sha256"],
            "uncompressed_sha256": record["cnf_uncompressed_sha256"],
        },
    }


class CoreProofReplayTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.assets = self.root / "assets"
        self.assets.mkdir()
        self.cnf_raw_a = b"p cnf 1 1\n1 0\n"
        self.cnf_raw_b = b"p cnf 2 1\n-2 0\n"
        self.proof_raw_a = b"1 0\n0\n"
        self.proof_raw_b = b"-2 0\n0\n"
        self.cnf_a = _gzip_bytes(self.cnf_raw_a)
        self.cnf_b = _gzip_bytes(self.cnf_raw_b)
        self.proof_a = _gzip_bytes(self.proof_raw_a)
        self.proof_b = _gzip_bytes(self.proof_raw_b)
        self.record_a = _record(
            "A",
            ((11, 62), (18, 61)),
            "branch1_core_A.cnf.gz",
            "branch1_core_A.drat.gz",
            self.cnf_a,
            self.proof_a,
            self.cnf_raw_a,
        )
        self.record_b = _record(
            "B",
            ((18, 64), (18, 69)),
            "branch1_core_B.cnf.gz",
            "branch1_core_B.drat.gz",
            self.cnf_b,
            self.proof_b,
            self.cnf_raw_b,
        )
        for name, data in (
            ("branch1_core_A.cnf.gz", self.cnf_a),
            ("branch1_core_A.drat.gz", self.proof_a),
            ("branch1_core_B.cnf.gz", self.cnf_b),
            ("branch1_core_B.drat.gz", self.proof_b),
        ):
            (self.assets / name).write_bytes(data)
        self.summary_path = self.assets / "summary.json"
        self.summary = _summary([self.record_a, self.record_b])
        self.summary_path.write_text(json.dumps(self.summary), encoding="utf-8")
        self.matrix = self.root / "matrix.txt"
        self.bank = self.root / "bank.json"
        self.matrix.write_text("unused", encoding="ascii")
        self.bank.write_text("{}", encoding="ascii")
        self.checker = self.root / "drat-trim"
        _write_executable(self.checker, "printf 's VERIFIED\\n'\n")
        (self.root / "SOURCE_COMMIT").write_text(
            PINNED_DRAT_TRIM_COMMIT + "\n", encoding="ascii"
        )
        self.summary["external_toolchains"]["drat_trim"]["binary_sha256"] = _sha256(
            self.checker.read_bytes()
        )
        self.summary_path.write_text(json.dumps(self.summary), encoding="utf-8")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _semantic_side_effect(self, **kwargs):
        by_label = {record["label"]: record for record in self.summary["records"]}
        return _semantic_result(by_label[kwargs["label"]])

    def _audit(self):
        with mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.audit_production_cnf",
            side_effect=self._semantic_side_effect,
        ) as semantic, mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.EXPECTED_SUMMARY_SHA256",
            _sha256(self.summary_path.read_bytes()),
        ):
            result = audit_core_proofs(
                summary_path=self.summary_path,
                artifact_dir=self.assets,
                matrix_path=self.matrix,
                bank_path=self.bank,
                drat_trim=self.checker,
                timeout_seconds=5,
            )
        return result, semantic

    def test_generic_record_family_is_semantically_audited_and_freshly_replayed(self) -> None:
        result, semantic = self._audit()
        self.assertEqual(result["status"], "ALL_FINAL_BRANCH1_CORE_PROOFS_REPLAYED")
        self.assertEqual(result["records_verified"], 2)
        self.assertEqual(result["assets_verified"], 4)
        self.assertEqual(semantic.call_count, 2)
        self.assertTrue(
            all(record["drat_replay"]["status"] == "VERIFIED" for record in result["records"])
        )
        self.assertIsNone(result["global_ramsey_implication"])

    def test_tracked_production_summary_is_the_exact_frozen_singleton_family(self) -> None:
        tracked = Path(__file__).with_name(
            "r3_18_budget7_branch1_core_proof_summary.json"
        )
        payload, digest = _load_frozen_summary(tracked, EXPECTED_SUMMARY_SHA256)
        records = validate_summary(payload)
        self.assertEqual(digest, EXPECTED_SUMMARY_SHA256)
        self.assertEqual(payload["status"], EXPECTED_SUMMARY_STATUS)
        self.assertEqual(
            [
                (
                    record.label,
                    record.edges,
                    record.assumption_units,
                    record.cnf_asset,
                    record.proof_asset,
                )
                for record in records
            ],
            [
                (
                    "K_a",
                    ((11, 62),),
                    (-1085,),
                    "branch1_core_K_a_size1.cnf.gz",
                    "branch1_core_K_a_size1.drat.gz",
                ),
                (
                    "K_b",
                    ((18, 61),),
                    (-1672,),
                    "branch1_core_K_b_size1.cnf.gz",
                    "branch1_core_K_b_size1.drat.gz",
                ),
                (
                    "K_c",
                    ((18, 64),),
                    (-1675,),
                    "branch1_core_K_c_size1.cnf.gz",
                    "branch1_core_K_c_size1.drat.gz",
                ),
                (
                    "K_d",
                    ((18, 69),),
                    (-1680,),
                    "branch1_core_K_d_size1.cnf.gz",
                    "branch1_core_K_d_size1.drat.gz",
                ),
            ],
        )

    def test_duplicate_label_and_duplicate_asset_are_rejected(self) -> None:
        for name, mutation, pattern in (
            (
                "label",
                lambda value: value["records"][1].__setitem__("label", "A"),
                "duplicate record label",
            ),
            (
                "asset",
                lambda value: value["records"][1].__setitem__(
                    "cnf_asset", value["records"][0]["cnf_asset"]
                ),
                "duplicate asset basename",
            ),
        ):
            with self.subTest(name=name):
                broken = copy.deepcopy(self.summary)
                mutation(broken)
                with self.assertRaisesRegex(AuditError, pattern):
                    validate_summary(broken)

    def test_noncanonical_edge_and_unit_are_rejected(self) -> None:
        for name, mutation, pattern in (
            (
                "edge",
                lambda value: value["records"][0].__setitem__(
                    "deletion_edges", [[62, 11], [18, 61]]
                ),
                "noncanonical edge",
            ),
            (
                "unit",
                lambda value: value["records"][0].__setitem__(
                    "assumption_units", [1085, -1672]
                ),
                "noncanonical deletion units",
            ),
        ):
            with self.subTest(name=name):
                broken = copy.deepcopy(self.summary)
                mutation(broken)
                with self.assertRaisesRegex(AuditError, pattern):
                    validate_summary(broken)

    def test_claim_bits_fail_closed_at_summary_and_record_levels(self) -> None:
        mutations = (
            (
                "summary-minimality",
                lambda value: value.__setitem__("minimality_claim", True),
                "claims minimality",
            ),
            (
                "summary-global",
                lambda value: value.__setitem__("global_ramsey_implication", True),
                "global implication",
            ),
            (
                "record-proof",
                lambda value: value["records"][0].__setitem__("proof_verified", 1),
                "proof bit",
            ),
            (
                "record-minimality",
                lambda value: value["records"][0].__setitem__("minimality_claim", True),
                "claims minimality",
            ),
            (
                "record-global",
                lambda value: value["records"][0].__setitem__(
                    "global_ramsey_implication", "R(3,18)>=101"
                ),
                "global implication",
            ),
        )
        for name, mutation, pattern in mutations:
            with self.subTest(name=name):
                broken = copy.deepcopy(self.summary)
                mutation(broken)
                with self.assertRaisesRegex(AuditError, pattern):
                    validate_summary(broken)

    def test_final_records_must_form_an_antichain(self) -> None:
        broken = copy.deepcopy(self.summary)
        superset = _record(
            "superset",
            ((11, 62), (18, 61), (18, 64)),
            "branch1_core_superset.cnf.gz",
            "branch1_core_superset.drat.gz",
            _gzip_bytes(b"different cnf"),
            _gzip_bytes(b"different proof"),
            b"different cnf",
        )
        broken["records"].append(superset)
        with self.assertRaisesRegex(AuditError, "not an antichain"):
            validate_summary(broken)

    def test_asset_swap_is_rejected_before_semantic_audit(self) -> None:
        self.summary["records"][0]["cnf_asset"] = "branch1_core_B.cnf.gz"
        self.summary["records"][1]["cnf_asset"] = "branch1_core_A.cnf.gz"
        self.summary_path.write_text(json.dumps(self.summary), encoding="utf-8")
        with mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.audit_production_cnf"
        ) as semantic, mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.EXPECTED_SUMMARY_SHA256",
            _sha256(self.summary_path.read_bytes()),
        ):
            with self.assertRaisesRegex(AuditError, "asset (?:byte count|SHA-256) mismatch"):
                audit_core_proofs(
                    summary_path=self.summary_path,
                    artifact_dir=self.assets,
                    matrix_path=self.matrix,
                    bank_path=self.bank,
                    drat_trim=self.checker,
                    timeout_seconds=5,
                )
        semantic.assert_not_called()

    def test_missing_and_bad_gzip_assets_fail_closed(self) -> None:
        missing = self.assets / self.record_a["proof_asset"]
        missing.unlink()
        with mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.audit_production_cnf",
            side_effect=self._semantic_side_effect,
        ), mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.EXPECTED_SUMMARY_SHA256",
            _sha256(self.summary_path.read_bytes()),
        ):
            with self.assertRaisesRegex(AuditError, "missing DRAT asset"):
                audit_core_proofs(
                    summary_path=self.summary_path,
                    artifact_dir=self.assets,
                    matrix_path=self.matrix,
                    bank_path=self.bank,
                    drat_trim=self.checker,
                    timeout_seconds=5,
                )
        bad = b"not gzip"
        missing.write_bytes(bad)
        self.summary["records"][0]["proof_gzip_bytes"] = len(bad)
        self.summary["records"][0]["proof_gzip_sha256"] = _sha256(bad)
        self.summary_path.write_text(json.dumps(self.summary), encoding="utf-8")
        with mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.audit_production_cnf",
            side_effect=self._semantic_side_effect,
        ), mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.EXPECTED_SUMMARY_SHA256",
            _sha256(self.summary_path.read_bytes()),
        ):
            with self.assertRaisesRegex(AuditError, "invalid or incomplete gzip"):
                audit_core_proofs(
                    summary_path=self.summary_path,
                    artifact_dir=self.assets,
                    matrix_path=self.matrix,
                    bank_path=self.bank,
                    drat_trim=self.checker,
                    timeout_seconds=5,
                )

    def test_undeclared_stale_core_asset_is_rejected(self) -> None:
        stale = self.assets / "branch1_core_stale_size1.cnf.gz"
        stale.write_bytes(_gzip_bytes(b"stale"))
        with mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.EXPECTED_SUMMARY_SHA256",
            _sha256(self.summary_path.read_bytes()),
        ):
            with self.assertRaisesRegex(AuditError, "undeclared branch1-core assets"):
                audit_core_proofs(
                    summary_path=self.summary_path,
                    artifact_dir=self.assets,
                    matrix_path=self.matrix,
                    bank_path=self.bank,
                    drat_trim=self.checker,
                    timeout_seconds=5,
                )

    def test_resolved_asset_alias_is_rejected(self) -> None:
        alias = self.assets / "branch1_core_B.drat.gz"
        alias.unlink()
        alias.symlink_to("branch1_core_A.drat.gz")
        self.summary_path.write_text(json.dumps(self.summary), encoding="utf-8")
        with mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.EXPECTED_SUMMARY_SHA256",
            _sha256(self.summary_path.read_bytes()),
        ):
            with self.assertRaisesRegex(AuditError, "resolve to the same"):
                audit_core_proofs(
                    summary_path=self.summary_path,
                    artifact_dir=self.assets,
                    matrix_path=self.matrix,
                    bank_path=self.bank,
                    drat_trim=self.checker,
                    timeout_seconds=5,
                )

    def test_checker_requires_exit_zero_and_one_exact_stdout_line(self) -> None:
        cnf = self.root / "tiny.cnf"
        proof = self.root / "tiny.drat"
        cnf.write_text("p cnf 1 1\n1 0\n", encoding="ascii")
        proof.write_text("0\n", encoding="ascii")
        cases = (
            ("wrong-line", "printf 's VERIFIED-ish\\n'\n", "exactly one"),
            ("spaces", "printf ' s VERIFIED \\n'\n", "exactly one"),
            ("duplicate", "printf 's VERIFIED\\ns VERIFIED\\n'\n", "exactly one"),
            ("stderr", "printf 's VERIFIED\\n' >&2\n", "exactly one"),
            ("nonzero", "printf 's VERIFIED\\n'\nexit 1\n", "exited nonzero"),
        )
        for name, body, pattern in cases:
            with self.subTest(name=name):
                checker = self.root / f"checker-{name}"
                _write_executable(checker, body)
                with self.assertRaisesRegex(AuditError, pattern):
                    replay_drat(checker, cnf, proof, 5)

    def test_checker_timeout_is_not_promoted(self) -> None:
        with mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.subprocess.run",
            side_effect=subprocess.TimeoutExpired(["drat-trim"], 1),
        ):
            with self.assertRaisesRegex(AuditError, "timed out"):
                replay_drat(self.checker, self.matrix, self.bank, 1)

    def test_loader_injection_environment_is_removed_from_checker_process(self) -> None:
        completed = subprocess.CompletedProcess(
            [str(self.checker)], 0, stdout="s VERIFIED\n", stderr=""
        )
        injected = {
            "LD_PRELOAD": "/tmp/evil.so",
            "LD_LIBRARY_PATH": "/tmp/evil",
            "LD_AUDIT": "/tmp/audit.so",
            "DYLD_INSERT_LIBRARIES": "/tmp/evil.dylib",
            "DYLD_LIBRARY_PATH": "/tmp/evil",
            "LDR_PRELOAD": "/tmp/evil.a",
            "GCONV_PATH": "/tmp/gconv",
            "LIBPATH": "/tmp/evil",
            "SHLIB_PATH": "/tmp/evil",
            "RAMSEY_HARMLESS_TEST": "kept",
        }
        with mock.patch.dict(os.environ, injected, clear=False), mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.subprocess.run",
            return_value=completed,
        ) as run:
            replay_drat(self.checker, self.matrix, self.bank, 1)
        environment = run.call_args.kwargs["env"]
        for key in injected:
            if key != "RAMSEY_HARMLESS_TEST":
                self.assertNotIn(key, environment)
        self.assertEqual(environment["RAMSEY_HARMLESS_TEST"], "kept")
        self.assertEqual(environment["LC_ALL"], "C")
        self.assertEqual(environment["LANG"], "C")

    def test_summary_hash_and_parser_use_one_in_memory_read(self) -> None:
        raw = json.dumps(self.summary).encode("utf-8")

        class CountingSummary:
            def __init__(self, data: bytes) -> None:
                self.data = data
                self.reads = 0

            def is_file(self) -> bool:
                return True

            def read_bytes(self) -> bytes:
                self.reads += 1
                if self.reads > 1:
                    raise AssertionError("summary was reopened")
                return self.data

            def __str__(self) -> str:
                return "counting-summary.json"

        source = CountingSummary(raw)
        payload, digest = _load_frozen_summary(source, _sha256(raw))  # type: ignore[arg-type]
        self.assertEqual(source.reads, 1)
        self.assertEqual(payload["schema"], SUMMARY_SCHEMA)
        self.assertEqual(digest, _sha256(raw))

    def test_authenticated_private_snapshots_survive_source_path_mutation(self) -> None:
        def mutate_sources_after_staging(**kwargs):
            record = next(
                record
                for record in self.summary["records"]
                if record["label"] == kwargs["label"]
            )
            self.assertNotEqual(kwargs["cnf_path"].parent, self.assets)
            if kwargs["label"] == "A":
                (self.assets / self.record_a["cnf_asset"]).write_bytes(b"mutated")
                (self.assets / self.record_a["proof_asset"]).write_bytes(b"mutated")
                _write_executable(self.checker, "exit 1\n")
            return _semantic_result(record)

        with mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.audit_production_cnf",
            side_effect=mutate_sources_after_staging,
        ), mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.EXPECTED_SUMMARY_SHA256",
            _sha256(self.summary_path.read_bytes()),
        ):
            result = audit_core_proofs(
                summary_path=self.summary_path,
                artifact_dir=self.assets,
                matrix_path=self.matrix,
                bank_path=self.bank,
                drat_trim=self.checker,
                timeout_seconds=5,
            )
        self.assertEqual(result["records_verified"], 2)

    def test_runtime_checker_requires_the_adjacent_pinned_source_marker(self) -> None:
        marker = self.root / "SOURCE_COMMIT"
        for name, replacement, pattern in (
            ("missing", None, "lacks an adjacent"),
            ("wrong", "0" * 40 + "\n", "SOURCE_COMMIT mismatch"),
        ):
            with self.subTest(name=name):
                if replacement is None:
                    marker.unlink(missing_ok=True)
                else:
                    marker.write_text(replacement, encoding="ascii")
                with mock.patch(
                    "routes.finite.check_r3_18_budget7_branch1_core_proofs.EXPECTED_SUMMARY_SHA256",
                    _sha256(self.summary_path.read_bytes()),
                ):
                    with self.assertRaisesRegex(AuditError, pattern):
                        audit_core_proofs(
                            summary_path=self.summary_path,
                            artifact_dir=self.assets,
                            matrix_path=self.matrix,
                            bank_path=self.bank,
                            drat_trim=self.checker,
                            timeout_seconds=5,
                        )
                marker.write_text(PINNED_DRAT_TRIM_COMMIT + "\n", encoding="ascii")
        fake = self.root / "fake-drat-trim"
        _write_executable(fake, "printf 's VERIFIED\\n'\n# different binary\n")
        with mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.EXPECTED_SUMMARY_SHA256",
            _sha256(self.summary_path.read_bytes()),
        ):
            with self.assertRaisesRegex(AuditError, "outside the frozen allowlist"):
                audit_core_proofs(
                    summary_path=self.summary_path,
                    artifact_dir=self.assets,
                    matrix_path=self.matrix,
                    bank_path=self.bank,
                    drat_trim=fake,
                    timeout_seconds=5,
                )

    def test_frozen_summary_digest_rejects_record_deletion_and_reordering(self) -> None:
        frozen_digest = _sha256(self.summary_path.read_bytes())
        mutations = (
            lambda value: value["records"].pop(),
            lambda value: value["records"].reverse(),
        )
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                broken = copy.deepcopy(self.summary)
                mutation(broken)
                self.summary_path.write_text(json.dumps(broken), encoding="utf-8")
                with mock.patch(
                    "routes.finite.check_r3_18_budget7_branch1_core_proofs.EXPECTED_SUMMARY_SHA256",
                    frozen_digest,
                ):
                    with self.assertRaisesRegex(AuditError, "frozen value"):
                        audit_core_proofs(
                            summary_path=self.summary_path,
                            artifact_dir=self.assets,
                            matrix_path=self.matrix,
                            bank_path=self.bank,
                            drat_trim=self.checker,
                            timeout_seconds=5,
                        )
        self.summary_path.write_text(json.dumps(self.summary), encoding="utf-8")

    def test_json_output_cannot_overwrite_any_authenticated_input(self) -> None:
        protected = (
            self.summary_path,
            self.matrix,
            self.bank,
            self.checker,
            self.root / "SOURCE_COMMIT",
            self.assets / self.record_a["cnf_asset"],
            self.assets / self.record_a["proof_asset"],
        )
        before = {path: path.read_bytes() for path in protected}
        for target in protected:
            with self.subTest(target=target.name):
                stdout = io.StringIO()
                stderr = io.StringIO()
                with redirect_stdout(stdout), redirect_stderr(stderr), mock.patch(
                    "routes.finite.check_r3_18_budget7_branch1_core_proofs.EXPECTED_SUMMARY_SHA256",
                    _sha256(self.summary_path.read_bytes()),
                ):
                    code = main(
                        [
                            "--artifact-dir",
                            str(self.assets),
                            "--summary",
                            str(self.summary_path),
                            "--matrix",
                            str(self.matrix),
                            "--universal-bank",
                            str(self.bank),
                            "--drat-trim",
                            str(self.checker),
                            "--json-output",
                            str(target),
                            "--overwrite",
                        ]
                    )
                self.assertEqual(code, 1)
                self.assertEqual(stdout.getvalue(), "")
                self.assertIn("collides", stderr.getvalue())
                self.assertEqual(target.read_bytes(), before[target])

    def test_output_preflight_protects_transitive_semantic_sources(self) -> None:
        with mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.EXPECTED_SUMMARY_SHA256",
            _sha256(self.summary_path.read_bytes()),
        ):
            protected = protected_replay_inputs(
                summary_path=self.summary_path,
                artifact_dir=self.assets,
                matrix_path=self.matrix,
                bank_path=self.bank,
                drat_trim=self.checker,
            )
        finite = Path(__file__).resolve().parent
        for name in (
            "check_r3_18_budget7_branch1_core_proofs.py",
            "check_r3_18_budget7_branch1_core_cnf.py",
            "independent_seqcounter.py",
        ):
            self.assertIn((finite / name).resolve(), protected)

        semantic_source = finite / "check_r3_18_budget7_branch1_core_cnf.py"
        source_before = semantic_source.read_bytes()
        output_alias = self.root / "semantic-source-alias.json"
        output_alias.symlink_to(semantic_source)
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr), mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.EXPECTED_SUMMARY_SHA256",
            _sha256(self.summary_path.read_bytes()),
        ):
            code = main(
                [
                    "--artifact-dir",
                    str(self.assets),
                    "--summary",
                    str(self.summary_path),
                    "--matrix",
                    str(self.matrix),
                    "--universal-bank",
                    str(self.bank),
                    "--drat-trim",
                    str(self.checker),
                    "--json-output",
                    str(output_alias),
                    "--overwrite",
                ]
            )
        self.assertEqual(code, 1)
        self.assertIn("collides", stderr.getvalue())
        self.assertTrue(output_alias.is_symlink())
        self.assertEqual(semantic_source.read_bytes(), source_before)

    def test_output_parent_symlink_swap_cannot_redirect_authenticated_write(self) -> None:
        output_parent = self.root / "output-parent"
        output_parent.mkdir()
        relocated_parent = self.root / "opened-output-parent"
        output = output_parent / self.summary_path.name
        summary_before = self.summary_path.read_bytes()
        synthetic_success = {
            "schema": "synthetic-test-result",
            "status": "ALL_FINAL_BRANCH1_CORE_PROOFS_REPLAYED",
        }

        def swap_parent_after_preflight(**kwargs):
            output_parent.rename(relocated_parent)
            output_parent.symlink_to(self.assets, target_is_directory=True)
            return synthetic_success

        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr), mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.EXPECTED_SUMMARY_SHA256",
            _sha256(self.summary_path.read_bytes()),
        ), mock.patch(
            "routes.finite.check_r3_18_budget7_branch1_core_proofs.audit_core_proofs",
            side_effect=swap_parent_after_preflight,
        ):
            code = main(
                [
                    "--artifact-dir",
                    str(self.assets),
                    "--summary",
                    str(self.summary_path),
                    "--matrix",
                    str(self.matrix),
                    "--universal-bank",
                    str(self.bank),
                    "--drat-trim",
                    str(self.checker),
                    "--json-output",
                    str(output),
                    "--overwrite",
                ]
            )

        self.assertEqual(code, 0, stderr.getvalue())
        self.assertEqual(self.summary_path.read_bytes(), summary_before)
        self.assertTrue(output_parent.is_symlink())
        self.assertEqual(
            json.loads((relocated_parent / self.summary_path.name).read_text()),
            synthetic_success,
        )
        self.assertEqual(json.loads(stdout.getvalue()), synthetic_success)

    def test_finite_heavy_invokes_core_replay_and_cannot_print_success_after_failure(self) -> None:
        commands: list[list[str]] = []

        def collect(command, **kwargs):
            commands.append(command)

        with redirect_stdout(io.StringIO()), mock.patch.object(
            reproduce, "check_assets", return_value={}
        ), mock.patch.object(reproduce, "build_finite_overlay"), mock.patch.object(
            reproduce, "run", side_effect=collect
        ):
            reproduce.finite_heavy(self.assets, self.checker)
        core_commands = [
            command
            for command in commands
            if any("check_r3_18_budget7_branch1_core_proofs.py" in part for part in command)
        ]
        self.assertEqual(len(core_commands), 1)
        self.assertIn("--drat-trim", core_commands[0])

        def fail_on_core(command, **kwargs):
            if any("check_r3_18_budget7_branch1_core_proofs.py" in part for part in command):
                raise subprocess.CalledProcessError(1, command)

        stdout = io.StringIO()
        with redirect_stdout(stdout), mock.patch.object(
            reproduce, "check_assets", return_value={}
        ), mock.patch.object(reproduce, "build_finite_overlay"), mock.patch.object(
            reproduce, "run", side_effect=fail_on_core
        ):
            with self.assertRaises(subprocess.CalledProcessError):
                reproduce.finite_heavy(self.assets, self.checker)
        self.assertNotIn("FINITE_HEAVY_REPRODUCTION_PASS", stdout.getvalue())

    def test_strict_json_rejects_duplicate_keys(self) -> None:
        path = self.root / "duplicate.json"
        path.write_text('{"schema":"one","schema":"two"}', encoding="ascii")
        with self.assertRaisesRegex(AuditError, "duplicate JSON key"):
            _read_strict_json(path)

    def test_cli_failure_never_prints_a_success_payload(self) -> None:
        broken = copy.deepcopy(self.summary)
        broken["records"][0]["proof_verified"] = False
        self.summary_path.write_text(json.dumps(broken), encoding="utf-8")
        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            with mock.patch(
                "routes.finite.check_r3_18_budget7_branch1_core_proofs.EXPECTED_SUMMARY_SHA256",
                _sha256(self.summary_path.read_bytes()),
            ):
                code = main(
                    [
                        "--artifact-dir",
                        str(self.assets),
                        "--summary",
                        str(self.summary_path),
                        "--matrix",
                        str(self.matrix),
                        "--universal-bank",
                        str(self.bank),
                        "--drat-trim",
                        str(self.checker),
                    ]
                )
        self.assertEqual(code, 1)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("FAILED_BRANCH1_CORE_PROOF_REPLAY", stderr.getvalue())
        self.assertNotIn("ALL_FINAL_BRANCH1_CORE_PROOFS_REPLAYED", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
