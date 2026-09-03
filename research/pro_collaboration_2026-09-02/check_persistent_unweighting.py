#!/usr/bin/env python3
"""Small independent persistent-domain checks for the spectral-transfer claim.

Requires the parent direction-selection NumPy/SciPy environment. This is a
finite diagnostic, not a proof of an infinite family or a quantum simulation.
"""
from itertools import combinations, product
import json
import numpy as np
from scipy.linalg import null_space

TOL = 2e-8


def complex_from_facets(facets):
    result = set()
    for facet in facets:
        for size in range(1, len(facet) + 1):
            result.update(combinations(sorted(facet), size))
    return result


def simplices(complex_, degree):
    return sorted(s for s in complex_ if len(s) == degree + 1)


def boundary(complex_, degree, weights):
    cols = simplices(complex_, degree)
    if degree == 0:
        return np.zeros((0, len(cols)))
    rows = {s: i for i, s in enumerate(simplices(complex_, degree - 1))}
    matrix = np.zeros((len(rows), len(cols)))
    for j, simplex in enumerate(cols):
        for i, vertex in enumerate(simplex):
            matrix[rows[simplex[:i] + simplex[i+1:]], j] = (-1)**i * weights[vertex]
    return matrix


def kernel(matrix):
    if matrix.shape[1] == 0:
        return np.zeros((0, 0))
    if matrix.shape[0] == 0:
        return np.eye(matrix.shape[1])
    return null_space(matrix, rcond=1e-11)


def persistent(first, last, degree, weights):
    target = simplices(first, degree)
    ambient = simplices(last, degree)
    rows = [ambient.index(s) for s in target]
    outside = [i for i, s in enumerate(ambient) if s not in first]
    full_boundary = boundary(last, degree + 1, weights)
    domain = kernel(full_boundary[outside, :])
    restricted = full_boundary[rows, :] @ domain
    down = boundary(first, degree, weights)
    result = restricted @ restricted.T + down.T @ down
    return (result + result.T) / 2


def blocks_for(multiplicities):
    blocks, labels, cursor = {}, {}, 0
    for vertex, count in sorted(multiplicities.items()):
        blocks[vertex] = tuple(range(cursor, cursor + count))
        for label in blocks[vertex]:
            labels[label] = vertex
        cursor += count
    return blocks, labels


def blowup(complex_, blocks, labels):
    present = sorted({v for simplex in complex_ for v in simplex})
    copies = [copy for vertex in present for copy in blocks[vertex]]
    result = set()
    for size in range(1, len(copies) + 1):
        for simplex in combinations(copies, size):
            support = tuple(sorted({labels[v] for v in simplex}))
            if support in complex_:
                result.add(simplex)
    return result


def lift(complex_, expanded, degree, blocks):
    source = simplices(complex_, degree)
    target = {s: i for i, s in enumerate(simplices(expanded, degree))}
    matrix = np.zeros((len(target), len(source)))
    for j, simplex in enumerate(source):
        coefficient = np.prod([len(blocks[v]) for v in simplex]) ** -0.5
        for copies in product(*(blocks[v] for v in simplex)):
            matrix[target[tuple(copies)], j] = coefficient
    return matrix


def inclusion(first, last, degree):
    source = simplices(first, degree)
    rows = {s: i for i, s in enumerate(simplices(last, degree))}
    matrix = np.zeros((len(rows), len(source)))
    for j, simplex in enumerate(source):
        matrix[rows[simplex], j] = 1
    return matrix


def operator_norm(matrix):
    return float(np.linalg.norm(matrix, 2)) if matrix.size else 0.0


def eigmin(matrix):
    return float(np.linalg.eigvalsh(matrix)[0]) if matrix.size else None


