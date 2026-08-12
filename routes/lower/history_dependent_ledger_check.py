#!/usr/bin/env python3
"""Arithmetic replay for HISTORY_DEPENDENT_LEDGER_ATTEMPT.md.

This checker is deliberately independent of the author-side formula code in
``hms_parameter_optimization_check.py``.  It verifies finite recursion and
calculus formulas, not the probabilistic reverse induction or source bridge.
"""

from __future__ import annotations

from math import comb

import mpmath as mp


mp.mp.dps = 140
SQRT2 = mp.sqrt(2)
SQRT2PI = mp.sqrt(2 * mp.pi)


def phi(x: mp.mpf) -> mp.mpf:
    return mp.exp(-x * x / 2) / SQRT2PI


def upper_tail(x: mp.mpf) -> mp.mpf:
    return mp.erfc(x / SQRT2) / 2


def mills(x: mp.mpf) -> mp.mpf:
    return phi(x) / upper_tail(x)


def mprime(x: mp.mpf) -> mp.mpf:
    m = mills(x)
    return m * (m - x)


def msecond(x: mp.mpf) -> mp.mpf:
    m = mills(x)
    return mprime(x) * (2 * m - x) - m


def cgf(b: mp.mpf, u: mp.mpf) -> mp.mpf:
    return (
        u * u / 2
        + u * mills(b)
        + mp.log(upper_tail(b + u))
        - mp.log(upper_tail(b))
    )


