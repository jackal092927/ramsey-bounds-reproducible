#!/usr/bin/env python3
"""Certify the scalar gates for the retained-spine transfer attempt.

This checker deliberately does not claim a numerical value for the new
two-dimensional transfer maximum.  It proves the strict scalar inequalities
used by the compactness argument in ``RETAINED_SPINE_TRANSFER_ATTEMPT.md``.
All terminating decimals below are interpreted exactly by Arb.
"""

from __future__ import annotations

import json
from pathlib import Path

from flint import arb, ctx

from verify_region_direct_arb import ONE, prove_concavity, rate, rate_prime


ctx.prec = 256

HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "certificate-higher-order-tetradecic-chain-v6.json"


def main() -> None:
    payload = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    coefficients = [arb(str(value)) for value in payload["target_coefficients"]]

    # Fixed Yang--Mao parameters.  For r=2 and d=3 their explicit root-filter
    # constant is u=max{1, log(4)/(3/2), log(432)}=log(432).
    eta = arb("0.032")
    p = arb("0.46799")
    delta = arb("0.00001")
    lambda_zero = arb("25000")
    tau = arb("0.00005")

    u = arb(432).log()
    assert u > ONE
    assert u > arb(4).log() / arb("1.5")

    beta = ONE / 48
    correlation_C = 8 * u
    rho = (arb(2) / beta).log()  # log(96)
    L = (ONE / delta).log()
    L_p = (ONE / p).log()
    Pi = 3 * delta / p + 6 * L * L_p / lambda_zero
    Xi = (
        2 * rho
        + 4 * correlation_C * lambda_zero ** (ONE / 3)
        + 12 * correlation_C * L / lambda_zero ** (arb(2) / 3)
    )

    regularization_cost = (arb(2) / (ONE + eta)).log()
    page_cost = L_p + Pi
    U_one = rate(ONE, coefficients)
    U_prime_one = rate_prime(ONE, coefficients)

    # Yang--Mao book-theorem parameter gates.
    assert arb(0) < eta
    assert arb(0) < p < arb("0.5") - eta
    assert arb(0) < delta <= p / 4
    assert delta <= arb("0.25")
    assert lambda_zero >= 2
    assert lambda_zero >= 6 * L
    assert arb(0) < tau < ONE

    # The imported P6 rate is strictly concave on (0,1].
    concavity_upper = prove_concavity(coefficients)
    assert concavity_upper < 0

    # Direct branch, book page branch at the origin, and book reservoir branch.
    assert 2 * regularization_cost < U_one
    assert regularization_cost < U_prime_one
    assert page_cost < U_prime_one
    assert 2 * tau * Xi < U_one

    print("PASS: retained-spine scalar transfer gates")
    print(f"P6 concavity upper: {concavity_upper}")
    print(f"U(1): {U_one}")
    print(f"U'(1): {U_prime_one}")
    print(f"regularization c_eta: {regularization_cost}")
    print(f"U(1)-2*c_eta: {U_one - 2 * regularization_cost}")
    print(f"U'(1)-c_eta: {U_prime_one - regularization_cost}")
    print(f"Pi: {Pi}")
    print(f"page cost log(1/p)+Pi: {page_cost}")
    print(f"U'(1)-page cost: {U_prime_one - page_cost}")
    print(f"Xi: {Xi}")
    print(f"U(1)-2*tau*Xi: {U_one - 2 * tau * Xi}")


if __name__ == "__main__":
    main()
