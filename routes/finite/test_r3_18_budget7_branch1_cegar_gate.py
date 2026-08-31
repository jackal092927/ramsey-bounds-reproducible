"""Small, asset-free regressions for the bounded branch-1 CEGAR gate."""

from __future__ import annotations

import gzip
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from .check_r3_18_budget7_branch1_core_cnf import AuditError
from .r3_18_budget7_branch1_cegar_gate import (
    FIXED_BRANCH1_BASE_MASKS,
    AUGMENTED_PROOF_REPLAY_SCHEMA,
    FROZEN_AUGMENTED_CNF_BYTES,
    FROZEN_AUGMENTED_CNF_CLAUSES,
    FROZEN_AUGMENTED_CNF_SHA256,
    FROZEN_CANONICAL_REPRODUCER_FILE_SHA256,
    FROZEN_CORE_REPLAY_SCHEMA,
    FROZEN_CORE_REPLAY_STATUS,
    FROZEN_HISTORY_EXCLUSION_FILE_SHA256,
    FROZEN_MASK_BATCH_FILE_SHA256,
    FROZEN_MASK_BATCH_ORDERED_SHA256,
    FROZEN_SINGLETON_SUMMARY_SHA256,
    FROZEN_STANDALONE_GENERATOR_FILE_SHA256,
    HISTORY_EXCLUSION_MASKS,
    HISTORY_EXCLUSION_ORDERED_SHA256,
    HISTORY_EXCLUSION_SCHEMA,
    HISTORICAL_EXPLORATION_RUNNER_SHA256,
    HISTORICAL_EXPLORATION_RUNNER_SNAPSHOT,
    MASK_BATCH_SCHEMA,
    PINNED_CADICAL_COMMIT,
    PRODUCTION_BANK_MASKS,
    PROVED_POSITIVE_UNITS,
    STATUS_SAT_ESCALATE,
    STATUS_UNSAT_UNCHECKED,
    STATUS_UNKNOWN_ERROR,
    STATUS_UNKNOWN_UNSAT,
    STATUS_UNKNOWN_WALL,
    StableOutputDirectory,
    _sha256_file,
    build_endpoint_record,
    checked_independent_witness,
    classify_raw_solver_result,
    deterministic_gzip_file,
    emit_augmented_cnf,
    evaluate_dimacs_model,
    lexicographic_edge_variables,
    load_history_exclusion,
    load_and_validate_mask_batch,
    ordered_masks_sha256,
    parse_sat_stdout,
    pending_unsat_promotion_record,
    run_pinned_cadical,
    validate_generation_provenance,
    validate_pinned_cadical,
    validate_positive_units,
    validate_unsat_promotion_evidence,
)


def _gzip_bytes(raw: bytes) -> bytes:
    import io

    output = io.BytesIO()
    with gzip.GzipFile(filename="", mode="wb", fileobj=output, mtime=0) as zipped:
        zipped.write(raw)
    return output.getvalue()


