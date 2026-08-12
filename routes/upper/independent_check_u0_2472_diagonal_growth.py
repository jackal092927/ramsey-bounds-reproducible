#!/usr/bin/env python3
"""Genuinely non-importing 512-bit replay of the u0=309/125 candidate.

This program imports no author checker.  It reconstructs the root filters,
the ratio and diagonal-growth proofs, the degree-14 rate and derivatives,
and the retained-spine wedge.  It uses finer inner grids and endpoint
monotonicity arguments in place of the author's outer derivative grids.
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


FROZEN_SHA256 = {
    "U0_2472_DIAGONAL_GROWTH_CANDIDATE.md":
        "5900745028807c817fdb92dd0f6caf9df435df5106bfe2fd4309d8afe173a738",
    "check_u0_2472_diagonal_growth.py":
        "f10e9f43e6666e11e916fe4d9998fe3e9ff7fd4b9b42750e48b5fdd5c1d1f5d9",
    "check_retained_spine_u0_2472.py":
        "a04f44b931f27225ad7d75caa013d72176a185e94fb08aacb17643e2083fe682",
    "certificate-higher-order-tetradecic-chain-v6.json":
        "8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8",
    "RETAINED_SPINE_TRANSFER_ATTEMPT.md":
        "5aa5d6cb1ee1cc2d9f4d34b8564b6c57f78cfd7444a89abcfbb64542274e4aaa",
    "INDEPENDENT_RETAINED_SPINE_REFEREE.md":
        "6ba57fdbe13bf45255644ae94af5474b7a34afda3aefeda26415f3cc3f9b66db",
    "check_retained_spine_transfer.py":
        "b10815b10cb3ab922aa079ee74289c52239ec90939ed41b93907bf06a60ee274",
    "verify_region_direct_arb.py":
        "e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe",
    "HYBRID_CORRELATION_SHARPENING.md":
        "4b29c692dd1fc96859491b25d61c9b0e1124a33cf57a45ef01abb5a2e49ed30d",
    "STRONG_SEPARATOR_GROWTH_SHARPENING.md":
        "80b5ae4d663194623b4b6222181792d1bf71f5f73684133d84f936ed1807fefb",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def q(numerator: int, denominator: int = 1) -> arb:
    return arb(numerator) / denominator


def exact(value: Fraction) -> arb:
    return q(value.numerator, value.denominator)


def hull(lo: arb, hi: arb) -> arb:
    return lo.union(hi)


def filters(u: arb) -> tuple[arb, arb, arb, arb]:
    """Independent reconstruction of both cubic filters and derivatives."""
    s = arb(3).sqrt()
    theta = s * u / 2
    c = theta.cos()
    sn = theta.sin()
    ep = u.exp()
    en = (-u).exp()
    eh = (u / 2).exp()
    emh = (-u / 2).exp()
    p = (ep + 2 * emh * c) / 3
    n = (en + 2 * eh * c) / 3
    dp = (ep - emh * c - s * emh * sn) / 3
    dn = (-en + eh * c - s * eh * sn) / 3
    return p, n, dp, dn


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
    value = polynomial(coefficients, x)
    derivative = polynomial_prime(coefficients, x)
    return ((ONE + x) / x).log() + (derivative - value) * (-x).exp()


def rate_second(coefficients: list[arb], x: arb) -> arb:
    value = polynomial(coefficients, x)
    derivative = polynomial_prime(coefficients, x)
    second = polynomial_second(coefficients, x)
    return -ONE / (x * (ONE + x)) + (
        second - 2 * derivative + value
    ) * (-x).exp()


def replay_concavity(coefficients: list[arb]) -> arb:
    split = ONE / 65_536
    small = hull(ZERO, split)
    correction = (
        polynomial_second(coefficients, small)
        - 2 * polynomial_prime(coefficients, small)
        + polynomial(coefficients, small)
    ) * (-small).exp()
    worst = -ONE / (split * (ONE + split)) + correction
    assert worst < ZERO
    cells = 65_536
    for cell in range(cells):
        lo = split + (ONE - split) * cell / cells
        hi = split + (ONE - split) * (cell + 1) / cells
        enclosure = rate_second(coefficients, hull(lo, hi))
        assert enclosure < ZERO, (cell, enclosure)
        if enclosure.upper() > worst.upper():
            worst = enclosure
    return worst


def replay_inner() -> dict[str, object]:
    u0_f = Fraction(309, 125)
    sigma0_f = Fraction(1, 10_000)
    target_f = Fraction(10_001, 5_000)
    separator_f = Fraction(5_001, 10_000)
    growth_f = Fraction(89, 1_000_000)
    beta_f = Fraction(833, 1250)
    epsilon_f = Fraction(7113, 10_000_000)
    c_f = Fraction(3_092_197_917, 312_500_000)
    assert target_f == 2 + 2 * sigma0_f
    assert separator_f == (1 + 2 * sigma0_f) / 2
    assert c_f == 4 * u0_f * (1 + epsilon_f)

    u0 = exact(u0_f)
    a = (-u0).exp()
    target = exact(target_f)
    growth = exact(growth_f)
    switch = q(29, 10)

    p, n, _, _ = filters(u0)
    endpoint_slack = (ONE + a * p**2) / (ONE + a * n**2) - target
    assert endpoint_slack > q(1, 100_000)

    # Four times the author's cell count.
    ratio_cells = 131_072
    ratio_worst = None
    ratio_cell = None
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
            ratio_cell = cell

    eu = switch.exp()
    eh = (switch / 2).exp()
    em = (-switch).exp()
    emh = (-switch / 2).exp()
    p_lower = (eu - 2 * emh) / 3
    n_upper = (2 * eh + em) / 3
    tail_ratio = (
        (ONE + a * p_lower**2) / (ONE + a * n_upper**2) - target
    )
    bracket = (
        eu**2 - 4 * target * eu - 4 * eh - 4 * target * emh
        + 4 * em - target * em**2
    )
    k_switch = a * bracket - 9 * (target - ONE)
    derivative = 2 * eu * (eu - 2 * target) - 2 * eh - 4 * em
    derivative_prime = 4 * eu**2 - 4 * target * eu - eh + 4 * em
    assert p_lower > ZERO
    assert tail_ratio > q(3, 10)
    assert k_switch > ZERO
    assert derivative > ZERO
    assert derivative_prime > ZERO

    # Eight times the author's negative-axis grid.
    assert (a * u0.exp() - ONE).contains(0)
    negative_cells = 131_072
    negative_worst = None
    for cell in range(negative_cells):
        v = hull(u0 * cell / negative_cells,
                 u0 * (cell + 1) / negative_cells)
        negative = filters(v)[1]
        slack = 2 - (ONE + a * negative**2)
        assert slack > ZERO, (cell, slack)
        if negative_worst is None or slack.lower() < negative_worst.lower():
            negative_worst = slack

    # Twice the author's compact grid, with w built solely from endpoint
    # images to avoid a repeated-variable dependency.
    cutoff = q(20)
    growth_cells = 131_072
    growth_worst = None
    growth_cell = None
    for cell in range(growth_cells):
        lo = cutoff * cell / growth_cells
        hi = cutoff * (cell + 1) / growth_cells
        u = hull(lo, hi)
        w = hull((lo**3 + u0**3) ** (ONE / 3),
                 (hi**3 + u0**3) ** (ONE / 3))
        p, n, _, _ = filters(u)
        hp = ONE + a * p**2
        hn = ONE + a * n**2
        slack = growth - (hp**2 - hn**2) / (4 * w).exp()
        assert slack > ZERO, (cell, slack)
        if growth_worst is None or slack.lower() < growth_worst.lower():
            growth_worst = slack
            growth_cell = cell

    oscillation = ONE + 2 * (-3 * cutoff / 2).exp()
    tail_upper = (
        2 * a / 9 * (-2 * cutoff).exp() * oscillation**2
        + a**2 / 81 * oscillation**4
    )
    tail_slack = growth - tail_upper
    asymptotic_slack = growth - a**2 / 81
    assert tail_slack > q(1, 1_000_000)
    assert asymptotic_slack > q(1, 10_000_000)

    cost = growth_f * beta_f * (1 + Fraction(2, 1) / epsilon_f)
    credit = separator_f * (1 - beta_f)
    budget = credit - cost
    assert budget == Fraction(89_775_619, 8_891_250_000_000)
    assert budget > Fraction(1, 100_000)

    return {
        "ratio_endpoint_slack": endpoint_slack,
        "ratio_cells": ratio_cells,
        "ratio_worst_cell": ratio_cell,
        "ratio_derivative_worst_lower": ratio_worst.lower(),
        "tail_ratio_slack": tail_ratio,
        "negative_cells": negative_cells,
        "negative_worst_slack_lower": negative_worst.lower(),
        "growth_cells": growth_cells,
        "growth_worst_cell": growth_cell,
        "growth_worst_slack_lower": growth_worst.lower(),
        "growth_tail_upper": tail_upper,
        "growth_tail_slack": tail_slack,
        "growth_asymptotic_slack": asymptotic_slack,
        "tail_cost_exact": cost,
        "tail_credit_exact": credit,
        "tail_budget_exact": budget,
        "correlation_C_exact": c_f,
    }


def replay_outer() -> dict[str, object]:
    payload = json.loads(
        (HERE / "certificate-higher-order-tetradecic-chain-v6.json")
        .read_text(encoding="utf-8")
    )
    assert payload.get("schema") == "corrected-two-sided-ramsey-v1"
    fractions = [Fraction(str(value)) for value in payload["target_coefficients"]]
    coefficients = [exact(value) for value in fractions]
    assert len(coefficients) == 14

    eta = q(2_868_925, 100_000_000)
    probability = q(47_130_784, 100_000_000)
    book_delta = q(53_934, 1_000_000_000)
    lambda_zero = q(13_235)
    tau = q(69_374, 100_000_000)
    gap = q(34_727, 10_000_000_000)

    beta_f = Fraction(833, 1250)
    epsilon_f = Fraction(7113, 10_000_000)
    u0_f = Fraction(309, 125)
    correlation_f = Fraction(3_092_197_917, 312_500_000)
    assert correlation_f == 4 * u0_f * (1 + epsilon_f)
    beta = exact(beta_f)
    correlation = exact(correlation_f)

    c_eta = (2 / (ONE + eta)).log()
    log_delta = (ONE / book_delta).log()
    log_probability = (ONE / probability).log()
    page_cost = (
        log_probability + 3 * book_delta / probability
        + 6 * log_delta * log_probability / lambda_zero
    )
    rho = (2 / beta).log()
    xi_cost = (
        2 * rho + 4 * correlation * lambda_zero ** (ONE / 3)
        + 12 * correlation * log_delta / lambda_zero ** (q(2, 3))
    )

    assert ZERO < eta
    assert ZERO < probability < ONE / 2 - eta
    assert ZERO < book_delta <= probability / 4
    assert book_delta <= ONE / 4
    assert lambda_zero >= 2
    assert lambda_zero >= 6 * log_delta
    assert ZERO < tau < ONE
    degree_slack = tau * (ONE / 2 - eta - probability)
    assert degree_slack > q(1, 1_000_000_000)

    concavity = replay_concavity(coefficients)
    u_one = rate(coefficients, ONE)
    up_one = rate_prime(coefficients, ONE)
    diagonal = u_one - 2 * c_eta
    off_diagonal = up_one - c_eta
    assert ZERO < diagonal < off_diagonal
    assert page_cost < up_one
    assert 2 * tau * xi_cost < u_one

    r_axis = gap / off_diagonal
    r_diag = gap / diagonal
    slope = ONE - diagonal / off_diagonal
    assert ZERO < r_axis < tau < r_diag < ONE
    assert ZERO < slope < ONE

    z_lo = ONE - tau / (ONE - r_diag)
    z_hi = (ONE - tau) / (ONE - r_axis)
    assert ZERO < z_lo < z_hi < ONE

    # Independent analytic endpoint proof for the full red boundary.
    # Concavity makes U' decrease and U-zU' increase.  Moreover the boundary
    # derivative B has B'(z)=(slope*z-1)U''(z)>0.  Hence its maximum is z_hi.
    red_x = c_eta - rate_prime(coefficients, z_hi)
    red_y = (
        c_eta - rate(coefficients, z_hi)
        + z_hi * rate_prime(coefficients, z_hi)
    )
    assert red_x < ZERO
    assert red_y > ZERO
    assert slope * z_hi < ONE
    red_boundary = red_x + slope * red_y
    assert red_boundary < ZERO

    red_page = (
        c_eta * r_axis + tau * page_cost
        + (ONE - r_axis)
        * rate(coefficients, (ONE - tau) / (ONE - r_axis))
    )
    red_margin = u_one - gap - red_page
    assert red_margin > q(1, 1_000_000_000)

    # Concavity also shows both relevant blue derivatives attain their
    # maxima at the origin, avoiding the author's diagonal cell grid.
    blue_y = c_eta - rate_prime(coefficients, ONE - tau)
    blue_diagonal = (
        2 * c_eta - rate(coefficients, ONE - tau)
        - tau * rate_prime(coefficients, ONE - tau)
    )
    assert blue_y < ZERO
    assert blue_diagonal < ZERO
    blue_page = tau * page_cost + rate(coefficients, ONE - tau)
    blue_margin = u_one - gap - blue_page
    assert blue_margin > q(1, 1_000_000_000)

    reservoir = 2 * c_eta * r_diag + 2 * tau * xi_cost
    reservoir_margin = u_one - gap - reservoir
    assert reservoir_margin > q(1, 1_000_000_000)

    base = (u_one - gap).exp()
    safe = q(3_780_685_300, 1_000_000_000)
    old_safe = q(3_780_685_320, 1_000_000_000)
    rounding = safe - base
    improvement = old_safe - safe
    assert rounding > q(1, 1_000_000_000)
    assert improvement >= q(1, 100_000_000)

    return {
        "correlation_C_exact": correlation_f,
        "rho": rho,
        "q": page_cost,
        "Xi": xi_cost,
        "concavity_worst_upper": concavity.upper(),
        "degree_slack": degree_slack,
        "red_boundary_upper": red_boundary,
        "red_page_margin": red_margin,
        "blue_diagonal_upper": blue_diagonal,
        "blue_page_margin": blue_margin,
        "reservoir_margin": reservoir_margin,
        "base_upper": base,
        "safe_decimal": Fraction(3_780_685_300, 1_000_000_000),
        "rounding_margin": rounding,
        "safe_improvement": improvement,
    }


def main() -> None:
    assert flint.__version__ == "0.9.0"
    for name, expected in FROZEN_SHA256.items():
        actual = sha256(HERE / name)
        assert actual == expected, (name, actual, expected)

    inner = replay_inner()
    outer = replay_outer()
    assert inner["correlation_C_exact"] == outer["correlation_C_exact"]

    print("PASS: non-importing 512-bit u0=309/125 replay")
    print(f"python_flint_version: {flint.__version__}")
    print(f"precision_bits: {ctx.prec}")
    for name, value in inner.items():
        print(f"inner_{name}: {value}")
    for name, value in outer.items():
        print(f"outer_{name}: {value}")


if __name__ == "__main__":
    main()
