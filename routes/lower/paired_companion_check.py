#!/usr/bin/env python3
"""Finite sanity checks for the paired companion ledger.

This script checks exact algebra and a deterministic collection of perturbed
histories.  It is not a proof of the asymptotic or Ramsey statements.
"""

from __future__ import annotations

import math
import random
from statistics import NormalDist


def exact_sum(r: int) -> int:
    return r * (r - 1) * (r - 2) * (3 * r - 5) // 12


def upper_truncated_parameters(p: float) -> tuple[float, float, float]:
    cutoff = NormalDist().inv_cdf(p)
    density = math.exp(-cutoff * cutoff / 2) / math.sqrt(2 * math.pi)
    mills = density / p
    variance = 1 - cutoff * mills - mills * mills
    return mills, variance, 1 - variance


def check_history(
    *, k: int, d: float, lam: float, mus: list[float], variances: list[float], P: float
) -> tuple[float, float]:
    coefficients = [sum(mus) - mu for mu in mus]
    hms_linear = lam * lam / d * sum(a_i * a_i for a_i in coefficients)
    refined_linear = (
        P
        * lam
        * lam
        / (2 * d)
        * sum(v_i * a_i * a_i for v_i, a_i in zip(variances, coefficients))
    )
    exact_difference = hms_linear - refined_linear
    identity_difference = (
        lam
        * lam
        / d
        * sum(
            (1 - P * v_i / 2) * a_i * a_i
            for v_i, a_i in zip(variances, coefficients)
        )
    )
    assert math.isclose(exact_difference, identity_difference, rel_tol=2e-13)
    assert len(mus) == len(variances) == k
    return exact_difference, min(abs(a_i) for a_i in coefficients)


def main() -> None:
    for r in range(1, 200):
        direct = sum(k * (k - 1) ** 2 for k in range(1, r))
        assert direct == exact_sum(r)

    p = 0.2
    C = 2.0
    D = 400.0
    ell = 1000
    d = (D * ell) ** 2
    mills, variance, gamma = upper_truncated_parameters(p)
    lam = -mills * math.sqrt(d)
    Q = D / (8 * C * mills)
    P = Q / (Q - 1)

    rng = random.Random(20260812)
    weakest_ratio = math.inf
    for k in range(2, 101):
        for _ in range(50):
            mus = [
                -mills / math.sqrt(d)
                + rng.uniform(-1, 1) / (D * math.sqrt(d))
                for _ in range(k)
            ]
            variances = [
                variance + rng.uniform(-1, 1) / D for _ in range(k)
            ]
            difference, _ = check_history(
                k=k,
                d=d,
                lam=lam,
                mus=mus,
                variances=variances,
                P=P,
            )
            leading = (
                (1 + gamma)
                / 2
                * mills**4
                * k
                * (k - 1) ** 2
                / d
            )
            weakest_ratio = min(weakest_ratio, difference / leading)
            assert difference > 0

    print(f"exact sum checked for r < 200")
    print(f"p={p}, C={C}, D={D}, P={P:.9f}")
    print(f"gamma_R={gamma:.9f}")
    print(f"weakest sampled (exact deficit)/(leading deficit)={weakest_ratio:.9f}")
    print("PASS: local identity and positivity hold on all sampled histories")


if __name__ == "__main__":
    main()