def solve_pc(C: mp.mpf) -> mp.mpf:
    lo = mp.mpf(10) ** (-mp.mp.dps + 20)
    hi = mp.mpf("0.5")
    for _ in range(5 * mp.mp.dps):
        mid = (lo + hi) / 2
        if mp.log(mid) - C * mp.log1p(-mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def solve_c(p: mp.mpf) -> mp.mpf:
    lo = mp.mpf(0)
    hi = mp.sqrt(2 * mp.log(1 / p)) + 10
    for _ in range(5 * mp.mp.dps):
        mid = (lo + hi) / 2
        if upper_tail(mid) > p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def edge(a: int, b: int) -> tuple[int, int]:
    return (a, b) if a < b else (b, a)


def build_weights(
    r: int, t0: mp.mpf, gamma: mp.mpf
) -> dict[tuple[int, int], mp.mpf]:
    weights: dict[tuple[int, int], mp.mpf] = {}
    for i in range(r - 1, 0, -1):
        for j in range(i + 1, r + 1):
            degree = mp.fsum(
                weights[edge(j, q)] for q in range(i + 1, r + 1) if q != j
            )
            weights[(i, j)] = t0 + gamma * degree
    return weights


def future_statistics(
    weights: dict[tuple[int, int], mp.mpf], i: int, r: int, t0: mp.mpf
) -> tuple[mp.mpf, mp.mpf, dict[int, mp.mpf]]:
    degrees = {j: mp.mpf(0) for j in range(i + 1, r + 1)}
    total = mp.mpf(0)
    for j in range(i + 1, r + 1):
        for q in range(j + 1, r + 1):
            delta = weights[(j, q)] - t0
            assert delta >= 0
            total += delta
            degrees[j] += delta
            degrees[q] += delta
    return total, max(degrees.values(), default=mp.mpf(0)), degrees


def constants(C: mp.mpf) -> dict[str, mp.mpf]:
    pc = solve_pc(C)
    p = pc + 1 / C
    c = solve_c(p)
    a = phi(c)
    m0 = a / p
    mp0 = mprime(c)
    D = 4 * a * C / (1 - p)
    omega = 100 * mp.log(10 / p) / D
    M = mills(c + omega)
    rho = m0 * mp0 / D
    jminus = mprime(c - omega)
    jplus = mprime(c + omega)
    hessian_margin = jminus - jplus**2 * m0 / (D * (1 - rho))
    feasibility_margin = mp.mpf("0.5") - (
        4 * m0 / D + 4 * m0**2 * mp0 / ((1 - rho) * D**2)
    )
    linear_cost = (
        4 * m0 * M**2 / D
        + 2 * M**2 * m0**2 * mp0 / ((1 - rho) * D**2)
        + 96 * m0**2 * M**2 / ((1 - rho) * D**2)
    )
    B = m0**2 - mp.mpf(16) / 3 - linear_cost
    H = m0**2 * mp0 * B / (12 * D**2)
    return {
        "C": C,
        "p": p,
        "c": c,
        "D": D,
        "omega": omega,
        "m0": m0,
        "mp0": mp0,
        "M": M,
        "rho": rho,
        "jminus": jminus,
        "jplus": jplus,
        "hessian_margin": hessian_margin,
        "feasibility_margin": feasibility_margin,
        "linear_cost": linear_cost,
        "B": B,
        "H": H,
        "scaled_H": 96 * mp.log(C) * H,
    }


def check_finite_recursion(x: dict[str, mp.mpf]) -> None:
    r = 18
    ell = 18
    sqrt_d = x["D"] * ell
    d = sqrt_d**2
    t0 = x["m0"] * sqrt_d
    gamma = x["m0"] * x["mp0"] / sqrt_d
    weights = build_weights(r, t0, gamma)
    rho = x["m0"] * x["mp0"] / x["D"]

    max_weight = max(weights.values())
    assert max_weight <= t0 / (1 - rho)

    total_S = mp.mpf(0)
    for i in range(1, r):
        k = r - i
        S, R, _ = future_statistics(weights, i, r, t0)
        total_S += S
        lower_S = gamma * t0 * k * (k - 1) * (k - 2) / 3
        assert S >= lower_S - mp.mpf("1e-100")
        assert R <= gamma * t0 * (k - 1) ** 2 / (1 - rho) + mp.mpf("1e-100")
        if k >= 3 and S > 0:
            assert R / S <= 6 / ((1 - rho) * k)

        # Exact weighted-gradient identity for every boundary edge (i,j).
        for j in range(i + 1, r + 1):
            degree_T = mp.fsum(
                weights[edge(j, q)] for q in range(i + 1, r + 1) if q != j
            )
            gradient = -x["m0"] - x["m0"] * x["mp0"] * degree_T / d
            assert mp.almosteq(gradient, -weights[(i, j)] / sqrt_d)

    assert total_S >= 2 * gamma * t0 * comb(r, 4)
    print("finite weighted recursion, gradient, and mass bounds: PASS")


def check_hessian_and_centered_cost(x: dict[str, mp.mpf]) -> None:
    r = 12
    i = 2
    ell = 12
    sqrt_d = x["D"] * ell
    d = sqrt_d**2
    t0 = x["m0"] * sqrt_d
    gamma = x["m0"] * x["mp0"] / sqrt_d
    weights = build_weights(r, t0, gamma)
    vertices = list(range(i + 1, r + 1))
    bvals = {
        j: x["c"] + (x["omega"] if j % 2 else -x["omega"])
        for j in vertices
    }

    # Direct Hessian eigenvalue check at a deliberately nonconstant cutoff.
    H = mp.matrix(len(vertices))
    for a, j in enumerate(vertices):
        weighted_m_degree = mp.fsum(
            weights[edge(j, q)] * mills(bvals[q]) for q in vertices if q != j
        )
        H[a, a] = -mprime(bvals[j]) - msecond(bvals[j]) * weighted_m_degree / d
        for b, q in enumerate(vertices):
            if j != q:
                H[a, b] = (
                    -weights[edge(j, q)]
                    * mprime(bvals[j])
                    * mprime(bvals[q])
                    / d
                )
    eigenvalues, _ = mp.eigsy(H)
    assert max(eigenvalues) < 0

    S, R, degrees = future_statistics(weights, i, r, t0)
    k = len(vertices)
    u0: dict[int, mp.mpf] = {}
    du: dict[int, mp.mpf] = {}
    for j in vertices:
        u0[j] = t0 * mp.fsum(mills(bvals[q]) for q in vertices if q != j) / d
        du[j] = mp.fsum(
            (weights[edge(j, q)] - t0) * mills(bvals[q])
            for q in vertices
            if q != j
        ) / d

    a = 4 * t0 * k / d
    z = 4 * R / d
    P0 = 1 / (1 - a)
    P = 1 / (1 - a - z)
    exact_increment = mp.fsum(
        cgf(bvals[j], P * (u0[j] + du[j])) / P
        - cgf(bvals[j], P0 * u0[j]) / P0
        for j in vertices
    )
    asserted_bound = x["linear_cost"] * S / d
    assert exact_increment >= 0
    assert exact_increment <= asserted_bound
    assert P <= 2
    assert z <= 4 * x["m0"] ** 2 * x["mp0"] / (
        (1 - x["rho"]) * x["D"] ** 2
    )
    assert mp.fsum(degrees.values()) == 2 * S
    print("full Hessian sample and exact linear-CGF cost comparison: PASS")


def main() -> None:
    previous = mp.mpf(0)
    snapshots: list[dict[str, mp.mpf]] = []
    for C_text in ("1e12", "1e20", "1e40", "1e80"):
        x = constants(mp.mpf(C_text))
        snapshots.append(x)
        assert x["rho"] < 1
        assert x["hessian_margin"] > 0
        assert x["feasibility_margin"] > 0
        assert x["B"] > 0
        assert msecond(x["c"] - x["omega"]) > 0
        assert msecond(x["c"] + x["omega"]) > 0
        assert x["scaled_H"] > previous
        assert x["scaled_H"] < 1
        previous = x["scaled_H"]
        print(
            "C={C} rho={rho} Hessian-margin={hm} B={B} "
            "96log(C)H={scaled}".format(
                C=C_text,
                rho=mp.nstr(x["rho"], 10),
                hm=mp.nstr(x["hessian_margin"], 10),
                B=mp.nstr(x["B"], 12),
                scaled=mp.nstr(x["scaled_H"], 12),
            )
        )

    check_finite_recursion(snapshots[1])
    check_hessian_and_centered_cost(snapshots[1])
    print("cutoff-box conditions and positive candidate constants: PASS")
    print("asymptotic approach to 1/(96 log C): PASS")


if __name__ == "__main__":
    main()
