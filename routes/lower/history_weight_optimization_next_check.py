#!/usr/bin/env python3
"""Independent arithmetic replay for HISTORY_WEIGHT_OPTIMIZATION_NEXT.md.

The script imports no project code.  It checks the controlled triangular
recursion, the residual-gradient square completion, all deterministic weight
bounds, a full Hessian sample, the exact linear-CGF increment, the accumulated
combinatorics, and the advertised large-C constant.  As in the predecessor
checker, it does not replace the source-level reverse-induction proof.
"""

from __future__ import annotations

from math import comb

import mpmath as mp


mp.mp.dps = 160
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
    lo = mp.mpf(10) ** (-mp.mp.dps + 30)
    hi = mp.mpf("0.5")
    for _ in range(6 * mp.mp.dps):
        mid = (lo + hi) / 2
        if mp.log(mid) - C * mp.log1p(-mid) < 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def solve_c(p: mp.mpf) -> mp.mpf:
    lo = mp.mpf(0)
    hi = mp.sqrt(2 * mp.log(1 / p)) + 10
    for _ in range(6 * mp.mp.dps):
        mid = (lo + hi) / 2
        if upper_tail(mid) > p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def edge(a: int, b: int) -> tuple[int, int]:
    return (a, b) if a < b else (b, a)


def constants(C: mp.mpf) -> dict[str, mp.mpf]:
    pc = solve_pc(C)
    p = pc + 1 / C
    c = solve_c(p)
    density = phi(c)
    m0 = density / p
    mp0 = mprime(c)
    D = 4 * density * C / (1 - p)
    omega = 100 * mp.log(10 / p) / D
    M = mills(c + omega)
    rho = m0 * mp0 / D

    theta = m0**2
    A0 = m0**2 * mp0
    amin = min(A0, theta)
    aplus = max(theta, (A0 + rho * theta) / (1 - rho))
    tbar = (m0 + theta / D) / (1 - rho)
    jminus = mprime(c - omega)
    jplus = mprime(c + omega)
    mu = jminus - jplus**2 * tbar / D
    feasibility = mp.mpf("0.5") - (4 * m0 / D + 4 * aplus / D**2)

    linear_cost = (
        4 * m0 * M**2 / D
        + 2 * M**2 * aplus / D**2
        + 32 * m0**2 * M**2 * aplus / (amin * D**2)
    )
    B = m0**2 - mp.mpf(16) / 3 - linear_cost
    control_net = B * theta - theta**2 / (2 * mu)
    Hhat = (B * A0 + control_net) / (12 * D**2)

    # Refereed predecessor constant, evaluated independently for comparison.
    old_linear_cost = (
        4 * m0 * M**2 / D
        + 2 * M**2 * m0**2 * mp0 / ((1 - rho) * D**2)
        + 96 * m0**2 * M**2 / ((1 - rho) * D**2)
    )
    old_B = m0**2 - mp.mpf(16) / 3 - old_linear_cost
    old_H = old_B * A0 / (12 * D**2)
    return {
        "C": C,
        "p": p,
        "c": c,
        "D": D,
        "omega": omega,
        "M": M,
        "m0": m0,
        "mp0": mp0,
        "rho": rho,
        "theta": theta,
        "A0": A0,
        "amin": amin,
        "aplus": aplus,
        "mu": mu,
        "feasibility": feasibility,
        "linear_cost": linear_cost,
        "B": B,
        "control_net": control_net,
        "Hhat": Hhat,
        "old_H": old_H,
        "scaled": 64 * mp.log(C) * Hhat,
    }


def build_controlled_weights(
    r: int, t0: mp.mpf, gamma: mp.mpf, theta: mp.mpf
) -> tuple[dict[tuple[int, int], mp.mpf], dict[tuple[int, int], mp.mpf]]:
    weights: dict[tuple[int, int], mp.mpf] = {}
    controls: dict[tuple[int, int], mp.mpf] = {}
    for i in range(r - 1, 0, -1):
        for j in range(i + 1, r + 1):
            degree = mp.fsum(
                weights[edge(j, q)] for q in range(i + 1, r + 1) if q != j
            )
            eij = theta * (i - 1)
            weights[(i, j)] = t0 + gamma * degree + eij
            controls[(i, j)] = eij
    return weights, controls


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


