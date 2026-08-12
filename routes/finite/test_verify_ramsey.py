#!/usr/bin/env python3
"""Small exhaustive-oracle tests for verify_ramsey.py."""

from __future__ import annotations

import itertools
import random
import unittest

from pysat.solvers import Solver

try:
    from .graph_utils import enumerate_cliques
    from .extension_sat_cegar import diagnose
    from .compound_search_r3 import conflicts, exact_delta, flip_edge, pair_counts
    from .addition_repair_sat_cegar import repair as add_only_repair
    from .bounded_deletion_sat_cegar import solve as bounded_delete_solve
    from .budget9_core_guided import forced_hub_proof, solve_limited_once
    from .benders_budget9 import (
        conditional_cut_truth,
        fixed_deletion_repair,
        locally_eligible,
        two_addition_deletion_lower_bound,
    )
    from .verify_ramsey_sat import (
        sat_contains_clique,
        sat_contains_clique_positional,
    )
    from .verify_ramsey import CliqueTargetSearch, complement
    from .new_basin_search import (
        minimum_triangle_edge_hitting_set,
        triangle_edge_multiplicity,
        triangle_tuples,
    )
except ImportError:  # Support unittest discovery with routes/finite as start dir.
    from graph_utils import enumerate_cliques
    from extension_sat_cegar import diagnose
    from compound_search_r3 import conflicts, exact_delta, flip_edge, pair_counts
    from addition_repair_sat_cegar import repair as add_only_repair
    from bounded_deletion_sat_cegar import solve as bounded_delete_solve
    from budget9_core_guided import forced_hub_proof, solve_limited_once
    from benders_budget9 import (
        conditional_cut_truth,
        fixed_deletion_repair,
        locally_eligible,
        two_addition_deletion_lower_bound,
    )
    from verify_ramsey_sat import sat_contains_clique, sat_contains_clique_positional
    from verify_ramsey import CliqueTargetSearch, complement
    from new_basin_search import (
        minimum_triangle_edge_hitting_set,
        triangle_edge_multiplicity,
        triangle_tuples,
    )


def rows_from_mask(n: int, edge_mask: int) -> list[int]:
    rows = [0] * n
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (edge_mask >> k) & 1:
                rows[i] |= 1 << j
                rows[j] |= 1 << i
            k += 1
    return rows


def brute_exists(rows: list[int], target: int) -> bool:
    for vertices in itertools.combinations(range(len(rows)), target):
        if all((rows[u] >> v) & 1 for u, v in itertools.combinations(vertices, 2)):
            return True
    return False


def brute_extendable(rows: list[int], r: int, s: int) -> bool:
    n = len(rows)
    if brute_exists(rows, r) or brute_exists(complement(rows), s):
        return False
    for neighborhood in range(1 << n):
        augmented = rows.copy() + [neighborhood]
        for v in range(n):
            if (neighborhood >> v) & 1:
                augmented[v] |= 1 << n
        if not brute_exists(augmented, r) and not brute_exists(
            complement(augmented), s
        ):
            return True
    return False


def edge_mask_from_rows(rows: list[int]) -> int:
    mask = 0
    k = 0
    for u in range(len(rows)):
        for v in range(u + 1, len(rows)):
            if (rows[u] >> v) & 1:
                mask |= 1 << k
            k += 1
    return mask


def brute_repair_exists(
    rows: list[int], s: int, deletion_budget: int, add_only: bool = False
) -> bool:
    n = len(rows)
    initial = edge_mask_from_rows(rows)
    edge_count = n * (n - 1) // 2
    for final in range(1 << edge_count):
        deleted = (initial & ~final).bit_count()
        if deleted > deletion_budget:
            continue
        if add_only and deleted:
            continue
        candidate = rows_from_mask(n, final)
        if not brute_exists(candidate, 3) and not brute_exists(
            complement(candidate), s
        ):
            return True
    return False


