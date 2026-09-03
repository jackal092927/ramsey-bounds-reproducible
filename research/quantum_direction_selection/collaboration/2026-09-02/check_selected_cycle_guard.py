"""Exact offline checks for the selected-cycle guard construction.

Uses the immutable archived source graph, never gh, network, or Sage.
It checks chain identities and transferred data; it does not recompute the
large guarded graph's rational rank or establish source priority.
"""
from collections import Counter
import hashlib
import itertools
import json
from pathlib import Path

import numpy as np
from certify_representative_bulk import (
    Graph, VERTEX_NAMES, all_cliques, boundary, weighted_boundary,
    echelon_mod_prime, register_basis,
)

FOLDER = Path(__file__).resolve().parent
SOURCE_CERTIFICATE_SHA = "916819fb8a9e371b322a1fab1161b1fc2686ad7fdaf9cf785f52fc2fcb0cae3a"


def clean(counter):
    return {key: int(value) for key, value in counter.items() if value}


def oriented(vertices):
    assert len(vertices) == len(set(vertices))
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


def chain_boundary(chain, weights):
    result = Counter()
    for simplex, coefficient in chain.items():
        for i, vertex in enumerate(simplex):
            result[simplex[:i] + simplex[i + 1:]] += (
                coefficient * (-1) ** i * weights[vertex]
            )
    return clean(result)


def bowtie(prefix):
    graph = Graph()
    cycles = []
    for bit in (0, 1):
        petal = "b" if bit else "a"
        walk = [prefix + "xx", prefix + petal + "3",
                prefix + petal + "2", prefix + petal + "4"]
        chain = Counter()
        for i in range(4):
            edge = (walk[i], walk[(i + 1) % 4])
            graph.add_edges([edge])
            canonical, sign = oriented(edge)
            chain[canonical] += sign
        cycles.append(clean(chain))
    return graph, cycles


def flat_cells(cells, augmented=True):
    answer = {simplex for level in cells.values() for simplex in level}
    if augmented:
        answer.add(())
    return answer


def attach_guard(base, register, bit=0):
    guard, guard_cycles = bowtie("zzguard.")
    selected = {v for edge in guard_cycles[bit] for v in edge}
    graph = base.union(guard)
    graph.add_edges(itertools.product(register, guard.vertices))
    graph.add_edges(itertools.product(base.vertices - register, selected))
    return graph, guard, guard_cycles, selected


def check_chain_decomposition(base, register, graph, guard, selected):
    base_cells = all_cliques(base)
    new_cells = all_cliques(graph)
    guard_cells = all_cliques(guard)
    base_flat = flat_cells(base_cells)
    new_flat = flat_cells(new_cells)
    guard_flat = flat_cells(guard_cells)
    selected_flat = {s for s in guard_flat if set(s) <= selected}
    register_flat = {s for s in base_flat if set(s) <= register}
    union = {tuple(sorted(a + b)) for a in base_flat for b in selected_flat}
    union |= {tuple(sorted(a + b)) for a in register_flat for b in guard_flat}
    assert union == new_flat
    private = base.vertices - register
    private_columns = [s for s in new_flat if set(s) & private]
    zero_weights = {v: int(v not in private) for v in graph.vertices}
    one_weights = {v: 1 for v in graph.vertices}
    checked = 0
    for simplex in private_columns:
        a = tuple(v for v in simplex if v in base.vertices)
        b = tuple(v for v in simplex if v in guard.vertices)
        _, input_sign = oriented(a + b)
        for weights in (zero_weights, one_weights):
            actual = {face: c for face, c in chain_boundary(
                {simplex: 1}, weights).items() if set(face) & private}
            first = {face: c for face, c in chain_boundary(
                {a: 1}, weights).items() if set(face) & private}
            expected = Counter(join_chain(first, {b: 1}))
            second = join_chain({a: 1}, chain_boundary({b: 1}, weights))
            for face, c in second.items():
                expected[face] += (-1) ** len(a) * c
            expected = {face: input_sign * c for face, c in clean(expected).items()}
            assert actual == expected
            if weights is zero_weights:
                assert chain_boundary({simplex: 1}, weights) == actual
            checked += 1
    return new_cells, {
        "clique_union_exact": True,
        "relative_and_zero_weight_tensor_boundary_checks": checked,
        "all_actual_degrees_checked": sorted(new_cells),
        "zero_weight_private_to_register_block_zero": True,
    }


