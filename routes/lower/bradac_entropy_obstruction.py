#!/usr/bin/env python3
"""Toy optimization exposing the obstruction in a naive Bradač refinement.

If type-l unmarked steps have relative fanout at most

    q^(t-l) exp(-c i/q)

at their i-th occurrence, their product has log-overhead

    (t-l) j log q - c j(j-1)/(2q).

The maximum is still Theta(q log^2 q), so this potential decay alone cannot
lower the k >= C q (log q)^2 threshold to C q log q.
"""

from __future__ import annotations

import argparse
import math


def log_overhead(q: int, codimension: int, shrink: float, j: int) -> float:
    return codimension * j * math.log(q) - shrink * j * (j - 1) / (2 * q)


def maximize(q: int, codimension: int, shrink: float) -> tuple[int, float]:
    # The concave quadratic has its continuous maximizer here; inspect nearby integers.
    center = codimension * q * math.log(q) / shrink + 0.5
    candidates = {max(0, int(math.floor(center)) + d) for d in range(-3, 4)}
    best_j = max(candidates, key=lambda j: log_overhead(q, codimension, shrink, j))
    return best_j, log_overhead(q, codimension, shrink, best_j)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--t", type=int, default=4)
    parser.add_argument("--shrink", type=float, default=1 / 128)
    parser.add_argument("--q", type=int, nargs="*", default=[64, 128, 256, 512, 1024, 2048])
    args = parser.parse_args()
    if args.t < 1 or not (0 < args.shrink <= 1):
        raise SystemExit("need t>=1 and 0<shrink<=1")

    print("q   codim  maximizing j    log overhead    /[q(log q)^2]   /[q log q]")
    for q in args.q:
        for codim in range(1, args.t + 1):
            j, value = maximize(q, codim, args.shrink)
            print(
                f"{q:<4d}{codim:>7d}{j:>14d}{value:>16.5f}"
                f"{value/(q*math.log(q)**2):>18.6f}"
                f"{value/(q*math.log(q)):>15.4f}"
            )
        print()


if __name__ == "__main__":
    main()
