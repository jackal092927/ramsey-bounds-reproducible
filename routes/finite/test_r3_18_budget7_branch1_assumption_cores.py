"""Soundness regressions for the branch-1 deletion-assumption-core pilot."""

from __future__ import annotations

import unittest
from pathlib import Path
from unittest.mock import Mock

from pysat.solvers import Solver

from .bounded_deletion_sat_cegar import build_variables
from .budget8_next import masks_hash, sha256
from .new_basin_search import edge_present
from .r3_18_budget5_branch import EXPECTED_INPUT_SHA256
from .r3_18_budget7_branch1_assumption_cores import (
    DEGREE_CAP,
    FIXED_EDGE,
    HISTORICAL_TRUSTED_SUPPORTS,
    RESIDUAL_DELETIONS,
    _shareable_path,
    accept_core_only_after_replay,
    build_common_formula,
    deletion_core_to_master_no_good,
    deletion_assumptions,
    encode_final_degree_upper_bounds,
    extract_core_only_after_unsat,
    final_core_after_cross_check,
    first_completed_cores_are_size_six,
    greedy_minimize_replayed_core,
    validate_deletion_support,
    validate_reported_core,
    validate_solver_pair,
)
from .r3_18_budget7_branch import load_universal_bank
from .verify_ramsey import read_matrix


HERE = Path(__file__).resolve().parent
SEED = HERE / "certificates" / "r3_18_n100_nearmiss.txt"


