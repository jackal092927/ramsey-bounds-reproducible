#!/usr/bin/env python3
"""Bounded fixed-base search for a dispersed R(3,13;61) near miss.

Starting from a verified 60-vertex (3,13) graph, choose the neighbourhood S
of a new vertex.  Every edge of the old graph induced by S creates exactly
one triangle.  The multiplicity of a new--old edge (60,v) is exactly the
degree of v in the old graph induced by S.  We therefore encode both an
exact triangle count and a hard maximum triangle-edge multiplicity.

All independent 12-sets of the base are preloaded.  Consequently a model
has no independent 13-set after the new vertex is added.  Solver limits are
reported literally; only a completed UNSAT call is labelled UNSAT.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path
from typing import Any

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Solver

try:
    from .graph_utils import add_vertex, enumerate_cliques, write_matrix
    from .new_basin_search import (
        bounded_cegar_loop,
        edge_present,
        sha256,
        triangle_edge_multiplicity,
        triangle_tuples,
    )
    from .verify_ramsey import complement, read_matrix, verify
except ImportError:  # pragma: no cover - direct execution
    from graph_utils import add_vertex, enumerate_cliques, write_matrix
    from new_basin_search import (
        bounded_cegar_loop,
        edge_present,
        sha256,
        triangle_edge_multiplicity,
        triangle_tuples,
    )
    from verify_ramsey import complement, read_matrix, verify


def selected_induced_edge_diagnostics(
    rows: list[int], selected: list[int]
) -> tuple[int, int, dict[int, int]]:
    """Return induced edge count, max induced degree, and all degrees."""
    chosen = set(selected)
    degrees = {
        v: sum(edge_present(rows, v, u) for u in chosen if u != v)
        for v in selected
    }
    edge_count = sum(degrees.values()) // 2
    return edge_count, max(degrees.values(), default=0), degrees


def source_status(status: str) -> str:
    if status == "UNKNOWN_GLOBAL_WALL_LIMIT":
        return "TIME_LIMIT"
    if status == "UNKNOWN_GLOBAL_CONFLICT_LIMIT":
        return "UNKNOWN_CONFLICT_LIMIT"
    return status


def run(args: argparse.Namespace) -> dict[str, Any]:
    base_check = verify(args.matrix, 3, 13)
    if not base_check["valid_ramsey_certificate"] or base_check["vertices"] != 60:
        raise ValueError("a valid 60-vertex (3,13) base is required")

    rows = read_matrix(args.matrix)
    n = len(rows)
    base_edges = [
        (u, v)
        for u in range(n)
        for v in range(u + 1, n)
        if edge_present(rows, u, v)
    ]
    x = {v: v + 1 for v in range(n)}
    induced = {edge: n + i + 1 for i, edge in enumerate(base_edges)}
    pool = IDPool(start_from=n + len(base_edges) + 1)
    clauses: list[list[int]] = []

    # Exact reification y_uv <-> (x_u and x_v).
    for (u, v), flag in induced.items():
        clauses.append([-x[u], -x[v], flag])
        clauses.append([-flag, x[u]])
        clauses.append([-flag, x[v]])

    edge_cardinality = CardEnc.atmost if args.at_most else CardEnc.equals
    clauses.extend(
        edge_cardinality(
            lits=list(induced.values()),
            bound=args.triangles,
            vpool=pool,
            encoding=EncType.seqcounter,
        ).clauses
    )

    degree_clause_count = 0
    for v in range(n):
        incident = [flag for edge, flag in induced.items() if v in edge]
        encoded = CardEnc.atmost(
            lits=incident,
            bound=args.max_multiplicity,
            vpool=pool,
            encoding=EncType.seqcounter,
        ).clauses
        degree_clause_count += len(encoded)
        clauses.extend(encoded)

    blue_count = 0
    blue_hash = hashlib.sha256()
    for mask in enumerate_cliques(complement(rows), 12):
        clauses.append([x[v] for v in range(n) if (mask >> v) & 1])
        blue_count += 1
        blue_hash.update(f"{mask:016x}\n".encode())

    def no_lazy_cuts(_model: list[int]) -> list[list[int]]:
        return []

    started = time.perf_counter()
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        # Prefer neighbourhood membership, but prefer few auxiliary edge flags
        # until the exact-cardinality constraint needs them.
        solver.set_phases(list(x.values()) + [-flag for flag in induced.values()])
        raw_status, model, solver_run = bounded_cegar_loop(
            solver,
            no_lazy_cuts,
            args.conflict_chunk,
            args.max_conflicts,
            args.per_call_seconds,
            args.max_seconds,
        )

    status = source_status(raw_status)
    result: dict[str, Any] = {
        "schema": "ramsey-second-new-basin-fixed-extension-v1",
        "status": status,
        "raw_solver_status": raw_status,
        "claim_scope": (
            "fixed 60-vertex base; one new vertex; exact triangle count and "
            "maximum triangle-edge multiplicity cap"
        ),
        "target": {"r": 3, "s": 13, "n": 61},
        "input": str(args.matrix.resolve()),
        "input_sha256": sha256(args.matrix),
        "solver": args.solver,
        "formula": {
            "neighborhood_variables": n,
            "induced_edge_indicators": len(induced),
            "triangle_count_relation": "at_most" if args.at_most else "exact",
            "triangle_count_bound": args.triangles,
            "maximum_triangle_edge_multiplicity": args.max_multiplicity,
            "preloaded_all_base_I12_clauses": blue_count,
            "preloaded_base_I12_sha256": blue_hash.hexdigest(),
            "degree_cap_clauses": degree_clause_count,
            "initial_clauses": len(clauses),
        },
        "limits": {
            "conflicts_per_call": args.conflict_chunk,
            "global_conflicts": args.max_conflicts,
            "per_call_wall_seconds": args.per_call_seconds,
            "global_wall_seconds": args.max_seconds,
        },
        "run": solver_run,
        "elapsed_seconds": time.perf_counter() - started,
    }

    if status == "SAT":
        if model is None:
            raise RuntimeError("SAT without a model")
        positive = {lit for lit in model if 0 < lit <= n}
        neighborhood = [v for v in range(n) if x[v] in positive]
        induced_edges, max_degree, degrees = selected_induced_edge_diagnostics(
            rows, neighborhood
        )
        triangle_bound_ok = (
            induced_edges <= args.triangles
            if args.at_most
            else induced_edges == args.triangles
        )
        if not triangle_bound_ok or max_degree > args.max_multiplicity:
            raise RuntimeError("SAT model violates reconstructed structural bounds")

        candidate = add_vertex(rows, neighborhood)
        triangles = triangle_tuples(candidate)
        multiplicities = triangle_edge_multiplicity(triangles)
        maximum = max(multiplicities.values(), default=0)
        full_bound_ok = (
            len(triangles) <= args.triangles
            if args.at_most
            else len(triangles) == args.triangles
        )
        if not full_bound_ok or maximum > args.max_multiplicity:
            raise RuntimeError("full reconstruction disagrees with local diagnostics")

        write_matrix(candidate, args.output)
        bitset = verify(args.output, 3, 13)
        if bitset["searches"]["forbidden_independent_set"]["exists"]:
            raise RuntimeError("preloaded I12 clauses failed to exclude an I13")
        if not bitset["searches"]["forbidden_clique"]["exists"]:
            raise RuntimeError("near miss unexpectedly has no triangle")

        result.update(
            {
                "output": str(args.output.resolve()),
                "output_sha256": sha256(args.output),
                "neighborhood": neighborhood,
                "neighborhood_size": len(neighborhood),
                "induced_old_edge_count": induced_edges,
                "selected_induced_degrees": {
                    str(v): degrees[v] for v in sorted(degrees)
                },
                "triangle_count": len(triangles),
                "triangles": [list(t) for t in triangles],
                "maximum_triangles_sharing_one_edge": maximum,
                "triangle_edge_multiplicities": {
                    f"{u},{v}": count
                    for (u, v), count in sorted(multiplicities.items())
                },
                "independent_bitset_verification": bitset,
            }
        )

    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--triangles", type=int, required=True)
    parser.add_argument(
        "--at-most",
        action="store_true",
        help="interpret --triangles as an upper bound instead of an equality",
    )
    parser.add_argument("--max-multiplicity", type=int, required=True)
    parser.add_argument("--solver", default="cadical195")
    parser.add_argument("--conflict-chunk", type=int, default=10_000)
    parser.add_argument("--max-conflicts", type=int, required=True)
    parser.add_argument("--per-call-seconds", type=float, default=10.0)
    parser.add_argument("--max-seconds", type=float, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()

    result = run(args)
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
