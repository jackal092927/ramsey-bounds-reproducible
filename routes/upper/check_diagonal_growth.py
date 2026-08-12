#!/usr/bin/env python3
"""512-bit Arb certificate for the diagonal good-event growth bound.

The mathematical reduction from two variables to the diagonal is proved in
``DIAGONAL_GROWTH_SHARPENING_CANDIDATE.md``.  This checker certifies the only
non-symbolic input in that reduction,

    H(u^3)^2 - H(-u^3)^2 < 10^-4 exp(4 (u^3+u0^3)^(1/3)),  u >= 0,

using exact rational cells on [0,20] and a closed-form root-filter envelope
on [20,infinity).  It also verifies the exact correlation tail budget for
the rational parameters used by the downstream candidate.

This is deliberately stronger than the required exact diagonal value
F(z,z)=H(z)^2-H(z)H(-z): on z>=0, H(z)>=H(-z)>0, so the checked square
difference is an upper bound.
"""

from __future__ import annotations

from fractions import Fraction

import flint
from flint import arb, ctx


ctx.prec = 512
ZERO = arb(0)
ONE = arb(1)


def exact_ratio(numerator: int, denominator: int = 1) -> arb:
    return arb(numerator) / denominator


def hull(lo: arb, hi: arb) -> arb:
    return lo.union(hi)


def root_filters(u: arb) -> tuple[arb, arb]:
    """Return E(u^3) and E(-u^3) from the cubic roots-of-unity filter."""
    root_three = arb(3).sqrt()
    angle = root_three * u / 2
    cosine = angle.cos()
    positive = (u.exp() + 2 * (-u / 2).exp() * cosine) / 3
    negative = ((-u).exp() + 2 * (u / 2).exp() * cosine) / 3
    return positive, negative


def main() -> None:
    assert flint.__version__ == "0.9.0"

    u0 = exact_ratio(619, 250)
    a = (-u0).exp()
    growth = exact_ratio(1, 10_000)

    # The mixed-sign reduction uses H(-v^3) <= 2 for 0 <= v <= u0.
    # The symbolic proof is |E(-v^3)| <= exp(v/2), so it suffices here to
    # record the endpoint identity and independently enclose the full segment.
    assert (a * u0.exp() - ONE).contains(0)
    worst_negative_slack = None
    negative_cells = 16_384
    for cell in range(negative_cells):
        v = hull(u0 * cell / negative_cells, u0 * (cell + 1) / negative_cells)
        negative = root_filters(v)[1]
        slack = 2 - (ONE + a * negative**2)
        assert slack > ZERO, (cell, slack)
        if (
            worst_negative_slack is None
            or slack.lower() < worst_negative_slack.lower()
        ):
            worst_negative_slack = slack

    # Direct compact certificate.  Monotonicity of u -> w lets us construct
    # its range from the rational endpoints, avoiding dependency inflation in
    # (u^3+u0^3)^(1/3).
    cutoff = exact_ratio(20)
    cells = 65_536
    worst_compact_slack = None
    worst_compact_cell = None
    for cell in range(cells):
        lo = cutoff * cell / cells
        hi = cutoff * (cell + 1) / cells
        u = hull(lo, hi)
        w = hull(
            (lo**3 + u0**3) ** (ONE / 3),
            (hi**3 + u0**3) ** (ONE / 3),
        )
        positive, negative = root_filters(u)
        h_positive = ONE + a * positive**2
        h_negative = ONE + a * negative**2
        diagonal = h_positive**2 - h_negative**2
        normalized = diagonal / (4 * w).exp()
        slack = growth - normalized
        assert slack > ZERO, (cell, slack, normalized)
        if (
            worst_compact_slack is None
            or slack.lower() < worst_compact_slack.lower()
        ):
            worst_compact_slack = slack
            worst_compact_cell = cell

    assert worst_compact_slack is not None

    # Analytic half-line.  For u >= 20,
    #
    #   |E(u^3)| <= e^u(1+2e^(-3u/2))/3,
    #   H(-u^3)^2 >= 1, and w >= u.
    #
    # Expanding H(u^3)^2-1 and normalizing by exp(4w) gives the decreasing
    # upper envelope below.  Replacing u by 20 is therefore valid on the
    # complete half-line.
    tail_oscillation = ONE + 2 * (-3 * cutoff / 2).exp()
    tail_linear = (
        2 * a / 9 * (-2 * cutoff).exp() * tail_oscillation**2
    )
    tail_quadratic = a**2 / 81 * tail_oscillation**4
    tail_upper = tail_linear + tail_quadratic
    tail_slack = growth - tail_upper
    assert tail_slack > exact_ratio(1, 100_000)

    # Exact rational master-tail budget.  The choice beta=3253/5000 is
    # intentionally below the floating optimum and leaves a large margin.
    sigma = Fraction(501, 1000)
    beta = Fraction(3253, 5000)
    epsilon = Fraction(93, 125_000)
    growth_q = Fraction(1, 10_000)
    tail_cost = growth_q * beta * (1 + Fraction(2, 1) / epsilon)
    tail_credit = sigma * (1 - beta)
    budget_margin = tail_credit - tail_cost
    assert budget_margin > Fraction(1, 100_000)

    print("PASS: 512-bit diagonal good-event growth certificate")
    print(f"precision_bits: {ctx.prec}")
    print(f"negative_H_cells: {negative_cells}")
    print(f"negative_H_worst_slack_lower: {worst_negative_slack.lower()}")
    print(f"compact_cells: {cells}")
    print(f"worst_compact_cell: {worst_compact_cell}")
    print(f"worst_compact_slack_lower: {worst_compact_slack.lower()}")
    print(f"tail_linear_upper: {tail_linear.upper()}")
    print(f"tail_quadratic_upper: {tail_quadratic.upper()}")
    print(f"tail_upper: {tail_upper.upper()}")
    print(f"tail_slack_lower: {tail_slack.lower()}")
    print(f"separator_sigma: {sigma}")
    print(f"growth_prefactor: {growth_q}")
    print(f"epsilon: {epsilon}")
    print(f"beta: {beta}")
    print(f"tail_cost_exact: {tail_cost}")
    print(f"tail_credit_exact: {tail_credit}")
    print(f"tail_budget_margin_exact: {budget_margin}")


if __name__ == "__main__":
    main()