class Budget7Branch1AssumptionCoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.rows = read_matrix(SEED)
        cls.variables, cls.pairs = build_variables(len(cls.rows))
        cls.original_edges = {
            edge for edge in cls.pairs if edge_present(cls.rows, *edge)
        }
        cls.residual_edges = cls.original_edges - {FIXED_EDGE}

    def test_historical_supports_match_recorded_full_D_semantics(self) -> None:
        self.assertEqual(sha256(SEED), EXPECTED_INPUT_SHA256)
        self.assertEqual(len(HISTORICAL_TRUSTED_SUPPORTS), 2)
        self.assertEqual(
            HISTORICAL_TRUSTED_SUPPORTS[0],
            (
                (1, 97),
                (10, 64),
                (11, 62),
                (17, 98),
                (18, 61),
                (18, 64),
            ),
        )
        self.assertEqual(
            HISTORICAL_TRUSTED_SUPPORTS[1][:-1],
            HISTORICAL_TRUSTED_SUPPORTS[0][:-1],
        )
        self.assertEqual(HISTORICAL_TRUSTED_SUPPORTS[1][-1], (18, 69))
        for support in HISTORICAL_TRUSTED_SUPPORTS:
            canonical = validate_deletion_support(support, self.residual_edges)
            self.assertEqual(len(canonical), RESIDUAL_DELETIONS)
            assumptions = deletion_assumptions(canonical, self.variables)
            self.assertEqual(len(assumptions), RESIDUAL_DELETIONS)
            self.assertTrue(all(literal < 0 for literal in assumptions))
            self.assertEqual(
                {-literal for literal in assumptions},
                {self.variables[edge] for edge in canonical},
            )

    def test_fixed_D_validation_rejects_bad_supports(self) -> None:
        valid = list(HISTORICAL_TRUSTED_SUPPORTS[0])
        with self.assertRaisesRegex(ValueError, "exactly six"):
            validate_deletion_support(valid[:-1], self.residual_edges)
        with self.assertRaisesRegex(ValueError, "duplicate"):
            validate_deletion_support(valid[:-1] + [valid[0]], self.residual_edges)
        with self.assertRaisesRegex(ValueError, "non-residual"):
            validate_deletion_support(valid[:-1] + [FIXED_EDGE], self.residual_edges)
        with self.assertRaisesRegex(ValueError, "non-residual"):
            validate_deletion_support(valid[:-1] + [(0, 1)], self.residual_edges)
        with self.assertRaisesRegex(ValueError, "integer JSON numbers"):
            validate_deletion_support(valid[:-1] + [(1.9, 97)], self.residual_edges)
        with self.assertRaisesRegex(ValueError, "integer JSON numbers"):
            validate_deletion_support(valid[:-1] + [(True, 97)], self.residual_edges)
        with self.assertRaisesRegex(ValueError, "integer JSON numbers"):
            validate_deletion_support(valid[:-1] + [("1", 97)], self.residual_edges)

    def test_core_validation_is_positive_deletion_subset_only(self) -> None:
        support = validate_deletion_support(
            HISTORICAL_TRUSTED_SUPPORTS[0], self.residual_edges
        )
        requested = deletion_assumptions(support, self.variables)
        mapping = {-self.variables[edge]: edge for edge in self.residual_edges}
        core = validate_reported_core(
            [requested[-1], requested[0]], requested, mapping
        )
        self.assertEqual(
            core,
            sorted(
                [requested[-1], requested[0]], key=lambda literal: mapping[literal]
            ),
        )
        with self.assertRaisesRegex(ValueError, "duplicate"):
            validate_reported_core([requested[0], requested[0]], requested, mapping)
        with self.assertRaisesRegex(ValueError, "positive-deletion-only"):
            validate_reported_core([-requested[0]], requested, mapping)
        outsider = next(lit for lit in mapping if lit not in requested)
        with self.assertRaisesRegex(ValueError, "subset"):
            validate_reported_core([outsider], requested, mapping)
        with self.assertRaisesRegex(ValueError, "no assumption core"):
            validate_reported_core(None, requested, mapping)

    def test_unknown_and_SAT_never_query_or_accept_a_core(self) -> None:
        solver = Mock()
        solver.get_core.side_effect = AssertionError("get_core must not be called")
        requested = [-1, -2]
        mapping = {-1: (0, 1), -2: (0, 2)}
        self.assertIsNone(
            extract_core_only_after_unsat("UNKNOWN_WALL_LIMIT", solver, requested, mapping)
        )
        self.assertIsNone(
            extract_core_only_after_unsat("SAT", solver, requested, mapping)
        )
        solver.get_core.assert_not_called()
        self.assertIsNone(accept_core_only_after_replay(requested, "SAT"))
        self.assertIsNone(
            accept_core_only_after_replay(requested, "UNKNOWN_CONFLICT_LIMIT")
        )

    def test_minimization_removes_only_UNSAT_and_final_cross_check_is_fail_closed(self) -> None:
        outcomes = iter(("UNSAT", "SAT", "UNKNOWN_WALL_LIMIT"))

        def scripted(trial: list[int]) -> dict[str, object]:
            return {
                "outcome": next(outcomes),
                "elapsed_seconds": 0.0,
                "calls": 1,
                "stats_delta": {},
            }

        mapping = {-1: (0, 1), -2: (0, 2), -3: (0, 3)}
        minimized, trials, complete = greedy_minimize_replayed_core(
            [-1, -2, -3], mapping, scripted
        )
        self.assertEqual(minimized, [-2, -3])
        self.assertFalse(complete)
        self.assertEqual(
            [trial["removed_only_if_completed_UNSAT"] for trial in trials],
            [True, False, False],
        )
        self.assertEqual(
            final_core_after_cross_check([-1, -2, -3], minimized, "UNSAT"),
            (minimized, "ACCEPT_MINIMIZED_AFTER_FRESH_UNSAT"),
        )
        self.assertEqual(
            final_core_after_cross_check(
                [-1, -2, -3], minimized, "UNKNOWN_CONFLICT_LIMIT"
            ),
            ([-1, -2, -3], "FALLBACK_TO_ORIGINAL_ON_UNKNOWN"),
        )
        accepted, decision = final_core_after_cross_check(
            [-1, -2, -3], minimized, "SAT"
        )
        self.assertIsNone(accepted)
        self.assertEqual(decision, "QUARANTINE_SAT_MISMATCH")

    def test_no_good_polarity_is_or_of_positive_x_literals(self) -> None:
        support = validate_deletion_support(
            HISTORICAL_TRUSTED_SUPPORTS[0], self.residual_edges
        )
        assumptions = deletion_assumptions(support, self.variables)
        mapping = {-self.variables[edge]: edge for edge in self.residual_edges}
        no_good = deletion_core_to_master_no_good(
            assumptions, mapping, self.variables
        )
        self.assertTrue(all(literal > 0 for literal in no_good))
        self.assertEqual(
            no_good, [self.variables[edge] for edge in sorted(support)]
        )

    def test_size_six_stop_requires_completed_requested_minimization(self) -> None:
        def record(complete: bool, requested: bool = True) -> dict[str, object]:
            return {
                "accepted_core": {
                    "size": 6,
                    "greedy_minimization_requested": requested,
                    "greedy_minimization_complete": complete,
                }
            }

        self.assertTrue(first_completed_cores_are_size_six([record(True)] * 16))
        self.assertFalse(
            first_completed_cores_are_size_six(
                [record(True)] * 15 + [record(False)]
            )
        )
        self.assertFalse(
            first_completed_cores_are_size_six(
                [record(True)] * 15 + [record(True, requested=False)]
            )
        )

    def test_definitive_UNSAT_core_replays_on_distinct_backend(self) -> None:
        # The common toy clause says x1 OR x2.  Positive deletion assumptions
        # d1=d2=true are encoded as -x1,-x2 and make it UNSAT.
        requested = [-1, -2]
        mapping = {-1: (0, 1), -2: (0, 2)}
        with Solver(name="glucose42", bootstrap_with=[[1, 2]]) as primary:
            self.assertFalse(primary.solve(assumptions=requested))
            core = extract_core_only_after_unsat(
                "UNSAT", primary, requested, mapping
            )
        self.assertIsNotNone(core)
        with Solver(name="minisat22", bootstrap_with=[[1, 2]]) as replay:
            self.assertFalse(replay.solve(assumptions=core))
        self.assertEqual(accept_core_only_after_replay(core, "UNSAT"), core)

    def test_degree_cap_encoding_is_necessary_and_active(self) -> None:
        variables, _ = build_variables(5)
        clauses, maximum, metadata = encode_final_degree_upper_bounds(
            5, variables, max(variables.values()), degree_cap=2
        )
        self.assertGreater(maximum, max(variables.values()))
        self.assertEqual(metadata["degree_blocks"], 5)
        self.assertGreater(metadata["degree_clauses"], 0)
        star = [variables[(0, 1)], variables[(0, 2)], variables[(0, 3)]]
        with Solver(name="glucose42", bootstrap_with=clauses) as solver:
            self.assertTrue(solver.solve(assumptions=star[:2]))
            self.assertFalse(solver.solve(assumptions=star))

    def test_solver_pair_rejects_aliases_and_accepts_distinct_backends(self) -> None:
        with self.assertRaisesRegex(ValueError, "distinct backends"):
            validate_solver_pair("g42", "glucose42")
        validate_solver_pair("glucose42", "minisat22")

    def test_production_common_formula_has_pinned_identity(self) -> None:
        bank = HERE / "r3_18_budget6_branch_0_universal_union.cuts.json"
        masks, info = load_universal_bank(bank)
        formula = build_common_formula(
            self.rows, sha256(SEED), masks, info
        )
        metadata = formula.metadata
        self.assertEqual(metadata["structural_clauses"], 181381)
        self.assertEqual(metadata["degree_clauses"], 285300)
        self.assertEqual(metadata["universal_I18_bank"]["masks"], 251771)
        self.assertEqual(metadata["total_clauses"], 718452)
        self.assertEqual(metadata["maximum_variable"], 154190)
        self.assertEqual(metadata["learned_core_clauses_installed"], 0)
        self.assertIn([-formula.variables[FIXED_EDGE]], formula.clauses)
        structural = metadata["structural_metadata"]
        self.assertEqual(structural["triangle_clauses"], 161700)
        self.assertEqual(structural["exact_six_residual_counter_literals"], 826)
        self.assertEqual(structural["exact_residual_input_edge_deletions"], 6)
        self.assertEqual(structural["fixed_deleted_edge"], [97, 99])
        self.assertEqual(metadata["degree_metadata"]["degree_cap"], DEGREE_CAP)
        self.assertEqual(
            metadata["universal_I18_bank"]["sha256"], sha256(bank)
        )
        self.assertEqual(
            metadata["formula_fingerprint_sha256"],
            "a6f920afa451174ed05932174951481a63647a2ba603c762379f9357323fa5e2",
        )

    def test_mask_digest_empty_value_is_stable(self) -> None:
        # Guards the ordered-bank identity helper used in the common formula.
        self.assertEqual(
            masks_hash([]),
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
        )

    def test_external_paths_are_redacted(self) -> None:
        self.assertEqual(
            _shareable_path(Path("/common/home/private-user/input.json")),
            "external/input.json",
        )


if __name__ == "__main__":
    unittest.main()
