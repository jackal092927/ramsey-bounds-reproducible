#!/usr/bin/env python3
"""Arithmetic checks for TRANSVERSE_ENCODING_ATTEMPT.md.

The proof is field-theoretic.  This script checks its exact incidence
inequalities and evaluates the resulting path-count lower bound.
"""

from __future__ import annotations

import argparse
import math
from fractions import Fraction


def qbracket(d: int, q: int) -> int:
    if d == 0:
        return 0
    return (q**d - 1) // (q - 1)


def check_case(t: int, q: int, capacity_constant: float) -> None:
    if t < 2 or q < 4:
        raise ValueError("require t >= 2 and q >= 4")

    n = qbracket(t + 1, q)
    p = Fraction(qbracket(t, q), n)
    p2 = Fraction(qbracket(t - 1, q), n)

    # Exact two-point covariance and the elementary p bounds.
    assert p2 <= p * p
    assert p > Fraction(3, 4 * q)
    assert p < Fraction(1, q)

    k = math.floor((t - 1) * q * math.log(q) / 12)
    if k < 1:
        raise ValueError("q is too small for k_q >= 1")

    alpha = Fraction(2 * q - 3, 2 * q)
    assert -math.log(float(alpha)) <= 12 / (5 * q)

    # Worst-prefix lower bound for mu = p |S|.
    log_mu_lower = (
        math.log(float(p)) + math.log(n) + k * math.log(float(alpha))
    )
    assert log_mu_lower >= math.log(8)
    mu_lower = math.exp(log_mu_lower)

    # Exact formula (2), evaluated logarithmically.
    log_l = (
        k * math.log(float(p * n * n / 4))
        + (k * (k - 1) / 2) * math.log(float(alpha))
    )
    log_root = log_l / k
    claimed_log_root = (
        math.log(3 / 16) + (t + 0.9 * (t - 1)) * math.log(q)
    )
    assert log_root >= claimed_log_root - 1e-12

    log_capacity_root = math.log(capacity_constant) + t * math.log(q)

    print(
        f"t={t} q={q} N={n} k={k} "
        f"p={float(p):.8g} p2-p^2={float(p2-p*p):.3e}"
    )
    print(
        f"  worst-prefix mu lower={mu_lower:.6g} "
        f"(Chebyshev threshold 8)"
    )
    print(
        "  log_q path-root lower="
        f"{log_root / math.log(q):.8f}; "
        "formula-(4)="
        f"{claimed_log_root / math.log(q):.8f}; "
        f"capacity(C={capacity_constant:g})="
        f"{log_capacity_root / math.log(q):.8f}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", type=int, nargs="*", default=[2, 3, 4])
    parser.add_argument("--q", type=int, nargs="*", default=[101, 257, 1021])
    parser.add_argument("--capacity-constant", type=float, default=100.0)
    args = parser.parse_args()

    for t in args.t:
        for q in args.q:
            check_case(t, q, args.capacity_constant)

    print("all transverse-encoding arithmetic checks PASS")


if __name__ == "__main__":
    main()
