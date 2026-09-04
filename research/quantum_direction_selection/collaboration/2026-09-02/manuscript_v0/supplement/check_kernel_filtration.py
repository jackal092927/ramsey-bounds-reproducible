"""Small clique-complex check of independent fillings and persistence ranks.

This is classical exact-combinatorial / floating-point linear algebra, not a
quantum simulation and not a test of the full King--Kohler construction.
Run: python3 research/quantum_direction_selection/round2/check_kernel_filtration.py
"""

import itertools
import json

import numpy as np
from scipy.linalg import eigh, null_space, svdvals


def edge(a, b):
    return tuple(sorted((a, b)))


def bouquet(offset):
    cycles = ((0, 1, 2, 3), (0, 4, 5, 6))
    return {
        edge(offset + cycle[i], offset + cycle[(i + 1) % 4])
        for cycle in cycles for i in range(4)
    }


def complex_at(level):
    # Join two flag figure-eights. Added cones have no mutual edge.
    edges = bouquet(0) | bouquet(7)
    edges |= {edge(a, b) for a in range(7) for b in range(7, 14)}
    if level >= 1:
        edges |= {edge(14, v) for v in [0, 1, 2, 3] + list(range(7, 14))}
    if level >= 2:
        edges |= {edge(15, v) for v in [7, 8, 9, 10] + list(range(7))}
    simplices = {}
    for degree in (2, 3, 4):
        simplices[degree] = [
            s for s in itertools.combinations(range(16), degree + 1)
            if all(edge(a, b) in edges for a, b in itertools.combinations(s, 2))
        ]
    return simplices


def boundary(simplices, degree, weights):
    rows = {s: i for i, s in enumerate(simplices[degree - 1])}
    out = np.zeros((len(rows), len(simplices[degree])))
    for j, s in enumerate(simplices[degree]):
        for i, v in enumerate(s):
            out[rows[s[:i] + s[i + 1:]], j] = (-1) ** i * weights[v]
    return out


def inclusion(source, target):
    rows = {s: i for i, s in enumerate(target[3])}
    out = np.zeros((len(rows), len(source[3])))
    for j, s in enumerate(source[3]):
        out[rows[s], j] = 1
    return out


def main():
    complexes = [complex_at(i) for i in range(3)]
    inclusions = [inclusion(complexes[i], complexes[i + 1]) for i in range(2)]
    results = []
    for lam in (1.0, 0.5, 0.25, 0.125):
        weights = [1.0] * 14 + [lam, lam]
        harmonics = []
        gaps = []
        counts = []
        rank_pairs = []
        for simplices in complexes:
            down = boundary(simplices, 3, weights)
            up = boundary(simplices, 4, weights)
            assert np.max(np.abs(down @ up), initial=0.0) < 1e-12
            lap = down.T @ down + up @ up.T
            spectrum, vectors = eigh(lap)
            harmonic = vectors[:, np.abs(spectrum) < 1e-9]
            harmonics.append(harmonic)
            counts.append(harmonic.shape[1])
            gaps.append(float(spectrum[spectrum > 1e-9][0]))
            rank_pairs.append((down, up))
        assert counts == [4, 2, 1], counts
        maps = []
        for i, embed in enumerate(inclusions):
            values = svdvals(harmonics[i + 1].T @ embed @ harmonics[i])
            rank = int(np.count_nonzero(values > 1e-8))
            # Independent rank formula on cycle and boundary spaces.
            cycles = embed @ null_space(rank_pairs[i][0])
            final_boundaries = rank_pairs[i + 1][1]
            concat_rank = np.linalg.matrix_rank(
                np.column_stack((cycles, final_boundaries)), tol=1e-8
            )
            boundary_rank = np.linalg.matrix_rank(final_boundaries, tol=1e-8)
            assert rank == concat_rank - boundary_rank == counts[i + 1]
            maps.append({"rank": rank, "ratio": rank / counts[i],
                         "positive_singular_values": values[values > 1e-8].tolist()})
        results.append({"lambda": lam, "betti": counts, "positive_gaps": gaps,
                        "successive_maps": maps})
    print(json.dumps({"status": "PASS", "kind": "classical mathematical fixture",
                      "vertices": 16, "degree": 3,
                      "degree_3_simplices": [len(c[3]) for c in complexes],
                      "expected_betti_by_Kunneth_and_relative_homology": [4, 2, 1],
                      "results": results}, indent=2))


if __name__ == "__main__":
    main()
