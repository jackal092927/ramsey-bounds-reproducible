#!/usr/bin/env python3
"""Heuristic outer search for the u0=309/125 diagonal-growth candidate.

This program is exploratory only.  It fixes the pre-registered source-level
constants sigma=5001/10000 and D=89/10^6, searches the retained-spine
parameters, and leaves rationalization and Arb replay to separate checkers.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, differential_evolution, minimize


HERE = Path(__file__).resolve().parent
PAYLOAD = json.loads(
    (HERE / "certificate-higher-order-tetradecic-chain-v6.json").read_text()
)
COEFFICIENTS = np.asarray(PAYLOAD["target_coefficients"], dtype=float)

U0 = 309.0 / 125.0
SIGMA = 5001.0 / 10000.0
GROWTH = 89.0 / 1_000_000.0
TAIL_MARGIN = 2.0e-9
DEGREE_MARGIN = 2.0e-9
BRANCH_MARGIN = 2.0e-9


def polynomial(x: float) -> float:
    return float(COEFFICIENTS @ (x ** np.arange(1, len(COEFFICIENTS) + 1)))


def polynomial_prime(x: float) -> float:
    degrees = np.arange(1, len(COEFFICIENTS) + 1)
    return float((degrees * COEFFICIENTS) @ (x ** (degrees - 1)))


def rate(x: float) -> float:
    return ((1 + x) * math.log1p(x) - x * math.log(x)
            + polynomial(x) * math.exp(-x))


def rate_prime(x: float) -> float:
    return (math.log((1 + x) / x)
            + (polynomial_prime(x) - polynomial(x)) * math.exp(-x))


U_ONE = rate(1.0)
UP_ONE = rate_prime(1.0)


def correlation_parameters(epsilon: float) -> tuple[float, float]:
    multiplier = 1.0 + 2.0 / epsilon
    beta = (SIGMA - TAIL_MARGIN) / (SIGMA + GROWTH * multiplier)
    correlation = 4.0 * U0 * (1.0 + epsilon)
    return beta, correlation


def red_capacity(c_eta: float, q: float, tau: float,
                 off_diagonal: float) -> float:
    def margin(gap: float) -> float:
        r_axis = gap / off_diagonal
        z = (1.0 - tau) / (1.0 - r_axis)
        page = (c_eta * r_axis + tau * q
                + (1.0 - r_axis) * rate(z))
        return U_ONE - gap - page - BRANCH_MARGIN

    hi = min(0.99 * off_diagonal * tau, 2.0e-5)
    if margin(0.0) <= 0.0 or margin(hi) >= 0.0:
        return -1.0
    return brentq(margin, 0.0, hi, xtol=1e-15, rtol=1e-13)


def evaluate(vector: np.ndarray, verbose: bool = False):
    eta, log_delta, log_lambda, log_tau, log_epsilon = map(float, vector)
    book_delta = math.exp(log_delta)
    lambda_zero = math.exp(log_lambda)
    tau = math.exp(log_tau)
    epsilon = math.exp(log_epsilon)
    probability = 0.5 - eta - DEGREE_MARGIN / tau
    if probability <= 0.0 or book_delta > min(0.25, probability / 4.0):
        return None
    if lambda_zero < max(2.0, 6.0 * math.log(1.0 / book_delta)):
        return None

    beta, correlation = correlation_parameters(epsilon)
    if not 0.0 < beta < 1.0:
        return None

    c_eta = math.log(2.0 / (1.0 + eta))
    diagonal = U_ONE - 2.0 * c_eta
    off_diagonal = UP_ONE - c_eta
    if not 0.0 < diagonal < off_diagonal:
        return None

    log_delta_value = math.log(1.0 / book_delta)
    log_probability = math.log(1.0 / probability)
    page_cost = (log_probability + 3.0 * book_delta / probability
                 + 6.0 * log_delta_value * log_probability / lambda_zero)
    rho = math.log(2.0 / beta)
    xi_cost = (2.0 * rho
               + 4.0 * correlation * lambda_zero ** (1.0 / 3.0)
               + 12.0 * correlation * log_delta_value
               / lambda_zero ** (2.0 / 3.0))
    if page_cost >= UP_ONE or 2.0 * tau * xi_cost >= U_ONE:
        return None

    cap_red = red_capacity(c_eta, page_cost, tau, off_diagonal)
    cap_blue = U_ONE - tau * page_cost - rate(1.0 - tau) - BRANCH_MARGIN
    cap_reservoir = (diagonal
                     * (U_ONE - 2.0 * tau * xi_cost - BRANCH_MARGIN)
                     / U_ONE)
    cap_wedge = 0.99 * off_diagonal * tau
    gap = min(cap_red, cap_blue, cap_reservoir, cap_wedge)
    if gap <= diagonal * tau:
        return None

    result = {
        "gap": gap,
        "base": math.exp(U_ONE - gap),
        "eta": eta,
        "p": probability,
        "delta": book_delta,
        "lambda0": lambda_zero,
        "tau": tau,
        "epsilon": epsilon,
        "beta": beta,
        "C": correlation,
        "q": page_cost,
        "Xi": xi_cost,
        "A": diagonal,
        "E": off_diagonal,
        "cap_red": cap_red,
        "cap_blue": cap_blue,
        "cap_reservoir": cap_reservoir,
        "cap_wedge": cap_wedge,
        "tail_margin": (SIGMA * (1.0 - beta)
                        - GROWTH * beta * (1.0 + 2.0 / epsilon)),
        "degree_margin": tau * (0.5 - eta - probability),
    }
    if verbose:
        print(json.dumps(result, indent=2, sort_keys=True))
    return result


def objective(vector: np.ndarray) -> float:
    result = evaluate(vector)
    return 1.0 if result is None else -result["gap"]


def main() -> None:
    bounds = [
        (0.026, 0.033),
        (math.log(1e-5), math.log(2e-4)),
        (math.log(8_000), math.log(30_000)),
        (math.log(3e-4), math.log(1.2e-3)),
        (math.log(1e-4), math.log(3e-3)),
    ]
    global_result = differential_evolution(
        objective, bounds, seed=2026081211, workers=1, popsize=32,
        maxiter=1100, tol=1e-12, polish=False,
    )
    local_result = minimize(
        objective, global_result.x, method="Nelder-Mead",
        options={"maxiter": 100_000, "xatol": 1e-13, "fatol": 1e-17},
    )
    candidate = (local_result.x if local_result.fun < global_result.fun
                 else global_result.x)
    evaluate(candidate, verbose=True)


if __name__ == "__main__":
    main()