class CliqueSearchTests(unittest.TestCase):
    def test_new_basin_triangle_transversal_against_brute_force(self) -> None:
        rng = random.Random(20260813)
        for n in range(3, 7):
            pairs = list(itertools.combinations(range(n), 2))
            for _ in range(80):
                rows = rows_from_mask(n, rng.getrandbits(len(pairs)))
                triangles = triangle_tuples(rows)
                got, witness = minimum_triangle_edge_hitting_set(triangles)
                expected = len(pairs) + 1
                for mask in range(1 << len(pairs)):
                    chosen = {
                        pairs[i] for i in range(len(pairs)) if (mask >> i) & 1
                    }
                    if all(
                        any(
                            tuple(sorted(edge)) in chosen
                            for edge in itertools.combinations(triangle, 2)
                        )
                        for triangle in triangles
                    ):
                        expected = min(expected, len(chosen))
                self.assertEqual(got, expected)
                self.assertEqual(len(witness), got)
                self.assertTrue(
                    all(
                        any(
                            tuple(sorted(edge)) in set(witness)
                            for edge in itertools.combinations(triangle, 2)
                        )
                        for triangle in triangles
                    )
                )
                multiplicity = triangle_edge_multiplicity(triangles)
                self.assertEqual(sum(multiplicity.values()), 3 * len(triangles))

    def test_two_addition_joint_cost_against_brute_vertex_cover(self) -> None:
        labels = [(0, i + 1) for i in range(6)]
        possible = list(itertools.combinations(labels, 2))
        matchings = []
        for mask in range(1 << len(possible)):
            chosen = [possible[i] for i in range(len(possible)) if mask >> i & 1]
            flattened = [label for pair in chosen for label in pair]
            if len(flattened) == len(set(flattened)):
                matchings.append(chosen)
        for first in matchings:
            for second in matchings:
                requirements = set(first + second)
                expected = len(labels) + 1
                for mask in range(1 << len(labels)):
                    selected = {
                        labels[i] for i in range(len(labels)) if mask >> i & 1
                    }
                    if all(left in selected or right in selected for left, right in requirements):
                        expected = min(expected, len(selected))
                self.assertEqual(
                    two_addition_deletion_lower_bound(first, second), expected
                )

    def test_benders_conditional_cut_small_graph_oracle(self) -> None:
        # Exhaust every pair (triangle-free base H, triangle-free final G) on
        # four vertices.  Whenever alpha(G)<3, actual additions in G satisfy
        # local eligibility and every semantic conditional I_3 cut is true.
        # This independently checks the logical implication behind master cut
        # (1), including sets made independent only by base-edge deletions.
        n = 4
        edge_total = n * (n - 1) // 2
        for base_mask in range(1 << edge_total):
            base = rows_from_mask(n, base_mask)
            if brute_exists(base, 3):
                continue
            base_edges = {
                edge
                for edge in itertools.combinations(range(n), 2)
                if (base[edge[0]] >> edge[1]) & 1
            }
            for final_mask in range(1 << edge_total):
                final = rows_from_mask(n, final_mask)
                if brute_exists(final, 3) or brute_exists(complement(final), 3):
                    continue
                final_edges = {
                    edge
                    for edge in itertools.combinations(range(n), 2)
                    if (final[edge[0]] >> edge[1]) & 1
                }
                deleted = base_edges - final_edges
                additions = final_edges - base_edges
                self.assertTrue(
                    all(locally_eligible(base, deleted, edge) for edge in additions)
                )
                for subset in itertools.combinations(range(n), 3):
                    self.assertTrue(
                        conditional_cut_truth(
                            base, deleted, additions, subset
                        ),
                        (base_mask, final_mask, subset),
                    )

    def test_fixed_deletion_subproblem_forbids_readding_deleted_edge(self) -> None:
        # K2 with its sole edge selected for deletion cannot have alpha<2 if
        # deleted original edges remain fixed false.  The legacy post-delete
        # add-only routine would treat that edge as addable and return SAT;
        # this is the exact regression the Benders subproblem must prevent.
        base = rows_from_mask(2, 1)
        result, candidate = fixed_deletion_repair(
            base_rows=base,
            deleted={(0, 1)},
            fixed_absent=set(),
            s=2,
            seed_masks=[],
            solver_name="minisat22",
            conflict_chunk=100,
            max_conflicts=1000,
            per_call_seconds=1.0,
            max_seconds=2.0,
            oracle_nodes=1000,
            oracle_seconds=1.0,
        )
        self.assertEqual(result["status"], "UNSAT")
        self.assertFalse(result["deleted_original_edges_are_addition_variables"])
        self.assertIsNone(candidate)

        post_delete = rows_from_mask(2, 0)
        legacy = add_only_repair(post_delete, 2, "minisat22", None)
        self.assertEqual(legacy["status"], "SAT")
        self.assertEqual(legacy["added_edges"], [[0, 1]])

    def test_forced_hub_triangle_hitting_proof(self) -> None:
        triangles = [(0, 1, 2), (0, 1, 3), (0, 1, 4)]
        proof = forced_hub_proof(triangles, (0, 1), budget=2)
        self.assertTrue(proof["hub_deletion_forced"])
        self.assertEqual(proof["deletion_lower_bound_if_hub_kept"], 3)
        self.assertTrue(proof["off_hub_groups_pairwise_edge_disjoint"])

        non_forced = forced_hub_proof(triangles, (0, 1), budget=3)
        self.assertFalse(non_forced["hub_deletion_forced"])

    def test_conflict_limited_solver_slice_returns_unknown(self) -> None:
        # Unsatisfiable pigeonhole PHP(6,5), intentionally stopped long before
        # a proof. This protects the budget-9 runner against a regression to a
        # blocking, unbounded solver.solve() call.
        pigeons, holes = 6, 5

        def variable(pigeon: int, hole: int) -> int:
            return pigeon * holes + hole + 1

        clauses = [
            [variable(pigeon, hole) for hole in range(holes)]
            for pigeon in range(pigeons)
        ]
        clauses.extend(
            [-variable(first, hole), -variable(second, hole)]
            for hole in range(holes)
            for first in range(pigeons)
            for second in range(first + 1, pigeons)
        )
        with Solver(name="minisat22", bootstrap_with=clauses) as solver:
            outcome, timer_fired, _, delta = solve_limited_once(
                solver, conflict_budget=1, wall_seconds=1.0
            )
        self.assertIsNone(outcome)
        self.assertFalse(timer_fired)
        self.assertGreaterEqual(delta["conflicts"], 1)

    def test_all_graphs_through_six_vertices(self) -> None:
        # All graphs through n=5, plus a deterministic sample at n=6.
        cases: list[tuple[int, int]] = []
        for n in range(1, 6):
            cases.extend((n, m) for m in range(1 << (n * (n - 1) // 2)))
        rng = random.Random(20260812)
        cases.extend((6, rng.getrandbits(15)) for _ in range(2000))
        for n, mask in cases:
            rows = rows_from_mask(n, mask)
            for graph in (rows, complement(rows)):
                for target in range(1, n + 1):
                    got = CliqueTargetSearch(graph, target).run().exists
                    self.assertEqual(got, brute_exists(graph, target))

    def test_clique_enumerator_against_brute_force(self) -> None:
        rng = random.Random(1701)
        for n in range(1, 8):
            for _ in range(100):
                rows = rows_from_mask(n, rng.getrandbits(n * (n - 1) // 2))
                for target in range(1, n + 1):
                    got = set(enumerate_cliques(rows, target))
                    expected = {
                        sum(1 << v for v in vertices)
                        for vertices in itertools.combinations(range(n), target)
                        if all(
                            (rows[u] >> v) & 1
                            for u, v in itertools.combinations(vertices, 2)
                        )
                    }
                    self.assertEqual(got, expected)

    def test_restricted_candidate_search(self) -> None:
        # K4 restricted to vertices {0,1,2} should expose only a K3.
        rows = rows_from_mask(4, (1 << 6) - 1)
        self.assertTrue(
            CliqueTargetSearch(rows, 3).run(candidates=0b0111).exists
        )
        self.assertFalse(
            CliqueTargetSearch(rows, 4).run(candidates=0b0111).exists
        )

    def test_sat_clique_checker_against_complete_truth_table(self) -> None:
        for n in range(1, 6):
            for mask in range(1 << (n * (n - 1) // 2)):
                rows = rows_from_mask(n, mask)
                for target in range(1, n + 1):
                    self.assertEqual(
                        sat_contains_clique(rows, target)["exists"],
                        brute_exists(rows, target),
                        (n, mask, target),
                    )
                    self.assertEqual(
                        sat_contains_clique_positional(rows, target)["exists"],
                        brute_exists(rows, target),
                        ("positional", n, mask, target),
                    )

    def test_extension_cegar_against_complete_truth_table(self) -> None:
        rng = random.Random(31317)
        cases: list[tuple[int, int]] = []
        for n in range(1, 5):
            cases.extend((n, mask) for mask in range(1 << (n * (n - 1) // 2)))
        cases.extend((5, rng.getrandbits(10)) for _ in range(100))
        for n, mask in cases:
            rows = rows_from_mask(n, mask)
            for r, s in ((3, 3), (3, 4), (4, 3), (4, 4), (3, 5), (5, 3)):
                if brute_exists(rows, r) or brute_exists(complement(rows), s):
                    continue
                expected = brute_extendable(rows, r, s)
                got = diagnose(rows, r, s, "cadical195", None)[
                    "one_vertex_extendable"
                ]
                self.assertEqual(got, expected, (n, mask, r, s))

    def test_exact_r3_edge_deltas_against_full_recount(self) -> None:
        rng = random.Random(3013)
        for n in range(4, 9):
            for _ in range(50):
                rows = rows_from_mask(
                    n, rng.getrandbits(n * (n - 1) // 2)
                )
                for s in (3, 4):
                    triangles, independent, truncated = conflicts(rows, s)
                    self.assertFalse(truncated)
                    score = len(triangles) + len(independent)
                    triangle_counts = pair_counts(triangles)
                    independent_counts = pair_counts(independent)
                    for u in range(n):
                        for v in range(u + 1, n):
                            delta, _ = exact_delta(
                                rows,
                                u,
                                v,
                                s,
                                triangle_counts,
                                independent_counts,
                                None,
                            )
                            changed = rows.copy()
                            flip_edge(changed, u, v)
                            new_triangles, new_independent, _ = conflicts(
                                changed, s
                            )
                            self.assertEqual(
                                delta,
                                len(new_triangles)
                                + len(new_independent)
                                - score,
                                (n, s, u, v),
                            )

    def test_repair_sat_encodings_against_complete_graph_space(self) -> None:
        for n in range(2, 5):
            for mask in range(1 << (n * (n - 1) // 2)):
                rows = rows_from_mask(n, mask)
                for s in (3, 4):
                    if not brute_exists(rows, 3):
                        expected_add = brute_repair_exists(
                            rows, s, deletion_budget=0, add_only=True
                        )
                        got_add = add_only_repair(
                            rows, s, "cadical195", None
                        )["status"] == "SAT"
                        self.assertEqual(got_add, expected_add, (n, mask, s))
                    for budget in (0, 1):
                        expected = brute_repair_exists(rows, s, budget)
                        got = bounded_delete_solve(
                            rows, s, budget, "cadical195", None, None
                        )["status"] == "SAT"
                        self.assertEqual(
                            got, expected, (n, mask, s, budget)
                        )


if __name__ == "__main__":
    unittest.main()
