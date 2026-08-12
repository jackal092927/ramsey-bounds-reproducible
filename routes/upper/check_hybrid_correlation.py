#!/usr/bin/env python3
"""384-bit Arb proof checker for the hybrid r=2,d=3 correlation lemma."""

from __future__ import annotations

import hashlib
from fractions import Fraction
from pathlib import Path

import flint
from flint import arb, ctx


ctx.prec = 384
HERE = Path(__file__).resolve().parent
ZERO = arb(0)
ONE = arb(1)

PROOF_SHA256 = "4b29c692dd1fc96859491b25d61c9b0e1124a33cf57a45ef01abb5a2e49ed30d"


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            value.update(block)
    return value.hexdigest()


def hull(lo: arb, hi: arb) -> arb:
    return lo.union(hi)


def root_filters(u: arb) -> tuple[arb, arb, arb, arb]:
    root_three = arb(3).sqrt()
    angle = root_three * u / 2
    cosine = angle.cos()
    sine = angle.sin()
    eu = u.exp()
    em = (-u).exp()
    eh = (u / 2).exp()
    emh = (-u / 2).exp()
    positive = (eu + 2 * emh * cosine) / 3
    negative = (em + 2 * eh * cosine) / 3
    positive_prime = (eu - emh * cosine - root_three * emh * sine) / 3
    negative_prime = (-em + eh * cosine - root_three * eh * sine) / 3
    return positive, negative, positive_prime, negative_prime


def main() -> None:
    assert flint.__version__ == "0.9.0"
    actual_proof = digest(HERE / "HYBRID_CORRELATION_SHARPENING.md")
    assert actual_proof == PROOF_SHA256, (actual_proof, PROOF_SHA256)

    u0_exact = Fraction(619, 250)
    switch_exact = Fraction(29, 10)
    sigma = Fraction(1, 1000)
    target = Fraction(1001, 500)
    epsilon = Fraction(21, 10000)
    beta = Fraction(1, 4_000_000)
    c_exact = 4 * u0_exact
    correlation = Fraction(6_202_999, 625_000)
    assert target == 2 + 2 * sigma
    assert correlation == (1 + epsilon) * c_exact

    u0 = arb(u0_exact.numerator) / u0_exact.denominator
    switch = arb(switch_exact.numerator) / switch_exact.denominator
    target_arb = arb(target.numerator) / target.denominator
    a = (-u0).exp()

    # Exact endpoint ratio.
    positive, negative, _, _ = root_filters(u0)
    h_positive = ONE + a * positive**2
    h_negative = ONE + a * negative**2
    endpoint_ratio_slack = h_positive / h_negative - target_arb
    assert endpoint_ratio_slack > arb("0.0001")

    # Exhaustive rational-cell proof of R'(u)>0 on [u0, 2.9].
    cells = 4096
    worst_derivative_numerator = None
    width = switch - u0
    for index in range(cells):
        lo = u0 + width * index / cells
        hi = u0 + width * (index + 1) / cells
        u = hull(lo, hi)
        p, n, pp, np = root_filters(u)
        hp = ONE + a * p**2
        hn = ONE + a * n**2
        numerator_without_positive_factor = p * pp * hn - n * np * hp
        assert numerator_without_positive_factor > ZERO, (
            index,
            numerator_without_positive_factor,
        )
        if (
            worst_derivative_numerator is None
            or numerator_without_positive_factor.lower()
            < worst_derivative_numerator.lower()
        ):
            worst_derivative_numerator = numerator_without_positive_factor
    assert worst_derivative_numerator is not None

    # Analytic-envelope endpoint at 2.9.
    eu = switch.exp()
    eh = (switch / 2).exp()
    em = (-switch).exp()
    emh = (-switch / 2).exp()
    positive_lower = (eu - 2 * emh) / 3
    negative_upper = (2 * eh + em) / 3
    assert positive_lower > ZERO
    envelope_ratio_slack = (
        (ONE + a * positive_lower**2)
        / (ONE + a * negative_upper**2)
        - target_arb
    )
    assert envelope_ratio_slack > arb("0.3")

    bracket = (
        eu**2
        - 4 * target_arb * eu
        - 4 * eh
        - 4 * target_arb * emh
        + 4 * em
        - target_arb * em**2
    )
    tail_endpoint = a * bracket - 9 * (target_arb - ONE)
    assert tail_endpoint > ZERO
    assert eu > 18
    derivative_lower_endpoint = (
        2 * eu * (eu - 2 * target_arb) - 2 * eh - 4 * em
    )
    assert derivative_lower_endpoint > ZERO

    # Exact generalized-separator tail budget.
    tail_cost = 4 * beta * (1 + Fraction(2, 1) / epsilon)
    tail_credit = sigma * (1 - beta)
    assert tail_cost == Fraction(20021, 21_000_000)
    assert tail_credit == Fraction(3_999_999, 4_000_000_000)
    assert tail_credit - tail_cost > Fraction(1, 100_000)

    print("PASS: hybrid exact/envelope two-colour correlation arithmetic")
    print(f"precision_bits: {ctx.prec}")
    print(f"proof_sha256: {actual_proof}")
    print(f"u0: {u0}")
    print(f"exact_endpoint_ratio_slack: {endpoint_ratio_slack}")
    print(
        "finite_interval_derivative_numerator_worst: "
        f"{worst_derivative_numerator}"
    )
    print(f"tail_envelope_ratio_slack_at_2.9: {envelope_ratio_slack}")
    print(f"tail_endpoint_K: {tail_endpoint}")
    print(f"tail_derivative_lower_endpoint: {derivative_lower_endpoint}")
    print(f"sigma: {sigma}")
    print(f"beta: {beta}")
    print(f"tail_cost_exact: {tail_cost}")
    print(f"tail_credit_exact: {tail_credit}")
    print(f"C_correlation: {correlation}")


if __name__ == "__main__":
    main()
