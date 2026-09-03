"""Certify the remaining one- and two-term active source atoms exactly.

Default mode replays only pinned source graph-building definitions and stops before
Sage. --offline recomputes the mathematical certificates from archived graphs.
"""
import argparse
import ast
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import subprocess

import numpy as np

from certify_representative_bulk import (
    CaptureGraph, Graph, SOURCE_COMMIT, SOURCE_PATH, SOURCE_SHA256, SOURCE_URL,
    VERTEX_NAMES, all_cliques, boundary, det_mod_prime, echelon_mod_prime,
    reconstruct_rational, weighted_boundary,
)

FOLDER = Path(__file__).resolve().parent
PRIME = 1000003


def clean(chain):
    return {simplex: int(coefficient) for simplex, coefficient in chain.items()
            if coefficient}


def oriented(vertices):
    sign = (-1) ** sum(vertices[i] > vertices[j]
                       for i in range(len(vertices)) for j in range(i + 1, len(vertices)))
    return tuple(sorted(vertices)), sign


def join_chain(first, second):
    result = Counter()
    for a, ca in first.items():
        for b, cb in second.items():
            simplex, sign = oriented(a + b)
            result[simplex] += sign * ca * cb
    return clean(result)


def chain_boundary(chain):
    result = Counter()
    for simplex, coefficient in chain.items():
        for i in range(len(simplex)):
            result[simplex[:i] + simplex[i + 1:]] += coefficient * (-1) ** i
    return clean(result)


def petal_cycle(qubit, bit):
    petal = "b" if bit else "a"
    walk = [f"{qubit}.xx", f"{qubit}.{petal}3",
            f"{qubit}.{petal}2", f"{qubit}.{petal}4"]
    result = Counter()
    for i in range(4):
        edge, sign = oriented((walk[i], walk[(i + 1) % 4]))
        result[edge] += sign
    return clean(result)


def logical_basis(n):
    answer = []
    for bits in itertools.product((0, 1), repeat=n):
        chain = {(): 1}
        for qubit, bit in enumerate(bits):
            chain = join_chain(chain, petal_cycle(qubit, bit))
        answer.append(chain)
    return answer


def chain_vector(chain, simplices):
    rows = {simplex: i for i, simplex in enumerate(simplices)}
    result = np.zeros(len(rows), dtype=np.int64)
    for simplex, coefficient in chain.items():
        result[rows[simplex]] = coefficient
    return result


def recover_graphs(upstream, state_names):
    assert hashlib.sha256(upstream).hexdigest() == SOURCE_SHA256
    wanted = {"make_graph", "thicken", "fill_cycle", "join_keep_names"} | set(state_names)
    tree = ast.parse(upstream.decode())
    definitions = [node for node in tree.body
                   if isinstance(node, ast.FunctionDef) and node.name in wanted]
    assert {node.name for node in definitions} == wanted
    namespace = {
        "Graph": Graph, "itertools": itertools, "v0": "v0",
        "vertex_names": VERTEX_NAMES,
    }
    exec(compile(ast.Module(body=definitions, type_ignores=[]), SOURCE_URL, "exec"),
         namespace)
    graphs = {}
    for name in state_names:
        try:
            namespace[name]()
        except CaptureGraph as captured:
            graphs[name] = captured.graph
        else:
            raise AssertionError("Expected graph capture before Sage for " + name)
    return graphs


def exact_ranks(boundaries, cells, prime):
    ranks = {degree: len(echelon_mod_prime(matrix, prime)[1])
             for degree, matrix in boundaries.items()}
    bounds = {}
    for degree, lower in ranks.items():
        candidates = [
            len(cells[degree - 1]) - ranks.get(degree - 1, 0),
            len(cells[degree]) - ranks.get(degree + 1, 0),
        ]
        # Every graph boundary has column sum zero. The matching modular
        # lower bound n_0-1 also certifies connectedness and exact rank.
        if degree == 1:
            candidates.append(len(cells[0]) - 1)
        upper = min(candidates)
        assert lower == upper, (degree, lower, upper)
        bounds[str(degree)] = {
            "rank_mod_prime": lower,
            "rational_rank_upper_bound": upper,
        }
    return ranks, bounds


