#!/usr/bin/env python3
"""Non-importing 512-bit replay of the diagonal-growth candidate.

This implementation imports no author checker.  It independently rebuilds
the cubic root filters, the diagonal compact/tail bound, the exact rational
tail budget, the degree-14 rate and its first two derivatives, and the full
retained-spine wedge.  Its interval grids and outer derivative reductions are
different from the author implementations.
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
    "DIAGONAL_GROWTH_SHARPENING_CANDIDATE.md":
        "b6b7bfe049f138ae69e166502d932576924833f20daec8d63c4eac612d623916",
    "check_diagonal_growth.py":
        "ff183fc15797504b7d17dab14e51ac6b49edaf46b1593794fde733e579880faa",
    "check_retained_spine_diagonal_growth.py":
        "c612e898b07c05b68c6fc54f6a8f8f684eba449676cd3bf90553360a9303ccf2",
    "STRONG_SEPARATOR_GROWTH_SHARPENING.md":
        "80b5ae4d663194623b4b6222181792d1bf71f5f73684133d84f936ed1807fefb",
    "check_strong_separator_growth.py":
        "9ea998eeab45a839c0fd24428bf9ccc7e0123cfc1550aaacc45f9e64a1568ccd",
    "RETAINED_SPINE_TRANSFER_ATTEMPT.md":
        "5aa5d6cb1ee1cc2d9f4d34b8564b6c57f78cfd7444a89abcfbb64542274e4aaa",
    "INDEPENDENT_RETAINED_SPINE_REFEREE.md":
        "6ba57fdbe13bf45255644ae94af5474b7a34afda3aefeda26415f3cc3f9b66db",
    "check_retained_spine_transfer.py":
        "b10815b10cb3ab922aa079ee74289c52239ec90939ed41b93907bf06a60ee274",
    "certificate-higher-order-tetradecic-chain-v6.json":
        "8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8",
    "INDEPENDENT_PROOF_REPLAY.md":
        "2f142a9371d29f07ffd68253c7dbb0981fe440f7f0b8284b4a81430f38395dbc",
    "STAGE6_SEARCH.md":
        "2881e8b1df310b449d0bffff5715b9176d9c191ba2a5d05bb376ab2843c58ccd",
    "INDEPENDENT_STAGE6_REFEREE.md":
        "2bb40e6dc4f83203998adad57a0e922565bc8f6f07e1bdc810dd3ebfea481f5d",
    "verify_region_direct_arb.py":
        "e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def exact(value: Fraction | int) -> arb:
    if isinstance(value, int):
        return arb(value)
    return arb(value.numerator) / value.denominator


def q(numerator: int, denominator: int = 1) -> arb:
    return arb(numerator) / denominator


def hull(lo: arb, hi: arb) -> arb:
    return lo.union(hi)


def root_filters(u: arb) -> tuple[arb, arb, arb, arb]:
    """Cubic filters and u derivatives, reconstructed from exponentials."""
    root_three = arb(3).sqrt()
    theta = root_three * u / 2
    cosine = theta.cos()
    sine = theta.sin()
    exp_u = u.exp()
    exp_minus_u = (-u).exp()
    exp_half = (u / 2).exp()
    exp_minus_half = (-u / 2).exp()
    positive = (exp_u + 2 * exp_minus_half * cosine) / 3
    negative = (exp_minus_u + 2 * exp_half * cosine) / 3
    positive_prime = (
        exp_u - exp_minus_half * cosine
        - root_three * exp_minus_half * sine
    ) / 3
    negative_prime = (
        -exp_minus_u + exp_half * cosine
        - root_three * exp_half * sine
    ) / 3
    return positive, negative, positive_prime, negative_prime


def polynomial(coefficients: list[arb], x: arb) -> arb:
    """Evaluate sum c_i x^(i+1) with explicit ascending powers."""
    total = ZERO
    power = x
    for coefficient in coefficients:
        total += coefficient * power
        power *= x
    return total


def polynomial_prime(coefficients: list[arb], x: arb) -> arb:
    total = ZERO
    power = ONE
    for index, coefficient in enumerate(coefficients, start=1):
        total += index * coefficient * power
        power *= x
    return total


def polynomial_second(coefficients: list[arb], x: arb) -> arb:
    total = ZERO
    power = ONE
    for index, coefficient in enumerate(coefficients[1:], start=2):
        total += index * (index - 1) * coefficient * power
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
    split = ONE / 65536
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


def replay_inner() -> dict[str, arb | Fraction | int]:
    u0 = q(619, 250)
    a = (-u0).exp()
    growth = q(1, 10_000)

    # Independently recheck the endpoint and finite interval of the imported
    # ratio separator.  R'(u) has the sign of the following numerator.
    ratio_target = q(1001, 500)
    positive, negative, _, _ = root_filters(u0)
    endpoint_ratio = (
        (ONE + a * positive**2) / (ONE + a * negative**2)
    )
    assert endpoint_ratio - ratio_target > q(1, 10_000)
    switch = q(29, 10)
    ratio_cells = 32_768
    worst_ratio_derivative = None
    for cell in range(ratio_cells):
        lo = u0 + (switch - u0) * cell / ratio_cells
        hi = u0 + (switch - u0) * (cell + 1) / ratio_cells
        p, n, pp, np = root_filters(hull(lo, hi))
        hp = ONE + a * p**2
        hn = ONE + a * n**2
        numerator = p * pp * hn - n * np * hp
        assert numerator > ZERO, (cell, numerator)
        if (
            worst_ratio_derivative is None
            or numerator.lower() < worst_ratio_derivative.lower()
        ):
            worst_ratio_derivative = numerator

    # Analytic ratio-tail endpoint and persistence gates.
    eu = switch.exp()
    eh = (switch / 2).exp()
    em = (-switch).exp()
    emh = (-switch / 2).exp()
    p_lower = (eu - 2 * emh) / 3
    n_upper = (2 * eh + em) / 3
    tail_ratio_slack = (
        ONE + a * p_lower**2
        - ratio_target * (ONE + a * n_upper**2)
    )
    derivative_gate = (
        2 * eu * (eu - 2 * ratio_target) - 2 * eh - 4 * em
    )
    derivative_prime_gate = (
        4 * eu**2 - 4 * ratio_target * eu - eh + 4 * em
    )
    assert p_lower > ZERO
    assert tail_ratio_slack > q(3, 10)
    assert derivative_gate > ZERO
    assert derivative_prime_gate > ZERO

    # The mixed-sign proof only needs H(-v^3)<=2.  Verify its analytic
    # reduction a*exp(u0)=1 and also replay the full segment on a grid that is
    # four times finer than the author's grid.
    assert (a * u0.exp() - ONE).contains(0)
    negative_cells = 65_536
    worst_negative_slack = None
    for cell in range(negative_cells):
        v = hull(
            u0 * cell / negative_cells,
            u0 * (cell + 1) / negative_cells,
        )
        negative = root_filters(v)[1]
        slack = 2 - (ONE + a * negative**2)
        assert slack > ZERO, (cell, slack)
        if (
            worst_negative_slack is None
            or slack.lower() < worst_negative_slack.lower()
        ):
            worst_negative_slack = slack

    # A grid twice as fine as the author's, using separately constructed
    # endpoint ranges for w.  This certifies the stronger square-difference
    # upper envelope, not merely the exact F diagonal.
    cutoff = q(20)
    cells = 131_072
    worst_slack = None
    worst_cell = None
    for cell in range(cells):
        lo = cutoff * cell / cells
        hi = cutoff * (cell + 1) / cells
        u = hull(lo, hi)
        w = hull(
            (lo**3 + u0**3) ** (ONE / 3),
            (hi**3 + u0**3) ** (ONE / 3),
        )
        p, n, _, _ = root_filters(u)
        hp = ONE + a * p**2
        hn = ONE + a * n**2
        normalized_square_difference = (hp**2 - hn**2) / (4 * w).exp()
        slack = growth - normalized_square_difference
        assert slack > ZERO, (cell, slack)
        if worst_slack is None or slack.lower() < worst_slack.lower():
            worst_slack = slack
            worst_cell = cell

    # Independently reconstruct the analytic tail envelope at u=20.
    oscillation = ONE + 2 * (-3 * cutoff / 2).exp()
    tail_upper = (
        2 * a / 9 * (-2 * cutoff).exp() * oscillation**2
        + a**2 / 81 * oscillation**4
    )
    tail_slack = growth - tail_upper
    assert tail_slack > q(1, 100_000)

    sigma_f = Fraction(501, 1000)
    growth_f = Fraction(1, 10_000)
    beta_f = Fraction(3253, 5000)
    epsilon_f = Fraction(93, 125_000)
    cost = growth_f * beta_f * (1 + Fraction(2, 1) / epsilon_f)
    credit = sigma_f * (1 - beta_f)
    budget = credit - cost
    assert cost == Fraction(813_552_529, 4_650_000_000)
    assert credit == Fraction(875_247, 5_000_000)
    assert budget == Fraction(427_181, 4_650_000_000)
    assert budget > Fraction(1, 100_000)

    return {
        "ratio_endpoint_slack": endpoint_ratio - ratio_target,
        "ratio_derivative_worst_lower": worst_ratio_derivative.lower(),
        "ratio_tail_slack": tail_ratio_slack,
        "negative_H_cells": negative_cells,
        "negative_H_worst_slack_lower": worst_negative_slack.lower(),
        "compact_cells": cells,
        "compact_worst_cell": worst_cell,
        "compact_worst_slack_lower": worst_slack.lower(),
        "tail_upper": tail_upper,
        "tail_slack": tail_slack,
        "tail_cost": cost,
        "tail_credit": credit,
        "tail_budget": budget,
    }


def replay_outer() -> dict[str, arb]:
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

    eta = q(286_892, 10_000_000)
    probability = q(4_713_079, 10_000_000)
    book_delta = q(5_393, 100_000_000)
    lambda_zero = q(13_236)
    tau = q(69_255, 100_000_000)
    gap = q(3_469, 1_000_000_000)
    beta = q(3253, 5000)
    epsilon = q(93, 125_000)
    correlation = 4 * q(619, 250) * (ONE + epsilon)
    assert (
        4 * Fraction(619, 250) * (1 + Fraction(93, 125_000))
        == Fraction(154_865_134, 15_625_000)
    )

    c_eta = (2 / (ONE + eta)).log()
    log_delta = (ONE / book_delta).log()
    log_probability = (ONE / probability).log()
    page_cost = (
        log_probability
        + 3 * book_delta / probability
        + 6 * log_delta * log_probability / lambda_zero
    )
    rho = (2 / beta).log()
    xi_cost = (
        2 * rho
        + 4 * correlation * lambda_zero ** (ONE / 3)
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

    concavity_worst = prove_concavity(coefficients)
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

    # Independent endpoint proof: global concavity makes U' decrease and
    # U-zU' increase.  Along the red sloping boundary its derivative B(z)
    # has B'(z)=(slope*z-1)U''(z)>0, so its maximum is z_hi.
    red_x_upper = c_eta - rate_prime(coefficients, z_hi)
    red_y_lower = (
        c_eta - rate(coefficients, z_hi)
        + z_hi * rate_prime(coefficients, z_hi)
    )
    assert red_x_upper < ZERO
    assert red_y_lower > ZERO
    assert slope * z_hi < ONE
    red_boundary_upper = red_x_upper + slope * red_y_lower
    assert red_boundary_upper < ZERO

    red_page = (
        c_eta * r_axis
        + tau * page_cost
        + (ONE - r_axis)
        * rate(coefficients, (ONE - tau) / (ONE - r_axis))
    )
    red_margin = u_one - gap - red_page
    assert red_margin > q(1, 1_000_000_000)

    # For the blue branch, both the y derivative and the diagonal derivative
    # attain their maxima at the origin under U''<0.
    blue_y_upper = c_eta - rate_prime(coefficients, ONE - tau)
    blue_diagonal_upper = (
        2 * c_eta
        - rate(coefficients, ONE - tau)
        - tau * rate_prime(coefficients, ONE - tau)
    )
    assert blue_y_upper < ZERO
    assert blue_diagonal_upper < ZERO
    blue_page = tau * page_cost + rate(coefficients, ONE - tau)
    blue_margin = u_one - gap - blue_page
    assert blue_margin > q(1, 1_000_000_000)

    reservoir = 2 * c_eta * r_diag + 2 * tau * xi_cost
    reservoir_margin = u_one - gap - reservoir
    assert reservoir_margin > q(1, 1_000_000_000)

    base = (u_one - gap).exp()
    safe = q(3_780_685_320, 1_000_000_000)
    previous = q(3_780_685_405, 1_000_000_000)
    rounding_margin = safe - base
    improvement = previous - safe
    assert rounding_margin > q(1, 1_000_000_000)
    assert improvement >= q(5, 100_000_000)

    return {
        "correlation_C": correlation,
        "rho": rho,
        "q": page_cost,
        "Xi": xi_cost,
        "concavity_worst_upper": concavity_worst.upper(),
        "degree_slack": degree_slack,
        "red_boundary_upper": red_boundary_upper,
        "red_page_margin": red_margin,
        "blue_diagonal_upper": blue_diagonal_upper,
        "blue_page_margin": blue_margin,
        "reservoir_margin": reservoir_margin,
        "base_upper": base,
        "rounding_margin": rounding_margin,
        "safe_improvement": improvement,
    }


def main() -> None:
    assert flint.__version__ == "0.9.0"
    for name, expected in FROZEN_SHA256.items():
        actual = sha256(HERE / name)
        assert actual == expected, (name, actual, expected)

    inner = replay_inner()
    outer = replay_outer()
    print("PASS: non-importing 512-bit diagonal-growth replay")
    print(f"python_flint_version: {flint.__version__}")
    print(f"precision_bits: {ctx.prec}")
    for name, value in inner.items():
        print(f"inner_{name}: {value}")
    for name, value in outer.items():
        print(f"outer_{name}: {value}")


if __name__ == "__main__":
    main()
