#!/usr/bin/env python3
"""Higher-order shared-deficit master for the forced-hub R(3,13) basin.

This is a separate continuation of ``benders_budget9.py``.  It imports the
strict conditional I_13 masks from a frozen earlier record, rebuilds the local
eligibility and pairwise cuts, and adds genuine ternary cuts.

For an addition f={u,v}, local triangle safety requires the residual deletion
set D to hit every spoke pair {{u,w},{v,w}} over common base neighbours w.  For
three additions f,g,h, let Q be the graph whose vertices are deletable base
edges and whose edges are all their spoke-pair requirements.  If Q has no
vertex cover of size at most eight, then f,g,h cannot all be selected, so

    not y_f OR not y_g OR not y_h

is valid.  Cover feasibility is decided exactly by the standard edge-branching
recurrence: every vertex cover contains at least one endpoint of a selected
edge.  A greedy matching is used only as a safe lower-bound prune.

All SAT calls and clique separations are bounded.  Resource-limit returns are
UNKNOWN.  Any candidate is written and checked by the independent bitset
checker before the machine record can call it a Ramsey certificate.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import time
from collections import Counter, deque
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Solver

try:
    from .benders_budget9 import (
        Edge,
        edge_set,
        enumerate_cliques_interruptible,
        fixed_deletion_addition_pairs,
        fixed_deletion_repair,
        flip_off,
        forced_hub_proof,
        input_triangles,
        locally_eligible,
        make_conditional_clause,
        master_support,
        normalized_edge,
        solve_limited_once,
        triangle_witness,
        two_addition_deletion_lower_bound,
        vertices,
    )
    from .graph_utils import enumerate_cliques, write_matrix
    from .verify_ramsey import complement, read_matrix, verify
except ImportError:  # pragma: no cover - direct execution
    from benders_budget9 import (
        Edge,
        edge_set,
        enumerate_cliques_interruptible,
        fixed_deletion_addition_pairs,
        fixed_deletion_repair,
        flip_off,
        forced_hub_proof,
        input_triangles,
        locally_eligible,
        make_conditional_clause,
        master_support,
        normalized_edge,
        solve_limited_once,
        triangle_witness,
        two_addition_deletion_lower_bound,
        vertices,
    )
    from graph_utils import enumerate_cliques, write_matrix
    from verify_ramsey import complement, read_matrix, verify


Requirement = tuple[Edge, Edge]


def canonical_requirements(requirements: Iterable[Requirement]) -> frozenset[Requirement]:
    return frozenset(
        tuple(sorted((normalized_edge(*left), normalized_edge(*right))))
        for left, right in requirements
        if normalized_edge(*left) != normalized_edge(*right)
    )


def greedy_matching_lower_bound(requirements: frozenset[Requirement]) -> int:
    """Return the size of a deterministic matching, a valid cover lower bound."""
    used: set[Edge] = set()
    count = 0
    for left, right in sorted(requirements):
        if left not in used and right not in used:
            used.add(left)
            used.add(right)
            count += 1
    return count


def vertex_coverable(
    requirements: Iterable[Requirement], budget: int
) -> tuple[bool, dict[str, int]]:
    """Decide exactly whether the requirement graph has a cover <= ``budget``."""
    if budget < 0:
        return False, {"recursive_calls": 0, "memo_entries": 0}
    initial = canonical_requirements(requirements)
    calls = 0

    @lru_cache(maxsize=None)
    def search(edges: frozenset[Requirement], remaining: int) -> bool:
        nonlocal calls
        calls += 1
        if not edges:
            return True
        if remaining <= 0:
            return False
        if greedy_matching_lower_bound(edges) > remaining:
            return False

        degrees: Counter[Edge] = Counter(
            endpoint for edge in edges for endpoint in edge
        )
        left, right = max(
            sorted(edges),
            key=lambda edge: (
                degrees[edge[0]] + degrees[edge[1]],
                degrees[edge[0]],
                degrees[edge[1]],
                edge,
            ),
        )
        # Every cover hits {left,right}; branch on which endpoint is chosen.
        for endpoint in sorted(
            (left, right), key=lambda item: (-degrees[item], item)
        ):
            residual = frozenset(edge for edge in edges if endpoint not in edge)
            if search(residual, remaining - 1):
                return True
        return False

    answer = search(initial, budget)
    return answer, {"recursive_calls": calls, "memo_entries": search.cache_info().currsize}


def addition_requirements(base: list[int], addition: Edge) -> list[Requirement]:
    u, v = addition
    result: list[Requirement] = []
    common = base[u] & base[v]
    while common:
        bit = common & -common
        common ^= bit
        w = bit.bit_length() - 1
        result.append((normalized_edge(u, w), normalized_edge(v, w)))
    return result


def seed_coverage(
    seed_masks: list[int], additions: set[Edge]
) -> Counter[Edge]:
    counts: Counter[Edge] = Counter()
    for mask in seed_masks:
        for edge in itertools.combinations(vertices(mask), 2):
            if edge in additions:
                counts[edge] += 1
    return counts


def generate_ternary_cuts(
    ranked_additions: list[Edge],
    requirements: dict[Edge, list[Requirement]],
    residual_budget: int,
    top_k: int,
    max_triples: int,
    max_seconds: float,
) -> tuple[list[tuple[Edge, Edge, Edge]], dict[str, Any]]:
    """Materialize a bounded deterministic set of genuine ternary no-goods."""
    started = time.perf_counter()
    selected = ranked_additions[:top_k]
    cuts: list[tuple[Edge, Edge, Edge]] = []
    considered = 0
    pairwise_subsumed = 0
    coverable_count = 0
    recursion_calls = 0
    memo_entries = 0
    stopped_reason = "EXHAUSTED_TOP_K_TRIPLES"
    stream = hashlib.sha256()

    for triple in itertools.combinations(selected, 3):
        if considered >= max_triples:
            stopped_reason = "TRIPLE_LIMIT"
            break
        if considered & 1023 == 0 and time.perf_counter() - started >= max_seconds:
            stopped_reason = "WALL_LIMIT"
            break
        considered += 1
        first, second, third = triple
        if any(
            two_addition_deletion_lower_bound(requirements[left], requirements[right])
            > residual_budget
            for left, right in (
                (first, second),
                (first, third),
                (second, third),
            )
        ):
            pairwise_subsumed += 1
            continue
        feasible, stats = vertex_coverable(
            requirements[first] + requirements[second] + requirements[third],
            residual_budget,
        )
        recursion_calls += stats["recursive_calls"]
        memo_entries += stats["memo_entries"]
        if feasible:
            coverable_count += 1
            continue
        cuts.append(triple)
        stream.update(
            (
                f"{first[0]},{first[1]}:"
                f"{second[0]},{second[1]}:"
                f"{third[0]},{third[1]}\n"
            ).encode()
        )

    return cuts, {
        "ranked_additions_considered": len(selected),
        "possible_top_k_triples": len(selected) * (len(selected) - 1) * (len(selected) - 2) // 6,
        "triples_examined": considered,
        "pairwise_subsumed": pairwise_subsumed,
        "genuinely_ternary_incompatible": len(cuts),
        "coverable_at_residual_budget": coverable_count,
        "exact_cover_recursive_calls": recursion_calls,
        "exact_cover_memo_entries": memo_entries,
        "stopped_reason": stopped_reason,
        "cut_stream_sha256": stream.hexdigest(),
        "elapsed_seconds": time.perf_counter() - started,
    }


def load_strict_masks(path: Path, input_sha: str) -> tuple[list[int], str]:
    raw = path.read_bytes()
    record = json.loads(raw)
    if record.get("schema") != "ramsey-r3-13-benders-budget9-v1":
        raise ValueError("strict-cut JSON has the wrong schema")
    if record.get("provenance", {}).get("input_sha256") != input_sha:
        raise ValueError("strict-cut JSON belongs to a different input graph")
    if record.get("master", {}).get("heuristic_unknown_no_goods") != 0:
        raise ValueError("refusing a cut record containing heuristic UNKNOWN no-goods")
    masks = [
        int(encoded, 16)
        for encoded in record.get("reusable_strict_cuts", {}).get(
            "conditional_I13_masks_hex", []
        )
    ]
    if len(masks) != len(set(masks)):
        raise ValueError("strict-cut JSON contains duplicate masks")
    if any(mask.bit_count() != 13 for mask in masks):
        raise ValueError("strict-cut JSON contains a non-I13 mask")
    return masks, hashlib.sha256(raw).hexdigest()


def run_next(
    initial: list[int],
    d8_record: dict[str, Any],
    imported_masks: list[int],
    s: int,
    budget: int,
    hub: Edge,
    solver_name: str,
    top_k: int,
    max_triples: int,
    triple_preprocess_seconds: float,
    conflict_chunk: int,
    max_conflicts: int,
    per_call_seconds: float,
    max_seconds: float,
    max_iterations: int,
    cuts_per_iteration: int,
    oracle_nodes: int,
    oracle_seconds: float,
    subsolver: str,
    sub_conflict_chunk: int,
    sub_max_conflicts: int,
    sub_per_call_seconds: float,
    sub_max_seconds: float,
) -> tuple[dict[str, Any], list[int] | None]:
    started = time.perf_counter()
    n = len(initial)
    hub = normalized_edge(*hub)
    proof = forced_hub_proof(input_triangles(initial), hub, budget)
    if not proof["hub_deletion_forced"]:
        raise ValueError("hub deletion is not proved for this input")
    if d8_record.get("status") != "UNSAT" or d8_record.get("deletion_budget") != budget - 1:
        raise ValueError("prior residual-budget record is not exact UNSAT")

    base = initial.copy()
    flip_off(base, hub)
    base_edges = sorted(edge_set(base))
    additions = fixed_deletion_addition_pairs(base, set(), {hub})
    addition_set = set(additions)
    dvars = {edge: i + 1 for i, edge in enumerate(base_edges)}
    yvars = {edge: len(dvars) + i + 1 for i, edge in enumerate(additions)}
    pool = IDPool(start_from=len(dvars) + len(yvars) + 1)
    exact = CardEnc.equals(
        lits=list(dvars.values()),
        bound=budget - 1,
        vpool=pool,
        encoding=EncType.seqcounter,
    )
    clauses = list(exact.clauses)
    requirements = {edge: addition_requirements(base, edge) for edge in additions}

    eligibility_count = 0
    for edge, yvar in yvars.items():
        for left, right in requirements[edge]:
            clauses.append([-yvar, dvars[left], dvars[right]])
            eligibility_count += 1

    pairwise_count = 0
    pairwise_hasher = hashlib.sha256()
    for index, first in enumerate(additions):
        for second in additions[index + 1 :]:
            if two_addition_deletion_lower_bound(
                requirements[first], requirements[second]
            ) > budget - 1:
                clauses.append([-yvars[first], -yvars[second]])
                pairwise_count += 1
                pairwise_hasher.update(
                    f"{first[0]},{first[1]}:{second[0]},{second[1]}\n".encode()
                )

    seed_masks = sorted(enumerate_cliques(complement(base), s))
    coverage = seed_coverage(seed_masks, addition_set)
    ranked = sorted(
        additions,
        key=lambda edge: (coverage[edge], len(requirements[edge]), edge),
        reverse=True,
    )
    ternary, ternary_stats = generate_ternary_cuts(
        ranked,
        requirements,
        budget - 1,
        top_k,
        max_triples,
        triple_preprocess_seconds,
    )
    for first, second, third in ternary:
        clauses.append([-yvars[first], -yvars[second], -yvars[third]])

    cut_masks = set(imported_masks)
    for mask in sorted(cut_masks):
        clauses.append(make_conditional_clause(mask, base, dvars, yvars))

    build_elapsed = time.perf_counter() - started
    strict_no_goods: list[list[list[int]]] = []
    new_mask_hasher = hashlib.sha256()
    new_mask_count = 0
    master_iterations = 0
    limited_calls = 0
    timer_interruptions = 0
    oracle_total_nodes = 0
    oracle_total_seconds = 0.0
    samples: deque[dict[str, Any]] = deque(maxlen=12)
    last_subproblem: dict[str, Any] | None = None
    subproblem_counts: Counter[str] = Counter()
    candidate: list[int] | None = None
    status = "UNKNOWN_INTERNAL"

    with Solver(name=solver_name, bootstrap_with=clauses) as solver:
        solver.set_phases(
            [-variable for variable in yvars.values()]
            + [-variable for variable in dvars.values()]
        )
        initial_stats = solver.accum_stats()
        while True:
            elapsed = time.perf_counter() - started
            used = solver.accum_stats().get("conflicts", 0) - initial_stats.get(
                "conflicts", 0
            )
            if elapsed >= max_seconds:
                status = "UNKNOWN_GLOBAL_WALL_LIMIT"
                break
            if used >= max_conflicts:
                status = "UNKNOWN_MASTER_CONFLICT_LIMIT"
                break
            if master_iterations >= max_iterations:
                status = "UNKNOWN_ITERATION_LIMIT"
                break
            outcome, fired, _, _ = solve_limited_once(
                solver,
                min(conflict_chunk, max_conflicts - used),
                min(per_call_seconds, max_seconds - elapsed),
            )
            limited_calls += 1
            timer_interruptions += int(fired)
            if outcome is None:
                continue
            if outcome is False:
                status = "UNSAT"
                break

            master_iterations += 1
            positive = {literal for literal in solver.get_model() if literal > 0}
            deleted = {edge for edge, var in dvars.items() if var in positive}
            selected = {edge for edge, var in yvars.items() if var in positive}
            if len(deleted) != budget - 1:
                raise RuntimeError("master violated exact residual deletion budget")
            if any(not locally_eligible(base, deleted, edge) for edge in selected):
                raise RuntimeError("master selected a locally unsafe addition")

            support = master_support(base, deleted, selected)
            search = enumerate_cliques_interruptible(
                complement(support),
                s,
                cuts_per_iteration,
                oracle_nodes,
                oracle_seconds,
            )
            oracle_total_nodes += search.recursive_nodes
            oracle_total_seconds += search.elapsed_seconds
            fresh = [mask for mask in search.witnesses if mask not in cut_masks]
            sample = {
                "iteration": master_iterations,
                "deleted_edges": [list(edge) for edge in sorted(deleted)],
                "selected_eligible_additions": len(selected),
                "oracle_witnesses": len(search.witnesses),
                "fresh_conditional_cuts": len(fresh),
                "oracle_complete": search.complete,
                "oracle_reason": search.reason,
                "oracle_recursive_nodes": search.recursive_nodes,
            }
            samples.append(sample)
            if fresh:
                for mask in fresh:
                    solver.add_clause(make_conditional_clause(mask, base, dvars, yvars))
                    cut_masks.add(mask)
                    new_mask_hasher.update(f"{mask:016x}\n".encode())
                new_mask_count += len(fresh)
                continue
            if search.witnesses:
                raise RuntimeError("separator returned only installed violated cuts")
            if not search.complete:
                status = f"UNKNOWN_MASTER_ORACLE_{search.reason}"
                break
            if triangle_witness(support) is None:
                candidate = support
                status = "SAT"
                sample["resolution"] = "MASTER_SUPPORT_CANDIDATE"
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
                subsolver,
                sub_conflict_chunk,
                sub_max_conflicts,
                sub_per_call_seconds,
                min(sub_max_seconds, remaining),
                oracle_nodes,
                oracle_seconds,
                selected,
            )
            subproblem_counts[last_subproblem["status"]] += 1
            sample["subproblem_status"] = last_subproblem["status"]
            if repaired is not None:
                candidate = repaired
                status = "SAT"
                break
            if last_subproblem["status"] == "UNSAT":
                solver.add_clause([-dvars[edge] for edge in sorted(deleted)])
                strict_no_goods.append([list(edge) for edge in sorted(deleted)])
                sample["resolution"] = "STRICT_FIXED_D_NO_GOOD"
                continue
            status = f"UNKNOWN_SUBPROBLEM_{last_subproblem['status']}"
            break
        final_stats = solver.accum_stats()

    seed_payload = "".join(f"{mask:016x}\n" for mask in seed_masks).encode()
    result: dict[str, Any] = {
        "schema": "ramsey-r3-13-benders-next-v1",
        "status": status,
        "candidate": None,
        "all_installed_exclusions_strict": True,
        "heuristic_unknown_no_goods": 0,
        "claim_boundary": (
            "UNSAT is exact only if returned by the bounded master; every "
            "resource-limit status remains UNKNOWN. SAT requires independent "
            "verification of the emitted matrix."
        ),
        "target": {"r": 3, "s": s, "n": n},
        "structure": {
            "forced_hub_proof": proof,
            "residual_deletion_budget": budget - 1,
            "base_edges_after_hub": len(base_edges),
            "addition_selectors": len(additions),
            "seed_I13_count": len(seed_masks),
            "seed_I13_sha256": hashlib.sha256(seed_payload).hexdigest(),
        },
        "master": {
            "solver": solver_name,
            "exact_budget_clauses": len(exact.clauses),
            "local_eligibility_clauses": eligibility_count,
            "pairwise_incompatibility_cuts": pairwise_count,
            "pairwise_cut_stream_sha256": pairwise_hasher.hexdigest(),
            "imported_conditional_I13_cuts": len(imported_masks),
            "new_conditional_I13_cuts": new_mask_count,
            "new_conditional_cut_stream_sha256": new_mask_hasher.hexdigest(),
            "strict_fixed_deletion_no_goods": strict_no_goods,
            "iterations": master_iterations,
            "limited_calls": limited_calls,
            "timer_interruptions": timer_interruptions,
            "solver_stats": {
                key: final_stats.get(key, 0) - initial_stats.get(key, 0)
                for key in final_stats
            },
        },
        "higher_order_shared_deficit": {
            **ternary_stats,
            "selection_rule": (
                "Rank original nonedges by descending occurrence in the "
                "25,685 seed I13 sets, then by local requirement count and edge."
            ),
            "selected_additions": [
                {
                    "edge": list(edge),
                    "seed_I13_coverage": coverage[edge],
                    "individual_requirement_count": len(requirements[edge]),
                }
                for edge in ranked[:top_k]
            ],
        },
        "oracle": {
            "recursive_nodes_total": oracle_total_nodes,
            "elapsed_seconds_total": oracle_total_seconds,
        },
        "subproblems": {
            "status_counts": dict(subproblem_counts),
            "last": last_subproblem,
        },
        "empirical": {
            "last_master_candidates": list(samples),
            "caution": "Master samples are heuristic observations, not necessity claims.",
        },
        "reusable_strict_cuts": {
            "conditional_I13_masks_hex": [
                f"{mask:016x}" for mask in sorted(cut_masks)
            ],
            "ternary_addition_no_goods": [
                (
                    f"{first[0]},{first[1]}:"
                    f"{second[0]},{second[1]}:"
                    f"{third[0]},{third[1]}"
                )
                for first, second, third in ternary
            ],
        },
        "limits": {
            "higher_order_top_k": top_k,
            "higher_order_max_triples": max_triples,
            "higher_order_preprocess_seconds": triple_preprocess_seconds,
            "global_wall_seconds": max_seconds,
            "master_conflicts": max_conflicts,
            "master_conflicts_per_call": conflict_chunk,
            "master_per_call_seconds": per_call_seconds,
            "master_iterations": max_iterations,
            "cuts_per_iteration": cuts_per_iteration,
            "oracle_nodes_per_call": oracle_nodes,
            "oracle_seconds_per_call": oracle_seconds,
            "subproblem_conflicts": sub_max_conflicts,
            "subproblem_conflicts_per_call": sub_conflict_chunk,
            "subproblem_per_call_seconds": sub_per_call_seconds,
            "subproblem_max_seconds": sub_max_seconds,
        },
        "timing": {
            "formula_and_cut_build_seconds": build_elapsed,
            "total_elapsed_seconds": time.perf_counter() - started,
        },
    }
    return result, candidate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--d8-json", type=Path, required=True)
    parser.add_argument("--strict-cut-json", type=Path, required=True)
    parser.add_argument("--s", type=int, default=13)
    parser.add_argument("--budget", type=int, default=9)
    parser.add_argument("--hub", nargs=2, type=int, default=(56, 60))
    parser.add_argument("--solver", default="minisat22")
    parser.add_argument("--higher-order-top-k", type=int, default=128)
    parser.add_argument("--higher-order-max-triples", type=int, default=400000)
    parser.add_argument("--higher-order-preprocess-seconds", type=float, default=30.0)
    parser.add_argument("--conflicts-per-call", type=int, default=5000)
    parser.add_argument("--max-conflicts", type=int, default=750000)
    parser.add_argument("--per-call-seconds", type=float, default=8.0)
    parser.add_argument("--max-seconds", type=float, default=180.0)
    parser.add_argument("--max-iterations", type=int, default=1000)
    parser.add_argument("--cuts-per-iteration", type=int, default=4096)
    parser.add_argument("--oracle-nodes", type=int, default=16000000)
    parser.add_argument("--oracle-seconds", type=float, default=8.0)
    parser.add_argument("--subsolver", default="minisat22")
    parser.add_argument("--sub-conflicts-per-call", type=int, default=5000)
    parser.add_argument("--sub-max-conflicts", type=int, default=100000)
    parser.add_argument("--sub-per-call-seconds", type=float, default=5.0)
    parser.add_argument("--sub-max-seconds", type=float, default=30.0)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()

    if args.higher_order_top_k < 3:
        parser.error("--higher-order-top-k must be at least 3")
    if args.higher_order_max_triples < 1:
        parser.error("--higher-order-max-triples must be positive")
    input_bytes = args.matrix.read_bytes()
    input_sha = hashlib.sha256(input_bytes).hexdigest()
    d8_bytes = args.d8_json.read_bytes()
    d8_record = json.loads(d8_bytes)
    if d8_record.get("input_sha256") != input_sha:
        raise ValueError("d8 record and input graph hashes disagree")
    imported_masks, strict_cut_sha = load_strict_masks(args.strict_cut_json, input_sha)
    result, candidate = run_next(
        read_matrix(args.matrix),
        d8_record,
        imported_masks,
        args.s,
        args.budget,
        tuple(args.hub),
        args.solver,
        args.higher_order_top_k,
        args.higher_order_max_triples,
        args.higher_order_preprocess_seconds,
        args.conflicts_per_call,
        args.max_conflicts,
        args.per_call_seconds,
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
    )
    result["provenance"] = {
        "input": str(args.matrix),
        "input_sha256": input_sha,
        "prior_d8_record": str(args.d8_json),
        "prior_d8_record_sha256": hashlib.sha256(d8_bytes).hexdigest(),
        "strict_cut_record": str(args.strict_cut_json),
        "strict_cut_record_sha256": strict_cut_sha,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
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
    rendered = json.dumps(result, indent=2, sort_keys=True)
    args.json.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
