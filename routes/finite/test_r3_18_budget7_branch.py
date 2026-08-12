"""Primitive semantic tests for the exact-seven R(3,18) branch runner."""

from __future__ import annotations

import json
import math
import tempfile
import unittest
from pathlib import Path

from pysat.solvers import Solver

from .bounded_deletion_sat_cegar import build_variables
from .check_r3_18_budget7 import validate_directory
from .new_basin_search import edge_present
from .r3_18_budget7_branch import (
    BRANCH_EDGES,
    RESIDUAL_DELETIONS,
    TOTAL_DELETIONS,
    load_incremental_masks,
    parse_mask,
    structural_formula,
    validate_budget6_dependency,
    validate_masks,
)
from .verify_ramsey import read_matrix


HERE = Path(__file__).resolve().parent
SEED = HERE / "certificates" / "r3_18_n100_nearmiss.txt"


class Budget7Tests(unittest.TestCase):
    def test_budget_constants(self) -> None:
        self.assertEqual(TOTAL_DELETIONS, 7)
        self.assertEqual(RESIDUAL_DELETIONS, 6)
        self.assertEqual(BRANCH_EDGES, ((97, 98), (97, 99), (98, 99)))

    def test_hex_and_decimal_mask_parsing(self) -> None:
        mask = sum(1 << v for v in range(18))
        self.assertEqual(parse_mask(f"{mask:025x}"), mask)
        self.assertEqual(parse_mask(str(mask)), mask)
        self.assertEqual(validate_masks([mask, f"{mask:025x}"]), [mask])

    def test_incremental_checkpoint_deduplication(self) -> None:
        a = sum(1 << v for v in range(18))
        b = sum(1 << v for v in range(1, 19))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "checkpoint.json"
            path.write_text(json.dumps({"last_checkpoint": {"new_masks": [a, b, a]}}))
            self.assertEqual(load_incremental_masks([path]), [a, b])

    def test_budget6_dependency_is_exact_three_branch_proof_package(self) -> None:
        payload = json.loads((HERE / "r3_18_budget6_summary.json").read_text())
        validate_budget6_dependency(payload)
        damaged = json.loads(json.dumps(payload))
        damaged["branches"][1]["proof"]["checker_status"] = "UNKNOWN"
        with self.assertRaisesRegex(ValueError, "checker status"):
            validate_budget6_dependency(damaged)

    def test_frozen_first_round_endpoints(self) -> None:
        checked = validate_directory(HERE)
        self.assertEqual(checked["status"], "FIRST_ROUND_STATE_VERIFIED")
        self.assertTrue(checked["all_three_branches_unknown"])
        self.assertIsNone(checked["global_ramsey_implication"])

    def test_exact_six_residual_counter_semantics(self) -> None:
        rows = read_matrix(SEED)
        variables, pairs = build_variables(len(rows))
        original = {edge for edge in pairs if edge_present(rows, *edge)}
        fixed = BRANCH_EDGES[0]
        clauses, _, metadata = structural_formula(
            len(rows), variables, pairs, original, fixed
        )
        self.assertEqual(metadata["exact_six_residual_counter_literals"], 826)
        residual = sorted(original - {fixed})
        nonedges = sorted(set(pairs) - original)
        triangle_clause_count = math.comb(len(rows), 3)
        counter_clause_count = metadata["exact_six_residual_counter_clauses"]
        counter = clauses[
            triangle_clause_count : triangle_clause_count + counter_clause_count
        ]
        counter_input_variables = {
            abs(literal)
            for clause in counter
            for literal in clause
            if abs(literal) <= len(pairs)
        }
        self.assertEqual(
            counter_input_variables,
            {variables[edge] for edge in residual},
        )
        self.assertTrue(
            {variables[edge] for edge in nonedges}.isdisjoint(counter_input_variables)
        )

        # With every nonedge left for the solver to choose, the structural
        # formula is extendible exactly at six residual deletions.
        for count, expected in ((5, False), (6, True), (7, False)):
            assumptions = [-variables[fixed]]
            deleted = set(residual[:count])
            assumptions.extend(
                -variables[e] if e in deleted else variables[e]
                for e in residual
            )
            with Solver(name="cadical195", bootstrap_with=clauses) as solver:
                self.assertEqual(solver.solve(assumptions=assumptions), expected)

        # "Not counted" does not mean an original nonedge can always be set
        # positive: triangle clauses still constrain additions.  Exhibit one
        # nonedge whose addition closes a triangle under the six-deletion
        # assignment and check that it is correctly rejected.
        deleted = set(residual[:6]) | {fixed}
        retained = original - deleted
        conflict = next(
            edge
            for edge in nonedges
            if any(
                tuple(sorted((edge[0], w))) in retained
                and tuple(sorted((edge[1], w))) in retained
                for w in range(len(rows))
                if w not in edge
            )
        )
        assumptions = [
            -variables[edge] if edge in deleted else variables[edge]
            for edge in original
        ]
        assumptions.append(variables[conflict])
        with Solver(name="cadical195", bootstrap_with=clauses) as solver:
            self.assertFalse(solver.solve(assumptions=assumptions))


if __name__ == "__main__":
    unittest.main()
