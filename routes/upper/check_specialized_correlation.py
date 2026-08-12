#!/usr/bin/env python3
"""Arb arithmetic for the specialized r=2,d=3 correlation lemma."""

from __future__ import annotations

from fractions import Fraction

import flint
from flint import arb, ctx


ctx.prec = 384


def main() -> None:
    assert flint.__version__ == "0.9.0"

    u0 = arb(29) / 10
    sigma = Fraction(1, 200)
    epsilon = Fraction(9, 5000)
    beta = Fraction(1, 1000000)
    ratio_target = Fraction(201, 100)
    c_exact = Fraction(58, 5)
    correlation_exact = Fraction(145261, 12500)

    assert ratio_target == 2 + 2 * sigma
    assert c_exact == 4 * Fraction(29, 10)
    assert correlation_exact == (1 + epsilon) * c_exact

    eu = u0.exp()
    ehalf = (u0 / 2).exp()
    eminus = (-u0).exp()
    eminushalf = (-u0 / 2).exp()

    bracket = (
        eu**2
        - arb(ratio_target.numerator) / ratio_target.denominator
        * 4 * eu
        - 4 * ehalf
        - arb(ratio_target.numerator) / ratio_target.denominator
        * 4 * eminushalf
        + 4 * eminus
        - arb(ratio_target.numerator) / ratio_target.denominator
        * eminus**2
    )
    tail_endpoint = (
        eminus * bracket
        - 9 * (arb(ratio_target.numerator) / ratio_target.denominator - 1)
    )
    assert tail_endpoint > 0

    derivative_lower_endpoint = (
        2 * eu
        * (
            eu
            - 2 * arb(ratio_target.numerator) / ratio_target.denominator
        )
        - 2 * ehalf - 4 * eminus
    )
    assert derivative_lower_endpoint > 0

    # Exact generalized separator budget.
    tail_cost = 4 * beta * (1 + Fraction(2, 1) / epsilon)
    tail_credit = sigma * (1 - beta)
    assert tail_cost < tail_credit

    old_correlation = 8 * arb(432).log()
    new_correlation = arb(correlation_exact.numerator) / correlation_exact.denominator
    assert new_correlation < old_correlation

    positive_axis = (eu - 2 * eminushalf) / 3
    negative_axis = (2 * ehalf + eminus) / 3
    ratio_lower = (1 + eminus * positive_axis**2) / (
        1 + eminus * negative_axis**2
    )
    assert ratio_lower > (
        arb(ratio_target.numerator) / ratio_target.denominator
    )

    print("PASS: specialized two-colour correlation arithmetic")
    print(f"precision_bits: {ctx.prec}")
    print(f"u0: {u0}")
    print(f"tail_endpoint_J: {tail_endpoint}")
    print(f"derivative_lower_endpoint: {derivative_lower_endpoint}")
    print(f"root_ratio_lower: {ratio_lower}")
    print(f"separator_sigma: {float(sigma):.18g}")
    print(f"beta: {float(beta):.18g}")
    print(f"tail_cost_exact: {tail_cost}")
    print(f"tail_credit_exact: {tail_credit}")
    print(f"c_envelope: {float(c_exact):.18g}")
    print(f"C_correlation: {new_correlation}")
    print(f"printed_C_correlation: {old_correlation}")


if __name__ == "__main__":
    main()
