#!/usr/bin/env python3
"""Focused theorem-to-code regression tests for the upper-bound route."""

from __future__ import annotations

from flint import arb, ctx

from verify_arb import (
    HALF,
    ONE,
    ZERO,
    envelope_upper_candidates,
    parse,
    polynomial,
    polynomial_derivative,
    polynomial_second_derivative,
    prior_u,
    rate_prime,
)


ctx.prec = 256


def horizon_union_gap_test() -> None:
    """Exhibit a strict union-pass/intersection-fail verifier point.

    A one-sided prior rate only controls ell<=k.  Its swapped inequality is
    separately needed for ell>k.  Thus this is a concrete false positive of
    Horizon's stated *rate-envelope certificate*.  It does not assert that the
    numerical point cannot belong to the true, larger Ramsey region by some
    unrelated theorem.
    """
    lam = parse("0.001")
    m = parse("0.001")
    y = parse("0.26320792385176556")
    target = [parse(x) for x in ["-0.25", "0.033", "0.08", "0", "-0.07795"]]
    prior = [parse(x) for x in ["-0.25", "0.033", "0.08"]]

    fp = rate_prime(lam, target)
    log_x = (ONE - m).log() + (ONE - (-fp).exp()).log() / (ONE - m)
    a = -log_x
    b = -y.log()

    standard_at_half = a + HALF * b - prior_u(HALF, prior)
    if not standard_at_half < ZERO:
        raise AssertionError(f"expected standard orientation to fail: {standard_at_half}")

    _, swapped_candidates = envelope_upper_candidates(a, prior)
    swapped_margins = [b - candidate for candidate in swapped_candidates]
    if not all(margin > ZERO for margin in swapped_margins):
        raise AssertionError(f"expected swapped orientation to pass: {swapped_margins}")

    print("PASS: Horizon union-gap test")
    print(f"lambda={lam}; M={m}; Y={y}; a=-log X={a}; b=-log Y={b}")
    print(f"standard margin at mu=1/2: {standard_at_half} (strictly negative)")
    print(
        f"swapped envelope margins: {swapped_margins} (all strictly positive; "
        "Horizon union accepts, but the all-k,l rate certificate is incomplete)"
    )


def derivative_sign_test() -> None:
    """The real-valued X formula itself forces F'>0, not F'<0."""
    fp = parse("0.7")
    base = ONE - (-fp).exp()
    if not base > ZERO:
        raise AssertionError("positive derivative should give a positive X base")
    negative_fp = parse("-0.7")
    negative_base = ONE - (-negative_fp).exp()
    if not negative_base < ZERO:
        raise AssertionError("negative derivative should give a negative X base")
    print("PASS: derivative sign regression; X base is positive iff F'>0")


def generic_polynomial_derivative_test() -> None:
    """Guard the arbitrary-degree prior-concavity implementation."""
    z = parse("0.37")
    coefficients = [parse(x) for x in ["-0.25", "0.06", "-0.03", "0.1", "-0.02"]]
    expected_first = sum(
        index * coefficient * z ** (index - 1)
        for index, coefficient in enumerate(coefficients, start=1)
    )
    expected_second = sum(
        index * (index - 1) * coefficient * z ** (index - 2)
        for index, coefficient in enumerate(coefficients, start=1)
        if index >= 2
    )
    if not (polynomial_derivative(z, coefficients) - expected_first).contains(0):
        raise AssertionError("generic first polynomial derivative failed")
    if not (
        polynomial_second_derivative(z, coefficients) - expected_second
    ).contains(0):
        raise AssertionError("generic second polynomial derivative failed")
    print("PASS: arbitrary-degree polynomial derivative regression")


if __name__ == "__main__":
    derivative_sign_test()
    generic_polynomial_derivative_test()
    horizon_union_gap_test()
