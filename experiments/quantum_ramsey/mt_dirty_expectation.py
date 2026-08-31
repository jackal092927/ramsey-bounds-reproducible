#!/usr/bin/env python3
"""Exact one-step dirty-flaw expectation for Ramsey resampling.

The current coloring is an integer bit mask on E(K_n).  Given a k-set S,
the script computes the exact conditional expectation of the number of
monochromatic k-sets sharing at least two vertices with S after all edges
inside S are independently recolored.

No independence between different dirty flaws is assumed; the computation
uses linearity of expectation and exact rational arithmetic.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from fractions import Fraction


def edge_data(n: int) -> tuple[tuple[tuple[int, int], ...], dict[tuple[int, int], int]]:
    edges = tuple(itertools.combinations(range(n), 2))
    return edges, {edge: index for index, edge in enumerate(edges)}


def edge_color(mask: int, index: dict[tuple[int, int], int], u: int, v: int) -> int:
    edge = (u, v) if u < v else (v, u)
    return (mask >> index[edge]) & 1


def conditional_dirty_expectation(
    n: int, k: int, coloring: int, resampled_vertices: tuple[int, ...]
) -> tuple[Fraction, dict[int, int]]:
    if len(resampled_vertices) != k or len(set(resampled_vertices)) != k:
        raise ValueError("resampled_vertices must contain k distinct vertices")

    _, index = edge_data(n)
    resampled_set = frozenset(resampled_vertices)
    compatible_by_intersection: dict[int, int] = {}
    expectation = Fraction(0)

    for candidate in itertools.combinations(range(n), k):
        candidate_set = frozenset(candidate)
        intersection_size = len(candidate_set & resampled_set)
        if intersection_size < 2:
            continue
        if candidate_set == resampled_set:
            expectation += Fraction(2, 1 << math.comb(k, 2))
            continue

        unchanged_colors = {
            edge_color(coloring, index, u, v)
            for u, v in itertools.combinations(candidate, 2)
            if not (u in resampled_set and v in resampled_set)
        }
        if len(unchanged_colors) == 1:
            compatible_by_intersection[intersection_size] = (
                compatible_by_intersection.get(intersection_size, 0) + 1
            )
            expectation += Fraction(1, 1 << math.comb(intersection_size, 2))

    return expectation, compatible_by_intersection


def lll_parameters(n: int, k: int) -> tuple[Fraction, int, float]:
    probability = Fraction(2, 1 << math.comb(k, 2))
    dependency_degree = sum(
        math.comb(k, j) * math.comb(n - k, k - j)
        for j in range(2, k)
        if 0 <= k - j <= n - k
    )
    lll_left_side = math.e * (dependency_degree + 1) * float(probability)
    return probability, dependency_degree, lll_left_side


def all_red_summary(n: int, k: int) -> dict[str, object]:
    expectation, compatibility = conditional_dirty_expectation(
        n, k, coloring=0, resampled_vertices=tuple(range(k))
    )
    probability, dependency_degree, lll_left_side = lll_parameters(n, k)
    return {
        "n": n,
        "k": k,
        "bad_event_probability": str(probability),
        "dependency_degree": dependency_degree,
        "d_times_p": float(dependency_degree * probability),
        "e_times_d_plus_1_times_p": lll_left_side,
        "compatible_counts_by_intersection": {
            str(j): count for j, count in sorted(compatibility.items())
        },
        "conditional_expected_dirty_violations": str(expectation),
        "conditional_expected_dirty_violations_float": float(expectation),
    }


def self_check() -> None:
    result = all_red_summary(10, 6)
    assert result["dependency_degree"] == 209
    assert result["compatible_counts_by_intersection"] == {
        "2": 15,
        "3": 80,
        "4": 90,
        "5": 24,
    }
    expected = (
        Fraction(1, 1 << 14)
        + Fraction(15, 2)
        + Fraction(80, 8)
        + Fraction(90, 64)
        + Fraction(24, 1024)
    )
    assert result["conditional_expected_dirty_violations"] == str(expected)
    assert result["e_times_d_plus_1_times_p"] < 1


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=10)
    parser.add_argument("--k", type=int, default=6)
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()

    if not 2 <= args.k <= args.n:
        parser.error("require 2 <= k <= n")
    if args.self_check:
        self_check()
    print(json.dumps(all_red_summary(args.n, args.k), indent=2))


if __name__ == "__main__":
    main()
