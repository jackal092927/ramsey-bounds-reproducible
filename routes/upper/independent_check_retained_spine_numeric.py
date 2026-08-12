#!/usr/bin/env python3
"""Independent replay of the retained-spine numerical enclosure.

This referee implementation deliberately differs from
``check_retained_spine_numeric.py`` in four ways:

* the fourteen P6 coefficients are hard-coded and compared byte-for-byte with
  the frozen JSON payload;
* polynomials and their derivatives are evaluated by Horner's rule;
* the two page derivative signs are reduced to exact evaluations at the upper
  endpoint of the z interval using independently replayed global concavity;
* global concavity uses a different split point and 16,384 closed cells.

It certifies the same conservative exponent gap 10^(-8); it does not search
for or approximate the maximizer defining C_*.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import flint
from flint import arb, ctx


ctx.prec = 320

HERE = Path(__file__).resolve().parent
ZERO = arb(0)
ONE = arb(1)

P6_JSON_SHA256 = (
    "8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8"
)

# These are coefficients of z, z^2, ..., z^14, not a constant-first list.
P6_TEXT = [
    "-0.250000000000000",
    "0.019891840059418",
    "-0.012275954247190",
    "0.144110816398083",
    "0.006277913420654",
    "-0.066101623491668",
    "-0.002287675993602",
    "-0.058238059505066",
    "0.030675864198693",
    "0.052472201910597",
    "0.043300454861853",
    "-0.042529975074653",
    "-0.055263639426635",
    "0.036695886931268",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def interval(lo: arb, hi: arb) -> arb:
    return lo.union(hi)


def horner_constant_first(z: arb, coefficients: list[arb]) -> arb:
    """Evaluate c_0+c_1*z+... by Horner's rule."""
    value = ZERO
    for coefficient in reversed(coefficients):
        value = value * z + coefficient
    return value


def polynomial(z: arb, coefficients: list[arb]) -> arb:
    # P has zero constant coefficient.
    return z * horner_constant_first(z, coefficients)


def derivative_coefficients(coefficients: list[arb]) -> list[arb]:
    return [(index + 1) * value for index, value in enumerate(coefficients)]


def second_derivative_coefficients(coefficients: list[arb]) -> list[arb]:
    return [
        (index + 2) * (index + 1) * value
        for index, value in enumerate(coefficients[1:])
    ]


def polynomial_prime(z: arb, coefficients: list[arb]) -> arb:
    return horner_constant_first(z, derivative_coefficients(coefficients))


def polynomial_second(z: arb, coefficients: list[arb]) -> arb:
    return horner_constant_first(z, second_derivative_coefficients(coefficients))


def entropy(z: arb) -> arb:
    return (ONE + z) * (ONE + z).log() - z * z.log()


def rate(z: arb, coefficients: list[arb]) -> arb:
    return entropy(z) + polynomial(z, coefficients) * (-z).exp()


def rate_prime(z: arb, coefficients: list[arb]) -> arb:
    p = polynomial(z, coefficients)
    pp = polynomial_prime(z, coefficients)
    return ((ONE + z) / z).log() + (pp - p) * (-z).exp()


def rate_second(z: arb, coefficients: list[arb]) -> arb:
    p = polynomial(z, coefficients)
    pp = polynomial_prime(z, coefficients)
    ppp = polynomial_second(z, coefficients)
    return -ONE / (z * (ONE + z)) + (ppp - 2 * pp + p) * (-z).exp()


def replay_global_concavity(coefficients: list[arb]) -> arb:
    """Prove U''<0 on (0,1] with a partition different from the author one."""
    split = ONE / 16384
    near_zero = interval(ZERO, split)
    correction = (
        polynomial_second(near_zero, coefficients)
        - 2 * polynomial_prime(near_zero, coefficients)
        + polynomial(near_zero, coefficients)
    ) * (-near_zero).exp()
    worst = -ONE / (split * (ONE + split)) + correction
    assert worst < ZERO, f"near-zero concavity unresolved: {worst}"

    cell_count = 16384
    for index in range(cell_count):
        lo = split + (ONE - split) * index / cell_count
        hi = split + (ONE - split) * (index + 1) / cell_count
        enclosure = rate_second(interval(lo, hi), coefficients)
        assert enclosure < ZERO, (
            f"concavity unresolved in independent cell {index}: {enclosure}"
        )
        if enclosure.upper() > worst.upper():
            worst = enclosure
    return worst


