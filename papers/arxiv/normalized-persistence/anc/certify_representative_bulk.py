"""Recover the source representative graph and certify its central bulk.

The upstream graph construction is GPLv2-or-later, attributed to Dorian Rudolph.
We fetch its pinned source but do not redistribute it here. Only the inspected
graph-building function definitions are evaluated; the graph shim stops before
Sage homology routines, plotting, or any top-level upstream calls execute.
Outputs are mathematical graph data and a modular certificate for an integer Gram matrix.

With --offline, read the archived graph instead and recompute every mathematical
certificate field without invoking gh or the network. This mode verifies the
supplied graph; it does not independently replay upstream graph construction.
"""

import argparse
import ast
from pathlib import Path
import hashlib
import itertools
import json
import math
from fractions import Fraction
import subprocess

import numpy as np

SOURCE_COMMIT = "30ac70e5dacdecce97c38d801c128ec3ed93a96a"
SOURCE_SHA256 = "c8918f9e037ae79796bb65640170c8e60f31883625d24348f3476f7644dcd29a"
VERTEX_NAMES = "xx, a2, a3, a4, b2, b3, b4".split(", ")
SOURCE_PATH = "gadget_homology.py"
SOURCE_URL = (
    "https://github.com/DorianRudolph/QMA1-gateset-paper/blob/"
    + SOURCE_COMMIT + "/" + SOURCE_PATH
)


class CaptureGraph(Exception):
    def __init__(self, graph):
        self.graph = graph


class Graph:
    def __init__(self, edges=None):
        self.vertices = set()
        self.pairs = set()
        if edges is not None:
            self.add_edges(edges)

    def __iter__(self):
        return iter(sorted(self.vertices))

    def add_edges(self, edges):
        for a, b in edges:
            self.vertices.update((a, b))
            if a != b:
                self.pairs.add(tuple(sorted((a, b))))

    def edges(self, labels=False, sort_vertices=True):
        return sorted(self.pairs)

    def union(self, other):
        result = Graph()
        result.vertices = self.vertices | other.vertices
        result.pairs = self.pairs | other.pairs
        return result

    def delete_edge(self, a, b):
        self.pairs.remove(tuple(sorted((a, b))))

    def merge_vertices(self, vertices):
        target = vertices[0]
        merged = set(vertices)
        result = set()
        for a, b in self.pairs:
            a = target if a in merged else a
            b = target if b in merged else b
            if a != b:
                result.add(tuple(sorted((a, b))))
        self.vertices = (self.vertices - merged) | {target}
        self.pairs = result

    def clique_complex(self):
        raise CaptureGraph(self)


def all_cliques(graph):
    vertices = sorted(graph.vertices)
    adjacent = {v: set() for v in vertices}
    for a, b in graph.pairs:
        adjacent[a].add(b)
        adjacent[b].add(a)
    by_degree = {}

    def extend(prefix, candidates):
        for i, v in enumerate(candidates):
            simplex = prefix + (v,)
            by_degree.setdefault(len(simplex) - 1, []).append(simplex)
            extend(simplex, [w for w in candidates[i + 1:] if w in adjacent[v]])

    extend((), vertices)
    return by_degree


def boundary(cells, degree):
    rows = {s: i for i, s in enumerate(cells.get(degree - 1, []))}
    columns = cells.get(degree, [])
    matrix = np.zeros((len(rows), len(columns)), dtype=np.int64)
    for j, simplex in enumerate(columns):
        for i in range(degree + 1):
            matrix[rows[simplex[:i] + simplex[i + 1:]], j] = (-1) ** i
    return matrix


def weighted_boundary(cells, degree, weights):
    rows = {s: i for i, s in enumerate(cells.get(degree - 1, []))}
    columns = cells.get(degree, [])
    matrix = np.zeros((len(rows), len(columns)), dtype=np.int64)
    for j, simplex in enumerate(columns):
        for i, vertex in enumerate(simplex):
            matrix[rows[simplex[:i] + simplex[i + 1:]], j] = (-1) ** i * weights[vertex]
    return matrix


