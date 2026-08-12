#!/usr/bin/env python3
"""Independent 512-bit replay of the strong-growth retained-spine package.

This checker deliberately imports no author checker.  It reconstructs the
cubic root filters, the two new growth envelopes, the exact tail budget, the
degree-14 rate and its first two derivatives, and the complete retained-spine
wedge from the frozen JSON coefficients.

For the two fragile outer derivatives it uses consequences of U'' < 0 rather
than copying the author's cellwise implementation:

* the red sloping-boundary derivative is increasing in its scalar argument;
* the blue diagonal derivative is decreasing in the diagonal coordinate.

Thus both are reduced to independently evaluated endpoints.
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
    "STRONG_SEPARATOR_GROWTH_SHARPENING.md":
        "80b5ae4d663194623b4b6222181792d1bf71f5f73684133d84f936ed1807fefb",
    "check_strong_separator_growth.py":
        "9ea998eeab45a839c0fd24428bf9ccc7e0123cfc1550aaacc45f9e64a1568ccd",
    "RETAINED_SPINE_STRONG_GROWTH_CANDIDATE.md":
        "f185d5ffe07944e52aeee8c54272da948b9d9be2efe6cfad4f6ddfc8549c0d96",
    "check_retained_spine_strong_growth.py":
        "3c9d6dadbab9469c1971466791ea4218313c93ec1a16825460099631b0251faf",
    "HYBRID_CORRELATION_SHARPENING.md":
        "4b29c692dd1fc96859491b25d61c9b0e1124a33cf57a45ef01abb5a2e49ed30d",
    "INDEPENDENT_JOINT_CORRELATION_SPINE_REFEREE.md":
        "47bde6908563ee3a855cea2e9f75fe5167ab46e52a5e8691e9be0f2e1f5d5afc",
    "independent_check_retained_spine_joint_optimized.py":
        "830f9133b16abecf01fb879109c50bf4acfd8b93c7a87313626e08b197dc32d4",
    "RETAINED_SPINE_TRANSFER_ATTEMPT.md":
        "5aa5d6cb1ee1cc2d9f4d34b8564b6c57f78cfd7444a89abcfbb64542274e4aaa",
    "INDEPENDENT_RETAINED_SPINE_REFEREE.md":
        "6ba57fdbe13bf45255644ae94af5474b7a34afda3aefeda26415f3cc3f9b66db",
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
    "check_retained_spine_transfer.py":
        "b10815b10cb3ab922aa079ee74289c52239ec90939ed41b93907bf06a60ee274",
    "BOOKCOR_AUDIT.md":
        "86fc83d1735644a063616ba1ba5aea2d1519f4088bbca591d871b784d21f2d18",
}


def sha256(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            value.update(block)
    return value.hexdigest()


def exact_ratio(numerator: int, denominator: int = 1) -> arb:
    return arb(numerator) / denominator


def hull(lo: arb, hi: arb) -> arb:
    return lo.union(hi)


def root_filters(u: arb) -> tuple[arb, arb, arb, arb]:
    """Return E(u^3), E(-u^3), and their u-derivatives."""
    root_three = arb(3).sqrt()
    angle = root_three * u / 2
    cosine = angle.cos()
    sine = angle.sin()
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


def ascending_polynomial(coefficients: list[arb], x: arb) -> arb:
    """Evaluate sum_i coefficients[i] x^(i+1), without Horner reuse."""
    value = ZERO
    power = x
    for coefficient in coefficients:
        value += coefficient * power
        power *= x
    return value


def ascending_polynomial_prime(coefficients: list[arb], x: arb) -> arb:
    value = ZERO
    power = ONE
    for index, coefficient in enumerate(coefficients):
        value += (index + 1) * coefficient * power
        power *= x
    return value


def ascending_polynomial_second(coefficients: list[arb], x: arb) -> arb:
    value = ZERO
    power = ONE
    for index in range(1, len(coefficients)):
        value += index * (index + 1) * coefficients[index] * power
        power *= x
    return value


def rate(coefficients: list[arb], x: arb) -> arb:
    entropy = (ONE + x) * (ONE + x).log() - x * x.log()
    return entropy + ascending_polynomial(coefficients, x) * (-x).exp()


def rate_prime(coefficients: list[arb], x: arb) -> arb:
    polynomial = ascending_polynomial(coefficients, x)
    derivative = ascending_polynomial_prime(coefficients, x)
    return ((ONE + x) / x).log() + (derivative - polynomial) * (-x).exp()


def rate_second(coefficients: list[arb], x: arb) -> arb:
    polynomial = ascending_polynomial(coefficients, x)
    derivative = ascending_polynomial_prime(coefficients, x)
    second = ascending_polynomial_second(coefficients, x)
    return -ONE / (x * (ONE + x)) + (
        second - 2 * derivative + polynomial
    ) * (-x).exp()


def prove_global_concavity(coefficients: list[arb]) -> arb:
    """Prove U'' < 0 on (0,1] with an independent power evaluator."""
    split = ONE / 65536
    near_zero = hull(ZERO, split)
    correction = (
        ascending_polynomial_second(coefficients, near_zero)
        - 2 * ascending_polynomial_prime(coefficients, near_zero)
        + ascending_polynomial(coefficients, near_zero)
    ) * (-near_zero).exp()
    # -1/(x(1+x)) <= -1/(split(1+split)) for 0 < x <= split.
    worst = -ONE / (split * (ONE + split)) + correction
    assert worst < ZERO, worst

    cells = 65536
    for cell in range(cells):
        lo = split + (ONE - split) * cell / cells
        hi = split + (ONE - split) * (cell + 1) / cells
        enclosure = rate_second(coefficients, hull(lo, hi))
        assert enclosure < ZERO, (cell, enclosure)
        if enclosure.upper() > worst.upper():
            worst = enclosure
    return worst


def replay_ratio_and_growth() -> dict[str, arb | Fraction]:
    u0 = exact_ratio(619, 250)
    length = u0**3
    a = (-u0).exp()

    # Recheck the imported strict ratio H(t)/H(-t) > 1001/500.  This is not
    # logically new, but prevents the new identity from hiding a stale pin.
    switch = exact_ratio(29, 10)
    ratio_target = exact_ratio(1001, 500)
    positive, negative, _, _ = root_filters(u0)
    endpoint_ratio_slack = (
        (ONE + a * positive**2) / (ONE + a * negative**2)
        - ratio_target
    )
    assert endpoint_ratio_slack > exact_ratio(1, 10000)

    worst_ratio_derivative = None
    ratio_cells = 16384
    for cell in range(ratio_cells):
        lo = u0 + (switch - u0) * cell / ratio_cells
        hi = u0 + (switch - u0) * (cell + 1) / ratio_cells
        positive, negative, positive_prime, negative_prime = root_filters(
            hull(lo, hi)
        )
        h_positive = ONE + a * positive**2
        h_negative = ONE + a * negative**2
        numerator = (
            positive * positive_prime * h_negative
            - negative * negative_prime * h_positive
        )
        assert numerator > ZERO, (cell, numerator)
        if (
            worst_ratio_derivative is None
            or numerator.lower() < worst_ratio_derivative.lower()
        ):
            worst_ratio_derivative = numerator
    assert worst_ratio_derivative is not None

    # Independent endpoint form of the analytic ratio tail.
    exp_u = switch.exp()
    exp_half = (switch / 2).exp()
    exp_minus_u = (-switch).exp()
    exp_minus_half = (-switch / 2).exp()
    p_lower = (exp_u - 2 * exp_minus_half) / 3
    n_upper = (2 * exp_half + exp_minus_u) / 3
    ratio_tail_slack = (
        ONE + a * p_lower**2
        - ratio_target * (ONE + a * n_upper**2)
    )
    d_at_switch = (
        2 * exp_u * (exp_u - 2 * ratio_target)
        - 2 * exp_half - 4 * exp_minus_u
    )
    d_prime_at_switch = (
        4 * exp_u**2 - 4 * ratio_target * exp_u
        - exp_half + 4 * exp_minus_u
    )
    assert p_lower > ZERO
    assert ratio_tail_slack > exact_ratio(3, 10)
    assert exp_u > 18
    assert d_at_switch > ZERO
    assert d_prime_at_switch > ZERO

    # H(-v^3) <= 1.13 exp(2 (u0^3-v^3)^(1/3)), 0 <= v <= u0.
    d_one = exact_ratio(113, 100)
    worst_negative_h = None
    negative_cells = 32768
    for cell in range(negative_cells):
        lo = u0 * cell / negative_cells
        hi = u0 * (cell + 1) / negative_cells
        v = hull(lo, hi)
        # Form the cube-root range from monotone endpoints.  This avoids the
        # repeated-u0 dependency at the final cell.
        w_lo = (
            ZERO if cell == negative_cells - 1
            else (u0**3 - hi**3) ** (ONE / 3)
        )
        w_hi = (u0**3 - lo**3) ** (ONE / 3)
        w = hull(w_lo, w_hi)
        _, e_negative, _, _ = root_filters(v)
        slack = d_one * (2 * w).exp() - (ONE + a * e_negative**2)
        assert slack > ZERO, (cell, slack)
        if worst_negative_h is None or slack.lower() < worst_negative_h.lower():
            worst_negative_h = slack
    assert worst_negative_h is not None

    # E(u^3) <= exp((u^3+u0^3)^(1/3))/3 on 0 <= u <= 20.
    cutoff = arb(20)
    positive_cells = 131072
    worst_positive_e = None
    for cell in range(positive_cells):
        lo = cutoff * cell / positive_cells
        hi = cutoff * (cell + 1) / positive_cells
        u = hull(lo, hi)
        w_lo = (lo**3 + u0**3) ** (ONE / 3)
        w_hi = (hi**3 + u0**3) ** (ONE / 3)
        w = hull(w_lo, w_hi)
        e_positive, _, _, _ = root_filters(u)
        slack = w.exp() / 3 - e_positive
        assert slack > ZERO, (cell, slack)
        if worst_positive_e is None or slack.lower() < worst_positive_e.lower():
            worst_positive_e = slack
    assert worst_positive_e is not None

    # For u >= 20, let q=u0^3/u^3 and
    # l(u)=u0^3/[3u^2(1+q)^(2/3)].  Then
    # d log(l)/du = -2/[u(1+q)] >= -2/u >= -1/10,
    # whereas d log(2 exp(-3u/2))/du=-3/2.  The endpoint ordering persists.
    q_at_cutoff = u0**3 / cutoff**3
    cube_root_increment_lower = (
        u0**3
        / (3 * cutoff**2 * (ONE + q_at_cutoff) ** (exact_ratio(2, 3)))
    )
    exponential_majorant = 2 * (-3 * cutoff / 2).exp()
    logarithmic_target = (ONE + exponential_majorant).log()
    assert cube_root_increment_lower > exponential_majorant
    assert exponential_majorant > logarithmic_target
    assert exact_ratio(3, 2) > exact_ratio(2, 20)

    direct_prefactor = 113 * a / 900
    assert ONE + a < d_one
    assert direct_prefactor < exact_ratio(11, 1000)

    sigma = Fraction(501, 1000)
    growth = Fraction(11, 1000)
    beta = Fraction(11, 250)
    epsilon = Fraction(203, 100000)
    tail_cost = growth * beta * (1 + Fraction(2, 1) / epsilon)
    tail_credit = sigma * (1 - beta)
    tail_margin = tail_credit - tail_cost
    assert tail_cost == Fraction(24224563, 50750000)
    assert tail_credit == Fraction(119739, 250000)
    assert tail_margin == Fraction(41227, 25375000)
    assert tail_margin > Fraction(1, 100000)

    return {
        "L": length,
        "endpoint_ratio_slack": endpoint_ratio_slack,
        "ratio_derivative_worst_lower": worst_ratio_derivative.lower(),
        "ratio_tail_crossmultiplied_slack": ratio_tail_slack,
        "negative_H_envelope_worst_lower": worst_negative_h.lower(),
        "positive_E_envelope_worst_lower": worst_positive_e.lower(),
        "halfline_increment_lower_at_20": cube_root_increment_lower,
        "halfline_log_target_at_20": logarithmic_target,
        "direct_prefactor": direct_prefactor,
        "tail_cost": tail_cost,
        "tail_credit": tail_credit,
        "tail_margin": tail_margin,
    }


def replay_retained_spine() -> dict[str, arb]:
    payload = json.loads(
        (HERE / "certificate-higher-order-tetradecic-chain-v6.json")
        .read_text(encoding="utf-8")
    )
    assert payload.get("schema") == "corrected-two-sided-ramsey-v1"
    coefficient_rationals = [
        Fraction(str(value)) for value in payload["target_coefficients"]
    ]
    coefficients = [
        exact_ratio(value.numerator, value.denominator)
        for value in coefficient_rationals
    ]
    assert len(coefficients) == 14

    eta = exact_ratio(286887, 10_000_000)
    probability = exact_ratio(4_713_083, 10_000_000)
    book_delta = exact_ratio(5355, 100_000_000)
    lambda_zero = arb(13340)
    tau = exact_ratio(686, 1_000_000)
    gap = exact_ratio(3445, 1_000_000_000)
    beta = exact_ratio(11, 250)
    epsilon = exact_ratio(203, 100000)
    correlation = 4 * exact_ratio(619, 250) * (ONE + epsilon)
    assert (
        4 * Fraction(619, 250) * (1 + Fraction(203, 100000))
        == Fraction(62025657, 6250000)
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
        + 12 * correlation * log_delta / lambda_zero ** (exact_ratio(2, 3))
    )

    # Reconstruct every scalar gate in the parameterized transfer theorem.
    assert ZERO < eta
    assert ZERO < probability < ONE / 2 - eta
    assert ZERO < book_delta <= probability / 4
    assert book_delta <= ONE / 4
    assert lambda_zero >= 2
    assert lambda_zero >= 6 * log_delta
    assert ZERO < tau < ONE
    raw_degree_slack = ONE / 2 - eta - probability
    degree_slack = tau * raw_degree_slack
    assert degree_slack > exact_ratio(1, 1_000_000_000)

    concavity_worst = prove_global_concavity(coefficients)
    u_one = rate(coefficients, ONE)
    up_one = rate_prime(coefficients, ONE)
    diagonal = u_one - 2 * c_eta
    off_diagonal = up_one - c_eta
    assert ZERO < diagonal < off_diagonal
    assert page_cost < up_one
    assert 2 * tau * xi_cost < u_one
    page_input_margin = up_one - page_cost
    reservoir_input_margin = u_one - 2 * tau * xi_cost
    lambda_log_margin = lambda_zero - 6 * log_delta
    delta_gate_margin = probability / 4 - book_delta

    # Complete direct-branch complement in 0 <= x <= y.
    r_axis = gap / off_diagonal
    r_diag = gap / diagonal
    slope = ONE - diagonal / off_diagonal
    assert ZERO < r_axis < tau < r_diag < ONE
    assert ZERO < slope < ONE
    # h(r_diag)=r_diag exactly; form the identity without interval
    # cancellation and check the geometric monotonicity separately.
    assert 1 + slope > ZERO

    z_lo = ONE - tau / (ONE - r_diag)
    z_hi = (ONE - tau) / (ONE - r_axis)
    assert ZERO < z_lo < z_hi < ONE

    # Red coordinate signs.  Concavity makes U' decreasing and
    # U-zU' increasing, so both worst cases occur at z_hi.
    red_x_upper = c_eta - rate_prime(coefficients, z_hi)
    red_y_lower = (
        c_eta - rate(coefficients, z_hi)
        + z_hi * rate_prime(coefficients, z_hi)
    )
    assert red_x_upper < ZERO
    assert red_y_lower > ZERO

    # Along y=h(x), dP_R/dx=B(z).  Since
    # B'(z)=(slope*z-1)U''(z)>0, B is increasing.  Its maximum is at z_hi.
    assert slope * z_hi < ONE
    red_boundary_upper = red_x_upper + slope * red_y_lower
    assert red_boundary_upper < ZERO

    red_page = (
        c_eta * r_axis + tau * page_cost
        + (ONE - r_axis)
        * rate(coefficients, (ONE - tau) / (ONE - r_axis))
    )
    red_margin = u_one - gap - red_page
    assert red_margin > exact_ratio(1, 1_000_000_000)

    # The blue y derivative is largest at (0,0), where w=1-tau.
    blue_y_upper = c_eta - rate_prime(coefficients, ONE - tau)
    assert blue_y_upper < ZERO

    # On y=x, let t=tau/(1-x), w=1-t.  The derivative is
    # B(x)=2c-U(w)-tU'(w), and B'(x)=t^2 U''(w)/(1-x)<0.
    # Hence its maximum is the x=0 endpoint.
    blue_diagonal_upper = (
        2 * c_eta - rate(coefficients, ONE - tau)
        - tau * rate_prime(coefficients, ONE - tau)
    )
    assert blue_diagonal_upper < ZERO

    blue_page = tau * page_cost + rate(coefficients, ONE - tau)
    blue_margin = u_one - gap - blue_page
    assert blue_margin > exact_ratio(1, 1_000_000_000)

    # x+y increases along h(x) because 1+slope>0, so the reservoir maximum
    # is the diagonal endpoint (r_diag,r_diag).
    reservoir = 2 * c_eta * r_diag + 2 * tau * xi_cost
    reservoir_margin = u_one - gap - reservoir
    assert reservoir_margin > exact_ratio(1, 1_000_000_000)

    base = (u_one - gap).exp()
    safe_decimal = exact_ratio(3_780_685_405, 1_000_000_000)
    old_safe_decimal = exact_ratio(3_780_685_745, 1_000_000_000)
    rounding_margin = safe_decimal - base
    advertised_improvement = old_safe_decimal - safe_decimal
    assert base < exact_ratio(3_780_685_403_313, 1_000_000_000_000)
    assert rounding_margin > exact_ratio(1, 1_000_000_000)
    assert advertised_improvement > exact_ratio(1, 10_000_000)

    return {
        "C": correlation,
        "rho": rho,
        "q": page_cost,
        "Xi": xi_cost,
        "concavity_worst_upper": concavity_worst.upper(),
        "raw_degree_slack": raw_degree_slack,
        "degree_slack": degree_slack,
        "delta_gate_margin": delta_gate_margin,
        "lambda_log_margin": lambda_log_margin,
        "page_input_margin": page_input_margin,
        "reservoir_input_margin": reservoir_input_margin,
        "U_one": u_one,
        "U_prime_one": up_one,
        "A": diagonal,
        "E": off_diagonal,
        "r_axis": r_axis,
        "r_diag": r_diag,
        "slope": slope,
        "red_x_upper": red_x_upper,
        "red_y_lower": red_y_lower,
        "red_boundary_upper": red_boundary_upper,
        "red_page_margin": red_margin,
        "blue_y_upper": blue_y_upper,
        "blue_diagonal_upper": blue_diagonal_upper,
        "blue_page_margin": blue_margin,
        "reservoir_margin": reservoir_margin,
        "base_upper": base,
        "rounding_margin": rounding_margin,
        "advertised_decimal_improvement": advertised_improvement,
    }


def main() -> None:
    assert flint.__version__ == "0.9.0", flint.__version__
    for name, expected in FROZEN_SHA256.items():
        actual = sha256(HERE / name)
        assert actual == expected, (name, actual, expected)

    inner = replay_ratio_and_growth()
    outer = replay_retained_spine()

    print("PASS: independent 512-bit strong-growth retained-spine replay")
    print(f"python_flint_version: {flint.__version__}")
    print(f"precision_bits: {ctx.prec}")
    for name, value in inner.items():
        print(f"inner_{name}: {value}")
    for name, value in outer.items():
        print(f"outer_{name}: {value}")


if __name__ == "__main__":
    main()
