#!/usr/bin/env python3
"""Arithmetic sanity checks for HMS_APPENDIX_BRIDGE.md.

This script samples no probabilistic histories and proves no theorem. It
recomputes the explicitly defined constants, exact finite sum, red/blue
published-ledger bottleneck, and blue-Holder incompatibility.
"""

from __future__ import annotations

import math


def solve_pc(C: float) -> float:
    """Solve log(p) = C log(1-p) by monotone bisection."""
    lo, hi = 1e-300, 0.5
    for _ in range(300):
        mid = (lo + hi) / 2.0
        f = math.log(mid) - C * math.log1p(-mid)
        if f < 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def normal_upper_tail(x: float) -> float:
    return 0.5 * math.erfc(x / math.sqrt(2.0))


def solve_cp(p: float) -> float:
    """Solve P[Z <= -c_p] = p."""
    lo, hi = 0.0, 50.0
    for _ in range(300):
        mid = (lo + hi) / 2.0
        if normal_upper_tail(mid) > p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def mills_upper(b: float) -> float:
    phi = math.exp(-0.5 * b * b) / math.sqrt(2.0 * math.pi)
    return phi / normal_upper_tail(b)


def upper_truncated_variance_at_minus_b(b: float) -> float:
    m = mills_upper(b)
    return 1.0 + b * m - m * m


def exact_sum(r: int) -> int:
    direct = sum(k * (k - 1) ** 2 for k in range(1, r))
    closed = r * (r - 1) * (r - 2) * (3 * r - 5) // 12
    assert direct == closed
    return direct


def constants(C: float) -> dict[str, float]:
    pc = solve_pc(C)
    p = pc + 1.0 / C
    cp = solve_cp(p)
    a = math.exp(-0.5 * cp * cp) / math.sqrt(2.0 * math.pi)
    m0 = a / p
    D = 4.0 * a * C / (1.0 - p)
    alpha_r = 10.0 * math.sqrt(math.log(10.0 / p))
    omega = 2.0 * alpha_r * alpha_r / D
    b_lo = cp - omega
    m_minus = mills_upper(b_lo)
    v_plus = upper_truncated_variance_at_minus_b(b_lo)
    Q = D / (8.0 * m0)
    P = Q / (Q - 1.0)
    kappa = 1.0 - P * v_plus / 2.0
    c_red = kappa * m0 * m0 * m_minus * m_minus
    gain = c_red / (4.0 * D * D)

    # These are the leading (theta_C = 1) versions of (8c)--(8d).
    # The proof keeps the source's unknown absolute error symbolically.
    b_red_leading = -math.log1p(1.0 / (C * pc)) + a**3 / (3.0 * p**3 * D)
    b_blue = math.log1p(1.0 / (C * (1.0 - p))) - (
        4.0 * a**3 * C / (3.0 * (1.0 - p) ** 3 * D)
    )

    m_blue = a / (1.0 - p)
    gamma_blue = m_blue * (cp + m_blue)
    q_max = 1.0 / (1.0 - gamma_blue / 2.0)
    q_min = 2.0 / (1.0 + gamma_blue)

    base = -0.5 * math.log(pc)
    red_rate = base + 1.0 / 20.0 + gain
    blue_rate = base + 1.0 / 6.0
    return {
        "C": C,
        "pc": pc,
        "p": p,
        "cp": cp,
        "D": D,
        "omega": omega,
        "Q_red": Q,
        "v_plus": v_plus,
        "kappa": kappa,
        "c_red": c_red,
        "gain": gain,
        "gain_times_32_logC": gain * 32.0 * math.log(C),
        "red_source_bonus_leading": b_red_leading / 2.0,
        "blue_source_bonus": C * b_blue / 2.0,
        "red_rate": red_rate,
        "blue_rate": blue_rate,
        "blue_q_max": q_max,
        "blue_q_min": q_min,
        "gamma_blue": gamma_blue,
    }


def main() -> None:
    for r in (1, 2, 3, 10, 101):
        exact_sum(r)
    print("exact finite-sum identity: PASS")

    # The source's projection constant is deliberately very conservative, so
    # the asymptotic ratio approaches one only for extremely large C.
    for C in (1e12, 1e20, 1e40, 1e80):
        x = constants(C)
        assert x["Q_red"] > 1.0
        assert x["kappa"] > 0.0
        assert x["c_red"] > 0.0
        assert x["red_rate"] < x["blue_rate"]
        assert x["gamma_blue"] < 0.5
        assert x["blue_q_min"] >= x["blue_q_max"]
        print(
            "C={C:.0e} pc={pc:.8g} D={D:.6g} "
            "kappa={kappa:.8g} gain={gain:.8g} "
            "32log(C)*gain={gain_times_32_logC:.8g} "
            "red-source={red_source_bonus_leading:.8g} "
            "blue-source={blue_source_bonus:.8g} "
            "red<blue={bottleneck} blue-Q-empty={blocked}".format(
                **x,
                bottleneck=x["red_rate"] < x["blue_rate"],
                blocked=x["blue_q_min"] >= x["blue_q_max"],
            )
        )
    print("appendix bridge arithmetic checks: PASS")


if __name__ == "__main__":
    main()
