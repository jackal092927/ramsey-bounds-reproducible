#!/usr/bin/env python3
"""Certified single-point audit of the corrected GNNW Lemma-14 hull.

Requires python-flint.  This script does not prove a Ramsey lower or upper
bound; it verifies that the paper's first positive-alpha parameter update
fails Theorem 13's analytic condition at lambda=1 when Y is replaced by the
all-ratio envelope actually implied by Lemma 14's premise.
"""

from __future__ import annotations

from flint import arb, ctx


def main() -> None:
    ctx.prec = 200

    one = arb(1)
    two = arb(2)
    e = one.exp()

    # First positive-alpha update in source line 487.
    alpha = arb(9) / (arb(100) * e)
    beta = arb(9) / arb(200)
    lam = one

    # Source lines 473-480, evaluated directly rather than from decimal data.
    h = (one + lam) * (one + lam).log() - lam * lam.log()
    g = -lam / arb(4) + beta * lam**2 + arb(2) * lam**3 / arb(25)
    g_prime = -one / arb(4) + two * beta * lam + arb(6) * lam**2 / arb(25)
    f = h + g * (-lam).exp()
    f_prime = ((one + lam) / lam).log() + (g_prime - g) * (-lam).exp()
    m = lam * (-lam).exp()
    x = (one - (-f_prime).exp()) ** (one / (one - m)) * (one - m)

    E = alpha.exp()
    threshold = E / (one + E)
    y_legal = one - x / E
    y_paper = E * (one - x)

    psi_legal = f + (x.log() + lam * m.log() + lam * y_legal.log()) / two
    psi_paper = f + (x.log() + lam * m.log() + lam * y_paper.log()) / two

    # Interval comparisons are true only when the balls are disjoint.
    assert x < one / two
    assert x < threshold
    assert y_legal < y_paper
    assert psi_legal.upper() < 0
    assert psi_paper.lower() > 0

    # Literal counterexample to source line 460 at alpha=0.
    x0 = arb(2) / arb(5)
    a0 = one - x0
    left = x0**-2 * a0**-1
    right = x0**-1 * a0**-2
    assert left > right

    print(f"alpha       = {alpha}")
    print(f"X           = {x}")
    print(f"threshold   = {threshold}")
    print(f"Y legal     = {y_legal}")
    print(f"Y paper     = {y_paper}")
    print(f"psi legal   = {psi_legal}")
    print(f"psi paper   = {psi_paper}")
    print(f"line460 LHS = {left}")
    print(f"line460 RHS = {right}")
    print("CERTIFIED: corrected-hull psi(1) < 0; paper-branch psi(1) > 0")


if __name__ == "__main__":
    main()
