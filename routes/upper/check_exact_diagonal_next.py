#!/usr/bin/env python3
"""512-bit author certificate for the exact-diagonal inner candidate."""

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


def filters(u: arb) -> tuple[arb, arb, arb, arb]:
    s = arb(3).sqrt()
    theta = s * u / 2
    cosine = theta.cos()
    sine = theta.sin()
    ep = u.exp()
    en = (-u).exp()
    eh = (u / 2).exp()
    emh = (-u / 2).exp()
    p = (ep + 2 * emh * cosine) / 3
    n = (en + 2 * eh * cosine) / 3
    dp = (ep - emh * cosine - s * emh * sine) / 3
    dn = (-en + eh * cosine - s * eh * sine) / 3
    return p, n, dp, dn


def main() -> None:
    assert flint.__version__ == "0.9.0"

    u0_f = Fraction(1_235_783, 500_000)  # 2.471566
    sigma0_f = Fraction(1, 100_000_000)
    target_f = Fraction(100_000_001, 50_000_000)
    separator_f = Fraction(50_000_001, 100_000_000)
    growth_f = Fraction(88_053, 1_000_000_000)
    beta_f = Fraction(330_867, 500_000)
    epsilon_f = Fraction(6893, 10_000_000)
    correlation_f = Fraction(12_366_348_252_219, 1_250_000_000_000)
    assert target_f == 2 + 2 * sigma0_f
    assert separator_f == (1 + 2 * sigma0_f) / 2
    assert correlation_f == 4 * u0_f * (1 + epsilon_f)

    u0 = q(u0_f.numerator, u0_f.denominator)
    target = q(target_f.numerator, target_f.denominator)
    growth = q(growth_f.numerator, growth_f.denominator)
    a = (-u0).exp()

    # Ratio proof on [u0,2.9] plus analytic half-line.
    p, n, _, _ = filters(u0)
    hp = ONE + a * p**2
    hn = ONE + a * n**2
    endpoint_ratio_slack = hp / hn - target
    assert endpoint_ratio_slack > q(1, 10_000_000)

    switch = q(29, 10)
    ratio_cells = 65_536
    ratio_worst = None
    ratio_worst_cell = None
    for cell in range(ratio_cells):
        lo = u0 + (switch - u0) * cell / ratio_cells
        hi = u0 + (switch - u0) * (cell + 1) / ratio_cells
        p, n, dp, dn = filters(hull(lo, hi))
        hp = ONE + a * p**2
        hn = ONE + a * n**2
        numerator = p * dp * hn - n * dn * hp
        assert numerator > ZERO, (cell, numerator)
        if ratio_worst is None or numerator.lower() < ratio_worst.lower():
            ratio_worst = numerator
            ratio_worst_cell = cell

    eu = switch.exp()
    eh = (switch / 2).exp()
    em = (-switch).exp()
    emh = (-switch / 2).exp()
    p_lower = (eu - 2 * emh) / 3
    n_upper = (2 * eh + em) / 3
    tail_ratio_slack = (
        (ONE + a * p_lower**2) / (ONE + a * n_upper**2) - target
    )
    bracket = (
        eu**2 - 4 * target * eu - 4 * eh - 4 * target * emh
        + 4 * em - target * em**2
    )
    tail_endpoint = a * bracket - 9 * (target - ONE)
    derivative_gate = 2 * eu * (eu - 2 * target) - 2 * eh - 4 * em
    derivative_prime_gate = 4 * eu**2 - 4 * target * eu - eh + 4 * em
    assert p_lower > ZERO
    assert tail_ratio_slack > q(3, 10)
    assert tail_endpoint > ZERO
    assert derivative_gate > ZERO
    assert derivative_prime_gate > ZERO

    # Complete two-variable reduction: H(-v^3)<=2 for -L<=x<=0.
    assert (a * u0.exp() - ONE).contains(0)
    negative_cells = 32_768
    negative_worst = None
    for cell in range(negative_cells):
        v = hull(u0 * cell / negative_cells,
                 u0 * (cell + 1) / negative_cells)
        negative = filters(v)[1]
        slack = 2 - (ONE + a * negative**2)
        assert slack > ZERO, (cell, slack)
        if negative_worst is None or slack.lower() < negative_worst.lower():
            negative_worst = slack

    # Exact diagonal F(z,z)=H(z)^2-H(z)H(-z), not square difference.
    cutoff = q(20)
    growth_cells = 131_072
    growth_worst = None
    growth_worst_cell = None
    for cell in range(growth_cells):
        lo = cutoff * cell / growth_cells
        hi = cutoff * (cell + 1) / growth_cells
        u = hull(lo, hi)
        w = hull((lo**3 + u0**3) ** (ONE / 3),
                 (hi**3 + u0**3) ** (ONE / 3))
        p, n, _, _ = filters(u)
        hp = ONE + a * p**2
        hn = ONE + a * n**2
        exact_diagonal = hp**2 - hp * hn
        normalized = exact_diagonal / (4 * w).exp()
        slack = growth - normalized
        assert slack > ZERO, (cell, slack, normalized)
        if growth_worst is None or slack.lower() < growth_worst.lower():
            growth_worst = slack
            growth_worst_cell = cell

    # Analytic exact-diagonal tail.  Since H(-u^3)>=1,
    # H(u^3)^2-H(u^3)H(-u^3) <= H(u^3)^2-H(u^3).
    # With P<=e^u(1+2e^-3u/2)/3 and w>=u this yields the envelope below.
    oscillation = ONE + 2 * (-3 * cutoff / 2).exp()
    tail_linear = a / 9 * (-2 * cutoff).exp() * oscillation**2
    tail_quadratic = a**2 / 81 * oscillation**4
    tail_upper = tail_linear + tail_quadratic
    tail_slack = growth - tail_upper
    asymptotic_slack = growth - a**2 / 81
    # These are strict proof margins, not outer critical margins governed by
    # the protocol's 1e-9 gate.  Record the fixed 1e-10 inner proof gate.
    assert tail_slack > q(1, 10_000_000_000)
    assert asymptotic_slack > q(1, 10_000_000_000)

    # Exact expectation-tail budget.
    tail_cost = growth_f * beta_f * (1 + Fraction(2, 1) / epsilon_f)
    tail_credit = separator_f * (1 - beta_f)
    tail_budget = tail_credit - tail_cost
    assert tail_budget == Fraction(
        39_437_634_699_447, 3_446_500_000_000_000_000
    )
    assert tail_budget > Fraction(1, 100_000)

    print("PASS: 512-bit exact-diagonal inner certificate")
    print(f"precision_bits: {ctx.prec}")
    print(f"u0: {u0_f}")
    print(f"ratio_target: {target_f}")
    print(f"separator_sigma: {separator_f}")
    print(f"ratio_endpoint_slack: {endpoint_ratio_slack}")
    print(f"ratio_cells: {ratio_cells}")
    print(f"ratio_worst_cell: {ratio_worst_cell}")
    print(f"ratio_derivative_worst_lower: {ratio_worst.lower()}")
    print(f"tail_ratio_slack: {tail_ratio_slack}")
    print(f"negative_H_worst_slack_lower: {negative_worst.lower()}")
    print(f"growth_prefactor: {growth_f}")
    print(f"growth_cells: {growth_cells}")
    print(f"growth_worst_cell: {growth_worst_cell}")
    print(f"growth_compact_worst_slack_lower: {growth_worst.lower()}")
    print(f"growth_tail_upper: {tail_upper.upper()}")
    print(f"growth_tail_slack_lower: {tail_slack.lower()}")
    print(f"growth_asymptotic_slack_lower: {asymptotic_slack.lower()}")
    print(f"beta: {beta_f}")
    print(f"epsilon: {epsilon_f}")
    print(f"correlation_C_exact: {correlation_f}")
    print(f"tail_cost_exact: {tail_cost}")
    print(f"tail_credit_exact: {tail_credit}")
    print(f"tail_budget_margin_exact: {tail_budget}")


if __name__ == "__main__":
    main()
