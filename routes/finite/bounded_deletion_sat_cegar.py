#!/usr/bin/env python3
"""Exact triangle-free / I_s-free search within a base-edge deletion budget.

Every final edge is a SAT variable.  All triangle-free clauses are present from
the start.  At most ``budget`` edges present in the input may be deleted;
initial nonedges may be added without a count limit.  Independent s-sets are
found by the independent bitset oracle and added lazily as edge-hitting clauses.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import time
from pathlib import Path

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Solver

try:
    from .graph_utils import write_matrix
    from .verify_ramsey import CliqueTargetSearch, complement, read_matrix, verify
except ImportError:  # pragma: no cover
    from graph_utils import write_matrix
    from verify_ramsey import CliqueTargetSearch, complement, read_matrix, verify


def build_variables(n: int) -> tuple[dict[tuple[int, int], int], list[tuple[int, int]]]:
    pairs = list(itertools.combinations(range(n), 2))
    return {pair: i + 1 for i, pair in enumerate(pairs)}, pairs


def solve(
    initial: list[int],
    s: int,
    budget: int,
    solver_name: str,
    max_iterations: int | None,
    max_seconds: float | None,
) -> dict:
    start = time.perf_counter()
    n = len(initial)
    variables, pairs = build_variables(n)
    original_edges = [
        variables[(u, v)] for u, v in pairs if (initial[u] >> v) & 1
    ]
    pool = IDPool(start_from=len(pairs) + 1)
    clauses = [
        [-variables[(a, b)], -variables[(a, c)], -variables[(b, c)]]
        for a, b, c in itertools.combinations(range(n), 3)
    ]
    clauses.extend(
        CardEnc.atmost(
            lits=[-variable for variable in original_edges],
            bound=budget,
            vpool=pool,
            encoding=EncType.seqcounter,
        ).clauses
    )
    phases = [
        variable if (initial[u] >> v) & 1 else -variable
        for (u, v), variable in variables.items()
    ]
    iterations = 0
    independent_clauses = 0

    with Solver(name=solver_name, bootstrap_with=clauses) as solver:
        solver.set_phases(phases)
        while max_iterations is None or iterations < max_iterations:
            if max_seconds is not None and time.perf_counter() - start >= max_seconds:
                return {
                    "status": "TIME_LIMIT",
                    "solver": solver_name,
                    "deletion_budget": budget,
                    "cegar_iterations": iterations,
                    "independent_hitting_clauses": independent_clauses,
                    "elapsed_seconds": time.perf_counter() - start,
                }
            iterations += 1
            if not solver.solve():
                return {
                    "status": "UNSAT",
                    "solver": solver_name,
                    "deletion_budget": budget,
                    "edge_variables": len(pairs),
                    "original_edges": len(original_edges),
                    "triangle_free_clauses": n * (n - 1) * (n - 2) // 6,
                    "independent_hitting_clauses": independent_clauses,
                    "cegar_iterations": iterations,
                    "elapsed_seconds": time.perf_counter() - start,
                }

            positive = {lit for lit in solver.get_model() if 0 < lit <= len(pairs)}
            candidate = [0] * n
            final_edges = []
            for (u, v), variable in variables.items():
                if variable in positive:
                    candidate[u] |= 1 << v
                    candidate[v] |= 1 << u
                    final_edges.append((u, v))
            missed = CliqueTargetSearch(complement(candidate), s).run()
            if not missed.exists:
                initial_set = {
                    (u, v) for u, v in pairs if (initial[u] >> v) & 1
                }
                final_set = set(final_edges)
                return {
                    "status": "SAT",
                    "solver": solver_name,
                    "deletion_budget": budget,
                    "edge_variables": len(pairs),
                    "original_edges": len(original_edges),
                    "triangle_free_clauses": n * (n - 1) * (n - 2) // 6,
                    "independent_hitting_clauses": independent_clauses,
                    "cegar_iterations": iterations,
                    "elapsed_seconds": time.perf_counter() - start,
                    "deleted_edges": [list(edge) for edge in sorted(initial_set-final_set)],
                    "added_edges": [list(edge) for edge in sorted(final_set-initial_set)],
                    "candidate_rows": candidate,
                }

            witness = missed.witness or []
            solver.add_clause(
                [
                    variables[(min(u, v), max(u, v))]
                    for u, v in itertools.combinations(witness, 2)
                ]
            )
            independent_clauses += 1

    return {
        "status": "ITERATION_LIMIT",
        "solver": solver_name,
        "deletion_budget": budget,
        "cegar_iterations": iterations,
        "elapsed_seconds": time.perf_counter() - start,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("s", type=int)
    parser.add_argument("--budget", type=int, required=True)
    parser.add_argument("--solver", default="cadical195")
    parser.add_argument("--max-iterations", type=int)
    parser.add_argument("--max-seconds", type=float)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()

    initial = read_matrix(args.matrix)
    result = solve(
        initial,
        args.s,
        args.budget,
        args.solver,
        args.max_iterations,
        args.max_seconds,
    )
    result["input_sha256"] = hashlib.sha256(args.matrix.read_bytes()).hexdigest()
    if result["status"] == "SAT" and args.output:
        candidate = result.pop("candidate_rows")
        write_matrix(candidate, args.output)
        result["output_sha256"] = hashlib.sha256(
            args.output.read_bytes()
        ).hexdigest()
        result["independent_verification"] = verify(args.output, 3, args.s)
    else:
        result.pop("candidate_rows", None)
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
