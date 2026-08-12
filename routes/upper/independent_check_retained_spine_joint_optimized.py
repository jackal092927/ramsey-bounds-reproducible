#!/usr/bin/env python3
"""Independent 512-bit replay of the joint hybrid-correlation candidate.

This file imports neither author checker.  It uses a different polynomial
representation, four times as many finite-correlation cells, a finer global
concavity partition, and cellwise replays of both fragile page derivatives.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import flint
from flint import arb, ctx


ctx.prec = 512
HERE = Path(__file__).resolve().parent
ZERO = arb(0)
ONE = arb(1)

AUTHOR_SHA256 = {
    "HYBRID_CORRELATION_SHARPENING.md":
        "4b29c692dd1fc96859491b25d61c9b0e1124a33cf57a45ef01abb5a2e49ed30d",
    "check_hybrid_correlation.py":
        "a620937acd6770f622fc799fe28e5dcd6f0ebf072e395bc16d81220e1c02fc30",
    "RETAINED_SPINE_JOINT_OPTIMIZED_CERTIFICATE.md":
        "34118932b873f5f08fcd81b640882344a564e2d39efd8451ec18c390b0e69fe0",
    "check_retained_spine_joint_optimized.py":
        "f9fc324c7199cce760f7b59e011e4a2364473b6e9168870eab5f7ff91397e3cb",
    "RETAINED_SPINE_TRANSFER_ATTEMPT.md":
        "5aa5d6cb1ee1cc2d9f4d34b8564b6c57f78cfd7444a89abcfbb64542274e4aaa",
    "INDEPENDENT_RETAINED_SPINE_REFEREE.md":
        "6ba57fdbe13bf45255644ae94af5474b7a34afda3aefeda26415f3cc3f9b66db",
    "certificate-higher-order-tetradecic-chain-v6.json":
        "8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8",
}


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            value.update(block)
    return value.hexdigest()


def interval(lo: arb, hi: arb) -> arb:
    return lo.union(hi)


def horner(coefficients: list[arb], x: arb) -> arb:
    value = ZERO
    for coefficient in reversed(coefficients):
        value = value * x + coefficient
    return value


def polynomial(coefficients: list[arb], x: arb) -> arb:
    return x * horner(coefficients, x)


def polynomial_prime(coefficients: list[arb], x: arb) -> arb:
    derived = [(index + 1) * value for index, value in enumerate(coefficients)]
    return horner(derived, x)


def polynomial_second(coefficients: list[arb], x: arb) -> arb:
    derived = [
        (index + 2) * (index + 1) * coefficients[index + 1]
        for index in range(len(coefficients) - 1)
    ]
    return horner(derived, x)


def rate(coefficients: list[arb], x: arb) -> arb:
    entropy = (ONE + x) * (ONE + x).log() - x * x.log()
    return entropy + polynomial(coefficients, x) * (-x).exp()


def rate_prime(coefficients: list[arb], x: arb) -> arb:
    poly = polynomial(coefficients, x)
    return ((ONE + x) / x).log() + (
        polynomial_prime(coefficients, x) - poly
    ) * (-x).exp()


def rate_second(coefficients: list[arb], x: arb) -> arb:
    poly = polynomial(coefficients, x)
    return -ONE / (x * (ONE + x)) + (
        polynomial_second(coefficients, x)
        - 2 * polynomial_prime(coefficients, x)
        + poly
    ) * (-x).exp()


def prove_concavity(coefficients: list[arb]) -> arb:
    split = ONE / 65536
    near_zero = interval(ZERO, split)
    correction = (
        polynomial_second(coefficients, near_zero)
        - 2 * polynomial_prime(coefficients, near_zero)
        + polynomial(coefficients, near_zero)
    ) * (-near_zero).exp()
    worst = -ONE / (split * (ONE + split)) + correction
    assert worst < ZERO

    for cell in range(65536):
        lo = split + (ONE - split) * cell / 65536
        hi = split + (ONE - split) * (cell + 1) / 65536
        value = rate_second(coefficients, interval(lo, hi))
        assert value < ZERO, (cell, value)
        if value.upper() > worst.upper():
            worst = value
    return worst


def exact_root_filter_values(u: arb) -> tuple[arb, arb, arb, arb]:
    root_three = arb(3).sqrt()
    theta = root_three * u / 2
    cosine = theta.cos()
    sine = theta.sin()
    exp_u = u.exp()
    exp_minus_u = (-u).exp()
    exp_half = (u / 2).exp()
    exp_minus_half = (-u / 2).exp()
    plus = (exp_u + 2 * exp_minus_half * cosine) / 3
    minus = (exp_minus_u + 2 * exp_half * cosine) / 3
    plus_derivative = (
        exp_u - exp_minus_half * cosine
        - root_three * exp_minus_half * sine
    ) / 3
    minus_derivative = (
        -exp_minus_u + exp_half * cosine
        - root_three * exp_half * sine
    ) / 3
    return plus, minus, plus_derivative, minus_derivative


def replay_hybrid_correlation() -> dict[str, arb | Fraction]:
    u0 = arb(619) / 250
    switch = arb(29) / 10
    target = Fraction(1001, 500)
    sigma = Fraction(1, 1000)
    beta = Fraction(1, 4_000_000)
    epsilon = Fraction(21, 10_000)
    target_arb = arb(target.numerator) / target.denominator
    a = (-u0).exp()

    # Direct endpoint replay.
    plus, minus, _, _ = exact_root_filter_values(u0)
    endpoint_slack = (
        (ONE + a * plus**2) / (ONE + a * minus**2) - target_arb
    )
    assert endpoint_slack > arb("0.0001")

    # 16,384 cells, versus 4,096 in the author checker.  Work with the
    # numerator after deleting the common strictly positive factor 2a.
    worst_numerator = None
    for cell in range(16384):
        lo = u0 + (switch - u0) * cell / 16384
        hi = u0 + (switch - u0) * (cell + 1) / 16384
        u = interval(lo, hi)
        plus, minus, plus_prime, minus_prime = exact_root_filter_values(u)
        h_plus = ONE + a * plus**2
        h_minus = ONE + a * minus**2
        numerator = (
            plus * plus_prime * h_minus
            - minus * minus_prime * h_plus
        )
        assert numerator > ZERO, (cell, numerator)
        if worst_numerator is None or numerator.lower() < worst_numerator.lower():
            worst_numerator = numerator
    assert worst_numerator is not None

    # Direct half-line-envelope endpoint replay, without the author's
    # expanded K implementation.
    exp_u = switch.exp()
    exp_half = (switch / 2).exp()
    exp_minus_u = (-switch).exp()
    exp_minus_half = (-switch / 2).exp()
    positive_lower = (exp_u - 2 * exp_minus_half) / 3
    negative_upper = (2 * exp_half + exp_minus_u) / 3
    assert positive_lower > ZERO
    envelope_slack = (
        (ONE + a * positive_lower**2)
        - target_arb * (ONE + a * negative_upper**2)
    )
    assert envelope_slack > arb("0.3")
    derivative_lower = (
        2 * exp_u * (exp_u - 2 * target_arb)
        - 2 * exp_half - 4 * exp_minus_u
    )
    derivative_second_lower = (
        4 * exp_u**2 - 4 * target_arb * exp_u
        - exp_half + 4 * exp_minus_u
    )
    assert exp_u > 18
    assert derivative_lower > ZERO
    assert derivative_second_lower > ZERO

    tail_cost = 4 * beta * (1 + Fraction(2, 1) / epsilon)
    tail_credit = sigma * (1 - beta)
    assert tail_cost == Fraction(20021, 21_000_000)
    assert tail_credit == Fraction(3_999_999, 4_000_000_000)
    assert tail_credit - tail_cost > Fraction(1, 100_000)

    return {
        "endpoint_ratio_slack": endpoint_slack,
        "finite_derivative_numerator_worst": worst_numerator,
        "tail_envelope_crossmultiplied_slack": envelope_slack,
        "tail_derivative_lower": derivative_lower,
        "tail_derivative_second_lower": derivative_second_lower,
        "tail_cost": tail_cost,
        "tail_credit": tail_credit,
    }


def main() -> None:
    assert flint.__version__ == "0.9.0"
    for name, expected in AUTHOR_SHA256.items():
        actual = digest(HERE / name)
        assert actual == expected, (name, actual, expected)

    correlation = replay_hybrid_correlation()

    payload = json.loads(
        (HERE / "certificate-higher-order-tetradecic-chain-v6.json")
        .read_text(encoding="utf-8")
    )
    assert payload["schema"] == "corrected-two-sided-ramsey-v1"
    coefficients = [arb(str(value)) for value in payload["target_coefficients"]]
    assert len(coefficients) == 14

    eta = arb(28688) / 1_000_000
    probability = arb(471310) / 1_000_000
    book_delta = arb(525) / 10_000_000
    lambda_zero = arb(13580)
    tau = arb(665) / 1_000_000
    gap = arb(3355) / 1_000_000_000
    beta = arb(1) / 4_000_000
    correlation_constant = arb(6_202_999) / 625_000

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
        + 4 * correlation_constant * lambda_zero ** (ONE / 3)
        + 12 * correlation_constant * log_delta
        / lambda_zero ** (arb(2) / 3)
    )

    assert ZERO < eta
    assert ZERO < probability < ONE / 2 - eta
    assert ZERO < book_delta <= probability / 4
    assert book_delta <= ONE / 4
    assert lambda_zero >= 2
    assert lambda_zero >= 6 * log_delta
    assert ZERO < tau < ONE
    degree_slack = tau * (ONE / 2 - eta - probability)
    assert degree_slack > arb("0.000000001")

    concavity = prove_concavity(coefficients)
    u_one = rate(coefficients, ONE)
    up_one = rate_prime(coefficients, ONE)
    diagonal = u_one - 2 * c_eta
    off_diagonal = up_one - c_eta
    assert ZERO < diagonal < off_diagonal
    assert page_cost < up_one
    assert 2 * tau * xi_cost < u_one

    r_diag = gap / diagonal
    r_axis = gap / off_diagonal
    slope = ONE - diagonal / off_diagonal
    assert ZERO < r_axis < tau < r_diag < ONE
    assert ZERO < slope < ONE

    z_lo = ONE - tau / (ONE - r_diag)
    z_hi = (ONE - tau) / (ONE - r_axis)
    assert ZERO < z_lo < z_hi < ONE

    # Concavity supplies monotone endpoint checks for the coordinate signs.
    red_x_upper = c_eta - rate_prime(coefficients, z_hi)
    red_y_lower = (
        c_eta - rate(coefficients, z_hi)
        + z_hi * rate_prime(coefficients, z_hi)
    )
    assert red_x_upper < ZERO
    assert red_y_lower > ZERO

    # Replay the mixed sloping-boundary derivative on 8,192 cells.
    worst_red_boundary = None
    for cell in range(8192):
        lo = z_lo + (z_hi - z_lo) * cell / 8192
        hi = z_lo + (z_hi - z_lo) * (cell + 1) / 8192
        z = interval(lo, hi)
        value = (
            c_eta - rate_prime(coefficients, z)
            + slope * (
                c_eta - rate(coefficients, z)
                + z * rate_prime(coefficients, z)
            )
        )
        assert value < ZERO, (cell, value)
        if worst_red_boundary is None or value.upper() > worst_red_boundary.upper():
            worst_red_boundary = value
    assert worst_red_boundary is not None

    axis_ratio = (ONE - tau) / (ONE - r_axis)
    red_page = (
        c_eta * r_axis + tau * page_cost
        + (ONE - r_axis) * rate(coefficients, axis_ratio)
    )
    red_margin = u_one - gap - red_page
    assert red_margin > arb("0.000000001")

    blue_y_upper = c_eta - rate_prime(coefficients, ONE - tau)
    assert blue_y_upper < ZERO

    # Replay the blue diagonal derivative on 16,384 cells.
    worst_blue_diagonal = None
    for cell in range(16384):
        xlo = r_diag * cell / 16384
        xhi = r_diag * (cell + 1) / 16384
        x = interval(xlo, xhi)
        denominator = ONE - x
        w = ONE - tau / denominator
        value = (
            2 * c_eta - rate(coefficients, w)
            - tau / denominator * rate_prime(coefficients, w)
        )
        assert value < ZERO, (cell, value)
        if (
            worst_blue_diagonal is None
            or value.upper() > worst_blue_diagonal.upper()
        ):
            worst_blue_diagonal = value
    assert worst_blue_diagonal is not None

    blue_page = tau * page_cost + rate(coefficients, ONE - tau)
    blue_margin = u_one - gap - blue_page
    assert blue_margin > arb("0.000000001")

    assert 2 - diagonal / off_diagonal > ZERO
    reservoir = 2 * c_eta * r_diag + 2 * tau * xi_cost
    reservoir_margin = u_one - gap - reservoir
    assert reservoir_margin > arb("0.000000001")

    base = (u_one - gap).exp()
    safe_decimal = arb(3_780_685_745) / 1_000_000_000
    rounding_margin = safe_decimal - base
    assert safe_decimal < arb(3_780_687) / 1_000_000
    assert rounding_margin > arb("0.000000001")

    print("PASS: independent 512-bit joint hybrid retained-spine replay")
    print(f"precision_bits: {ctx.prec}")
    for name, value in correlation.items():
        print(f"correlation_{name}: {value}")
    print(f"concavity_worst_upper: {concavity.upper()}")
    print(f"degree_slack: {degree_slack}")
    print(f"A: {diagonal}")
    print(f"E: {off_diagonal}")
    print(f"r_axis: {r_axis}")
    print(f"r_diag: {r_diag}")
    print(f"red_x_endpoint_upper: {red_x_upper.upper()}")
    print(f"red_y_endpoint_lower: {red_y_lower.lower()}")
    print(f"red_boundary_derivative_upper: {worst_red_boundary.upper()}")
    print(f"red_page_margin: {red_margin}")
    print(f"blue_y_upper: {blue_y_upper.upper()}")
    print(f"blue_diagonal_derivative_upper: {worst_blue_diagonal.upper()}")
    print(f"blue_page_margin: {blue_margin}")
    print(f"reservoir_margin: {reservoir_margin}")
    print(f"base_upper: {base}")
    print(f"rounding_margin: {rounding_margin}")


if __name__ == "__main__":
    main()
