"""Minimal structural tests for the second R(3,13) basin generator."""

from __future__ import annotations

import unittest

from .graph_utils import add_vertex
from .new_basin_search import triangle_edge_multiplicity, triangle_tuples
from .second_new_basin_search import selected_induced_edge_diagnostics


class SecondNewBasinTests(unittest.TestCase):
    def test_induced_degree_equals_new_edge_triangle_multiplicity(self) -> None:
        # Old graph: path 0-1-2-3 plus isolated vertex 4 (triangle-free).
        rows = [0] * 5
        for u, v in [(0, 1), (1, 2), (2, 3)]:
            rows[u] |= 1 << v
            rows[v] |= 1 << u
        selected = [0, 1, 2, 3, 4]
        edge_count, max_degree, degrees = selected_induced_edge_diagnostics(
            rows, selected
        )
        self.assertEqual(edge_count, 3)
        self.assertEqual(max_degree, 2)
        self.assertEqual(degrees, {0: 1, 1: 2, 2: 2, 3: 1, 4: 0})

        candidate = add_vertex(rows, selected)
        triangles = triangle_tuples(candidate)
        multiplicity = triangle_edge_multiplicity(triangles)
        self.assertEqual(len(triangles), edge_count)
        self.assertEqual(max(multiplicity.values()), max_degree)

    def test_empty_neighborhood_is_degenerate_but_exact(self) -> None:
        rows = [0, 0, 0]
        self.assertEqual(
            selected_induced_edge_diagnostics(rows, []), (0, 0, {})
        )


if __name__ == "__main__":
    unittest.main()

