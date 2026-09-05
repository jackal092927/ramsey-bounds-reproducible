"""Classical matrix test of a rational three-term history construction.

Tests valid-clock sectors for two small circuits, not the full clique gadgets
and not a quantum-computer speedup. Deterministic; NumPy/SciPy only.
"""

import json

import numpy as np
from scipy.linalg import eigh


def check_zero_final_kernel():
    """A reproducible valid-clock test with no surviving final history."""
    identity = np.eye(4)
    k = np.array([[1, 1], [1, -1]], dtype=float)
    first = np.zeros((12, 12))
    for left, right, time in ((np.kron(k, np.eye(2)), -identity, 0),
                              (identity, -np.kron(np.eye(2), k), 1)):
        rows = np.zeros((4, 12))
        rows[:, 4 * time:4 * (time + 1)] = left / np.sqrt(3)
        rows[:, 4 * (time + 1):4 * (time + 2)] = right / np.sqrt(3)
        assert np.linalg.norm(rows @ rows.T - identity) < 1e-12
        first += rows.T @ rows
    second = first.copy()
    second[-4:, -4:] += identity
    eigen1 = np.linalg.eigvalsh(first)
    eigen2 = np.linalg.eigvalsh(second)
    assert np.count_nonzero(np.abs(eigen1) < 1e-10) == 4
    assert eigen2[0] >= 1 / (120 * 3 ** 3)
    return {"kernel_dimensions": [4, 0],
            "minimum_final_eigenvalue": float(eigen2[0]),
            "claimed_lower_bound": 1 / (120 * 3 ** 3)}


def main():
    identity = np.eye(8)
    h = np.array([[1, 1], [1, -1]], dtype=float) / np.sqrt(2)
    h1 = np.kron(np.eye(2), np.kron(h, np.eye(2)))
    h2 = np.kron(np.eye(4), h)
    ccx = np.zeros((8, 8))
    x0 = np.zeros((8, 8))
    for z in range(8):
        ccx[z ^ (4 if (z & 3) == 3 else 0), z] = 1
        x0[z ^ 4, z] = 1
    initial = identity[:, :4]  # Clean most-significant work qubit is zero.
    reject = np.diag([1.0] * 4 + [0.0] * 4)
    invalid = identity - reject
    results = []
    for invert_output in (False, True):
        transitions = [(np.sqrt(2) * h1, "up"),
                       (h2 / np.sqrt(2), "down"), (ccx, "unitary")]
        if invert_output:
            transitions.append((x0, "unitary"))
        length = len(transitions) + 1
        first = np.zeros((8 * length, 8 * length))
        first[:8, :8] += invalid
        prefixes = [identity]
        scales_squared = [1]
        for t, (a, kind) in enumerate(transitions, start=1):
            b = np.zeros((8, 8 * length))
            if kind == "up":
                b[:, 8 * (t - 1):8 * t] = a / np.sqrt(3)
                b[:, 8 * t:8 * (t + 1)] = -identity / np.sqrt(3)
            elif kind == "down":
                b[:, 8 * (t - 1):8 * t] = identity / np.sqrt(3)
                b[:, 8 * t:8 * (t + 1)] = -np.linalg.inv(a) / np.sqrt(3)
            else:
                b[:, 8 * (t - 1):8 * t] = a / np.sqrt(2)
                b[:, 8 * t:8 * (t + 1)] = -identity / np.sqrt(2)
            assert np.linalg.norm(b @ b.T - identity) < 1e-12
            first += b.T @ b
            prefixes.append(a @ prefixes[-1])
            scales_squared.append(2 if kind == "up" else 1)
        normalization = sum(scales_squared)
        history = np.vstack([u @ initial for u in prefixes]) / np.sqrt(normalization)
        assert np.linalg.norm(history.T @ history - np.eye(4)) < 1e-12
        assert np.linalg.norm(first @ history) < 1e-12
        output_penalty = np.zeros_like(first)
        output_penalty[-8:, -8:] = reject
        second = first + output_penalty
        acceptance = initial.T @ prefixes[-1].T @ invalid @ prefixes[-1] @ initial
        assert np.linalg.norm(history.T @ output_penalty @ history
                              - (np.eye(4) - acceptance) / normalization) < 1e-12
        eigen1, vec1 = eigh(first)
        eigen2, _ = eigh(second)
        dim1 = int(np.count_nonzero(np.abs(eigen1) < 1e-10))
        dim2 = int(np.count_nonzero(np.abs(eigen2) < 1e-10))
        expected = 3 if invert_output else 1
        assert dim1 == 4 and dim2 == expected
        kernel1 = vec1[:, np.abs(eigen1) < 1e-10]
        assert np.linalg.norm(kernel1 @ kernel1.T - history @ history.T) < 1e-10
        gap1 = float(eigen1[eigen1 > 1e-10][0])
        gap2 = float(eigen2[eigen2 > 1e-10][0])
        assert gap1 >= 1 / (8 * length ** 2)
        assert gap2 >= 1 / (120 * length ** 3)
        results.append({"case": "YES" if invert_output else "NO",
                        "clock_positions": length, "clock_weights": scales_squared,
                        "normalization": normalization, "kernel_dimensions": [dim1, dim2],
                        "fraction": dim2 / dim1,
                        "acceptance_trace_fraction": float(np.trace(acceptance) / 4),
                        "positive_gaps": [gap1, gap2]})
    print(json.dumps({"status": "PASS", "kind": "classical valid-clock matrix check",
                      "results": results,
                      "zero_final_kernel": check_zero_final_kernel()}, indent=2))


if __name__ == "__main__":
    main()
