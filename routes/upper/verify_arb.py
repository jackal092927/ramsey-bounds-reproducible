#!/usr/bin/env python3
"""Independent Arb checker for the corrected diagonal-Ramsey candidate.

Unlike the HorizonMath validator, this checker

* uses python-flint/Arb ball arithmetic rather than mpmath.iv;
* requires *both* orientations of the prior-rate Ramsey envelope;
* derives the two envelope maxima from strict concavity of the prior rate;
* checks the small-lambda analytic splice separately.

Acceptance is evidence for the numerical inequalities in the audited GNNW
theorem.  The accompanying THEOREM_AUDIT.md records the mathematical bridge.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Iterable

from flint import arb, ctx


ctx.prec = 256

ZERO = arb(0)
ONE = arb(1)
HALF = arb("0.5")
MU_TAIL = arb("1e-20")


def ball_interval(lo: arb, hi: arb) -> arb:
    """Enclose two point balls without accidentally doubling endpoint radii."""
    return lo.union(hi)


def parse(value: str | int | float) -> arb:
    return arb(str(value))


def lower_float(value: arb) -> float:
    return float(value.lower())


def polynomial(z: arb, coefficients: list[arb]) -> arb:
    result = ZERO
    power = z
    for coefficient in coefficients:
        result += coefficient * power
        power *= z
    return result


def polynomial_derivative(z: arb, coefficients: list[arb]) -> arb:
    result = ZERO
    power = ONE
    for index, coefficient in enumerate(coefficients, start=1):
        result += index * coefficient * power
        power *= z
    return result


def polynomial_second_derivative(z: arb, coefficients: list[arb]) -> arb:
    """Evaluate the second derivative of ``sum c_i z^i`` generically."""
    result = ZERO
    power = ONE
    for index, coefficient in enumerate(coefficients, start=1):
        if index >= 2:
            result += index * (index - 1) * coefficient * power
            power *= z
    return result


def entropy(z: arb) -> arb:
    return (ONE + z) * (ONE + z).log() - z * z.log()


def rate(z: arb, coefficients: list[arb]) -> arb:
    return entropy(z) + polynomial(z, coefficients) * (-z).exp()


def rate_prime(z: arb, coefficients: list[arb]) -> arb:
    p = polynomial(z, coefficients)
    pp = polynomial_derivative(z, coefficients)
    return ((ONE + z) / z).log() + (pp - p) * (-z).exp()


def prior_u(z: arb, prior: list[arb]) -> arb:
    return rate(z, prior)


def prior_up(z: arb, prior: list[arb]) -> arb:
    return rate_prime(z, prior)


def prior_a(z: arb, prior: list[arb]) -> arb:
    """A(mu)=U(mu)-mu U'(mu), in a cancellation-free form."""
    s = polynomial(z, prior)
    sp = polynomial_derivative(z, prior)
    return (ONE + z).log() + (s - z * (sp - s)) * (-z).exp()


def prove_prior_concavity(prior: list[arb], cells: int = 4096) -> tuple[float, float]:
    """Prove U''<0 on (0,1] by interval subdivision.

    For an arbitrary finite polynomial s, the correction contribution is
    exp(-mu)(s''-2s'+s).  The entropy contribution is -1/(mu(1+mu)).
    The interval containing zero is handled analytically by the negative pole.
    """
    worst_upper = -math.inf
    start = parse("0.001")
    # Prove the formerly-comment-only small interval.  The entropy pole is
    # <= -1/.001001, while the correction contribution is < 1.
    small = ZERO.union(start)
    s = polynomial(small, prior)
    sp = polynomial_derivative(small, prior)
    spp = polynomial_second_derivative(small, prior)
    correction = (spp - 2 * sp + s) * (-small).exp()
    if not correction < ONE:
        raise AssertionError(f"small-mu concavity correction is not <1: {correction}")
    small_upper = -ONE / parse("0.001001") + ONE
    if not small_upper < ZERO:
        raise AssertionError("small-mu concavity analytic upper bound is not negative")
    # The interval computation handles [0.001,1].
    for index in range(cells):
        lo = start + (ONE - start) * index / cells
        hi = start + (ONE - start) * (index + 1) / cells
        mu = ball_interval(lo, hi)
        # Generic derivatives permit a proved higher-order rate to serve as
        # the exact prior at the next descent stage.
        s = polynomial(mu, prior)
        sp = polynomial_derivative(mu, prior)
        spp = polynomial_second_derivative(mu, prior)
        second = -ONE / (mu * (ONE + mu)) + (spp - 2 * sp + s) * (-mu).exp()
        if not second < ZERO:
            raise AssertionError(f"could not prove prior U''<0 on cell {index}: {second}")
        worst_upper = max(worst_upper, float(second.upper()))
    return max(worst_upper, float(small_upper.upper())), float(correction.upper())


