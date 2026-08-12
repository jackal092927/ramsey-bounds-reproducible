#!/usr/bin/env python3
"""512-bit Arb certificate for the u0=309/125 diagonal-growth lemma."""

from __future__ import annotations

from fractions import Fraction

import flint
from flint import arb, ctx


ctx.prec = 512
ZERO = arb(0)
ONE = arb(1)


def q(numerator: int, denominator: int = 1) -> arb:
    return arb(numerator) / denominator


def hull(lo: arb, hi: arb) -> arb:
    return lo.union(hi)


def root_filters(u: arb) -> tuple[arb, arb, arb, arb]:
    """Return E(u^3), E(-u^3), and their u derivatives."""
    root_three = arb(3).sqrt()
    angle = root_three * u / 2
    cosine = angle.cos()
    sine = angle.sin()
    exp_u = u.exp()
    exp_minus_u = (-u).exp()
    exp_half = (u / 2).exp()
    exp_minus_half = (-u / 2).exp()
    positive = (exp_u + 2 * exp_minus_half * cosine) / 3
    negative = (exp_minus_u + 2 * exp_half * cosine) / 3
    positive_prime = (
        exp_u - exp_minus_half * cosine
        - root_three * exp_minus_half * sine
    ) / 3
    negative_prime = (
        -exp_minus_u + exp_half * cosine
        - root_three * exp_half * sine
    ) / 3
    return positive, negative, positive_prime, negative_prime


