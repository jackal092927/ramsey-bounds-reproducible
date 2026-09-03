"""Transport the certified three-term gadget to all four split-Hadamard atoms.

This uses only archived graph data. New graphs are register relabelings of the
certified source graph. Integer chain maps verify the logical action and each
transported filling; spectral and zero-weight data transfer by chain isometry.
"""

from collections import defaultdict
from pathlib import Path
import hashlib
import json

import numpy as np

from certify_representative_bulk import Graph, all_cliques, boundary, register_basis

INPUT_SHA256 = "916819fb8a9e371b322a1fab1161b1fc2686ad7fdaf9cf785f52fc2fcb0cae3a"


def image_simplex(simplex, permutation):
    image = tuple(permutation[v] for v in simplex)
    inversions = sum(image[i] > image[j]
                     for i in range(len(image)) for j in range(i + 1, len(image)))
    return tuple(sorted(image)), (-1) ** inversions


def generator(vertices, operation):
    qubit = 0 if operation[-1] == "c" else 1
    permutation = {v: v for v in vertices}
    if operation[0] == "X":
        for label in ("2", "3", "4"):
            a, b = f"{qubit}.a{label}", f"{qubit}.b{label}"
            permutation[a], permutation[b] = b, a
    else:
        assert operation[0] == "Z"
        a, b = f"{qubit}.b3", f"{qubit}.b4"
        permutation[a], permutation[b] = b, a
    return permutation


def main():
    folder = Path(__file__).resolve().parent
    payload = (folder / "RUDOLPH_REPRESENTATIVE_BULK_CERTIFICATE.json").read_bytes()
    assert hashlib.sha256(payload).hexdigest() == INPUT_SHA256
    source = json.loads(payload)
    graph = Graph(source["graph"]["edges"])
    graph.vertices = set(source["graph"]["vertices"])
    cells = all_cliques(graph)
    basis = register_basis(cells)
    assert np.array_equal(basis.T @ basis, 16 * np.eye(4, dtype=np.int64))
    register = set(source["zero_weight_certificate"]["register_vertices"])
    register_edges = {e for e in graph.pairs if set(e) <= register}
    base_phi = np.array([1, 0, -1, -1], dtype=np.int64)
    i2 = np.eye(2, dtype=np.int64)
    x2 = np.array([[0, 1], [1, 0]], dtype=np.int64)
    z2 = np.diag([1, -1])
    logical_generators = {
        "Xc": np.kron(x2, i2), "Zc": np.kron(z2, i2),
        "Xw": np.kron(i2, x2), "Zw": np.kron(i2, z2),
    }
    # Vertex operations are listed in the order in which they are applied.
    cases = [
        ("d0", [], 1, [1, 0, -1, -1]),
        ("d1", ["Xw", "Zw", "Zc"], -1, [0, 1, -1, 1]),
        ("u0", ["Xc"], -1, [1, 1, -1, 0]),
        ("u1", ["Xw", "Zw", "Zc", "Xc"], 1, [1, -1, 0, -1]),
    ]
    records = []
    for name, operations, phase, amplitudes in cases:
        permutation = {v: v for v in graph.vertices}
        expected_action = np.eye(4, dtype=np.int64)
        for operation in operations:
            step = generator(graph.vertices, operation)
            permutation = {v: step[permutation[v]] for v in graph.vertices}
            expected_action = logical_generators[operation] @ expected_action
        assert set(permutation.values()) == graph.vertices
        assert all(permutation[v] == v for v in graph.vertices - register)
        changed_graph = Graph([
            (permutation[a], permutation[b]) for a, b in graph.pairs
        ])
        changed_graph.vertices = set(graph.vertices)
        assert {e for e in changed_graph.pairs if set(e) <= register} == register_edges
        changed_cells = all_cliques(changed_graph)
        for degree, simplices in cells.items():
            mapped = {image_simplex(s, permutation)[0] for s in simplices}
            assert mapped == set(changed_cells[degree])
        target_rows = {s: j for j, s in enumerate(changed_cells[3])}
        mapped_basis = np.zeros_like(basis)
        for i, simplex in enumerate(cells[3]):
            target, sign = image_simplex(simplex, permutation)
            mapped_basis[target_rows[target]] = sign * basis[i]
        changed_basis = register_basis(changed_cells)
        numerator = changed_basis.T @ mapped_basis
        assert not np.any(numerator % 16)
        action = numerator // 16
        assert np.array_equal(action, expected_action)
        assert np.array_equal(mapped_basis, changed_basis @ action)
        assert np.array_equal(action.T @ action, np.eye(4, dtype=np.int64))
        target_amplitudes = np.array(amplitudes, dtype=np.int64)
        assert np.array_equal(action @ base_phi, phase * target_amplitudes)
        filling = defaultdict(int)
        for term in source["topology_certificate"]["exact_filling_chain"]:
            image, sign = image_simplex(tuple(term["simplex"]), permutation)
            filling[image] += phase * sign * term["coefficient"]
        coeffs = np.array([filling.get(s, 0) for s in changed_cells[4]], dtype=np.int64)
        assert np.array_equal(boundary(changed_cells, 4) @ coeffs,
                              changed_basis @ target_amplitudes)
        records.append({
            "atom": name,
            "normalized_logical_amplitudes": {
                "numerators_in_order_00_01_10_11": amplitudes,
                "common_denominator": "sqrt(3)",
            },
            "applied_vertex_operations_in_order": operations,
            "changed_register_vertices": {
                v: permutation[v] for v in sorted(permutation) if permutation[v] != v
            },
            "logical_action": action.tolist(),
            "image_of_d0_equals_phase_times_target": phase,
            "all_cliques_transport_bijectively": True,
            "register_graph_preserved": True,
            "private_vertices_fixed": True,
            "integer_filling_equation_verified": True,
            "transported_filling_nonzeros": int(np.count_nonzero(coeffs)),
            "graph_edges_sha256": hashlib.sha256(
                json.dumps(sorted(changed_graph.pairs), separators=(",", ":")).encode()
            ).hexdigest(),
        })
    output = {
        "status": "PASS",
        "input_certificate_sha256": INPUT_SHA256,
        "source_graph_commit": source["source"]["commit"],
        "basis_order": ["00", "01", "10", "11"],
        "all_four_split_hadamard_atoms_covered": True,
        "records": records,
        "transported_properties": [
            "Exact target boundary intersection and Betti multiplicity",
            "Zero-weight kernel equal to V direct-sum Q",
            "Projected central pair injectivity and annihilation on V",
            "All positive-weight spectra and uniform constants",
        ],
        "proof_mechanism": "Weight-preserving vertex relabeling induces signed permutation chain isometries in every degree, preserving the private/central subspaces.",
        "scope": "Only the unguarded active three-term atoms and their outside harmonic padding. Other atom types and guarded attaching-sphere products are not certified here.",
        "new_source_replay": False,
    }
    destination = folder / "ACTIVE_HADAMARD_ORBIT_CERTIFICATE.json"
    destination.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({
        "status": "PASS", "atoms": [r["atom"] for r in records],
        "integer_fillings_verified": len(records),
        "input_certificate_sha256": INPUT_SHA256, "file": destination.name,
        "scope": output["scope"],
    }, indent=2))


if __name__ == "__main__":
    main()