def _bisect_increasing_a(a: arb, prior: list[arb], iterations: int = 180) -> tuple[arb, arb]:
    """Bracket every root of A(mu)=a for a in the ball ``a``."""
    lo, hi = ZERO, ONE
    for _ in range(iterations):
        mid = (lo + hi) / 2
        sign = prior_a(mid, prior) - a
        if sign < ZERO:
            lo = mid
        elif sign > ZERO:
            hi = mid
        else:
            break
    return lo, hi


def _bisect_decreasing_up(a: arb, prior: list[arb], iterations: int = 180) -> tuple[arb, arb]:
    """Bracket every root of U'(mu)=a for a in the ball ``a``."""
    lo, hi = MU_TAIL, ONE
    if not prior_up(lo, prior) - a > ZERO:
        raise AssertionError("MU_TAIL is not left of the U'=a root")
    for _ in range(iterations):
        mid = (lo + hi) / 2
        sign = prior_up(mid, prior) - a
        if sign > ZERO:
            lo = mid
        elif sign < ZERO:
            hi = mid
        else:
            break
    return lo, hi


def envelope_upper_candidates(a: arb, prior: list[arb]) -> tuple[list[arb], list[arb]]:
    """Rigorous upper candidates for the two required boundary maxima.

    Standard: sup_mu (U(mu)-a)/mu.
    Swapped:  sup_mu U(mu)-mu*a.

    Concavity gives A'= -mu U''>0 and U' decreasing.  Endpoint candidates
    are retained even when redundant, making threshold-straddling cells safe.
    """
    u1 = prior_u(ONE, prior)
    a1 = prior_a(ONE, prior)
    up1 = prior_up(ONE, prior)

    standard = [ZERO, u1 - a]
    if not a > a1:
        lo, _ = _bisect_increasing_a(a, prior)
        # For every scalar a0 in the ball a, its root mu(a0) is >= lo and U'
        # is decreasing.  Hence U'(lo) is a valid upper bound on the envelope.
        standard.append(prior_up(lo, prior))

    swapped = [ZERO, u1 - a]
    if not a < up1:
        lo, hi = _bisect_decreasing_up(a, prior)
        mu = ball_interval(lo, hi)
        swapped.append(prior_u(mu, prior) - mu * a)
    return standard, swapped


def region_margins_over_lambda(
    lo: arb,
    hi: arb,
    m: arb,
    b: arb,
    target: list[arb],
    prior: list[arb],
    depth: int = 0,
) -> tuple[float, float]:
    """Prove both region envelopes, recursively reducing dependency loss."""
    lam = ball_interval(lo, hi)
    fp = rate_prime(lam, target)
    log_x = (ONE - m).log() + (ONE - (-fp).exp()).log() / (ONE - m)
    a = -log_x
    # The standard threshold decreases with a.  The swapped threshold also
    # decreases with a.  Replace the dependency-wide ball by a rigorous point
    # lower endpoint, which is the worst case for both thresholds.
    a_worst = a.lower()
    standard, swapped = envelope_upper_candidates(a_worst, prior)
    std_margins = [b - candidate for candidate in standard]
    swap_margins = [b - candidate for candidate in swapped]
    if all(margin > ZERO for margin in std_margins) and all(
        margin > ZERO for margin in swap_margins
    ):
        return (
            min(lower_float(margin) for margin in std_margins),
            min(lower_float(margin) for margin in swap_margins),
        )
    if depth >= 16:
        raise AssertionError(
            f"Ramsey envelope unresolved after subdivision on [{lo}, {hi}]: "
            f"standard={std_margins}; swapped={swap_margins}"
        )
    mid = (lo + hi) / 2
    left = region_margins_over_lambda(lo, mid, m, b, target, prior, depth + 1)
    right = region_margins_over_lambda(mid, hi, m, b, target, prior, depth + 1)
    return min(left[0], right[0]), min(left[1], right[1])


def main_slack_over_lambda(
    lo: arb,
    hi: arb,
    m: arb,
    y: arb,
    target: list[arb],
    depth: int = 0,
) -> float:
    """Prove the main inequality, recursively reducing interval dependency."""
    lam = ball_interval(lo, hi)
    f = rate(lam, target)
    fp = rate_prime(lam, target)
    log_x = (ONE - m).log() + (ONE - (-fp).exp()).log() / (ONE - m)
    slack = f + HALF * (log_x + lam * m.log() + lam * y.log())
    if slack > ZERO:
        return lower_float(slack)
    if depth >= 16:
        raise AssertionError(
            f"main inequality unresolved after subdivision on [{lo}, {hi}]: {slack}"
        )
    mid = (lo + hi) / 2
    return min(
        main_slack_over_lambda(lo, mid, m, y, target, depth + 1),
        main_slack_over_lambda(mid, hi, m, y, target, depth + 1),
    )


