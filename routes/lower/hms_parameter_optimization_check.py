#!/usr/bin/env python3
"""High-precision checks for LOWER_HMS_PARAMETER_OPTIMIZATION.md.

This program checks only the explicit arithmetic in the proof package.  It
does not certify the Gaussian moment lemmas, the reverse induction, or the
Ramsey extraction.  Run it with the repository virtual environment, which
contains mpmath:

    .venv/bin/python routes/lower/hms_parameter_optimization_check.py
"""

from __future__ import annotations

import mpmath as mp


mp.mp.dps = 180
SQRT_TWO = mp.sqrt(2)
SQRT_TWO_PI = mp.sqrt(2 * mp.pi)


def normal_upper_tail(x: mp.mpf) -> mp.mpf:
    return mp.erfc(x / SQRT_TWO) / 2


def solve_pc(C: mp.mpf) -> mp.mpf:
    """Solve log(p_C)=C log(1-p_C) by monotone bisection."""
    lo = mp.mpf(10) ** (-mp.mp.dps + 20)
    hi = mp.mpf("0.5")
    for _ in range(6 * mp.mp.dps):
        mid = (lo + hi) / 2
        residual = mp.log(mid) - C * mp.log1p(-mid)
        if residual < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def solve_cp(p: mp.mpf) -> mp.mpf:
    """Solve P[Z <= -c_p]=p by monotone bisection."""
    lo = mp.mpf(0)
    hi = mp.sqrt(2 * mp.log(1 / p)) + 10
    for _ in range(6 * mp.mp.dps):
        mid = (lo + hi) / 2
        if normal_upper_tail(mid) > p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def density(x: mp.mpf) -> mp.mpf:
    return mp.exp(-x * x / 2) / SQRT_TWO_PI


def mills_red(b: mp.mpf) -> mp.mpf:
    """phi(b)/Phi(-b), for conditioning on Z <= -b."""
    return density(b) / normal_upper_tail(b)


def variance_red(b: mp.mpf) -> mp.mpf:
    m = mills_red(b)
    return 1 + b * m - m * m


def centered_cgf(b: mp.mpf, u: mp.mpf) -> mp.mpf:
    """Exact log E exp(uY) for centered Z | Z <= -b."""
    m = mills_red(b)
    return (
        u * u / 2
        + u * m
        + mp.log(normal_upper_tail(b + u))
        - mp.log(normal_upper_tail(b))
    )


def psi(b: mp.mpf, u: mp.mpf) -> mp.mpf:
    """K_b(u)/u^2, continuously extended at u=0."""
    if abs(u) < mp.mpf("1e-50"):
        return variance_red(b) / 2
    return centered_cgf(b, u) / (u * u)


def exact_sum(r: int) -> int:
    direct = sum(k * (k - 1) ** 2 for k in range(1, r))
    closed = r * (r - 1) * (r - 2) * (3 * r - 5) // 12
    assert direct == closed
    return direct


