"""Finite checks of exact-filling coercivity and an angle-bound guard.

Uses actual weighted clique boundary matrices for small cone attachments.
These graphs are NOT the King--Kohler/Rudolph palette, and this calculation
does not certify the all-chain theorem or a spectral asymptotic.
"""

from pathlib import Path
import importlib.util
import itertools
import json

import numpy as np
from scipy.linalg import eigh

support_path = Path(__file__).resolve().parent / "check_kernel_filtration.py"
spec = importlib.util.spec_from_file_location("kernel_fixture_support", support_path)
support = importlib.util.module_from_spec(spec)
spec.loader.exec_module(support)

CYCLES = ((0, 1, 2, 3), (0, 4, 5, 6))


def make_complex(attachments):
    edges = set(support.bouquet(0))
    vertices = set(range(7))
    for vertex, target in attachments:
        vertices.add(vertex)
        edges.update(support.edge(vertex, v) for v in CYCLES[target])
    return {
        degree: [
            simplex for simplex in itertools.combinations(sorted(vertices), degree + 1)
            if all(support.edge(a, b) in edges
                   for a, b in itertools.combinations(simplex, 2))
        ]
        for degree in (0, 1, 2)
    }


def embed(source, target):
    target_rows = {simplex: i for i, simplex in enumerate(target[1])}
    matrix = np.zeros((len(target[1]), len(source[1])))
    for j, simplex in enumerate(source[1]):
        matrix[target_rows[simplex], j] = 1
    return matrix


def cycle_vector(simplices, which):
    rows = {simplex: i for i, simplex in enumerate(simplices[1])}
    vector = np.zeros(len(rows))
    cycle = CYCLES[which]
    for i in range(4):
        a, b = cycle[i], cycle[(i + 1) % 4]
        vector[rows[support.edge(a, b)]] = (1 if a < b else -1) / 2
    return vector


def matrices(simplices, weights):
    down = support.boundary(simplices, 1, weights)
    boundary_up = support.boundary(simplices, 2, weights)
    assert np.linalg.norm(down @ boundary_up) < 1e-12
    up = boundary_up @ boundary_up.T
    lap = down.T @ down + up
    values, vectors = eigh(lap)
    assert values[0] > -1e-9
    positive = values[values > 1e-8]
    harmonic = vectors[:, np.abs(values) < 1e-8]
    return boundary_up, up, lap, positive[0], harmonic


def check_cliques():
    records = []
    register = make_complex([])
    for targets in ((0,), (0, 0), (0, 1), (0, 0, 1), (0, 1, 0, 1)):
        attachments = [(7 + i, target) for i, target in enumerate(targets)]
        global_complex = make_complex(attachments)
        for lam in (0.5, 0.25, 0.125):
            weights = [1.0] * 7 + [lam] * len(targets)
            _, global_up, _, global_gap, harmonics = matrices(global_complex, weights)
            assert harmonics.shape[1] == 2 - len(set(targets))
            aggregate_up = np.zeros_like(global_up)
            logical = np.zeros_like(global_up)
            local_gaps, filling_residuals = [], []
            for attachment in attachments:
                local = make_complex([attachment])
                boundary_up, up, _, gap, _ = matrices(local, weights)
                inclusion = embed(local, global_complex)
                aggregate_up += inclusion @ up @ inclusion.T
                phi_local = cycle_vector(local, attachment[1])
                filling = np.linalg.lstsq(boundary_up, phi_local, rcond=None)[0]
                residual = np.linalg.norm(boundary_up @ filling - phi_local)
                assert residual < 1e-9
                filling_residuals.append(float(residual))
                phi_global = cycle_vector(global_complex, attachment[1])
                logical += np.outer(phi_global, phi_global)
                local_gaps.append(float(gap))
            additivity_error = np.linalg.norm(global_up - aggregate_up)
            assert additivity_error < 1e-10
            # Use half the numerically resolved local gap to keep a margin.
            delta = min(local_gaps) / 2
            minimum = float(eigh(global_up - delta * logical, eigvals_only=True)[0])
            assert minimum > -1e-9
            annihilation_error = float(np.linalg.norm(logical @ harmonics))
            assert annihilation_error < 1e-8
            records.append({
                "targets": list(targets), "lambda": lam,
                "betti_1": harmonics.shape[1], "delta_for_psd_check": delta,
                "psd_residual_min_eigenvalue": minimum,
                "up_additivity_error": float(additivity_error),
                "max_filling_residual": max(filling_residuals),
                "logical_harmonic_annihilation_error": annihilation_error,
                "measured_global_positive_gap": float(global_gap),
            })
    assert len(records) == 15
    return records


def check_missing_hypotheses():
    missing_filling_min = float(np.linalg.eigvalsh(
        np.diag([1.0, 0.0]) - np.diag([0.0, 1.0])
    )[0])
    assert missing_filling_min == -1.0

    eta = 0.8
    common = np.ones((2, 2)) / 2
    qa = np.diag([1.0, 0.0])
    v = np.array([1.0, 99.0])
    qb = np.outer(v, v) / np.dot(v, v)
    actual_errors = [
        float(np.linalg.norm(qa - common, 2)),
        float(np.linalg.norm(qb - common, 2)),
    ]
    assert max(actual_errors) <= eta
    signed_lower = 1 - 2 * eta * eta
    overlap = float(np.trace(qa @ qb))
    assert 0 < overlap < signed_lower * signed_lower
    return {
        "missing_exact_filling": {
            "minimum_eigenvalue": missing_filling_min,
            "meaning": "Direct logical domination fails without boundary containment.",
        },
        "negative_angle_bound_cannot_be_squared": {
            "eta_bound": eta, "actual_projector_errors": actual_errors,
            "signed_singular_value_lower_bound": signed_lower,
            "invalid_squared_lower_bound": signed_lower * signed_lower,
            "actual_overlap_with_rank_one_map": overlap,
            "repair": "Require a nonnegative angle bound, or use its positive part.",
        },
    }


def main():
    result = {
        "status": "PASS",
        "scope": "15 small clique fixtures and two hypothesis guards; not a palette certificate",
        "clique_cases": check_cliques(),
        "hypothesis_guards": check_missing_hypotheses(),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
