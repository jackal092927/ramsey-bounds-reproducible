#!/usr/bin/env python3
"""Strictly bounded searches outside the old R(3,13) k=11 hub basin.

The script exposes three independent experiments:

``seed-r3``
    Find a frozen-base-optimal ten-triangle extension of the public 60-vertex
    R(3,13) graph whose ten triangles do *not* all share one edge.

``repair-r3``
    Search the full edge-edit space around that 61-vertex seed, with arbitrary
    additions and an at-most-d budget on deletions of seed edges.

``edit-r4``
    Add a 160th vertex to the public 159-vertex R(4,15) graph while allowing at
    most d deletions among the old vertices.  No old-old additions are allowed.

Every SAT call is sliced by both a conflict budget and a timer.  Reaching a
limit is serialized as UNKNOWN, never UNSAT.  A candidate is accepted only
after reconstruction and the independent bitset verifier.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import threading
import time
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Solver

try:
    from .bounded_deletion_sat_cegar import build_variables
    from .graph_utils import add_vertex, enumerate_cliques, write_matrix
    from .verify_ramsey import CliqueTargetSearch, complement, read_matrix, verify
except ImportError:  # pragma: no cover - direct script execution
    from bounded_deletion_sat_cegar import build_variables
    from graph_utils import add_vertex, enumerate_cliques, write_matrix
    from verify_ramsey import CliqueTargetSearch, complement, read_matrix, verify


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def edge_present(rows: list[int], u: int, v: int) -> bool:
    return bool((rows[u] >> v) & 1)


def normalized_edge(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)


def triangle_tuples(rows: list[int]) -> list[tuple[int, int, int]]:
    result: list[tuple[int, int, int]] = []
    for a, b, c in itertools.combinations(range(len(rows)), 3):
        if (
            edge_present(rows, a, b)
            and edge_present(rows, a, c)
            and edge_present(rows, b, c)
        ):
            result.append((a, b, c))
    return result


def triangle_edge_multiplicity(
    triangles: Iterable[tuple[int, int, int]],
) -> Counter[tuple[int, int]]:
    counts: Counter[tuple[int, int]] = Counter()
    for triangle in triangles:
        for u, v in itertools.combinations(triangle, 2):
            counts[normalized_edge(u, v)] += 1
    return counts


def minimum_triangle_edge_hitting_set(
    triangles: list[tuple[int, int, int]],
) -> tuple[int, list[tuple[int, int]]]:
    """Exact branch-and-bound transversal for the tiny diagnostic instances."""
    edge_sets = [
        frozenset(normalized_edge(u, v) for u, v in itertools.combinations(t, 2))
        for t in triangles
    ]
    best: list[tuple[int, int]] | None = None

    def visit(remaining: list[frozenset[tuple[int, int]]], chosen: list[tuple[int, int]]) -> None:
        nonlocal best
        if not remaining:
            if best is None or len(chosen) < len(best):
                best = chosen.copy()
            return
        if best is not None and len(chosen) >= len(best):
            return
        pivot = min(remaining, key=len)
        frequencies = Counter(edge for edges in remaining for edge in edges)
        for edge in sorted(pivot, key=lambda item: (-frequencies[item], item)):
            visit([edges for edges in remaining if edge not in edges], chosen + [edge])

    visit(edge_sets, [])
    return (len(best or []), best or [])


def stats_delta(after: dict[str, int], before: dict[str, int]) -> dict[str, int]:
    return {key: after.get(key, 0) - before.get(key, 0) for key in after}


def solve_limited_once(
    solver: Solver, conflict_budget: int, wall_seconds: float
) -> tuple[bool | None, bool, float, dict[str, int]]:
    fired = threading.Event()

    def interrupt() -> None:
        fired.set()
        solver.interrupt()

    before = solver.accum_stats()
    solver.conf_budget(max(1, conflict_budget))
    timer = threading.Timer(max(0.001, wall_seconds), interrupt)
    timer.daemon = True
    timer.start()
    started = time.perf_counter()
    try:
        outcome = solver.solve_limited(expect_interrupt=True)
    finally:
        elapsed = time.perf_counter() - started
        timer.cancel()
        timer.join()
        solver.clear_interrupt()
    return outcome, fired.is_set(), elapsed, stats_delta(solver.accum_stats(), before)


def bounded_cegar_loop(
    solver: Solver,
    separate,
    conflict_chunk: int,
    max_conflicts: int,
    per_call_seconds: float,
    max_seconds: float,
) -> tuple[str, list[int] | None, dict[str, Any]]:
    """Run persistent limited SAT; ``separate(model)`` returns new clauses."""
    start = time.perf_counter()
    initial_stats = solver.accum_stats()
    calls = 0
    timer_interrupts = 0
    cegar_models = 0
    clauses_added = 0
    call_tail: list[dict[str, Any]] = []
    last_model: list[int] | None = None

    while True:
        elapsed = time.perf_counter() - start
        current = solver.accum_stats()
        conflicts = current.get("conflicts", 0) - initial_stats.get("conflicts", 0)
        if elapsed >= max_seconds:
            status = "UNKNOWN_GLOBAL_WALL_LIMIT"
            break
        if conflicts >= max_conflicts:
            status = "UNKNOWN_GLOBAL_CONFLICT_LIMIT"
            break
        outcome, timer_fired, call_elapsed, delta = solve_limited_once(
            solver,
            min(conflict_chunk, max_conflicts - conflicts),
            min(per_call_seconds, max_seconds - elapsed),
        )
        calls += 1
        timer_interrupts += int(timer_fired)
        call_tail.append(
            {
                "call": calls,
                "outcome": "SAT" if outcome is True else "UNSAT" if outcome is False else "UNKNOWN",
                "timer_interrupted": timer_fired,
                "elapsed_seconds": call_elapsed,
                "stats_delta": delta,
            }
        )
        call_tail = call_tail[-12:]
        if outcome is None:
            continue
        if outcome is False:
            status = "UNSAT"
            last_model = None
            break
        cegar_models += 1
        last_model = solver.get_model()
        new_clauses = separate(last_model)
        if not new_clauses:
            status = "SAT"
            break
        for clause in new_clauses:
            if not clause:
                raise RuntimeError("separator produced an empty clause")
            solver.add_clause(clause)
        clauses_added += len(new_clauses)

    final_stats = solver.accum_stats()
    total = stats_delta(final_stats, initial_stats)
    return status, last_model, {
        "limited_solver_calls": calls,
        "timer_interrupts": timer_interrupts,
        "cegar_models": cegar_models,
        "lazy_clauses_added": clauses_added,
        "solver_stats": total,
        "elapsed_seconds": time.perf_counter() - start,
        "call_tail": call_tail,
    }


def run_seed_r3(args: argparse.Namespace) -> dict[str, Any]:
    base_check = verify(args.matrix, 3, 13)
    if not base_check["valid_ramsey_certificate"] or base_check["vertices"] != 60:
        raise ValueError("seed-r3 requires a valid 60-vertex (3,13) graph")
    rows = read_matrix(args.matrix)
    n = len(rows)
    base_edges = [
        (u, v)
        for u, v in itertools.combinations(range(n), 2)
        if edge_present(rows, u, v)
    ]
    x = {v: v + 1 for v in range(n)}
    red = {edge: n + i + 1 for i, edge in enumerate(base_edges)}
    pool = IDPool(start_from=n + len(base_edges) + 1)
    clauses: list[list[int]] = []
    for (u, v), indicator in red.items():
        # Exact reification: indicator iff both endpoints are selected.
        clauses.append([-x[u], -x[v], indicator])
        clauses.append([-indicator, x[u]])
        clauses.append([-indicator, x[v]])
    clauses.extend(
        CardEnc.equals(
            lits=list(red.values()),
            bound=args.triangles,
            vpool=pool,
            encoding=EncType.seqcounter,
        ).clauses
    )
    # At most nine incident conflicts at every old vertex excludes a common
    # new--old edge across all ten triangles.
    for v in range(n):
        incident = [flag for edge, flag in red.items() if v in edge]
        clauses.extend(
            CardEnc.atmost(
                lits=incident,
                bound=args.triangles - 1,
                vpool=pool,
                encoding=EncType.seqcounter,
            ).clauses
        )

    comp = complement(rows)
    all_vertices = (1 << n) - 1
    preloaded_blue = 0
    preloaded_blue_hash = hashlib.sha256()
    if args.preload_blue:
        for mask in enumerate_cliques(comp, 12):
            clause = [x[v] for v in range(n) if (mask >> v) & 1]
            clauses.append(clause)
            preloaded_blue += 1
            preloaded_blue_hash.update(f"{mask:016x}\n".encode())
    separator_counts: list[int] = []
    accepted_neighborhood: list[int] | None = None

    def separate(model: list[int]) -> list[list[int]]:
        nonlocal accepted_neighborhood
        positive = {lit for lit in model if 0 < lit <= n}
        neighborhood = [v for v in range(n) if x[v] in positive]
        mask = sum(1 << v for v in neighborhood)
        missed = enumerate_cliques(
            comp,
            12,
            candidates=all_vertices ^ mask,
            limit=args.batch_size,
        )
        separator_counts.append(len(missed))
        if not missed:
            accepted_neighborhood = neighborhood
            return []
        return [
            [x[v] for v in range(n) if (witness >> v) & 1]
            for witness in missed
        ]

    start = time.perf_counter()
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        solver.set_phases(list(x.values()) + [-flag for flag in red.values()])
        status, model, run = bounded_cegar_loop(
            solver,
            separate,
            args.conflict_chunk,
            args.max_conflicts,
            args.per_call_seconds,
            args.max_seconds,
        )

    result: dict[str, Any] = {
        "schema": "ramsey-new-basin-r3-nonstar-seed-v1",
        "status": status,
        "target": {"r": 3, "s": 13, "n": 61},
        "input": str(args.matrix.resolve()),
        "input_sha256": sha256(args.matrix),
        "solver": args.solver,
        "formula": {
            "neighborhood_variables": n,
            "red_conflict_indicators": len(red),
            "triangle_bound": args.triangles,
            "per_old_vertex_triangle_degree_bound": args.triangles - 1,
            "preloaded_all_base_I12_clauses": preloaded_blue,
            "preloaded_base_I12_sha256": preloaded_blue_hash.hexdigest(),
            "initial_clauses": len(clauses),
        },
        "limits": {
            "conflicts_per_call": args.conflict_chunk,
            "global_conflicts": args.max_conflicts,
            "per_call_wall_seconds": args.per_call_seconds,
            "global_wall_seconds": args.max_seconds,
            "blue_batch_size": args.batch_size,
        },
        "run": run,
        "separator_batch_counts": separator_counts,
        "total_elapsed_seconds": time.perf_counter() - start,
    }

    if status == "SAT":
        if accepted_neighborhood is None or model is None:
            raise RuntimeError("SAT without an accepted neighborhood")
        candidate = add_vertex(rows, accepted_neighborhood)
        triangles = triangle_tuples(candidate)
        multiplicity = triangle_edge_multiplicity(triangles)
        no_common_edge = max(multiplicity.values(), default=0) < len(triangles)
        if len(triangles) != args.triangles or not no_common_edge:
            raise RuntimeError("accepted seed violated exact nonstar diagnostics")
        write_matrix(candidate, args.output)
        independent = verify(args.output, 3, 13)
        result.update(
            {
                "output": str(args.output.resolve()),
                "output_sha256": sha256(args.output),
                "neighborhood": accepted_neighborhood,
                "triangle_count": len(triangles),
                "triangles": [list(t) for t in triangles],
                "maximum_triangles_sharing_one_edge": max(multiplicity.values()),
                "all_triangles_share_one_edge": not no_common_edge,
                "independent_bitset_verification": independent,
            }
        )
        # A near miss must fail only on K3, not on I13.
        if independent["searches"]["forbidden_independent_set"]["exists"]:
            raise RuntimeError("seed contains an independent 13-set")
    return result


def rows_from_edge_model(
    model: list[int], n: int, variables: dict[tuple[int, int], int]
) -> list[int]:
    positive = {lit for lit in model if 0 < lit <= n * (n - 1) // 2}
    rows = [0] * n
    for (u, v), variable in variables.items():
        if variable in positive:
            rows[u] |= 1 << v
            rows[v] |= 1 << u
    return rows


def run_repair_r3(args: argparse.Namespace) -> dict[str, Any]:
    initial = read_matrix(args.matrix)
    n = len(initial)
    if n != 61:
        raise ValueError("repair-r3 requires a 61-vertex near miss")
    input_triangles = triangle_tuples(initial)
    hit_number, hit_witness = minimum_triangle_edge_hitting_set(input_triangles)
    variables, pairs = build_variables(n)
    original_edges = {
        edge for edge in pairs if edge_present(initial, *edge)
    }
    pool = IDPool(start_from=len(pairs) + 1)
    triangle_clause_count = n * (n - 1) * (n - 2) // 6
    clauses = [
        [-variables[(a, b)], -variables[(a, c)], -variables[(b, c)]]
        for a, b, c in itertools.combinations(range(n), 3)
    ]
    clauses.extend(
        CardEnc.atmost(
            lits=[-variables[edge] for edge in sorted(original_edges)],
            bound=args.budget,
            vpool=pool,
            encoding=EncType.seqcounter,
        ).clauses
    )
    accepted: list[int] | None = None
    witness_hash = hashlib.sha256()

    def separate(model: list[int]) -> list[list[int]]:
        nonlocal accepted
        candidate = rows_from_edge_model(model, n, variables)
        masks = enumerate_cliques(
            complement(candidate), 13, limit=args.batch_size
        )
        if not masks:
            accepted = candidate
            return []
        result = []
        for mask in masks:
            witness_hash.update(f"{mask:016x}\n".encode())
            vertices = [v for v in range(n) if (mask >> v) & 1]
            result.append(
                [variables[normalized_edge(u, v)] for u, v in itertools.combinations(vertices, 2)]
            )
        return result

    phases = [
        variables[edge] if edge in original_edges else -variables[edge]
        for edge in pairs
    ]
    start = time.perf_counter()
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        solver.set_phases(phases)
        status, model, run = bounded_cegar_loop(
            solver,
            separate,
            args.conflict_chunk,
            args.max_conflicts,
            args.per_call_seconds,
            args.max_seconds,
        )
    result: dict[str, Any] = {
        "schema": "ramsey-new-basin-r3-edit-v1",
        "status": status,
        "target": {"r": 3, "s": 13, "n": n},
        "input": str(args.matrix.resolve()),
        "input_sha256": sha256(args.matrix),
        "input_triangle_count": len(input_triangles),
        "input_triangles": [list(t) for t in input_triangles],
        "input_all_triangles_share_one_edge": (
            max(triangle_edge_multiplicity(input_triangles).values(), default=0)
            == len(input_triangles)
        ),
        "exact_triangle_edge_deletion_lower_bound": hit_number,
        "triangle_edge_hitting_witness": [list(e) for e in hit_witness],
        "solver": args.solver,
        "deletion_budget": args.budget,
        "arbitrary_old_and_new_nonedge_additions_allowed": True,
        "formula": {
            "edge_variables": len(pairs),
            "original_edges": len(original_edges),
            "triangle_clauses": triangle_clause_count,
            "initial_clause_count": len(clauses),
        },
        "limits": {
            "conflicts_per_call": args.conflict_chunk,
            "global_conflicts": args.max_conflicts,
            "per_call_wall_seconds": args.per_call_seconds,
            "global_wall_seconds": args.max_seconds,
            "blue_batch_size": args.batch_size,
        },
        "run": run,
        "lazy_witness_stream_sha256": witness_hash.hexdigest(),
        "total_elapsed_seconds": time.perf_counter() - start,
    }
    if status == "SAT":
        if accepted is None or model is None:
            raise RuntimeError("SAT without accepted graph")
        write_matrix(accepted, args.output)
        verification = verify(args.output, 3, 13)
        if not verification["valid_ramsey_certificate"]:
            raise RuntimeError("independent verifier rejected R3 candidate")
        final_edges = {
            edge for edge in pairs if edge_present(accepted, *edge)
        }
        result.update(
            {
                "output": str(args.output.resolve()),
                "output_sha256": sha256(args.output),
                "deleted_edges": [list(e) for e in sorted(original_edges - final_edges)],
                "added_edges": [list(e) for e in sorted(final_edges - original_edges)],
                "independent_bitset_verification": verification,
            }
        )
    return result


def apply_deletions(rows: list[int], deleted: set[tuple[int, int]]) -> list[int]:
    result = rows.copy()
    for u, v in deleted:
        result[u] &= ~(1 << v)
        result[v] &= ~(1 << u)
    return result


def run_edit_r4(args: argparse.Namespace) -> dict[str, Any]:
    base_check = verify(args.matrix, 4, 15)
    if not base_check["valid_ramsey_certificate"] or base_check["vertices"] != 159:
        raise ValueError("edit-r4 requires a valid 159-vertex (4,15) graph")
    base = read_matrix(args.matrix)
    n = len(base)
    base_edges = [
        edge
        for edge in itertools.combinations(range(n), 2)
        if edge_present(base, *edge)
    ]
    triangles = triangle_tuples(base)
    x = {v: v + 1 for v in range(n)}
    d = {edge: n + i + 1 for i, edge in enumerate(base_edges)}
    pool = IDPool(start_from=n + len(base_edges) + 1)
    clauses: list[list[int]] = []
    for a, b, c in triangles:
        clauses.append(
            [
                -x[a],
                -x[b],
                -x[c],
                d[normalized_edge(a, b)],
                d[normalized_edge(a, c)],
                d[normalized_edge(b, c)],
            ]
        )
    clauses.extend(
        CardEnc.atmost(
            lits=list(d.values()),
            bound=args.budget,
            vpool=pool,
            encoding=EncType.seqcounter,
        ).clauses
    )
    accepted: list[int] | None = None
    old_side_clauses = 0
    new_side_clauses = 0
    witness_hash = hashlib.sha256()

    def deleted_from_model(model: list[int]) -> set[tuple[int, int]]:
        positive = set(model)
        return {edge for edge, variable in d.items() if variable in positive}

    def deletion_block(mask: int) -> list[int]:
        vertices = [v for v in range(n) if (mask >> v) & 1]
        result: list[int] = []
        for u, v in itertools.combinations(vertices, 2):
            edge = normalized_edge(u, v)
            if edge in d:
                result.append(-d[edge])
        return result

    def separate(model: list[int]) -> list[list[int]]:
        nonlocal accepted, old_side_clauses, new_side_clauses
        positive = set(model)
        deleted = deleted_from_model(model)
        current = apply_deletions(base, deleted)
        neighborhood = [v for v in range(n) if x[v] in positive]
        neighborhood_mask = sum(1 << v for v in neighborhood)
        comp = complement(current)
        old_missed = enumerate_cliques(comp, 15, limit=args.batch_size)
        new_missed = enumerate_cliques(
            comp,
            14,
            candidates=((1 << n) - 1) ^ neighborhood_mask,
            limit=args.batch_size,
        )
        separated: list[list[int]] = []
        for mask in old_missed:
            clause = deletion_block(mask)
            if not clause:
                raise RuntimeError("original valid base unexpectedly contains I15")
            witness_hash.update(f"old:{mask:040x}\n".encode())
            separated.append(clause)
        old_side_clauses += len(old_missed)
        for mask in new_missed:
            vertices = [v for v in range(n) if (mask >> v) & 1]
            clause = [x[v] for v in vertices] + deletion_block(mask)
            witness_hash.update(f"new:{mask:040x}\n".encode())
            separated.append(clause)
        new_side_clauses += len(new_missed)
        if separated:
            return separated
        accepted = add_vertex(current, neighborhood)
        return []

    start = time.perf_counter()
    with Solver(name=args.solver, bootstrap_with=clauses) as solver:
        solver.set_phases(list(x.values()) + [-variable for variable in d.values()])
        status, model, run = bounded_cegar_loop(
            solver,
            separate,
            args.conflict_chunk,
            args.max_conflicts,
            args.per_call_seconds,
            args.max_seconds,
        )
    result: dict[str, Any] = {
        "schema": "ramsey-new-basin-r4-small-edit-v1",
        "status": status,
        "target": {"r": 4, "s": 15, "n": 160},
        "input": str(args.matrix.resolve()),
        "input_sha256": sha256(args.matrix),
        "solver": args.solver,
        "edit_family": {
            "old_old_edge_deletions_at_most": args.budget,
            "old_old_edge_additions_allowed": False,
            "new_vertex_neighborhood_free": True,
        },
        "formula": {
            "neighborhood_variables": n,
            "old_edge_deletion_variables": len(d),
            "base_triangles": len(triangles),
            "new_vertex_K4_clauses": len(triangles),
            "initial_clause_count": len(clauses),
        },
        "limits": {
            "conflicts_per_call": args.conflict_chunk,
            "global_conflicts": args.max_conflicts,
            "per_call_wall_seconds": args.per_call_seconds,
            "global_wall_seconds": args.max_seconds,
            "witness_batch_size_per_side": args.batch_size,
        },
        "run": run,
        "lazy_old_I15_clauses": old_side_clauses,
        "lazy_new_vertex_I15_clauses": new_side_clauses,
        "lazy_witness_stream_sha256": witness_hash.hexdigest(),
        "total_elapsed_seconds": time.perf_counter() - start,
    }
    if status == "SAT":
        if accepted is None or model is None:
            raise RuntimeError("SAT without accepted graph")
        write_matrix(accepted, args.output)
        verification = verify(args.output, 4, 15)
        if not verification["valid_ramsey_certificate"]:
            raise RuntimeError("independent verifier rejected R4 candidate")
        deleted = deleted_from_model(model)
        result.update(
            {
                "output": str(args.output.resolve()),
                "output_sha256": sha256(args.output),
                "deleted_old_edges": [list(edge) for edge in sorted(deleted)],
                "new_vertex_neighborhood": [
                    v for v in range(n) if x[v] in set(model)
                ],
                "independent_bitset_verification": verification,
            }
        )
    return result


def add_common_limits(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--solver", default="minisat22")
    parser.add_argument("--conflict-chunk", type=int, default=5000)
    parser.add_argument("--max-conflicts", type=int, required=True)
    parser.add_argument("--per-call-seconds", type=float, default=8.0)
    parser.add_argument("--max-seconds", type=float, required=True)
    parser.add_argument("--batch-size", type=int, default=256)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    seed = sub.add_parser("seed-r3")
    seed.add_argument("matrix", type=Path)
    seed.add_argument("--triangles", type=int, default=10)
    seed.add_argument("--preload-blue", action="store_true")
    add_common_limits(seed)

    repair = sub.add_parser("repair-r3")
    repair.add_argument("matrix", type=Path)
    repair.add_argument("--budget", type=int, required=True)
    add_common_limits(repair)

    edit = sub.add_parser("edit-r4")
    edit.add_argument("matrix", type=Path)
    edit.add_argument("--budget", type=int, required=True)
    add_common_limits(edit)

    args = parser.parse_args()
    if args.command == "seed-r3":
        result = run_seed_r3(args)
    elif args.command == "repair-r3":
        result = run_repair_r3(args)
    else:
        result = run_edit_r4(args)
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