def constants_and_gains(C: mp.mpf) -> dict[str, mp.mpf]:
    pc = solve_pc(C)
    p = pc + 1 / C
    cp = solve_cp(p)
    a = density(cp)
    m0 = a / p
    D = 4 * a * C / (1 - p)
    alpha_squared = 100 * mp.log(10 / p)

    # Optimized limiting cutoff window.
    omega_star = alpha_squared / D
    b_star = cp - omega_star
    m_star = mills_red(b_star)
    v_star = variance_red(b_star)

    # Pointwise maximal legal Q(x)=D/(4m0 x), hence minimal P(x).
    def optimized_integrand(x: mp.mpf) -> mp.mpf:
        if x == 0:
            return mp.mpf(0)
        P_x = D / (D - 4 * m0 * x)
        u_x = P_x * m0 * m_star * x / D
        return x**3 * (1 - P_x * psi(b_star, u_x))

    optimized_integral = mp.quad(optimized_integrand, [0, 1])
    gain_star = m0**2 * m_star**2 / D**2 * optimized_integral

    # Exact-CGF gain with the best *constant* Q, to isolate the benefit from
    # allowing the legal Holder exponent to vary with the group size k.
    P_constant = D / (D - 4 * m0)
    z_constant = P_constant * m0 * m_star / D
    constant_q_integral = mp.quad(
        lambda x: x**3 * (1 - P_constant * psi(b_star, z_constant * x)),
        [0, 1],
    )
    gain_constant_q = m0**2 * m_star**2 / D**2 * constant_q_integral

    # Frozen theorem's previous window and Holder choice.
    omega_old = 2 * alpha_squared / D
    b_old = cp - omega_old
    m_old = mills_red(b_old)
    v_old = variance_red(b_old)
    P_old = D / (D - 8 * m0)
    kappa_old = 1 - P_old * v_old / 2
    gain_old = kappa_old * m0**2 * m_old**2 / (4 * D**2)

    # Strict exact-CGF improvement with literally the same old cutoff window
    # and the same old constant Holder pair.  This isolates the improvement
    # from any window or feasibility re-optimization.
    z_same_old = P_old * m0 * m_old / D
    same_old_integral = mp.quad(
        lambda x: x**3 * (1 - P_old * psi(b_old, z_same_old * x)),
        [0, 1],
    )
    gain_same_old = m0**2 * m_old**2 / D**2 * same_old_integral

    method_cap = m0**4 / (4 * D**2)
    return {
        "C": C,
        "pc": pc,
        "p": p,
        "cp": cp,
        "D": D,
        "omega_star": omega_star,
        "b_star": b_star,
        "m0": m0,
        "m_star": m_star,
        "v_star": v_star,
        "P_at_one": D / (D - 4 * m0),
        "gain_star": gain_star,
        "gain_constant_q": gain_constant_q,
        "gain_same_old": gain_same_old,
        "gain_old": gain_old,
        "method_cap": method_cap,
        "scaled_gain": 32 * mp.log(C) * gain_star,
        "scaled_cap": 32 * mp.log(C) * method_cap,
    }


def main() -> None:
    for r in (1, 2, 3, 10, 101, 1000):
        exact_sum(r)
    print("exact finite-sum identity: PASS")

    previous_scaled = mp.mpf(0)
    for C_text in ("1e12", "1e20", "1e40", "1e80"):
        x = constants_and_gains(mp.mpf(C_text))
        assert x["D"] > 8 * x["m0"]
        assert x["P_at_one"] * x["v_star"] < 2
        assert x["gain_star"] > x["gain_constant_q"]
        assert x["gain_constant_q"] > x["gain_same_old"]
        assert x["gain_same_old"] > x["gain_old"]
        assert x["gain_star"] < x["method_cap"]
        assert x["scaled_gain"] > previous_scaled
        assert x["scaled_gain"] < x["scaled_cap"]
        previous_scaled = x["scaled_gain"]

        # K_b(u)/u^2 is decreasing in both b and u.  The proof is analytic;
        # this grid only catches sign/orientation mistakes in the formulas.
        b = x["b_star"]
        u0 = x["P_at_one"] * x["m0"] * x["m_star"] / x["D"]
        assert psi(b, u0) < psi(b, u0 / 2) < variance_red(b) / 2
        assert psi(b + mp.mpf("0.01"), u0) < psi(b, u0)

        print(
            "C={C} b*={b} P(1)={P} old={old} same-old={same} constant-Q={const} "
            "optimized={new} cap={cap} 32log(C)*optimized={scaled}".format(
                C=C_text,
                b=mp.nstr(x["b_star"], 12),
                P=mp.nstr(x["P_at_one"], 12),
                old=mp.nstr(x["gain_old"], 14),
                same=mp.nstr(x["gain_same_old"], 14),
                const=mp.nstr(x["gain_constant_q"], 14),
                new=mp.nstr(x["gain_star"], 14),
                cap=mp.nstr(x["method_cap"], 14),
                scaled=mp.nstr(x["scaled_gain"], 12),
            )
        )

    print("strict finite-C improvement checks: PASS")
    print("method-cap and asymptotic-approach checks: PASS")


if __name__ == "__main__":
    main()
