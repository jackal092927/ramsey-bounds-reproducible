#!/usr/bin/env python3
"""Exhaustive small-instance oracles for higher-order Benders cuts."""

from __future__ import annotations

import itertools
import unittest

try:
    from .benders_next import (
        canonical_requirements,
        generate_ternary_cuts,
        vertex_coverable,
    )
except ImportError:  # pragma: no cover
    from benders_next import (
        canonical_requirements,
        generate_ternary_cuts,
        vertex_coverable,
    )


def brute_coverable(requirements, vertices, budget):
    requirements = canonical_requirements(requirements)
    for size in range(budget + 1):
        for selected in itertools.combinations(vertices, size):
            cover = set(selected)
            if all(left in cover or right in cover for left, right in requirements):
                return True
    return False


class HigherOrderBendersTests(unittest.TestCase):
    def test_exact_vertex_cover_oracle_all_graphs_through_six_vertices(self):
        labels = [(0, index + 1) for index in range(6)]
        possible = list(itertools.combinations(labels, 2))
        for mask in range(1 << len(possible)):
            requirements = [
                possible[index]
                for index in range(len(possible))
                if (mask >> index) & 1
            ]
            for budget in range(7):
                expected = brute_coverable(requirements, labels, budget)
                got, _ = vertex_coverable(requirements, budget)
                self.assertEqual(got, expected, (mask, budget))

    def test_genuine_ternary_cut_not_subsumed_by_any_pair(self):
        # Nine disjoint requirement edges are split among three additions.
        # Every pair needs six deletions (<=8), but all three need nine (>8).
        labels = [(0, index + 1) for index in range(18)]
        matching = list(zip(labels[::2], labels[1::2]))
        additions = [(0, 1), (0, 2), (0, 3)]
        requirements = {
            additions[0]: matching[:3],
            additions[1]: matching[3:6],
            additions[2]: matching[6:9],
        }
        for first, second in itertools.combinations(additions, 2):
            feasible, _ = vertex_coverable(
                requirements[first] + requirements[second], 8
            )
            self.assertTrue(feasible)
        feasible, _ = vertex_coverable(
            sum((requirements[edge] for edge in additions), []), 8
        )
        self.assertFalse(feasible)
        cuts, stats = generate_ternary_cuts(
            additions,
            requirements,
            residual_budget=8,
            top_k=3,
            max_triples=1,
            max_seconds=1.0,
        )
        self.assertEqual(cuts, [tuple(additions)])
        self.assertEqual(stats["pairwise_subsumed"], 0)
        self.assertEqual(stats["genuinely_ternary_incompatible"], 1)

    def test_generated_ternary_no_good_semantics_exhaustively(self):
        # Exhaust all three matchings on four deletion variables.  Whenever
        # the generator emits a ternary cut, no deletion set within the budget
        # can hit all three requirement families.
        labels = [(0, index + 1) for index in range(4)]
        possible = list(itertools.combinations(labels, 2))
        matchings = []
        for mask in range(1 << len(possible)):
            selected = [
                possible[index]
                for index in range(len(possible))
                if (mask >> index) & 1
            ]
            flattened = [endpoint for pair in selected for endpoint in pair]
            if len(flattened) == len(set(flattened)):
                matchings.append(selected)
        additions = [(0, 10), (0, 11), (0, 12)]
        for first in matchings:
            for second in matchings:
                for third in matchings:
                    requirements = dict(zip(additions, (first, second, third)))
                    for budget in range(3):
                        cuts, _ = generate_ternary_cuts(
                            additions,
                            requirements,
                            residual_budget=budget,
                            top_k=3,
                            max_triples=1,
                            max_seconds=1.0,
                        )
                        if cuts:
                            self.assertFalse(
                                brute_coverable(
                                    first + second + third, labels, budget
                                )
                            )


if __name__ == "__main__":
    unittest.main()
