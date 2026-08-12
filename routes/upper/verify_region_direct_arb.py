#!/usr/bin/env python3
"""Independent direct Arb replay of the two Ramsey-region inequalities.

This deliberately does not import ``verify_arb.py`` and does not use its
``A(mu)=U(mu)-mu*U'(mu)`` envelope reduction.  For every target-lambda cell it
checks the two exponent slacks directly:

    h_standard(mu) = a + mu*b - U(mu),
    h_swapped(mu)  = b + mu*a - U(mu).

Strict concavity of U makes each slack convex.  Its only possible interior
minimum is therefore found from U'(mu)=b or U'(mu)=a, respectively.  Arb balls
bracket those roots and evaluate the complete continuous interval, including
the mu -> 0 endpoint.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from flint import arb, ctx


ctx.prec = 256

ZERO = arb(0)
ONE = arb(1)
TAIL = arb("1e-30")


def parse(value: object) -> arb:
    return arb(str(value))


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
    s = poly(z, coefficients)
    sp = poly_prime(z, coefficients)
    return ((ONE + z) / z).log() + (sp - s) * (-z).exp()


def rate_second(z: arb, coefficients: list[arb]) -> arb:
    s = poly(z, coefficients)
    sp = poly_prime(z, coefficients)
    spp = poly_second(z, coefficients)
    return -ONE / (z * (ONE + z)) + (spp - 2 * sp + s) * (-z).exp()


def prove_concavity(coefficients: list[arb]) -> float:
    """Prove U''<0 independently on (0,1]."""
    split = arb("0.0001")
    small = hull(ZERO, split)
    correction = (
        poly_second(small, coefficients)
        - 2 * poly_prime(small, coefficients)
        + poly(small, coefficients)
    ) * (-small).exp()
    pole_upper = -ONE / (split * (ONE + split))
    if not pole_upper + correction < ZERO:
        raise AssertionError(
            f"small-mu concavity was not proved: pole={pole_upper}, "
            f"correction={correction}"
        )

    worst = float((pole_upper + correction).upper())
    cells = 8192
    for index in range(cells):
        lo = split + (ONE - split) * index / cells
        hi = split + (ONE - split) * (index + 1) / cells
        second = rate_second(hull(lo, hi), coefficients)
        if not second < ZERO:
            raise AssertionError(
                f"prior concavity unresolved on independent cell {index}: {second}"
            )
        worst = max(worst, float(second.upper()))
    return worst


def bracket_uprime(level: arb, prior: list[arb]) -> arb | None:
    """Bracket the unique U'(mu)=level root; return None for endpoint minimum."""
    up_one = rate_prime(ONE, prior)
    # If level <= U'(1), level-U' is nonpositive throughout (0,1], so the
    # corresponding convex slack decreases through the right endpoint.
    if level <= up_one:
        return None
    if not rate_prime(TAIL, prior) > level:
        raise AssertionError(f"tail is not left of root for level {level}")

    lo, hi = TAIL, ONE
    for _ in range(220):
        mid = (lo + hi) / 2
        sign = rate_prime(mid, prior) - level
        if sign > ZERO:
            lo = mid
        elif sign < ZERO:
            hi = mid
        else:
            # At 256-bit precision this can occur only after an already tiny
            # bracket.  Retain the entire current bracket.
            break
    root = hull(lo, hi)
    if not rate_prime(lo, prior) >= level:
        raise AssertionError("left root-bracket sign failed")
    if not rate_prime(hi, prior) <= level:
        raise AssertionError("right root-bracket sign failed")
    return root


def lower(value: arb) -> float:
    return float(value.lower())


def direct_minima(a: arb, b: arb, prior: list[arb]) -> tuple[float, float]:
    """Return rigorous scalar lower bounds for both slacks on 0<=mu<=1."""
    u_one = rate(ONE, prior)
    common_right = a + b - u_one

    standard = [a, common_right]
    root_b = bracket_uprime(b, prior)
    if root_b is not None:
        standard.append(a + root_b * b - rate(root_b, prior))

    swapped = [b, common_right]
    root_a = bracket_uprime(a, prior)
    if root_a is not None:
        swapped.append(b + root_a * a - rate(root_a, prior))

    if not all(candidate > ZERO for candidate in standard):
        raise AssertionError(f"nonpositive standard direct candidate: {standard}")
    if not all(candidate > ZERO for candidate in swapped):
        raise AssertionError(f"nonpositive swapped direct candidate: {swapped}")
    return min(map(lower, standard)), min(map(lower, swapped))


def replay(payload: dict) -> dict:
    prior = [parse(item) for item in payload["prior_coefficients"]]
    target = [parse(item) for item in payload["target_coefficients"]]
    expected = parse(payload["lambda_split"])

    worst_standard = (math.inf, None)
    worst_swapped = (math.inf, None)
    for index, segment in enumerate(payload["segments"]):
        lo, hi = parse(segment["lo"]), parse(segment["hi"])
        if not (lo - expected).contains(0) or not hi > lo:
            raise AssertionError(f"coverage failure at target segment {index}")
        expected = hi

        lam = hull(lo, hi)
        m = parse(segment["M"])
        y = parse(segment["Y"])
        if not ZERO < m < ONE or not ZERO < y < ONE:
            raise AssertionError(f"range failure at target segment {index}")

        fp = rate_prime(lam, target)
        q = (-fp).exp()
        if not ZERO < q < ONE:
            raise AssertionError(f"q range failure at target segment {index}")
        log_x = (ONE - m).log() + (ONE - q).log() / (ONE - m)
        # Every scalar a(lambda) in the cell is at least this exact lower
        # endpoint.  Both direct slacks increase with a, so it is the safe
        # dependency-free choice for the whole lambda cell.
        a = (-log_x).lower()
        b = -y.log()
        standard, swapped = direct_minima(a, b, prior)
        if standard < worst_standard[0]:
            worst_standard = (standard, index)
        if swapped < worst_swapped[0]:
            worst_swapped = (swapped, index)

    if not (expected - ONE).contains(0):
        raise AssertionError("target segments do not end at lambda=1")
    return {
        "segments": len(payload["segments"]),
        "worst_standard_exponent_slack": worst_standard,
        "worst_swapped_exponent_slack": worst_swapped,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.certificate.read_text(encoding="utf-8"))
    if payload.get("schema") != "corrected-two-sided-ramsey-v1":
        raise AssertionError("unexpected certificate schema")

    prior = [parse(item) for item in payload["prior_coefficients"]]
    concavity = prove_concavity(prior)
    result = replay(payload)
    print("PASS: independent direct two-sided Ramsey-region replay")
    print(f"prior U'' worst certified upper bound: {concavity:.17g}")
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
