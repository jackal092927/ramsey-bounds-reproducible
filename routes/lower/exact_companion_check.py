#!/usr/bin/env python3
"""Arithmetic audit for the exact HMS-versus-Hoelder companion.

Uses only the Python standard library.  The output is diagnostic: the
``HMS candidate`` column assumes the missing paired reverse-induction lemma.
It is not a Ramsey-number theorem.
"""

from __future__ import annotations

import argparse
import math
from statistics import NormalDist


def crossing_probability(C: float) -> float:
    """Solve p=(1-p)^C on (0,1/2]."""
    if C < 1:
        raise ValueError("C must be at least 1")
    lo, hi = 0.0, 0.5
    for _ in range(220):
        p = (lo + hi) / 2
        if p - (1 - p) ** C < 0:
            lo = p
        else:
            hi = p
    return (lo + hi) / 2


def exact_sum(r: int) -> int:
    """Return sum_{k=1}^{r-1} k(k-1)^2."""
    return r * (r - 1) * (r - 2) * (3 * r - 5) // 12


def row(C: float) -> tuple[float, ...]:
    p = crossing_probability(C)
    q = 1 - p
    c = -NormalDist().inv_cdf(p)
    a = math.exp(-c * c / 2) / math.sqrt(2 * math.pi)

    gamma_red = (a / p) * (a / p - c)
    gamma_blue = (a / q) * (a / q + c)
    weight_red = C * p / (C * p + q)

    beta_red = gamma_red * a**4 / (8 * p**4)
    beta_blue = gamma_blue * a**4 / (8 * q**4)
    unit = weight_red * beta_red + (1 - weight_red) * C**3 * beta_blue

    beta_red_hms = (1 + gamma_red) * a**4 / (8 * p**4)
    beta_blue_hms = (1 + gamma_blue) * a**4 / (8 * q**4)
    hms_candidate = (
        weight_red * beta_red_hms
        + (1 - weight_red) * C**3 * beta_blue_hms
    )
    return p, c, gamma_red, gamma_blue, unit, hms_candidate


def self_check() -> None:
    for r in range(1, 100):
        direct = sum(k * (k - 1) ** 2 for k in range(1, r))
        assert direct == exact_sum(r)

    p, c, gamma_red, gamma_blue, unit, hms = row(1.0)
    assert abs(p - 0.5) < 1e-15
    assert abs(c) < 1e-15
    assert abs(gamma_red - 2 / math.pi) < 1e-14
    assert abs(gamma_blue - 2 / math.pi) < 1e-14
    assert abs(unit - 1 / math.pi**3) < 1e-14
    assert hms > unit > 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "C",
        nargs="*",
        type=float,
        default=[1, 1.1, 2, 5, 10, 100],
    )
    args = parser.parse_args()
    self_check()

    print("C       p_C       gamma_R    gamma_B    unit-Hoelder   HMS-candidate")
    for C in args.C:
        p, _, gamma_red, gamma_blue, unit, hms = row(C)
        print(
            f"{C:6g}  {p:9.7f}  {gamma_red:9.7f}  {gamma_blue:9.7f}  "
            f"{unit:12.7f}  {hms:13.7f}"
        )
    print("\nAll final columns multiply D^{-2}; HMS-candidate is conditional.")


if __name__ == "__main__":
    main()
