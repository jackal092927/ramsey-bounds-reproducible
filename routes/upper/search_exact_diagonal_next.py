#!/usr/bin/env python3
"""Exploratory joint search for the exact-diagonal next-round protocol.

The diagonal floor is modeled by exp(-2*u0)/81 plus a fixed exploratory
proof allowance.  Output is floating-point frontier evidence only; it is
not a certificate and may be used to rationalize at most one candidate.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import brentq, differential_evolution, minimize


HERE = Path(__file__).resolve().parent
COEFFICIENTS = np.asarray(json.loads(
    (HERE / "certificate-higher-order-tetradecic-chain-v6.json").read_text()
)["target_coefficients"], dtype=float)

RATIO_ALLOWANCE = 2.0e-9
INNER_BUDGET = 1.02e-5
ASYMPTOTIC_ALLOWANCE = 2.0e-10
DEGREE_MARGIN = 1.5e-9
BRANCH_MARGIN = 1.2e-9


def polynomial(x: float) -> float:
    powers = x ** np.arange(1, len(COEFFICIENTS) + 1)
    return float(COEFFICIENTS @ powers)


def polynomial_prime(x: float) -> float:
    degrees = np.arange(1, len(COEFFICIENTS) + 1)
    return float((degrees * COEFFICIENTS) @ (x ** (degrees - 1)))


def rate(x: float) -> float:
    return ((1.0 + x) * math.log1p(x) - x * math.log(x)
            + polynomial(x) * math.exp(-x))


def rate_prime(x: float) -> float:
    return (math.log((1.0 + x) / x)
            + (polynomial_prime(x) - polynomial(x)) * math.exp(-x))


U_ONE = rate(1.0)
UP_ONE = rate_prime(1.0)


def exact_ratio(u0: float) -> float:
    a = math.exp(-u0)
    theta = math.sqrt(3.0) * u0 / 2.0
    p = (math.exp(u0) + 2.0 * math.exp(-u0 / 2.0)
         * math.cos(theta)) / 3.0
    n = (math.exp(-u0) + 2.0 * math.exp(u0 / 2.0)
         * math.cos(theta)) / 3.0
    return (1.0 + a * p * p) / (1.0 + a * n * n)


def inner_parameters(u0: float, epsilon: float):
    ratio = exact_ratio(u0)
    sigma0 = (ratio - 2.0 - RATIO_ALLOWANCE) / 2.0
    separator = (1.0 + 2.0 * sigma0) / 2.0
    if sigma0 <= 0.0:
        return None
    growth = math.exp(-2.0 * u0) / 81.0 + ASYMPTOTIC_ALLOWANCE
    multiplier = 1.0 + 2.0 / epsilon
    beta = (separator - INNER_BUDGET) / (separator + growth * multiplier)
    if not 0.0 < beta < 1.0:
        return None
    correlation = 4.0 * u0 * (1.0 + epsilon)
    return sigma0, separator, growth, beta, correlation, ratio


def red_capacity(c_eta: float, page_cost: float, tau: float,
                 off_diagonal: float) -> float:
    def margin(gap: float) -> float:
        r_axis = gap / off_diagonal
        z = (1.0 - tau) / (1.0 - r_axis)
        page = (c_eta * r_axis + tau * page_cost
                + (1.0 - r_axis) * rate(z))
        return U_ONE - gap - page - BRANCH_MARGIN

    upper = min(0.99 * off_diagonal * tau, 2.0e-5)
    if margin(0.0) <= 0.0 or margin(upper) >= 0.0:
        return -1.0
    return brentq(margin, 0.0, upper, xtol=1e-15, rtol=1e-13)


def evaluate(vector: np.ndarray, verbose: bool = False):
    eta, log_delta, log_lambda, log_tau, u0, log_epsilon = map(float, vector)
    delta = math.exp(log_delta)
    lambda_zero = math.exp(log_lambda)
    tau = math.exp(log_tau)
    epsilon = math.exp(log_epsilon)
    probability = 0.5 - eta - DEGREE_MARGIN / tau
    if probability <= 0.0 or delta > min(0.25, probability / 4.0):
        return None
    loss = math.log(1.0 / delta)
    if lambda_zero < max(2.0, 6.0 * loss):
        return None

    inner = inner_parameters(u0, epsilon)
    if inner is None:
        return None
    sigma0, separator, growth, beta, correlation, ratio = inner

    c_eta = math.log(2.0 / (1.0 + eta))
    diagonal = U_ONE - 2.0 * c_eta
    off_diagonal = UP_ONE - c_eta
    if not 0.0 < diagonal < off_diagonal:
        return None

    log_probability = math.log(1.0 / probability)
    page_cost = (log_probability + 3.0 * delta / probability
                 + 6.0 * loss * log_probability / lambda_zero)
    rho = math.log(2.0 / beta)
    xi_cost = (2.0 * rho
               + 4.0 * correlation * lambda_zero ** (1.0 / 3.0)
               + 12.0 * correlation * loss
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
        "delta": delta,
        "lambda0": lambda_zero,
        "tau": tau,
        "u0": u0,
        "ratio": ratio,
        "sigma0": sigma0,
        "separator": separator,
        "D": growth,
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
        "inner_budget": (separator * (1.0 - beta)
                         - growth * beta * (1.0 + 2.0 / epsilon)),
        "degree_margin": tau * (0.5 - eta - probability),
    }
    if verbose:
        print(json.dumps(result, indent=2, sort_keys=True))
    return result


def objective(vector: np.ndarray) -> float:
    value = evaluate(vector)
    return 1.0 if value is None else -value["gap"]


def main() -> None:
    bounds = [
        (0.026, 0.033),
        (math.log(1e-5), math.log(2e-4)),
        (math.log(8_000.0), math.log(30_000.0)),
        (math.log(3e-4), math.log(1.2e-3)),
        (2.4718, 2.49),
        (math.log(1e-4), math.log(3e-3)),
    ]
    global_result = differential_evolution(
        objective, bounds, seed=2026081217, workers=1, popsize=36,
        maxiter=1400, tol=5e-13, polish=False,
    )
    local_result = minimize(
        objective, global_result.x, method="Nelder-Mead",
        options={"maxiter": 150_000, "xatol": 3e-14, "fatol": 1e-17},
    )
    candidate = (local_result.x if local_result.fun < global_result.fun
                 else global_result.x)
    evaluate(candidate, verbose=True)


if __name__ == "__main__":
    main()
