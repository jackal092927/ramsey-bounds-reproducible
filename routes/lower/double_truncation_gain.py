#!/usr/bin/env python3
"""Numerical audit for the two-sided truncated-Gaussian correction.

This script is only a numerical coefficient audit.  The fixed-C blue-side
induction is proved separately in ``BLUE_INDUCTION_DRAFT.md`` and
``PAIRED_COMPANION_ATTEMPT.md``; identification with a final published HMS
comparator remains open.

Only mpmath is required.  All logarithms are natural.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import mpmath as mp


@dataclass(frozen=True)
class Gain:
    C: mp.mpf
    p: mp.mpf
    cutoff: mp.mpf
    gamma_red: mp.mpf
    gamma_blue: mp.mpf
    beta_red: mp.mpf
    beta_blue: mp.mpf
    weight_red: mp.mpf
    red_contribution: mp.mpf
    blue_contribution: mp.mpf

    @property
    def total_contribution(self) -> mp.mpf:
        return self.red_contribution + self.blue_contribution

    @property
    def blue_to_red(self) -> mp.mpf:
        return self.blue_contribution / self.red_contribution


def normal_pdf(x: mp.mpf) -> mp.mpf:
    return mp.exp(-(x * x) / 2) / mp.sqrt(2 * mp.pi)


def p_for_ratio(C: mp.mpf) -> mp.mpf:
    """Solve p=(1-p)^C for the unique p in (0, 1/2)."""
    if C <= 1:
        if C == 1:
            return mp.mpf("0.5")
        raise ValueError("C must be at least 1")
    lo = mp.mpf("1e-80")
    hi = mp.mpf("0.5")
    for _ in range(400):
        mid = (lo + hi) / 2
        # p-(1-p)^C is strictly increasing.
        if mid - mp.power(1 - mid, C) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def evaluate(C_value: float | str | mp.mpf) -> Gain:
    C = mp.mpf(C_value)
    p = p_for_ratio(C)
    # Phi(-c)=p, so c>0 for C>1.
    c = -mp.sqrt(2) * mp.erfinv(2 * p - 1)
    a = normal_pdf(c)

    # Upper truncation Z <= -c: V=1+c*m-m^2, m=a/p.
    m_red = a / p
    gamma_red = m_red * (m_red - c)

    # Lower truncation Z >= -c: V=1-c*m-m^2, m=a/(1-p).
    m_blue = a / (1 - p)
    gamma_blue = m_blue * (m_blue + c)

    beta_red = gamma_red * a**4 / (8 * p**4)
    beta_blue = gamma_blue * a**4 / (8 * (1 - p) ** 4)

    # Sensitivity of max_p min{red, blue} at the transverse crossing.
    weight_red = C * p / (C * p + 1 - p)
    red_contribution = weight_red * beta_red
    blue_contribution = (1 - weight_red) * C**3 * beta_blue

    return Gain(
        C=C,
        p=p,
        cutoff=c,
        gamma_red=gamma_red,
        gamma_blue=gamma_blue,
        beta_red=beta_red,
        beta_blue=beta_blue,
        weight_red=weight_red,
        red_contribution=red_contribution,
        blue_contribution=blue_contribution,
    )


def fmt(x: mp.mpf, digits: int = 9) -> str:
    return mp.nstr(x, digits)


def self_check() -> None:
    # At C=1, p=1/2 and both beta values equal 1/pi^3.
    g = evaluate(1)
    expected = 1 / mp.pi**3
    assert abs(g.beta_red - expected) < mp.mpf("1e-40")
    assert abs(g.beta_blue - expected) < mp.mpf("1e-40")
    assert abs(g.total_contribution - expected) < mp.mpf("1e-40")

    # Variance deficits and sensitivity weights must lie in (0,1).
    for C in ("1.01", "1.1", "2", "5", "10", "100"):
        row = evaluate(C)
        assert 0 < row.gamma_red < 1
        assert 0 < row.gamma_blue < 1
        assert 0 < row.weight_red < 1
        assert row.total_contribution > row.red_contribution > 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "C",
        nargs="*",
        default=["1", "1.01", "1.1", "1.5", "2", "3", "5", "10", "100"],
        help="ratios k/l (each must be >=1)",
    )
    args = parser.parse_args()
    mp.mp.dps = 70
    self_check()

    print(
        "C            p_C          c_p       red coeff      blue coeff     total coeff    blue/red"
    )
    for C in args.C:
        row = evaluate(C)
        print(
            f"{fmt(row.C, 7):>7}  {fmt(row.p, 10):>12}  {fmt(row.cutoff, 8):>10}  "
            f"{fmt(row.red_contribution, 10):>14}  "
            f"{fmt(row.blue_contribution, 10):>14}  "
            f"{fmt(row.total_contribution, 10):>14}  "
            f"{fmt(row.blue_to_red, 8):>10}"
        )
    print(
        "\nAll coefficients multiply D^{-2} and are relative to the "
        "unit-Hoelder companion; this table is not a final-HMS comparison."
    )


if __name__ == "__main__":
    main()
