#!/usr/bin/env python3
"""Exact lazy-SAT diagnosis of one-vertex Ramsey-graph extension.

It adds the large blue-side clauses lazily.  Each SAT candidate is checked by the independent
bitset clique oracle.  A missed independent set becomes a new hard clause.  The
loop terminates either with a verified extension or with solver-level UNSAT.

The UNSAT result is exact relative to the fixed base graph.  It is not a DRAT
certificate and says nothing about graphs obtained after changing base edges.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

from pysat.solvers import Solver

try:
    from .graph_utils import add_vertex, enumerate_cliques, write_matrix
    from .verify_ramsey import CliqueTargetSearch, complement, read_matrix, verify
except ImportError:  # pragma: no cover - direct CLI execution
    from graph_utils import add_vertex, enumerate_cliques, write_matrix
    from verify_ramsey import CliqueTargetSearch, complement, read_matrix, verify


def diagnose(
    rows: list[int],
    r: int,
    s: int,
    solver_name: str,
    max_iterations: int | None,
) -> dict:
    start = time.perf_counter()
    n = len(rows)
    red_masks = enumerate_cliques(rows, r - 1)
    red_clauses = [[-(v + 1) for v in range(n) if (mask >> v) & 1] for mask in red_masks]
    comp = complement(rows)
    all_vertices = (1 << n) - 1
    blue_added = 0
    iterations = 0

    with Solver(name=solver_name, bootstrap_with=red_clauses) as solver:
        # Prefer a large candidate neighborhood while respecting red clauses.
        solver.set_phases(list(range(1, n + 1)))
        while max_iterations is None or iterations < max_iterations:
            iterations += 1
            if not solver.solve():
                return {
                    "one_vertex_extendable": False,
                    "solver_status": "UNSAT",
                    "solver": solver_name,
                    "vertices_in_base": n,
                    "r": r,
                    "s": s,
                    "red_extension_clauses": len(red_clauses),
                    "blue_clauses_discovered": blue_added,
                    "cegar_iterations": iterations,
                    "elapsed_seconds": time.perf_counter() - start,
                }

            model_positive = {lit for lit in solver.get_model() if 0 < lit <= n}
            neighborhood = [v for v in range(n) if v + 1 in model_positive]
            neighborhood_mask = sum(1 << v for v in neighborhood)
            outside = all_vertices ^ neighborhood_mask
            missed = CliqueTargetSearch(comp, s - 1).run(candidates=outside)
            if not missed.exists:
                return {
                    "one_vertex_extendable": True,
                    "solver_status": "SAT",
                    "solver": solver_name,
                    "vertices_in_base": n,
                    "r": r,
                    "s": s,
                    "red_extension_clauses": len(red_clauses),
                    "blue_clauses_discovered": blue_added,
                    "cegar_iterations": iterations,
                    "elapsed_seconds": time.perf_counter() - start,
                    "neighborhood": neighborhood,
                }

            solver.add_clause([v + 1 for v in missed.witness or []])
            blue_added += 1

    return {
        "one_vertex_extendable": None,
        "solver_status": "ITERATION_LIMIT",
        "solver": solver_name,
        "vertices_in_base": n,
        "r": r,
        "s": s,
        "red_extension_clauses": len(red_clauses),
        "blue_clauses_discovered": blue_added,
        "cegar_iterations": iterations,
        "elapsed_seconds": time.perf_counter() - start,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("r", type=int)
    parser.add_argument("s", type=int)
    parser.add_argument("--solver", default="cadical195")
    parser.add_argument("--max-iterations", type=int)
    parser.add_argument("--json", type=Path)
    parser.add_argument("--extension", type=Path)
    args = parser.parse_args()

    base = verify(args.matrix, args.r, args.s)
    if not base["valid_ramsey_certificate"]:
        raise SystemExit("base matrix is not a valid Ramsey certificate")
    rows = read_matrix(args.matrix)
    result = diagnose(
        rows, args.r, args.s, args.solver, args.max_iterations
    )
    result["base_sha256"] = base["sha256"]

    if result["one_vertex_extendable"] and args.extension:
        augmented = add_vertex(rows, result["neighborhood"])
        write_matrix(augmented, args.extension)
        result["extension_sha256"] = hashlib.sha256(
            args.extension.read_bytes()
        ).hexdigest()
        result["extension_independent_verification"] = verify(
            args.extension, args.r, args.s
        )

    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
