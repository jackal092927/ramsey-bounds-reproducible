#!/usr/bin/env python3
"""384-bit author checker for the strong-growth retained-spine candidate."""

import json
from pathlib import Path
import flint
from flint import arb, ctx

from check_retained_spine_optimized import (
    ONE, ZERO, hull, prove_concavity, rate, rate_prime,
)

ctx.prec = 384
HERE = Path(__file__).resolve().parent


def main() -> None:
    assert flint.__version__ == "0.9.0"
    payload = json.loads((HERE / "certificate-higher-order-tetradecic-chain-v6.json").read_text())
    assert payload.get("schema") == "corrected-two-sided-ramsey-v1"
    coefficients = [arb(str(x)) for x in payload["target_coefficients"]]
    assert len(coefficients) == 14

    eta = arb("0.0286887")
    probability = arb("0.4713083")
    book_delta = arb("0.00005355")
    lambda_zero = arb(13340)
    tau = arb("0.000686")
    exponent_gap = arb("0.000003445")
    beta = arb(11) / 250
    epsilon = arb(203) / 100000
    correlation = 4 * arb(619) / 250 * (ONE + epsilon)

    c_eta = (arb(2) / (ONE + eta)).log()
    log_delta = (ONE / book_delta).log()
    log_probability = (ONE / probability).log()
    page_cost = log_probability + 3 * book_delta / probability + 6 * log_delta * log_probability / lambda_zero
    rho = (arb(2) / beta).log()
    xi_cost = 2 * rho + 4 * correlation * lambda_zero ** (ONE / 3) + 12 * correlation * log_delta / lambda_zero ** (arb(2) / 3)

    assert ZERO < eta
    assert ZERO < probability < arb("0.5") - eta
    assert ZERO < book_delta <= probability / 4
    assert lambda_zero >= 6 * log_delta
    assert ZERO < tau < ONE

    concavity = prove_concavity(coefficients)
    u_one = rate(ONE, coefficients)
    up_one = rate_prime(ONE, coefficients)
    diagonal = u_one - 2 * c_eta
    off_diagonal = up_one - c_eta
    assert ZERO < diagonal < off_diagonal
    assert page_cost < up_one
    assert 2 * tau * xi_cost < u_one
    degree_slack = tau * (arb("0.5") - eta - probability)
    assert degree_slack > arb("0.000000001")

    r_diag = exponent_gap / diagonal
    r_axis = exponent_gap / off_diagonal
    slope = ONE - diagonal / off_diagonal
    assert ZERO < r_axis < tau < r_diag < ONE
    assert ZERO < slope < ONE

    # Pointwise signs for the easy red directions.
    z_lo = ONE - tau / (ONE - r_diag)
    z_hi = (ONE - tau) / (ONE - r_axis)
    z_box = hull(z_lo, z_hi)
    pr_x = c_eta - rate_prime(z_box, coefficients)
    pr_y = c_eta - rate(z_box, coefficients) + z_box * rate_prime(z_box, coefficients)
    assert pr_x < ZERO
    assert pr_y > ZERO

    # Cellwise sloping-boundary derivative, avoiding interval dependency.
    worst_red_derivative = None
    for cell in range(4096):
        x = hull(r_axis * cell / 4096, r_axis * (cell + 1) / 4096)
        y = r_axis + slope * x
        z = (ONE - tau - x) / (ONE - y)
        derivative = c_eta - rate_prime(z, coefficients) + slope * (
            c_eta - rate(z, coefficients) + z * rate_prime(z, coefficients)
        )
        assert derivative < ZERO, (cell, derivative)
        if worst_red_derivative is None or derivative.upper() > worst_red_derivative.upper():
            worst_red_derivative = derivative

    red_page = c_eta * r_axis + tau * page_cost + (ONE - r_axis) * rate((ONE - tau) / (ONE - r_axis), coefficients)
    red_margin = u_one - exponent_gap - red_page
    assert red_margin > arb("0.000000001")

    assert c_eta - rate_prime(z_box, coefficients) < ZERO
    worst_blue_derivative = None
    for cell in range(4096):
        x = hull(r_diag * cell / 4096, r_diag * (cell + 1) / 4096)
        denominator = ONE - x
        z = ONE - tau / denominator
        derivative = 2 * c_eta - rate(z, coefficients) - tau / denominator * rate_prime(z, coefficients)
        assert derivative < ZERO, (cell, derivative)
        if worst_blue_derivative is None or derivative.upper() > worst_blue_derivative.upper():
            worst_blue_derivative = derivative

    blue_page = tau * page_cost + rate(ONE - tau, coefficients)
    blue_margin = u_one - exponent_gap - blue_page
    assert blue_margin > arb("0.000000001")

    reservoir = 2 * c_eta * r_diag + 2 * tau * xi_cost
    reservoir_margin = u_one - exponent_gap - reservoir
    assert reservoir_margin > arb("0.000000001")

    base = (u_one - exponent_gap).exp()
    safe_decimal = arb("3.780685405")
    rounding_margin = safe_decimal - base
    assert safe_decimal < arb("3.780685745")
    assert rounding_margin > arb("0.000000001")

    print("PASS: retained spine with strong correlation growth")
    print(f"precision_bits: {ctx.prec}")
    print(f"global_concavity_worst_upper: {concavity.upper()}")
    print(f"beta: {beta}")
    print(f"correlation_C: {correlation}")
    print(f"rho: {rho}")
    print(f"q: {page_cost}")
    print(f"Xi: {xi_cost}")
    print(f"degree_slack: {degree_slack}")
    print(f"worst_red_boundary_derivative_upper: {worst_red_derivative.upper()}")
    print(f"red_page_margin: {red_margin}")
    print(f"worst_blue_diagonal_derivative_upper: {worst_blue_derivative.upper()}")
    print(f"blue_page_margin: {blue_margin}")
    print(f"reservoir_margin: {reservoir_margin}")
    print(f"exponent_gap: {exponent_gap}")
    print(f"base_upper: {base}")
    print(f"safe_decimal_upper: {safe_decimal}")
    print(f"rounding_margin: {rounding_margin}")


if __name__ == "__main__":
    main()
