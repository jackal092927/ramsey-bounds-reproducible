#!/usr/bin/env python3
"""Tests for the fail-closed branch-1 maximal-union gate."""

from __future__ import annotations

import gzip
import hashlib
import json
import os
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest import mock

from routes.finite import check_r3_18_budget7_branch1_maximal_union_gate as checker
from routes.finite import r3_18_budget7_branch1_maximal_union_gate as gate


HERE = Path(__file__).resolve().parent


class MaximalUnionGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.production = {
            "seed_path": HERE / "certificates" / "r3_18_n100_nearmiss.txt",
            "budget6_path": HERE / "r3_18_budget6_summary.json",
            "singleton_summary_path": (
                HERE / "r3_18_budget7_branch1_core_proof_summary.json"
            ),
            "universal_path": (
                HERE / "r3_18_budget6_branch_0_universal_union.cuts.json"
            ),
            "history_path": (
                HERE / "r3_18_budget7_branch1_cegar_history_exclusion.json"
            ),
            "aplus_path": HERE / "r3_18_budget7_branch1_cegar_Aplus_batch.json",
        }
        cls.design, cls.appended = gate.build_design(**cls.production)

    def test_production_design_exact_counts_and_boundaries(self) -> None:
        self.assertEqual(self.design["status"], gate.STATUS_DESIGN)
        self.assertEqual(self.design["formula"]["final_variables"], 639_290)
        self.assertEqual(self.design["formula"]["final_clauses"], 1_972_360)
        self.assertEqual(len(self.appended), 278_754)
        self.assertEqual(
            gate.ordered_masks_sha256(self.appended),
            gate.EXPECTED_APPEND_ORDERED_SHA256,
        )
        self.assertFalse(self.design["claim_boundary"]["branch1_closed"])
        self.assertFalse(
            self.design["claim_boundary"]["other_triangle_edge_branches_closed"]
        )
        self.assertTrue(
            self.design["branch_scope"]["no_transfer_to_other_triangle_edge_branches"]
        )
        self.assertIn("A+ appended only", self.design["non_repetition"]["versus_Aplus"])
        self.assertIn(
            "deletion-support master",
            self.design["non_repetition"]["versus_Benders_all_fixed_base_cuts"],
        )
        basis = dict(self.design)
        recorded = basis.pop("record_sha256")
        self.assertEqual(gate.canonical_sha256(basis), recorded)

    def test_independent_union_rebuild_matches_generator(self) -> None:
        rebuilt = checker.rebuild_appended_masks(
            seed=self.production["seed_path"],
            universal=self.production["universal_path"],
            history=self.production["history_path"],
            aplus=self.production["aplus_path"],
        )
        self.assertEqual(rebuilt, self.appended)

    def test_full_selector_numbering_and_two_implementations(self) -> None:
        variables, pairs = gate.edge_variables()
        clauses = gate.iter_selector_clauses(variables, pairs)
        first = next(clauses)
        self.assertEqual(first[0], 1)
        self.assertEqual(first[1], gate.COMMON_VARIABLES + 1)
        self.assertEqual(first[-1], gate.COMMON_VARIABLES + 98)
        self.assertEqual(gate.selector_variable(4_949, 97), gate.FINAL_VARIABLES)

        generator_hash = hashlib.sha256()
        generator_count = 0
        for clause in gate.iter_selector_clauses(variables, pairs):
            generator_hash.update(
                (" ".join(map(str, clause)) + " 0\n").encode("ascii")
            )
            generator_count += 1
        checker_hash = hashlib.sha256()
        checker_count = 0
        for line in checker._selector_lines(variables, pairs):
            checker_hash.update(line)
            checker_count += 1
        self.assertEqual(generator_count, gate.SELECTOR_CLAUSES)
        self.assertEqual(checker_count, gate.SELECTOR_CLAUSES)
        self.assertEqual(generator_hash.hexdigest(), checker_hash.hexdigest())

    def test_atomic_emitter_byte_cap_leaves_no_output(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            output = Path(name) / "gate.cnf"
            emitter = gate._AtomicDimacs(output, 3)
            with self.assertRaises(gate.GateError):
                emitter.write(b"abcd")
            emitter.abort()
            self.assertFalse(output.exists())
            self.assertFalse(emitter.temporary.exists())

    def test_design_refuses_symlinked_authenticated_input(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            link = Path(name) / "seed.txt"
            link.symlink_to(self.production["seed_path"])
            modified = dict(self.production)
            modified["seed_path"] = link
            with self.assertRaisesRegex(gate.GateError, "non-symlink"):
                gate.build_design(**modified)

    def test_generator_cli_does_not_resolve_symlink_before_validation(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            link = Path(name) / "seed.txt"
            link.symlink_to(self.production["seed_path"])
            output = Path(name) / "design.json"
            with self.assertRaisesRegex(gate.GateError, "non-symlink"):
                gate.main(
                    [
                        "design",
                        "--seed",
                        str(link),
                        "--output-record",
                        str(output),
                    ]
                )
            self.assertFalse(output.exists())

    def test_checker_cli_preserves_lexical_symlink_path(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            target = Path(name) / "target.cnf"
            target.write_text("p cnf 0 0\n", encoding="ascii")
            link = Path(name) / "linked.cnf"
            link.symlink_to(target)
            captured = {}

            def fake_audit_cnf(**kwargs):
                captured.update(kwargs)
                return {"status": "TEST_ONLY"}

            with mock.patch.object(checker, "audit_cnf", side_effect=fake_audit_cnf):
                with redirect_stdout(StringIO()):
                    checker.main(
                        [
                            "cnf",
                            "--cnf",
                            str(link),
                            "--record",
                            str(HERE / "r3_18_budget7_branch1_maximal_union_gate_production.json"),
                            "--common-cnf",
                            str(link),
                        ]
                    )
            self.assertTrue(captured["cnf"].is_symlink())

    def test_model_parser_requires_complete_unique_assignment(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            valid = Path(name) / "valid.model.gz"
            valid.write_bytes(gzip.compress(b"s SATISFIABLE\nv 1 -2 3 0\n", mtime=0))
            assignment, info = checker.parse_complete_model(valid, 3)
            self.assertEqual(assignment[1:], [True, False, True])
            self.assertEqual(info["assignment_literals"], 3)

            duplicate = Path(name) / "duplicate.model.gz"
            duplicate.write_bytes(
                gzip.compress(b"s SATISFIABLE\nv 1 -1 2 3 0\n", mtime=0)
            )
            with self.assertRaises(checker.AuditError):
                checker.parse_complete_model(duplicate, 3)

            missing = Path(name) / "missing.model.gz"
            missing.write_bytes(gzip.compress(b"s SATISFIABLE\nv 1 -2 0\n", mtime=0))
            with self.assertRaises(checker.AuditError):
                checker.parse_complete_model(missing, 3)

    def test_clause_evaluator_accepts_only_satisfying_complete_model(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            cnf = Path(name) / "toy.cnf"
            cnf.write_bytes(b"p cnf 3 2\n1 -2 0\n2 3 0\n")
            good = [None, True, False, True]
            result = checker.evaluate_model(cnf, good, maximum_variable=3, clauses=2)
            self.assertTrue(result["all_clauses_satisfied"])
            bad = [None, False, True, False]
            with self.assertRaisesRegex(checker.AuditError, "falsifies"):
                checker.evaluate_model(cnf, bad, maximum_variable=3, clauses=2)

    def test_unpinned_proof_checker_is_rejected_before_execution(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            binary = Path(name) / "drat-trim"
            binary.write_text("#!/bin/sh\necho 's VERIFIED'\n", encoding="ascii")
            binary.chmod(0o700)
            (Path(name) / "SOURCE_COMMIT").write_text(
                gate.PINNED_DRAT_TRIM_COMMIT + "\n", encoding="ascii"
            )
            destination = Path(name) / "staged"
            with self.assertRaisesRegex(checker.AuditError, "allowlist"):
                checker._stage_executable(binary, destination)
            self.assertFalse(destination.exists())

    def test_status_never_learns_on_design_or_unknown(self) -> None:
        self.assertEqual(self.design["limits"]["learned_masks"], [])
        self.assertFalse(self.design["limits"]["solver_invoked"])
        self.assertIn("learns nothing", self.design["state_machine"]["UNKNOWN"])
        self.assertFalse(
            self.design["claim_boundary"]["UNKNOWN_learns_any_cut"]
        )


if __name__ == "__main__":
    unittest.main()
