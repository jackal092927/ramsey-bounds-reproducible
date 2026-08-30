"""Exhaustive tests for the PySAT-free sequential-counter checker."""

from __future__ import annotations

import ast
import itertools
import unittest
from pathlib import Path

from .check_r3_18_seqcounter import audit
from .independent_seqcounter import (
    AtMostEncoding,
    EqualsEncoding,
    clauses_hold,
    construct_atmost_extension,
    construct_equals_extension,
    encode_atmost,
    encode_equals,
    literal_truth,
)


HERE = Path(__file__).resolve().parent


def auxiliary_variables(encoding: AtMostEncoding | EqualsEncoding) -> list[int]:
    if isinstance(encoding, AtMostEncoding):
        return sorted(encoding.auxiliary_by_coordinate.values())
    return sorted(
        {
            *encoding.lower.auxiliary_by_coordinate.values(),
            *encoding.upper.auxiliary_by_coordinate.values(),
        }
    )


def has_extension(
    encoding: AtMostEncoding | EqualsEncoding, primary: dict[int, bool]
) -> bool:
    for bits in itertools.product((False, True), repeat=len(auxiliary_variables(encoding))):
        values = dict(primary)
        values.update(zip(auxiliary_variables(encoding), bits, strict=True))
        if clauses_hold(encoding.clauses, values):
            return True
    return False


class IndependentSequentialCounterTests(unittest.TestCase):
    def test_modules_do_not_import_pysat(self) -> None:
        for name in ("independent_seqcounter.py", "check_r3_18_seqcounter.py"):
            tree = ast.parse((HERE / name).read_text(encoding="utf-8"))
            imported = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imported.extend(alias.name for alias in node.names)
                elif isinstance(node, ast.ImportFrom) and node.module:
                    imported.append(node.module)
            self.assertFalse(
                any(
                    module == "pysat" or module.startswith("pysat.")
                    for module in imported
                )
            )

    def test_known_irredundant_clause_order(self) -> None:
        atmost = encode_atmost([1, 2, 3, 4], 2, 100)
        self.assertEqual(
            atmost.clauses,
            [
                [-1, 101],
                [-101, 102],
                [-2, -101, 103],
                [-103, 104],
                [-3, -103],
                [-2, 102],
                [-3, -102, 104],
                [-4, -104],
            ],
        )
        equals = encode_equals([1, 2, 3, 4], 2, 100)
        self.assertEqual(
            equals.clauses,
            [
                [1, 101],
                [-101, 102],
                [2, -101, 103],
                [-103, 104],
                [3, -103],
                [2, 102],
                [3, -102, 104],
                [4, -104],
                [-1, 105],
                [-105, 106],
                [-2, -105, 107],
                [-107, 108],
                [-3, -107],
                [-2, 106],
                [-3, -106, 108],
                [-4, -108],
            ],
        )

    def test_atmost_projection_semantics_exhaustively(self) -> None:
        for literals in ([1, 2, 3, 4, 5], [-1, 2, -3, 4, -5]):
            for bound in range(len(literals) + 1):
                encoding = encode_atmost(literals, bound, len(literals))
                for bits in itertools.product((False, True), repeat=len(literals)):
                    primary = {index + 1: bit for index, bit in enumerate(bits)}
                    expected = sum(literal_truth(literal, primary) for literal in literals) <= bound
                    self.assertEqual(has_extension(encoding, primary), expected)
                    constructed = construct_atmost_extension(encoding, primary)
                    self.assertEqual(constructed is not None, expected)

    def test_equals_projection_semantics_exhaustively(self) -> None:
        for literals in ([1, 2, 3, 4], [-1, 2, -3, 4]):
            for bound in range(len(literals) + 1):
                encoding = encode_equals(literals, bound, len(literals))
                for bits in itertools.product((False, True), repeat=len(literals)):
                    primary = {index + 1: bit for index, bit in enumerate(bits)}
                    expected = sum(literal_truth(literal, primary) for literal in literals) == bound
                    self.assertEqual(has_extension(encoding, primary), expected)
                    constructed = construct_equals_extension(encoding, primary)
                    self.assertEqual(constructed is not None, expected)

    def test_all_six_large_schemas_and_frozen_digests(self) -> None:
        result = audit(HERE, schema_only=True)
        self.assertEqual(result["status"], "INDEPENDENT_SEQCOUNTER_SCHEMA_VERIFIED")
        self.assertFalse(result["pysat_cardenc_imported"])
        self.assertEqual(len(result["branches"]), 6)
        self.assertEqual(
            [branch["counter_clauses"] for branch in result["branches"]],
            [7_394, 7_394, 7_394, 16_420, 16_420, 16_420],
        )


if __name__ == "__main__":
    unittest.main()
