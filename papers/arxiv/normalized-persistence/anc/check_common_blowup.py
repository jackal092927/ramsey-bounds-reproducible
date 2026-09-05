"""Tiny deterministic linear-algebra check, not a quantum speedup simulation."""
from itertools import combinations, product
from math import prod, sqrt
import json

import numpy as np


def simplices(vertices, edges, max_degree=2):
    return [[s for s in combinations(vertices, k + 1)
             if all(tuple(sorted(e)) in edges for e in combinations(s, 2))]
            for k in range(max_degree + 1)]


def coboundary(lower, upper, weights):
    index = {s: i for i, s in enumerate(lower)}
    matrix = np.zeros((len(upper), len(lower)))
    for row, simplex in enumerate(upper):
        for j, v in enumerate(simplex):
            matrix[row, index[simplex[:j] + simplex[j+1:]]] = (-1)**j * weights[v]
    return matrix


def inclusion(source, target):
    result = np.zeros((len(target), len(source)))
    index = {s: i for i, s in enumerate(target)}
    for j, simplex in enumerate(source):
        result[index[simplex], j] = 1
    return result


def fixture(edges, f):
    base_vertices = tuple(range(len(f)))
    vertices = tuple((v, j) for v in base_vertices for j in range(f[v]))
    blown_edges = {tuple(sorted((u, v))) for u, v in combinations(vertices, 2)
                  if u[0] == v[0] or tuple(sorted((u[0], v[0]))) in edges}
    base = simplices(base_vertices, edges)
    blown = simplices(vertices, blown_edges)
    transforms = []
    for k in range(3):
        index = {s: i for i, s in enumerate(blown[k])}
        T = np.zeros((len(blown[k]), len(base[k])))
        for j, simplex in enumerate(base[k]):
            amplitude = 1 / sqrt(prod(f[v] for v in simplex))
            for copy in product(*(range(f[v]) for v in simplex)):
                lifted = tuple(zip(simplex, copy))
                T[index[lifted], j] = amplitude
        transforms.append(T)
    return base, blown, transforms


def main():
    f, M = (4, 1, 2), 4
    weights = {v: sqrt(f[v] / M) for v in range(3)}
    first = fixture({(0, 1), (1, 2)}, f)
    second = fixture({(0, 1), (1, 2), (0, 2)}, f)
    output = {"multiplicities": f, "M": M, "levels": [0, 2, 1], "checks": []}
    for level, (base, blown, T) in enumerate((first, second), 1):
        blown_weights = {v: 1 for s in blown[0] for v in s}
        ds = [coboundary(base[k], base[k+1], weights) for k in range(2)]
        dh = [coboundary(blown[k], blown[k+1], blown_weights) for k in range(2)]
        for k in range(3):
            error = float(np.linalg.norm(T[k].T @ T[k] - np.eye(len(base[k]))))
            assert error < 1e-12
        for k in range(2):
            d_error = float(np.linalg.norm(dh[k] @ T[k] - sqrt(M) * T[k+1] @ ds[k]))
            boundary_error = float(np.linalg.norm(dh[k].T @ T[k+1] - sqrt(M) * T[k] @ ds[k].T))
            assert max(d_error, boundary_error) < 1e-12
            output["checks"].append({"level": level, "d_degree": k,
                                     "coboundary_error": d_error,
                                     "boundary_error": boundary_error})
        delta = ds[0] @ ds[0].T + ds[1].T @ ds[1]
        delta_hat = dh[0] @ dh[0].T + dh[1].T @ dh[1]
        error = float(np.linalg.norm(delta_hat @ T[1] - M * T[1] @ delta))
        assert error < 1e-12
        output["checks"].append({"level": level, "H1_laplacian_intertwining_error": error})
    for k in range(3):
        J = inclusion(first[0][k], second[0][k])
        Jh = inclusion(first[1][k], second[1][k])
        error = float(np.linalg.norm(Jh @ first[2][k] - second[2][k] @ J))
        assert error < 1e-12
        output["checks"].append({"degree": k, "inclusion_error": error})
    # Sharp smallest counterexample when multiplicities differ across levels.
    # One base vertex, one copy first, two copies second; include the first copy.
    old = np.array([1.0, 0.0])
    new = np.array([1.0, 1.0]) / sqrt(2)
    output["unequal_multiplicity_counterexample"] = {
        "base": "one vertex", "multiplicities": [1, 2],
        "commuting_square_error": float(np.linalg.norm(old - new)),
        "overlap": float(old @ new),
    }
    output["status"] = "TINY_FLOATING_POINT_IDENTITY_CHECK_PASSED"
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
