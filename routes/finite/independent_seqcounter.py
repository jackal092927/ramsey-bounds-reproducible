#!/usr/bin/env python3
"""PySAT-free construction and semantics helpers for sequential counters.

The production formulas were emitted by PySAT.  This module deliberately does
not import :mod:`pysat.card` or :class:`pysat.formula.IDPool`.  It implements
the irredundant Sinz/Knuth sequential schema directly, so a checker can compare
the stored clause blocks with a second implementation and can construct the
auxiliary values promised by the projection-semantics proof in the paper.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Mapping


@dataclass
class AtMostEncoding:
    """One independently generated ``sum(literals) <= bound`` encoding."""

    literals: tuple[int, ...]
    bound: int
    base_top_id: int
    top_id: int
    clauses: list[list[int]]
    auxiliary_by_coordinate: dict[tuple[int, int], int]


@dataclass
class EqualsEncoding:
    """Equality as at-most on complements followed by at-most on positives."""

    literals: tuple[int, ...]
    bound: int
    lower: AtMostEncoding
    upper: AtMostEncoding

    @property
    def clauses(self) -> list[list[int]]:
        return [*self.lower.clauses, *self.upper.clauses]

    @property
    def top_id(self) -> int:
        return self.upper.top_id


def _validated_literals(literals: list[int] | tuple[int, ...]) -> tuple[int, ...]:
    normalized = tuple(int(literal) for literal in literals)
    if any(literal == 0 for literal in normalized):
        raise ValueError("a sequential-counter input literal cannot be zero")
    variables = [abs(literal) for literal in normalized]
    if len(set(variables)) != len(variables):
        raise ValueError("sequential-counter input variables must be distinct")
    return normalized


def encode_atmost(
    literals: list[int] | tuple[int, ...], bound: int, top_id: int
) -> AtMostEncoding:
    """Generate the irredundant sequential encoding without calling PySAT.

    For the nontrivial case ``0 < bound < n - 1``, the auxiliary variable at
    coordinate ``(level, offset)`` represents the threshold statement that at
    least ``level + 1`` inputs among positions ``0`` through
    ``offset + level`` are true.  Variable allocation and clause order match
    the schema used by PySAT 1.9.dev13, but the implementation is independent.
    """

    normalized = _validated_literals(literals)
    n = len(normalized)
    if bound < 0:
        raise ValueError("an at-most bound cannot be negative")
    base_top_id = max([int(top_id), *(abs(literal) for literal in normalized)])
    current_top = base_top_id
    clauses: list[list[int]] = []
    auxiliary: dict[tuple[int, int], int] = {}

    if not normalized or bound >= n:
        return AtMostEncoding(
            normalized, bound, base_top_id, current_top, clauses, auxiliary
        )
    if bound == n - 1:
        clauses.append([-literal for literal in normalized])
        return AtMostEncoding(
            normalized, bound, base_top_id, current_top, clauses, auxiliary
        )
    if bound == 0:
        clauses.extend([[-literal] for literal in normalized])
        return AtMostEncoding(
            normalized, bound, base_top_id, current_top, clauses, auxiliary
        )

    def y(level: int, offset: int) -> int:
        nonlocal current_top
        coordinate = (level, offset)
        if coordinate not in auxiliary:
            current_top += 1
            auxiliary[coordinate] = current_top
        return auxiliary[coordinate]

    width = n - bound
    for offset in range(width):
        first = y(0, offset)
        clauses.append([-normalized[offset], first])

        for level in range(bound - 1):
            current = y(level, offset)
            if offset < width - 1:
                clauses.append([-current, y(level, offset + 1)])
            next_level = y(level + 1, offset)
            clauses.append(
                [-normalized[offset + level + 1], -current, next_level]
            )

        last = y(bound - 1, offset)
        if offset < width - 1:
            clauses.append([-last, y(bound - 1, offset + 1)])
        clauses.append([-normalized[offset + bound], -last])

    return AtMostEncoding(
        normalized, bound, base_top_id, current_top, clauses, auxiliary
    )


def encode_atleast(
    literals: list[int] | tuple[int, ...], bound: int, top_id: int
) -> AtMostEncoding:
    """Encode ``sum(literals) >= bound`` as at-most on complemented inputs."""

    normalized = _validated_literals(literals)
    if bound < 0 or bound > len(normalized):
        raise ValueError("an at-least bound must lie between zero and n")
    return encode_atmost(
        tuple(-literal for literal in normalized), len(normalized) - bound, top_id
    )


def encode_equals(
    literals: list[int] | tuple[int, ...], bound: int, top_id: int
) -> EqualsEncoding:
    """Encode equality in the same two-block order as the frozen formulas."""

    normalized = _validated_literals(literals)
    if bound < 0 or bound > len(normalized):
        raise ValueError("an equality bound must lie between zero and n")
    lower = encode_atleast(normalized, bound, top_id)
    upper = encode_atmost(normalized, bound, lower.top_id)
    return EqualsEncoding(normalized, bound, lower, upper)


def literal_truth(literal: int, values: Mapping[int, bool]) -> bool:
    """Evaluate one signed literal under a total assignment of its variable."""

    variable = abs(literal)
    if variable not in values:
        raise KeyError(f"missing truth value for variable {variable}")
    value = bool(values[variable])
    return value if literal > 0 else not value


def clauses_hold(clauses: list[list[int]], values: Mapping[int, bool]) -> bool:
    """Return whether every clause is true under ``values``."""

    return all(any(literal_truth(literal, values) for literal in clause) for clause in clauses)


def construct_atmost_extension(
    encoding: AtMostEncoding, primary_values: Mapping[int, bool]
) -> dict[int, bool] | None:
    """Construct the prefix-threshold auxiliary assignment when the bound holds.

    Returning ``None`` means that the primary assignment violates the projected
    cardinality constraint.  Otherwise the returned total assignment satisfies
    every independently generated clause.
    """

    truths = [literal_truth(literal, primary_values) for literal in encoding.literals]
    if sum(truths) > encoding.bound:
        return None
    values = {int(variable): bool(value) for variable, value in primary_values.items()}
    for (level, offset), variable in encoding.auxiliary_by_coordinate.items():
        prefix = truths[: offset + level + 1]
        values[variable] = sum(prefix) >= level + 1
    if not clauses_hold(encoding.clauses, values):
        raise AssertionError("constructive sequential-counter extension failed")
    return values


def construct_equals_extension(
    encoding: EqualsEncoding, primary_values: Mapping[int, bool]
) -> dict[int, bool] | None:
    """Construct both disjoint auxiliary blocks of an equality encoding."""

    lower_values = construct_atmost_extension(encoding.lower, primary_values)
    if lower_values is None:
        return None
    upper_values = construct_atmost_extension(encoding.upper, primary_values)
    if upper_values is None:
        return None
    values = {**lower_values, **upper_values}
    if not clauses_hold(encoding.clauses, values):
        raise AssertionError("constructive equality-counter extension failed")
    return values


def dimacs_clause_sha256(clauses: list[list[int]]) -> str:
    """Hash clauses in their canonical DIMACS-line representation."""

    digest = hashlib.sha256()
    for clause in clauses:
        digest.update((" ".join(str(literal) for literal in clause) + " 0\n").encode("ascii"))
    return digest.hexdigest()