class Branch1CegarGateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="ramsey-cegar-gate-test-")
        self.root = Path(self.temporary.name)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _mask_file(self, name: str, masks: list[str]) -> Path:
        path = self.root / name
        path.write_text(json.dumps({"masks": masks}), encoding="utf-8")
        return path

    def _executable(self, name: str, body: str) -> Path:
        directory = self.root / name
        directory.mkdir()
        executable = directory / "cadical"
        executable.write_text("#!/bin/sh\n" + body, encoding="ascii")
        executable.chmod(0o755)
        (directory / "SOURCE_COMMIT").write_text(
            PINNED_CADICAL_COMMIT + "\n", encoding="ascii"
        )
        return executable

    def test_mask_batch_is_canonical_new_and_independent_in_model(self) -> None:
        variables, _ = lexicographic_edge_variables(5)
        assignment: list[bool | None] = [None] + [False] * len(variables)
        path = self._mask_file("masks.json", ["07", "0b"])
        masks, info = load_and_validate_mask_batch(
            path,
            assignment=assignment,
            variables=variables,
            installed_masks=set(),
            order=5,
            set_size=3,
            expected_count=2,
        )
        self.assertEqual(masks, [0x07, 0x0B])
        self.assertEqual(info["ordered_masks_sha256"], ordered_masks_sha256(masks, 2))
        self.assertTrue(info["all_new_relative_to_three_frozen_exclusion_families"])
        self.assertTrue(info["all_independent_in_frozen_model"])

    def test_mask_batch_rejects_count_format_order_duplicates_and_old_masks(self) -> None:
        variables, _ = lexicographic_edge_variables(5)
        assignment: list[bool | None] = [None] + [False] * len(variables)
        cases = (
            ("count", ["07"], set(), "exactly 2"),
            ("uppercase", ["07", "0B"], set(), "canonical"),
            ("order", ["0b", "07"], set(), "strictly increasing"),
            ("duplicate", ["07", "07"], set(), "strictly increasing"),
            ("installed", ["07", "0b"], {0x0B}, "frozen exclusion"),
            ("wrong-size", ["03", "0b"], set(), "not an 3-set"),
        )
        for name, encoded, installed, pattern in cases:
            with self.subTest(name=name):
                path = self._mask_file(f"{name}.json", encoded)
                with self.assertRaisesRegex(AuditError, pattern):
                    load_and_validate_mask_batch(
                        path,
                        assignment=assignment,
                        variables=variables,
                        installed_masks=installed,
                        order=5,
                        set_size=3,
                        expected_count=2,
                    )

    def test_mask_batch_rejects_nonindependence_and_duplicate_json_keys(self) -> None:
        variables, _ = lexicographic_edge_variables(5)
        assignment: list[bool | None] = [None] + [False] * len(variables)
        assignment[variables[(0, 1)]] = True
        with self.assertRaisesRegex(AuditError, "not independent"):
            load_and_validate_mask_batch(
                self._mask_file("adjacent.json", ["07", "0b"]),
                assignment=assignment,
                variables=variables,
                installed_masks=set(),
                order=5,
                set_size=3,
                expected_count=2,
            )

        duplicate = self.root / "duplicate-key.json"
        duplicate.write_text('{"masks":["07"],"masks":["0b"]}', encoding="ascii")
        with self.assertRaisesRegex(AuditError, "duplicate key"):
            load_and_validate_mask_batch(
                duplicate,
                assignment=[None] + [False] * len(variables),
                variables=variables,
                installed_masks=set(),
                order=5,
                set_size=3,
                expected_count=1,
            )

    def test_history_exclusion_has_a_strict_source_ledger_and_frozen_union(self) -> None:
        masks = [0x07, 0x0B]
        digest = ordered_masks_sha256(masks, 2)
        payload = {
            "schema": HISTORY_EXCLUSION_SCHEMA,
            "masks": ["07", "0b"],
            "masks_count": 2,
            "ordered_masks_sha256": digest,
            "sources": [
                {
                    "path": "run/a.json",
                    "file_sha256": "a" * 64,
                    "field": "strict_state.additional_conditional_masks_hex",
                    "raw_count": 1,
                },
                {
                    "path": "run/b.json",
                    "file_sha256": "b" * 64,
                    "field": "strict_state.additional_conditional_masks_hex",
                    "raw_count": 2,
                },
            ],
            "source_raw_count_sum": 3,
            "within_source_duplicates": 0,
            "union_duplicates_removed": 1,
        }
        path = self.root / "history.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        frozen_file_sha256 = _sha256_file(path)
        loaded, info = load_history_exclusion(
            path,
            order=5,
            set_size=3,
            expected_count=2,
            expected_ordered_sha256=digest,
            expected_sources=2,
            expected_raw_masks=3,
            expected_file_sha256=frozen_file_sha256,
        )
        self.assertEqual(loaded, masks)
        self.assertEqual(info["source_checkpoints"], 2)

        broken = dict(payload)
        broken["ordered_masks_sha256"] = "0" * 64
        path.write_text(json.dumps(broken), encoding="utf-8")
        with self.assertRaisesRegex(AuditError, "recorded ordered digest"):
            load_history_exclusion(
                path,
                order=5,
                set_size=3,
                expected_count=2,
                expected_ordered_sha256=digest,
                expected_sources=2,
                expected_raw_masks=3,
                expected_file_sha256=_sha256_file(path),
            )

    def test_final_batch_requires_reverse_first_frozen_exclusion_provenance(self) -> None:
        variables, _ = lexicographic_edge_variables(5)
        assignment: list[bool | None] = [None] + [False] * len(variables)
        bare = self._mask_file("bare.json", ["07", "0b"])
        with self.assertRaisesRegex(AuditError, "frozen-exclusion provenance"):
            load_and_validate_mask_batch(
                bare,
                assignment=assignment,
                variables=variables,
                installed_masks=set(),
                order=5,
                set_size=3,
                expected_count=2,
                require_frozen_exclusion_provenance=True,
                expected_file_sha256=_sha256_file(bare),
                expected_ordered_sha256=ordered_masks_sha256([0x07, 0x0B], 2),
            )

        base_digest = "1" * 64
        history_digest = "2" * 64
        masks = [0x07, 0x0B]
        final_payload = {
            "schema": MASK_BATCH_SCHEMA,
            "masks": ["07", "0b"],
            "masks_count": 2,
            "ordered_masks_sha256": ordered_masks_sha256(masks, 2),
            "enumeration": "reverse-first",
            "exclusions": {
                "base_universal_bank": {
                    "masks": PRODUCTION_BANK_MASKS,
                    "ordered_masks_sha256": base_digest,
                },
                "historical_union": {
                    "masks": HISTORY_EXCLUSION_MASKS,
                    "ordered_masks_sha256": history_digest,
                },
                "fixed_branch1_base_family": {
                    "masks": FIXED_BRANCH1_BASE_MASKS,
                    "ordered_masks_sha256": "3" * 64,
                },
            },
        }
        final = self.root / "final.json"
        final.write_text(json.dumps(final_payload), encoding="utf-8")
        final_file_sha256 = _sha256_file(final)
        loaded, info = load_and_validate_mask_batch(
            final,
            assignment=assignment,
            variables=variables,
            installed_masks=set(),
            order=5,
            set_size=3,
            expected_count=2,
            require_frozen_exclusion_provenance=True,
            expected_base_ordered_sha256=base_digest,
            expected_history_ordered_sha256=history_digest,
            fixed_base_rows=[0b00010, 0b00001, 0, 0, 0],
            expected_fixed_base_ordered_sha256="3" * 64,
            expected_file_sha256=final_file_sha256,
            expected_ordered_sha256=final_payload["ordered_masks_sha256"],
        )
        self.assertEqual(loaded, masks)
        self.assertEqual(info["ordered_masks_sha256"], final_payload["ordered_masks_sha256"])
        with self.assertRaisesRegex(AuditError, "fixed-base I18 family"):
            load_and_validate_mask_batch(
                final,
                assignment=assignment,
                variables=variables,
                installed_masks=set(),
                order=5,
                set_size=3,
                expected_count=2,
                require_frozen_exclusion_provenance=True,
                expected_base_ordered_sha256=base_digest,
                expected_history_ordered_sha256=history_digest,
                fixed_base_rows=[0, 0, 0, 0, 0],
                expected_fixed_base_ordered_sha256="3" * 64,
                expected_file_sha256=final_file_sha256,
                expected_ordered_sha256=final_payload["ordered_masks_sha256"],
            )

    def test_Aplus_file_and_ordered_hashes_are_frozen(self) -> None:
        for value in (
            FROZEN_HISTORY_EXCLUSION_FILE_SHA256,
            FROZEN_MASK_BATCH_FILE_SHA256,
            FROZEN_MASK_BATCH_ORDERED_SHA256,
        ):
            self.assertRegex(value, r"\A[0-9a-f]{64}\Z")
        self.assertEqual(
            FROZEN_HISTORY_EXCLUSION_FILE_SHA256,
            "d5100bb5dce48da3ca8ab3810290ff553ebb9d6c87ff9df1f287700563f456b0",
        )
        self.assertEqual(
            FROZEN_MASK_BATCH_FILE_SHA256,
            "835137c2df19bc851618761cc0af92400b3fa2677dd00c47101d1074c7406e8b",
        )
        self.assertEqual(
            FROZEN_MASK_BATCH_ORDERED_SHA256,
            "a3cff8d8a4c77c6effb49c03e76065a17f754d0a7de727d229652276b6e8cda0",
        )
        snapshot = Path(__file__).resolve().with_name(
            HISTORICAL_EXPLORATION_RUNNER_SNAPSHOT
        )
        self.assertEqual(
            _sha256_file(snapshot), HISTORICAL_EXPLORATION_RUNNER_SHA256
        )

    def test_tracked_reproducer_is_normative_and_binds_original_snapshot(self) -> None:
        here = Path(__file__).resolve().parent
        record = validate_generation_provenance(
            here / "r3_18_budget7_branch1_cegar_Aplus_provenance.json",
            here / "generate_r3_18_budget7_branch1_cegar_Aplus.py",
        )
        self.assertEqual(
            record["canonical_reproducer"]["sha256"],
            FROZEN_CANONICAL_REPRODUCER_FILE_SHA256,
        )
        self.assertTrue(record["canonical_reproducer"]["normative"])
        self.assertEqual(
            record["original_standalone_snapshot"]["sha256"],
            FROZEN_STANDALONE_GENERATOR_FILE_SHA256,
        )
        self.assertFalse(record["original_standalone_snapshot"]["normative"])

    def test_history_digest_constant_uses_actual_lf_not_literal_backslash_n(self) -> None:
        canonical = hashlib.sha256(b"0000000000000000000000007\n").hexdigest()
        escaped = hashlib.sha256(b"0000000000000000000000007\\n").hexdigest()
        self.assertEqual(ordered_masks_sha256([7], 25), canonical)
        self.assertNotEqual(canonical, escaped)
        self.assertEqual(
            HISTORY_EXCLUSION_ORDERED_SHA256,
            "74b4b99c18e925a7a1bbb0e4a1636dad4bf8741ba67623c2164f3607a65172a8",
        )

    def test_four_positive_units_are_exact_and_true(self) -> None:
        variables, _ = lexicographic_edge_variables(100)
        assignment: list[bool | None] = [None] + [False] * len(variables)
        for unit in PROVED_POSITIVE_UNITS:
            assignment[unit] = True
        self.assertEqual(
            validate_positive_units(
                PROVED_POSITIVE_UNITS,
                assignment=assignment,
                variables=variables,
            ),
            PROVED_POSITIVE_UNITS,
        )
        with self.assertRaisesRegex(AuditError, "differ"):
            validate_positive_units(
                tuple(reversed(PROVED_POSITIVE_UNITS)),
                assignment=assignment,
                variables=variables,
            )
        assignment[PROVED_POSITIVE_UNITS[0]] = False
        with self.assertRaisesRegex(AuditError, "false"):
            validate_positive_units(
                PROVED_POSITIVE_UNITS,
                assignment=assignment,
                variables=variables,
            )

    def test_augmented_cnf_emission_is_byte_deterministic_and_ordered(self) -> None:
        raw = b"p cnf 3 2\n1 -2 0\n3 0\n"
        common = self.root / "common.cnf.gz"
        common.write_bytes(_gzip_bytes(raw))
        variables, _ = lexicographic_edge_variables(3)
        first = self.root / "first.cnf"
        second = self.root / "second.cnf"
        info = emit_augmented_cnf(
            common,
            first,
            variables_count=3,
            common_clause_count=2,
            positive_units=[1],
            masks=[0b111],
            edge_variables=variables,
            order=3,
        )
        again = emit_augmented_cnf(
            common,
            second,
            variables_count=3,
            common_clause_count=2,
            positive_units=[1],
            masks=[0b111],
            edge_variables=variables,
            order=3,
        )
        expected = b"p cnf 3 4\n1 -2 0\n3 0\n1 0\n1 2 3 0\n"
        self.assertEqual(first.read_bytes(), expected)
        self.assertEqual(second.read_bytes(), expected)
        self.assertEqual(info["sha256"], again["sha256"])
        self.assertEqual(info["sha256"], hashlib.sha256(expected).hexdigest())
        self.assertEqual(info["clauses"], 4)

    def test_augmented_cnf_rejects_changed_common_header_or_body_count(self) -> None:
        for name, raw, pattern in (
            ("header", b"p cnf 3 3\n1 0\n", "header changed"),
            ("body", b"p cnf 3 2\n1 0\n", "body line count"),
        ):
            with self.subTest(name=name):
                common = self.root / f"{name}.cnf.gz"
                common.write_bytes(_gzip_bytes(raw))
                variables, _ = lexicographic_edge_variables(3)
                output = self.root / f"{name}.cnf"
                with self.assertRaisesRegex(AuditError, pattern):
                    emit_augmented_cnf(
                        common,
                        output,
                        variables_count=3,
                        common_clause_count=2,
                        positive_units=[1],
                        masks=[],
                        edge_variables=variables,
                        order=3,
                    )
                self.assertFalse(output.exists())

    def test_stable_output_directory_survives_parent_symlink_swap(self) -> None:
        parent = self.root / "parent"
        parent.mkdir()
        stable = StableOutputDirectory.create(parent / "out")
        moved_parent = self.root / "moved-parent"
        attacker = self.root / "attacker"
        attacker.mkdir()
        parent.rename(moved_parent)
        parent.symlink_to(attacker, target_is_directory=True)
        source = self.root / "source.bin"
        source.write_bytes(b"authenticated bytes\n")
        try:
            installed = stable.install_file(
                source,
                "artifact.bin",
                expected_bytes=source.stat().st_size,
                expected_sha256=_sha256_file(source),
            )
            stable.write_json("record.json", {"status": "VERIFIED"})
        finally:
            stable.close()
        self.assertEqual(
            (moved_parent / "out" / "artifact.bin").read_bytes(),
            b"authenticated bytes\n",
        )
        self.assertEqual(installed["sha256"], hashlib.sha256(b"authenticated bytes\n").hexdigest())
        self.assertFalse((attacker / "out").exists())

    def test_model_evaluator_binds_the_exact_cnf_sha256(self) -> None:
        cnf = self.root / "tiny-hash.cnf"
        cnf.write_bytes(b"p cnf 1 1\n1 0\n")
        assignment = [None, True]
        expected = _sha256_file(cnf)
        verified = evaluate_dimacs_model(
            cnf,
            assignment,
            expected_variables=1,
            expected_clauses=1,
            expected_sha256=expected,
        )
        self.assertEqual(verified["cnf_sha256_evaluated"], expected)
        with self.assertRaisesRegex(AuditError, "SHA-256 changed"):
            evaluate_dimacs_model(
                cnf,
                assignment,
                expected_variables=1,
                expected_clauses=1,
                expected_sha256="0" * 64,
            )

    def test_sat_transcript_requires_a_complete_unique_model(self) -> None:
        assignment, canonical = parse_sat_stdout(
            b"c fake CaDiCaL\ns SATISFIABLE\nv 1 -2\nv 3 0\n", 3
        )
        self.assertEqual(assignment, [None, True, False, True])
        self.assertEqual(canonical, b"s SATISFIABLE\nv 1 -2 3 0\n")
        for name, transcript, pattern in (
            ("missing", b"s SATISFIABLE\nv 1 -2 0\n", "does not assign"),
            ("duplicate", b"s SATISFIABLE\nv 1 -1 2 3 0\n", "more than once"),
            ("wrong-status", b"s SAT\nv 1 2 3 0\n", "status line"),
            ("zero", b"s SATISFIABLE\nv 1 0 2 3\n", "final zero"),
        ):
            with self.subTest(name=name), self.assertRaisesRegex(AuditError, pattern):
                parse_sat_stdout(transcript, 3)

    def test_new_model_is_evaluated_and_witness_is_checked_new(self) -> None:
        variables, _ = lexicographic_edge_variables(4)
        assignment: list[bool | None] = [None] + [False] * len(variables)
        assignment[variables[(0, 1)]] = True
        cnf = self.root / "tiny.cnf"
        cnf.write_text("p cnf 6 1\n1 0\n", encoding="ascii")
        evaluation = evaluate_dimacs_model(
            cnf, assignment, expected_variables=6, expected_clauses=1
        )
        self.assertEqual(evaluation["clauses_evaluated"], 1)
        witness = checked_independent_witness(
            assignment,
            variables=variables,
            order=4,
            target=3,
            universal_bank_masks=set(),
            historical_masks=set(),
            new_gate_masks=set(),
        )
        self.assertTrue(witness["independent_set_exists"])
        self.assertFalse(witness["installed_or_learned_by_this_gate"])
        known = checked_independent_witness(
            assignment,
            variables=variables,
            order=4,
            target=3,
            universal_bank_masks=set(),
            historical_masks=set(),
            new_gate_masks=set(),
            fixed_base_rows=[0, 0, 0, 0],
        )
        self.assertTrue(known["known_from_exhaustive_fixed_base_family"])
        self.assertFalse(known["new_relative_to_three_frozen_exclusion_families"])
        witness_mask = int(witness["mask_hex"], 16)
        historical = checked_independent_witness(
            assignment,
            variables=variables,
            order=4,
            target=3,
            universal_bank_masks=set(),
            historical_masks={witness_mask},
            new_gate_masks=set(),
        )
        self.assertTrue(historical["known_from_historical_learned_union"])
        self.assertFalse(
            historical["new_relative_to_three_frozen_exclusion_families"]
        )
        self.assertTrue(
            historical["overlap_with_exclusion_families"][
                "historical_learned_union"
            ]
        )
        self.assertFalse(historical["installed_or_learned_by_this_gate"])

        with self.assertRaisesRegex(AuditError, "installed"):
            checked_independent_witness(
                assignment,
                variables=variables,
                order=4,
                target=3,
                universal_bank_masks=set(),
                historical_masks=set(),
                new_gate_masks={witness_mask},
            )

        assignment[variables[(0, 1)]] = False
        with self.assertRaisesRegex(AuditError, "falsifies"):
            evaluate_dimacs_model(
                cnf, assignment, expected_variables=6, expected_clauses=1
            )

    def test_fake_binary_with_correct_marker_is_not_pinned(self) -> None:
        fake = self._executable("fake-unpinned", "exit 0\n")
        with self.assertRaisesRegex(AuditError, "SHA-256 mismatch"):
            validate_pinned_cadical(fake, self.root / "staged-cadical")

    def test_hard_wall_kills_checker_group_and_learns_nothing(self) -> None:
        slow = self._executable("slow", "sleep 5\n")
        cnf = self.root / "input.cnf"
        cnf.write_text("p cnf 1 0\n", encoding="ascii")
        proof = self.root / "timeout.drat"
        digest = _sha256_file(slow)
        with mock.patch(
            "routes.finite.r3_18_budget7_branch1_cegar_gate.PINNED_CADICAL_SHA256",
            digest,
        ):
            result = run_pinned_cadical(slow, cnf, proof, 0.05)
        self.assertEqual(result["status"], STATUS_UNKNOWN_WALL)
        self.assertEqual(result["learned_masks"], [])
        self.assertFalse(proof.exists())
        self.assertLess(result["elapsed_seconds"], 2.0)

    def test_unsat_exit_is_only_pending_until_a_proof_is_checked(self) -> None:
        unsat = self._executable(
            "unsat",
            "printf '0\\n' > \"$4\"\nprintf 's UNSATISFIABLE\\n'\nexit 20\n",
        )
        cnf = self.root / "input.cnf"
        cnf.write_text("p cnf 1 1\n1 0\n", encoding="ascii")
        raw_proof = self.root / "proof.drat"
        with mock.patch(
            "routes.finite.r3_18_budget7_branch1_cegar_gate.PINNED_CADICAL_SHA256",
            _sha256_file(unsat),
        ):
            raw = run_pinned_cadical(unsat, cnf, raw_proof, 2.0)
        classified = classify_raw_solver_result(raw, raw_proof)
        self.assertEqual(classified["status"], "UNSAT_PROOF_PENDING_COMPRESSION")
        self.assertEqual(classified["learned_masks"], [])
        compressed = self.root / "proof.drat.gz"
        info = deterministic_gzip_file(raw_proof, compressed)
        self.assertEqual(info["uncompressed_sha256"], hashlib.sha256(b"0\n").hexdigest())
        self.assertNotIn("proof_verified", classified)

    def test_unsat_promotion_requires_both_fresh_replay_chains(self) -> None:
        pending = pending_unsat_promotion_record()
        self.assertFalse(pending["scoped_unsat_claim_accepted"])
        self.assertEqual(
            pending["required_singleton_core_replay"]["exact_labels"],
            ["K_a", "K_b", "K_c", "K_d"],
        )
        proof_sha256 = "a" * 64
        gate = {
            "solver": {
                "status": STATUS_UNSAT_UNCHECKED,
                "proof": {"sha256": proof_sha256},
            },
            "augmentation": {
                "augmented_cnf": {
                    "sha256": FROZEN_AUGMENTED_CNF_SHA256,
                    "bytes": FROZEN_AUGMENTED_CNF_BYTES,
                    "clauses": FROZEN_AUGMENTED_CNF_CLAUSES,
                }
            },
        }
        core = {
            "schema": FROZEN_CORE_REPLAY_SCHEMA,
            "status": FROZEN_CORE_REPLAY_STATUS,
            "records_verified": 4,
            "assets_verified": 8,
            "summary": {"sha256": FROZEN_SINGLETON_SUMMARY_SHA256},
            "checker": {
                "source_commit": (
                    "2e3b2dc0ecf938addbd779d42877b6ed69d9a985"
                ),
                "sha256": (
                    "b535cc5334e97fba5b5db6013625c5a0b16ce348a98d59ff91b45a83fa56b39e"
                ),
            },
            "records": [
                {
                    "label": label,
                    "semantic_reconstruction": (
                        "VERIFIED_INDEPENDENT_CNF_RECONSTRUCTION"
                    ),
                    "drat_replay": {"status": "VERIFIED", "exitcode": 0},
                }
                for label in ("K_a", "K_b", "K_c", "K_d")
            ],
        }
        augmented = {
            "schema": AUGMENTED_PROOF_REPLAY_SCHEMA,
            "status": "AUGMENTED_CNF_PROOF_REPLAYED",
            "proof_verified": True,
            "augmented_cnf": {
                "sha256": FROZEN_AUGMENTED_CNF_SHA256,
                "bytes": FROZEN_AUGMENTED_CNF_BYTES,
            },
            "proof": {"gzip_sha256": proof_sha256},
            "checker": {
                "source_commit": (
                    "2e3b2dc0ecf938addbd779d42877b6ed69d9a985"
                ),
                "sha256": (
                    "b535cc5334e97fba5b5db6013625c5a0b16ce348a98d59ff91b45a83fa56b39e"
                ),
                "exitcode": 0,
                "verified_lines": ["s VERIFIED"],
            },
        }
        promoted = validate_unsat_promotion_evidence(gate, core, augmented)
        self.assertTrue(promoted["scoped_unsat_claim_accepted"])
        broken_core = dict(core)
        broken_core["records"] = core["records"][:-1]
        with self.assertRaisesRegex(AuditError, "singleton replay"):
            validate_unsat_promotion_evidence(gate, broken_core, augmented)
        broken_augmented = dict(augmented)
        broken_augmented["proof_verified"] = False
        with self.assertRaisesRegex(AuditError, "augmented-proof"):
            validate_unsat_promotion_evidence(gate, core, broken_augmented)

    def test_endpoint_records_preserve_sat_lower_bound_and_unknown_boundaries(self) -> None:
        cnf = {
            "sha256": FROZEN_AUGMENTED_CNF_SHA256,
            "bytes": FROZEN_AUGMENTED_CNF_BYTES,
            "clauses": FROZEN_AUGMENTED_CNF_CLAUSES,
        }
        sat = {
            "status": STATUS_SAT_ESCALATE,
            "model": {"sha256": "a" * 64, "bytes": 123},
            "model_evaluation": {
                "all_clauses_satisfied": True,
                "cnf_sha256_evaluated": FROZEN_AUGMENTED_CNF_SHA256,
            },
            "I18_search": {"independent_set_exists": False},
            "learned_masks": [],
        }
        sat_record = build_endpoint_record(sat, cnf)
        implication = sat_record["candidate_target_implication"]
        self.assertEqual(implication["conditional_result"], "R(3,18) >= 101")
        self.assertTrue(implication["eligible_for_global_lower_bound"])
        self.assertFalse(implication["local_branch_closure_only"])
        self.assertIn("branch1_cegar_sat.model.gz", sat_record["files_to_freeze"])

        unknown = {
            "status": STATUS_UNKNOWN_WALL,
            "checker": {"sha256": "b" * 64},
            "learned_masks": [],
        }
        unknown_record = build_endpoint_record(unknown, cnf)
        self.assertIn("Authenticated endpoint only", unknown_record["unknown_claim_boundary"])
        with self.assertRaisesRegex(AuditError, "checker record"):
            build_endpoint_record(
                {"status": STATUS_UNKNOWN_WALL, "learned_masks": []}, cnf
            )

    def test_exit_twenty_without_proof_and_status_mismatch_are_unknown(self) -> None:
        proof = self.root / "absent.drat"
        no_proof = {
            "status": "RAW_SOLVER_RESULT",
            "exitcode": 20,
            "_stdout": b"s UNSATISFIABLE\n",
            "learned_masks": [],
        }
        self.assertEqual(
            classify_raw_solver_result(no_proof, proof)["status"],
            STATUS_UNKNOWN_UNSAT,
        )
        mismatch = {
            "status": "RAW_SOLVER_RESULT",
            "exitcode": 10,
            "_stdout": b"s UNSATISFIABLE\n",
            "learned_masks": [],
        }
        self.assertEqual(
            classify_raw_solver_result(mismatch, proof)["status"],
            STATUS_UNKNOWN_ERROR,
        )


if __name__ == "__main__":
    unittest.main()
