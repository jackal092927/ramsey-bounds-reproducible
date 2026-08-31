from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from routes.finite.check_r3_18_seed_automorphism_wl import (
    AuditError,
    audit,
    parse_seed,
    refine,
)


HERE = Path(__file__).resolve().parent
SEED = HERE / "certificates" / "r3_18_n100_nearmiss.txt"


class SeedAutomorphismWlTests(unittest.TestCase):
    def test_frozen_seed_is_individualized_in_two_rounds(self) -> None:
        result = audit(SEED)
        self.assertEqual(result["automorphism_group_order"], 1)
        self.assertEqual(
            [entry["classes"] for entry in result["refinement_rounds"]],
            [3, 15, 100],
        )
        self.assertFalse(result["branch_symmetry_transfer_available"])

    def test_cycle_is_not_falsely_individualized(self) -> None:
        matrix = [[0] * 100 for _ in range(100)]
        for vertex in range(100):
            other = (vertex + 1) % 100
            matrix[vertex][other] = matrix[other][vertex] = 1
        colors, rounds = refine(matrix)
        self.assertEqual(len(set(colors)), 1)
        self.assertEqual([entry["classes"] for entry in rounds], [1, 1])

    def test_symlinked_seed_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as name:
            link = Path(name) / "seed.txt"
            link.symlink_to(SEED)
            with self.assertRaisesRegex(AuditError, "non-symlink"):
                parse_seed(link)


if __name__ == "__main__":
    unittest.main()