def main() -> None:
    assert flint.__version__ == "0.9.0"

    u0_f = Fraction(309, 125)
    sigma0_f = Fraction(1, 10_000)
    ratio_target_f = Fraction(10_001, 5_000)
    separator_f = Fraction(5_001, 10_000)
    growth_f = Fraction(89, 1_000_000)
    beta_f = Fraction(833, 1250)
    epsilon_f = Fraction(7113, 10_000_000)
    correlation_f = Fraction(3_092_197_917, 312_500_000)

    # Lock the two similar-looking constants to their correct identities.
    assert ratio_target_f == 2 + 2 * sigma0_f
    assert separator_f == (1 + 2 * sigma0_f) / 2
    assert correlation_f == 4 * u0_f * (1 + epsilon_f)

    u0 = q(u0_f.numerator, u0_f.denominator)
    a = (-u0).exp()
    ratio_target = q(ratio_target_f.numerator, ratio_target_f.denominator)
    growth = q(growth_f.numerator, growth_f.denominator)

    # Exact endpoint and exhaustive monotonicity proof for the ratio on
    # [u0, 2.9].  R' has the sign of the numerator checked below.
    positive, negative, _, _ = root_filters(u0)
    h_positive = ONE + a * positive**2
    h_negative = ONE + a * negative**2
    endpoint_ratio_slack = h_positive / h_negative - ratio_target
    assert endpoint_ratio_slack > q(1, 100_000)

    switch = q(29, 10)
    ratio_cells = 32_768
    ratio_worst = None
    ratio_worst_cell = None
    for cell in range(ratio_cells):
        lo = u0 + (switch - u0) * cell / ratio_cells
        hi = u0 + (switch - u0) * (cell + 1) / ratio_cells
        p, n, pp, np = root_filters(hull(lo, hi))
        hp = ONE + a * p**2
        hn = ONE + a * n**2
        numerator = p * pp * hn - n * np * hp
        assert numerator > ZERO, (cell, numerator)
        if ratio_worst is None or numerator.lower() < ratio_worst.lower():
            ratio_worst = numerator
            ratio_worst_cell = cell
    assert ratio_worst is not None

    # Analytic ratio tail at and beyond 2.9.
    eu = switch.exp()
    eh = (switch / 2).exp()
    em = (-switch).exp()
    emh = (-switch / 2).exp()
    positive_lower = (eu - 2 * emh) / 3
    negative_upper = (2 * eh + em) / 3
    tail_ratio_slack = (
        (ONE + a * positive_lower**2)
        / (ONE + a * negative_upper**2)
        - ratio_target
    )
    bracket = (
        eu**2 - 4 * ratio_target * eu - 4 * eh
        - 4 * ratio_target * emh + 4 * em - ratio_target * em**2
    )
    tail_endpoint = a * bracket - 9 * (ratio_target - ONE)
    derivative_gate = (
        2 * eu * (eu - 2 * ratio_target) - 2 * eh - 4 * em
    )
    derivative_prime_gate = (
        4 * eu**2 - 4 * ratio_target * eu - eh + 4 * em
    )
    assert positive_lower > ZERO
    assert tail_ratio_slack > q(3, 10)
    assert tail_endpoint > ZERO
    assert derivative_gate > ZERO
    assert derivative_prime_gate > ZERO

    # The two-variable diagonal reduction uses H(-v^3)<=2 on 0<=v<=u0.
    # Its analytic proof is a*exp(u0)=1; the grid is a redundant replay.
    assert (a * u0.exp() - ONE).contains(0)
    negative_cells = 16_384
    negative_worst = None
    for cell in range(negative_cells):
        v = hull(u0 * cell / negative_cells,
                 u0 * (cell + 1) / negative_cells)
        negative_value = root_filters(v)[1]
        slack = 2 - (ONE + a * negative_value**2)
        assert slack > ZERO, (cell, slack)
        if negative_worst is None or slack.lower() < negative_worst.lower():
            negative_worst = slack

    # Direct compact certificate for the stronger square-difference bound.
    cutoff = q(20)
    growth_cells = 65_536
    growth_worst = None
    growth_worst_cell = None
    for cell in range(growth_cells):
        lo = cutoff * cell / growth_cells
        hi = cutoff * (cell + 1) / growth_cells
        u = hull(lo, hi)
        w = hull(
            (lo**3 + u0**3) ** (ONE / 3),
            (hi**3 + u0**3) ** (ONE / 3),
        )
        p, n, _, _ = root_filters(u)
        hp = ONE + a * p**2
        hn = ONE + a * n**2
        normalized = (hp**2 - hn**2) / (4 * w).exp()
        slack = growth - normalized
        assert slack > ZERO, (cell, slack, normalized)
        if growth_worst is None or slack.lower() < growth_worst.lower():
            growth_worst = slack
            growth_worst_cell = cell
    assert growth_worst is not None

    # Analytic half-line envelope.  Both displayed terms decrease in u, so
    # the endpoint at 20 covers the complete tail.
    oscillation = ONE + 2 * (-3 * cutoff / 2).exp()
    tail_linear = 2 * a / 9 * (-2 * cutoff).exp() * oscillation**2
    tail_quadratic = a**2 / 81 * oscillation**4
    growth_tail_upper = tail_linear + tail_quadratic
    growth_tail_slack = growth - growth_tail_upper
    asymptotic_slack = growth - a**2 / 81
    assert growth_tail_slack > q(1, 1_000_000)
    assert asymptotic_slack > q(1, 10_000_000)

    # Exact expectation-tail budget and exact inner/outer C interface.
    tail_cost = growth_f * beta_f * (1 + Fraction(2, 1) / epsilon_f)
    tail_credit = separator_f * (1 - beta_f)
    tail_budget = tail_credit - tail_cost
    assert tail_budget == Fraction(89_775_619, 8_891_250_000_000)
    assert tail_budget > Fraction(1, 100_000)

    print("PASS: 512-bit u0=309/125 diagonal-growth certificate")
    print(f"precision_bits: {ctx.prec}")
    print(f"ratio_target: {ratio_target_f}")
    print(f"separator_sigma: {separator_f}")
    print(f"ratio_endpoint_slack: {endpoint_ratio_slack}")
    print(f"ratio_cells: {ratio_cells}")
    print(f"ratio_worst_cell: {ratio_worst_cell}")
    print(f"ratio_derivative_worst_lower: {ratio_worst.lower()}")
    print(f"ratio_tail_slack_at_2.9: {tail_ratio_slack}")
    print(f"negative_H_worst_slack_lower: {negative_worst.lower()}")
    print(f"growth_prefactor: {growth_f}")
    print(f"growth_cells: {growth_cells}")
    print(f"growth_worst_cell: {growth_worst_cell}")
    print(f"growth_compact_worst_slack_lower: {growth_worst.lower()}")
    print(f"growth_tail_upper: {growth_tail_upper.upper()}")
    print(f"growth_tail_slack_lower: {growth_tail_slack.lower()}")
    print(f"growth_asymptotic_slack_lower: {asymptotic_slack.lower()}")
    print(f"beta: {beta_f}")
    print(f"epsilon: {epsilon_f}")
    print(f"correlation_C: {correlation_f}")
    print(f"tail_cost_exact: {tail_cost}")
    print(f"tail_credit_exact: {tail_credit}")
    print(f"tail_budget_margin_exact: {tail_budget}")


if __name__ == "__main__":
    main()
