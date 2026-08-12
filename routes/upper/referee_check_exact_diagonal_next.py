#!/usr/bin/env python3
"""Independent adaptive 512-bit replay for the exact-diagonal candidate.

This referee program imports no author checker.  It uses adaptive dyadic
subdivision rather than any of the fixed grids in the frozen package and
reconstructs the inner functions, the degree-14 rate, and the outer wedge.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

import flint
from flint import arb, ctx


ctx.prec = 512
HERE = Path(__file__).resolve().parent
ZERO = arb(0)
ONE = arb(1)

FROZEN = {
    "EXACT_DIAGONAL_NEXT_PROTOCOL.md":
        "7fa44c0ae2755f0e1dbb436a9cf3a6b0f50867d3fcb8df0e74bb13c394636827",
    "EXACT_DIAGONAL_NEXT_CANDIDATE.md":
        "e4ea58def640593690a7545e111c3b38f1bfcf8a5735fe7985600481e0bf36d4",
    "check_exact_diagonal_next.py":
        "17db00d9374ce3ba3e68a3a4626ec2c51a70ec45a307972dacc245b153382c3e",
    "check_retained_spine_exact_diagonal_next.py":
        "e2035cbffefcb147141fcee4831cac2af085f26d9183091ee20d90acc89ac87b",
    "independent_check_exact_diagonal_next.py":
        "fc379e3b861b69054aadaa80ebc3c791cb8358f22c9b0aa01070c56aa131c26c",
    "certificate-higher-order-tetradecic-chain-v6.json":
        "8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def aq(value: Fraction | int) -> arb:
    value = Fraction(value)
    return arb(value.numerator) / value.denominator


def hull(lo: Fraction, hi: Fraction) -> arb:
    return aq(lo).union(aq(hi))


def filters(u: arb) -> tuple[arb, arb, arb, arb]:
    root_three = arb(3).sqrt()
    angle = root_three * u / 2
    cosine = angle.cos()
    sine = angle.sin()
    eu = u.exp()
    emu = (-u).exp()
    ehalf = (u / 2).exp()
    emhalf = (-u / 2).exp()
    positive = (eu + 2 * emhalf * cosine) / 3
    negative = (emu + 2 * ehalf * cosine) / 3
    positive_prime = (
        eu - emhalf * cosine - root_three * emhalf * sine
    ) / 3
    negative_prime = (
        -emu + ehalf * cosine - root_three * ehalf * sine
    ) / 3
    return positive, negative, positive_prime, negative_prime


def adaptive_sign(function, lo: Fraction, hi: Fraction, positive: bool,
                  max_depth: int = 30) -> tuple[int, int, arb]:
    """Prove a strict sign by adaptive dyadic subdivision."""
    stack = [(lo, hi, 0)]
    leaves = 0
    deepest = 0
    weakest = None
    while stack:
        left, right, depth = stack.pop()
        value = function(left, right)
        resolved = value > ZERO if positive else value < ZERO
        if resolved:
            leaves += 1
            deepest = max(deepest, depth)
            if weakest is None:
                weakest = value
            elif positive and value.lower() < weakest.lower():
                weakest = value
            elif not positive and value.upper() > weakest.upper():
                weakest = value
            continue
        if depth >= max_depth:
            raise AssertionError((left, right, depth, value))
        middle = (left + right) / 2
        stack.append((middle, right, depth + 1))
        stack.append((left, middle, depth + 1))
    assert weakest is not None
    return leaves, deepest, weakest


def polynomial(coefficients: list[arb], x: arb) -> arb:
    total = ZERO
    power = x
    for coefficient in coefficients:
        total += coefficient * power
        power *= x
    return total


def polynomial_prime(coefficients: list[arb], x: arb) -> arb:
    total = ZERO
    power = ONE
    for degree, coefficient in enumerate(coefficients, start=1):
        total += degree * coefficient * power
        power *= x
    return total


def polynomial_second(coefficients: list[arb], x: arb) -> arb:
    total = ZERO
    power = ONE
    for degree, coefficient in enumerate(coefficients[1:], start=2):
        total += degree * (degree - 1) * coefficient * power
        power *= x
    return total


def rate(coefficients: list[arb], x: arb) -> arb:
    entropy = (ONE + x) * (ONE + x).log() - x * x.log()
    return entropy + polynomial(coefficients, x) * (-x).exp()


def rate_prime(coefficients: list[arb], x: arb) -> arb:
    p = polynomial(coefficients, x)
    dp = polynomial_prime(coefficients, x)
    return ((ONE + x) / x).log() + (dp - p) * (-x).exp()


def rate_second(coefficients: list[arb], x: arb) -> arb:
    p = polynomial(coefficients, x)
    dp = polynomial_prime(coefficients, x)
    ddp = polynomial_second(coefficients, x)
    return -ONE / (x * (ONE + x)) + (ddp - 2 * dp + p) * (-x).exp()


def main() -> None:
    assert flint.__version__ == "0.9.0"
    for name, expected in FROZEN.items():
        assert sha256(HERE / name) == expected, name

    u0_f = Fraction(1_235_783, 500_000)
    sigma0_f = Fraction(1, 100_000_000)
    target_f = Fraction(100_000_001, 50_000_000)
    separator_f = Fraction(50_000_001, 100_000_000)
    growth_f = Fraction(88_053, 1_000_000_000)
    beta_f = Fraction(330_867, 500_000)
    epsilon_f = Fraction(6_893, 10_000_000)
    correlation_f = Fraction(12_366_348_252_219, 1_250_000_000_000)
    assert target_f == 2 + 2 * sigma0_f
    assert separator_f == (1 + 2 * sigma0_f) / 2
    assert correlation_f == 4 * u0_f * (1 + epsilon_f)

    u0 = aq(u0_f)
    target = aq(target_f)
    growth = aq(growth_f)
    a = (-u0).exp()

    p0, n0, _, _ = filters(u0)
    ratio_endpoint = (ONE + a * p0**2) / (ONE + a * n0**2) - target
    assert ratio_endpoint > ZERO

    def ratio_derivative(left: Fraction, right: Fraction) -> arb:
        p, n, dp, dn = filters(hull(left, right))
        hp = ONE + a * p**2
        hn = ONE + a * n**2
        return p * dp * hn - n * dn * hp

    ratio_leaves, ratio_depth, ratio_weakest = adaptive_sign(
        ratio_derivative, u0_f, Fraction(29, 10), True
    )

    switch = aq(Fraction(29, 10))
    eu = switch.exp()
    eh = (switch / 2).exp()
    em = (-switch).exp()
    emh = (-switch / 2).exp()
    bracket = (
        eu**2 - 4 * target * eu - 4 * eh - 4 * target * emh
        + 4 * em - target * em**2
    )
    tail_cross_margin = a * bracket - 9 * (target - ONE)
    d0 = 2 * eu * (eu - 2 * target) - 2 * eh - 4 * em
    # Persistence is analytic: e^u>T+1 implies
    # D0'=4e^u(e^u-T)-e^(u/2)+4e^-u > 4e^u-e^(u/2)>0.
    persistence = eu - (target + ONE)
    assert tail_cross_margin > ZERO
    assert d0 > ZERO
    assert persistence > ZERO

    cutoff_f = Fraction(20)

    def diagonal_slack(left: Fraction, right: Fraction) -> arb:
        u = hull(left, right)
        w = aq(left**3 + u0_f**3) ** (ONE / 3)
        w = w.union(aq(right**3 + u0_f**3) ** (ONE / 3))
        p, n, _, _ = filters(u)
        hp = ONE + a * p**2
        hn = ONE + a * n**2
        exact_diagonal = hp**2 - hp * hn
        return growth - exact_diagonal / (4 * w).exp()

    diagonal_leaves, diagonal_depth, diagonal_weakest = adaptive_sign(
        diagonal_slack, Fraction(0), cutoff_f, True, max_depth=35
    )

    cutoff = aq(cutoff_f)
    oscillation = ONE + 2 * (-3 * cutoff / 2).exp()
    tail_upper = (
        a / 9 * (-2 * cutoff).exp() * oscillation**2
        + a**2 / 81 * oscillation**4
    )
    tail_slack = growth - tail_upper
    asymptotic_slack = growth - a**2 / 81
    assert tail_slack > aq(Fraction(1, 10_000_000_000))
    assert asymptotic_slack > aq(Fraction(1, 10_000_000_000))

    tail_cost = growth_f * beta_f * (1 + Fraction(2) / epsilon_f)
    tail_credit = separator_f * (1 - beta_f)
    tail_budget = tail_credit - tail_cost
    assert tail_budget == Fraction(
        39_437_634_699_447, 3_446_500_000_000_000_000
    )
    assert tail_budget > Fraction(1, 100_000)

    payload = json.loads(
        (HERE / "certificate-higher-order-tetradecic-chain-v6.json")
        .read_text(encoding="utf-8")
    )
    coefficient_fractions = [
        Fraction(str(value)) for value in payload["target_coefficients"]
    ]
    assert len(coefficient_fractions) == 14
    coefficients = [aq(value) for value in coefficient_fractions]

    split_f = Fraction(1, 4096)
    split = aq(split_f)
    small = hull(Fraction(0), split_f)
    correction = (
        polynomial_second(coefficients, small)
        - 2 * polynomial_prime(coefficients, small)
        + polynomial(coefficients, small)
    ) * (-small).exp()
    small_concavity = -ONE / (split * (ONE + split)) + correction
    assert small_concavity < ZERO

    def concavity(left: Fraction, right: Fraction) -> arb:
        return rate_second(coefficients, hull(left, right))

    concavity_leaves, concavity_depth, concavity_weakest = adaptive_sign(
        concavity, split_f, Fraction(1), False, max_depth=35
    )

    eta = aq(Fraction(2_868_896, 100_000_000))
    probability = aq(Fraction(47_130_887, 100_000_000))
    book_delta = aq(Fraction(53_863, 1_000_000_000))
    lambda_zero = aq(Fraction(13_233))
    tau = aq(Fraction(69_386, 100_000_000))
    gap = aq(Fraction(34_754, 10_000_000_000))
    beta = aq(beta_f)
    correlation = aq(correlation_f)

    c_eta = (2 / (ONE + eta)).log()
    log_delta = (ONE / book_delta).log()
    log_probability = (ONE / probability).log()
    page_cost = (
        log_probability + 3 * book_delta / probability
        + 6 * log_delta * log_probability / lambda_zero
    )
    rho = (2 / beta).log()
    xi = (
        2 * rho + 4 * correlation * lambda_zero ** (ONE / 3)
        + 12 * correlation * log_delta / lambda_zero ** (aq(Fraction(2, 3)))
    )
    u_one = rate(coefficients, ONE)
    up_one = rate_prime(coefficients, ONE)
    diagonal_gain = u_one - 2 * c_eta
    axis_gain = up_one - c_eta
    degree_slack = tau * (ONE / 2 - eta - probability)
    assert degree_slack >= aq(Fraction(1, 1_000_000_000))
    assert ZERO < diagonal_gain < axis_gain

    r_axis = gap / axis_gain
    r_diagonal = gap / diagonal_gain
    slope = ONE - diagonal_gain / axis_gain
    assert ZERO < r_axis < tau < r_diagonal < ONE
    assert ZERO < slope < ONE
    z_low = ONE - tau / (ONE - r_diagonal)
    z_high = (ONE - tau) / (ONE - r_axis)
    assert ZERO < z_low < z_high < ONE

    # Concavity makes the two coordinate signs and the boundary derivative
    # reducible to z_high.  This is a different proof from the author's
    # 8192-cell boundary sampling.
    red_x = c_eta - rate_prime(coefficients, z_high)
    red_y = (
        c_eta - rate(coefficients, z_high)
        + z_high * rate_prime(coefficients, z_high)
    )
    red_boundary = red_x + slope * red_y
    assert red_x < ZERO
    assert red_y > ZERO
    assert slope * z_high < ONE
    assert red_boundary < ZERO

    red_page = (
        c_eta * r_axis + tau * page_cost
        + (ONE - r_axis)
        * rate(coefficients, (ONE - tau) / (ONE - r_axis))
    )
    red_margin = u_one - gap - red_page

    # On the blue page, d/dy<0.  On y=x the derivative decreases because
    # its derivative with respect to s=tau/(1-x) is s U''(1-s)<0.
    blue_y = c_eta - rate_prime(coefficients, ONE - tau)
    blue_diagonal = (
        2 * c_eta - rate(coefficients, ONE - tau)
        - tau * rate_prime(coefficients, ONE - tau)
    )
    assert blue_y < ZERO
    assert blue_diagonal < ZERO
    blue_page = tau * page_cost + rate(coefficients, ONE - tau)
    blue_margin = u_one - gap - blue_page

    reservoir_margin = (
        u_one - gap - 2 * c_eta * r_diagonal - 2 * tau * xi
    )
    for margin in (red_margin, blue_margin, reservoir_margin):
        assert margin >= aq(Fraction(1, 1_000_000_000))

    base = (u_one - gap).exp()
    previous_base = (
        u_one - aq(Fraction(34_727, 10_000_000_000))
    ).exp()
    actual_improvement = previous_base - base
    safe = aq(Fraction(3_780_685_290, 1_000_000_000))
    rounding = safe - base
    assert actual_improvement >= aq(Fraction(1, 100_000_000))
    assert rounding >= aq(Fraction(1, 1_000_000_000))

    print("PASS: independent adaptive 512-bit exact-diagonal referee replay")
    print(f"precision_bits: {ctx.prec}")
    print(f"ratio_endpoint_slack: {ratio_endpoint.lower()}")
    print(f"ratio_adaptive_leaves: {ratio_leaves}")
    print(f"ratio_adaptive_max_depth: {ratio_depth}")
    print(f"ratio_worst_lower: {ratio_weakest.lower()}")
    print(f"tail_cross_margin: {tail_cross_margin.lower()}")
    print(f"diagonal_adaptive_leaves: {diagonal_leaves}")
    print(f"diagonal_adaptive_max_depth: {diagonal_depth}")
    print(f"diagonal_worst_lower: {diagonal_weakest.lower()}")
    print(f"tail_slack_lower: {tail_slack.lower()}")
    print(f"asymptotic_slack_lower: {asymptotic_slack.lower()}")
    print(f"tail_budget_exact: {tail_budget}")
    print(f"correlation_C_exact: {correlation_f}")
    print(f"concavity_adaptive_leaves: {concavity_leaves}")
    print(f"concavity_adaptive_max_depth: {concavity_depth}")
    print(f"concavity_worst_upper: {concavity_weakest.upper()}")
    print(f"degree_slack: {degree_slack.lower()}")
    print(f"red_boundary_upper: {red_boundary.upper()}")
    print(f"red_margin: {red_margin.lower()}")
    print(f"blue_diagonal_upper: {blue_diagonal.upper()}")
    print(f"blue_margin: {blue_margin.lower()}")
    print(f"reservoir_margin: {reservoir_margin.lower()}")
    print(f"base_upper: {base.upper()}")
    print(f"actual_improvement_lower: {actual_improvement.lower()}")
    print(f"rounding_margin_lower: {rounding.lower()}")


if __name__ == "__main__":
    main()
