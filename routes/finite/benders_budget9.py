#!/usr/bin/env python3
"""Interruptible Benders search in the forced-hub R(3,13) budget-9 basin.

The base graph ``H`` is the input graph after deleting the already-proved
forced hub.  A master assignment chooses exactly eight further edges of H to
delete.  For every original nonedge f={u,v}, an auxiliary master literal y_f
may be true only when those deletions hit every common-neighbour spoke pair

    {{u,w}, {v,w}}  for w in N_H(u) intersect N_H(v).

Thus y_f certifies that adding f cannot by itself close a triangle with two
retained base edges.  If X is a 13-set, the following is a valid master cut:

    OR_{e in E_H(X)} not d_e   OR   OR_{f in nonedges_H(X)} y_f.       (1)

Indeed, when all base edges in X are deleted, every feasible final graph must
add an edge f inside X; triangle-freeness makes that f locally eligible, hence
its y_f is allowed.  Cuts (1) are separated from I_13 witnesses in the graph
of retained base edges plus selected y_f edges.

Once the local relaxation passes, a fixed-deletion add-only SAT subproblem
checks collective triangle constraints exactly.  Importantly, an original
edge selected for deletion is fixed false and is *not* an add-variable.  A
proved subproblem UNSAT yields a strict master no-good.  A bounded UNKNOWN may
optionally be excluded for candidate exploration, but such heuristic no-goods
are tracked separately and can never support a basin-UNSAT claim.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import time
from collections import Counter, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Solver

try:
    from .budget9_core_guided import (
        edge_present,
        forced_hub_proof,
        input_triangles,
        normalized_edge,
        solve_limited_once,
    )
    from .graph_utils import enumerate_cliques, write_matrix
    from .verify_ramsey import complement, read_matrix, verify
except ImportError:  # pragma: no cover - direct script execution
    from budget9_core_guided import (
        edge_present,
        forced_hub_proof,
        input_triangles,
        normalized_edge,
        solve_limited_once,
    )
    from graph_utils import enumerate_cliques, write_matrix
    from verify_ramsey import complement, read_matrix, verify


Edge = tuple[int, int]


def flip_off(rows: list[int], edge: Edge) -> None:
    u, v = edge
    rows[u] &= ~(1 << v)
    rows[v] &= ~(1 << u)


def flip_on(rows: list[int], edge: Edge) -> None:
    u, v = edge
    rows[u] |= 1 << v
    rows[v] |= 1 << u


def vertices(mask: int) -> list[int]:
    return [v for v in range(mask.bit_length()) if (mask >> v) & 1]


def edge_set(rows: list[int]) -> set[Edge]:
    return {
        (u, v)
        for u, v in itertools.combinations(range(len(rows)), 2)
        if edge_present(rows, u, v)
    }


def graph_hash(rows: list[int]) -> str:
    payload = "\n".join(
        f"{u},{v}" for u, v in sorted(edge_set(rows))
    ).encode()
    return hashlib.sha256(payload).hexdigest()


def fixed_deletion_addition_pairs(
    base_rows: list[int], deleted: Iterable[Edge], fixed_absent: Iterable[Edge] = ()
) -> list[Edge]:
    """Return original nonedges only; deleted original edges stay fixed false."""
    deleted_set = {normalized_edge(*edge) for edge in deleted}
    fixed_set = {normalized_edge(*edge) for edge in fixed_absent}
    pairs: list[Edge] = []
    for edge in itertools.combinations(range(len(base_rows)), 2):
        if edge in fixed_set or edge in deleted_set:
            continue
        if not edge_present(base_rows, *edge):
            pairs.append(edge)
    return pairs


def locally_eligible(
    base_rows: list[int], deleted: set[Edge], addition: Edge
) -> bool:
    """Necessary and sufficient for one addition not to close a base triangle."""
    u, v = addition
    common = base_rows[u] & base_rows[v]
    while common:
        bit = common & -common
        common ^= bit
        w = bit.bit_length() - 1
        if normalized_edge(u, w) not in deleted and normalized_edge(v, w) not in deleted:
            return False
    return True


def two_addition_deletion_lower_bound(
    first: list[tuple[Edge, Edge]], second: list[tuple[Edge, Edge]]
) -> int:
    """Exact joint deletion cost for two local-eligibility requirement sets.

    Each requirement set is a matching on deletion-edge variables.  Their
    union therefore has maximum degree two and only path/even-cycle
    components.  A component on q vertices has minimum vertex cover floor(q/2).
    """
    requirement_edges = {
        tuple(sorted((left, right))) for left, right in first + second
    }
    adjacency: dict[Edge, set[Edge]] = {}
    for left, right in requirement_edges:
        adjacency.setdefault(left, set()).add(right)
        adjacency.setdefault(right, set()).add(left)
    if any(len(neighbors) > 2 for neighbors in adjacency.values()):
        raise AssertionError("union of two requirement matchings has degree > 2")
    seen: set[Edge] = set()
    cover = 0
    for root in adjacency:
        if root in seen:
            continue
        stack = [root]
        seen.add(root)
        component_vertices = 0
        degree_sum = 0
        while stack:
            current = stack.pop()
            component_vertices += 1
            degree_sum += len(adjacency[current])
            for neighbor in adjacency[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        component_edges = degree_sum // 2
        if component_edges == component_vertices and component_vertices % 2:
            raise AssertionError("odd cycle cannot be a union of two matchings")
        cover += component_vertices // 2
    return cover


def conditional_cut_truth(
    base_rows: list[int],
    deleted: set[Edge],
    selected_eligible: set[Edge],
    subset: Iterable[int],
    fixed_absent: Iterable[Edge] = (),
) -> bool:
    """Semantic truth value of cut (1), used by the small-graph oracle."""
    fixed_set = {normalized_edge(*edge) for edge in fixed_absent}
    for edge in itertools.combinations(sorted(subset), 2):
        if edge_present(base_rows, *edge) and edge not in deleted:
            return True
        if (
            not edge_present(base_rows, *edge)
            and edge not in fixed_set
            and edge in selected_eligible
        ):
            return True
    return False


@dataclass
class EnumerationResult:
    witnesses: list[int]
    complete: bool
    reason: str
    recursive_nodes: int
    elapsed_seconds: float


def enumerate_cliques_interruptible(
    adjacency: list[int],
    size: int,
    max_witnesses: int,
    max_nodes: int,
    max_seconds: float,
) -> EnumerationResult:
    """Enumerate a bounded batch; ``complete`` proves absence after exhaustion."""
    started = time.perf_counter()
    found: list[int] = []
    nodes = 0
    stopped = False
    reason = "EXHAUSTED"

    def visit(prefix: int, remaining: int, need: int) -> None:
        nonlocal nodes, stopped, reason
        if stopped:
            return
        nodes += 1
        if nodes > max_nodes:
            stopped = True
            reason = "NODE_LIMIT"
            return
        if nodes & 1023 == 0 and time.perf_counter() - started >= max_seconds:
            stopped = True
            reason = "WALL_LIMIT"
            return
        if need == 0:
            found.append(prefix)
            if len(found) >= max_witnesses:
                stopped = True
                reason = "WITNESS_LIMIT"
            return
        while not stopped and remaining.bit_count() >= need:
            bit = remaining & -remaining
            remaining ^= bit
            v = bit.bit_length() - 1
            visit(prefix | bit, remaining & adjacency[v], need - 1)

    visit(0, (1 << len(adjacency)) - 1, size)
    return EnumerationResult(
        witnesses=found,
        complete=not stopped,
        reason=reason,
        recursive_nodes=nodes,
        elapsed_seconds=time.perf_counter() - started,
    )


def triangle_witness(rows: list[int]) -> list[int] | None:
    for a in range(len(rows)):
        common = rows[a]
        while common:
            bbit = common & -common
            common ^= bbit
            b = bbit.bit_length() - 1
            if b <= a:
                continue
            tail = rows[a] & rows[b] & ~((1 << (b + 1)) - 1)
            if tail:
                c = (tail & -tail).bit_length() - 1
                return [a, b, c]
    return None


def fixed_deletion_repair(
    base_rows: list[int],
    deleted: set[Edge],
    fixed_absent: set[Edge],
    s: int,
    seed_masks: list[int],
    solver_name: str,
    conflict_chunk: int,
    max_conflicts: int,
    per_call_seconds: float,
    max_seconds: float,
    oracle_nodes: int,
    oracle_seconds: float,
    preferred_additions: set[Edge] | None = None,
) -> tuple[dict[str, Any], list[int] | None]:
    """Exact add-only subproblem for a fixed deletion set, with bounded calls."""
    started = time.perf_counter()
    n = len(base_rows)
    deleted = {normalized_edge(*edge) for edge in deleted}
    fixed_absent = {normalized_edge(*edge) for edge in fixed_absent}
    post_delete = base_rows.copy()
    for edge in deleted:
        if not edge_present(base_rows, *edge):
            raise ValueError(f"cannot delete base nonedge {edge}")
        flip_off(post_delete, edge)

    addition_pairs = fixed_deletion_addition_pairs(
        base_rows, deleted, fixed_absent
    )
    variables = {edge: i + 1 for i, edge in enumerate(addition_pairs)}
    triangle_clauses: list[list[int]] = []
    for triple in itertools.combinations(range(n), 3):
        literals: list[int] = []
        impossible = False
        for edge in itertools.combinations(triple, 2):
            if edge_present(base_rows, *edge):
                if edge in deleted:
                    impossible = True
                    break
            elif edge in fixed_absent:
                impossible = True
                break
            else:
                literals.append(-variables[edge])
        if not impossible:
            if not literals:
                raise AssertionError(f"base graph has retained triangle {triple}")
            triangle_clauses.append(literals)

    seed_clauses: list[list[int]] = []
    for mask in seed_masks:
        clause = [
            variables[edge]
            for edge in itertools.combinations(vertices(mask), 2)
            if edge in variables
        ]
        seed_clauses.append(clause)

    calls = conflicts = timer_interrupts = cegar_models = lazy = 0
    oracle_nodes_total = 0
    oracle_wall_total = 0.0
    candidate: list[int] | None = None
    status = "UNKNOWN_INTERNAL"
    tail: deque[dict[str, Any]] = deque(maxlen=8)
    with Solver(
        name=solver_name, bootstrap_with=triangle_clauses + seed_clauses
    ) as solver:
        phases = []
        preferred = preferred_additions or set()
        for edge, variable in variables.items():
            phases.append(variable if edge in preferred else -variable)
        solver.set_phases(phases)
        initial_stats = solver.accum_stats()
        while True:
            elapsed = time.perf_counter() - started
            used = solver.accum_stats().get("conflicts", 0) - initial_stats.get(
                "conflicts", 0
            )
            if elapsed >= max_seconds:
                status = "UNKNOWN_WALL_LIMIT"
                break
            if used >= max_conflicts:
                status = "UNKNOWN_CONFLICT_LIMIT"
                break
            outcome, fired, call_elapsed, delta = solve_limited_once(
                solver,
                min(conflict_chunk, max_conflicts - used),
                min(per_call_seconds, max_seconds - elapsed),
            )
            calls += 1
            timer_interrupts += int(fired)
            tail.append(
                {
                    "outcome": "SAT" if outcome is True else "UNSAT" if outcome is False else "UNKNOWN",
                    "timer_interrupted": fired,
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
            positive = {lit for lit in solver.get_model() if lit > 0}
            candidate = post_delete.copy()
            selected: list[Edge] = []
            for edge, variable in variables.items():
                if variable in positive:
                    flip_on(candidate, edge)
                    selected.append(edge)
            search = enumerate_cliques_interruptible(
                complement(candidate), s, 1, oracle_nodes, oracle_seconds
            )
            oracle_nodes_total += search.recursive_nodes
            oracle_wall_total += search.elapsed_seconds
            if search.witnesses:
                witness = vertices(search.witnesses[0])
                clause = [
                    variables[edge]
                    for edge in itertools.combinations(witness, 2)
                    if edge in variables
                ]
                solver.add_clause(clause)
                lazy += 1
                candidate = None
                continue
            if not search.complete:
                status = f"UNKNOWN_ORACLE_{search.reason}"
                candidate = None
                break
            status = "SAT"
            break
        final_stats = solver.accum_stats()
        conflicts = final_stats.get("conflicts", 0) - initial_stats.get(
            "conflicts", 0
        )

    result = {
        "status": status,
        "deleted_edges": [list(edge) for edge in sorted(deleted)],
        "addition_variables": len(variables),
        "deleted_original_edges_are_addition_variables": any(
            edge in variables for edge in deleted
        ),
        "triangle_clauses": len(triangle_clauses),
        "seed_I13_clauses": len(seed_clauses),
        "cegar_models": cegar_models,
        "lazy_I13_clauses": lazy,
        "limited_calls": calls,
        "timer_interruptions": timer_interrupts,
        "conflicts": conflicts,
        "oracle_recursive_nodes": oracle_nodes_total,
        "oracle_elapsed_seconds": oracle_wall_total,
        "last_calls": list(tail),
        "elapsed_seconds": time.perf_counter() - started,
    }
    if candidate is not None:
        final = edge_set(candidate)
        result["added_edges"] = [
            list(edge) for edge in sorted(final - edge_set(post_delete))
        ]
        result["candidate_graph_sha256"] = graph_hash(candidate)
    return result, candidate if status == "SAT" else None


def make_conditional_clause(
    mask: int,
    base_rows: list[int],
    dvars: dict[Edge, int],
    yvars: dict[Edge, int],
) -> list[int]:
    clause: list[int] = []
    for edge in itertools.combinations(vertices(mask), 2):
        if edge_present(base_rows, *edge):
            clause.append(-dvars[edge])
        elif edge in yvars:
            clause.append(yvars[edge])
    return clause


def master_support(
    base_rows: list[int], deleted: set[Edge], selected_y: set[Edge]
) -> list[int]:
    rows = base_rows.copy()
    for edge in deleted:
        flip_off(rows, edge)
    for edge in selected_y:
        flip_on(rows, edge)
    return rows


def run_benders(
    initial: list[int],
    d8_record: dict[str, Any],
    s: int,
    budget: int,
    hub: Edge,
    solver_name: str,
    master_conflict_chunk: int,
    master_max_conflicts: int,
    master_per_call_seconds: float,
    max_seconds: float,
    max_iterations: int,
    cuts_per_iteration: int,
    oracle_nodes: int,
    oracle_seconds: float,
    subsolver_name: str,
    sub_conflict_chunk: int,
    sub_max_conflicts: int,
    sub_per_call_seconds: float,
    sub_max_seconds: float,
    explore_unknown: bool,
    resume_cut_masks: list[int] | None = None,
    pairwise_incompatibility_cuts: bool = True,
) -> tuple[dict[str, Any], list[int] | None]:
    started = time.perf_counter()
    n = len(initial)
    hub = normalized_edge(*hub)
    proof = forced_hub_proof(input_triangles(initial), hub, budget)
    if not proof["hub_deletion_forced"]:
        raise ValueError("hub deletion was not established")
    if d8_record.get("status") != "UNSAT" or d8_record.get("deletion_budget") != budget - 1:
        raise ValueError("prior budget-(d-1) record is not exact UNSAT")

    base = initial.copy()
    flip_off(base, hub)
    base_edges = sorted(edge_set(base))
    addition_pairs = fixed_deletion_addition_pairs(base, set(), {hub})
    dvars = {edge: i + 1 for i, edge in enumerate(base_edges)}
    yvars = {
        edge: len(dvars) + i + 1 for i, edge in enumerate(addition_pairs)
    }
    pool = IDPool(start_from=len(dvars) + len(yvars) + 1)
    exact = CardEnc.equals(
        lits=list(dvars.values()),
        bound=budget - 1,
        vpool=pool,
        encoding=EncType.seqcounter,
    )
    clauses = list(exact.clauses)
    eligibility_clause_count = 0
    eligibility_requirements: dict[Edge, list[tuple[Edge, Edge]]] = {}
    for (u, v), yvar in yvars.items():
        requirements: list[tuple[Edge, Edge]] = []
        common = base[u] & base[v]
        while common:
            bit = common & -common
            common ^= bit
            w = bit.bit_length() - 1
            first, second = normalized_edge(u, w), normalized_edge(v, w)
            requirements.append((first, second))
            clauses.append([-yvar, dvars[first], dvars[second]])
            eligibility_clause_count += 1
        eligibility_requirements[(u, v)] = requirements

    pairwise_count = 0
    pairwise_hasher = hashlib.sha256()
    if pairwise_incompatibility_cuts:
        additions = sorted(yvars)
        residual_budget = budget - 1
        for i, first in enumerate(additions):
            first_requirements = eligibility_requirements[first]
            for second in additions[i + 1 :]:
                if two_addition_deletion_lower_bound(
                    first_requirements, eligibility_requirements[second]
                ) > residual_budget:
                    clauses.append([-yvars[first], -yvars[second]])
                    pairwise_count += 1
                    pairwise_hasher.update(
                        f"{first[0]},{first[1]}:{second[0]},{second[1]}\n".encode()
                    )

    seed_masks = sorted(enumerate_cliques(complement(base), s))
    seed_payload = "".join(f"{mask:016x}\n" for mask in seed_masks).encode()
    clause_masks: set[int] = set(resume_cut_masks or [])
    clause_hasher = hashlib.sha256()
    for mask in sorted(clause_masks):
        clauses.append(make_conditional_clause(mask, base, dvars, yvars))
        clause_hasher.update(f"{mask:016x}\n".encode())
    imported_cuts = len(clause_masks)
    strict_no_goods = 0
    heuristic_no_goods = 0
    strict_no_good_sets: list[list[list[int]]] = []
    heuristic_excluded_sets: list[list[list[int]]] = []
    master_iterations = 0
    separated_cuts = 0
    master_calls = 0
    master_timer_interrupts = 0
    master_initial_stats: dict[str, int]
    oracle_nodes_total = 0
    oracle_wall_total = 0.0
    subproblem_statuses: Counter[str] = Counter()
    deletion_frequency: Counter[Edge] = Counter()
    samples: deque[dict[str, Any]] = deque(maxlen=12)
    strongest_oracle = {
        "max_batch_witnesses": 0,
        "max_recursive_nodes": 0,
        "max_elapsed_seconds": 0.0,
    }
    candidate: list[int] | None = None
    proof_complete = True
    status = "UNKNOWN_INTERNAL"
    last_subproblem: dict[str, Any] | None = None

    with Solver(name=solver_name, bootstrap_with=clauses) as master:
        # Sparse y is a useful initial direction; cuts force only shared repairs.
        master.set_phases(
            [-var for var in yvars.values()] + [-var for var in dvars.values()]
        )
        master_initial_stats = master.accum_stats()
        while True:
            total_elapsed = time.perf_counter() - started
            master_conflicts = master.accum_stats().get(
                "conflicts", 0
            ) - master_initial_stats.get("conflicts", 0)
            if total_elapsed >= max_seconds:
                status = "UNKNOWN_GLOBAL_WALL_LIMIT"
                break
            if master_iterations >= max_iterations:
                status = "UNKNOWN_ITERATION_LIMIT"
                break
            if master_conflicts >= master_max_conflicts:
                status = "UNKNOWN_MASTER_CONFLICT_LIMIT"
                break

            outcome, fired, _, _ = solve_limited_once(
                master,
                min(master_conflict_chunk, master_max_conflicts - master_conflicts),
                min(master_per_call_seconds, max_seconds - total_elapsed),
            )
            master_calls += 1
            master_timer_interrupts += int(fired)
            if outcome is None:
                continue
            if outcome is False:
                if heuristic_no_goods:
                    status = "UNKNOWN_MASTER_UNSAT_WITH_HEURISTIC_EXCLUSIONS"
                    proof_complete = False
                else:
                    status = "UNSAT"
                break

            master_iterations += 1
            positive = {lit for lit in master.get_model() if lit > 0}
            deleted = {edge for edge, var in dvars.items() if var in positive}
            selected_y = {edge for edge, var in yvars.items() if var in positive}
            if len(deleted) != budget - 1:
                raise RuntimeError("master violated exact residual deletion budget")
            if any(
                not locally_eligible(base, deleted, edge) for edge in selected_y
            ):
                raise RuntimeError("master selected a falsely eligible addition")
            for edge in deleted:
                deletion_frequency[edge] += 1

            support = master_support(base, deleted, selected_y)
            search = enumerate_cliques_interruptible(
                complement(support),
                s,
                cuts_per_iteration,
                oracle_nodes,
                oracle_seconds,
            )
            oracle_nodes_total += search.recursive_nodes
            oracle_wall_total += search.elapsed_seconds
            strongest_oracle["max_batch_witnesses"] = max(
                strongest_oracle["max_batch_witnesses"], len(search.witnesses)
            )
            strongest_oracle["max_recursive_nodes"] = max(
                strongest_oracle["max_recursive_nodes"], search.recursive_nodes
            )
            strongest_oracle["max_elapsed_seconds"] = max(
                strongest_oracle["max_elapsed_seconds"], search.elapsed_seconds
            )
            new_masks = [mask for mask in search.witnesses if mask not in clause_masks]
            sample = {
                "iteration": master_iterations,
                "deleted_edges": [list(edge) for edge in sorted(deleted)],
                "selected_eligible_additions": len(selected_y),
                "oracle_witnesses": len(search.witnesses),
                "new_cuts": len(new_masks),
                "oracle_complete": search.complete,
                "oracle_reason": search.reason,
                "oracle_nodes": search.recursive_nodes,
            }
            samples.append(sample)
            if new_masks:
                for mask in new_masks:
                    master.add_clause(make_conditional_clause(mask, base, dvars, yvars))
                    clause_masks.add(mask)
                    clause_hasher.update(f"{mask:016x}\n".encode())
                separated_cuts += len(new_masks)
                continue
            if search.witnesses:
                raise RuntimeError("separator returned only already-installed violated cuts")
            if not search.complete:
                status = f"UNKNOWN_MASTER_ORACLE_{search.reason}"
                break

            # The selected local support is already alpha<s.  It is a final
            # candidate if collective additions are also triangle-free.
            if triangle_witness(support) is None:
                candidate = support
                status = "SAT"
                sample["resolution"] = "MASTER_SUPPORT_IS_CANDIDATE"
                break

            remaining = max_seconds - (time.perf_counter() - started)
            if remaining <= 0:
                status = "UNKNOWN_GLOBAL_WALL_LIMIT"
                break
            last_subproblem, repaired = fixed_deletion_repair(
                base,
                deleted,
                {hub},
                s,
                seed_masks,
                subsolver_name,
                sub_conflict_chunk,
                sub_max_conflicts,
                sub_per_call_seconds,
                min(sub_max_seconds, remaining),
                oracle_nodes,
                oracle_seconds,
                selected_y,
            )
            subproblem_statuses[last_subproblem["status"]] += 1
            sample["subproblem_status"] = last_subproblem["status"]
            if repaired is not None:
                candidate = repaired
                status = "SAT"
                break
            if last_subproblem["status"] == "UNSAT":
                master.add_clause([-dvars[edge] for edge in sorted(deleted)])
                strict_no_goods += 1
                strict_no_good_sets.append(
                    [list(edge) for edge in sorted(deleted)]
                )
                sample["resolution"] = "STRICT_FIXED_D_NO_GOOD"
                continue

            proof_complete = False
            if explore_unknown:
                master.add_clause([-dvars[edge] for edge in sorted(deleted)])
                heuristic_no_goods += 1
                heuristic_excluded_sets.append(
                    [list(edge) for edge in sorted(deleted)]
                )
                sample["resolution"] = "HEURISTIC_UNKNOWN_NO_GOOD"
                continue
            status = f"UNKNOWN_SUBPROBLEM_{last_subproblem['status']}"
            break

        final_stats = master.accum_stats()

    result: dict[str, Any] = {
        "schema": "ramsey-r3-13-benders-budget9-v1",
        "status": status,
        "proof_complete": proof_complete and heuristic_no_goods == 0,
        "target": {"r": 3, "s": s, "n": n},
        "claim_boundary": (
            "SAT is reported only after independent matrix verification; exact "
            "UNSAT is possible only without heuristic UNKNOWN exclusions; all "
            "resource-limit outcomes preserve UNKNOWN."
        ),
        "structure": {
            "forced_hub_proof": proof,
            "residual_deletion_budget": budget - 1,
            "base_edges_after_hub": len(base_edges),
            "addition_pairs_original_nonedges_only": len(addition_pairs),
            "deleted_original_edges_may_be_readded": False,
            "seed_I13_count": len(seed_masks),
            "seed_I13_sha256": hashlib.sha256(seed_payload).hexdigest(),
        },
        "master": {
            "solver": solver_name,
            "deletion_variables": len(dvars),
            "eligible_addition_selectors": len(yvars),
            "cardinality_aux_variables": exact.nv - len(dvars) - len(yvars),
            "exact_budget_clauses": len(exact.clauses),
            "local_eligibility_clauses": eligibility_clause_count,
            "pairwise_incompatible_addition_cuts": pairwise_count,
            "pairwise_incompatibility_stream_sha256": pairwise_hasher.hexdigest(),
            "iterations": master_iterations,
            "limited_calls": master_calls,
            "timer_interruptions": master_timer_interrupts,
            "imported_conditional_I13_cuts": imported_cuts,
            "new_conditional_I13_cuts": separated_cuts,
            "strict_conditional_I13_cuts": len(clause_masks),
            "conditional_cut_stream_sha256": clause_hasher.hexdigest(),
            "unique_conditional_cut_masks": len(clause_masks),
            "strict_fixed_deletion_no_goods": strict_no_goods,
            "strict_fixed_deletion_no_good_sets": strict_no_good_sets,
            "heuristic_unknown_no_goods": heuristic_no_goods,
            "heuristic_unknown_excluded_sets": heuristic_excluded_sets,
            "solver_stats": {
                key: final_stats.get(key, 0) - master_initial_stats.get(key, 0)
                for key in final_stats
            },
        },
        "oracle": {
            "recursive_nodes_total": oracle_nodes_total,
            "elapsed_seconds_total": oracle_wall_total,
            "strongest_single_iteration": strongest_oracle,
        },
        "reusable_strict_cuts": {
            "mask_encoding": (
                "Each 16-hex-digit mask is a vertex subset X. Reconstruct cut "
                "OR_{e in E_H(X)} -d_e OR_{f in nonedges_H(X), f != hub} y_f."
            ),
            "conditional_I13_masks_hex": [
                f"{mask:016x}" for mask in sorted(clause_masks)
            ],
            "pairwise_rule": (
                "For additions f,g, form the union of common-neighbor spoke-pair "
                "requirements. Add (-y_f OR -y_g) when its exact minimum vertex "
                "cover exceeds the residual deletion budget."
            ),
        },
        "subproblems": {
            "status_counts": dict(subproblem_statuses),
            "last": last_subproblem,
        },
        "empirical": {
            "last_master_candidates": list(samples),
            "deletion_frequency": [
                {"edge": list(edge), "master_models": count}
                for edge, count in deletion_frequency.most_common(40)
            ],
            "caution": "Candidate frequencies and heuristic UNKNOWN no-goods are not logical necessity claims.",
        },
        "limits": {
            "global_wall_seconds": max_seconds,
            "master_iterations": max_iterations,
            "master_conflicts": master_max_conflicts,
            "master_conflicts_per_call": master_conflict_chunk,
            "master_per_call_seconds": master_per_call_seconds,
            "cuts_per_iteration": cuts_per_iteration,
            "oracle_nodes_per_call": oracle_nodes,
            "oracle_seconds_per_call": oracle_seconds,
            "subproblem_conflicts": sub_max_conflicts,
            "subproblem_conflicts_per_call": sub_conflict_chunk,
            "subproblem_per_call_seconds": sub_per_call_seconds,
            "subproblem_max_seconds": sub_max_seconds,
            "explore_unknown_subproblems": explore_unknown,
            "pairwise_incompatibility_cuts": pairwise_incompatibility_cuts,
        },
        "elapsed_seconds": time.perf_counter() - started,
    }
    return result, candidate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--d8-json", type=Path, required=True)
    parser.add_argument("--s", type=int, default=13)
    parser.add_argument("--budget", type=int, default=9)
    parser.add_argument("--hub", nargs=2, type=int, default=(56, 60))
    parser.add_argument("--solver", default="minisat22")
    parser.add_argument("--master-conflicts-per-call", type=int, default=5000)
    parser.add_argument("--master-max-conflicts", type=int, default=500000)
    parser.add_argument("--master-per-call-seconds", type=float, default=8.0)
    parser.add_argument("--max-seconds", type=float, default=240.0)
    parser.add_argument("--max-iterations", type=int, default=10000)
    parser.add_argument("--cuts-per-iteration", type=int, default=64)
    parser.add_argument("--oracle-nodes", type=int, default=2000000)
    parser.add_argument("--oracle-seconds", type=float, default=8.0)
    parser.add_argument("--subsolver", default="minisat22")
    parser.add_argument("--sub-conflicts-per-call", type=int, default=5000)
    parser.add_argument("--sub-max-conflicts", type=int, default=100000)
    parser.add_argument("--sub-per-call-seconds", type=float, default=5.0)
    parser.add_argument("--sub-max-seconds", type=float, default=30.0)
    parser.add_argument(
        "--stop-on-unknown-subproblem", action="store_true",
        help="do not heuristically exclude a bounded-UNKNOWN fixed-D subproblem",
    )
    parser.add_argument(
        "--resume-json",
        type=Path,
        help="import reusable_strict_cuts from an earlier matching run",
    )
    parser.add_argument(
        "--no-pairwise-incompatibility-cuts",
        action="store_true",
        help="disable strict binary cuts derived from joint local deletion cost",
    )
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()

    input_bytes = args.matrix.read_bytes()
    d8_bytes = args.d8_json.read_bytes()
    d8_record = json.loads(d8_bytes)
    input_sha = hashlib.sha256(input_bytes).hexdigest()
    if d8_record.get("input_sha256") != input_sha:
        raise ValueError("d8 record and matrix SHA256 do not match")
    resume_masks: list[int] = []
    resume_sha: str | None = None
    if args.resume_json:
        resume_bytes = args.resume_json.read_bytes()
        resume = json.loads(resume_bytes)
        if resume.get("schema") != "ramsey-r3-13-benders-budget9-v1":
            raise ValueError("resume JSON has the wrong schema")
        if resume.get("provenance", {}).get("input_sha256") != input_sha:
            raise ValueError("resume JSON belongs to a different input")
        resume_masks = [
            int(encoded, 16)
            for encoded in resume.get("reusable_strict_cuts", {}).get(
                "conditional_I13_masks_hex", []
            )
        ]
        if len(resume_masks) != len(set(resume_masks)):
            raise ValueError("resume JSON contains duplicate cut masks")
        resume_sha = hashlib.sha256(resume_bytes).hexdigest()
    result, candidate = run_benders(
        read_matrix(args.matrix),
        d8_record,
        args.s,
        args.budget,
        tuple(args.hub),
        args.solver,
        args.master_conflicts_per_call,
        args.master_max_conflicts,
        args.master_per_call_seconds,
        args.max_seconds,
        args.max_iterations,
        args.cuts_per_iteration,
        args.oracle_nodes,
        args.oracle_seconds,
        args.subsolver,
        args.sub_conflicts_per_call,
        args.sub_max_conflicts,
        args.sub_per_call_seconds,
        args.sub_max_seconds,
        not args.stop_on_unknown_subproblem,
        resume_masks,
        not args.no_pairwise_incompatibility_cuts,
    )
    result["provenance"] = {
        "input": str(args.matrix),
        "input_sha256": input_sha,
        "prior_d8_record": str(args.d8_json),
        "prior_d8_record_sha256": hashlib.sha256(d8_bytes).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "resume_json": str(args.resume_json) if args.resume_json else None,
        "resume_json_sha256": resume_sha,
    }
    if candidate is not None:
        if args.output is None:
            raise ValueError("SAT requires --output for independent verification")
        write_matrix(candidate, args.output)
        checked = verify(args.output, 3, args.s)
        result["candidate"] = {
            "path": str(args.output),
            "sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
            "independent_bitset_verification": checked,
        }
        if not checked["valid_ramsey_certificate"]:
            result["status"] = "INTERNAL_ERROR_INDEPENDENT_VERIFICATION_FAILED"
    else:
        result["candidate"] = None
    rendered = json.dumps(result, indent=2, sort_keys=True)
    args.json.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