def det_mod_prime(matrix, prime):
    value = np.remainder(matrix, prime).copy()
    n = len(value)
    determinant = 1
    for column in range(n):
        candidates = np.flatnonzero(value[column:, column])
        if not len(candidates):
            return 0, column
        pivot = column + int(candidates[0])
        if pivot != column:
            value[[column, pivot]] = value[[pivot, column]]
            determinant = -determinant
        pivot_value = int(value[column, column])
        determinant = determinant * pivot_value % prime
        inverse = pow(pivot_value, -1, prime)
        factors = value[column + 1:, column] * inverse % prime
        value[column + 1:, column:] = (
            value[column + 1:, column:]
            - factors[:, None] * value[column, column:][None, :]
        ) % prime
    return determinant % prime, n


def echelon_mod_prime(matrix, prime, rhs=None):
    columns = matrix.shape[1]
    value = np.remainder(
        np.column_stack((matrix, rhs)) if rhs is not None else matrix, prime
    ).copy()
    pivots = []
    row = 0
    for column in range(columns):
        candidates = np.flatnonzero(value[row:, column])
        if not len(candidates):
            continue
        pivot = row + int(candidates[0])
        if pivot != row:
            value[[row, pivot]] = value[[pivot, row]]
        inverse = pow(int(value[row, column]), -1, prime)
        factors = value[row + 1:, column] * inverse % prime
        value[row + 1:, column:] = (
            value[row + 1:, column:]
            - factors[:, None] * value[row, column:][None, :]
        ) % prime
        pivots.append(column)
        row += 1
        if row == len(value):
            break
    return value, pivots


