#!/usr/bin/env python3
"""Bounded-uphill exact-delta search for an R(3,s) graph.

The score is exactly (# triangles + # independent s-sets).  Edge-flip deltas
are exact:

* add uv: common_neighbors(u,v) - I_s sets containing {u,v};
* remove uv: -triangles containing uv + newly created I_s sets containing uv.

Only states whose independent sets can be fully enumerated under the active
score cap are accepted.  Thus every reported score is verifier-consistent.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import time
from collections import Counter
from pathlib import Path

try:
    from .graph_utils import enumerate_cliques, write_matrix
    from .verify_ramsey import complement, read_matrix, verify
except ImportError:  # pragma: no cover
    from graph_utils import enumerate_cliques, write_matrix
    from verify_ramsey import complement, read_matrix, verify


def triangle_masks(rows: list[int]) -> list[int]:
    result = []
    n = len(rows)
    for u in range(n):
        later = rows[u] & ~((1 << (u + 1)) - 1)
        while later:
            vbit = later & -later
            later ^= vbit
            v = vbit.bit_length() - 1
            common = rows[u] & rows[v] & ~((1 << (v + 1)) - 1)
            while common:
                wbit = common & -common
                common ^= wbit
                result.append((1 << u) | (1 << v) | wbit)
    return result


def conflicts(
    rows: list[int], s: int, independent_limit: int | None = None
) -> tuple[list[int], list[int], bool]:
    triangles = triangle_masks(rows)
    independent = enumerate_cliques(
        complement(rows), s, limit=independent_limit
    )
    truncated = (
        independent_limit is not None and len(independent) >= independent_limit
    )
    return triangles, independent, truncated


def pair_counts(masks: list[int]) -> Counter[tuple[int, int]]:
    counts: Counter[tuple[int, int]] = Counter()
    for mask in masks:
        vertices = [i for i in range(mask.bit_length()) if (mask >> i) & 1]
        for pos, u in enumerate(vertices):
            for v in vertices[pos + 1 :]:
                counts[(u, v)] += 1
    return counts


def flip_edge(rows: list[int], u: int, v: int) -> None:
    rows[u] ^= 1 << v
    rows[v] ^= 1 << u


def removal_created_independent_count(
    rows: list[int], u: int, v: int, s: int, limit: int | None
) -> tuple[int, bool]:
    n = len(rows)
    mask = (1 << n) - 1
    candidates = mask & ~(rows[u] | rows[v] | (1 << u) | (1 << v))
    found = enumerate_cliques(
        complement(rows), s - 2, candidates=candidates, limit=limit
    )
    truncated = limit is not None and len(found) >= limit
    return len(found), truncated


def exact_delta(
    rows: list[int],
    u: int,
    v: int,
    s: int,
    triangle_pair_count: Counter[tuple[int, int]],
    independent_pair_count: Counter[tuple[int, int]],
    max_new_independent: int | None,
) -> tuple[int | None, dict]:
    pair = (min(u, v), max(u, v))
    if (rows[u] >> v) & 1:
        created, truncated = removal_created_independent_count(
            rows, u, v, s, max_new_independent
        )
        if truncated:
            return None, {"operation": "remove", "capped": True}
        destroyed = triangle_pair_count[pair]
        return created - destroyed, {
            "operation": "remove",
            "destroyed_triangles": destroyed,
            "created_independent_sets": created,
        }
    created = (rows[u] & rows[v]).bit_count()
    destroyed = independent_pair_count[pair]
    return created - destroyed, {
        "operation": "add",
        "created_triangles": created,
        "destroyed_independent_sets": destroyed,
    }


def candidate_pairs(
    rows: list[int],
    triangles: list[int],
    independent: list[int],
    rng: random.Random,
    random_candidates: int,
) -> set[tuple[int, int]]:
    n = len(rows)
    result = set(pair_counts(triangles)) | set(pair_counts(independent))
    total = n * (n - 1) // 2
    for _ in range(min(random_candidates, total)):
        u = rng.randrange(n)
        v = rng.randrange(n - 1)
        if v >= u:
            v += 1
        result.add((min(u, v), max(u, v)))
    return result


def search(
    initial: list[int],
    s: int,
    seconds: float,
    max_uphill: int,
    tabu_length: int,
    random_candidates: int,
    plateau_patience: int,
    seed: int,
) -> tuple[list[int], dict]:
    rng = random.Random(seed)
    rows = initial.copy()
    triangles, independent, truncated = conflicts(rows, s)
    if truncated:
        raise AssertionError("uncapped initial enumeration was truncated")
    score = len(triangles) + len(independent)
    best_rows = rows.copy()
    best_score = score
    best_split = [len(triangles), len(independent)]
    start_score = score
    start = time.perf_counter()
    iterations = 0
    accepted = 0
    restarts = 0
    improvements = []
    compound_launches = []
    tabu_until: dict[tuple[int, int], int] = {}
    stagnation = 0

    while time.perf_counter() - start < seconds and best_score > 0:
        iterations += 1
        triangle_counts = pair_counts(triangles)
        independent_counts = pair_counts(independent)
        pairs = candidate_pairs(
            rows, triangles, independent, rng, random_candidates
        )
        cap = best_score + max_uphill
        moves = []
        for u, v in pairs:
            if tabu_until.get((u, v), -1) > iterations:
                continue
            remaining_capacity = max(1, cap - (score - triangle_counts[(u, v)]) + 1)
            delta, detail = exact_delta(
                rows,
                u,
                v,
                s,
                triangle_counts,
                independent_counts,
                remaining_capacity,
            )
            if delta is None or score + delta > cap:
                continue
            moves.append((score + delta, rng.random(), u, v, detail))

        if not moves:
            rows = best_rows.copy()
            triangles, independent, _ = conflicts(rows, s)
            score = best_score
            tabu_until.clear()
            stagnation = 0
            restarts += 1
            continue

        improving = [move for move in moves if move[0] < score]
        if improving:
            improving.sort()
            pool = improving[: min(8, len(improving))]
            chosen = rng.choice(pool)
        elif stagnation >= plateau_patience:
            supported = [
                move
                for move in moves
                if (move[2], move[3]) in triangle_counts
                or (move[2], move[3]) in independent_counts
            ]
            supported.sort()
            chosen = supported[0] if supported else min(moves)
            compound_launches.append(
                {
                    "iteration": iterations,
                    "from_score": score,
                    "to_score": chosen[0],
                    "move": [chosen[2], chosen[3]],
                    "detail": chosen[4],
                }
            )
        else:
            moves.sort()
            # Usually take a low barrier, with a small diversity tail.
            pool = moves[: min(16, len(moves))]
            chosen = rng.choice(pool)

        new_score_predicted, _, u, v, detail = chosen
        flip_edge(rows, u, v)
        new_triangles, new_independent, was_truncated = conflicts(
            rows, s, independent_limit=cap + 1
        )
        if was_truncated:
            flip_edge(rows, u, v)
            tabu_until[(u, v)] = iterations + tabu_length
            continue
        exact_new_score = len(new_triangles) + len(new_independent)
        if exact_new_score != new_score_predicted:
            raise AssertionError(
                f"delta mismatch for {(u, v)}: predicted {new_score_predicted}, "
                f"recomputed {exact_new_score}, detail={detail}"
            )
        triangles, independent, score = (
            new_triangles,
            new_independent,
            exact_new_score,
        )
        accepted += 1
        tabu_until[(u, v)] = iterations + tabu_length
        stagnation += 1

        if score < best_score:
            best_score = score
            best_rows = rows.copy()
            best_split = [len(triangles), len(independent)]
            improvements.append(
                {
                    "iteration": iterations,
                    "score": score,
                    "triangles": best_split[0],
                    "independent_sets": best_split[1],
                    "move": [u, v],
                    "detail": detail,
                    "elapsed_seconds": time.perf_counter() - start,
                }
            )
            stagnation = 0
        elif stagnation >= 200:
            rows = best_rows.copy()
            triangles, independent, _ = conflicts(rows, s)
            score = best_score
            tabu_until.clear()
            stagnation = 0
            restarts += 1

    return best_rows, {
        "seed": seed,
        "seconds_requested": seconds,
        "elapsed_seconds": time.perf_counter() - start,
        "iterations": iterations,
        "accepted_moves": accepted,
        "anchored_restarts": restarts,
        "max_uphill": max_uphill,
        "tabu_length": tabu_length,
        "random_candidates": random_candidates,
        "plateau_patience": plateau_patience,
        "start_score": start_score,
        "best_score": best_score,
        "best_triangles": best_split[0],
        "best_independent_sets": best_split[1],
        "improvements": improvements,
        "compound_launches": compound_launches[:100],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("s", type=int)
    parser.add_argument("--seconds", type=float, default=60.0)
    parser.add_argument("--max-uphill", type=int, default=64)
    parser.add_argument("--tabu-length", type=int, default=8)
    parser.add_argument("--random-candidates", type=int, default=32)
    parser.add_argument("--plateau-patience", type=int, default=8)
    parser.add_argument("--seed", type=int, default=20260812)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()

    initial = read_matrix(args.matrix)
    best, result = search(
        initial,
        args.s,
        args.seconds,
        args.max_uphill,
        args.tabu_length,
        args.random_candidates,
        args.plateau_patience,
        args.seed,
    )
    write_matrix(best, args.output)
    result["input_sha256"] = hashlib.sha256(args.matrix.read_bytes()).hexdigest()
    result["output_sha256"] = hashlib.sha256(args.output.read_bytes()).hexdigest()
    if result["best_score"] == 0:
        result["independent_verification"] = verify(args.output, 3, args.s)
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
