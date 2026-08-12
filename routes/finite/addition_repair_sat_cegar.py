#!/usr/bin/env python3
"""Exact add-only SAT repair after selected edge deletions in an R(3,s) near miss.

Each absent edge is a Boolean add-variable.  All triples are constrained to
remain triangle-free, including triangles that would require two or three added
edges.  Independent s-sets are discovered lazily and converted to hitting
clauses requiring at least one missing edge of that set to be added.  SAT yields
a graph passed to the independent checker; UNSAT is exact for the chosen
deletion set and add-only repair family.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import time
from pathlib import Path

from pysat.solvers import Solver

try:
    from .graph_utils import write_matrix
    from .verify_ramsey import CliqueTargetSearch, complement, read_matrix, verify
except ImportError:  # pragma: no cover
    from graph_utils import write_matrix
    from verify_ramsey import CliqueTargetSearch, complement, read_matrix, verify


def flip(rows: list[int], u: int, v: int) -> None:
    rows[u] ^= 1 << v
    rows[v] ^= 1 << u


def addition_variables(rows: list[int]) -> tuple[dict[tuple[int, int], int], list[tuple[int, int]]]:
    pairs = [
        (u, v)
        for u in range(len(rows))
        for v in range(u + 1, len(rows))
        if not ((rows[u] >> v) & 1)
    ]
    return {pair: i + 1 for i, pair in enumerate(pairs)}, pairs


def triangle_free_clauses(
    rows: list[int], variables: dict[tuple[int, int], int]
) -> list[list[int]]:
    clauses = []
    for a, b, c in itertools.combinations(range(len(rows)), 3):
        absent = []
        for u, v in ((a, b), (a, c), (b, c)):
            if not ((rows[u] >> v) & 1):
                absent.append(variables[(u, v)])
        if not absent:
            raise ValueError(f"post-deletion graph still has triangle {(a,b,c)}")
        clauses.append([-variable for variable in absent])
    return clauses


def repair(
    rows: list[int], s: int, solver_name: str, max_iterations: int | None
) -> dict:
    start = time.perf_counter()
    variables, pairs = addition_variables(rows)
    clauses = triangle_free_clauses(rows, variables)
    iterations = 0
    independent_clauses = 0

    with Solver(name=solver_name, bootstrap_with=clauses) as solver:
        # Prefer sparse repairs.
        solver.set_phases([-i for i in range(1, len(pairs) + 1)])
        while max_iterations is None or iterations < max_iterations:
            iterations += 1
            if not solver.solve():
                return {
                    "status": "UNSAT",
                    "solver": solver_name,
                    "addition_variables": len(pairs),
                    "triangle_free_clauses": len(clauses),
                    "independent_hitting_clauses": independent_clauses,
                    "cegar_iterations": iterations,
                    "elapsed_seconds": time.perf_counter() - start,
                }

            positive = {lit for lit in solver.get_model() if lit > 0}
            candidate = rows.copy()
            added = []
            for pair, variable in variables.items():
                if variable in positive:
                    flip(candidate, *pair)
                    added.append(list(pair))

            missed = CliqueTargetSearch(complement(candidate), s).run()
            if not missed.exists:
                return {
                    "status": "SAT",
                    "solver": solver_name,
                    "addition_variables": len(pairs),
                    "triangle_free_clauses": len(clauses),
                    "independent_hitting_clauses": independent_clauses,
                    "cegar_iterations": iterations,
                    "elapsed_seconds": time.perf_counter() - start,
                    "added_edges": added,
                    "candidate_rows": candidate,
                }

            witness = missed.witness or []
            hitting = [
                variables[(min(u, v), max(u, v))]
                for u, v in itertools.combinations(witness, 2)
                if (min(u, v), max(u, v)) in variables
            ]
            if not hitting:
                # An independent set should contain only nonedges, so this is a
                # defensive assertion against parser/oracle mismatch.
                raise AssertionError("independent witness has no addable edge")
            solver.add_clause(hitting)
            independent_clauses += 1

    return {
        "status": "ITERATION_LIMIT",
        "solver": solver_name,
        "addition_variables": len(pairs),
        "triangle_free_clauses": len(clauses),
        "independent_hitting_clauses": independent_clauses,
        "cegar_iterations": iterations,
        "elapsed_seconds": time.perf_counter() - start,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("s", type=int)
    parser.add_argument(
        "--delete", nargs=2, type=int, action="append", required=True
    )
    parser.add_argument("--solver", default="cadical195")
    parser.add_argument("--max-iterations", type=int)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()

    rows = read_matrix(args.matrix)
    deleted = []
    for u, v in args.delete:
        if not ((rows[u] >> v) & 1):
            raise SystemExit(f"cannot delete absent edge {(u,v)}")
        flip(rows, u, v)
        deleted.append([min(u, v), max(u, v)])

    if CliqueTargetSearch(rows, 3).run().exists:
        raise SystemExit("selected deletions do not destroy every initial triangle")
    result = repair(rows, args.s, args.solver, args.max_iterations)
    result["input_sha256"] = hashlib.sha256(args.matrix.read_bytes()).hexdigest()
    result["deleted_edges"] = deleted

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