def projected_pair(cells, degree, weights, guard_vertices, cycle, active_degree):
    """Unnormalized contraction against a guard cycle on central outputs."""
    result = Counter()

    def output_row(simplex, kind):
        a = tuple(v for v in simplex if v not in guard_vertices)
        b = tuple(v for v in simplex if v in guard_vertices)
        target_size = active_degree if kind == "down" else active_degree + 2
        if "v0" not in a or len(a) != target_size or b not in cycle:
            return None
        _, sign = oriented(a + b)
        return (kind, a), sign * cycle[b]

    for column in cells[degree]:
        for i, vertex in enumerate(column):
            face = column[:i] + column[i + 1:]
            match = output_row(face, "down")
            if match:
                row, coefficient = match
                result[(row, column)] += coefficient * (-1) ** i * weights[vertex]
    for upper in cells.get(degree + 1, []):
        match = output_row(upper, "up")
        if match:
            row, coefficient = match
            for i, vertex in enumerate(upper):
                column = upper[:i] + upper[i + 1:]
                result[(row, column)] += coefficient * (-1) ** i * weights[vertex]
    return clean(result)


def main():
    source_bytes = (FOLDER / "RUDOLPH_REPRESENTATIVE_BULK_CERTIFICATE.json").read_bytes()
    assert hashlib.sha256(source_bytes).hexdigest() == SOURCE_CERTIFICATE_SHA
    source = json.loads(source_bytes)
    base = Graph(source["graph"]["edges"])
    base.vertices = set(source["graph"]["vertices"])
    register = set(source["zero_weight_certificate"]["register_vertices"])
    private = base.vertices - register
    base_cells = all_cliques(base)
    graph, guard, cycles, selected = attach_guard(base, register)
    cells, tensor_checks = check_chain_decomposition(base, register, graph, guard, selected)
    d, degree = 3, 5
    weights0 = {v: int(v not in private) for v in graph.vertices}
    weights1 = {v: int(v in private) for v in graph.vertices}
    t0 = projected_pair(cells, degree, weights0, guard.vertices, cycles[0], d)
    t1 = projected_pair(cells, degree, weights1, guard.vertices, cycles[0], d)
    assert not t0

    old_t1 = projected_pair(
        base_cells, d, {v: int(v in private) for v in base.vertices},
        set(), {(): 1}, d,
    )
    bulk = {s for s in base_cells[d] if "v0" in s}
    assert len(bulk) == 176
    restricted_old = {key: c for key, c in old_t1.items() if key[1] in bulk}
    new_on_bulk = Counter()
    for (row, column), coefficient in t1.items():
        a = tuple(v for v in column if v in base.vertices)
        b = tuple(v for v in column if v in guard.vertices)
        if a in bulk and b in cycles[0]:
            _, sign = oriented(a + b)
            new_on_bulk[(row, a)] += coefficient * sign * cycles[0][b]
    # Gamma has norm 2: contraction and input each give this norm factor.
    assert clean(new_on_bulk) == {key: 4 * c for key, c in restricted_old.items()}

    basis = register_basis(base_cells)
    basis_chains = [
        {s: int(basis[i, j]) for i, s in enumerate(base_cells[d]) if basis[i, j]}
        for j in range(4)
    ]
    for active_cycle in basis_chains:
        for guard_cycle in cycles:
            logical = join_chain(active_cycle, guard_cycle)
            result = Counter()
            for (row, column), coefficient in t1.items():
                result[row] += coefficient * logical.get(column, 0)
            assert not clean(result)

    filling = {tuple(item["simplex"]): item["coefficient"]
               for item in source["topology_certificate"]["exact_filling_chain"]}
    phi = Counter()
    for j, coefficient in enumerate(source["projector"]["integer_amplitudes_00_01_10_11"]):
        for simplex, value in basis_chains[j].items():
            phi[simplex] += coefficient * value
    guarded_filling = join_chain(filling, cycles[0])
    guarded_phi = join_chain(clean(phi), cycles[0])
    assert all(s in set(cells[degree + 1]) for s in guarded_filling)
    assert chain_boundary(guarded_filling, {v: 1 for v in graph.vertices}) == guarded_phi

    sample_bulk = sorted(bulk)[0]
    sample_edge = sorted(cycles[0])[0]
    raw_coordinate = join_chain({sample_bulk: 1}, {sample_edge: 1})
    raw_down = chain_boundary(raw_coordinate, weights0)
    assert sum(c * c for c in raw_down.values()) == 2
    harmonic_bulk = join_chain({sample_bulk: 1}, cycles[0])
    assert not chain_boundary(harmonic_bulk, weights0)

    # A separate small exact rank certificate for the elementary basis cone.
    basis_register, basis_cycles = bowtie("base.")
    basis_graph = basis_register.union(Graph())
    basis_graph.add_edges(("v0", vertex) for edge in basis_cycles[0] for vertex in edge)
    basis_cells = all_cliques(basis_graph)
    b1, b2 = boundary(basis_cells, 1), boundary(basis_cells, 2)
    p = 1000003
    rank1 = len(echelon_mod_prime(b1, p)[1])
    rank2 = len(echelon_mod_prime(b2, p)[1])
    zero = {v: int(v != "v0") for v in basis_graph.vertices}
    pair0 = np.vstack((weighted_boundary(basis_cells, 1, zero),
                       weighted_boundary(basis_cells, 2, zero).T))
    rank0 = len(echelon_mod_prime(pair0, p)[1])
    rows = {s: i for i, s in enumerate(basis_cells[1])}
    z = np.zeros((len(rows), 2), dtype=np.int64)
    for j, cycle in enumerate(basis_cycles):
        for simplex, coefficient in cycle.items():
            z[rows[simplex], j] = coefficient
    assert not np.any(pair0 @ z)
    assert rank0 == len(rows) - 2 == 10
    assert rank1 == len(basis_cells[0]) - 1 == 7
    assert rank2 == len(basis_cells[2]) == 4
    assert len(rows) - rank1 - rank2 == 1
    cone_filling = join_chain({("v0",): 1}, basis_cycles[0])
    assert chain_boundary(cone_filling, {v: 1 for v in basis_graph.vertices}) == basis_cycles[0]
    survivors = np.array([basis_cycles[1].get(s, 0) for s in basis_cells[1]])
    assert len(echelon_mod_prime(np.column_stack((b2, survivors)), p)[1]) == rank2 + 1

    output = {
        "status": "PASS",
        "scope": "Exact chain identities for one selected guard on the source Hadamard atom, plus an elementary basis atom. Guarded ranks are transported by the structural proof, not recomputed numerically.",
        "upstream_replayed_this_run": False,
        "input_certificate_sha256": SOURCE_CERTIFICATE_SHA,
        "guarded_graph": {
            "vertices": sorted(graph.vertices), "edges": [list(e) for e in sorted(graph.pairs)],
            "simplex_counts": {str(k): len(v) for k, v in sorted(cells.items())},
            "target_degree": degree, "maximum_degree": max(cells),
            "edge_sha256": hashlib.sha256(json.dumps(sorted(graph.pairs), separators=(",", ":")).encode()).hexdigest(),
        },
        "exact_checks": {
            **tensor_checks,
            "projected_T0_zero_on_entire_target_domain": True,
            "projected_T1_annihilates_all_eight_register_cycles": True,
            "normalized_bulk_pair_identical_to_old_pair": True,
            "bulk_dimension_transferred": len(bulk),
            "guarded_filling_terms": len(guarded_filling),
            "guarded_cycle_terms": len(guarded_phi),
            "filling_equation_exact": True,
            "raw_coordinate_zero_weight_down_energy": 2,
            "selected_harmonic_factor_cancels_weight_one_differential": True,
        },
        "filling_recipe": {
            "old_chain": "topology_certificate.exact_filling_chain in the input certificate",
            "operation": "oriented join with the integer guard cycle; all coefficients remain integers",
            "guard_cycle": [{"edge": list(e), "coefficient": c} for e, c in sorted(cycles[0].items())],
        },
        "basis_cone": {
            "simplex_counts": {str(k): len(v) for k, v in sorted(basis_cells.items())},
            "prime": p, "rank_boundary1": rank1, "rank_boundary2": rank2,
            "target_betti_over_Q": 1, "zero_pair_rank": rank0,
            "known_zero_kernel_dimension": 2, "Q_dimension": 0,
            "rank_upper_bounds": "rank boundary1<=vertices-1; rank boundary2<=columns; rank D0<=target_dimension-2 from the two exact register cycles. Modular lower bounds meet these.",
            "unfilled_petal_independent_mod_boundaries": True,
            "integer_cone_filling_terms": len(cone_filling),
        },
        "not_certified": [
            "External review of the general guard lemma",
            "One-qubit difference and two-qubit two-term active atoms",
            "Complete palette integration, source priority, or source-class hardness",
            "Independent rerun of upstream code in this offline check",
        ],
    }
    target = FOLDER / "SELECTED_CYCLE_GUARD_CHECKS.json"
    target.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({"status": output["status"], "exact_checks": output["exact_checks"],
                      "basis_cone": output["basis_cone"],
                      "guarded_simplex_counts": output["guarded_graph"]["simplex_counts"],
                      "output": str(target)}, indent=2))


if __name__ == "__main__":
    main()
