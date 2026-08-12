#!/usr/bin/env python3
"""Deterministic floating-point frontier search for retained-spine round 2.

This is a diagnostic optimizer, not a proof checker.  It searches the closure
of the Yang--Mao degree gate, p = 1/2-eta.  This is favourable to feasibility:
the page cost is strictly decreasing in p, while the other expressions do not
depend on p.  Consequently any legal p < 1/2-eta has a no-better frontier.

For fixed (eta, delta, lambda0, Delta), the red axis page is strictly improved
by increasing tau, whereas the diagonal reservoir cost increases with tau.
The relaxed best tau therefore saturates the reservoir inequality.  The
remaining search is three dimensional.  Reported results are finite-box,
floating-point evidence only.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, differential_evolution


HERE = Path(__file__).resolve().parent
COEFFICIENTS = tuple(
    map(
        float,
        json.loads(
            (HERE / "certificate-higher-order-tetradecic-chain-v6.json")
            .read_text(encoding="utf-8")
        )["target_coefficients"],
    )
)


def polynomial(x: float) -> float:
    # The certificate stores the coefficients of x, ..., x^14.
    return sum(a * x ** (i + 1) for i, a in enumerate(COEFFICIENTS))


def polynomial_prime(x: float) -> float:
    return sum((i + 1) * a * x**i for i, a in enumerate(COEFFICIENTS))


def rate(x: float) -> float:
    return (
        (1.0 + x) * math.log1p(x)
        - x * math.log(x)
        + polynomial(x) * math.exp(-x)
    )


def rate_prime(x: float) -> float:
    return (
        math.log((1.0 + x) / x)
        + (polynomial_prime(x) - polynomial(x)) * math.exp(-x)
    )


U_ONE = rate(1.0)
UP_ONE = rate_prime(1.0)
CORRELATION = 8.0 * math.log(432.0)
ETA_MIN = 2.0 * math.exp(-U_ONE / 2.0) - 1.0
ETA_MAX = 0.5 - math.exp(-UP_ONE)

# These bounds deliberately contain the previously found optimizer by several
# orders of magnitude.  They are part of the reported bounded-search verdict.
LOG_DELTA_BOUNDS = (math.log(1e-12), math.log(0.125))
LOG_LAMBDA_BOUNDS = (math.log(10.0), math.log(1e9))


def relaxed_frontier(vector: np.ndarray, details: bool = False):
    eta, log_delta, log_lambda = map(float, vector)
    probability = 0.5 - eta  # favourable closure of the strict source gate
    book_delta = math.exp(log_delta)
    lambda_zero = math.exp(log_lambda)
    loss = math.log(1.0 / book_delta)

    if not (
        ETA_MIN < eta < ETA_MAX
        and 0.0 < book_delta <= min(probability / 4.0, 0.25)
        and lambda_zero >= max(2.0, 6.0 * loss)
    ):
        return None if details else -1.0

    c_eta = math.log(2.0 / (1.0 + eta))
    diagonal = U_ONE - 2.0 * c_eta
    off_diagonal = UP_ONE - c_eta
    log_probability = math.log(1.0 / probability)
    page_cost = (
        log_probability
        + 3.0 * book_delta / probability
        + 6.0 * loss * log_probability / lambda_zero
    )
    xi_cost = (
        2.0 * math.log(96.0)
        + 4.0 * CORRELATION * lambda_zero ** (1.0 / 3.0)
        + 12.0 * CORRELATION * loss / lambda_zero ** (2.0 / 3.0)
    )
    if not (0.0 < diagonal < off_diagonal and page_cost < UP_ONE):
        return None if details else -1.0

    # Reservoir equality at the diagonal point x=y=Delta/diagonal:
    # 2*c*Delta/diagonal + 2*tau*Xi = U(1)-Delta.
    # Since 1+2*c/diagonal=U(1)/diagonal, this simplifies exactly.
    def tau_max(gap: float) -> float:
        return U_ONE * (1.0 - gap / diagonal) / (2.0 * xi_cost)

    def page_margin(gap: float) -> float:
        tau = tau_max(gap)
        radius = gap / off_diagonal
        if not (0.0 < radius < tau < 1.0 and gap < diagonal):
            return -1.0
        ratio = (1.0 - tau) / (1.0 - radius)
        page = (
            c_eta * radius
            + tau * page_cost
            + (1.0 - radius) * rate(ratio)
        )
        return U_ONE - gap - page

    # tau=Delta/E is the end of the legal red-axis wedge.  It gives a safe
    # finite upper bracket before Delta reaches the diagonal coefficient.
    legal_upper = U_ONE / (
        U_ONE / diagonal + 2.0 * xi_cost / off_diagonal
    )
    upper = legal_upper * (1.0 - 1e-12)
    grid = np.linspace(upper / 256.0, upper, 256)
    values = np.asarray([page_margin(float(x)) for x in grid])
    feasible = np.flatnonzero(values >= 0.0)
    if feasible.size == 0:
        return None if details else -1.0
    index = int(feasible[-1])
    gap = float(grid[index])
    if index + 1 < grid.size and values[index + 1] < 0.0:
        gap = brentq(
            page_margin,
            float(grid[index]),
            float(grid[index + 1]),
            xtol=5e-324,
            rtol=1e-14,
        )

    if not details:
        return gap
    tau = tau_max(gap)
    return {
        "eta": eta,
        "p_closure": probability,
        "delta": book_delta,
        "lambda0": lambda_zero,
        "tau": tau,
        "Delta": gap,
        "A": diagonal,
        "E": off_diagonal,
        "q": page_cost,
        "Xi": xi_cost,
        "page_margin": page_margin(gap),
        "reservoir_margin": 0.0,
    }


def main() -> None:
    bounds = [
        (ETA_MIN + 1e-10, ETA_MAX - 1e-10),
        LOG_DELTA_BOUNDS,
        LOG_LAMBDA_BOUNDS,
    ]
    seeds = (260801962, 260801963, 260801964, 260801965)
    results = []
    for seed in seeds:
        result = differential_evolution(
            lambda x: -float(relaxed_frontier(x)),
            bounds,
            seed=seed,
            popsize=20,
            maxiter=250,
            tol=1e-11,
            polish=True,
            updating="immediate",
            workers=1,
        )
        details = relaxed_frontier(result.x, details=True)
        assert details is not None
        results.append(details)
        print(f"seed={seed}: Delta={details['Delta']:.16g}", flush=True)

    best = max(results, key=lambda item: item["Delta"])
    print("search_status: FLOATING_POINT_FINITE_BOX_ONLY")
    print(f"eta_box: [{ETA_MIN + 1e-10:.16g}, {ETA_MAX - 1e-10:.16g}]")
    print(f"delta_box: [{math.exp(LOG_DELTA_BOUNDS[0]):.1e}, "
          f"{math.exp(LOG_DELTA_BOUNDS[1]):.1e}]")
    print(f"lambda0_box: [{math.exp(LOG_LAMBDA_BOUNDS[0]):.1e}, "
          f"{math.exp(LOG_LAMBDA_BOUNDS[1]):.1e}]")
    for key, value in best.items():
        print(f"best_{key}: {value:.17g}")
    print("preregistered_target: 1e-6")
    print(f"target_shortfall: {1e-6 - best['Delta']:.17g}")
    print("accepted: NO")


if __name__ == "__main__":
    main()
