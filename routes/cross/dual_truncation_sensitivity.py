#!/usr/bin/env python3
"""Numerical audit of a conditional two-sided Lin--Niu sensitivity formula.

This does not prove the omitted blue-side induction.  It checks the algebraic
consequence *if* that induction supplies the stated beta'_quad term uniformly.
Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import json
import math
from statistics import NormalDist


NORMAL = NormalDist()


def solve_p(C: float) -> float:
    """Solve log(p) / log(1-p) = C on (0, 1/2]."""
    if C < 1:
        raise ValueError("C must be at least 1")
    if C == 1:
        return 0.5
    lo, hi = 1e-15, 0.5
    for _ in range(200):
        mid = (lo + hi) / 2
        value = math.log(mid) / math.log1p(-mid)
        # The ratio decreases from infinity to one as p increases.
        if value > C:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def coefficients(C: float) -> dict[str, float]:
    p = solve_p(C)
    b = NORMAL.inv_cdf(p)  # b = -c_p
    a = math.exp(-(b * b) / 2) / math.sqrt(2 * math.pi)

    mean_upper = -a / p
    second_upper = 1 - b * a / p
    variance_upper = second_upper - mean_upper * mean_upper

    mean_lower = a / (1 - p)
    second_lower = 1 + b * a / (1 - p)
    variance_lower = second_lower - mean_lower * mean_lower

    gamma_red = 1 - variance_upper
    gamma_blue = 1 - variance_lower
    beta_red = gamma_red * a**4 / (8 * p**4)
    beta_blue = gamma_blue * a**4 / (8 * (1 - p) ** 4)

    sensitivity_red = C * p / (C * p + 1 - p)
    sensitivity_blue = 1 - sensitivity_red
    red_contribution = sensitivity_red * beta_red
    # P_blue(C l) gains -beta_blue*(C l)^4/(D^2 l^2).
    # Since its normalized exponent is C*rho*l^2, delta rho=C^3 beta/D^2.
    blue_contribution = sensitivity_blue * C**3 * beta_blue

    return {
        "C": C,
        "p_C": p,
        "cutoff_b_minus_c_p": b,
        "gamma_red_upper_truncation": gamma_red,
        "gamma_blue_lower_truncation": gamma_blue,
        "beta_red": beta_red,
        "beta_blue": beta_blue,
        "lambda_red": sensitivity_red,
        "lambda_blue": sensitivity_blue,
        "red_coefficient_of_D_minus_2": red_contribution,
        "conditional_blue_coefficient_of_D_minus_2": blue_contribution,
        "conditional_total_coefficient_of_D_minus_2": (
            red_contribution + blue_contribution
        ),
        "conditional_blue_to_red_gain_ratio": blue_contribution / red_contribution,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("C", nargs="*", type=float, default=[1.1, 2, 5, 10, 100])
    args = parser.parse_args()
    print(json.dumps([coefficients(C) for C in args.C], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
