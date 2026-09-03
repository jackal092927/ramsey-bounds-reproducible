"""Finite check of the conditional persistent-Laplacian unweighting identity.

Run from the repository root:
python3 research/quantum_direction_selection/collaboration/2026-09-02/check_persistent_laplacian.py
This tests small matrices and the inherited-domain metric, not priority or a
general imported spectral theorem.
"""
from pathlib import Path
import importlib.util
import json
from math import sqrt

import numpy as np
from scipy.linalg import null_space

SPEC = importlib.util.spec_from_file_location(
    "common_blowup_fixture",
    Path(__file__).resolve().parents[2] / "tda_probe" / "check_common_blowup.py",
)
fixture_module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(fixture_module)


def boundary(complex_, degree, weights):
    if degree == 0:
        return np.zeros((0, len(complex_[0])))
    return fixture_module.coboundary(
        complex_[degree - 1], complex_[degree], weights
    ).T


def persistent_laplacian(initial, later, degree, weights):
    b_later = boundary(later, degree + 1, weights)
    inc = fixture_module.inclusion(initial[degree], later[degree])
    initial_faces = set(initial[degree])
    outside = [i for i, s in enumerate(later[degree]) if s not in initial_faces]
    restricted = b_later[outside, :]
    # Orthonormal coordinates for the domain's inherited inner product.
    domain = (
        null_space(restricted, rcond=1e-12)
        if outside else np.eye(b_later.shape[1])
    )
    b_persistent = inc.T @ b_later @ domain
    down = boundary(initial, degree, weights)
    delta = b_persistent @ b_persistent.T + down.T @ down
    z_initial = null_space(down, rcond=1e-12)
    rank = lambda a: int(np.linalg.matrix_rank(a, tol=1e-9)) if a.size else 0
    persistent_rank = rank(np.column_stack((inc @ z_initial, b_later))) - rank(b_later)
    nullity = int(np.sum(np.linalg.eigvalsh(delta) < 1e-9))
    assert nullity == persistent_rank
    return delta, {
        "domain_dimension": int(domain.shape[1]),
        "outside_rows": len(outside),
        "nullity": nullity,
        "independent_persistent_rank": persistent_rank,
        "domain_constraint_residual": float(np.linalg.norm(restricted @ domain)),
    }


def main():
    f, scale = (2, 1, 2, 1), 4
    weights = {v: sqrt(f[v] / scale) for v in range(len(f))}
    cycle = {(0, 1), (1, 2), (2, 3), (0, 3)}
    filled = cycle | {(0, 2)}
    levels = [fixture_module.fixture(edges, f) for edges in (cycle, filled)]
    records = []
    for initial_index, later_index in ((0, 0), (0, 1), (1, 1)):
        initial, blown_initial, lifts = levels[initial_index]
        later, blown_later, _ = levels[later_index]
        blown_weights = {v: 1.0 for (v,) in blown_later[0]}
        for degree in (0, 1):
            delta, base_info = persistent_laplacian(initial, later, degree, weights)
            delta_hat, blown_info = persistent_laplacian(
                blown_initial, blown_later, degree, blown_weights
            )
            ordinary_hat, _ = persistent_laplacian(
                blown_initial, blown_initial, degree, blown_weights
            )
            lift = lifts[degree]
            asym = null_space(lift.T, rcond=1e-12)
            intertwining_error = float(np.linalg.norm(
                delta_hat @ lift - scale * lift @ delta
            ))
            mixing_error = float(np.linalg.norm(lift.T @ delta_hat @ asym))
            asym_min = (
                float(np.linalg.eigvalsh(asym.T @ delta_hat @ asym).min())
                if asym.shape[1] else None
            )
            domination_min = float(np.linalg.eigvalsh(delta_hat - ordinary_hat).min())
            assert intertwining_error < 1e-9
            assert mixing_error < 1e-9
            assert domination_min > -1e-9
            assert asym_min is None or asym_min >= min(f) - 1e-9
            assert base_info["nullity"] == blown_info["nullity"]
            records.append({
                "pair": [initial_index, later_index],
                "degree": degree,
                "base": base_info,
                "blown_up": blown_info,
                "symmetric_intertwining_residual": intertwining_error,
                "cross_sector_residual": mixing_error,
                "asymmetric_min_eigenvalue": asym_min,
                "claimed_asymmetric_lower_bound": min(f),
                "persistent_minus_initial_min_eigenvalue": domination_min,
            })
    nontrivial = next(r for r in records if r["pair"] == [0, 1] and r["degree"] == 1)
    assert nontrivial["base"]["outside_rows"] == 1
    assert nontrivial["base"]["domain_dimension"] == 1
    assert nontrivial["base"]["nullity"] == 0
    before = next(r for r in records if r["pair"] == [0, 0] and r["degree"] == 1)
    assert before["base"]["nullity"] == 1
    print(json.dumps({
        "status": "PASS",
        "kind": "finite floating-point persistent-domain and sector check",
        "fixture": "four-cycle filled through a later diagonal and two triangles",
        "base_vertices": 4,
        "blown_up_vertices": sum(f),
        "multiplicities": f,
        "laplacian_scale": scale,
        "checks": records,
    }, indent=2))


if __name__ == "__main__":
    main()
