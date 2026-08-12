#!/usr/bin/env python3
"""Second independent certificate checker using SAT vertex-selection encoding."""

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
    from .verify_ramsey import complement, read_matrix
except ImportError:  # pragma: no cover
    from verify_ramsey import complement, read_matrix


def sat_contains_clique(
    rows: list[int], target: int, solver_name: str = "cadical195"
) -> dict:
    start = time.perf_counter()
    n = len(rows)
    clauses = []
    for u in range(n):
        for v in range(u + 1, n):
            if not ((rows[u] >> v) & 1):
                clauses.append([-(u + 1), -(v + 1)])
    pool = IDPool(start_from=n + 1)
    # Exactly target is equivalent to at least target for clique existence and
    # prevents the solver from exploring unnecessarily oversized selections.
    clauses.extend(
        CardEnc.equals(
            lits=list(range(1, n + 1)),
            bound=target,
            vpool=pool,
            encoding=EncType.seqcounter,
        ).clauses
    )
    with Solver(name=solver_name, bootstrap_with=clauses) as solver:
        solver.set_phases(list(range(-1, -n - 1, -1)))
        exists = solver.solve()
        witness = None
        if exists:
            selected = {lit for lit in solver.get_model() if 0 < lit <= n}
            witness = sorted(v - 1 for v in selected)[:target]
        return {
            "target": target,
            "exists": exists,
            "witness": witness,
            "solver": solver_name,
            "clauses": len(clauses),
            "elapsed_seconds": time.perf_counter() - start,
        }


def sat_contains_clique_positional(
    rows: list[int], target: int, solver_name: str = "cadical195"
) -> dict:
    """Ordered-position clique encoding, useful for large target cliques."""
    start = time.perf_counter()
    n = len(rows)

    def variable(position: int, vertex: int) -> int:
        return position * n + vertex + 1

    pool = IDPool(start_from=target * n + 1)
    clauses: list[list[int]] = []
    for position in range(target):
        clauses.extend(
            CardEnc.equals(
                lits=[variable(position, v) for v in range(n)],
                bound=1,
                vpool=pool,
                encoding=EncType.seqcounter,
            ).clauses
        )
    # Consecutive positions must be strictly increasing.
    for position in range(target - 1):
        for u in range(n):
            for v in range(u + 1):
                clauses.append(
                    [-variable(position, u), -variable(position + 1, v)]
                )
    # Increasing vertex pairs selected in any two positions must be edges.
    nonedges = [
        (u, v)
        for u in range(n)
        for v in range(u + 1, n)
        if not ((rows[u] >> v) & 1)
    ]
    for first in range(target):
        for second in range(first + 1, target):
            for u, v in nonedges:
                clauses.append(
                    [-variable(first, u), -variable(second, v)]
                )
    with Solver(name=solver_name, bootstrap_with=clauses) as solver:
        solver.set_phases(
            [-variable(position, v) for position in range(target) for v in range(n)]
        )
        exists = solver.solve()
        witness = None
        if exists:
            positive = {lit for lit in solver.get_model() if lit > 0}
            witness = [
                next(v for v in range(n) if variable(position, v) in positive)
                for position in range(target)
            ]
        return {
            "target": target,
            "exists": exists,
            "witness": witness,
            "solver": solver_name,
            "encoding": "ordered_positions",
            "clauses": len(clauses),
            "elapsed_seconds": time.perf_counter() - start,
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("r", type=int)
    parser.add_argument("s", type=int)
    parser.add_argument("--solver", default="cadical195")
    parser.add_argument(
        "--encoding", choices=("selector", "positional"), default="selector"
    )
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    rows = read_matrix(args.matrix)
    checker = (
        sat_contains_clique_positional
        if args.encoding == "positional"
        else sat_contains_clique
    )
    clique = checker(rows, args.r, args.solver)
    independent = checker(complement(rows), args.s, args.solver)
    valid = not clique["exists"] and not independent["exists"]
    result = {
        "input": str(args.matrix.resolve()),
        "sha256": hashlib.sha256(args.matrix.read_bytes()).hexdigest(),
        "vertices": len(rows),
        "r": args.r,
        "s": args.s,
        "valid_ramsey_certificate": valid,
        "certified_lower_bound": len(rows) + 1 if valid else None,
        "searches": {
            "forbidden_clique_sat": clique,
            "forbidden_independent_set_sat": independent,
        },
    }
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.json:
        args.json.write_text(rendered + "\n", encoding="utf-8")
    raise SystemExit(0 if valid else 1)


if __name__ == "__main__":
    main()