def reconstruct_rational(residue, prime):
    bound = math.isqrt(prime // 2)
    a, b, u, v = prime, int(residue), 0, 1
    while abs(b) > bound:
        quotient = a // b
        a, b, u, v = b, a - quotient * b, v, u - quotient * v
    if not v or abs(v) > bound or (b - int(residue) * v) % prime:
        raise ArithmeticError("Rational reconstruction failed")
    return Fraction(b, v)


def register_basis(cells):
    rows = {simplex: i for i, simplex in enumerate(cells[3])}

    def edges(qubit, bit):
        petal = "b" if bit else "a"
        cycle = [f"{qubit}.xx", f"{qubit}.{petal}3",
                 f"{qubit}.{petal}2", f"{qubit}.{petal}4"]
        return [(cycle[i], cycle[(i + 1) % 4]) for i in range(4)]

    basis = np.zeros((len(rows), 4), dtype=np.int64)
    for first in (0, 1):
        for second in (0, 1):
            for a, b in itertools.product(edges(0, first), edges(1, second)):
                oriented = a + b
                inversions = sum(oriented[i] > oriented[j]
                                 for i in range(4) for j in range(i + 1, 4))
                basis[rows[tuple(sorted(oriented))], 2 * first + second] += (-1) ** inversions
    return basis


def recover_source_graph(upstream):
    assert hashlib.sha256(upstream).hexdigest() == SOURCE_SHA256
    wanted = {
        "make_graph", "thicken", "fill_cycle", "join_keep_names",
        "state_00m10m11",
    }
    parsed = ast.parse(upstream.decode())
    definitions = [
        node for node in parsed.body
        if isinstance(node, ast.FunctionDef) and node.name in wanted
    ]
    assert {node.name for node in definitions} == wanted
    namespace = {
        "Graph": Graph, "itertools": itertools, "v0": "v0",
        "vertex_names": VERTEX_NAMES,
    }
    exec(compile(ast.Module(body=definitions, type_ignores=[]), SOURCE_URL, "exec"), namespace)
    try:
        namespace["state_00m10m11"]()
    except CaptureGraph as captured:
        return captured.graph
    else:
        raise AssertionError("Expected capture before source homology computation")


def main():
    folder = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true",
                        help="Recompute the certificate from archived graph data; no gh/network.")
    parser.add_argument("--certificate", type=Path,
                        default=folder / "RUDOLPH_REPRESENTATIVE_BULK_CERTIFICATE.json")
    args = parser.parse_args()
    archived = None
    archived_bytes = None
    if args.offline:
        archived_bytes = args.certificate.read_bytes()
        archived = json.loads(archived_bytes)
        assert archived["source"]["commit"] == SOURCE_COMMIT
        assert archived["source"]["sha256"] == SOURCE_SHA256
        graph = Graph(archived["graph"]["edges"])
        declared_vertices = set(archived["graph"]["vertices"])
        assert graph.vertices <= declared_vertices
        graph.vertices = declared_vertices
    else:
        upstream = subprocess.check_output([
            "gh", "api",
            "repos/DorianRudolph/QMA1-gateset-paper/contents/"
            + SOURCE_PATH + "?ref=" + SOURCE_COMMIT,
            "-H", "Accept: application/vnd.github.raw+json",
        ])
        graph = recover_source_graph(upstream)

    cells = all_cliques(graph)
    central = "v0"
    neighbors = {
        b if a == central else a
        for a, b in graph.pairs if central in (a, b)
    }
    link = Graph()
    link.vertices = neighbors
    link.pairs = {e for e in graph.pairs if set(e) <= neighbors}
    link_cells = all_cliques(link)
    d2 = boundary(link_cells, 2)
    d3 = boundary(link_cells, 3)
    assert not np.any(d2 @ d3)
    gram = d2.T @ d2 + d3 @ d3.T
    dimension = gram.shape[0]
    assert dimension > 0 and gram.shape[1] == dimension
    prime = 1000003
    assert all(prime % divisor for divisor in range(2, math.isqrt(prime) + 1))
    determinant, rank = det_mod_prime(gram, prime)
    assert determinant != 0 and rank == dimension
    bound = int(np.abs(gram).sum(axis=1).max())
    # A positive integral determinant is >=1; each eigenvalue is <=bound.
    # sigma_min([d2; d3.T]) >= bound^(-(dimension-1)/2) >= bound^(-dimension).
    denominator = str(pow(bound, dimension))
    boundaries = {degree: boundary(cells, degree) for degree in range(1, max(cells) + 1)}
    for degree in range(2, max(cells) + 1):
        assert not np.any(boundaries[degree - 1] @ boundaries[degree])
    basis = register_basis(cells)
    assert np.array_equal(basis.T @ basis, 16 * np.eye(4, dtype=np.int64))
    assert not np.any(boundaries[3] @ basis)
    phi = basis @ np.array([1, 0, -1, -1], dtype=np.int64)
    survivors = basis @ np.array([[1, 0, 0], [0, 0, 1],
                                 [0, 1, 0], [1, -1, 0]], dtype=np.int64)
    echelon4, pivots4 = echelon_mod_prime(
        boundaries[4], prime, np.column_stack((phi, survivors))
    )
    ranks = {}
    for degree, matrix in boundaries.items():
        ranks[degree] = len(pivots4) if degree == 4 else len(echelon_mod_prime(matrix, prime)[1])
    exact_rank_bounds = {}
    for degree, lower in ranks.items():
        upper = min(
            len(cells[degree - 1]) - ranks.get(degree - 1, 0),
            len(cells[degree]) - ranks.get(degree + 1, 0),
        )
        assert lower == upper, (degree, lower, upper)
        exact_rank_bounds[str(degree)] = {"rank_mod_prime": lower, "rational_rank_upper_bound": upper}
    ncols4 = boundaries[4].shape[1]
    assert not np.any(echelon4[len(pivots4):, ncols4])
    survivor_rank = len(echelon_mod_prime(
        echelon4[len(pivots4):, ncols4 + 1:], prime
    )[1])
    assert survivor_rank == 3
    modular_solution = np.zeros(ncols4, dtype=np.int64)
    for row in range(len(pivots4) - 1, -1, -1):
        column = pivots4[row]
        residue = (int(echelon4[row, ncols4])
                   - int(echelon4[row, column + 1:ncols4] @ modular_solution[column + 1:])) % prime
        modular_solution[column] = residue * pow(int(echelon4[row, column]), -1, prime) % prime
    rational_solution = [reconstruct_rational(value, prime) for value in modular_solution]
    filling_denominator = math.lcm(*(value.denominator for value in rational_solution))
    coefficients = np.array([
        value.numerator * (filling_denominator // value.denominator)
        for value in rational_solution
    ], dtype=object)
    assert np.array_equal(
        boundaries[4].astype(object) @ coefficients, filling_denominator * phi.astype(object)
    )
    betti = {str(k): len(cells[k]) - ranks.get(k, 0) - ranks.get(k + 1, 0) for k in cells}
    assert betti["3"] == 3
    register_vertices = {f"{qubit}.{name}" for qubit in (0, 1)
                         for name in VERTEX_NAMES}
    zero_weights = {v: int(v in register_vertices) for v in graph.vertices}
    one_weights = {v: 1 - zero_weights[v] for v in graph.vertices}
    down0 = weighted_boundary(cells, 3, zero_weights)
    up0 = weighted_boundary(cells, 4, zero_weights)
    down1 = weighted_boundary(cells, 3, one_weights)
    up1 = weighted_boundary(cells, 4, one_weights)
    pair0 = np.vstack((down0, up0.T))
    pair1 = np.vstack((down1, up1.T))
    bulk_indices = [i for i, s in enumerate(cells[3]) if central in s]
    assert len(bulk_indices) == dimension
    assert not np.any(pair0 @ basis)
    assert not np.any(pair0[:, bulk_indices])
    rank0 = len(echelon_mod_prime(pair0, prime)[1])
    known_kernel_dimension = 4 + len(bulk_indices)
    assert rank0 == len(cells[3]) - known_kernel_dimension
    low_bulk_rows = [i for i, s in enumerate(cells[2]) if central in s]
    high_bulk_rows = [i for i, s in enumerate(cells[4]) if central in s]
    t0 = np.vstack((down0[low_bulk_rows, :], up0.T[high_bulk_rows, :]))
    t1 = np.vstack((down1[low_bulk_rows, :], up1.T[high_bulk_rows, :]))
    assert not np.any(t0)
    assert not np.any(t1 @ basis)
    assert all(v not in register_vertices for v in neighbors)
    zero_gram = pair0.T @ pair0
    derivative_gram = pair1.T @ pair1
    unweighted_gram = boundaries[3].T @ boundaries[3] + boundaries[4] @ boundaries[4].T
    gram_bounds = {
        "zero_weight_gram_infinity_norm": int(np.abs(zero_gram).sum(axis=1).max()),
        "derivative_gram_infinity_norm": int(np.abs(derivative_gram).sum(axis=1).max()),
        "unweighted_gram_infinity_norm": int(np.abs(unweighted_gram).sum(axis=1).max()),
    }
    output = {
        "status": "PASS",
        "scope": "Exact target homology, intended filling, zero-weight kernel, and central-relative-bulk injectivity for one source graph; not the complete guarded palette",
        "source": {
            "url": SOURCE_URL, "commit": SOURCE_COMMIT,
            "sha256": SOURCE_SHA256,
            "function": "state_00m10m11", "upstream_license": "GPLv2-or-later",
            "execution": "Only inspected graph-building AST definitions; stopped before Sage operations",
        },
        "projector": {
            "integer_amplitudes_00_01_10_11": [1, 0, -1, -1],
            "relation_to_requested_representative": "Overall minus sign; same rank-one projector",
        },
        "graph": {
            "vertices": sorted(graph.vertices),
            "edges": [list(e) for e in sorted(graph.pairs)],
            "simplex_counts": {str(k): len(v) for k, v in sorted(cells.items())},
            "maximum_dimension": max(cells),
        },
        "central_link": {
            "vertices": sorted(link.vertices),
            "edges": [list(e) for e in sorted(link.pairs)],
            "simplex_counts": {str(k): len(v) for k, v in sorted(link_cells.items())},
            "ordered_triangles": [list(t) for t in link_cells[2]],
        },
        "certificate": {
            "target_local_degree": 3, "link_degree": 2,
            "gram_dimension": dimension,
            "boundary_composition_exact_zero": True,
            "prime": prime, "determinant_mod_prime": determinant,
            "rank_mod_prime": rank, "integer_gram_infinity_norm": bound,
            "integer_gram_sha256": hashlib.sha256(
                json.dumps(gram.tolist(), separators=(",", ":")).encode()
            ).hexdigest(),
            "rational_lower_bound_for_unscaled_pair_singular_value": {
                "numerator": 1, "denominator": denominator,
            },
            "proof": "The nonzero determinant modulo a prime implies a nonzero integer determinant. The Gram matrix is positive definite. Its eigenvalues are at most the infinity norm, so its least eigenvalue is at least that bound to power -(dimension-1).",
            "weighted_consequence": "For binary weights, the projected central-bulk pair on degree 3 equals lambda times this link pair, up to orientation signs.",
        },
        "topology_certificate": {
            "ordinary_betti_over_Q": betti,
            "boundary_compositions_exact_zero": True,
            "boundary_ranks": exact_rank_bounds,
            "rank_proof": "Rational ranks are at least ranks modulo the prime. Each rank is at most either adjacent chain dimension minus the adjacent rank. The recorded lower and upper bounds agree.",
            "three_survivors_independent_mod_boundaries": True,
            "survivor_coefficient_columns_00_01_10_11": [[1, 0, 0], [0, 0, 1], [0, 1, 0], [1, -1, 0]],
            "survivor_proof": "The boundary rank over Q is certified exactly. Appending the three cycle columns increases rank by three modulo the prime, hence also over Q.",
            "exact_filling_denominator": filling_denominator,
            "exact_filling_chain": [
                {"simplex": list(cells[4][j]), "coefficient": int(coefficient)}
                for j, coefficient in enumerate(coefficients) if coefficient
            ],
            "filling_equation_verified_over_integers": True,
            "register_intersection": "Exactly the span of ket00-ket10-ket11: that cycle has an explicit rational filling and three complementary register cycles survive independently.",
            "positive_weight_extension": "Invertible diagonal weight gauge preserves homology; weight-one register coordinates preserve the exact register boundary intersection for every lambda>0.",
        },
        "zero_weight_certificate": {
            "register_vertices": sorted(register_vertices),
            "register_cycle_dimension": 4,
            "register_basis_gram": "16 I_4; divide each cycle by 4 for an isometry",
            "central_bulk_dimension": len(bulk_indices),
            "differential_pair_rank_mod_prime": rank0,
            "rational_rank_upper_bound_from_known_kernel": len(cells[3]) - known_kernel_dimension,
            "kernel_exactly_register_cycles_plus_central_bulk": True,
            "projected_bulk_pair_zero_constant_term": True,
            "projected_bulk_pair_annihilates_register_cycles": True,
            "central_vertex_has_only_new_neighbors": True,
            **gram_bounds,
            "positive_gap_proof": "For an integral PSD Gram matrix of rank r and norm at most B, its nonzero eigenvalue product is a positive integer, so the least positive eigenvalue is at least B^(-(r-1)).",
            "weighted_gap_proof": "For each boundary, partial_w=W_rows^(-1) partial_1 W_columns. The left scaling has minimum singular value at least one; a degree-k column weight is at least lambda^(k+1). Nonzero singular values therefore decrease by at most that factor. At target degree 3 this gives a whole positive Laplacian lower bound c lambda^10.",
            "not_certified": "Leading eigenvalue coefficient, optimal valuation, and guarded-palette closure are not implied by this certificate.",
        },
        "not_certified": [
            "Optimal weighted lifted eigenvalue valuation or its leading coefficient",
            "Full guarded-palette closure under the new finite zero-weight criterion",
            "Complete guarded palette through locality six",
            "Full reduction or priority",
        ],
    }
    summary = {
        "status": output["status"],
        "verification_mode": "archived_graph" if args.offline else "pinned_source_replay",
        "upstream_replayed_this_run": not args.offline,
        "source_sha256": output["source"]["sha256"],
        "graph_vertices": len(graph.vertices), "graph_edges": len(graph.pairs),
        "simplex_counts": output["graph"]["simplex_counts"],
        "maximum_dimension": max(cells),
        "central_link_simplex_counts": output["central_link"]["simplex_counts"],
        "gram_dimension": dimension, "prime": prime,
        "determinant_mod_prime": determinant, "infinity_norm": bound,
        "rational_bound_denominator_digits": len(denominator),
        "exact_boundary_ranks_over_Q": ranks, "betti_over_Q": betti,
        "filling_chain_nonzeros": int(np.count_nonzero(coefficients)),
        "filling_denominator": filling_denominator,
        "zero_weight_pair_rank": rank0,
        "zero_weight_kernel_dimension": known_kernel_dimension,
        **gram_bounds,
    }
    if args.offline:
        checked_fields = [
            "projector", "graph", "central_link", "certificate",
            "topology_certificate", "zero_weight_certificate",
        ]
        for field in checked_fields:
            assert output[field] == archived[field], ("certificate mismatch", field)
        summary.update({
            "input_certificate": args.certificate.name,
            "input_certificate_sha256": hashlib.sha256(archived_bytes).hexdigest(),
            "recomputed_fields_match_archive": checked_fields,
            "scope": "Exact recomputation from supplied graph data; upstream provenance was not reverified.",
        })
        destination = folder / "OFFLINE_REPRESENTATIVE_CHECKS.json"
        summary["file"] = destination.name
        destination.write_text(json.dumps(summary, indent=2) + "\n")
    else:
        destination = folder / "RUDOLPH_REPRESENTATIVE_BULK_CERTIFICATE.json"
        summary["file"] = destination.name
        destination.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
