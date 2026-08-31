#!/usr/bin/env python3
"""Bounded deletion-first Benders pilot for R(3,18) exact-seven branch 1.

The frozen 100-vertex seed has one triangle on ``{97,98,99}``.  This pilot
fixes ``(97,99)`` absent and asks for exactly six further *input-edge*
deletions.  Input nonedges may be added, while the seven deleted input edges
may not be re-added.

The master uses one deletion variable ``d_e`` for every remaining input edge
and one local-eligibility selector ``y_f`` for every original input nonedge.
For each common neighbour ``w`` of a possible addition ``f={u,v}``, the clause

    -y_f OR d_{uw} OR d_{vw}

ensures that selecting ``y_f`` is possible only if the deletion set breaks the
corresponding seed triangle.  Independent-18 conditional cuts are separated
lazily.  Both levels also impose the necessary degree cap 17: in a
triangle-free graph every open neighbourhood is independent.  Once a fixed
deletion set passes that relaxation, or its support oracle is incomplete but
has produced no new cut, an exact add-only subproblem checks all collective
triangle constraints and separates further independent 18-sets.

Every SAT call is bounded by both conflicts and wall time.  In particular, an
UNKNOWN subproblem stops the pilot and never creates a deletion no-good.  An
UNSAT result is still only a solver endpoint: this pilot does not emit DRAT and
therefore never promotes an unchecked UNSAT endpoint to a theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import time
from collections import Counter, deque
from pathlib import Path
from typing import Any, Iterable

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Solver

try:
    from .benders_budget9 import (
        edge_set,
        enumerate_cliques_interruptible,
        fixed_deletion_addition_pairs,
        flip_off,
        flip_on,
        locally_eligible,
        make_conditional_clause,
        master_support,
        triangle_witness,
        vertices,
    )
    from .budget8_next import masks_hash, sha256
    from .budget9_core_guided import (
        edge_present,
        input_triangles,
        normalized_edge,
        solve_limited_once,
    )
    from .graph_utils import enumerate_cliques, write_matrix
    from .r3_18_branch0_two_stage import atomic_json
    from .r3_18_budget5_branch import EXPECTED_INPUT_SHA256
    from .r3_18_budget7_branch import (
        EXPECTED_BUDGET6_SUMMARY_SHA256,
        load_universal_bank,
        validate_budget6_dependency,
    )
    from .verify_ramsey import complement, read_matrix, verify
    from .verify_ramsey_sat import sat_contains_clique
except ImportError:  # pragma: no cover - direct script execution
    from benders_budget9 import (
        edge_set,
        enumerate_cliques_interruptible,
        fixed_deletion_addition_pairs,
        flip_off,
        flip_on,
        locally_eligible,
        make_conditional_clause,
        master_support,
        triangle_witness,
        vertices,
    )
    from budget8_next import masks_hash, sha256
    from budget9_core_guided import (
        edge_present,
        input_triangles,
        normalized_edge,
        solve_limited_once,
    )
    from graph_utils import enumerate_cliques, write_matrix
    from r3_18_branch0_two_stage import atomic_json
    from r3_18_budget5_branch import EXPECTED_INPUT_SHA256
    from r3_18_budget7_branch import (
        EXPECTED_BUDGET6_SUMMARY_SHA256,
        load_universal_bank,
        validate_budget6_dependency,
    )
    from verify_ramsey import complement, read_matrix, verify
    from verify_ramsey_sat import sat_contains_clique


Edge = tuple[int, int]

SCHEMA = "ramsey-r3-18-n100-exact-budget7-benders-branch1-pilot-v1"
FIXED_EDGE: Edge = (97, 99)
EXPECTED_TRIANGLE = (97, 98, 99)
TARGET_S = 18
DEGREE_CAP = TARGET_S - 1
RESIDUAL_DELETIONS = 6
EXPECTED_VERTICES = 100
EXPECTED_INPUT_EDGES = 827
EXPECTED_BASE_EDGES = 826
EXPECTED_ADDITION_PAIRS = 4_123
EXPECTED_FIXED_BASE_I18 = 235_504
EXPECTED_FIXED_BASE_I18_SHA256 = (
    "1e9f89f40cd97a5f3b6fa93bb3c4835d45cadca8362e9d3150e90d4f385f6d8c"
)
REPOSITORY_ROOT = Path(__file__).resolve().parents[2]


def _mask_hex(mask: int, n: int = EXPECTED_VERTICES) -> str:
    return f"{mask:0{(n + 3) // 4}x}"


def _validate_mask(mask: int, n: int, size: int) -> None:
    if mask < 0 or mask.bit_count() != size or mask >> n:
        raise ValueError(f"mask is not a {size}-subset of [0,{n})")


def shareable_path(path: Path) -> str:
    """Render repository paths relatively and external paths by basename."""

    resolved = path.resolve()
    try:
        return resolved.relative_to(REPOSITORY_ROOT).as_posix()
    except ValueError:
        return path.name


def graph_sha256(rows: list[int]) -> str:
    payload = "".join(
        f"{u},{v}\n" for u, v in sorted(edge_set(rows))
    ).encode("ascii")
    return hashlib.sha256(payload).hexdigest()


def vertex_selection_sat_checks(
    rows: list[int], s: int, solver_name: str
) -> dict[str, Any]:
    """Second certificate check using a vertex-selection SAT encoding."""

    forbidden_triangle = sat_contains_clique(rows, 3, solver_name)
    forbidden_independent = sat_contains_clique(
        complement(rows), s, solver_name
    )
    return {
        "encoding": "independent vertex-selection SAT",
        "forbidden_triangle": forbidden_triangle,
        "forbidden_independent_set": forbidden_independent,
        "valid_ramsey_certificate": (
            not forbidden_triangle["exists"]
            and not forbidden_independent["exists"]
        ),
    }


def validate_frozen_seed(rows: list[int]) -> None:
    if len(rows) != EXPECTED_VERTICES:
        raise ValueError("the branch-1 pilot requires the frozen 100-vertex seed")
    if len(edge_set(rows)) != EXPECTED_INPUT_EDGES:
        raise ValueError("unexpected frozen-seed edge count")
    if input_triangles(rows) != [EXPECTED_TRIANGLE]:
        raise ValueError("unexpected frozen-seed triangle family")
    if not edge_present(rows, *FIXED_EDGE):
        raise ValueError("branch-1 fixed edge is not an input edge")


def validate_seed_verification(payload: dict[str, Any]) -> None:
    searches = payload.get("searches", {})
    forbidden = searches.get("forbidden_independent_set", {})
    if payload.get("sha256") != EXPECTED_INPUT_SHA256:
        raise ValueError("seed verification belongs to a different matrix")
    if payload.get("vertices") != EXPECTED_VERTICES:
        raise ValueError("seed verification has the wrong order")
    if payload.get("edges") != EXPECTED_INPUT_EDGES:
        raise ValueError("seed verification has the wrong edge count")
    if forbidden.get("target") != TARGET_S or forbidden.get("exists") is not False:
        raise ValueError("seed verification does not establish alpha(H)<18")


def branch1_base(rows: list[int]) -> list[int]:
    base = rows.copy()
    flip_off(base, FIXED_EDGE)
    if triangle_witness(base) is not None:
        raise AssertionError("fixed branch-1 base must be triangle-free")
    return base


def fixed_base_i18_masks(rows: list[int]) -> list[int]:
    """Enumerate all I18 sets created by deleting the fixed edge.

    The pinned seed has no I18.  Hence every I18 in ``H-(97,99)`` contains
    both endpoints, and the remaining sixteen vertices form an I16 in their
    common non-neighbourhood in the original graph.
    """

    u, v = FIXED_EDGE
    all_vertices = (1 << len(rows)) - 1
    candidates = all_vertices & ~(
        rows[u] | rows[v] | (1 << u) | (1 << v)
    )
    masks = [
        mask | (1 << u) | (1 << v)
        for mask in enumerate_cliques(
            complement(rows), TARGET_S - 2, candidates=candidates
        )
    ]
    masks.sort()
    return masks


def structural_fingerprint(
    dvars: dict[Edge, int],
    yvars: dict[Edge, int],
    requirements: dict[Edge, list[tuple[Edge, Edge]]],
    residual_budget: int,
    order: int,
    degree_cap: int,
    clauses: list[list[int]],
) -> str:
    digest = hashlib.sha256()
    digest.update(f"budget={residual_budget}\n".encode("ascii"))
    digest.update(f"vertices={order}\n".encode("ascii"))
    digest.update(f"degree_cap={degree_cap}\n".encode("ascii"))
    for edge, variable in sorted(dvars.items()):
        digest.update(f"d {edge[0]} {edge[1]} {variable}\n".encode("ascii"))
    for edge, variable in sorted(yvars.items()):
        digest.update(f"y {edge[0]} {edge[1]} {variable}\n".encode("ascii"))
        for first, second in requirements[edge]:
            digest.update(
                (
                    f"w {first[0]} {first[1]} "
                    f"{second[0]} {second[1]}\n"
                ).encode("ascii")
            )
    for clause in clauses:
        digest.update(
            ("c " + " ".join(str(literal) for literal in clause) + " 0\n").encode(
                "ascii"
            )
        )
    return digest.hexdigest()


def encode_degree_upper_bounds(
    order: int,
    dvars: dict[Edge, int],
    yvars: dict[Edge, int],
    degree_cap: int,
    pool: IDPool,
    fixed_degrees: list[int] | None = None,
) -> tuple[list[list[int]], dict[str, Any]]:
    """Encode final-degree bounds with a shared auxiliary-variable pool.

    A negative deletion literal ``-d_e`` is true exactly when a base edge is
    retained; a positive selector ``y_f`` is true exactly when an addition is
    selected.  ``fixed_degrees`` supplies already-retained constant edges, as
    needed by a fixed-deletion add-only subproblem.
    """

    if degree_cap < 0:
        raise ValueError("degree cap must be nonnegative")
    offsets = fixed_degrees if fixed_degrees is not None else [0] * order
    if len(offsets) != order or any(value < 0 for value in offsets):
        raise ValueError("invalid fixed-degree offsets")

    incident: list[list[int]] = [[] for _ in range(order)]
    for (u, v), variable in sorted(dvars.items()):
        incident[u].append(-variable)
        incident[v].append(-variable)
    for (u, v), variable in sorted(yvars.items()):
        incident[u].append(variable)
        incident[v].append(variable)

    clauses: list[list[int]] = []
    auxiliary_before = pool.top
    impossible_vertices: list[int] = []
    literal_histogram: Counter[int] = Counter()
    residual_bound_histogram: Counter[int] = Counter()
    encoded_blocks = 0
    for vertex, literals in enumerate(incident):
        bound = degree_cap - offsets[vertex]
        literal_histogram[len(literals)] += 1
        residual_bound_histogram[bound] += 1
        if bound < 0:
            # A constant retained degree already exceeds the necessary cap.
            clauses.append([])
            impossible_vertices.append(vertex)
        elif len(literals) > bound:
            block = CardEnc.atmost(
                lits=literals,
                bound=bound,
                vpool=pool,
                encoding=EncType.seqcounter,
            )
            clauses.extend(block.clauses)
            encoded_blocks += 1

    metadata = {
        "degree_cap": degree_cap,
        "degree_cap_basis": (
            "triangle-free and alpha<s imply every open neighborhood, an "
            "independent set, has size at most s-1"
        ),
        "degree_cardinality_blocks": encoded_blocks,
        "degree_cardinality_clauses": len(clauses),
        "degree_cardinality_auxiliary_variables": pool.top - auxiliary_before,
        "degree_impossible_vertices": impossible_vertices,
        "degree_variable_literal_count_histogram": {
            str(key): value for key, value in sorted(literal_histogram.items())
        },
        "degree_residual_bound_histogram": {
            str(key): value
            for key, value in sorted(residual_bound_histogram.items())
        },
    }
    return clauses, metadata


def build_master_formula(
    base_rows: list[int],
    fixed_absent: set[Edge],
    residual_budget: int,
) -> tuple[
    list[list[int]],
    dict[Edge, int],
    dict[Edge, int],
    dict[Edge, list[tuple[Edge, Edge]]],
    dict[str, Any],
]:
    """Build the deletion master without any conditional I18 cuts."""

    base_edges = sorted(edge_set(base_rows))
    addition_pairs = fixed_deletion_addition_pairs(
        base_rows, set(), fixed_absent
    )
    dvars = {edge: index + 1 for index, edge in enumerate(base_edges)}
    yvars = {
        edge: len(dvars) + index + 1
        for index, edge in enumerate(addition_pairs)
    }
    if not 0 <= residual_budget <= len(dvars):
        raise ValueError("residual deletion budget is outside the edge family")
    pool = IDPool(start_from=len(dvars) + len(yvars) + 1)
    exact = CardEnc.equals(
        lits=list(dvars.values()),
        bound=residual_budget,
        vpool=pool,
        encoding=EncType.seqcounter,
    )
    clauses = list(exact.clauses)
    requirements: dict[Edge, list[tuple[Edge, Edge]]] = {}
    eligibility_clauses = 0
    wedge_histogram: Counter[int] = Counter()
    for (u, v), yvar in sorted(yvars.items()):
        edge_requirements: list[tuple[Edge, Edge]] = []
        common = base_rows[u] & base_rows[v]
        while common:
            bit = common & -common
            common ^= bit
            w = bit.bit_length() - 1
            first = normalized_edge(u, w)
            second = normalized_edge(v, w)
            if first not in dvars or second not in dvars:
                raise AssertionError("eligibility wedge is not made of base edges")
            edge_requirements.append((first, second))
            clauses.append([-yvar, dvars[first], dvars[second]])
            eligibility_clauses += 1
        requirements[(u, v)] = edge_requirements
        wedge_histogram[len(edge_requirements)] += 1

    degree_clauses, degree_metadata = encode_degree_upper_bounds(
        len(base_rows), dvars, yvars, DEGREE_CAP, pool
    )
    clauses.extend(degree_clauses)
    fingerprint = structural_fingerprint(
        dvars,
        yvars,
        requirements,
        residual_budget,
        len(base_rows),
        DEGREE_CAP,
        clauses,
    )
    metadata = {
        "deletion_variables": len(dvars),
        "eligible_addition_selectors": len(yvars),
        "residual_deletion_budget": residual_budget,
        "cardinality_auxiliary_variables": (
            exact.nv - len(dvars) - len(yvars)
        ),
        "exact_cardinality_clauses": len(exact.clauses),
        "local_eligibility_clauses": eligibility_clauses,
        "structural_clauses": len(clauses),
        "common_neighbor_wedge_histogram": {
            str(key): value for key, value in sorted(wedge_histogram.items())
        },
        "fixed_base_degree_histogram": {
            str(key): value
            for key, value in sorted(
                Counter(row.bit_count() for row in base_rows).items()
            )
        },
        "fixed_base_vertices_above_degree_cap": [
            vertex
            for vertex, row in enumerate(base_rows)
            if row.bit_count() > DEGREE_CAP
        ],
        **degree_metadata,
        "structural_fingerprint_sha256": fingerprint,
    }
    return clauses, dvars, yvars, requirements, metadata


def strict_no_good_clause(
    subproblem_status: str,
    deleted: set[Edge],
    dvars: dict[Edge, int],
) -> list[int] | None:
    """Return a fixed-deletion no-good only for a completed UNSAT result."""

    if subproblem_status != "UNSAT":
        return None
    if (
        len(deleted) != RESIDUAL_DELETIONS
        or any(edge not in dvars for edge in deleted)
    ):
        raise ValueError("invalid fixed-deletion UNSAT set")
    return [-dvars[edge] for edge in sorted(deleted)]


def _addition_clause(
    mask: int,
    post_delete: list[int],
    variables: dict[Edge, int],
) -> list[int] | None:
    """Return the add-only hitting clause; None means already seed-satisfied."""

    subset = vertices(mask)
    for edge in itertools.combinations(subset, 2):
        if edge_present(post_delete, *edge):
            return None
    return [
        variables[edge]
        for edge in itertools.combinations(subset, 2)
        if edge in variables
    ]


def exact_add_only_subproblem(
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
    """Exact bounded add-only repair for one residual deletion set."""

    started = time.perf_counter()
    n = len(base_rows)
    deleted = {normalized_edge(*edge) for edge in deleted}
    fixed_absent = {normalized_edge(*edge) for edge in fixed_absent}
    post_delete = base_rows.copy()
    for edge in deleted:
        if not edge_present(base_rows, *edge):
            raise ValueError(f"cannot delete base nonedge {edge}")
        flip_off(post_delete, edge)

    additions = fixed_deletion_addition_pairs(
        base_rows, deleted, fixed_absent
    )
    variables = {edge: index + 1 for index, edge in enumerate(additions)}
    pool = IDPool(start_from=len(variables) + 1)
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
        if impossible:
            continue
        if not literals:
            raise AssertionError(f"retained base triangle {triple}")
        triangle_clauses.append(literals)

    seeded_clauses: list[list[int]] = []
    for mask in seed_masks:
        _validate_mask(mask, n, s)
        clause = _addition_clause(mask, post_delete, variables)
        if clause is not None:
            seeded_clauses.append(clause)

    degree_clauses, degree_metadata = encode_degree_upper_bounds(
        n,
        {},
        variables,
        s - 1,
        pool,
        [row.bit_count() for row in post_delete],
    )

    calls = 0
    timer_interruptions = 0
    cegar_models = 0
    lazy_cuts = 0
    oracle_nodes_total = 0
    oracle_seconds_total = 0.0
    last_calls: deque[dict[str, Any]] = deque(maxlen=12)
    status = "UNKNOWN_INTERNAL"
    candidate: list[int] | None = None
    with Solver(
        name=solver_name,
        bootstrap_with=triangle_clauses + seeded_clauses + degree_clauses,
    ) as solver:
        preferred = preferred_additions or set()
        solver.set_phases(
            [
                variable if edge in preferred else -variable
                for edge, variable in variables.items()
            ]
        )
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
            outcome, timer_fired, call_elapsed, delta = solve_limited_once(
                solver,
                min(conflict_chunk, max_conflicts - used),
                min(per_call_seconds, max_seconds - elapsed),
            )
            calls += 1
            timer_interruptions += int(timer_fired)
            last_calls.append(
                {
                    "call": calls,
                    "outcome": (
                        "SAT" if outcome is True else
                        "UNSAT" if outcome is False else "UNKNOWN"
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
            positive = {literal for literal in solver.get_model() if literal > 0}
            candidate = post_delete.copy()
            for edge, variable in variables.items():
                if variable in positive:
                    flip_on(candidate, edge)
            if triangle_witness(candidate) is not None:
                raise AssertionError("add-only SAT model contains a triangle")
            search = enumerate_cliques_interruptible(
                complement(candidate), s, 1, oracle_nodes, oracle_seconds
            )
            oracle_nodes_total += search.recursive_nodes
            oracle_seconds_total += search.elapsed_seconds
            if search.witnesses:
                clause = _addition_clause(
                    search.witnesses[0], post_delete, variables
                )
                if clause is None:
                    raise AssertionError("independent witness has a retained edge")
                solver.add_clause(clause)
                lazy_cuts += 1
                candidate = None
                continue
            if not search.complete:
                status = f"UNKNOWN_ORACLE_{search.reason}"
                candidate = None
                break
            status = "SAT"
            break
        final_stats = solver.accum_stats()

    result = {
        "status": status,
        "solver": solver_name,
        "deleted_edges": [list(edge) for edge in sorted(deleted)],
        "addition_variables": len(variables),
        "deleted_input_edges_are_addition_variables": any(
            edge in variables for edge in deleted
        ),
        "triangle_clauses": len(triangle_clauses),
        "seed_hitting_clauses": len(seeded_clauses),
        **degree_metadata,
        "cegar_models": cegar_models,
        "lazy_hitting_clauses": lazy_cuts,
        "limited_calls": calls,
        "timer_interruptions": timer_interruptions,
        "solver_stats": {
            key: final_stats.get(key, 0) - initial_stats.get(key, 0)
            for key in final_stats
        },
        "oracle_recursive_nodes": oracle_nodes_total,
        "oracle_elapsed_seconds": oracle_seconds_total,
        "last_calls": list(last_calls),
        "elapsed_seconds": time.perf_counter() - started,
    }
    if candidate is not None:
        result["candidate_graph_sha256"] = graph_sha256(candidate)
        result["added_edges"] = [
            list(edge)
            for edge in sorted(edge_set(candidate) - edge_set(post_delete))
        ]
    return result, candidate if status == "SAT" else None


def _phase_deletions(
    requirements: dict[Edge, list[tuple[Edge, Edge]]],
    residual_budget: int,
) -> list[Edge]:
    incidence: Counter[Edge] = Counter()
    for pairs in requirements.values():
        for first, second in pairs:
            incidence[first] += 1
            incidence[second] += 1
    ranked = sorted(incidence, key=lambda edge: (-incidence[edge], edge))
    return ranked[:residual_budget]


def _strict_state_hash(masks: Iterable[int], no_goods: Iterable[set[Edge]]) -> str:
    digest = hashlib.sha256()
    for mask in sorted(set(masks)):
        digest.update(f"m {_mask_hex(mask)}\n".encode("ascii"))
    normalized = sorted(tuple(sorted(group)) for group in no_goods)
    for group in normalized:
        digest.update(
            ("d " + " ".join(f"{u},{v}" for u, v in group) + "\n").encode(
                "ascii"
            )
        )
    return digest.hexdigest()


def load_resume_state(
    path: Path | None,
    input_sha256: str,
    structural_sha256: str,
    base_edges: set[Edge],
) -> tuple[list[int], list[set[Edge]], dict[str, Any] | None]:
    if path is None:
        return [], [], None
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema") != SCHEMA:
        raise ValueError("resume checkpoint has the wrong schema")
    if payload.get("input", {}).get("sha256") != input_sha256:
        raise ValueError("resume checkpoint belongs to a different seed")
    if payload.get("formula", {}).get(
        "structural_fingerprint_sha256"
    ) != structural_sha256:
        raise ValueError("resume checkpoint has a different master structure")
    strict = payload.get("strict_state", {})
    if strict.get("unknown_subproblem_no_goods") not in (0, None):
        raise ValueError("resume checkpoint contains forbidden UNKNOWN no-goods")
    masks: list[int] = []
    for encoded in strict.get("additional_conditional_masks_hex", []):
        mask = int(encoded, 16)
        _validate_mask(mask, EXPECTED_VERTICES, TARGET_S)
        masks.append(mask)
    if len(masks) != len(set(masks)):
        raise ValueError("resume checkpoint contains duplicate conditional masks")
    no_goods: list[set[Edge]] = []
    for encoded_group in strict.get("fixed_deletion_unsat_no_goods", []):
        group = {normalized_edge(*edge) for edge in encoded_group}
        if len(group) != RESIDUAL_DELETIONS or not group <= base_edges:
            raise ValueError("resume checkpoint contains an invalid deletion no-good")
        no_goods.append(group)
    expected_hash = strict.get("strict_state_sha256")
    if expected_hash != _strict_state_hash(masks, no_goods):
        raise ValueError("resume checkpoint strict-state digest mismatch")
    info = {
        "path": shareable_path(path),
        "sha256": sha256(path),
        "additional_conditional_masks": len(masks),
        "fixed_deletion_unsat_no_goods": len(no_goods),
    }
    return masks, no_goods, info


def run_branch1_benders(
    initial: list[int],
    input_sha256: str,
    initial_masks: list[int],
    initial_mask_metadata: dict[str, Any],
    sub_seed_masks: list[int],
    checkpoint_path: Path,
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
    resume_path: Path | None = None,
) -> tuple[dict[str, Any], list[int] | None]:
    """Run the bounded branch-1 master/subproblem loop."""

    started = time.perf_counter()
    validate_frozen_seed(initial)
    base = branch1_base(initial)
    clauses, dvars, yvars, requirements, formula = build_master_formula(
        base, {FIXED_EDGE}, RESIDUAL_DELETIONS
    )
    if len(dvars) != EXPECTED_BASE_EDGES:
        raise AssertionError("unexpected branch-1 deletion-variable count")
    if len(yvars) != EXPECTED_ADDITION_PAIRS:
        raise AssertionError("unexpected branch-1 addition-selector count")

    base_edges = set(dvars)
    resume_masks, resume_no_goods, resume_info = load_resume_state(
        resume_path,
        input_sha256,
        formula["structural_fingerprint_sha256"],
        base_edges,
    )
    for mask in initial_masks:
        _validate_mask(mask, len(initial), TARGET_S)
    installed_masks = sorted(set(initial_masks) | set(resume_masks))
    known_masks = set(installed_masks)
    initial_set = set(initial_masks)
    additional_masks = sorted(set(resume_masks) - initial_set)
    strict_no_goods = [set(group) for group in resume_no_goods]
    phase_deletions = _phase_deletions(requirements, RESIDUAL_DELETIONS)

    master_calls = 0
    master_iterations = 0
    master_timer_interruptions = 0
    separated_masks = 0
    master_oracle_incomplete_fallbacks = 0
    subproblem_statuses: Counter[str] = Counter()
    last_calls: deque[dict[str, Any]] = deque(maxlen=16)
    last_models: deque[dict[str, Any]] = deque(maxlen=12)
    last_subproblem: dict[str, Any] | None = None
    status = "UNKNOWN_INTERNAL"
    candidate: list[int] | None = None
    checkpoint_sequence = 0
    final_stats: dict[str, int] = {}
    initial_stats: dict[str, int] = {}

    formula.update(
        {
            "fixed_deleted_edge": list(FIXED_EDGE),
            "fixed_deleted_edge_cannot_be_readded": True,
            "initial_conditional_I18_clauses": len(initial_masks),
            "resumed_additional_conditional_I18_clauses": len(additional_masks),
            "installed_conditional_I18_clauses": len(installed_masks),
            "initial_total_clauses": len(clauses) + len(installed_masks)
            + len(strict_no_goods),
        }
    )

    def checkpoint(event_status: str, event: dict[str, Any] | None = None) -> None:
        nonlocal checkpoint_sequence
        checkpoint_sequence += 1
        current_stats = final_stats or initial_stats
        solver_stats = {
            key: current_stats.get(key, 0) - initial_stats.get(key, 0)
            for key in current_stats
        }
        strict_hash = _strict_state_hash(additional_masks, strict_no_goods)
        formula_snapshot = {
            **formula,
            "installed_conditional_I18_clauses": len(known_masks),
            "new_conditional_I18_clauses_this_run": separated_masks,
            "current_fixed_deletion_unsat_no_goods": len(strict_no_goods),
            "current_total_clauses": (
                len(clauses) + len(known_masks) + len(strict_no_goods)
            ),
        }
        payload = {
            "schema": SCHEMA,
            "status": event_status,
            "branch": 1,
            "fixed_deleted_edge": list(FIXED_EDGE),
            "input": {
                "sha256": input_sha256,
                "vertices": len(initial),
                "edges": len(edge_set(initial)),
            },
            "formula": formula_snapshot,
            "initial_cut_bank": initial_mask_metadata,
            "resume": resume_info,
            "strict_state": {
                "heuristic_exclusion_free": True,
                "subproblem_unsat_no_goods_proof_checked": False,
                "subproblem_unsat_no_goods_trust": (
                    "completed solver UNSAT endpoint; no DRAT emitted"
                ),
                "unknown_subproblem_no_goods": 0,
                "additional_conditional_masks_hex": [
                    _mask_hex(mask) for mask in sorted(additional_masks)
                ],
                "additional_conditional_masks_sha256": masks_hash(
                    sorted(additional_masks)
                ),
                "fixed_deletion_unsat_no_goods": [
                    [list(edge) for edge in sorted(group)]
                    for group in sorted(
                        strict_no_goods, key=lambda group: tuple(sorted(group))
                    )
                ],
                "strict_state_sha256": strict_hash,
            },
            "progress": {
                "checkpoint_sequence": checkpoint_sequence,
                "master_calls": master_calls,
                "master_iterations": master_iterations,
                "master_timer_interruptions": master_timer_interruptions,
                "new_conditional_I18_masks": separated_masks,
                "master_oracle_incomplete_fallbacks": (
                    master_oracle_incomplete_fallbacks
                ),
                "fixed_deletion_unsat_no_goods": len(strict_no_goods),
                "subproblem_statuses": dict(sorted(subproblem_statuses.items())),
                "solver_stats": solver_stats,
                "last_master_calls": list(last_calls),
                "last_master_models": list(last_models),
                "last_subproblem": last_subproblem,
                "elapsed_seconds": time.perf_counter() - started,
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
            },
            "solvers": {"master": solver_name, "subproblem": subsolver_name},
            "phase": {
                "strategy": "top common-neighbor-wedge incidence",
                "preferred_residual_deletions": [
                    list(edge) for edge in phase_deletions
                ],
                "preferred_addition_selectors": 0,
            },
            "event": event,
            "claim_boundary": (
                "SAT requires independent bitset, vertex-selection SAT, and "
                "exact-edit verification. This pilot emits no DRAT; every "
                "UNSAT solver endpoint remains proof-unchecked and all "
                "resource-limit outcomes remain UNKNOWN. An incomplete master "
                "support oracle may fall back to the exact fixed-deletion "
                "subproblem, but UNKNOWN subproblems never generate deletion "
                "no-goods."
            ),
        }
        atomic_json(checkpoint_path, payload)

    with Solver(name=solver_name, bootstrap_with=clauses) as master:
        for mask in installed_masks:
            master.add_clause(make_conditional_clause(mask, base, dvars, yvars))
        for group in strict_no_goods:
            clause = strict_no_good_clause("UNSAT", group, dvars)
            if clause is None:
                raise AssertionError("strict resume no-good was not reconstructed")
            master.add_clause(clause)
        phase_set = set(phase_deletions)
        master.set_phases(
            [-variable for variable in yvars.values()]
            + [
                variable if edge in phase_set else -variable
                for edge, variable in dvars.items()
            ]
        )
        initial_stats = master.accum_stats()
        final_stats = initial_stats
        checkpoint("READY", {"kind": "FORMULA_INSTALLED"})

        while True:
            elapsed = time.perf_counter() - started
            final_stats = master.accum_stats()
            conflicts = final_stats.get("conflicts", 0) - initial_stats.get(
                "conflicts", 0
            )
            if elapsed >= max_seconds:
                status = "UNKNOWN_GLOBAL_WALL_LIMIT"
                break
            if conflicts >= master_max_conflicts:
                status = "UNKNOWN_MASTER_CONFLICT_LIMIT"
                break
            if master_iterations >= max_iterations:
                status = "UNKNOWN_MASTER_ITERATION_LIMIT"
                break

            outcome, timer_fired, call_elapsed, delta = solve_limited_once(
                master,
                min(master_conflict_chunk, master_max_conflicts - conflicts),
                min(master_per_call_seconds, max_seconds - elapsed),
            )
            master_calls += 1
            master_timer_interruptions += int(timer_fired)
            call_record = {
                "call": master_calls,
                "outcome": (
                    "SAT" if outcome is True else
                    "UNSAT" if outcome is False else "UNKNOWN"
                ),
                "timer_interrupted": timer_fired,
                "elapsed_seconds": call_elapsed,
                "stats_delta": delta,
            }
            last_calls.append(call_record)
            final_stats = master.accum_stats()
            checkpoint("RUNNING", {"kind": "MASTER_SLICE", **call_record})
            if outcome is None:
                continue
            if outcome is False:
                status = "UNSAT_MASTER_RELAXATION_UNCHECKED"
                break

            master_iterations += 1
            positive = {literal for literal in master.get_model() if literal > 0}
            deleted = {edge for edge, var in dvars.items() if var in positive}
            selected_y = {edge for edge, var in yvars.items() if var in positive}
            if len(deleted) != RESIDUAL_DELETIONS:
                raise AssertionError("master violated exact-six deletion equality")
            if any(
                not locally_eligible(base, deleted, edge)
                for edge in selected_y
            ):
                raise AssertionError("master selected an ineligible addition")

            support = master_support(base, deleted, selected_y)
            search = enumerate_cliques_interruptible(
                complement(support),
                TARGET_S,
                cuts_per_iteration,
                oracle_nodes,
                oracle_seconds,
            )
            new_masks = sorted(
                mask for mask in search.witnesses
                if mask not in known_masks
            )
            model_record = {
                "iteration": master_iterations,
                "deleted_edges": [list(edge) for edge in sorted(deleted)],
                "selected_eligible_additions": len(selected_y),
                "selected_eligible_addition_edges": [
                    list(edge) for edge in sorted(selected_y)
                ],
                "oracle_witnesses": len(search.witnesses),
                "new_conditional_cuts": len(new_masks),
                "oracle_complete": search.complete,
                "oracle_reason": search.reason,
                "oracle_recursive_nodes": search.recursive_nodes,
                "oracle_elapsed_seconds": search.elapsed_seconds,
            }
            last_models.append(model_record)
            if new_masks:
                for mask in new_masks:
                    master.add_clause(
                        make_conditional_clause(mask, base, dvars, yvars)
                    )
                    installed_masks.append(mask)
                    known_masks.add(mask)
                    additional_masks.append(mask)
                installed_masks.sort()
                additional_masks = sorted(set(additional_masks))
                separated_masks += len(new_masks)
                checkpoint(
                    "RUNNING", {"kind": "MASTER_SEPARATOR", **model_record}
                )
                continue
            if search.witnesses:
                raise AssertionError("separator returned only installed violated cuts")
            if not search.complete:
                master_oracle_incomplete_fallbacks += 1
                model_record["control_flow"] = (
                    "MASTER_ORACLE_INCOMPLETE_FALLBACK_TO_EXACT_SUBPROBLEM"
                )
                model_record["master_oracle_incomplete_reason"] = search.reason
                checkpoint(
                    "RUNNING",
                    {
                        "kind": (
                            "MASTER_ORACLE_INCOMPLETE_FALLBACK_TO_"
                            "EXACT_SUBPROBLEM"
                        ),
                        **model_record,
                    },
                )
            else:
                model_record["control_flow"] = (
                    "MASTER_ORACLE_COMPLETE_TO_EXACT_SUBPROBLEM"
                )

            remaining = max_seconds - (time.perf_counter() - started)
            if remaining <= 0:
                status = "UNKNOWN_GLOBAL_WALL_LIMIT"
                break
            last_subproblem, repaired = exact_add_only_subproblem(
                base,
                deleted,
                {FIXED_EDGE},
                TARGET_S,
                sub_seed_masks,
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
            model_record["subproblem_status"] = last_subproblem["status"]
            if repaired is not None:
                candidate = repaired
                status = "SAT_CANDIDATE"
                break
            no_good = strict_no_good_clause(
                last_subproblem["status"], deleted, dvars
            )
            if no_good is not None:
                master.add_clause(no_good)
                strict_no_goods.append(set(deleted))
                model_record["resolution"] = "UNSAT_FIXED_D_NO_GOOD"
                checkpoint(
                    "RUNNING", {"kind": "SUBPROBLEM_UNSAT", **model_record}
                )
                continue

            # Deliberately stop.  Blocking this deletion set, or even only the
            # current y assignment, would change the proof state after UNKNOWN.
            status = f"UNKNOWN_SUBPROBLEM_{last_subproblem['status']}"
            model_record["resolution"] = "STOPPED_WITHOUT_NO_GOOD"
            break

        final_stats = master.accum_stats()

    checkpoint(status, {"kind": "FINAL_ENDPOINT"})
    result = json.loads(checkpoint_path.read_text(encoding="utf-8"))
    result["elapsed_seconds"] = time.perf_counter() - started
    result["candidate_graph_sha256"] = (
        graph_sha256(candidate) if candidate is not None else None
    )
    return result, candidate


def _positive(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return parsed


def _positive_float(value: str) -> float:
    parsed = float(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return parsed


def validate_limited_solver(name: str) -> None:
    """Fail early when a PySAT backend cannot continue bounded SAT slices."""

    try:
        with Solver(name=name, bootstrap_with=[[1]]) as solver:
            solver.conf_budget(1)
            solver.solve_limited(expect_interrupt=True)
            solver.clear_interrupt()
    except NotImplementedError as error:
        raise ValueError(
            f"solver {name!r} does not support conflict/time-bounded "
            "solve_limited slices"
        ) from error


def main() -> None:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument(
        "--budget6-summary",
        type=Path,
        default=here / "r3_18_budget6_summary.json",
    )
    parser.add_argument(
        "--seed-verification",
        type=Path,
        default=here / "r3_18_n100_nearmiss_verification.json",
    )
    parser.add_argument(
        "--universal-bank",
        type=Path,
        help="optional checked 251771-mask bank to translate into master cuts",
    )
    fixed_group = parser.add_mutually_exclusive_group()
    fixed_group.add_argument(
        "--initial-fixed-base-cuts",
        type=int,
        default=4096,
        help="deterministic prefix of branch-1 fixed-base I18 cuts",
    )
    fixed_group.add_argument(
        "--all-fixed-base-cuts",
        action="store_true",
        help="preload all 235504 branch-1 fixed-base I18 cuts",
    )
    parser.add_argument(
        "--sub-seed-cuts",
        type=int,
        default=4096,
        help="maximum initial master masks passed to each exact subproblem",
    )
    parser.add_argument("--solver", default="minisat22")
    parser.add_argument("--subsolver", default="minisat22")
    parser.add_argument(
        "--certificate-solver",
        default="cadical195",
        help="independent vertex-selection SAT checker used only for a candidate",
    )
    parser.add_argument("--master-conflicts-per-call", type=_positive, default=5000)
    parser.add_argument("--master-max-conflicts", type=_positive, default=100000)
    parser.add_argument("--master-per-call-seconds", type=_positive_float, default=5.0)
    parser.add_argument("--max-seconds", type=_positive_float, default=120.0)
    parser.add_argument("--max-iterations", type=_positive, default=1000)
    parser.add_argument("--cuts-per-iteration", type=_positive, default=256)
    parser.add_argument("--oracle-nodes", type=_positive, default=2000000)
    parser.add_argument("--oracle-seconds", type=_positive_float, default=8.0)
    parser.add_argument("--sub-conflicts-per-call", type=_positive, default=5000)
    parser.add_argument("--sub-max-conflicts", type=_positive, default=100000)
    parser.add_argument("--sub-per-call-seconds", type=_positive_float, default=5.0)
    parser.add_argument("--sub-max-seconds", type=_positive_float, default=30.0)
    parser.add_argument("--resume", type=Path)
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--candidate", type=Path)
    args = parser.parse_args()
    if args.initial_fixed_base_cuts < 0:
        parser.error("--initial-fixed-base-cuts must be nonnegative")
    if args.sub_seed_cuts < 0:
        parser.error("--sub-seed-cuts must be nonnegative")
    validate_limited_solver(args.solver)
    validate_limited_solver(args.subsolver)

    input_sha = sha256(args.matrix)
    if input_sha != EXPECTED_INPUT_SHA256:
        raise ValueError("unexpected frozen near-miss matrix identity")
    rows = read_matrix(args.matrix)
    validate_frozen_seed(rows)

    budget6_sha = sha256(args.budget6_summary)
    if budget6_sha != EXPECTED_BUDGET6_SUMMARY_SHA256:
        raise ValueError("unexpected budget-six summary identity")
    budget6 = json.loads(args.budget6_summary.read_text(encoding="utf-8"))
    validate_budget6_dependency(budget6)
    seed_verification_bytes = args.seed_verification.read_bytes()
    seed_verification = json.loads(seed_verification_bytes)
    validate_seed_verification(seed_verification)

    fixed_masks = fixed_base_i18_masks(rows)
    if len(fixed_masks) != EXPECTED_FIXED_BASE_I18:
        raise AssertionError("unexpected branch-1 fixed-base I18 count")
    if masks_hash(fixed_masks) != EXPECTED_FIXED_BASE_I18_SHA256:
        raise AssertionError("unexpected branch-1 fixed-base I18 digest")
    fixed_count = (
        len(fixed_masks) if args.all_fixed_base_cuts else
        min(args.initial_fixed_base_cuts, len(fixed_masks))
    )
    universal_masks: list[int] = []
    universal_info: dict[str, Any] | None = None
    if args.universal_bank:
        universal_masks, universal_info = load_universal_bank(args.universal_bank)
        # The reusable loader resolves paths for local audit logs.  Pilot JSON
        # remains shareable by preserving the user-supplied spelling instead.
        universal_info["path"] = shareable_path(args.universal_bank)
    initial_masks = sorted(set(universal_masks) | set(fixed_masks[:fixed_count]))
    # Fixed-base masks are guaranteed to be active before the six residual
    # deletions, so they are the most useful deterministic subproblem prefix.
    prioritized_sub_masks = list(fixed_masks[:fixed_count])
    prioritized_seen = set(prioritized_sub_masks)
    prioritized_sub_masks.extend(
        mask for mask in universal_masks if mask not in prioritized_seen
    )
    sub_seed_masks = prioritized_sub_masks[
        : min(args.sub_seed_cuts, len(prioritized_sub_masks))
    ]
    initial_metadata = {
        "fixed_base_I18_total": len(fixed_masks),
        "fixed_base_I18_sha256": masks_hash(fixed_masks),
        "fixed_base_I18_preloaded": fixed_count,
        "universal_bank": universal_info,
        "deduplicated_initial_masks": len(initial_masks),
        "deduplicated_initial_masks_sha256": masks_hash(initial_masks),
        "subproblem_seed_mask_prefix": len(sub_seed_masks),
        "subproblem_seed_mask_prefix_sha256": masks_hash(sub_seed_masks),
        "subproblem_seed_priority": "fixed-base masks, then universal bank",
        "ordering": "ascending integer vertex mask",
    }

    args.checkpoint.parent.mkdir(parents=True, exist_ok=True)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    result, candidate = run_branch1_benders(
        rows,
        input_sha,
        initial_masks,
        initial_metadata,
        sub_seed_masks,
        args.checkpoint,
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
        args.resume,
    )
    result["provenance"] = {
        "matrix": shareable_path(args.matrix),
        "matrix_sha256": input_sha,
        "budget6_summary": shareable_path(args.budget6_summary),
        "budget6_summary_sha256": budget6_sha,
        "seed_verification": shareable_path(args.seed_verification),
        "seed_verification_sha256": hashlib.sha256(
            seed_verification_bytes
        ).hexdigest(),
        "script_sha256": sha256(Path(__file__)),
    }

    if candidate is not None:
        if args.candidate is None:
            result["status"] = "INTERNAL_ERROR_SAT_REQUIRES_CANDIDATE_PATH"
        else:
            args.candidate.parent.mkdir(parents=True, exist_ok=True)
            write_matrix(candidate, args.candidate)
            checked = verify(args.candidate, 3, TARGET_S)
            checked["input"] = shareable_path(args.candidate)
            sat_checked = vertex_selection_sat_checks(
                candidate, TARGET_S, args.certificate_solver
            )
            input_edges = edge_set(rows)
            final_edges = edge_set(candidate)
            observed_deleted = input_edges - final_edges
            additions = final_edges - input_edges
            final_master_model = result["progress"]["last_master_models"][-1]
            declared_residual_deleted = {
                normalized_edge(*edge)
                for edge in final_master_model["deleted_edges"]
            }
            declared_deleted = declared_residual_deleted | {FIXED_EDGE}
            readded_declared_deleted = declared_deleted & final_edges
            edit_check = {
                "deleted_input_edges": [
                    list(edge) for edge in sorted(observed_deleted)
                ],
                "deleted_input_edge_count": len(observed_deleted),
                "declared_deleted_input_edges": [
                    list(edge) for edge in sorted(declared_deleted)
                ],
                "observed_matches_declared_deletions": (
                    observed_deleted == declared_deleted
                ),
                "fixed_edge_deleted": FIXED_EDGE in observed_deleted,
                "added_original_nonedges": [
                    list(edge) for edge in sorted(additions)
                ],
                "readded_declared_deleted_input_edges": [
                    list(edge) for edge in sorted(readded_declared_deleted)
                ],
                "deleted_input_edges_readded": bool(readded_declared_deleted),
                "exact_seven_deletion_semantics": (
                    len(declared_deleted) == RESIDUAL_DELETIONS + 1
                    and FIXED_EDGE in declared_deleted
                    and observed_deleted == declared_deleted
                    and not readded_declared_deleted
                ),
            }
            result["candidate"] = {
                "path": shareable_path(args.candidate),
                "sha256": sha256(args.candidate),
                "independent_bitset_verification": checked,
                "independent_vertex_selection_sat_verification": sat_checked,
                "edit_check": edit_check,
            }
            if (
                checked["valid_ramsey_certificate"]
                and sat_checked["valid_ramsey_certificate"]
                and edit_check["exact_seven_deletion_semantics"]
            ):
                result["status"] = "SAT_WITNESS_INDEPENDENTLY_VERIFIED"
                result["global_ramsey_implication"] = "R(3,18)>=101"
            else:
                result["status"] = "INTERNAL_ERROR_CANDIDATE_VERIFICATION_FAILED"
    else:
        result["candidate"] = None
        result["global_ramsey_implication"] = None

    atomic_json(args.json, result)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