def elementary_slack_over_lambda(
    lo: arb,
    hi: arb,
    coefficients: list[arb],
    required_floor: arb = ZERO,
    depth: int = 0,
) -> float:
    """Prove a rate using the elementary ``M=lambda e^-lambda, Y=1-X``.

    ``required_floor`` can demand a quantitative certificate rather than
    stopping at the first arbitrarily small positive interval lower bound.
    """
    lam = ball_interval(lo, hi)
    f = rate(lam, coefficients)
    fp = rate_prime(lam, coefficients)
    if not f > ZERO or not fp > ZERO:
        if depth >= 20:
            raise AssertionError(f"elementary F/F' unresolved on [{lo},{hi}]")
    else:
        m = lam * (-lam).exp()
        log_x = (ONE - m).log() + (ONE - (-fp).exp()).log() / (ONE - m)
        x = log_x.exp()
        y = ONE - x
        if x > ZERO and x < ONE and y > ZERO:
            slack = f + HALF * (log_x + lam * m.log() + lam * y.log())
            if slack > required_floor:
                return lower_float(slack)
    if depth >= 20:
        raise AssertionError(f"elementary prior unresolved on [{lo},{hi}]")
    mid = (lo + hi) / 2
    return min(
        elementary_slack_over_lambda(
            lo, mid, coefficients, required_floor, depth + 1
        ),
        elementary_slack_over_lambda(
            mid, hi, coefficients, required_floor, depth + 1
        ),
    )


def certify_elementary_prior(prior: list[arb], split: arb) -> tuple[arb, float]:
    """Close the prior-rate dependency using only Observation 7(1)."""
    normalized_small = prove_small_regime(prior, split)
    worst = math.inf
    cells = 4096
    required_floor = parse("1e-6")
    for index in range(cells):
        lo = split + (ONE - split) * index / cells
        hi = split + (ONE - split) * (index + 1) / cells
        worst = min(
            worst,
            elementary_slack_over_lambda(
                lo, hi, prior, required_floor=required_floor
            ),
        )
    return normalized_small, worst


def prove_small_regime(target: list[arb], split: arb) -> arb:
    """Prove the theorem conditions analytically on all ``(0, split]``.

    We use the elementary Ramsey-region witness ``Y=1-X``.  This avoids any
    dependence on GNNW Lemma 14 in the small regime.  The returned value is a
    lower bound for ``slack(lambda)/lambda``, whose unnormalised infimum is
    necessarily zero as lambda tends to zero.
    """
    # Bounds |p| <= C0 lambda and |p'-p| <= C1 on (0, split].
    c0 = ZERO
    c1 = ZERO
    power = ONE
    for index, coefficient in enumerate(target, start=1):
        magnitude = abs(coefficient)
        c0 += magnitude * power
        # |d(lambda^i)/d lambda - lambda^i|
        # = lambda^(i-1) (i-lambda) <= i lambda^(i-1)
        # on 0 < lambda <= split <= 1.
        c1 += magnitude * power * index
        power *= split

    lam = ZERO.union(split)
    p = polynomial(lam, target)
    pp = polynomial_derivative(lam, target)
    h = -(pp - p) * (-lam).exp()

    # q=exp(-F')=lambda/(1+lambda) exp(h).  These coefficients satisfy
    # q_lo*lambda <= q <= q_hi*lambda throughout the interval.
    q_lo = h.lower().exp() / (ONE + split)
    q_hi = h.upper().exp()
    if not q_hi * split < ONE:
        raise AssertionError("small-regime q<1 was not proved")

    # With M=lambda exp(-lambda),
    #   -log X <= A lambda,
    #   Y=1-X >= M+q-Mq >= D lambda.
    a_coefficient = ONE / (ONE - split) + q_hi / (
        (ONE - split) * (ONE - q_hi * split)
    )
    d_coefficient = (-split).exp() + q_lo - q_hi * split
    if not d_coefficient > ZERO:
        raise AssertionError("small-regime Y lower coefficient is not positive")

    # Entropy >= -lambda log(lambda)+lambda and |p|<=C0 lambda give
    # F>0.  Also F'>=log(1/lambda)-C1>0.
    if not -split.log() + ONE - c0 > ZERO:
        raise AssertionError("small-regime F positivity was not proved")
    if not -split.log() - c1 > ZERO:
        raise AssertionError("small-regime F' positivity was not proved")

    # Substituting log M=log lambda-lambda and
    # log Y>=log lambda+log D cancels the singular lambda log lambda terms.
    normalized_slack = (
        ONE - c0 - a_coefficient / 2 + d_coefficient.log() / 2 - split / 2
    )
    if not normalized_slack > ZERO:
        raise AssertionError(
            f"small-regime normalized main slack was not proved: {normalized_slack}"
        )
    return normalized_slack


