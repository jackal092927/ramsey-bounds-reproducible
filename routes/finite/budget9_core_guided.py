#!/usr/bin/env python3
"""Interruptible, structure-guided diagnosis of the R(3,13) budget-9 basin.

This is deliberately a diagnostic rather than an open-ended search.  It uses
two facts established outside the solver invocation:

* the 11 input triangles through edge (56, 60) force that edge to be deleted
  under a deletion budget of nine; and
* the exact d <= 8 CEGAR run is UNSAT, so any d = 9 solution must delete
  exactly nine original edges.

After fixing the hub deletion, every I_13 in that graph is installed as an
initial edge-hitting clause.  Further I_13 witnesses caused by the other eight
deletions are still separated lazily.  Each SAT call is bounded both by a
conflict budget and an interrupt timer, and the whole run has global wall and
conflict limits.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import threading
import time
from collections import Counter, deque
from pathlib import Path
from typing import Any

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Solver

try:
    from .bounded_deletion_sat_cegar import build_variables
    from .graph_utils import enumerate_cliques, write_matrix
    from .verify_ramsey import CliqueTargetSearch, complement, read_matrix, verify
except ImportError:  # pragma: no cover - direct script execution
    from bounded_deletion_sat_cegar import build_variables
    from graph_utils import enumerate_cliques, write_matrix
    from verify_ramsey import CliqueTargetSearch, complement, read_matrix, verify


def edge_present(rows: list[int], u: int, v: int) -> bool:
    return bool((rows[u] >> v) & 1)


def input_triangles(rows: list[int]) -> list[tuple[int, int, int]]:
    return [
        (a, b, c)
        for a, b, c in itertools.combinations(range(len(rows)), 3)
        if edge_present(rows, a, b)
        and edge_present(rows, a, c)
        and edge_present(rows, b, c)
    ]


def normalized_edge(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)


def forced_hub_proof(
    triangles: list[tuple[int, int, int]], hub: tuple[int, int], budget: int
) -> dict[str, Any]:
    """Return a checkable triangle-hitting proof that ``hub`` is forced off."""
    hub = normalized_edge(*hub)
    through_hub = []
    spoke_groups: list[list[tuple[int, int]]] = []
    for triangle in triangles:
        edges = {
            normalized_edge(u, v)
            for u, v in itertools.combinations(triangle, 2)
        }
        if hub in edges:
            through_hub.append(triangle)
            spoke_groups.append(sorted(edges - {hub}))

    flattened = [edge for group in spoke_groups for edge in group]
    pairwise_disjoint = len(flattened) == len(set(flattened))
    lower_bound_if_hub_kept = len(spoke_groups) if pairwise_disjoint else None
    forced = (
        lower_bound_if_hub_kept is not None
        and lower_bound_if_hub_kept > budget
    )
    return {
        "hub_edge": list(hub),
        "triangles_through_hub": [list(t) for t in through_hub],
        "triangle_count_through_hub": len(through_hub),
        "off_hub_spoke_groups": [
            [list(edge) for edge in group] for group in spoke_groups
        ],
        "off_hub_groups_pairwise_edge_disjoint": pairwise_disjoint,
        "deletion_lower_bound_if_hub_kept": lower_bound_if_hub_kept,
        "budget": budget,
        "hub_deletion_forced": forced,
        "proof": (
            "If the hub remains, each triangle through it needs a deleted "
            "spoke edge. The displayed spoke groups are pairwise disjoint."
        ),
    }


def rows_from_model(
    model: list[int], n: int, variables: dict[tuple[int, int], int]
) -> tuple[list[int], set[tuple[int, int]]]:
    positive = {lit for lit in model if 0 < lit <= n * (n - 1) // 2}
    rows = [0] * n
    edges: set[tuple[int, int]] = set()
    for (u, v), variable in variables.items():
        if variable in positive:
            rows[u] |= 1 << v
            rows[v] |= 1 << u
            edges.add((u, v))
    return rows, edges


def mask_vertices(mask: int) -> list[int]:
    return [v for v in range(mask.bit_length()) if (mask >> v) & 1]


def graph_hash(edges: set[tuple[int, int]]) -> str:
    payload = "\n".join(f"{u},{v}" for u, v in sorted(edges)).encode()
    return hashlib.sha256(payload).hexdigest()


def stats_delta(after: dict[str, int], before: dict[str, int]) -> dict[str, int]:
    return {key: after.get(key, 0) - before.get(key, 0) for key in after}


def solve_limited_once(
    solver: Solver, conflict_budget: int, wall_seconds: float
) -> tuple[bool | None, bool, float, dict[str, int]]:
    """Run one SAT slice; return result, timer-fired flag, time, stat delta."""
    fired = threading.Event()

    def interrupt() -> None:
        fired.set()
        solver.interrupt()

    before = solver.accum_stats()
    solver.conf_budget(conflict_budget)
    timer = threading.Timer(wall_seconds, interrupt)
    timer.daemon = True
    timer.start()
    started = time.perf_counter()
    try:
        result = solver.solve_limited(expect_interrupt=True)
    finally:
        elapsed = time.perf_counter() - started
        timer.cancel()
        timer.join()
        solver.clear_interrupt()
    return result, fired.is_set(), elapsed, stats_delta(solver.accum_stats(), before)


def run_diagnostic(
    initial: list[int],
    s: int,
    budget: int,
    hub: tuple[int, int],
    solver_name: str,
    conflict_chunk: int,
    max_conflicts: int,
    per_call_seconds: float,
    max_seconds: float,
    d8_record: dict[str, Any],
) -> tuple[dict[str, Any], list[int] | None]:
    start = time.perf_counter()
    n = len(initial)
    variables, pairs = build_variables(n)
    hub = normalized_edge(*hub)
    initial_edges = {
        (u, v) for u, v in pairs if edge_present(initial, u, v)
    }
    if hub not in initial_edges:
        raise ValueError(f"hub edge {hub} is not present in the input")

    triangles = input_triangles(initial)
    hub_proof = forced_hub_proof(triangles, hub, budget)
    if not hub_proof["hub_deletion_forced"]:
        raise ValueError("requested hub deletion is not proved by the input")
    if d8_record.get("status") != "UNSAT" or d8_record.get(
        "deletion_budget"
    ) != budget - 1:
        raise ValueError("the supplied prior record is not budget-(d-1) UNSAT")

    # The d<=8 result plus an at-most-nine target permits an exact-nine encoding.
    other_original_edges = sorted(initial_edges - {hub})
    deletion_literals = [-variables[edge] for edge in other_original_edges]
    pool = IDPool(start_from=len(pairs) + 1)
    exact_remaining = CardEnc.equals(
        lits=deletion_literals,
        bound=budget - 1,
        vpool=pool,
        encoding=EncType.seqcounter,
    )

    triangle_clauses = [
        [-variables[(a, b)], -variables[(a, c)], -variables[(b, c)]]
        for a, b, c in itertools.combinations(range(n), 3)
    ]

    post_hub = initial.copy()
    post_hub[hub[0]] &= ~(1 << hub[1])
    post_hub[hub[1]] &= ~(1 << hub[0])
    seed_masks = sorted(enumerate_cliques(complement(post_hub), s))
    seed_payload = "".join(f"{mask:016x}\n" for mask in seed_masks).encode()
    seed_clauses = []
    for mask in seed_masks:
        vertices = mask_vertices(mask)
        clause = [
            variables[normalized_edge(u, v)]
            for u, v in itertools.combinations(vertices, 2)
            if normalized_edge(u, v) != hub
        ]
        seed_clauses.append(clause)

    clauses = triangle_clauses + exact_remaining.clauses + [[-variables[hub]]]
    clauses.extend(seed_clauses)
    formula_ready = time.perf_counter()

    phases = [
        variable if edge_present(initial, u, v) else -variable
        for (u, v), variable in variables.items()
    ]
    phases[variables[hub] - 1] = -variables[hub]

    base_result: dict[str, Any] = {
        "schema": "ramsey-budget9-core-guided-v1",
        "status": None,
        "target": {"r": 3, "s": s, "n": n},
        "solver": solver_name,
        "deletion_budget": budget,
        "strict_structure": {
            "input_triangle_count": len(triangles),
            "input_triangles": [list(t) for t in triangles],
            "forced_hub_proof": hub_proof,
            "prior_budget_unsat": {
                "budget": d8_record["deletion_budget"],
                "status": d8_record["status"],
                "cegar_iterations": d8_record.get("cegar_iterations"),
                "independent_hitting_clauses": d8_record.get(
                    "independent_hitting_clauses"
                ),
            },
            "consequence": (
                "Any budget-9 solution deletes hub (56,60) and exactly eight "
                "other original edges."
            ),
        },
        "preseed": {
            "post_hub_independent_set_size": s,
            "witness_count": len(seed_masks),
            "witness_sha256": hashlib.sha256(seed_payload).hexdigest(),
            "all_witnesses_contain_hub_endpoints": all(
                (mask >> hub[0]) & 1 and (mask >> hub[1]) & 1
                for mask in seed_masks
            ),
            "clause_length_without_fixed_hub": (
                len(seed_clauses[0]) if seed_clauses else None
            ),
        },
        "formula": {
            "edge_variables": len(pairs),
            "original_edges": len(initial_edges),
            "triangle_clauses": len(triangle_clauses),
            "exact_eight_nonhub_deletion_clauses": len(exact_remaining.clauses),
            "cardinality_aux_variables": exact_remaining.nv - len(pairs),
            "forced_hub_unit_clauses": 1,
            "preseed_hitting_clauses": len(seed_clauses),
            "initial_clause_count": len(clauses),
            "formula_build_seconds": formula_ready - start,
        },
        "limits": {
            "conflicts_per_call": conflict_chunk,
            "global_conflicts": max_conflicts,
            "per_call_wall_seconds": per_call_seconds,
            "global_wall_seconds": max_seconds,
        },
    }

    calls = 0
    timer_interrupts = 0
    budget_exhaustions = 0
    cegar_models = 0
    lazy_witnesses = 0
    witness_hasher = hashlib.sha256()
    deletion_frequency: Counter[tuple[int, int]] = Counter()
    addition_counts: list[int] = []
    first_samples: list[dict[str, Any]] = []
    last_samples: deque[dict[str, Any]] = deque(maxlen=8)
    call_tail: deque[dict[str, Any]] = deque(maxlen=12)
    candidate_rows: list[int] | None = None

    with Solver(name=solver_name, bootstrap_with=clauses) as solver:
        solver.set_phases(phases)
        initial_stats = solver.accum_stats()

        while True:
            elapsed = time.perf_counter() - start
            stats = solver.accum_stats()
            used_conflicts = stats.get("conflicts", 0) - initial_stats.get(
                "conflicts", 0
            )
            if elapsed >= max_seconds:
                status = "UNKNOWN_GLOBAL_WALL_LIMIT"
                break
            if used_conflicts >= max_conflicts:
                status = "UNKNOWN_GLOBAL_CONFLICT_LIMIT"
                break

            slice_conflicts = min(conflict_chunk, max_conflicts - used_conflicts)
            slice_wall = min(per_call_seconds, max_seconds - elapsed)
            outcome, timer_fired, call_elapsed, delta = solve_limited_once(
                solver, slice_conflicts, slice_wall
            )
            calls += 1
            timer_interrupts += int(timer_fired)
            budget_exhaustions += int(outcome is None and not timer_fired)
            call_tail.append(
                {
                    "call": calls,
                    "outcome": (
                        "SAT" if outcome is True else "UNSAT" if outcome is False else "UNKNOWN"
                    ),
                    "timer_interrupted": timer_fired,
                    "elapsed_seconds": call_elapsed,
                    "stats_delta": delta,
                }
            )

            if outcome is None:
                continue
            if outcome is False:
                status = "UNSAT"
                break

            cegar_models += 1
            candidate_rows, final_edges = rows_from_model(
                solver.get_model(), n, variables
            )
            deleted = sorted(initial_edges - final_edges)
            added = sorted(final_edges - initial_edges)
            if hub not in deleted or len(deleted) != budget:
                raise RuntimeError(
                    "solver model violated the forced-hub/exact-budget encoding"
                )
            for edge in deleted:
                deletion_frequency[edge] += 1
            addition_counts.append(len(added))

            missed = CliqueTargetSearch(complement(candidate_rows), s).run()
            sample = {
                "cegar_model": cegar_models,
                "graph_sha256": graph_hash(final_edges),
                "deleted_edges": [list(edge) for edge in deleted],
                "added_edge_count": len(added),
                "contains_I13": missed.exists,
                "I13_witness": missed.witness,
            }
            if len(first_samples) < 8:
                first_samples.append(sample)
            last_samples.append(sample)

            if not missed.exists:
                status = "SAT"
                break

            witness = missed.witness or []
            witness_hasher.update(
                (",".join(str(v) for v in witness) + "\n").encode()
            )
            solver.add_clause(
                [
                    variables[normalized_edge(u, v)]
                    for u, v in itertools.combinations(witness, 2)
                ]
            )
            lazy_witnesses += 1
            candidate_rows = None

        final_stats = solver.accum_stats()
        final_var_count = solver.nof_vars()
        final_clause_count = solver.nof_clauses()

    elapsed_total = time.perf_counter() - start
    empirical = {
        "cegar_sat_models": cegar_models,
        "lazy_I13_clauses_added": lazy_witnesses,
        "lazy_witness_sequence_sha256": witness_hasher.hexdigest(),
        "sampled_model_deletion_edge_frequency": [
            {"edge": list(edge), "models": count}
            for edge, count in sorted(
                deletion_frequency.items(), key=lambda item: (-item[1], item[0])
            )
        ],
        "sampled_model_addition_count_range": (
            [min(addition_counts), max(addition_counts)]
            if addition_counts
            else None
        ),
        "first_model_samples": first_samples,
        "last_model_samples": list(last_samples),
        "caution": (
            "Frequencies and model samples are heuristic observations, not "
            "logical necessity claims."
        ),
    }
    base_result.update(
        {
            "status": status,
            "progress": {
                "limited_solve_calls": calls,
                "conflict_budget_exhaustions": budget_exhaustions,
                "timer_interruptions": timer_interrupts,
                "solver_stats": stats_delta(final_stats, initial_stats),
                "last_call_summaries": list(call_tail),
                "final_solver_variables": final_var_count,
                "final_solver_clauses": final_clause_count,
                "elapsed_seconds": elapsed_total,
            },
            "empirical_search_structure": empirical,
            "claim_boundary": (
                "SAT is a candidate pending independent verification; UNSAT is "
                "exact for this deletion basin; UNKNOWN changes no Ramsey bound."
            ),
        }
    )
    return base_result, candidate_rows if status == "SAT" else None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--d8-json", type=Path, required=True)
    parser.add_argument("--s", type=int, default=13)
    parser.add_argument("--budget", type=int, default=9)
    parser.add_argument("--hub", type=int, nargs=2, default=(56, 60))
    parser.add_argument("--solver", default="minisat22")
    parser.add_argument("--conflicts-per-call", type=int, default=5000)
    parser.add_argument("--max-conflicts", type=int, default=500000)
    parser.add_argument("--per-call-seconds", type=float, default=8.0)
    parser.add_argument("--max-seconds", type=float, default=240.0)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()

    input_bytes = args.matrix.read_bytes()
    d8_bytes = args.d8_json.read_bytes()
    d8_record = json.loads(d8_bytes)
    input_sha = hashlib.sha256(input_bytes).hexdigest()
    if d8_record.get("input_sha256") != input_sha:
        raise ValueError("d8 record and matrix SHA256 do not match")

    result, candidate = run_diagnostic(
        read_matrix(args.matrix),
        args.s,
        args.budget,
        tuple(args.hub),
        args.solver,
        args.conflicts_per_call,
        args.max_conflicts,
        args.per_call_seconds,
        args.max_seconds,
        d8_record,
    )
    result["provenance"] = {
        "input": str(args.matrix),
        "input_sha256": input_sha,
        "prior_d8_record": str(args.d8_json),
        "prior_d8_record_sha256": hashlib.sha256(d8_bytes).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }

    if candidate is not None:
        if args.output is None:
            raise ValueError("SAT requires --output for independent verification")
        write_matrix(candidate, args.output)
        result["candidate"] = {
            "path": str(args.output),
            "sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
            "independent_bitset_verification": verify(args.output, 3, args.s),
        }
    else:
        result["candidate"] = None

    rendered = json.dumps(result, indent=2, sort_keys=True)
    args.json.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
