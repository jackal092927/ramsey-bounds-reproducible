#!/usr/bin/env python3
"""512-bit author checker for the u0=309/125 retained-spine candidate."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import flint
from flint import arb, ctx

from check_retained_spine_optimized import (
    ONE,
    ZERO,
    hull,
    prove_concavity,
    rate,
    rate_prime,
)


ctx.prec = 512
HERE = Path(__file__).resolve().parent


def q(numerator: int, denominator: int = 1) -> arb:
    return arb(numerator) / denominator


def main() -> None:
    assert flint.__version__ == "0.9.0"
    payload = json.loads(
        (HERE / "certificate-higher-order-tetradecic-chain-v6.json")
        .read_text(encoding="utf-8")
    )
    assert payload.get("schema") == "corrected-two-sided-ramsey-v1"
    coefficients = [arb(str(value)) for value in payload["target_coefficients"]]
    assert len(coefficients) == 14

    # Every decimal below is an exact terminating rational.
    eta = q(2_868_925, 100_000_000)
    probability = q(47_130_784, 100_000_000)
    book_delta = q(53_934, 1_000_000_000)
    lambda_zero = q(13_235)
    tau = q(69_374, 100_000_000)
    exponent_gap = q(34_727, 10_000_000_000)

    u0_f = Fraction(309, 125)
    epsilon_f = Fraction(7113, 10_000_000)
    beta_f = Fraction(833, 1250)
    correlation_f = Fraction(3_092_197_917, 312_500_000)
    assert correlation_f == 4 * u0_f * (1 + epsilon_f)
    beta = q(beta_f.numerator, beta_f.denominator)
    correlation = q(correlation_f.numerator, correlation_f.denominator)

    c_eta = (2 / (ONE + eta)).log()
    log_delta = (ONE / book_delta).log()
    log_probability = (ONE / probability).log()
    page_cost = (
        log_probability
        + 3 * book_delta / probability
        + 6 * log_delta * log_probability / lambda_zero
    )
    rho = (2 / beta).log()
    xi_cost = (
        2 * rho
        + 4 * correlation * lambda_zero ** (ONE / 3)
        + 12 * correlation * log_delta / lambda_zero ** (q(2, 3))
    )

    # Source-level scalar gates.
    assert ZERO < eta
    assert ZERO < probability < ONE / 2 - eta
    assert ZERO < book_delta <= probability / 4
    assert book_delta <= ONE / 4
    assert lambda_zero >= 2
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

    degree_slack = tau * (ONE / 2 - eta - probability)
    assert degree_slack > q(1, 1_000_000_000)

    r_diag = exponent_gap / diagonal
    r_axis = exponent_gap / off_diagonal
    slope = ONE - diagonal / off_diagonal
    assert ZERO < r_axis < tau < r_diag < ONE
    assert ZERO < slope < ONE

    # Ordered red wedge.  The sign pattern plus concavity reduces it to the
    # sloping boundary; a cellwise derivative proof then reduces to x=0.
    z_lo = ONE - tau / (ONE - r_diag)
    z_hi = (ONE - tau) / (ONE - r_axis)
    z_box = hull(z_lo, z_hi)
    partial_x = c_eta - rate_prime(z_box, coefficients)
    partial_y = (
        c_eta - rate(z_box, coefficients)
        + z_box * rate_prime(z_box, coefficients)
    )
    assert partial_x < ZERO
    assert partial_y > ZERO

    derivative_cells = 8192
    red_derivative_worst = None
    for cell in range(derivative_cells):
        x = hull(r_axis * cell / derivative_cells,
                 r_axis * (cell + 1) / derivative_cells)
        y = r_axis + slope * x
        z = (ONE - tau - x) / (ONE - y)
        derivative = c_eta - rate_prime(z, coefficients) + slope * (
            c_eta - rate(z, coefficients) + z * rate_prime(z, coefficients)
        )
        assert derivative < ZERO, (cell, derivative)
        if (red_derivative_worst is None
                or derivative.upper() > red_derivative_worst.upper()):
            red_derivative_worst = derivative

    red_page = (
        c_eta * r_axis + tau * page_cost
        + (ONE - r_axis)
        * rate((ONE - tau) / (ONE - r_axis), coefficients)
    )
    red_margin = u_one - exponent_gap - red_page
    assert red_margin > q(1, 1_000_000_000)

    # Ordered blue wedge; monotonicity reduces it to the diagonal, and the
    # derivative check reduces the diagonal to the origin.
    blue_derivative_worst = None
    for cell in range(derivative_cells):
        x = hull(r_diag * cell / derivative_cells,
                 r_diag * (cell + 1) / derivative_cells)
        denominator = ONE - x
        z = ONE - tau / denominator
        derivative = (
            2 * c_eta - rate(z, coefficients)
            - tau / denominator * rate_prime(z, coefficients)
        )
        assert derivative < ZERO, (cell, derivative)
        if (blue_derivative_worst is None
                or derivative.upper() > blue_derivative_worst.upper()):
            blue_derivative_worst = derivative

    blue_page = tau * page_cost + rate(ONE - tau, coefficients)
    blue_margin = u_one - exponent_gap - blue_page
    assert blue_margin > q(1, 1_000_000_000)

    reservoir = 2 * c_eta * r_diag + 2 * tau * xi_cost
    reservoir_margin = u_one - exponent_gap - reservoir
    assert reservoir_margin > q(1, 1_000_000_000)

    base = (u_one - exponent_gap).exp()
    safe_decimal = q(3_780_685_300, 1_000_000_000)
    previous_safe_decimal = q(3_780_685_320, 1_000_000_000)
    rounding_margin = safe_decimal - base
    safe_improvement = previous_safe_decimal - safe_decimal
    assert rounding_margin > q(1, 1_000_000_000)
    assert safe_improvement >= q(1, 100_000_000)

    print("PASS: 512-bit u0=309/125 retained-spine candidate")
    print(f"precision_bits: {ctx.prec}")
    print(f"global_concavity_worst_upper: {concavity.upper()}")
    print(f"beta: {beta_f}")
    print(f"epsilon: {epsilon_f}")
    print(f"correlation_C_exact: {correlation_f}")
    print(f"rho: {rho}")
    print(f"q: {page_cost}")
    print(f"Xi: {xi_cost}")
    print(f"degree_slack: {degree_slack}")
    print(f"red_boundary_derivative_worst_upper: {red_derivative_worst.upper()}")
    print(f"red_page_margin: {red_margin}")
    print(f"blue_diagonal_derivative_worst_upper: {blue_derivative_worst.upper()}")
    print(f"blue_page_margin: {blue_margin}")
    print(f"reservoir_margin: {reservoir_margin}")
    print(f"exponent_gap: {exponent_gap}")
    print(f"base_upper: {base}")
    print(f"safe_decimal_upper: {safe_decimal}")
    print(f"rounding_margin: {rounding_margin}")
    print(f"safe_improvement_over_3.780685320: {safe_improvement}")


if __name__ == "__main__":
    main()
