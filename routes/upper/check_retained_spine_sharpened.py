#!/usr/bin/env python3
"""384-bit Arb certificate using the specialized correlation constants."""

from __future__ import annotations

import hashlib
import json
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


ctx.prec = 384
HERE = Path(__file__).resolve().parent

UPSTREAM_SHA256 = {
    "RETAINED_SPINE_TRANSFER_ATTEMPT.md":
        "5aa5d6cb1ee1cc2d9f4d34b8564b6c57f78cfd7444a89abcfbb64542274e4aaa",
    "INDEPENDENT_RETAINED_SPINE_REFEREE.md":
        "6ba57fdbe13bf45255644ae94af5474b7a34afda3aefeda26415f3cc3f9b66db",
    "certificate-higher-order-tetradecic-chain-v6.json":
        "8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8",
    "check_retained_spine_optimized.py":
        "4c38c953f2aa541def665467b59dd8e05d8ea6a32f4e5f5b19f7ddf556e373c8",
    "SPECIALIZED_CORRELATION_SHARPENING.md":
        "c28026ed8d30e0c4096ccc46e3cc04d7026fa2c2975eab4a2537a9021a866ebe",
    "check_specialized_correlation.py":
        "be17cc0848a54e606b4ad4bc3393b8ac317f030306c239d41bd0f90f38c5724a",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    assert flint.__version__ == "0.9.0"
    for name, expected in UPSTREAM_SHA256.items():
        actual = sha256(HERE / name)
        assert actual == expected, f"changed dependency {name}: {actual}"

    payload = json.loads(
        (HERE / "certificate-higher-order-tetradecic-chain-v6.json")
        .read_text(encoding="utf-8")
    )
    assert payload.get("schema") == "corrected-two-sided-ramsey-v1"
    coefficients = [arb(str(value)) for value in payload["target_coefficients"]]
    assert len(coefficients) == 14

    # Exact terminating-decimal retained-spine parameters.
    eta = arb("0.028681")
    probability = arb("0.471309")
    book_delta = arb("0.0000528")
    lambda_zero = arb("13520")
    tau = arb("0.000572")
    exponent_gap = arb("0.00000287")

    # Exact specialized correlation pair from the new lemma.
    beta = arb(1) / 1000000
    correlation = arb(145261) / 12500

    c_eta = (arb(2) / (ONE + eta)).log()
    log_delta = (ONE / book_delta).log()
    log_probability = (ONE / probability).log()
    pi_cost = (
        3 * book_delta / probability
        + 6 * log_delta * log_probability / lambda_zero
    )
    page_cost = log_probability + pi_cost
    rho = (arb(2) / beta).log()
    xi_cost = (
        2 * rho
        + 4 * correlation * lambda_zero ** (ONE / 3)
        + 12 * correlation * log_delta
        / lambda_zero ** (arb(2) / 3)
    )

    # Parameterized Yang--Mao book gates.
    assert ZERO < eta
    assert ZERO < probability < arb("0.5") - eta
    assert ZERO < book_delta <= probability / 4
    assert book_delta <= arb("0.25")
    assert lambda_zero >= 2
    assert lambda_zero >= 6 * log_delta
    assert ZERO < tau < ONE
    assert ZERO < beta <= ONE
    assert ZERO < correlation

    concavity_upper = prove_concavity(coefficients)
    u_one = rate(ONE, coefficients)
    up_one = rate_prime(ONE, coefficients)
    diagonal_coefficient = u_one - 2 * c_eta
    off_diagonal_coefficient = up_one - c_eta
    assert ZERO < diagonal_coefficient < off_diagonal_coefficient
    assert page_cost < up_one
    assert 2 * tau * xi_cost < u_one
    degree_slack = tau * (arb("0.5") - eta - probability)
    assert degree_slack > ZERO

    # Direct tangent wedge G <= exponent_gap.
    r_diag = exponent_gap / diagonal_coefficient
    r_axis = exponent_gap / off_diagonal_coefficient
    boundary_slope = ONE - diagonal_coefficient / off_diagonal_coefficient
    assert ZERO < r_axis < tau < r_diag < ONE
    assert ZERO < boundary_slope < ONE

    # Red-page branch: increasing in y, decreasing on the sloping boundary.
    z_lo = ONE - tau / (ONE - r_diag)
    z_hi = (ONE - tau) / (ONE - r_axis)
    z_box = hull(z_lo, z_hi)
    assert ZERO < z_lo < z_hi < ONE
    pr_x = c_eta - rate_prime(z_box, coefficients)
    pr_y = c_eta - rate(z_box, coefficients) + z_box * rate_prime(
        z_box, coefficients
    )
    pr_boundary = pr_x + boundary_slope * pr_y
    assert pr_x < ZERO
    assert pr_y > ZERO
    assert pr_boundary < ZERO

    axis_ratio = (ONE - tau) / (ONE - r_axis)
    page_axis = (
        c_eta * r_axis
        + tau * page_cost
        + (ONE - r_axis) * rate(axis_ratio, coefficients)
    )
    page_margin = u_one - exponent_gap - page_axis
    assert page_margin > arb("0.000000001")

    # Blue-page branch: reduce first to the diagonal and then to the origin.
    x_box = hull(ZERO, r_diag)
    one_minus_x = ONE - x_box
    diagonal_ratio = ONE - tau / one_minus_x
    pb_y = c_eta - rate_prime(z_box, coefficients)
    pb_diagonal = (
        2 * c_eta
        - rate(diagonal_ratio, coefficients)
        - tau / one_minus_x * rate_prime(diagonal_ratio, coefficients)
    )
    assert pb_y < ZERO
    assert pb_diagonal < ZERO
    page_origin = tau * page_cost + rate(ONE - tau, coefficients)
    other_page_margin = u_one - exponent_gap - page_origin
    assert other_page_margin > arb("0.000000001")

    # Reservoir cost is coordinatewise increasing and the wedge maximizes
    # x+y at its diagonal endpoint.
    reservoir_corner = 2 * c_eta * r_diag + 2 * tau * xi_cost
    reservoir_margin = u_one - exponent_gap - reservoir_corner
    assert reservoir_margin > arb("0.000000001")

    exponent_upper = u_one - exponent_gap
    base_upper = exponent_upper.exp()
    decimal_upper = arb("3.780687577208")
    rounding_margin = decimal_upper - base_upper
    assert rounding_margin > arb("0.000000000000001")

    print("PASS: retained-spine certificate with sharpened correlation")
    print(f"precision_bits: {ctx.prec}")
    print(f"global_concavity_worst_upper: {concavity_upper.upper()}")
    print(f"beta: {beta}")
    print(f"correlation_C: {correlation}")
    print(f"rho=log(2/beta): {rho}")
    print(f"Pi: {pi_cost}")
    print(f"q: {page_cost}")
    print(f"Xi: {xi_cost}")
    print(f"degree_slack: {degree_slack}")
    print(f"A: {diagonal_coefficient}")
    print(f"E: {off_diagonal_coefficient}")
    print(f"r_axis: {r_axis}")
    print(f"r_diag: {r_diag}")
    print(f"P_R_dx_upper: {pr_x.upper()}")
    print(f"P_R_dy_lower: {pr_y.lower()}")
    print(f"P_R_boundary_derivative_upper: {pr_boundary.upper()}")
    print(f"page_margin: {page_margin}")
    print(f"P_B_diagonal_derivative_upper: {pb_diagonal.upper()}")
    print(f"other_page_margin: {other_page_margin}")
    print(f"reservoir_margin: {reservoir_margin}")
    print(f"exponent_gap: {exponent_gap}")
    print(f"base_upper: {base_upper}")
    print(f"safe_decimal_upper: {decimal_upper}")
    print(f"rounding_margin: {rounding_margin}")


if __name__ == "__main__":
    main()
