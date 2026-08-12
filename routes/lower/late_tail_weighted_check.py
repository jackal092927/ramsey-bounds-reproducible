#!/usr/bin/env python3
"""Arithmetic checks for LATE_TAIL_WEIGHTED_AUDIT.md.

The mathematical proof is in the Markdown document.  This file checks only
its elementary inequalities over a finite grid.
"""

from __future__ import annotations

import math


def check_state_threshold(t: int, q: int) -> None:
    d = -math.log1p(-1.0 / (32.0 * t * q))
    for ell in range(t + 1):
        j = math.ceil((t - ell) * math.log(q) / d)
        log_left = math.log(2.0) + t * math.log(q) - d * j
        log_right = math.log(2.0) + ell * math.log(q)
        assert log_left <= log_right + 1e-10


def check_gaussian_bound(t: int, q: int) -> None:
    d = -math.log1p(-1.0 / (32.0 * t * q))
    assert d >= 1.0 / (32.0 * t * q)
    for ell in range(t + 1):
        a = (t - ell) * math.log(q)
        real_max = (a + d / 2.0) ** 2 / (2.0 * d)
        center = (a + d / 2.0) / d
        candidates = {
            0,
            max(0, math.floor(center) - 1),
            max(0, math.floor(center)),
            max(0, math.ceil(center)),
            max(0, math.ceil(center) + 1),
        }
        discrete_max = max(a * m - d * m * (m - 1) / 2.0 for m in candidates)
        assert discrete_max <= real_max + 1e-12 * max(1.0, abs(real_max))


def check_abstract_tree(t: int, q: int, depth_constant: float, base: float) -> None:
    w = math.floor(q * math.log(q))
    k = math.ceil(depth_constant * q * math.log(q))
    if k <= w:
        log_ratio = k * ((t - 1) * math.log(q) - math.log(base))
    else:
        log_ratio = w * (t - 1) * math.log(q) - k * math.log(base)
    # The asymptotic claim is only asserted once this finite instance is large.
    if q >= 2**160:
        assert log_ratio > 0


def check_potential_barrier(t: int, q: int, base: float) -> None:
    k = math.floor((t - 1) * q * math.log(q) / 12.0)
    if k <= 0:
        return
    log_ratio = k * (
        math.log(16.0 * base / 3.0) - 0.9 * (t - 1) * math.log(q)
    )
    claimed = -((t - 1) ** 2) * q * math.log(q) ** 2 / 20.0
    if math.log(16.0 * base / 3.0) <= (t - 1) * math.log(q) / 10.0 and k >= (
        (t - 1) * q * math.log(q) / 13.0
    ):
        assert log_ratio <= claimed + 1e-8


def main() -> None:
    for t in range(2, 8):
        for q in (16, 64, 256, 1024, 2**18, 2**160):
            check_state_threshold(t, q)
            check_gaussian_bound(t, q)
            for depth_constant in (0.25, 1.0, 3.0, 20.0):
                for base in (2.0, 100.0):
                    check_abstract_tree(t, q, depth_constant, base)
            for base in (1.0, 10.0, 100.0):
                check_potential_barrier(t, q, base)
    print("late-tail weighted arithmetic checks: PASS")


if __name__ == "__main__":
    main()