def verify_small_intervals(target: list[arb], split: arb) -> float:
    """Redundant Arb check of ``Y=1-X`` on ``[10^-5, split]``."""
    count = 512
    tail = parse("1e-5")
    ratio = (split / tail) ** (ONE / count)
    lo = tail
    worst = math.inf
    for index in range(count):
        hi = split if index + 1 == count else lo * ratio
        lam = ball_interval(lo, hi)
        f = rate(lam, target)
        fp = rate_prime(lam, target)
        if not f > ZERO or not fp > ZERO:
            raise AssertionError(f"small cell {index}: F/F' positivity failed")
        m = lam * (-lam).exp()
        log_x = (ONE - m).log() + (ONE - (-fp).exp()).log() / (ONE - m)
        x = log_x.exp()
        y = ONE - x
        if not y > ZERO or not y < ONE:
            raise AssertionError(f"small cell {index}: Y range failed")
        slack = f + HALF * (log_x + lam * m.log() + lam * y.log())
        if not slack > ZERO:
            raise AssertionError(f"small cell {index}: main slack failed: {slack}")
        worst = min(worst, lower_float(slack))
        lo = hi
    return worst


def verify_segments(payload: dict, target: list[arb], prior: list[arb], split: arb) -> dict:
    segments = payload["segments"]
    expected_left = split
    worst_main = (math.inf, None)
    worst_standard = (math.inf, None)
    worst_swapped = (math.inf, None)
    min_f = math.inf
    min_fp = math.inf

    for index, segment in enumerate(segments):
        lo, hi = parse(segment["lo"]), parse(segment["hi"])
        if not (lo - expected_left).contains(0):
            raise AssertionError(f"coverage gap/overlap before segment {index}")
        if not hi > lo:
            raise AssertionError(f"non-positive segment width at {index}")
        expected_left = hi

        lam = ball_interval(lo, hi)
        m, y = parse(segment["M"]), parse(segment["Y"])
        if not m > ZERO or not m < ONE or not y > ZERO or not y < ONE:
            raise AssertionError(f"M/Y range failure at segment {index}")

        f = rate(lam, target)
        fp = rate_prime(lam, target)
        if not f > ZERO or not fp > ZERO:
            raise AssertionError(f"F/F' positivity failure at segment {index}")
        min_f = min(min_f, lower_float(f))
        min_fp = min(min_fp, lower_float(fp))

        log_x = (ONE - m).log() + (ONE - (-fp).exp()).log() / (ONE - m)
        x = log_x.exp()
        if not x > ZERO or not x < ONE:
            raise AssertionError(f"X range failure at segment {index}")
        a = -log_x
        b = -y.log()

        std_lb, swap_lb = region_margins_over_lambda(
            lo, hi, m, b, target, prior
        )
        if std_lb < worst_standard[0]:
            worst_standard = (std_lb, index)
        if swap_lb < worst_swapped[0]:
            worst_swapped = (swap_lb, index)

        slack_lb = main_slack_over_lambda(lo, hi, m, y, target)
        if slack_lb < worst_main[0]:
            worst_main = (slack_lb, index)

    if not (expected_left - ONE).contains(0):
        raise AssertionError("segments do not cover through lambda=1")

    return {
        "segments": len(segments),
        "min_F": min_f,
        "min_F_prime": min_fp,
        "worst_standard_region_margin": worst_standard,
        "worst_swapped_region_margin": worst_swapped,
        "worst_large_main_slack": worst_main,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.certificate.read_text(encoding="utf-8"))
    if payload.get("schema") != "corrected-two-sided-ramsey-v1":
        raise AssertionError("unexpected certificate schema")

    prior = [parse(item) for item in payload["prior_coefficients"]]
    target = [parse(item) for item in payload["target_coefficients"]]
    split = parse(payload["lambda_split"])
    concavity_upper, small_correction_upper = prove_prior_concavity(prior)
    prior_small, prior_large = certify_elementary_prior(prior, split)
    normalized_small_slack = prove_small_regime(target, split)
    large = verify_segments(payload, target, prior, split)

    f1 = rate(ONE, target)
    growth_base = f1.exp()
    print("PASS: corrected two-sided Arb certificate")
    print(f"prior U'' worst certified upper bound: {concavity_upper:.17g}")
    print(f"prior small-mu correction certified upper bound: {small_correction_upper:.17g}")
    print(f"prior elementary small-regime slack/lambda: {prior_small}")
    print(f"prior elementary worst [split,1] slack: {prior_large:.17g}")
    print(f"analytic small-regime endpoint: {split}")
    print(f"analytic lower bound for slack/lambda: {normalized_small_slack}")
    for key, value in large.items():
        print(f"{key}: {value}")
    print(f"F(1): {f1}")
    print(f"growth base exp(F(1)): {growth_base}")


if __name__ == "__main__":
    main()