def main() -> None:
    assert flint.__version__ == "0.9.0"
    payload_path = HERE / "certificate-higher-order-tetradecic-chain-v6.json"
    assert sha256(payload_path) == P6_JSON_SHA256
    payload = json.loads(payload_path.read_text(encoding="utf-8"))
    assert payload["schema"] == "corrected-two-sided-ramsey-v1"
    assert payload["target_coefficients"] == P6_TEXT
    coefficients = [arb(item) for item in P6_TEXT]

    concavity_upper = replay_global_concavity(coefficients)

    eta = arb("0.032")
    probability = arb("0.46799")
    delta = arb("0.00001")
    lambda_zero = arb("25000")
    tau = arb("0.00005")
    radius = arb("0.0000016")
    exponent_gap = arb("0.00000001")

    c_eta = (arb(2) / (ONE + eta)).log()
    log_delta = (ONE / delta).log()
    log_probability = (ONE / probability).log()
    pi_cost = (
        3 * delta / probability
        + 6 * log_delta * log_probability / lambda_zero
    )
    page_cost = log_probability + pi_cost
    beta = ONE / 48
    rho = (arb(2) / beta).log()
    correlation = 8 * arb(432).log()
    reservoir_cost = (
        2 * rho
        + 4 * correlation * lambda_zero ** (ONE / 3)
        + 12 * correlation * log_delta / lambda_zero ** (arb(2) / 3)
    )

    u_one = rate(ONE, coefficients)
    up_one = rate_prime(ONE, coefficients)
    diagonal_gain_coefficient = u_one - 2 * c_eta
    off_diagonal_gain_coefficient = up_one - c_eta
    assert diagonal_gain_coefficient > ZERO
    assert off_diagonal_gain_coefficient >= diagonal_gain_coefficient

    # On either ordered outer triangle, equation (18) is at least
    # max(x,y)*(U(1)-2*c_eta).  The common diagonal boundary is included.
    outer_gain = radius * diagonal_gain_coefficient
    outer_margin = outer_gain - exponent_gap
    assert outer_margin > ZERO
    # The only point at which both homogeneous remainders vanish is handled
    # directly, and has the larger gain U(1)-2*c_eta.
    assert diagonal_gain_coefficient >= outer_gain

    # In the inner square, tau+x-y >= tau-radius > 0 fixes the coordinate
    # ordering of the first page branch; the second is its transpose.
    ordering_margin = tau - radius
    assert ordering_margin > ZERO
    z_lo = ONE - tau - radius
    z_hi = (ONE - tau) / (ONE - radius)
    assert ZERO < z_lo < z_hi < ONE

    # Since U''<0, U' is decreasing, and g(z)=U(z)-zU'(z) is increasing.
    # Hence both weakest page derivative signs occur at z_hi:
    #   dP_R/dx <= c_eta-U'(z_hi),
    #   dP_R/dy >= c_eta-[U(z_hi)-z_hi U'(z_hi)].
    dx_upper = c_eta - rate_prime(z_hi, coefficients)
    dy_lower = (
        c_eta
        - rate(z_hi, coefficients)
        + z_hi * rate_prime(z_hi, coefficients)
    )
    assert dx_upper < ZERO
    assert dy_lower > ZERO

    page_axis = (
        c_eta * radius
        + tau * page_cost
        + (ONE - radius) * rate(z_hi, coefficients)
    )
    page_margin = u_one - exponent_gap - page_axis
    assert page_margin > ZERO

    reservoir_corner = 2 * c_eta * radius + 2 * tau * reservoir_cost
    reservoir_margin = u_one - exponent_gap - reservoir_corner
    assert reservoir_margin > ZERO

    certified_exponent = u_one - exponent_gap
    certified_base = certified_exponent.exp()
    frozen_p6_base = u_one.exp()
    rounded_up_base = arb("3.780698389989140")
    assert certified_base < rounded_up_base
    assert frozen_p6_base > rounded_up_base
    base_improvement = frozen_p6_base - certified_base
    assert base_improvement > ZERO

    print("PASS: independent retained-spine numerical referee replay")
    print(f"precision_bits: {ctx.prec}")
    print(f"global_concavity_worst_upper: {concavity_upper.upper()}")
    print(f"outer_margin_over_1e-8: {outer_margin}")
    print(f"page_ordering_margin_tau_minus_r0: {ordering_margin}")
    print(f"page_z_lo: {z_lo}")
    print(f"page_z_hi: {z_hi}")
    print(f"page_dx_global_upper: {dx_upper}")
    print(f"page_dy_global_lower: {dy_lower}")
    print(f"page_margin_below_target: {page_margin}")
    print(f"reservoir_margin_below_target: {reservoir_margin}")
    print(f"certified_exponent: {certified_exponent}")
    print(f"certified_base: {certified_base}")
    print(f"strict_decimal_upper: {rounded_up_base}")
    print(f"frozen_p6_base: {frozen_p6_base}")
    print(f"rigorous_base_improvement: {base_improvement}")


if __name__ == "__main__":
    main()
