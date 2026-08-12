#!/usr/bin/env python3
"""Non-importing 512-bit replay of the exact-diagonal next candidate."""

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
    "EXACT_DIAGONAL_NEXT_PROTOCOL.md":
        "7fa44c0ae2755f0e1dbb436a9cf3a6b0f50867d3fcb8df0e74bb13c394636827",
    "EXACT_DIAGONAL_NEXT_CANDIDATE.md":
        "e4ea58def640593690a7545e111c3b38f1bfcf8a5735fe7985600481e0bf36d4",
    "check_exact_diagonal_next.py":
        "17db00d9374ce3ba3e68a3a4626ec2c51a70ec45a307972dacc245b153382c3e",
    "check_retained_spine_exact_diagonal_next.py":
        "e2035cbffefcb147141fcee4831cac2af085f26d9183091ee20d90acc89ac87b",
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


def root_filters(u: arb) -> tuple[arb, arb, arb, arb]:
    s = arb(3).sqrt()
    t = s * u / 2
    c = t.cos()
    sn = t.sin()
    ep = u.exp()
    em = (-u).exp()
    eh = (u / 2).exp()
    emh = (-u / 2).exp()
    positive = (ep + 2 * emh * c) / 3
    negative = (em + 2 * eh * c) / 3
    positive_prime = (ep - emh * c - s * emh * sn) / 3
    negative_prime = (-em + eh * c - s * eh * sn) / 3
    return positive, negative, positive_prime, negative_prime


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


def prove_concavity(coefficients: list[arb]) -> arb:
    split = ONE / 65_536
    small = hull(ZERO, split)
    correction = (
        polynomial_second(coefficients, small)
        - 2 * polynomial_prime(coefficients, small)
        + polynomial(coefficients, small)
    ) * (-small).exp()
    worst = -ONE / (split * (ONE + split)) + correction
    assert worst < ZERO
    for cell in range(65_536):
        lo = split + (ONE - split) * cell / 65_536
        hi = split + (ONE - split) * (cell + 1) / 65_536
        enclosure = rate_second(coefficients, hull(lo, hi))
        assert enclosure < ZERO, (cell, enclosure)
        if enclosure.upper() > worst.upper():
            worst = enclosure
    return worst


def inner_replay() -> dict[str, object]:
    u0_f = Fraction(1_235_783, 500_000)
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

    u0 = exact(u0_f)
    target = exact(target_f)
    growth = exact(growth_f)
    a = (-u0).exp()
    p, n, _, _ = root_filters(u0)
    endpoint = (ONE + a * p**2) / (ONE + a * n**2) - target
    assert endpoint > q(1, 10_000_000)

    switch = q(29, 10)
    ratio_cells = 131_072
    ratio_worst = None
    ratio_cell = None
    for cell in range(ratio_cells):
        lo = u0 + (switch - u0) * cell / ratio_cells
        hi = u0 + (switch - u0) * (cell + 1) / ratio_cells
        p, n, dp, dn = root_filters(hull(lo, hi))
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

    assert (a * u0.exp() - ONE).contains(0)
    negative_cells = 131_072
    negative_worst = None
    for cell in range(negative_cells):
        v = hull(u0 * cell / negative_cells,
                 u0 * (cell + 1) / negative_cells)
        n = root_filters(v)[1]
        slack = 2 - (ONE + a * n**2)
        assert slack > ZERO, (cell, slack)
        if negative_worst is None or slack.lower() < negative_worst.lower():
            negative_worst = slack

    cutoff = q(20)
    diagonal_cells = 262_144
    diagonal_worst = None
    diagonal_cell = None
    for cell in range(diagonal_cells):
        lo = cutoff * cell / diagonal_cells
        hi = cutoff * (cell + 1) / diagonal_cells
        u = hull(lo, hi)
        w = hull((lo**3 + u0**3) ** (ONE / 3),
                 (hi**3 + u0**3) ** (ONE / 3))
        p, n, _, _ = root_filters(u)
        hp = ONE + a * p**2
        hn = ONE + a * n**2
        # Replay the exact identity, never the square-difference surrogate.
        normalized = (hp**2 - hp * hn) / (4 * w).exp()
        slack = growth - normalized
        assert slack > ZERO, (cell, slack)
        if diagonal_worst is None or slack.lower() < diagonal_worst.lower():
            diagonal_worst = slack
            diagonal_cell = cell

    oscillation = ONE + 2 * (-3 * cutoff / 2).exp()
    tail_upper = (
        a / 9 * (-2 * cutoff).exp() * oscillation**2
        + a**2 / 81 * oscillation**4
    )
    tail_slack = growth - tail_upper
    asymptotic_slack = growth - a**2 / 81
    assert tail_slack > q(1, 10_000_000_000)
    assert asymptotic_slack > q(1, 10_000_000_000)

    tail_cost = growth_f * beta_f * (1 + Fraction(2, 1) / epsilon_f)
    tail_credit = separator_f * (1 - beta_f)
    budget = tail_credit - tail_cost
    assert budget == Fraction(
        39_437_634_699_447, 3_446_500_000_000_000_000
    )
    assert budget > Fraction(1, 100_000)

    return {
        "ratio_endpoint_slack": endpoint,
        "ratio_cells": ratio_cells,
        "ratio_worst_cell": ratio_cell,
        "ratio_derivative_worst_lower": ratio_worst.lower(),
        "tail_ratio_slack": tail_ratio,
        "negative_cells": negative_cells,
        "negative_worst_slack_lower": negative_worst.lower(),
        "diagonal_cells": diagonal_cells,
        "diagonal_worst_cell": diagonal_cell,
        "diagonal_worst_slack_lower": diagonal_worst.lower(),
        "tail_upper": tail_upper,
        "tail_slack": tail_slack,
        "asymptotic_slack": asymptotic_slack,
        "tail_budget_exact": budget,
        "correlation_C_exact": correlation_f,
    }


