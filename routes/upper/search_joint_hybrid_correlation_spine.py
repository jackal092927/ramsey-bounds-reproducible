#!/usr/bin/env python3
"""Exploratory search using the exact/analytic hybrid correlation separator.

The finite interval ``u in [u0, 2.9]`` is intended for a later cellwise Arb
proof of monotonicity of the exact root-filter ratio.  The half-line
``u >= 2.9`` is handled by the same analytic envelope as the frozen proof.
This search is heuristic only; its output must be rationalized and replayed.
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

RATIO_MARGIN = 2.0e-9
TAIL_MARGIN = 2.0e-9
DEGREE_MARGIN = 2.0e-9
BRANCH_MARGIN = 2.0e-9
TAIL_SWITCH = 2.9


def polynomial(x: float) -> float:
    return float(COEFFICIENTS @ (x ** np.arange(1, len(COEFFICIENTS) + 1)))


def polynomial_prime(x: float) -> float:
    d = np.arange(1, len(COEFFICIENTS) + 1)
    return float((d * COEFFICIENTS) @ (x ** (d - 1)))


def rate(x: float) -> float:
    return (1 + x) * math.log1p(x) - x * math.log(x) + polynomial(x) * math.exp(-x)


def rate_prime(x: float) -> float:
    return math.log((1 + x) / x) + (polynomial_prime(x) - polynomial(x)) * math.exp(-x)


U_ONE = rate(1.0)
UP_ONE = rate_prime(1.0)


def exact_ratio(u: float, u0: float) -> float:
    a = math.exp(-u0)
    theta = math.sqrt(3) * u / 2
    positive = (math.exp(u) + 2 * math.exp(-u / 2) * math.cos(theta)) / 3
    negative = (math.exp(-u) + 2 * math.exp(u / 2) * math.cos(theta)) / 3
    return (1 + a * positive * positive) / (1 + a * negative * negative)


def envelope_ratio(u: float, u0: float) -> float:
    a = math.exp(-u0)
    positive = (math.exp(u) - 2 * math.exp(-u / 2)) / 3
    negative = (2 * math.exp(u / 2) + math.exp(-u)) / 3
    return (1 + a * positive * positive) / (1 + a * negative * negative)


def correlation_parameters(u0: float, epsilon: float) -> tuple[float, ...] | None:
    endpoint = exact_ratio(u0, u0)
    tail_endpoint = envelope_ratio(TAIL_SWITCH, u0)
    binding_ratio = min(endpoint, tail_endpoint)
    sigma = (binding_ratio - 2 - RATIO_MARGIN) / 2
    if sigma <= TAIL_MARGIN:
        return None

    denominator = sigma + 4 * (1 + 2 / epsilon)
    beta = (sigma - TAIL_MARGIN) / denominator
    if not (0 < beta < 1):
        return None

    target = 2 + 2 * sigma
    u = TAIL_SWITCH
    derivative = (
        2 * math.exp(u) * (math.exp(u) - 2 * target)
        - 2 * math.exp(u / 2) - 4 * math.exp(-u)
    )
    derivative_second = (
        4 * math.exp(2 * u) - 4 * target * math.exp(u)
        - math.exp(u / 2) + 4 * math.exp(-u)
    )
    if min(derivative, derivative_second) <= 0:
        return None
    correlation = 4 * u0 * (1 + epsilon)
    return sigma, beta, correlation, endpoint - target, tail_endpoint - target


def red_capacity(c_eta: float, q: float, tau: float, e_coeff: float) -> float:
    def margin(gap: float) -> float:
        r_axis = gap / e_coeff
        z = (1 - tau) / (1 - r_axis)
        page = c_eta * r_axis + tau * q + (1 - r_axis) * rate(z)
        return U_ONE - gap - page - BRANCH_MARGIN

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
    p = 0.5 - eta - DEGREE_MARGIN / tau
    if p <= 0 or book_delta > min(0.25, p / 4):
        return None
    if lambda_zero < max(2.0, 6 * math.log(1 / book_delta)):
        return None

    corr = correlation_parameters(u0, epsilon)
    if corr is None:
        return None
    sigma, beta, correlation, exact_slack, envelope_slack = corr

    c_eta = math.log(2 / (1 + eta))
    a_coeff = U_ONE - 2 * c_eta
    e_coeff = UP_ONE - c_eta
    if not (0 < a_coeff < e_coeff):
        return None

    log_delta_value = math.log(1 / book_delta)
    log_probability = math.log(1 / p)
    pi = 3 * book_delta / p + 6 * log_delta_value * log_probability / lambda_zero
    q = log_probability + pi
    xi = (
        2 * math.log(2 / beta)
        + 4 * correlation * lambda_zero ** (1 / 3)
        + 12 * correlation * log_delta_value / lambda_zero ** (2 / 3)
    )
    if q >= UP_ONE or 2 * tau * xi >= U_ONE:
        return None

    cap_red = red_capacity(c_eta, q, tau, e_coeff)
    cap_blue = U_ONE - tau * q - rate(1 - tau) - BRANCH_MARGIN
    cap_reservoir = a_coeff * (U_ONE - 2 * tau * xi - BRANCH_MARGIN) / U_ONE
    cap_wedge = 0.99 * e_coeff * tau
    gap = min(cap_red, cap_blue, cap_reservoir, cap_wedge)
    if gap <= a_coeff * tau:
        return None

    answer = {
        "gap": gap,
        "base": math.exp(U_ONE - gap),
        "eta": eta,
        "p": p,
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
        "exact_ratio_slack": exact_slack,
        "envelope_ratio_slack": envelope_slack,
        "tail_margin": TAIL_MARGIN,
        "degree_margin": tau * (0.5 - eta - p),
    }
    if verbose:
        print(json.dumps(answer, indent=2, sort_keys=True))
    return answer


def objective(vector: np.ndarray) -> float:
    value = evaluate(vector)
    return 1.0 if value is None else -value["gap"]


def main() -> None:
    bounds = [
        (0.026, 0.033),
        (math.log(1e-5), math.log(2e-4)),
        (math.log(8_000), math.log(30_000)),
        (math.log(3e-4), math.log(1.2e-3)),
        (2.471, 2.50),
        (math.log(5e-4), math.log(5e-3)),
    ]
    global_result = differential_evolution(
        objective,
        bounds,
        seed=2026081202,
        workers=1,
        popsize=28,
        maxiter=900,
        tol=1e-11,
        polish=False,
    )
    local_result = minimize(
        objective,
        global_result.x,
        method="Nelder-Mead",
        options={"maxiter": 80_000, "xatol": 1e-13, "fatol": 1e-16},
    )
    candidate = local_result.x if local_result.fun < global_result.fun else global_result.x
    evaluate(candidate, verbose=True)


if __name__ == "__main__":
    main()