def verify_family(name, facets_by_level, multiplicities, scale, flag_scope):
    levels = [complex_from_facets(facets) for facets in facets_by_level]
    for first, last in zip(levels, levels[1:]):
        assert first <= last
    blocks, labels = blocks_for(multiplicities)
    expanded = [blowup(c, blocks, labels) for c in levels]
    weights = {v: (count / scale)**0.5 for v, count in multiplicities.items()}
    unweighted = {v: 1.0 for v in labels}
    results = []
    for a, first in enumerate(levels):
        for b in range(a, len(levels)):
            for degree in range(3):
                if not simplices(first, degree):
                    continue
                last = levels[b]
                left = persistent(first, last, degree, weights)
                right = persistent(expanded[a], expanded[b], degree, unweighted)
                ua = lift(first, expanded[a], degree, blocks)
                ub = lift(last, expanded[b], degree, blocks)
                residual = operator_norm(right @ ua - scale * ua @ left)
                naturality = operator_norm(inclusion(expanded[a], expanded[b], degree) @ ua
                                           - ub @ inclusion(first, last, degree))
                isometry = operator_norm(ua.T @ ua - np.eye(ua.shape[1]))
                complement = kernel(ua.T)
                asymmetric_min = eigmin(complement.T @ right @ complement)
                min_copies = min(multiplicities[v] for s in first for v in s)
                domination = eigmin(right - persistent(expanded[a], expanded[a], degree, unweighted))
                base_eigenvalues = np.linalg.eigvalsh(left)
                expanded_eigenvalues = np.linalg.eigvalsh(right)
                assert residual < TOL and naturality < TOL and isometry < TOL
                assert asymmetric_min is None or asymmetric_min >= min_copies - TOL
                assert domination is None or domination >= -TOL
                assert np.count_nonzero(abs(base_eigenvalues) < TOL) == np.count_nonzero(abs(expanded_eigenvalues) < TOL)
                cutoff = 0.73 * min_copies
                weighted_low = scale * base_eigenvalues[scale * base_eigenvalues < cutoff - TOL]
                unweighted_low = expanded_eigenvalues[expanded_eigenvalues < cutoff - TOL]
                assert len(weighted_low) == len(unweighted_low)
                assert np.allclose(weighted_low, unweighted_low, atol=TOL, rtol=TOL)
                results.append(dict(pair=[a, b], degree=degree, base_dim=len(left),
                                    expanded_dim=len(right), intertwining_residual=residual,
                                    naturality_residual=naturality, asymmetric_min=asymmetric_min,
                                    asymmetric_bound=min_copies, domination_min=domination,
                                    nullity=int(np.count_nonzero(abs(base_eigenvalues) < TOL))))
    return dict(name=name, within_stated_clique_scope=flag_scope, results=results)


def main():
    families = [
        ('path_to_triangle', [[(0, 1), (1, 2)], [(0, 1, 2)]], {0: 4, 1: 1, 2: 2}, 4, True),
        ('square_to_disk_with_diagonal_cancellation',
         [[(0, 1), (1, 2), (2, 3), (0, 3)], [(0, 1, 2), (0, 2, 3)]],
         {0: 2, 1: 1, 2: 2, 3: 1}, 4, True),
        ('vertices_path_triangle', [[(0,), (1,), (2,)], [(0, 1), (1, 2)], [(0, 1, 2)]],
         {0: 2, 1: 1, 2: 2}, 4, True),
        ('new_vertex_cone_over_square',
         [[(0, 1), (1, 2), (2, 3), (0, 3)],
          [(0, 1, 4), (1, 2, 4), (2, 3, 4), (0, 3, 4)]],
         {0: 1, 1: 2, 2: 1, 3: 2, 4: 1}, 4, True),
        ('nonflag_tetrahedron_boundary_diagnostic',
         [[(i, j) for i, j in combinations(range(4), 2)], list(combinations(range(4), 3))],
         {0: 2, 1: 1, 2: 1, 3: 2}, 4, False),
        ('sharp_asymmetric_threshold', [[(0,)]], {0: 3}, 1, True),
    ]
    records = [verify_family(*f) for f in families]
    # Independent trap: deleting outside rows is not the persistent boundary.
    square = complex_from_facets([(0, 1), (1, 2), (2, 3), (0, 3)])
    disk = complex_from_facets([(0, 1, 2), (0, 2, 3)])
    weights = {i: 1 for i in range(4)}
    true = persistent(square, disk, 1, weights)
    ambient = simplices(disk, 1)
    rows = [ambient.index(s) for s in simplices(square, 1)]
    sliced = boundary(disk, 2, weights)[rows, :]
    down = boundary(square, 1, weights)
    wrong = sliced @ sliced.T + down.T @ down
    trap_residual = operator_norm(wrong - true)
    assert trap_residual > 0.5
    all_rows = [r for f in records for r in f['results']]
    print(json.dumps(dict(status='PASS', tolerance=TOL, family_count=len(records),
                          pair_degree_checks=len(all_rows),
                          max_intertwining_residual=max(r['intertwining_residual'] for r in all_rows),
                          wrong_row_deletion_residual=trap_residual,
                          scope='Finite matrix diagnostics; nonflag case is outside the formal conditional theorem.',
                          families=records), indent=2))


if __name__ == '__main__':
    main()