def solve_filling(matrix, target, prime):
    echelon, pivots = echelon_mod_prime(matrix, prime, target)
    columns = matrix.shape[1]
    assert not np.any(echelon[len(pivots):, columns])
    solution = np.zeros(columns, dtype=np.int64)
    for row in range(len(pivots) - 1, -1, -1):
        column = pivots[row]
        residue = (
            int(echelon[row, columns])
            - int(echelon[row, column + 1:columns] @ solution[column + 1:])
        ) % prime
        solution[column] = residue * pow(int(echelon[row, column]), -1, prime) % prime
    rational = [reconstruct_rational(value, prime) for value in solution]
    denominator = math.lcm(*(value.denominator for value in rational))
    integer = np.array([
        value.numerator * (denominator // value.denominator) for value in rational
    ], dtype=object)
    assert np.array_equal(
        matrix.astype(object) @ integer,
        denominator * target.astype(object),
    )
    return denominator, integer


def certify_atom(graph, state, qubits, target_degree, amplitudes, survivors):
    cells = all_cliques(graph)
    boundaries = {
        degree: boundary(cells, degree) for degree in range(1, max(cells) + 1)
    }
    for degree in range(2, max(cells) + 1):
        assert not np.any(boundaries[degree - 1] @ boundaries[degree])
    ranks, rank_bounds = exact_ranks(boundaries, cells, PRIME)

    basis_chains = logical_basis(qubits)
    basis = np.column_stack([
        chain_vector(chain, cells[target_degree]) for chain in basis_chains
    ])
    assert np.array_equal(
        basis.T @ basis,
        (4 ** qubits) * np.eye(2 ** qubits, dtype=np.int64),
    )
    assert not np.any(boundaries[target_degree] @ basis)
    amplitudes_array = np.array(amplitudes, dtype=np.int64)
    phi = basis @ amplitudes_array
    survivor_matrix = basis @ np.array(survivors, dtype=np.int64)
    upper_boundary = boundaries[target_degree + 1]
    augmented, pivots = echelon_mod_prime(
        upper_boundary, PRIME, np.column_stack((phi, survivor_matrix))
    )
    upper_columns = upper_boundary.shape[1]
    assert not np.any(augmented[len(pivots):, upper_columns])
    survivor_increment = len(echelon_mod_prime(
        augmented[len(pivots):, upper_columns + 1:], PRIME
    )[1])
    assert survivor_increment == 2 ** qubits - 1
    denominator, filling = solve_filling(upper_boundary, phi, PRIME)

    betti = {
        str(k): len(cells[k]) - ranks.get(k, 0) - ranks.get(k + 1, 0)
        for k in cells
    }
    assert betti[str(target_degree)] == 2 ** qubits - 1

    register = {
        f"{qubit}.{name}" for qubit in range(qubits) for name in VERTEX_NAMES
    }
    private = graph.vertices - register
    weights0 = {v: int(v in register) for v in graph.vertices}
    weights1 = {v: int(v in private) for v in graph.vertices}
    down0 = weighted_boundary(cells, target_degree, weights0)
    up0 = weighted_boundary(cells, target_degree + 1, weights0)
    down1 = weighted_boundary(cells, target_degree, weights1)
    up1 = weighted_boundary(cells, target_degree + 1, weights1)
    pair0 = np.vstack((down0, up0.T))
    pair1 = np.vstack((down1, up1.T))
    bulk_indices = [
        i for i, simplex in enumerate(cells[target_degree]) if "v0" in simplex
    ]
    assert bulk_indices
    assert not np.any(pair0 @ basis)
    assert not np.any(pair0[:, bulk_indices])
    rank0 = len(echelon_mod_prime(pair0, PRIME)[1])
    known_kernel = len(basis_chains) + len(bulk_indices)
    assert rank0 == len(cells[target_degree]) - known_kernel

    low_rows = [
        i for i, simplex in enumerate(cells[target_degree - 1]) if "v0" in simplex
    ]
    high_rows = [
        i for i, simplex in enumerate(cells[target_degree + 1]) if "v0" in simplex
    ]
    t0 = np.vstack((down0[low_rows, :], up0.T[high_rows, :]))
    t1 = np.vstack((down1[low_rows, :], up1.T[high_rows, :]))
    assert not np.any(t0)
    assert not np.any(t1 @ basis)
    bulk_pair = t1[:, bulk_indices]
    gram = bulk_pair.T @ bulk_pair
    determinant, gram_rank = det_mod_prime(gram, PRIME)
    assert determinant and gram_rank == len(bulk_indices)

    neighbors = {
        b if a == "v0" else a
        for a, b in graph.pairs if "v0" in (a, b)
    }
    assert neighbors and neighbors <= private
    zero_gram = pair0.T @ pair0
    derivative_gram = pair1.T @ pair1
    unweighted_gram = (
        boundaries[target_degree].T @ boundaries[target_degree]
        + boundaries[target_degree + 1] @ boundaries[target_degree + 1].T
    )
    inf_norm = lambda a: int(np.abs(a).sum(axis=1).max()) if len(a) else 0
    gram_bound = inf_norm(gram)
    assert gram_bound >= 1
    filling_terms = [
        {"simplex": list(cells[target_degree + 1][i]), "coefficient": int(c)}
        for i, c in enumerate(filling) if c
    ]
    graph_edges = [list(edge) for edge in sorted(graph.pairs)]
    return {
        "status": "PASS",
        "state_function": state,
        "projector": {
            "qubits": qubits,
            "basis_order": [format(i, f"0{qubits}b") for i in range(2 ** qubits)],
            "integer_amplitudes": amplitudes,
            "logical_basis_gram": f"{4 ** qubits} I_{2 ** qubits}",
        },
        "graph": {
            "vertices": sorted(graph.vertices),
            "edges": graph_edges,
            "edge_sha256": hashlib.sha256(
                json.dumps(graph_edges, separators=(",", ":")).encode()
            ).hexdigest(),
            "simplex_counts": {str(k): len(v) for k, v in sorted(cells.items())},
            "maximum_dimension": max(cells),
        },
        "topology_certificate": {
            "target_degree": target_degree,
            "ordinary_betti_over_Q": betti,
            "boundary_ranks": rank_bounds,
            "exact_filling_denominator": denominator,
            "exact_filling_chain": filling_terms,
            "filling_equation_verified_over_integers": True,
            "complementary_register_cycles_independent_mod_boundaries":
                survivor_increment,
            "register_intersection":
                "Exactly the intended rank-one line: explicit filling plus "
                "2^n-1 independent complementary register cycles.",
        },
        "zero_weight_certificate": {
            "register_vertices": sorted(register),
            "register_cycle_dimension": len(basis_chains),
            "central_bulk_dimension": len(bulk_indices),
            "differential_pair_rank_mod_prime": rank0,
            "rational_rank_upper_bound_from_known_kernel":
                len(cells[target_degree]) - known_kernel,
            "kernel_exactly_register_cycles_plus_central_bulk": True,
            "projected_bulk_pair_zero_constant_term": True,
            "projected_bulk_pair_annihilates_register_cycles": True,
            "central_vertex_has_only_new_neighbors": True,
            "bulk_gram_prime": PRIME,
            "bulk_gram_determinant_mod_prime": determinant,
            "bulk_gram_infinity_norm": gram_bound,
            "rational_lower_bound_for_unscaled_pair_singular_value": {
                "numerator": 1, "denominator": str(pow(gram_bound, len(bulk_indices)))
            },
            "zero_weight_gram_infinity_norm": inf_norm(zero_gram),
            "derivative_gram_infinity_norm": inf_norm(derivative_gram),
            "unweighted_gram_infinity_norm": inf_norm(unweighted_gram),
            "weighted_gap_exponent": 2 * target_degree + 4,
        },
    }


def map_second_qubit(vertex):
    swaps = {f"1.{a}{i}": f"1.{b}{i}" for a, b in (("a", "b"), ("b", "a"))
             for i in (2, 3, 4)}
    for old, new in swaps.items():
        if vertex == old or vertex.startswith(old + "."):
            return new + vertex[len(old):]
    return vertex


def map_chain(chain, permutation):
    result = Counter()
    for simplex, coefficient in chain.items():
        mapped, sign = oriented(tuple(permutation(v) for v in simplex))
        result[mapped] += sign * coefficient
    return clean(result)


def check_two_term_transport(source, target, certificate):
    mapped_vertices = {map_second_qubit(v) for v in source.vertices}
    mapped_edges = {
        tuple(sorted((map_second_qubit(a), map_second_qubit(b))))
        for a, b in source.pairs
    }
    assert mapped_vertices == target.vertices and mapped_edges == target.pairs
    target_cells = all_cliques(target)
    source_basis = logical_basis(2)
    source_phi = Counter()
    for j, amplitude in enumerate([1, 0, 0, -1]):
        for simplex, coefficient in source_basis[j].items():
            source_phi[simplex] += amplitude * coefficient
    mapped_phi = map_chain(clean(source_phi), map_second_qubit)
    target_basis = logical_basis(2)
    expected = Counter()
    for j, amplitude in enumerate([0, 1, -1, 0]):
        for simplex, coefficient in target_basis[j].items():
            expected[simplex] += amplitude * coefficient
    assert mapped_phi == clean(expected)
    filling = {
        tuple(item["simplex"]): item["coefficient"]
        for item in certificate["topology_certificate"]["exact_filling_chain"]
    }
    transported = map_chain(filling, map_second_qubit)
    assert all(s in set(target_cells[4]) for s in transported)
    assert chain_boundary(transported) == clean(expected)
    return {
        "status": "PASS",
        "state_function": "state_01m10",
        "projector": {
            "qubits": 2, "basis_order": ["00", "01", "10", "11"],
            "integer_amplitudes": [0, 1, -1, 0],
            "source_relation": "Logical X on the second bowtie maps |00>-|11> "
                               "to |01>-|10>.",
        },
        "graph": {
            "vertices": sorted(target.vertices),
            "edges": [list(e) for e in sorted(target.pairs)],
            "simplex_counts": {
                str(k): len(v) for k, v in sorted(target_cells.items())
            },
            "maximum_dimension": max(target_cells),
        },
        "transport_certificate": {
            "weight_preserving_graph_isomorphism": True,
            "all_private_vertices_mapped": True,
            "all_cliques_transport_bijectively": True,
            "exact_integer_filling_transport": True,
            "transported_filling_terms": len(transported),
            "zero_weight_kernel_and_bulk_pair":
                "Transported by signed permutation chain isometries in every degree.",
            "same_constants_as": "state_00m11",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--certificate", type=Path,
                        default=FOLDER / "REMAINING_ACTIVE_ATOM_CERTIFICATES.json")
    args = parser.parse_args()
    state_names = ["state_0m1", "state_00m11", "state_01m10"]
    archived = None
    if args.offline:
        archived = json.loads(args.certificate.read_text())
        assert archived["source"]["commit"] == SOURCE_COMMIT
        assert archived["source"]["sha256"] == SOURCE_SHA256
        graphs = {}
        for name in state_names:
            item = archived["atoms"][name]
            graph = Graph(item["graph"]["edges"])
            graph.vertices = set(item["graph"]["vertices"])
            graphs[name] = graph
        replayed = False
    else:
        upstream = subprocess.check_output([
            "gh", "api",
            "repos/DorianRudolph/QMA1-gateset-paper/contents/"
            + SOURCE_PATH + "?ref=" + SOURCE_COMMIT,
            "-H", "Accept: application/vnd.github.raw+json",
        ])
        graphs = recover_graphs(upstream, state_names)
        replayed = True

    one = certify_atom(
        graphs["state_0m1"], "state_0m1", 1, 1,
        [1, -1], [[1], [1]],
    )
    two = certify_atom(
        graphs["state_00m11"], "state_00m11", 2, 3,
        [1, 0, 0, -1],
        [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0]],
    )
    other = check_two_term_transport(
        graphs["state_00m11"], graphs["state_01m10"], two
    )
    atoms = {"state_0m1": one, "state_00m11": two, "state_01m10": other}
    output = {
        "status": "PASS",
        "scope": "Exact topology, filling, zero-weight kernel and projected "
                 "central-bulk data for the remaining one-/two-term source atoms.",
        "source": {
            "url": SOURCE_URL, "commit": SOURCE_COMMIT, "sha256": SOURCE_SHA256,
            "upstream_license": "GPLv2-or-later",
            "upstream_replayed_this_run": replayed,
            "execution": "Only inspected graph-building AST definitions; capture "
                         "occurred at the first clique_complex call before Sage.",
        },
        "atoms": atoms,
        "consequence": {
            "base_atom_types_under_finite_criterion": [
                "|0>-|1>", "|00>-|11>", "|01>-|10>",
                "four Hadamard three-term atoms by the separate orbit certificate",
                "basis atoms by the separate cone certificate",
            ],
            "guard_closure": "Conditional on the separately reviewed selected-cycle lemma.",
            "safe_total_locality": 6,
            "safe_weighted_gap_exponent": 26,
        },
        "not_certified": [
            "Source priority or full-paper novelty",
            "Unrestricted complexity-class equivalence",
            "Optimal spectral valuation or practical performance",
            "Complete end-to-end reduction integration",
        ],
    }
    if args.offline:
        for name in state_names:
            assert atoms[name] == archived["atoms"][name]
        target = FOLDER / "OFFLINE_REMAINING_ACTIVE_ATOM_CHECKS.json"
        target.write_text(json.dumps({
            "status": "PASS",
            "input_certificate": str(args.certificate.name),
            "upstream_replayed_this_run": False,
            "all_three_atom_sections_recomputed_exactly": True,
            "source_provenance_not_rechecked_offline": True,
        }, indent=2) + "\n")
    else:
        target = args.certificate
        target.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({
        "status": "PASS", "offline": args.offline,
        "atoms": {
            name: {
                "vertices": len(item["graph"]["vertices"]),
                "simplex_counts": item["graph"]["simplex_counts"],
                "target_degree": item.get("topology_certificate", {}).get(
                    "target_degree", two["topology_certificate"]["target_degree"]
                ),
                "central_bulk_dimension": item.get(
                    "zero_weight_certificate", {}).get("central_bulk_dimension",
                                                       "transported"),
                "filling_terms": len(item.get(
                    "topology_certificate", {}).get("exact_filling_chain", []))
                    or item.get("transport_certificate", {}).get(
                        "transported_filling_terms"),
            } for name, item in atoms.items()
        },
        "output": str(target),
    }, indent=2))


if __name__ == "__main__":
    main()