def check_recursion_and_combinatorics(x: dict[str, mp.mpf]) -> None:
    r = 19
    ell = 19
    sqrt_d = x["D"] * ell
    d = sqrt_d**2
    t0 = x["m0"] * sqrt_d
    gamma = x["m0"] * x["mp0"] / sqrt_d
    weights, controls = build_controlled_weights(r, t0, gamma, x["theta"])
    tmax_bound = (t0 + x["theta"] * r) / (1 - x["rho"])
    assert max(weights.values()) <= tmax_bound

    total_S = mp.mpf(0)
    total_e2 = mp.mpf(0)
    for i in range(1, r):
        k = r - i
        S, R, degrees = future_statistics(weights, i, r, t0)
        total_S += S
        for j in range(i + 1, r + 1):
            eij = controls[(i, j)]
            total_e2 += eij**2
            degree_T = mp.fsum(
                weights[edge(j, q)] for q in range(i + 1, r + 1) if q != j
            )
            gradient = -x["m0"] - x["m0"] * x["mp0"] * degree_T / d
            assert mp.almosteq(
                gradient, -(weights[(i, j)] - eij) / sqrt_d
            )

            # The square completion used in the proof, tested on both signs.
            for delta in (-3, -mp.mpf("0.2"), mp.mpf("0.7"), 4):
                lhs = eij * delta / sqrt_d - x["mu"] * delta**2 / 2
                rhs = eij**2 / (2 * x["mu"] * d)
                assert lhs <= rhs + mp.mpf("1e-130")

        if k >= 2 and r >= 3:
            assert S >= x["amin"] * (r - 2) * comb(k, 2)
            assert R <= x["aplus"] * (r - 2) * (k - 1)
            assert R / S <= 2 * x["aplus"] / (x["amin"] * k)
            assert R / d <= x["aplus"] / x["D"] ** 2
        assert mp.almosteq(mp.fsum(degrees.values()), 2 * S)

    K = comb(r, 3) + 2 * comb(r, 4)
    mass_lower = 2 * x["A0"] * comb(r, 4) + x["theta"] * K
    assert total_S >= mass_lower
    assert mp.almosteq(total_e2, x["theta"] ** 2 * K)
    print("controlled recursion, residual gradient, and exact K_r identity: PASS")


def check_hessian_and_cgf(x: dict[str, mp.mpf]) -> None:
    r = 13
    i = 3
    ell = 13
    sqrt_d = x["D"] * ell
    d = sqrt_d**2
    t0 = x["m0"] * sqrt_d
    gamma = x["m0"] * x["mp0"] / sqrt_d
    weights, _ = build_controlled_weights(r, t0, gamma, x["theta"])
    vertices = list(range(i + 1, r + 1))
    bvals = {
        j: x["c"] + (x["omega"] if j % 2 else -x["omega"])
        for j in vertices
    }

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
    assert max(eigenvalues) <= -x["mu"]

    S, R, _ = future_statistics(weights, i, r, t0)
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
    assert exact_increment >= 0
    assert exact_increment <= x["linear_cost"] * S / d
    assert P <= 2
    print("full Hessian sample and exact controlled linear-CGF bound: PASS")


def main() -> None:
    snapshots: list[dict[str, mp.mpf]] = []
    previous = mp.mpf(0)
    for C_text in ("1e12", "1e20", "1e40", "1e80"):
        x = constants(mp.mpf(C_text))
        snapshots.append(x)
        assert x["rho"] < 1
        assert x["mu"] > 0
        assert x["feasibility"] > 0
        assert x["B"] > 0
        assert x["control_net"] > 0
        assert x["Hhat"] > x["old_H"] > 0
        assert msecond(x["c"] - x["omega"]) > 0
        assert msecond(x["c"] + x["omega"]) > 0
        assert previous < x["scaled"] < 1
        previous = x["scaled"]
        print(
            "C={C} mu={mu} B={B} control-net={net} "
            "64log(C)Hhat={scaled}".format(
                C=C_text,
                mu=mp.nstr(x["mu"], 11),
                B=mp.nstr(x["B"], 12),
                net=mp.nstr(x["control_net"], 12),
                scaled=mp.nstr(x["scaled"], 12),
            )
        )

    check_recursion_and_combinatorics(snapshots[1])
    check_hessian_and_cgf(snapshots[1])
    print("all controlled finite checks: PASS")
    print("sampled approach to Hhat ~ 1/(64 log C): PASS")


if __name__ == "__main__":
    main()
