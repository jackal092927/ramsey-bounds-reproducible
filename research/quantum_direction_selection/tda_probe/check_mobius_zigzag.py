"""Small mathematical sanity check: genuine simplicial zigzag angle obstruction.

No quantum simulation. A fixed triangulated Moebius band has equal-length
boundary and core circles, with boundary class twice the core over R.
Repeating boundary -> band <- core produces a scalar H1 zigzag.
"""
from itertools import combinations
from fractions import Fraction
import json

import numpy as np
from scipy.linalg import null_space


def exact_rref(matrix):
    rows = [[Fraction(int(x)) for x in row] for row in matrix]
    pivots = []
    r = 0
    for c in range(len(rows[0])):
        pivot = next((j for j in range(r, len(rows)) if rows[j][c]), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        scale = rows[r][c]
        rows[r] = [x / scale for x in rows[r]]
        for j in range(len(rows)):
            if j != r and rows[j][c]:
                scale = rows[j][c]
                rows[j] = [x - scale * y for x, y in zip(rows[j], rows[r])]
        pivots.append(c)
        r += 1
        if r == len(rows):
            break
    return rows, pivots


def exact_local_check(d1, d2, boundary, core):
    reduced, pivots = exact_rref(np.vstack((d1, d2.T)))
    free = [i for i in range(d1.shape[1]) if i not in pivots]
    assert len(free) == 1
    h = [Fraction(0)] * d1.shape[1]
    h[free[0]] = Fraction(1)
    for r, c in enumerate(pivots):
        h[c] = -reduced[r][free[0]]
    dot = lambda x, y: sum(a * int(b) for a, b in zip(x, y))
    hh = sum(x * x for x in h)
    a2 = dot(h, boundary)**2 / (hh * int(boundary @ boundary))
    b2 = dot(h, core)**2 / (hh * int(core @ core))
    rank_b = len(exact_rref(d2)[1])
    rank_augmented = len(exact_rref(np.column_stack((d2, boundary - 2 * core)))[1])
    assert rank_b == rank_augmented == 18
    assert a2 == Fraction(41, 86) and b2 == Fraction(41, 344)
    return {"a_squared": str(a2), "b_squared": str(b2),
            "boundary_matrix_rank": rank_b,
            "boundary_plus_relation_rank": rank_augmented,
            "status": "EXACT_RATIONAL_LOCAL_FIXTURE_PASSED"}


def mobius(length=3):
    def vertex(i, j):
        return (i * 3 + j) if i < length else (2 - j)

    triangles = set()
    for i in range(length):
        for j in range(2):
            a, b = vertex(i, j), vertex(i + 1, j)
            c, d = vertex(i, j + 1), vertex(i + 1, j + 1)
            triangles.add(tuple(sorted((a, b, d))))
            triangles.add(tuple(sorted((a, c, d))))
    core_walk = []
    for i in range(length):
        u, v, w = vertex(i, 1), vertex(i + 1, 1), 3 * length + i
        core_walk.extend((u, w))
        affected = [t for t in triangles if u in t and v in t]
        assert len(affected) == 2
        for t in affected:
            z = next(x for x in t if x not in (u, v))
            triangles.remove(t)
            triangles.add(tuple(sorted((u, w, z))))
            triangles.add(tuple(sorted((w, v, z))))
    boundary_walk = [vertex(i, 0) for i in range(length)]
    boundary_walk += [vertex(i, 2) for i in range(length)]
    triangles = sorted(triangles)
    edges = sorted({e for t in triangles for e in combinations(t, 2)})
    edge_index = {e: i for i, e in enumerate(edges)}
    d1 = np.zeros((4 * length, len(edges)))
    d2 = np.zeros((len(edges), len(triangles)))
    for i, (u, v) in enumerate(edges):
        d1[u, i], d1[v, i] = -1, 1
    for i, (a, b, c) in enumerate(triangles):
        for edge, sign in [((b, c), 1), ((a, c), -1), ((a, b), 1)]:
            d2[edge_index[edge], i] = sign

    def cycle(walk):
        c = np.zeros(len(edges))
        for u, v in zip(walk, walk[1:] + walk[:1]):
            c[edge_index[tuple(sorted((u, v)))]] += 1 if u < v else -1
        return c

    return d1, d2, cycle(boundary_walk), cycle(core_walk)


def zigzag(bands, a, b):
    n = 2 * bands + 1
    D, Bt = np.zeros((2 * bands, n)), np.zeros((2 * bands, n))
    for i in range(bands):
        x, y, z = 2 * i, 2 * i + 1, 2 * i + 2
        D[2 * i, x], D[2 * i, y] = -a, 1
        D[2 * i + 1, z], D[2 * i + 1, y] = -b, 1
        Bt[2 * i, x], Bt[2 * i, y] = -1, a
        Bt[2 * i + 1, z], Bt[2 * i + 1, y] = -1, b
    L = np.array([value for i in range(bands) for value in (2.0**i, a * 2.0**i)] + [2.0**bands])
    K = np.array([value for i in range(bands) for value in (2.0**-i, 2.0**-i / a)] + [2.0**-bands])
    L /= np.linalg.norm(L)
    K /= np.linalg.norm(K)
    assert np.linalg.norm(D @ L) < 1e-12
    assert np.linalg.norm(Bt @ K) < 1e-12
    return {
        "bands": bands,
        "poset_vertices": n,
        "rho": 1,
        "D_gap": float(np.linalg.svd(D, compute_uv=False)[-1]),
        "B_gap": float(np.linalg.svd(Bt, compute_uv=False)[-1]),
        "angle_cosine_formula": float((2 * bands + 1) / np.sqrt(
            ((4.0**(bands + 1) - 1 + a*a*(4.0**bands - 1)) / 3)
            * ((1 - 4.0**(-bands - 1) + (1 - 4.0**-bands)/(a*a)) / (1 - 0.25)))),
        "angle_cosine_direct": float(np.dot(L, K)),
    }


def main():
    d1, d2, boundary, core = mobius()
    assert np.linalg.norm(d1 @ d2) == 0
    assert np.linalg.norm(d1 @ boundary) == 0
    assert np.linalg.norm(d1 @ core) == 0
    assert np.linalg.norm(boundary) == np.linalg.norm(core)
    H = null_space(np.vstack((d1, d2.T)))
    assert H.shape[1] == 1
    h = H[:, 0]
    a = float(h @ boundary / np.linalg.norm(boundary))
    b = float(h @ core / np.linalg.norm(core))
    if b < 0:
        a, b = -a, -b
    assert abs(a / b - 2) < 1e-10
    # Chain-level homology relation, independently checked using a filling.
    filling, *_ = np.linalg.lstsq(d2, boundary - 2 * core, rcond=None)
    relation_residual = float(np.linalg.norm(d2 @ filling - boundary + 2 * core))
    assert relation_residual < 1e-10
    laplacian_eigenvalues = np.linalg.eigvalsh(d1.T @ d1 + d2 @ d2.T)
    rows = [zigzag(m, a, b) for m in (1, 2, 4, 8, 16, 32)]
    for row in rows:
        assert np.isclose(row["angle_cosine_formula"], row["angle_cosine_direct"], rtol=1e-12)
    print(json.dumps({
        "local_simplices": {"vertices": d1.shape[0], "edges": d1.shape[1], "triangles": d2.shape[1]},
        "circle_edges": int(np.sum(boundary**2)),
        "band_H1_dimension": H.shape[1],
        "local_H1_laplacian_gap": float(laplacian_eigenvalues[laplacian_eigenvalues > 1e-8][0]),
        "boundary_harmonic_coefficient_a": a,
        "core_harmonic_coefficient_b": b,
        "a_over_b": a / b,
        "relation_residual": relation_residual,
        "exact_local_check": exact_local_check(d1, d2, boundary, core),
        "uniform_D_B_gap_lower_bound": float((a - b) / np.sqrt(2 + a*a + b*b)),
        "zigzags": rows,
        "status": "NUMERICAL_SANITY_CHECK_NOT_COMPLEXITY_OR_NOVELTY_PROOF",
    }, indent=2))


if __name__ == "__main__":
    main()
