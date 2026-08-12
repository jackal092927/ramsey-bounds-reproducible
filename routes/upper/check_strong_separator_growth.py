#!/usr/bin/env python3
"""384-bit Arb checker for the strong separator/direct growth lemma."""

from fractions import Fraction
import flint
from flint import arb, ctx

ctx.prec = 384
ZERO = arb(0)
ONE = arb(1)


def hull(lo: arb, hi: arb) -> arb:
    return lo.union(hi)


def e_minus(v: arb) -> arb:
    root_three = arb(3).sqrt()
    return ((-v).exp() + 2 * (v / 2).exp()
            * (root_three * v / 2).cos()) / 3


def e_plus(u: arb) -> arb:
    root_three = arb(3).sqrt()
    return (u.exp() + 2 * (-u / 2).exp()
            * (root_three * u / 2).cos()) / 3


def main() -> None:
    assert flint.__version__ == "0.9.0"
    u0 = arb(619) / 250
    a = (-u0).exp()
    d_one = arb(113) / 100
    assert ONE + a < d_one

    # Negative segment of the normalized H envelope.
    worst_h_slack = None
    cells = 16384
    for cell in range(cells):
        lo = u0 * cell / cells
        hi = u0 * (cell + 1) / cells
        v = hull(lo, hi)
        radicand = u0**3 - v**3
        if cell == cells - 1:
            # Dependency inflation can make the naively repeated u0-v
            # expression straddle zero.  Its exact range on this cell is
            # [0, u0^3-(u0(1-1/cells))^3].
            rad_hi = u0**3 - (u0 * (cells - 1) / cells)**3
            w = hull(ZERO, rad_hi ** (ONE / 3))
        else:
            w = radicand ** (ONE / 3)
        slack = d_one * (2 * w).exp() - (ONE + a * e_minus(v)**2)
        assert slack > ZERO, (cell, slack)
        if worst_h_slack is None or slack.lower() < worst_h_slack.lower():
            worst_h_slack = slack

    # Exact positive root-filter envelope on a compact interval.
    exact_cells = 65536
    cutoff = arb(20)
    worst_e_slack = None
    for cell in range(exact_cells):
        lo = cutoff * cell / exact_cells
        hi = cutoff * (cell + 1) / exact_cells
        u = hull(lo, hi)
        w = (u**3 + u0**3) ** (ONE / 3)
        slack = (w.exp() / 3) - e_plus(u)
        assert slack > ZERO, (cell, slack)
        if worst_e_slack is None or slack.lower() < worst_e_slack.lower():
            worst_e_slack = slack

    # Analytic half-line gate.  Let q=u0^3/u^3.  The lower bound below for
    # w-u beats log(1+2 exp(-3u/2)) at u=20.  Its logarithmic derivative is
    # >= -2/u, while that of 2 exp(-3u/2) is -3/2; hence the ordering persists.
    q = u0**3 / cutoff**3
    lower = u0**3 / (3 * cutoff**2 * (ONE + q) ** (arb(2) / 3))
    tail_rhs = (ONE + 2 * (-3 * cutoff / 2).exp()).log()
    tail_majorant = 2 * (-3 * cutoff / 2).exp()
    assert lower > tail_majorant
    assert lower > tail_rhs
    assert arb(3) / 2 > 2 / cutoff

    direct_prefactor = 113 * a / 900
    assert direct_prefactor < arb(11) / 1000

    sigma = Fraction(501, 1000)
    prefactor = Fraction(11, 1000)
    beta = Fraction(11, 250)
    epsilon = Fraction(203, 100000)
    tail_cost = prefactor * beta * (1 + Fraction(2, 1) / epsilon)
    tail_credit = sigma * (1 - beta)
    assert tail_credit - tail_cost > Fraction(1, 100000)

    print("PASS: strong separator/direct good-event growth")
    print(f"precision_bits: {ctx.prec}")
    print(f"negative_H_envelope_worst_lower: {worst_h_slack.lower()}")
    print(f"positive_E_envelope_worst_lower: {worst_e_slack.lower()}")
    print(f"tail_halfline_lower_at_20: {lower}")
    print(f"tail_halfline_rhs_at_20: {tail_rhs}")
    print(f"tail_halfline_majorant_at_20: {tail_majorant}")
    print(f"direct_prefactor: {direct_prefactor}")
    print(f"separator_sigma: {sigma}")
    print(f"beta: {beta}")
    print(f"tail_cost_exact: {tail_cost}")
    print(f"tail_credit_exact: {tail_credit}")
    print(f"tail_budget_margin_exact: {tail_credit - tail_cost}")


if __name__ == "__main__":
    main()
