#!/usr/bin/env python3
"""Conservative 256-bit Arb certificate for the retained-spine maximum.

This checker proves only the deliberately non-optimal bound

    C_* <= U(1) - 10^(-8).

It uses the analytic direct-branch estimate outside a tiny square and proves
the monotonicity of both page branches inside that square.  The transfer
lemma itself is an upstream theorem and is pinned by SHA-256 below.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import flint
from flint import arb, ctx


ctx.prec = 256

HERE = Path(__file__).resolve().parent
ZERO = arb(0)
ONE = arb(1)

UPSTREAM_SHA256 = {
    "RETAINED_SPINE_TRANSFER_ATTEMPT.md":
        "5aa5d6cb1ee1cc2d9f4d34b8564b6c57f78cfd7444a89abcfbb64542274e4aaa",
    "INDEPENDENT_RETAINED_SPINE_REFEREE.md":
        "6ba57fdbe13bf45255644ae94af5474b7a34afda3aefeda26415f3cc3f9b66db",
    "check_retained_spine_transfer.py":
        "b10815b10cb3ab922aa079ee74289c52239ec90939ed41b93907bf06a60ee274",
    "certificate-higher-order-tetradecic-chain-v6.json":
        "8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8",
    "verify_region_direct_arb.py":
        "e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def hull(lo: arb, hi: arb) -> arb:
    return lo.union(hi)


def poly(z: arb, coefficients: list[arb]) -> arb:
    total = ZERO
    power = z
    for coefficient in coefficients:
        total += coefficient * power
        power *= z
    return total


def poly_prime(z: arb, coefficients: list[arb]) -> arb:
    total = ZERO
    power = ONE
    for degree, coefficient in enumerate(coefficients, start=1):
        total += degree * coefficient * power
        power *= z
    return total


def poly_second(z: arb, coefficients: list[arb]) -> arb:
    total = ZERO
    power = ONE
    for degree, coefficient in enumerate(coefficients, start=1):
        if degree >= 2:
            total += degree * (degree - 1) * coefficient * power
            power *= z
    return total


def entropy(z: arb) -> arb:
    return (ONE + z) * (ONE + z).log() - z * z.log()


def rate(z: arb, coefficients: list[arb]) -> arb:
    return entropy(z) + poly(z, coefficients) * (-z).exp()


def rate_prime(z: arb, coefficients: list[arb]) -> arb:
    value = poly(z, coefficients)
    derivative = poly_prime(z, coefficients)
    return ((ONE + z) / z).log() + (derivative - value) * (-z).exp()


def rate_second(z: arb, coefficients: list[arb]) -> arb:
    value = poly(z, coefficients)
    derivative = poly_prime(z, coefficients)
    second = poly_second(z, coefficients)
    return -ONE / (z * (ONE + z)) + (
        second - 2 * derivative + value
    ) * (-z).exp()


def prove_concavity(coefficients: list[arb]) -> arb:
    """Independently prove U''<0 on (0,1] by interval subdivision."""
    split = arb("0.0001")
    small = hull(ZERO, split)
    correction = (
        poly_second(small, coefficients)
        - 2 * poly_prime(small, coefficients)
        + poly(small, coefficients)
    ) * (-small).exp()
    worst = -ONE / (split * (ONE + split)) + correction
    assert worst < ZERO, f"concavity unresolved near zero: {worst}"

    cells = 8192
    for index in range(cells):
        lo = split + (ONE - split) * index / cells
        hi = split + (ONE - split) * (index + 1) / cells
        enclosure = rate_second(hull(lo, hi), coefficients)
        assert enclosure < ZERO, (
            f"concavity unresolved on cell {index}: {enclosure}"
        )
        if enclosure.upper() > worst.upper():
            worst = enclosure
    return worst


def main() -> None:
    assert flint.__version__ == "0.9.0", (
        f"unreviewed python-flint version: {flint.__version__}"
    )
    for name, expected in UPSTREAM_SHA256.items():
        actual = sha256(HERE / name)
        assert actual == expected, (
            f"upstream dependency changed: {name}: {actual} != {expected}"
        )

    payload = json.loads(
        (HERE / "certificate-higher-order-tetradecic-chain-v6.json")
        .read_text(encoding="utf-8")
    )
    assert payload.get("schema") == "corrected-two-sided-ramsey-v1"
    coefficients = [arb(str(x)) for x in payload["target_coefficients"]]

    # All displayed terminating decimals are exact rationals in Arb.
    eta = arb("0.032")
    p = arb("0.46799")
    delta = arb("0.00001")
    lambda_zero = arb("25000")
    tau = arb("0.00005")
    radius = arb("0.0000016")
    target_gap = arb("0.00000001")

    root_filter = arb(432).log()
    beta = ONE / 48
    correlation_c = 8 * root_filter
    rho = (arb(2) / beta).log()
    log_delta = (ONE / delta).log()
    log_p = (ONE / p).log()
    pi_cost = (
        3 * delta / p
        + 6 * log_delta * log_p / lambda_zero
    )
    xi_cost = (
        2 * rho
        + 4 * correlation_c * lambda_zero ** (ONE / 3)
        + 12 * correlation_c * log_delta
        / lambda_zero ** (arb(2) / 3)
    )
    regularization = (arb(2) / (ONE + eta)).log()
    page_cost = log_p + pi_cost

    u_one = rate(ONE, coefficients)
    up_one = rate_prime(ONE, coefficients)
    direct_diagonal = u_one - 2 * regularization
    direct_off_diagonal = up_one - regularization

    concavity_upper = prove_concavity(coefficients)
    assert ZERO < radius < tau < ONE
    assert direct_diagonal > ZERO
    assert direct_off_diagonal >= direct_diagonal

    # Outside [0,radius]^2, (18) is weakest on the diagonal.  Hence its
    # certified exponent gain is radius * (U(1)-2c_eta).
    outer_gain = radius * direct_diagonal
    assert outer_gain >= target_gap

    # For the first page branch, throughout the small square,
    #
    #   z=(1-tau-x)/(1-y),
    #   P_R=c(x+y)+tau*q+(1-y)U(z).
    #
    # Since tau>radius, the displayed coordinate is always the smaller one
    # in the homogeneous rate.  The other page branch is its transpose.
    z_lo = ONE - tau - radius
    z_hi = (ONE - tau) / (ONE - radius)
    assert ZERO < z_lo < z_hi < ONE
    z_box = hull(z_lo, z_hi)

    derivative_x = regularization - rate_prime(z_box, coefficients)
    derivative_y = (
        regularization
        - rate(z_box, coefficients)
        + z_box * rate_prime(z_box, coefficients)
    )
    assert derivative_x < ZERO, f"page d/dx sign unresolved: {derivative_x}"
    assert derivative_y > ZERO, f"page d/dy sign unresolved: {derivative_y}"

    # Thus P_R is maximized at (0,radius), P_B at (radius,0), with
    # the same value by symmetry.
    z_axis = (ONE - tau) / (ONE - radius)
    page_axis = (
        regularization * radius
        + tau * page_cost
        + (ONE - radius) * rate(z_axis, coefficients)
    )
    page_margin = u_one - target_gap - page_axis
    assert page_margin > ZERO

    # Q is coordinatewise increasing, so its maximum on the square is its
    # value at (radius,radius).
    reservoir_corner = (
        2 * regularization * radius + 2 * tau * xi_cost
    )
    reservoir_margin = u_one - target_gap - reservoir_corner
    assert reservoir_margin > ZERO

    certified_exponent = u_one - target_gap
    certified_base = certified_exponent.exp()
    decimal_upper = arb("3.780698389989140")
    assert certified_base < decimal_upper

    print("PASS: retained-spine numerical maximum certificate")
    print(f"precision_bits: {ctx.prec}")
    print(f"concavity_worst_upper: {concavity_upper.upper()}")
    print(f"U(1): {u_one}")
    print(f"radius: {radius}")
    print(f"target_exponent_gap: {target_gap}")
    print(f"outer_direct_gain: {outer_gain}")
    print(f"outer_margin_over_target: {outer_gain - target_gap}")
    print(f"page_z_box: {z_box}")
    print(f"page_d_dx: {derivative_x}")
    print(f"page_d_dy: {derivative_y}")
    print(f"page_axis_value: {page_axis}")
    print(f"page_margin_below_target: {page_margin}")
    print(f"reservoir_corner_value: {reservoir_corner}")
    print(f"reservoir_margin_below_target: {reservoir_margin}")
    print(f"certified_exponent: {certified_exponent}")
    print(f"certified_base: {certified_base}")
    print(f"certified_decimal_upper: {decimal_upper}")


if __name__ == "__main__":
    main()
