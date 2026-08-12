#!/usr/bin/env python3
"""Independent 512-bit replay of the specialized-correlation upper bound.

This script intentionally does not import either author checker.  It uses a
different polynomial representation, a finer concavity partition, endpoint
monotonicity for the red derivatives, and a cellwise blue-diagonal replay.
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
    "SPECIALIZED_CORRELATION_SHARPENING.md":
        "c28026ed8d30e0c4096ccc46e3cc04d7026fa2c2975eab4a2537a9021a866ebe",
    "check_specialized_correlation.py":
        "be17cc0848a54e606b4ad4bc3393b8ac317f030306c239d41bd0f90f38c5724a",
    "RETAINED_SPINE_SHARPENED_CERTIFICATE.md":
        "83e79f2a2950c73d0a3697193b3fd826130d69f197f57febd4a8f9f1c25acdbf",
    "check_retained_spine_sharpened.py":
        "1a74a21d81002805657c74373c44b760c57edd36ad942d768e7d7afd6abfac40",
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
    result = ZERO
    for coefficient in reversed(coefficients):
        result = result * x + coefficient
    return result


def p6(coefficients: list[arb], x: arb) -> arb:
    # Source payload stores coefficients of x through x^14.
    return x * horner(coefficients, x)


def p6_prime(coefficients: list[arb], x: arb) -> arb:
    derived = [(index + 1) * value for index, value in enumerate(coefficients)]
    return horner(derived, x)


def p6_second(coefficients: list[arb], x: arb) -> arb:
    derived = [
        (index + 2) * (index + 1) * coefficients[index + 1]
        for index in range(len(coefficients) - 1)
    ]
    return horner(derived, x)


def u_rate(coefficients: list[arb], x: arb) -> arb:
    entropy = (ONE + x) * (ONE + x).log() - x * x.log()
    return entropy + p6(coefficients, x) * (-x).exp()


def u_prime(coefficients: list[arb], x: arb) -> arb:
    poly = p6(coefficients, x)
    return ((ONE + x) / x).log() + (
        p6_prime(coefficients, x) - poly
    ) * (-x).exp()


def u_second(coefficients: list[arb], x: arb) -> arb:
    poly = p6(coefficients, x)
    return -ONE / (x * (ONE + x)) + (
        p6_second(coefficients, x)
        - 2 * p6_prime(coefficients, x)
        + poly
    ) * (-x).exp()


def prove_concavity(coefficients: list[arb]) -> arb:
    split = ONE / 65536
    near_zero = interval(ZERO, split)
    correction = (
        p6_second(coefficients, near_zero)
        - 2 * p6_prime(coefficients, near_zero)
        + p6(coefficients, near_zero)
    ) * (-near_zero).exp()
    worst = -ONE / (split * (ONE + split)) + correction
    assert worst < ZERO

    for cell in range(65536):
        lo = split + (ONE - split) * cell / 65536
        hi = split + (ONE - split) * (cell + 1) / 65536
        value = u_second(coefficients, interval(lo, hi))
        assert value < ZERO, (cell, value)
        if value.upper() > worst.upper():
            worst = value
    return worst


def replay_correlation() -> dict[str, arb | Fraction]:
    """Rebuild the generalized-sigma lemma without the author's B/J code."""
    u0 = arb(29) / 10
    sigma = Fraction(1, 200)
    beta = Fraction(1, 1_000_000)
    epsilon = Fraction(9, 5000)
    target = Fraction(201, 100)

    eu = u0.exp()
    eh = (u0 / 2).exp()
    em = (-u0).exp()
    emh = (-u0 / 2).exp()
    target_arb = arb(target.numerator) / target.denominator

    # Directly evaluate the two squared root-filter envelopes, independently
    # of the expanded B polynomial.
    positive = (eu - 2 * emh) / 3
    negative = (2 * eh + em) / 3
    assert positive > ZERO  # required before squaring the lower bound
    h_positive_lower = ONE + em * positive**2
    h_negative_upper = ONE + em * negative**2
    ratio_slack = h_positive_lower - target_arb * h_negative_upper
    assert ratio_slack > ZERO

    # Direct derivative of the expanded envelope difference.  Its lower
    # bound is positive at u0 and has derivative positive on u>=u0, because
    # e^u>18 and 4e^u-8.04>63.9>e^(-u/2).
    derivative_lower = (
        2 * eu * (eu - 2 * target_arb)
        - 2 * eh - 4 * em
    )
    derivative_second_lower = (
        4 * eu**2 - 4 * target_arb * eu - eh + 4 * em
    )
    assert eu > 18
    assert derivative_lower > ZERO
    assert derivative_second_lower > ZERO

    # Generalized bad-event expectation and tail contradiction.
    tail_cost = 4 * beta * (1 + Fraction(2, 1) / epsilon)
    tail_credit = sigma * (1 - beta)
    assert tail_cost == Fraction(1_000_900, 225_000_000)
    assert tail_credit == Fraction(999_999, 200_000_000)
    assert tail_cost < tail_credit

    correlation = Fraction(145261, 12500)
    assert correlation == (1 + epsilon) * Fraction(58, 5)
    return {
        "ratio_slack": ratio_slack,
        "derivative_lower": derivative_lower,
        "derivative_second_lower": derivative_second_lower,
        "tail_cost": tail_cost,
        "tail_credit": tail_credit,
    }


