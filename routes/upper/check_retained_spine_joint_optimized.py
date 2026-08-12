#!/usr/bin/env python3
"""384-bit Arb certificate for the hybrid-correlation retained spine."""

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
    "HYBRID_CORRELATION_SHARPENING.md":
        "4b29c692dd1fc96859491b25d61c9b0e1124a33cf57a45ef01abb5a2e49ed30d",
    "check_hybrid_correlation.py":
        "a620937acd6770f622fc799fe28e5dcd6f0ebf072e395bc16d81220e1c02fc30",
    "RETAINED_SPINE_JOINT_OPTIMIZED_CERTIFICATE.md":
        "34118932b873f5f08fcd81b640882344a564e2d39efd8451ec18c390b0e69fe0",
}


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            value.update(block)
    return value.hexdigest()


def main() -> None:
    assert flint.__version__ == "0.9.0"
    for name, expected in UPSTREAM_SHA256.items():
        actual = digest(HERE / name)
        assert actual == expected, (name, actual, expected)

    payload = json.loads(
        (HERE / "certificate-higher-order-tetradecic-chain-v6.json")
        .read_text(encoding="utf-8")
    )
    assert payload.get("schema") == "corrected-two-sided-ramsey-v1"
    coefficients = [arb(str(value)) for value in payload["target_coefficients"]]
    assert len(coefficients) == 14

    # Exact terminating-decimal retained-spine tuple.
    eta = arb("0.028688")
    probability = arb("0.471310")
    book_delta = arb("0.0000525")
    lambda_zero = arb(13580)
    tau = arb("0.000665")
    exponent_gap = arb("0.000003355")

    # Exact hybrid correlation pair.
    beta = arb(1) / 4_000_000
    correlation = arb(6_202_999) / 625_000

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
        + 12 * correlation * log_delta / lambda_zero ** (arb(2) / 3)
    )

    # Parameterized Yang--Mao gates.
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
    degree_parameter_slack = arb("0.5") - eta - probability
    degree_slack = tau * degree_parameter_slack
    assert degree_slack > arb("0.000000001")

    # Complete direct-branch complement G <= exponent_gap.
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
    red_page = (
        c_eta * r_axis
        + tau * page_cost
        + (ONE - r_axis) * rate(axis_ratio, coefficients)
    )
    red_page_margin = u_one - exponent_gap - red_page
    assert red_page_margin > arb("0.000000001")

    # Blue-page branch: first reduce to the diagonal, then to the origin.
    x_box = hull(ZERO, r_diag)
    denominator = ONE - x_box
    diagonal_ratio = ONE - tau / denominator
    pb_y = c_eta - rate_prime(z_box, coefficients)
    pb_diagonal = (
        2 * c_eta
        - rate(diagonal_ratio, coefficients)
        - tau / denominator * rate_prime(diagonal_ratio, coefficients)
    )
    assert pb_y < ZERO
    assert pb_diagonal < ZERO
    blue_page = tau * page_cost + rate(ONE - tau, coefficients)
    blue_page_margin = u_one - exponent_gap - blue_page
    assert blue_page_margin > arb("0.000000001")

    # Reservoir is coordinatewise increasing; x+y is maximal at r_diag.
    reservoir = 2 * c_eta * r_diag + 2 * tau * xi_cost
    reservoir_margin = u_one - exponent_gap - reservoir
    assert reservoir_margin > arb("0.000000001")

    exponent_upper = u_one - exponent_gap
    base_upper = exponent_upper.exp()
    safe_decimal = arb("3.780685745")
    preregistered_threshold = arb("3.7806870")
    rounding_margin = safe_decimal - base_upper
    assert safe_decimal < preregistered_threshold
    assert rounding_margin > arb("0.000000001")

    print("PASS: jointly optimized hybrid-correlation retained spine")
    print(f"precision_bits: {ctx.prec}")
    print(f"global_concavity_worst_upper: {concavity_upper.upper()}")
    print(f"beta: {beta}")
    print(f"correlation_C: {correlation}")
    print(f"rho=log(2/beta): {rho}")
    print(f"Pi: {pi_cost}")
    print(f"q: {page_cost}")
    print(f"Xi: {xi_cost}")
    print(f"degree_parameter_slack: {degree_parameter_slack}")
    print(f"degree_slack: {degree_slack}")
    print(f"A: {diagonal_coefficient}")
    print(f"E: {off_diagonal_coefficient}")
    print(f"r_axis: {r_axis}")
    print(f"r_diag: {r_diag}")
    print(f"P_R_dx_upper: {pr_x.upper()}")
    print(f"P_R_dy_lower: {pr_y.lower()}")
    print(f"P_R_boundary_derivative_upper: {pr_boundary.upper()}")
    print(f"red_page_margin: {red_page_margin}")
    print(f"P_B_dy_upper: {pb_y.upper()}")
    print(f"P_B_diagonal_derivative_upper: {pb_diagonal.upper()}")
    print(f"blue_page_margin: {blue_page_margin}")
    print(f"reservoir_margin: {reservoir_margin}")
    print(f"exponent_gap: {exponent_gap}")
    print(f"base_upper: {base_upper}")
    print(f"safe_decimal_upper: {safe_decimal}")
    print(f"rounding_margin: {rounding_margin}")


if __name__ == "__main__":
    main()
