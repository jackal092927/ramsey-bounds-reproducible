#!/usr/bin/env python3
"""Exploratory joint search for correlation and retained-spine parameters.

This is deliberately *not* a proof checker.  It evaluates the exact formulas
used by the frozen Arb certificates in ordinary double precision, reserves
explicit positive margins, and emits candidates for later rationalization and
independent Arb replay.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import differential_evolution, minimize
from scipy.optimize import brentq


HERE = Path(__file__).resolve().parent
PAYLOAD = json.loads(
    (HERE / "certificate-higher-order-tetradecic-chain-v6.json").read_text()
)
COEFFICIENTS = np.asarray(PAYLOAD["target_coefficients"], dtype=float)

# Search margins.  The final Arb certificate must separately prove >= 1e-9.
RATIO_MARGIN = 1.0e-8
TAIL_MARGIN = 2.0e-9
DEGREE_MARGIN = 2.0e-9
BRANCH_MARGIN = 2.0e-9


def polynomial(x: float) -> float:
    powers = x ** np.arange(1, len(COEFFICIENTS) + 1)
    return float(COEFFICIENTS @ powers)


def polynomial_prime(x: float) -> float:
    degrees = np.arange(1, len(COEFFICIENTS) + 1)
    return float((degrees * COEFFICIENTS) @ (x ** (degrees - 1)))


def rate(x: float) -> float:
    return (1 + x) * math.log1p(x) - x * math.log(x) + polynomial(x) * math.exp(-x)


def rate_prime(x: float) -> float:
    return math.log((1 + x) / x) + (polynomial_prime(x) - polynomial(x)) * math.exp(-x)


U_ONE = rate(1.0)
UP_ONE = rate_prime(1.0)


def correlation_parameters(u0: float, epsilon: float) -> tuple[float, ...] | None:
    """Maximize sigma and beta subject to reserved separator/tail margins."""
    eu = math.exp(u0)
    eh = math.exp(u0 / 2)
    em = math.exp(-u0)
    emh = math.exp(-u0 / 2)
    positive = (eu - 2 * emh) / 3
    negative = (2 * eh + em) / 3
    if positive <= 0:
        return None
    h_positive = 1 + em * positive * positive
    h_negative = 1 + em * negative * negative

    # h_positive - (2+2 sigma) h_negative = RATIO_MARGIN.
    sigma = ((h_positive - RATIO_MARGIN) / h_negative - 2) / 2
    if sigma <= TAIL_MARGIN:
        return None
    denominator = sigma + 4 * (1 + 2 / epsilon)
    beta = (sigma - TAIL_MARGIN) / denominator
    if not (0 < beta < 1):
        return None

    target = 2 + 2 * sigma
    derivative = 2 * eu * (eu - 2 * target) - 2 * eh - 4 * em
    derivative_second = 4 * eu * eu - 4 * target * eu - eh + 4 * em
    if min(derivative, derivative_second) <= 0:
        return None
    correlation = 4 * u0 * (1 + epsilon)
    return sigma, beta, correlation, h_positive - target * h_negative


def red_capacity(c_eta: float, q: float, tau: float, e_coeff: float) -> float:
    def margin(delta: float) -> float:
        r_axis = delta / e_coeff
        z = (1 - tau) / (1 - r_axis)
        page = c_eta * r_axis + tau * q + (1 - r_axis) * rate(z)
        return U_ONE - delta - page - BRANCH_MARGIN

    hi = min(0.99 * e_coeff * tau, 2.0e-5)
    if margin(0.0) <= 0 or margin(hi) >= 0:
        return -1.0
    return brentq(margin, 0.0, hi, xtol=1e-15, rtol=1e-13)


def evaluate(vector: np.ndarray, verbose: bool = False) -> dict[str, float] | None:
    eta, log_delta, log_lambda, log_tau, u0, log_epsilon = vector
    book_delta = math.exp(log_delta)
    lambda_zero = math.exp(log_lambda)
    tau = math.exp(log_tau)
    epsilon = math.exp(log_epsilon)
    degree_slack_parameter = DEGREE_MARGIN / tau
    probability = 0.5 - eta - degree_slack_parameter
    if probability <= 0 or book_delta > min(0.25, probability / 4):
        return None
    if lambda_zero < max(2.0, 6 * math.log(1 / book_delta)):
        return None

    corr = correlation_parameters(u0, epsilon)
    if corr is None:
        return None
    sigma, beta, correlation, ratio_margin = corr

    c_eta = math.log(2 / (1 + eta))
    a_coeff = U_ONE - 2 * c_eta
    e_coeff = UP_ONE - c_eta
    if not (0 < a_coeff < e_coeff):
        return None

    log_delta_value = math.log(1 / book_delta)
    log_probability = math.log(1 / probability)
    pi_cost = (
        3 * book_delta / probability
        + 6 * log_delta_value * log_probability / lambda_zero
    )
    q = log_probability + pi_cost
    xi = (
        2 * math.log(2 / beta)
        + 4 * correlation * lambda_zero ** (1 / 3)
        + 12 * correlation * log_delta_value / lambda_zero ** (2 / 3)
    )
    if q >= UP_ONE or 2 * tau * xi >= U_ONE:
        return None

    cap_red = red_capacity(c_eta, q, tau, e_coeff)
    cap_blue = U_ONE - tau * q - rate(1 - tau) - BRANCH_MARGIN
    cap_reservoir = (
        a_coeff * (U_ONE - 2 * tau * xi - BRANCH_MARGIN) / U_ONE
    )
    cap_wedge = 0.99 * e_coeff * tau
    cap = min(cap_red, cap_blue, cap_reservoir, cap_wedge)
    if cap <= a_coeff * tau:
        return None

    result = {
        "gap": cap,
        "eta": eta,
        "p": probability,
        "delta": book_delta,
        "lambda0": lambda_zero,
        "tau": tau,
        "u0": u0,
        "sigma": sigma,
        "epsilon": epsilon,
        "beta": beta,
        "C": correlation,
        "q": q,
        "Xi": xi,
        "A": a_coeff,
        "E": e_coeff,
        "cap_red": cap_red,
        "cap_blue": cap_blue,
        "cap_reservoir": cap_reservoir,
        "cap_wedge": cap_wedge,
        "ratio_margin": ratio_margin,
        "tail_margin": TAIL_MARGIN,
        "degree_margin": tau * degree_slack_parameter,
        "base": math.exp(U_ONE - cap),
    }
    if verbose:
        print(json.dumps(result, indent=2, sort_keys=True))
    return result


def objective(vector: np.ndarray) -> float:
    result = evaluate(vector)
    return 1.0 if result is None else -result["gap"]


def main() -> None:
    bounds = [
        (0.025, 0.034),
        (math.log(1e-5), math.log(2e-4)),
        (math.log(8_000), math.log(30_000)),
        (math.log(2e-4), math.log(9e-4)),
        (2.89, 2.94),
        (math.log(5e-4), math.log(5e-3)),
    ]
    global_result = differential_evolution(
        objective,
        bounds,
        seed=20260812,
        workers=1,
        popsize=24,
        maxiter=700,
        tol=1e-11,
        polish=False,
        updating="immediate",
    )
    local_result = minimize(
        objective,
        global_result.x,
        method="Nelder-Mead",
        options={"maxiter": 50_000, "xatol": 1e-13, "fatol": 1e-16},
    )
    candidate = local_result.x if local_result.fun < global_result.fun else global_result.x
    evaluate(candidate, verbose=True)


if __name__ == "__main__":
    main()
