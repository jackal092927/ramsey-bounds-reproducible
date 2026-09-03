"""Deterministic numerical sanity checks; no experiments or external calls.

Run from the repository root: python3 research/quantum_direction_selection/hyperbolic_probe/probe.py
The checks are not a proof and do not verify the NaviGraph manuscript.
"""

import itertools
import json
import math
import random


def lorentz(x, y):
    return x[0] * y[0] - sum(a * b for a, b in zip(x[1:], y[1:]))


def point(coords):
    return [math.sqrt(1 + sum(x * x for x in coords)), *coords]


def determinant(a):
    a = [row[:] for row in a]
    value = 1.0
    for j in range(len(a)):
        k = max(range(j, len(a)), key=lambda k: abs(a[k][j]))
        if abs(a[k][j]) < 1e-14:
            return 0.0
        if k != j:
            a[j], a[k] = a[k], a[j]
            value = -value
        pivot = a[j][j]
        value *= pivot
        for i in range(j + 1, len(a)):
            ratio = a[i][j] / pivot
            for k in range(j + 1, len(a)):
                a[i][k] -= ratio * a[j][k]
    return value


def solve(a, b):
    a = [row[:] + [v] for row, v in zip(a, b)]
    n = len(a)
    for j in range(n):
        k = max(range(j, n), key=lambda k: abs(a[k][j]))
        assert abs(a[k][j]) > 1e-14
        a[j], a[k] = a[k], a[j]
        pivot = a[j][j]
        a[j] = [x / pivot for x in a[j]]
        for i in range(n):
            if i != j:
                ratio = a[i][j]
                a[i] = [x - ratio * y for x, y in zip(a[i], a[j])]
    return [row[-1] for row in a]


def gram(xs):
    return [[lorentz(x, y) for y in xs] for x in xs]


def reconstruction_case(d, n, rank, seed):
    rng = random.Random(seed)
    # Embedded geodesic case uses rank 2 in a higher-dimensional ambient space.
    xs = [point([rng.uniform(-2, 2) for _ in range(rank - 1)]
                + [0.0] * (d - rank + 1)) for _ in range(n)]
    q = point([rng.uniform(-2, 2) for _ in range(d)])
    basis_ids = max(itertools.combinations(range(n), rank),
                    key=lambda ids: abs(determinant(gram([xs[i] for i in ids]))))
    anchors = [xs[i] for i in basis_ids]
    g = gram(anchors)
    b = [lorentz(a, q) for a in anchors]
    max_error = 0.0
    max_coefficient = 0.0
    max_l1 = 0.0
    max_robust_ratio = 0.0
    xi = 1e-7
    for x in xs:
        coefficients = solve(g, [lorentz(a, x) for a in anchors])
        recovered = sum(c * v for c, v in zip(coefficients, b))
        max_error = max(max_error, abs(recovered - lorentz(x, q)))
        max_coefficient = max(max_coefficient, *map(abs, coefficients))
        max_l1 = max(max_l1, sum(map(abs, coefficients)))
        perturbed = [v + xi * (1 if c >= 0 else -1)
                     for v, c in zip(b, coefficients)]
        perturbed_score = sum(c * v for c, v in zip(coefficients, perturbed))
        max_robust_ratio = max(max_robust_ratio,
                              abs(perturbed_score - recovered) / (rank * xi))
    assert max_error < 1e-9
    assert max_coefficient <= 1 + 1e-9
    assert max_l1 <= rank + 1e-9
    assert max_robust_ratio <= 1 + 1e-6
    return dict(d=d, n=n, rank=rank, query_count=rank, basis=list(basis_ids),
                maximum_score_error=max_error,
                maximum_absolute_coefficient=max_coefficient,
                maximum_coefficient_l1=max_l1,
                adversarial_noise_bound_ratio=max_robust_ratio)


def theta(r, delta):
    assert 0 <= delta <= r
    return 2 * math.asin(math.sqrt((math.cosh(r - delta) - 1)
                                  / (2 * math.sinh(r) ** 2)))


def cap_probability(d, r, delta):
    angle = theta(r, delta)
    if d == 2:
        return angle / math.pi
    if d == 3:
        # Stable equivalent of (1-cos(angle))/2.
        return math.sin(angle / 2) ** 2
    raise ValueError(d)


def cap_checks():
    rows = []
    for d in [2, 3]:
        for r in [8.0, 12.0, 20.0]:
            grid = [i / 100 for i in range(1, int(min(r, 8) * 100))]
            classical = max(grid, key=lambda z: z * cap_probability(d, r, z))
            quantum = max(grid, key=lambda z: z * math.sqrt(cap_probability(d, r, z)))
            p1 = cap_probability(d, r, 1.0)
            asymptotic_angle = 2 * math.exp(-(r + 1) / 2)
            rows.append(dict(d=d, radius=r, delta=1.0, cap_probability=p1,
                             angle_over_asymptotic=theta(r, 1.0)/asymptotic_angle,
                             optimal_proxy_delta_classical=classical,
                             optimal_proxy_delta_quantum=quantum,
                             limit_delta_classical=2/(d-1),
                             limit_delta_quantum=4/(d-1)))
    return rows


if __name__ == "__main__":
    print(json.dumps(dict(
        status="PASS", seed_policy="fixed seeds; deterministic finite checks",
        landmark_checks=[reconstruction_case(2, 18, 3, 7),
                         reconstruction_case(3, 16, 4, 8),
                         reconstruction_case(5, 20, 2, 9)],
        shell_checks=cap_checks()), indent=2))
