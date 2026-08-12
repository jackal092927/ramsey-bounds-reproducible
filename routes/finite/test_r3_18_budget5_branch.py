"""Small exhaustive tests for the R(3,18) branch formula primitives."""

from __future__ import annotations

import itertools
import unittest

from .r3_18_budget5_branch import delete_edge, hitting_clause


class R318Budget5PrimitiveTests(unittest.TestCase):
    def test_delete_edge_is_symmetric_and_preserves_other_edges(self) -> None:
        rows = [0] * 4
        for u, v in [(0, 1), (1, 2), (2, 3)]:
            rows[u] |= 1 << v
            rows[v] |= 1 << u
        reduced = delete_edge(rows, (1, 2))
        self.assertFalse((reduced[1] >> 2) & 1)
        self.assertFalse((reduced[2] >> 1) & 1)
        self.assertTrue((reduced[0] >> 1) & 1)
        self.assertTrue((reduced[2] >> 3) & 1)

    def test_hitting_clause_contains_every_pair_once(self) -> None:
        n = 7
        pairs = list(itertools.combinations(range(n), 2))
        variables = {pair: i + 1 for i, pair in enumerate(pairs)}
        vertices = [0, 2, 4, 6]
        mask = sum(1 << v for v in vertices)
        clause = hitting_clause(mask, n, variables)
        expected = [variables[pair] for pair in itertools.combinations(vertices, 2)]
        self.assertEqual(clause, expected)
        self.assertEqual(len(clause), 6)


if __name__ == "__main__":
    unittest.main()

