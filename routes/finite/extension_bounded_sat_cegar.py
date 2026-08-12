#!/usr/bin/env python3
"""Find and prove the exact frozen-base conflict radius by lazy SAT.

For bounds k=0,1,..., this asks whether the new vertex can hit every forbidden
blue set while completing at most k red (r-1)-cliques.  Red violations are
reified and constrained by an exact cardinality encoding; blue clauses are
discovered with the independent bitset oracle.  The first SAT k is therefore
the proved frozen-base optimum.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Solver

try:
    from .graph_utils import add_vertex, enumerate_cliques, write_matrix
    from .verify_ramsey import CliqueTargetSearch, complement, read_matrix, verify
except ImportError:  # pragma: no cover
    from graph_utils import add_vertex, enumerate_cliques, write_matrix
    from verify_ramsey import CliqueTargetSearch, complement, read_matrix, verify


def solve_at_bound(
    rows: list[int],
    r: int,
    s: int,
    bound: int,
    solver_name: str,
    batch_size: int,
) -> dict:
    n = len(rows)
    red_masks = enumerate_cliques(rows, r - 1)
    red_indicators = [n + i + 1 for i in range(len(red_masks))]
    clauses: list[list[int]] = []
    for mask, indicator in zip(red_masks, red_indicators):
        clauses.append(
            [-(v + 1) for v in range(n) if (mask >> v) & 1] + [indicator]
        )
    pool = IDPool(start_from=n + len(red_masks) + 1)
    clauses.extend(
        CardEnc.atmost(
            lits=red_indicators,
            bound=bound,
            vpool=pool,
            encoding=EncType.seqcounter,
        ).clauses
    )

    comp = complement(rows)
    all_vertices = (1 << n) - 1
    iterations = 0
    blue_added = 0
    start = time.perf_counter()
    with Solver(name=solver_name, bootstrap_with=clauses) as solver:
        solver.set_phases(list(range(1, n + 1)) + [-v for v in red_indicators])
        while True:
            iterations += 1
            if not solver.solve():
                return {
                    "status": "UNSAT",
                    "bound": bound,
                    "cegar_iterations": iterations,
                    "blue_clauses_discovered": blue_added,
                    "elapsed_seconds": time.perf_counter() - start,
                }
            positive = {lit for lit in solver.get_model() if 0 < lit <= n}
            neighborhood = [v for v in range(n) if v + 1 in positive]
            neighborhood_mask = sum(1 << v for v in neighborhood)
            outside = all_vertices ^ neighborhood_mask
            missed = enumerate_cliques(
                comp, s - 1, candidates=outside, limit=batch_size
            )
            if missed:
                for mask in missed:
                    solver.add_clause(
                        [v + 1 for v in range(n) if (mask >> v) & 1]
                    )
                blue_added += len(missed)
                continue

            actual_red = [
                mask for mask in red_masks if mask & neighborhood_mask == mask
            ]
            if len(actual_red) > bound:
                raise AssertionError("cardinality encoding accepted too many conflicts")
            return {
                "status": "SAT",
                "bound": bound,
                "actual_red_conflicts": len(actual_red),
                "red_conflict_witnesses": [
                    [v for v in range(n) if (mask >> v) & 1]
                    for mask in actual_red
                ],
                "neighborhood": neighborhood,
                "cegar_iterations": iterations,
                "blue_clauses_discovered": blue_added,
                "elapsed_seconds": time.perf_counter() - start,
            }


def optimize(
    rows: list[int],
    r: int,
    s: int,
    max_bound: int,
    min_bound: int,
    solver_name: str,
    batch_size: int,
) -> dict:
    attempts = []
    for bound in range(min_bound, max_bound + 1):
        attempt = solve_at_bound(rows, r, s, bound, solver_name, batch_size)
        attempts.append(attempt)
        if attempt["status"] == "SAT":
            return {
                "minimum_frozen_base_conflicts": bound
                if min_bound == 0
                else None,
                "minimum_proved": min_bound == 0,
                "feasible_frozen_base_conflicts": bound,
                "tested_bound_range": [min_bound, bound],
                "solver": solver_name,
                "r": r,
                "s": s,
                "vertices_in_base": len(rows),
                "attempts": attempts,
                "neighborhood": attempt["neighborhood"],
                "red_conflict_witnesses": attempt["red_conflict_witnesses"],
            }
    return {
        "minimum_frozen_base_conflicts": None,
        "minimum_proved": False,
        "feasible_frozen_base_conflicts": None,
        "tested_bound_range": [min_bound, max_bound],
        "proved_unsat_bounds": list(range(min_bound, max_bound + 1)),
        "solver": solver_name,
        "r": r,
        "s": s,
        "vertices_in_base": len(rows),
        "attempts": attempts,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("r", type=int)
    parser.add_argument("s", type=int)
    parser.add_argument("--solver", default="cadical195")
    parser.add_argument("--max-bound", type=int, default=20)
    parser.add_argument("--min-bound", type=int, default=0)
    parser.add_argument("--batch-size", type=int, default=256)
    parser.add_argument("--json", type=Path)
    parser.add_argument("--near-miss", type=Path)
    args = parser.parse_args()

    base = verify(args.matrix, args.r, args.s)
    if not base["valid_ramsey_certificate"]:
        raise SystemExit("base matrix is not a valid Ramsey certificate")
    rows = read_matrix(args.matrix)
    result = optimize(
        rows,
        args.r,
        args.s,
        args.max_bound,
        args.min_bound,
        args.solver,
        args.batch_size,
    )
    result["base_sha256"] = base["sha256"]

    if result["feasible_frozen_base_conflicts"] is not None and args.near_miss:
        augmented = add_vertex(rows, result["neighborhood"])
        write_matrix(augmented, args.near_miss)
        result["near_miss_sha256"] = hashlib.sha256(
            args.near_miss.read_bytes()
        ).hexdigest()
        result["has_forbidden_clique"] = CliqueTargetSearch(
            augmented, args.r
        ).run().exists
        result["has_forbidden_independent_set"] = CliqueTargetSearch(
            complement(augmented), args.s
        ).run().exists

    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