def outer_replay() -> dict[str, object]:
    payload = json.loads(
        (HERE / "certificate-higher-order-tetradecic-chain-v6.json")
        .read_text(encoding="utf-8")
    )
    assert payload.get("schema") == "corrected-two-sided-ramsey-v1"
    coefficient_fractions = [
        Fraction(str(value)) for value in payload["target_coefficients"]
    ]
    coefficients = [exact(value) for value in coefficient_fractions]
    assert len(coefficients) == 14

    eta = q(2_868_896, 100_000_000)
    probability = q(47_130_887, 100_000_000)
    book_delta = q(53_863, 1_000_000_000)
    lambda_zero = q(13_233)
    tau = q(69_386, 100_000_000)
    gap = q(34_754, 10_000_000_000)

    u0_f = Fraction(1_235_783, 500_000)
    epsilon_f = Fraction(6893, 10_000_000)
    beta_f = Fraction(330_867, 500_000)
    correlation_f = Fraction(12_366_348_252_219, 1_250_000_000_000)
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
    xi = (
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
    assert degree_slack >= q(1, 1_000_000_000)

    concavity = prove_concavity(coefficients)
    u_one = rate(coefficients, ONE)
    up_one = rate_prime(coefficients, ONE)
    diagonal = u_one - 2 * c_eta
    off_diagonal = up_one - c_eta
    assert ZERO < diagonal < off_diagonal
    assert page_cost < up_one
    assert 2 * tau * xi < u_one

    r_axis = gap / off_diagonal
    r_diag = gap / diagonal
    slope = ONE - diagonal / off_diagonal
    assert ZERO < r_axis < tau < r_diag < ONE
    assert ZERO < slope < ONE
    z_lo = ONE - tau / (ONE - r_diag)
    z_hi = (ONE - tau) / (ONE - r_axis)
    assert ZERO < z_lo < z_hi < ONE

    # Independent endpoint proof.  Under U''<0, the red boundary derivative
    # is increasing in z because B'(z)=(slope*z-1)U''(z)>0.
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
    assert red_margin >= q(1, 1_000_000_000)

    blue_y = c_eta - rate_prime(coefficients, ONE - tau)
    blue_diagonal = (
        2 * c_eta - rate(coefficients, ONE - tau)
        - tau * rate_prime(coefficients, ONE - tau)
    )
    assert blue_y < ZERO
    assert blue_diagonal < ZERO
    blue_page = tau * page_cost + rate(coefficients, ONE - tau)
    blue_margin = u_one - gap - blue_page
    assert blue_margin >= q(1, 1_000_000_000)

    reservoir = 2 * c_eta * r_diag + 2 * tau * xi
    reservoir_margin = u_one - gap - reservoir
    assert reservoir_margin >= q(1, 1_000_000_000)

    base = (u_one - gap).exp()
    previous_base = (u_one - q(34_727, 10_000_000_000)).exp()
    actual_improvement = previous_base - base
    safe_f = Fraction(3_780_685_290, 1_000_000_000)
    target_safe_f = Fraction(3_780_685_290, 1_000_000_000)
    previous_safe_f = Fraction(3_780_685_300, 1_000_000_000)
    assert safe_f <= target_safe_f
    assert previous_safe_f - safe_f >= Fraction(1, 100_000_000)
    safe = exact(safe_f)
    rounding = safe - base
    assert actual_improvement >= q(1, 100_000_000)
    assert rounding >= q(1, 1_000_000_000)

    return {
        "correlation_C_exact": correlation_f,
        "concavity_worst_upper": concavity.upper(),
        "rho": rho,
        "q": page_cost,
        "Xi": xi,
        "degree_slack": degree_slack,
        "red_boundary_upper": red_boundary,
        "red_page_margin": red_margin,
        "blue_diagonal_upper": blue_diagonal,
        "blue_page_margin": blue_margin,
        "reservoir_margin": reservoir_margin,
        "base_upper": base,
        "actual_improvement_lower": actual_improvement.lower(),
        "safe_decimal": safe_f,
        "rounding_margin": rounding,
        "safe_improvement": previous_safe_f - safe_f,
    }


def main() -> None:
    assert flint.__version__ == "0.9.0"
    for name, expected in FROZEN_SHA256.items():
        actual = sha256(HERE / name)
        assert actual == expected, (name, actual, expected)
    inner = inner_replay()
    outer = outer_replay()
    assert inner["correlation_C_exact"] == outer["correlation_C_exact"]
    print("PASS: genuinely non-importing 512-bit exact-diagonal replay")
    print(f"python_flint_version: {flint.__version__}")
    print(f"precision_bits: {ctx.prec}")
    for name, value in inner.items():
        print(f"inner_{name}: {value}")
    for name, value in outer.items():
        print(f"outer_{name}: {value}")


if __name__ == "__main__":
    main()
