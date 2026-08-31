"""Regression tests for the branch-1 deletion-covering projection."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from .check_r3_18_budget7_branch1_deletion_projection import (
    AuditError,
    EXPECTED_EXACT6_CNF_SHA256,
    EXPECTED_FIXED_COUNT,
    EXPECTED_FIXED_SHA256,
    audit,
    independent_formula,
    read_seed as checker_read_seed,
    reconstruction,
)
from .r3_18_budget7_branch1_deletion_projection import (
    FORCED_RETAINED_EDGES,
    ProjectionError,
    build_projection,
    eligibility_requirements,
    fixed_base_i18_family,
    formula_record,
    iter_named_clauses,
    solve_projection,
    strict_seed,
    validate_deletion_witness,
)


HERE = Path(__file__).resolve().parent
SEED = HERE / "certificates" / "r3_18_n100_nearmiss.txt"
LEDGER = HERE / "r3_18_budget7_branch1_deletion_projection.json"


class DeletionProjectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.seed_rows, _ = strict_seed(SEED)
        cls.exact6 = build_projection(cls.seed_rows, "exact-six")
        cls.exact7 = build_projection(cls.seed_rows, "exact-seven")
        cls.checked = audit(SEED, LEDGER)
        cls.ledger = json.loads(LEDGER.read_text(encoding="utf-8"))

    def test_fixed_base_family_rebuilt_from_65_vertex_i16_problem(self) -> None:
        masks, metadata = fixed_base_i18_family(
            self.seed_rows, self.exact6.base_rows
        )
        self.assertEqual(metadata["candidate_vertices_count"], 65)
        self.assertEqual(metadata["residual_I16_count"], EXPECTED_FIXED_COUNT)
        self.assertEqual(metadata["lifted_I18_count"], EXPECTED_FIXED_COUNT)
        self.assertEqual(
            metadata["lifted_I18_ordered_sha256"], EXPECTED_FIXED_SHA256
        )
        self.assertEqual(tuple(masks), self.exact6.fixed_masks)

    def test_independent_formula_hash_matches_generator_and_remote_cnf(self) -> None:
        generated = formula_record(self.exact6)
        self.assertEqual(
            generated, self.ledger["formula_reconstruction"]["exact_six"]
        )
        self.assertEqual(
            self.checked["exact_six_complete_dimacs_sha256"],
            EXPECTED_EXACT6_CNF_SHA256,
        )
        self.assertEqual(
            self.checked["exact_six_complete_dimacs_sha256"],
            self.ledger["exact_six_strength_gate"]["cnf"]["sha256"],
        )

    def test_exact_seven_profile_adds_only_counter_change_and_four_units(self) -> None:
        record = self.ledger["formula_reconstruction"]["exact_seven"]
        self.assertTrue(record["singleton_exclusions_installed"])
        self.assertEqual(
            record["clause_count_by_family"]["singleton_deletion_exclusion"], 4
        )
        units = []
        for name, clause in iter_named_clauses(self.exact7):
            if name == "singleton_deletion_exclusion":
                units.append(clause)
            elif name == "local_addition_eligibility":
                break
        self.assertEqual(
            units,
            [[-self.exact7.dvars[edge]] for edge in FORCED_RETAINED_EDGES],
        )

    def test_local_eligibility_clause_is_exact_common_neighbor_wedge(self) -> None:
        edge = next(
            edge
            for edge in self.exact6.additions
            if len(eligibility_requirements(self.exact6, edge)) == 1
        )
        first, second = eligibility_requirements(self.exact6, edge)[0]
        target = [
            -self.exact6.gvars[edge],
            self.exact6.dvars[first],
            self.exact6.dvars[second],
        ]
        self.assertIn(
            ("local_addition_eligibility", target),
            iter_named_clauses(self.exact6),
        )

    def test_invalid_small_deletion_witness_is_rejected(self) -> None:
        with self.assertRaisesRegex(ProjectionError, "exact residual"):
            validate_deletion_witness(self.exact6, self.exact6.base_edges[:4])
        forced = set(FORCED_RETAINED_EDGES)
        incident_98 = next(
            edge
            for edge in self.exact7.base_edges
            if 98 in edge and edge not in forced
        )
        filler = [
            edge
            for edge in self.exact7.base_edges
            if edge not in forced and edge != incident_98
        ]
        support = [FORCED_RETAINED_EDGES[0], incident_98, *filler[:4]]
        with self.assertRaisesRegex(ProjectionError, "singleton"):
            validate_deletion_witness(self.exact7, support)

    def test_pysat_cadical_backend_is_rejected_before_an_unbounded_call(self) -> None:
        with self.assertRaisesRegex(ProjectionError, "external process"):
            solve_projection(self.exact6, "cadical195", 1.0)
        with self.assertRaisesRegex(ProjectionError, "\(0,300\]"):
            solve_projection(self.exact6, "glucose42", 301.0)

    def test_unknown_endpoint_and_stop_rule_are_not_promoted(self) -> None:
        endpoint = self.ledger["exact_six_strength_gate"]
        self.assertEqual(endpoint["solver_status"], "UNKNOWN_HARD_WALL_LIMIT")
        self.assertEqual(endpoint["status_lines"], [])
        self.assertFalse(endpoint["partial_proof"]["used_as_evidence"])
        self.assertTrue(endpoint["partial_proof"]["deleted_after_hashing"])
        self.assertFalse(endpoint["exact_seven_was_run"])
        self.assertEqual(
            self.ledger["exact_seven_call_decision"]["recommendation"],
            "DO_NOT_RUN",
        )

    def test_seed_mutation_and_symlink_fail_closed(self) -> None:
        with tempfile.TemporaryDirectory(prefix="ramsey-deletion-projection-test-") as tmp:
            root = Path(tmp)
            changed = root / "changed.txt"
            changed.write_bytes(SEED.read_bytes() + b"\n")
            with self.assertRaisesRegex(ProjectionError, "SHA-256"):
                strict_seed(changed)
            symlink = root / "link.txt"
            symlink.symlink_to(SEED)
            with self.assertRaisesRegex(AuditError, "non-symlink"):
                checker_read_seed(symlink)

    def test_reverse_checker_is_not_generator_dependent(self) -> None:
        data = reconstruction(checker_read_seed(SEED))
        formula, cnf_hash = independent_formula(data, "exact-six")
        self.assertEqual(
            formula, self.ledger["formula_reconstruction"]["exact_six"]
        )
        self.assertEqual(cnf_hash, EXPECTED_EXACT6_CNF_SHA256)


if __name__ == "__main__":
    unittest.main()
