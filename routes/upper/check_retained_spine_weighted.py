#!/usr/bin/env python3
"""384-bit Arb certificate for a weighted retained-spine enclosure.

The already refereed transfer theorem defines

    C_* = max_[0,1]^2 min(D, B).

This script proves the two-sided numerical bracket

    U(1) - 0.0000001130243 <= C_* <= U(1) - 0.000000113024.

The upper bound uses the exact tangent gain

    G(x,y) = min(x,y) A + |x-y| E,
    A = U(1)-2c_eta, E = U'(1)-c_eta,

instead of enclosing the exceptional neighbourhood by a square.  Outside
G <= Delta the direct branch wins.  Inside it, analytic derivative signs
reduce both page branches to one-dimensional endpoints.  The lower bound is
an exact rational-axis witness, not a floating optimizer.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import flint
from flint import arb, ctx


ctx.prec = 384

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


def polynomial(z: arb, coefficients: list[arb]) -> arb:
    total = ZERO
    for coefficient in reversed(coefficients):
        total = z * (coefficient + total)
    return total


def polynomial_prime(z: arb, coefficients: list[arb]) -> arb:
    total = ZERO
    for degree in range(len(coefficients), 0, -1):
        total = degree * coefficients[degree - 1] + z * total
    return total


def polynomial_second(z: arb, coefficients: list[arb]) -> arb:
    total = ZERO
    for degree in range(len(coefficients), 1, -1):
        total = degree * (degree - 1) * coefficients[degree - 1] + z * total
    return total


def rate(z: arb, coefficients: list[arb]) -> arb:
    entropy = (ONE + z) * (ONE + z).log() - z * z.log()
    return entropy + polynomial(z, coefficients) * (-z).exp()


def rate_prime(z: arb, coefficients: list[arb]) -> arb:
    value = polynomial(z, coefficients)
    derivative = polynomial_prime(z, coefficients)
    return ((ONE + z) / z).log() + (derivative - value) * (-z).exp()


def rate_second(z: arb, coefficients: list[arb]) -> arb:
    value = polynomial(z, coefficients)
    derivative = polynomial_prime(z, coefficients)
    second = polynomial_second(z, coefficients)
    return -ONE / (z * (ONE + z)) + (
        second - 2 * derivative + value
    ) * (-z).exp()


def prove_concavity(coefficients: list[arb]) -> arb:
    """Re-prove U''<0 on (0,1] without importing an old evaluator."""
    split = arb(1) / 16384
    small = hull(ZERO, split)
    correction = (
        polynomial_second(small, coefficients)
        - 2 * polynomial_prime(small, coefficients)
        + polynomial(small, coefficients)
    ) * (-small).exp()
    worst = -ONE / (split * (ONE + split)) + correction
    assert worst < ZERO, f"concavity unresolved near zero: {worst}"

    cells = 16384
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
    coefficients = [arb(str(item)) for item in payload["target_coefficients"]]
    assert len(coefficients) == 14

    # Exact terminating decimals.
    eta = arb("0.032")
    probability = arb("0.46799")
    book_delta = arb("0.00001")
    lambda_zero = arb("25000")
    tau = arb("0.00005")
    upper_gap = arb("0.000000113024")
    lower_gap = arb("0.0000001130243")
    witness = arb("0.00000108477835")

    c_eta = (arb(2) / (ONE + eta)).log()
    log_delta = (ONE / book_delta).log()
    log_probability = (ONE / probability).log()
    pi_cost = (
        3 * book_delta / probability
        + 6 * log_delta * log_probability / lambda_zero
    )
    page_cost = log_probability + pi_cost
    correlation = 8 * arb(432).log()
    xi_cost = (
        2 * arb(96).log()
        + 4 * correlation * lambda_zero ** (ONE / 3)
        + 12 * correlation * log_delta
        / lambda_zero ** (arb(2) / 3)
    )

    concavity_upper = prove_concavity(coefficients)
    u_one = rate(ONE, coefficients)
    up_one = rate_prime(ONE, coefficients)
    diagonal_coefficient = u_one - 2 * c_eta       # A
    off_diagonal_coefficient = up_one - c_eta      # E
    assert ZERO < diagonal_coefficient < off_diagonal_coefficient

    # Exact claim and domain split.  In the ordered triangle 0 <= x <= y,
    # the direct-branch tangent gain is
    #
    #   G(x,y) = x*A + (y-x)*E.
    #
    # G >= upper_gap is controlled by D.  If G <= upper_gap, then
    # x <= r_diag, y-x <= r_axis and y <= r_diag.  The last assertion uses
    # h'(x)=1-A/E in (0,1) for the upper boundary
    # h(x)=x+(upper_gap-A*x)/E.
    r_diag = upper_gap / diagonal_coefficient
    r_axis = upper_gap / off_diagonal_coefficient
    boundary_slope = ONE - diagonal_coefficient / off_diagonal_coefficient
    assert ZERO < r_axis < r_diag < tau
    assert ZERO < boundary_slope < ONE
    assert tau - r_axis > ZERO

    # On the complete weighted inner triangle, the red-page branch is
    #
    # P_R=c(x+y)+tau*q+(1-y)U((1-tau-x)/(1-y)).
    #
    # A deliberately broad interval contains every possible ratio.  The
    # derivative signs prove P_R increases in y; along y=h(x), its derivative
    # is negative.  Thus its maximum is the axis endpoint (0,r_axis).
    z_lo = ONE - tau - r_diag
    z_hi = (ONE - tau) / (ONE - r_diag)
    z_box = hull(z_lo, z_hi)
    assert ZERO < z_lo < z_hi < ONE
    pr_x = c_eta - rate_prime(z_box, coefficients)
    pr_y = (
        c_eta - rate(z_box, coefficients)
        + z_box * rate_prime(z_box, coefficients)
    )
    pr_boundary = pr_x + boundary_slope * pr_y
    assert pr_x < ZERO
    assert pr_y > ZERO
    assert pr_boundary < ZERO

    axis_ratio = (ONE - tau) / (ONE - r_axis)
    page_axis = (
        c_eta * r_axis + tau * page_cost
        + (ONE - r_axis) * rate(axis_ratio, coefficients)
    )
    page_margin = u_one - upper_gap - page_axis
    assert page_margin > ZERO

    # For the blue-page branch in the same ordered triangle,
    #
    # P_B=c(x+y)+tau*q+(1-x)U((1-y-tau)/(1-x)).
    #
    # Its y-derivative is negative, hence P_B(x,y) <= P_B(x,x).  The exact
    # diagonal derivative below is negative on 0 <= x <= r_diag, so the
    # branch is bounded by P_B(0,0).
    x_box = hull(ZERO, r_diag)
    one_minus_x = ONE - x_box
    diagonal_ratio = ONE - tau / one_minus_x
    pb_y = c_eta - rate_prime(z_box, coefficients)
    pb_diagonal = (
        2 * c_eta - rate(diagonal_ratio, coefficients)
        - tau / one_minus_x * rate_prime(diagonal_ratio, coefficients)
    )
    assert pb_y < ZERO
    assert pb_diagonal < ZERO
    page_origin = tau * page_cost + rate(ONE - tau, coefficients)
    other_page_margin = u_one - upper_gap - page_origin
    assert other_page_margin > ZERO

    # Q is coordinatewise increasing.  The inner triangle lies in the square
    # [0,r_diag]^2, which gives a valid (intentionally loose) corner bound.
    reservoir_corner = 2 * c_eta * r_diag + 2 * tau * xi_cost
    reservoir_margin = u_one - upper_gap - reservoir_corner
    assert reservoir_margin > ZERO

    # Symmetry handles y <= x.  Hence every point either has D below the
    # upper target or all three constituents of B below it.
    exponent_upper = u_one - upper_gap
    base_upper = exponent_upper.exp()
    decimal_upper = arb("3.780698000486489")
    assert base_upper < decimal_upper

    # Rigorous lower bracket from the exact axis witness (0,witness).  Here
    # D=c*s+U(1-s), while the first page constituent of B is the expression
    # below because witness < tau.  If both exceed the lower target, then
    # min(D,B) does too because B >= P_R.
    assert ZERO < witness < tau
    witness_direct = c_eta * witness + rate(ONE - witness, coefficients)
    witness_page = (
        c_eta * witness + tau * page_cost
        + (ONE - witness)
        * rate((ONE - tau) / (ONE - witness), coefficients)
    )
    exponent_lower = u_one - lower_gap
    witness_direct_margin = witness_direct - exponent_lower
    witness_page_margin = witness_page - exponent_lower
    assert witness_direct_margin > ZERO
    assert witness_page_margin > ZERO
    base_lower = exponent_lower.exp()
    # Algebraically this is exactly lower_gap-upper_gap.  Form it before
    # subtracting two correlated U(1) balls, so interval dependency does not
    # obscure the terminating-rational identity.
    bracket_width = lower_gap - upper_gap
    base_bracket_width = base_upper - base_lower
    assert bracket_width > ZERO

    print("PASS: weighted retained-spine maximum certificate")
    print(f"precision_bits: {ctx.prec}")
    print(f"global_concavity_worst_upper: {concavity_upper.upper()}")
    print(f"U(1): {u_one}")
    print(f"A=U(1)-2*c_eta: {diagonal_coefficient}")
    print(f"E=U'(1)-c_eta: {off_diagonal_coefficient}")
    print(f"upper_exponent_gap: {upper_gap}")
    print(f"lower_exponent_gap: {lower_gap}")
    print(f"r_axis=upper_gap/E: {r_axis}")
    print(f"r_diag=upper_gap/A: {r_diag}")
    print(f"boundary_slope: {boundary_slope}")
    print(f"page_ratio_box: {z_box}")
    print(f"P_R_dx_upper: {pr_x.upper()}")
    print(f"P_R_dy_lower: {pr_y.lower()}")
    print(f"P_R_boundary_derivative_upper: {pr_boundary.upper()}")
    print(f"upper_page_margin: {page_margin}")
    print(f"P_B_diagonal_derivative_upper: {pb_diagonal.upper()}")
    print(f"other_page_margin: {other_page_margin}")
    print(f"reservoir_margin: {reservoir_margin}")
    print(f"axis_witness: {witness}")
    print(f"witness_direct_margin: {witness_direct_margin}")
    print(f"witness_page_margin: {witness_page_margin}")
    print(f"C_star_lower: {exponent_lower}")
    print(f"C_star_upper: {exponent_upper}")
    print(f"exponent_bracket_width: {bracket_width}")
    print(f"base_lower: {base_lower}")
    print(f"base_upper: {base_upper}")
    print(f"base_bracket_width: {base_bracket_width}")
    print(f"safe_terminating_decimal_upper: {decimal_upper}")


if __name__ == "__main__":
    main()