def main() -> None:
    assert flint.__version__ == "0.9.0"
    for name, expected in AUTHOR_SHA256.items():
        actual = digest(HERE / name)
        assert actual == expected, (name, actual, expected)

    correlation_replay = replay_correlation()

    payload = json.loads(
        (HERE / "certificate-higher-order-tetradecic-chain-v6.json")
        .read_text(encoding="utf-8")
    )
    assert payload["schema"] == "corrected-two-sided-ramsey-v1"
    coefficients = [arb(str(x)) for x in payload["target_coefficients"]]
    assert len(coefficients) == 14

    eta = arb(28681) / 1_000_000
    probability = arb(471309) / 1_000_000
    book_delta = arb(528) / 10_000_000
    lambda_zero = arb(13520)
    tau = arb(572) / 1_000_000
    exponent_gap = arb(287) / 100_000_000
    beta = arb(1) / 1_000_000
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
        + 12 * correlation * log_delta / lambda_zero ** (arb(2) / 3)
    )

    # Recheck the exact source gates.
    assert ZERO < eta
    assert ZERO < probability < ONE / 2 - eta
    assert ZERO < book_delta <= probability / 4
    assert book_delta <= ONE / 4
    assert lambda_zero >= 2
    assert lambda_zero >= 6 * log_delta
    assert ZERO < tau < ONE
    assert ZERO < beta <= ONE
    degree_slack = tau * (ONE / 2 - eta - probability)
    assert degree_slack > ZERO

    concavity = prove_concavity(coefficients)
    u_one = u_rate(coefficients, ONE)
    up_one = u_prime(coefficients, ONE)
    diagonal = u_one - 2 * c_eta
    off_diagonal = up_one - c_eta
    assert ZERO < diagonal < off_diagonal
    assert page_cost < up_one
    assert 2 * tau * xi_cost < u_one

    r_diag = exponent_gap / diagonal
    r_axis = exponent_gap / off_diagonal
    slope = ONE - diagonal / off_diagonal
    assert ZERO < r_axis < tau < r_diag < ONE
    assert ZERO < slope < ONE

    # Full direct-branch complement follows from concavity.  In the wedge,
    # z increases from the diagonal endpoint to the red-axis endpoint.
    z_lo = ONE - tau / (ONE - r_diag)
    z_hi = (ONE - tau) / (ONE - r_axis)
    assert ZERO < z_lo < z_hi < ONE

    # Because U''<0, c-U'(z) is increasing; evaluate its largest endpoint.
    pr_x_upper = c_eta - u_prime(coefficients, z_hi)
    assert pr_x_upper < ZERO

    # d/dz[c-U(z)+zU'(z)] = zU''(z)<0, so its minimum is at z_hi.
    pr_y_lower = (
        c_eta - u_rate(coefficients, z_hi)
        + z_hi * u_prime(coefficients, z_hi)
    )
    assert pr_y_lower > ZERO

    # Boundary derivative needs a full interval because it mixes opposite
    # monotonicities.  Use 4096 independent z cells rather than one hull.
    worst_boundary = None
    for cell in range(4096):
        lo = z_lo + (z_hi - z_lo) * cell / 4096
        hi = z_lo + (z_hi - z_lo) * (cell + 1) / 4096
        z = interval(lo, hi)
        derivative = (
            c_eta - u_prime(coefficients, z)
            + slope * (
                c_eta - u_rate(coefficients, z)
                + z * u_prime(coefficients, z)
            )
        )
        assert derivative < ZERO, (cell, derivative)
        if worst_boundary is None or derivative.upper() > worst_boundary.upper():
            worst_boundary = derivative
    assert worst_boundary is not None

    axis_ratio = (ONE - tau) / (ONE - r_axis)
    page_axis = (
        c_eta * r_axis + tau * page_cost
        + (ONE - r_axis) * u_rate(coefficients, axis_ratio)
    )
    page_margin = u_one - exponent_gap - page_axis
    assert page_margin > arb("0.000000001")

    # Blue-page y derivative: w<=1-tau and concavity imply
    # c-U'(w) <= c-U'(1-tau)<0.
    pb_y_upper = c_eta - u_prime(coefficients, ONE - tau)
    assert pb_y_upper < ZERO

    # Replay the diagonal derivative on 8192 cells without a broad x hull.
    worst_blue_diagonal = None
    for cell in range(8192):
        xlo = r_diag * cell / 8192
        xhi = r_diag * (cell + 1) / 8192
        x = interval(xlo, xhi)
        denominator = ONE - x
        w = ONE - tau / denominator
        derivative = (
            2 * c_eta - u_rate(coefficients, w)
            - tau / denominator * u_prime(coefficients, w)
        )
        assert derivative < ZERO, (cell, derivative)
        if (
            worst_blue_diagonal is None
            or derivative.upper() > worst_blue_diagonal.upper()
        ):
            worst_blue_diagonal = derivative
    assert worst_blue_diagonal is not None

    page_origin = tau * page_cost + u_rate(coefficients, ONE - tau)
    other_page_margin = u_one - exponent_gap - page_origin
    assert other_page_margin > arb("0.000000001")

    # Maximize x+y exactly over xA+(y-x)E<=Delta: on the edge its
    # derivative is 2-A/E>0, so the maximum is the diagonal endpoint.
    assert 2 - diagonal / off_diagonal > ZERO
    reservoir = 2 * c_eta * r_diag + 2 * tau * xi_cost
    reservoir_margin = u_one - exponent_gap - reservoir
    assert reservoir_margin > arb("0.000000001")

    base = (u_one - exponent_gap).exp()
    decimal = arb(3780687577208) / 1_000_000_000_000
    rounding_margin = decimal - base
    assert rounding_margin > arb("0.000000000000001")

    print("PASS: independent 512-bit sharpened retained-spine replay")
    print(f"precision_bits: {ctx.prec}")
    for name, value in correlation_replay.items():
        print(f"correlation_{name}: {value}")
    print(f"concavity_worst_upper: {concavity.upper()}")
    print(f"degree_slack: {degree_slack}")
    print(f"A: {diagonal}")
    print(f"E: {off_diagonal}")
    print(f"r_axis: {r_axis}")
    print(f"r_diag: {r_diag}")
    print(f"P_R_dx_endpoint_upper: {pr_x_upper.upper()}")
    print(f"P_R_dy_endpoint_lower: {pr_y_lower.lower()}")
    print(f"P_R_boundary_derivative_upper: {worst_boundary.upper()}")
    print(f"red_page_margin: {page_margin}")
    print(f"P_B_dy_upper: {pb_y_upper.upper()}")
    print(f"P_B_diagonal_derivative_upper: {worst_blue_diagonal.upper()}")
    print(f"blue_page_margin: {other_page_margin}")
    print(f"reservoir_margin: {reservoir_margin}")
    print(f"base_upper: {base}")
    print(f"rounding_margin: {rounding_margin}")


if __name__ == "__main__":
    main()
