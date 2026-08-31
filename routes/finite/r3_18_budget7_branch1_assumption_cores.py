#!/usr/bin/env python3
"""Proof-conservative deletion-assumption-core pilot for exact seven.

This module builds one common branch-1 relaxation in the original edge
variables ``x_e``.  For every residual input edge ``e``, the semantic deletion
variable is

    d_e := not x_e.

Consequently a *positive deletion assumption* is passed to PySAT as the
negative edge literal ``-x_e``.  The common formula already contains the
exact-six counter over all residual ``d_e`` literals.  It also contains every
triangle clause, the fixed branch unit ``-x_(97,99)``, the content-addressed
universal I18 bank, and the necessary final-degree upper bounds ``deg(v)<=17``.

An extracted core is accepted only after all of the following hold:

* the primary call completed with a definitive UNSAT result;
* every reported literal is a unique requested positive-deletion assumption;
* a distinct PySAT backend replays the core as definitive UNSAT against an
  independently initialized copy of the common formula.

SAT and UNKNOWN outcomes never learn a core.  Greedy minimization removes a
literal only after another completed UNSAT call; SAT or UNKNOWN retains it.
Extracted clauses are recorded but are deliberately never installed into the
core-extraction formula, avoiding circular cores.

This remains engineering telemetry, not a paper certificate.  A publishable
core needs a frozen DIMACS instance with assumption units and an externally
checked CaDiCaL DRAT/LRAT trace.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import platform
import subprocess
import sys
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Solver, SolverNames

try:
    from .bounded_deletion_sat_cegar import build_variables
    from .budget8_next import masks_hash, sha256
    from .new_basin_search import edge_present
    from .r3_18_branch0_two_stage import atomic_json
    from .r3_18_budget5_branch import EXPECTED_INPUT_SHA256, hitting_clause
    from .r3_18_budget7_branch import (
        EXPECTED_BUDGET6_SUMMARY_SHA256,
        load_universal_bank,
        structural_formula,
        validate_budget6_dependency,
    )
    from .verify_ramsey import read_matrix
except ImportError:  # pragma: no cover - direct script execution
    from bounded_deletion_sat_cegar import build_variables
    from budget8_next import masks_hash, sha256
    from new_basin_search import edge_present
    from r3_18_branch0_two_stage import atomic_json
    from r3_18_budget5_branch import EXPECTED_INPUT_SHA256, hitting_clause
    from r3_18_budget7_branch import (
        EXPECTED_BUDGET6_SUMMARY_SHA256,
        load_universal_bank,
        structural_formula,
        validate_budget6_dependency,
    )
    from verify_ramsey import read_matrix


Edge = tuple[int, int]

SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch1-assumption-core-pilot-v1"
FORMULA_SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch1-common-formula-v1"
CHECKPOINT_SCHEMA = SCHEMA
FIXED_EDGE: Edge = (97, 99)
EXPECTED_VERTICES = 100
EXPECTED_INPUT_EDGES = 827
EXPECTED_RESIDUAL_EDGES = 826
RESIDUAL_DELETIONS = 6
TARGET_S = 18
DEGREE_CAP = TARGET_S - 1
REPOSITORY_ROOT = Path(__file__).resolve().parents[2]

# These are exactly the two completed but proof-unchecked fixed-D UNSAT
# supports recorded by maple_c4096 in both the JSON summary and the human
# experiment record on 2026-08-30.  They are seeds for replay, not certificates.
HISTORICAL_TRUSTED_SUPPORTS: tuple[tuple[Edge, ...], ...] = (
    (
        (1, 97),
        (10, 64),
        (11, 62),
        (17, 98),
        (18, 61),
        (18, 64),
    ),
    (
        (1, 97),
        (10, 64),
        (11, 62),
        (17, 98),
        (18, 61),
        (18, 69),
    ),
)


@dataclass
class CommonFormula:
    """Materialized structural clauses plus a streamed universal bank."""

    clauses: list[list[int]]
    variables: dict[Edge, int]
    pairs: list[Edge]
    original_edges: set[Edge]
    residual_edges: set[Edge]
    universal_masks: list[int]
    metadata: dict[str, Any]


def _canonical_sha256(payload: Any) -> str:
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def _clauses_sha256(clauses: Iterable[Sequence[int]]) -> str:
    digest = hashlib.sha256()
    for clause in clauses:
        digest.update(
            ("c " + " ".join(str(literal) for literal in clause) + " 0\n").encode(
                "ascii"
            )
        )
    return digest.hexdigest()


def _mapping_sha256(variables: dict[Edge, int]) -> str:
    digest = hashlib.sha256()
    for edge, variable in sorted(variables.items()):
        digest.update(f"x {edge[0]} {edge[1]} {variable}\n".encode("ascii"))
    return digest.hexdigest()


def _shareable_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return str(resolved.relative_to(REPOSITORY_ROOT))
    except ValueError:
        # Result JSON is intended to be publishable.  Never leak a workstation
        # or cluster account path when an input is supplied outside the repo.
        return f"external/{resolved.name}"


def _edge_list(edges: Iterable[Edge]) -> list[list[int]]:
    return [list(edge) for edge in sorted(edges)]


def _support_sha256(edges: Iterable[Edge]) -> str:
    return _canonical_sha256(_edge_list(edges))


def encode_final_degree_upper_bounds(
    order: int,
    variables: dict[Edge, int],
    maximum_variable: int,
    degree_cap: int = DEGREE_CAP,
) -> tuple[list[list[int]], int, dict[str, Any]]:
    """Encode ``sum_{w != v} x_vw <= degree_cap`` for every vertex."""

    if order < 1 or degree_cap < 0:
        raise ValueError("invalid order or degree cap")
    expected_pairs = order * (order - 1) // 2
    if len(variables) != expected_pairs:
        raise ValueError("degree encoder requires one variable per graph edge")
    if set(variables.values()) != set(range(1, expected_pairs + 1)):
        raise ValueError("unexpected graph-edge variable numbering")

    pool = IDPool(start_from=maximum_variable + 1)
    clauses: list[list[int]] = []
    block_sizes: list[int] = []
    for vertex in range(order):
        literals = [
            variables[tuple(sorted((vertex, other)))]
            for other in range(order)
            if other != vertex
        ]
        block = CardEnc.atmost(
            lits=literals,
            bound=degree_cap,
            vpool=pool,
            encoding=EncType.seqcounter,
        )
        clauses.extend(block.clauses)
        block_sizes.append(len(block.clauses))
    metadata = {
        "degree_cap": degree_cap,
        "degree_cap_basis": (
            "In a triangle-free graph every open neighbourhood is independent; "
            "alpha<18 therefore implies degree at most 17."
        ),
        "degree_blocks": order,
        "degree_clauses": len(clauses),
        "degree_auxiliary_variables": pool.top - maximum_variable,
        "degree_block_clause_counts": sorted(set(block_sizes)),
        "maximum_variable_after_degree_encoding": pool.top,
    }
    return clauses, pool.top, metadata


def build_common_formula(
    rows: list[int],
    input_sha256: str,
    universal_masks: list[int],
    universal_info: dict[str, Any],
) -> CommonFormula:
    """Build the immutable branch-1 relaxation shared by every support."""

    if len(rows) != EXPECTED_VERTICES:
        raise ValueError("unexpected frozen-seed order")
    if input_sha256 != EXPECTED_INPUT_SHA256:
        raise ValueError("unexpected frozen near-miss matrix identity")
    variables, pairs = build_variables(len(rows))
    original_edges = {edge for edge in pairs if edge_present(rows, *edge)}
    if len(original_edges) != EXPECTED_INPUT_EDGES:
        raise ValueError("unexpected frozen-seed edge count")
    if FIXED_EDGE not in original_edges:
        raise ValueError("branch-1 fixed edge is not an input edge")

    structural, structural_top, structural_metadata = structural_formula(
        len(rows), variables, pairs, original_edges, FIXED_EDGE
    )
    degree_clauses, maximum_variable, degree_metadata = (
        encode_final_degree_upper_bounds(
            len(rows), variables, structural_top, DEGREE_CAP
        )
    )
    clauses = structural + degree_clauses
    residual_edges = original_edges - {FIXED_EDGE}
    if len(residual_edges) != EXPECTED_RESIDUAL_EDGES:
        raise AssertionError("unexpected residual input-edge family")

    universal_identity = {
        "sha256": universal_info.get("sha256"),
        "masks": universal_info.get("masks"),
        "ordered_masks_sha256": universal_info.get("ordered_masks_sha256"),
    }
    if universal_identity["masks"] != len(universal_masks):
        raise ValueError("universal-bank metadata/count mismatch")
    if universal_identity["ordered_masks_sha256"] != masks_hash(universal_masks):
        raise ValueError("universal-bank metadata/order mismatch")

    fingerprint_basis = {
        "schema": FORMULA_SCHEMA,
        "input_sha256": input_sha256,
        "order": len(rows),
        "fixed_deleted_edge": list(FIXED_EDGE),
        "residual_deletion_literal_semantics": "d_e := -x_e",
        "exact_residual_deletions": RESIDUAL_DELETIONS,
        "edge_variable_mapping_sha256": _mapping_sha256(variables),
        "structural_clauses": len(structural),
        "structural_clauses_sha256": _clauses_sha256(structural),
        "degree_clauses": len(degree_clauses),
        "degree_clauses_sha256": _clauses_sha256(degree_clauses),
        "universal_I18_bank": universal_identity,
        "maximum_variable": maximum_variable,
        "total_clauses": len(clauses) + len(universal_masks),
        "learned_core_clauses_installed": 0,
    }
    metadata = {
        **fingerprint_basis,
        "formula_fingerprint_sha256": _canonical_sha256(fingerprint_basis),
        "structural_metadata": structural_metadata,
        "degree_metadata": degree_metadata,
        "formula_is_relaxation_of_target": True,
        "formula_relaxation_reason": (
            "The installed I18 bank is universally necessary but need not list "
            "every I18; UNSAT is informative, SAT is only finite-bank telemetry."
        ),
        "core_clause_circularity_guard": (
            "No extracted deletion core is ever appended to either solver."
        ),
    }
    return CommonFormula(
        clauses=clauses,
        variables=variables,
        pairs=pairs,
        original_edges=original_edges,
        residual_edges=residual_edges,
        universal_masks=universal_masks,
        metadata=metadata,
    )


def validate_deletion_support(
    edges: Iterable[Edge],
    residual_edges: set[Edge],
) -> tuple[Edge, ...]:
    """Return a canonical full residual D or reject it before solving."""

    normalized: list[Edge] = []
    for raw in edges:
        if not isinstance(raw, (list, tuple)) or len(raw) != 2:
            raise ValueError("deletion edge must contain two vertices")
        if any(
            not isinstance(value, int) or isinstance(value, bool)
            for value in raw
        ):
            raise ValueError("deletion vertices must be integer JSON numbers")
        u, v = raw
        edge = tuple(sorted((u, v)))
        if u == v or not (0 <= edge[0] < edge[1] < EXPECTED_VERTICES):
            raise ValueError(f"invalid deletion edge {raw!r}")
        normalized.append(edge)
    if len(normalized) != RESIDUAL_DELETIONS:
        raise ValueError("a fixed-D support must contain exactly six edges")
    if len(set(normalized)) != len(normalized):
        raise ValueError("a fixed-D support contains duplicate edges")
    if any(edge not in residual_edges for edge in normalized):
        raise ValueError("a fixed-D support contains a non-residual input edge")
    return tuple(sorted(normalized))


def deletion_assumptions(
    support: Iterable[Edge], variables: dict[Edge, int]
) -> list[int]:
    """Encode positive ``d_e`` assumptions as negative ``x_e`` literals."""

    return [-variables[edge] for edge in sorted(support)]


def validate_reported_core(
    reported: Sequence[int] | None,
    requested: Sequence[int],
    deletion_literal_to_edge: dict[int, Edge],
) -> list[int]:
    """Validate and canonically order a solver-reported assumption core."""

    if reported is None:
        raise ValueError("UNSAT solver returned no assumption core")
    if len(reported) != len(set(reported)):
        raise ValueError("solver-reported core contains duplicate assumptions")
    requested_set = set(requested)
    for literal in reported:
        if not isinstance(literal, int) or isinstance(literal, bool):
            raise ValueError("solver-reported core contains a noninteger literal")
        if literal >= 0:
            raise ValueError("solver-reported core is not positive-deletion-only")
        if literal not in requested_set:
            raise ValueError("solver-reported core is not a subset of assumptions")
        if literal not in deletion_literal_to_edge:
            raise ValueError("solver-reported core is not a residual deletion")
    return sorted(reported, key=lambda literal: deletion_literal_to_edge[literal])


def extract_core_only_after_unsat(
    outcome: str,
    solver: Any,
    requested: Sequence[int],
    deletion_literal_to_edge: dict[int, Edge],
) -> list[int] | None:
    """Fail closed: never call ``get_core`` for SAT or UNKNOWN."""

    if outcome != "UNSAT":
        return None
    return validate_reported_core(
        solver.get_core(), requested, deletion_literal_to_edge
    )


def accept_core_only_after_replay(
    candidate: Sequence[int], replay_outcome: str
) -> list[int] | None:
    """A primary core becomes learnable only after definitive replay UNSAT."""

    return list(candidate) if replay_outcome == "UNSAT" else None


def greedy_minimize_replayed_core(
    candidate: Sequence[int],
    deletion_literal_to_edge: dict[int, Edge],
    solve_trial: Callable[[list[int]], dict[str, Any]],
) -> tuple[list[int], list[dict[str, Any]], bool]:
    """Greedily shrink a replayed core, removing only on completed UNSAT."""

    current = list(candidate)
    trials: list[dict[str, Any]] = []
    complete = True
    for literal in list(current):
        trial = [value for value in current if value != literal]
        result = solve_trial(trial)
        outcome = result.get("outcome")
        if not isinstance(outcome, str) or outcome not in {
            "SAT",
            "UNSAT",
            "UNKNOWN_GLOBAL_WALL_LIMIT",
            "UNKNOWN_WALL_LIMIT",
            "UNKNOWN_CONFLICT_LIMIT",
        }:
            raise ValueError("minimization callback returned an invalid outcome")
        removed = outcome == "UNSAT"
        if removed:
            current = trial
        if outcome.startswith("UNKNOWN"):
            complete = False
        trials.append(
            {
                "tested_removal_literal": literal,
                "tested_removal_edge": list(deletion_literal_to_edge[literal]),
                "outcome": outcome,
                "removed_only_if_completed_UNSAT": removed,
                "SAT_or_UNKNOWN_retained_literal": not removed,
                "elapsed_seconds": result.get("elapsed_seconds", 0.0),
                "calls": result.get("calls", 0),
                "stats_delta": result.get("stats_delta", {}),
            }
        )
        if outcome == "UNKNOWN_GLOBAL_WALL_LIMIT":
            break
    return current, trials, complete


def final_core_after_cross_check(
    original: Sequence[int],
    minimized: Sequence[int],
    confirmation_outcome: str,
) -> tuple[list[int] | None, str]:
    """Choose the accepted K after a fresh cross-backend final check.

    ``None`` means a SAT mismatch that must be quarantined.  UNKNOWN falls
    back to the original two-backend-replayed core and therefore learns
    nothing from the unconfirmed minimization.
    """

    if list(minimized) == list(original):
        return list(original), "UNCHANGED_ALREADY_TWO_BACKEND_REPLAYED"
    if confirmation_outcome == "UNSAT":
        return list(minimized), "ACCEPT_MINIMIZED_AFTER_FRESH_UNSAT"
    if confirmation_outcome == "SAT":
        return None, "QUARANTINE_SAT_MISMATCH"
    if confirmation_outcome.startswith("UNKNOWN"):
        return list(original), "FALLBACK_TO_ORIGINAL_ON_UNKNOWN"
    raise ValueError("invalid final core confirmation outcome")


def deletion_core_to_master_no_good(
    core: Sequence[int],
    deletion_literal_to_edge: dict[int, Edge],
    variables: dict[Edge, int],
) -> list[int]:
    """Translate K of positive deletions into ``OR_{e in K} x_e``."""

    validated = validate_reported_core(
        core, core, deletion_literal_to_edge
    )
    return [variables[deletion_literal_to_edge[literal]] for literal in validated]


def first_completed_cores_are_size_six(
    records: Sequence[dict[str, Any]], required: int = 16
) -> bool:
    """Stop only after ``required`` *completed* greedy size-six cores."""

    accepted = [
        record["accepted_core"]
        for record in records
        if record.get("accepted_core") is not None
    ]
    if len(accepted) < required:
        return False
    first = accepted[:required]
    return all(
        core.get("size") == RESIDUAL_DELETIONS
        and core.get("greedy_minimization_requested") is True
        and core.get("greedy_minimization_complete") is True
        for core in first
    )


def _git_provenance() -> dict[str, Any]:
    def run(*arguments: str) -> str:
        completed = subprocess.run(
            ["git", *arguments],
            cwd=REPOSITORY_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout.strip()

    try:
        commit = run("rev-parse", "HEAD")
        status = run("status", "--porcelain=v1", "--untracked-files=all")
        return {
            "commit": commit,
            "dirty": bool(status),
            "worktree_status_sha256": hashlib.sha256(
                status.encode("utf-8")
            ).hexdigest(),
        }
    except (OSError, subprocess.CalledProcessError) as error:
        return {"available": False, "error_type": type(error).__name__}


def _runtime_provenance(primary: str, replay: str) -> dict[str, Any]:
    dependencies = (
        "bounded_deletion_sat_cegar.py",
        "budget8_next.py",
        "new_basin_search.py",
        "r3_18_budget5_branch.py",
        "r3_18_budget7_branch.py",
    )
    here = Path(__file__).resolve().parent
    return {
        "python": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "python_executable_basename": Path(sys.executable).name,
        "python_sat": importlib.metadata.version("python-sat"),
        "platform_system": platform.system(),
        "platform_machine": platform.machine(),
        "primary_solver_family": _solver_family(primary),
        "replay_solver_family": _solver_family(replay),
        "git": _git_provenance(),
        "dependency_sha256": {
            name: sha256(here / name) for name in dependencies
        },
    }


def _solver_family(name: str) -> str:
    lowered = name.lower()
    for family, aliases in SolverNames.__dict__.items():
        if family.startswith("_") or not isinstance(aliases, tuple):
            continue
        if lowered in aliases:
            return family
    return lowered


def validate_solver_pair(primary: str, replay: str) -> None:
    """Require distinct backends with limited assumptions and core support."""

    if _solver_family(primary) == _solver_family(replay):
        raise ValueError("primary and replay solvers must be distinct backends")
    for name in (primary, replay):
        try:
            with Solver(name=name, bootstrap_with=[[1, 2]]) as solver:
                solver.conf_budget(100)
                outcome = solver.solve_limited(
                    assumptions=[-1, -2], expect_interrupt=True
                )
                solver.clear_interrupt()
                if outcome is not False:
                    raise ValueError(f"solver {name!r} failed the UNSAT smoke test")
                core = solver.get_core()
                if (
                    core is None
                    or len(core) != len(set(core))
                    or set(core) != {-1, -2}
                ):
                    raise ValueError(f"solver {name!r} lacks assumption cores")
        except NotImplementedError as error:
            raise ValueError(
                f"solver {name!r} lacks bounded assumption solving"
            ) from error


def _stats_delta(after: dict[str, int], before: dict[str, int]) -> dict[str, int]:
    return {
        key: after.get(key, 0) - before.get(key, 0)
        for key in sorted(set(after) | set(before))
    }


def solve_assumptions_limited(
    solver: Solver,
    assumptions: Sequence[int],
    conflict_chunk: int,
    max_conflicts: int,
    per_call_seconds: float,
    max_seconds: float,
    global_deadline: float,
) -> dict[str, Any]:
    """Continue bounded slices until SAT, UNSAT, or a declared limit."""

    if conflict_chunk <= 0 or max_conflicts <= 0:
        raise ValueError("conflict limits must be positive")
    if per_call_seconds <= 0 or max_seconds <= 0:
        raise ValueError("wall limits must be positive")
    started = time.perf_counter()
    initial_stats = solver.accum_stats()
    calls: list[dict[str, Any]] = []
    while True:
        elapsed = time.perf_counter() - started
        global_remaining = global_deadline - time.perf_counter()
        used_conflicts = (
            solver.accum_stats().get("conflicts", 0)
            - initial_stats.get("conflicts", 0)
        )
        if global_remaining <= 0:
            status = "UNKNOWN_GLOBAL_WALL_LIMIT"
            break
        if elapsed >= max_seconds:
            status = "UNKNOWN_WALL_LIMIT"
            break
        if used_conflicts >= max_conflicts:
            status = "UNKNOWN_CONFLICT_LIMIT"
            break

        call_wall = min(
            per_call_seconds,
            max_seconds - elapsed,
            global_remaining,
        )
        call_conflicts = min(conflict_chunk, max_conflicts - used_conflicts)
        fired = threading.Event()

        def interrupt() -> None:
            fired.set()
            solver.interrupt()

        before = solver.accum_stats()
        solver.conf_budget(call_conflicts)
        timer = threading.Timer(call_wall, interrupt)
        timer.daemon = True
        timer.start()
        call_started = time.perf_counter()
        try:
            outcome = solver.solve_limited(
                assumptions=list(assumptions), expect_interrupt=True
            )
        finally:
            call_elapsed = time.perf_counter() - call_started
            timer.cancel()
            timer.join()
            solver.clear_interrupt()
        calls.append(
            {
                "call": len(calls) + 1,
                "outcome": (
                    "SAT" if outcome is True else
                    "UNSAT" if outcome is False else
                    "UNKNOWN"
                ),
                "timer_interrupted": fired.is_set(),
                "elapsed_seconds": call_elapsed,
                "stats_delta": _stats_delta(solver.accum_stats(), before),
            }
        )
        if outcome is True:
            status = "SAT"
            break
        if outcome is False:
            status = "UNSAT"
            break

    final_stats = solver.accum_stats()
    result: dict[str, Any] = {
        "outcome": status,
        "elapsed_seconds": time.perf_counter() - started,
        "calls": len(calls),
        "last_calls": calls[-8:],
        "stats_delta": _stats_delta(final_stats, initial_stats),
    }
    if status == "SAT":
        result["model"] = solver.get_model()
    return result


def _install_common_formula(
    solver_name: str, formula: CommonFormula
) -> tuple[Solver, dict[str, Any]]:
    started = time.perf_counter()
    solver = Solver(name=solver_name, bootstrap_with=formula.clauses)
    try:
        for mask in formula.universal_masks:
            solver.add_clause(hitting_clause(mask, EXPECTED_VERTICES, formula.variables))
        phases = [
            variable if edge in formula.original_edges else -variable
            for edge, variable in sorted(formula.variables.items())
        ]
        phases[formula.variables[FIXED_EDGE] - 1] = -formula.variables[FIXED_EDGE]
        solver.set_phases(phases)
        telemetry = {
            "solver": solver_name,
            "solver_family": _solver_family(solver_name),
            "elapsed_seconds": time.perf_counter() - started,
            "structural_and_degree_clauses": len(formula.clauses),
            "universal_I18_clauses": len(formula.universal_masks),
            "total_clauses_installed": (
                len(formula.clauses) + len(formula.universal_masks)
            ),
            "learned_core_clauses_installed": 0,
            "initial_stats": solver.accum_stats(),
        }
        return solver, telemetry
    except BaseException:
        solver.delete()
        raise


def _projection_rows(model: Sequence[int], formula: CommonFormula) -> list[int]:
    positive = {literal for literal in model if literal > 0}
    rows = [0] * EXPECTED_VERTICES
    for (u, v), variable in formula.variables.items():
        if variable in positive:
            rows[u] |= 1 << v
            rows[v] |= 1 << u
    return rows


def validate_finite_relaxation_model(
    model: Sequence[int],
    assumptions: Sequence[int],
    formula: CommonFormula,
) -> dict[str, Any]:
    """Independently check the graph projection of a finite-bank SAT model."""

    positive = {literal for literal in model if literal > 0}
    if any(-literal in positive for literal in assumptions):
        raise AssertionError("SAT model violates a requested deletion")
    if formula.variables[FIXED_EDGE] in positive:
        raise AssertionError("SAT model re-adds the fixed branch edge")
    deleted = {
        edge
        for edge in formula.residual_edges
        if formula.variables[edge] not in positive
    }
    if len(deleted) != RESIDUAL_DELETIONS:
        raise AssertionError("SAT model violates exact-six deletion semantics")
    rows = _projection_rows(model, formula)
    if any(row.bit_count() > DEGREE_CAP for row in rows):
        raise AssertionError("SAT model violates the degree cap")
    for u, v in formula.pairs:
        if (rows[u] >> v) & 1 and rows[u] & rows[v]:
            raise AssertionError("SAT model contains a triangle")
    for mask in formula.universal_masks:
        subset = mask
        hit = False
        while subset and not hit:
            bit = subset & -subset
            subset ^= bit
            vertex = bit.bit_length() - 1
            hit = bool(rows[vertex] & mask)
        if not hit:
            raise AssertionError("SAT model violates the universal I18 bank")
    projection = bytes(
        1 if formula.variables[edge] in positive else 0
        for edge in formula.pairs
    )
    return {
        "checked": True,
        "deleted_residual_edges": _edge_list(deleted),
        "exact_six": True,
        "triangle_free": True,
        "degree_cap_17": True,
        "universal_I18_bank_satisfied": True,
        "edge_projection_sha256": hashlib.sha256(projection).hexdigest(),
        "claim_boundary": "SAT only satisfies the installed finite relaxation.",
    }


def _record_with_digest(record: dict[str, Any]) -> dict[str, Any]:
    result = dict(record)
    result["record_sha256"] = _canonical_sha256(record)
    return result


def evaluate_support(
    support: tuple[Edge, ...],
    formula: CommonFormula,
    primary_name: str,
    replay_name: str,
    conflict_chunk: int,
    max_conflicts: int,
    per_call_seconds: float,
    max_seconds: float,
    global_deadline: float,
    minimize: bool,
) -> dict[str, Any]:
    """Run one support through fresh primary extraction and fresh replay.

    Each support gets independently initialized solver instances.  This makes
    the formula fingerprint, assumptions, and backend names a complete account
    of the installed state; no clauses learned under an earlier support can
    affect a later replay.
    """

    assumptions = deletion_assumptions(support, formula.variables)
    literal_to_edge = {
        -formula.variables[edge]: edge for edge in formula.residual_edges
    }
    base_record: dict[str, Any] = {
        "support": _edge_list(support),
        "support_sha256": _support_sha256(support),
        "support_size": len(support),
        "assumption_semantics": "each listed d_e=true is passed as -x_e",
        "assumption_literals": assumptions,
        "exact_six_counter_is_in_common_formula": True,
        "primary_solver": primary_name,
        "replay_solver": replay_name,
        "accepted_core": None,
        "learned_master_no_good": None,
        "learned_core_clauses_installed_into_common_formula": 0,
        "solver_installation": {
            "primary": None,
            "replay": None,
            "final_minimized_core_confirmation": None,
        },
    }
    primary, primary_install = _install_common_formula(primary_name, formula)
    base_record["solver_installation"]["primary"] = primary_install
    try:
        primary_result = solve_assumptions_limited(
            primary,
            assumptions,
            conflict_chunk,
            max_conflicts,
            per_call_seconds,
            max_seconds,
            global_deadline,
        )
        primary_outcome = primary_result["outcome"]
        base_record["primary"] = {
            key: value for key, value in primary_result.items() if key != "model"
        }
        if primary_outcome == "SAT":
            base_record["status"] = "SAT_FINITE_RELAXATION"
            base_record["primary_model_validation"] = (
                validate_finite_relaxation_model(
                    primary_result["model"], assumptions, formula
                )
            )
            return _record_with_digest(base_record)
        if primary_outcome != "UNSAT":
            base_record["status"] = primary_outcome
            base_record["unknown_learned_nothing"] = True
            return _record_with_digest(base_record)

        try:
            candidate = extract_core_only_after_unsat(
                primary_outcome, primary, assumptions, literal_to_edge
            )
        except ValueError as error:
            base_record["status"] = "QUARANTINED_INVALID_PRIMARY_CORE"
            base_record["quarantine_reason"] = str(error)
            return _record_with_digest(base_record)
    finally:
        primary.delete()
    if candidate is None:  # pragma: no cover - guarded by primary_outcome
        raise AssertionError("definitive primary UNSAT produced no candidate core")
    base_record["primary_reported_core"] = {
        "literals": candidate,
        "deletion_edges": _edge_list(literal_to_edge[literal] for literal in candidate),
        "size": len(candidate),
        "validated_positive_deletion_subset": True,
    }

    if time.perf_counter() >= global_deadline:
        base_record["status"] = "UNKNOWN_REPLAY_GLOBAL_WALL_LIMIT"
        base_record["unknown_learned_nothing"] = True
        return _record_with_digest(base_record)
    replay, replay_install = _install_common_formula(replay_name, formula)
    base_record["solver_installation"]["replay"] = replay_install
    try:
        replay_result = solve_assumptions_limited(
            replay,
            candidate,
            conflict_chunk,
            max_conflicts,
            per_call_seconds,
            max_seconds,
            global_deadline,
        )
        replay_outcome = replay_result["outcome"]
        base_record["clean_replay"] = {
            key: value for key, value in replay_result.items() if key != "model"
        }
        accepted = accept_core_only_after_replay(candidate, replay_outcome)
        if replay_outcome == "SAT":
            base_record["status"] = "QUARANTINED_REPLAY_SAT_MISMATCH"
            base_record["replay_model_validation"] = (
                validate_finite_relaxation_model(
                    replay_result["model"], candidate, formula
                )
            )
            return _record_with_digest(base_record)
        if accepted is None:
            base_record["status"] = replay_outcome.replace(
                "UNKNOWN", "UNKNOWN_REPLAY", 1
            )
            base_record["unknown_learned_nothing"] = True
            return _record_with_digest(base_record)

        current = list(accepted)
        minimization_trials: list[dict[str, Any]] = []
        minimization_complete = not minimize
        if minimize:
            def solve_trial(trial: list[int]) -> dict[str, Any]:
                return solve_assumptions_limited(
                    replay,
                    trial,
                    conflict_chunk,
                    max_conflicts,
                    per_call_seconds,
                    max_seconds,
                    global_deadline,
                )

            current, minimization_trials, minimization_complete = (
                greedy_minimize_replayed_core(
                    current, literal_to_edge, solve_trial
                )
            )
    finally:
        replay.delete()

    # If minimization changed the core, independently confirm the final core
    # on a fresh instance of the original backend.  A SAT mismatch is
    # quarantined.  UNKNOWN does not promote the removals: the already
    # two-backend-replayed pre-minimization core remains the accepted fallback.
    minimized_candidate = list(current)
    if minimized_candidate != candidate:
        if time.perf_counter() >= global_deadline:
            confirmation_result = {
                "outcome": "UNKNOWN_GLOBAL_WALL_LIMIT",
                "elapsed_seconds": 0.0,
                "calls": 0,
                "last_calls": [],
                "stats_delta": {},
            }
        else:
            confirmation, confirmation_install = _install_common_formula(
                primary_name, formula
            )
            base_record["solver_installation"][
                "final_minimized_core_confirmation"
            ] = confirmation_install
            try:
                confirmation_result = solve_assumptions_limited(
                    confirmation,
                    minimized_candidate,
                    conflict_chunk,
                    max_conflicts,
                    per_call_seconds,
                    max_seconds,
                    global_deadline,
                )
            finally:
                confirmation.delete()
        confirmation_outcome = confirmation_result["outcome"]
        base_record["final_minimized_core_clean_primary_confirmation"] = {
            key: value
            for key, value in confirmation_result.items()
            if key != "model"
        }
        selected, cross_check_decision = final_core_after_cross_check(
            candidate, minimized_candidate, confirmation_outcome
        )
        base_record["final_core_cross_check_decision"] = cross_check_decision
        if selected is None:
            base_record["status"] = "QUARANTINED_MINIMIZED_CORE_REPLAY_SAT"
            base_record["minimized_candidate_not_accepted"] = {
                "literals": minimized_candidate,
                "deletion_edges": _edge_list(
                    literal_to_edge[literal] for literal in minimized_candidate
                ),
            }
            base_record["confirmation_model_validation"] = (
                validate_finite_relaxation_model(
                    confirmation_result["model"], minimized_candidate, formula
                )
            )
            return _record_with_digest(base_record)
        if selected == candidate and minimized_candidate != candidate:
            base_record["minimized_candidate_not_accepted"] = {
                "literals": minimized_candidate,
                "deletion_edges": _edge_list(
                    literal_to_edge[literal] for literal in minimized_candidate
                ),
                "reason": "fresh distinct-backend confirmation was not UNSAT",
                "outcome": confirmation_outcome,
            }
            current = selected
            minimization_complete = False
        else:
            current = selected

    accepted_edges = [literal_to_edge[literal] for literal in current]
    # Since d_e := -x_e, the master no-good OR(not d_e) is OR(x_e).
    no_good = deletion_core_to_master_no_good(
        current, literal_to_edge, formula.variables
    )
    base_record["accepted_core"] = {
        "literals": current,
        "deletion_edges": _edge_list(accepted_edges),
        "size": len(current),
        "primary_UNSAT": True,
        "distinct_backend_replay_UNSAT": True,
        "final_minimized_core_distinct_backend_confirmed": (
            minimized_candidate == candidate
            or base_record.get(
                "final_minimized_core_clean_primary_confirmation", {}
            ).get("outcome") == "UNSAT"
        ),
        "greedy_minimization_requested": minimize,
        "greedy_minimization_complete": minimization_complete,
        "engineering_telemetry_not_proof_certificate": True,
    }
    base_record["learned_master_no_good"] = {
        "x_literals": no_good,
        "semantics": "OR_{e in K} x_e, equivalently OR_{e in K} not d_e",
        "installed_into_common_formula": False,
        "paper_grade": False,
    }
    base_record["minimization_trials"] = minimization_trials
    base_record["status"] = (
        "CORE_REPLAY_VALIDATED_NO_MINIMIZATION"
        if not minimize else
        "CORE_REPLAY_VALIDATED_MINIMIZATION_COMPLETE"
        if minimization_complete else
        "CORE_REPLAY_VALIDATED_MINIMIZATION_INCOMPLETE"
    )
    return _record_with_digest(base_record)


def _load_supports(path: Path | None) -> tuple[list[Any], dict[str, Any]]:
    if path is None:
        raw = HISTORICAL_TRUSTED_SUPPORTS
        source = {
            "kind": "built_in_historical_solver_trusted_supports",
            "cross_checked_records": [
                "routes/finite/r3_18_budget7_benders_pilot_summary.json",
                "routes/finite/R3_18_BUDGET7_BENDERS_PILOT_2026-08-30.md",
            ],
            "claim_boundary": "The source endpoints had no checked proof.",
        }
    else:
        payload = json.loads(path.read_text(encoding="utf-8"))
        raw = payload.get("deletion_sets")
        if raw is None:
            raw = payload.get("trusted_fixed_deletion_unsat_sets_without_proof")
        if not isinstance(raw, list):
            raise ValueError("support JSON contains no deletion-set list")
        source = {
            "kind": "user_supplied_json",
            "path": _shareable_path(path),
            "sha256": sha256(path),
        }
    return list(raw), source


def _positive_int(value: str) -> int:
    parsed = int(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return parsed


def _positive_float(value: str) -> float:
    parsed = float(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return parsed


def main() -> None:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--matrix",
        type=Path,
        default=here / "certificates" / "r3_18_n100_nearmiss.txt",
    )
    parser.add_argument(
        "--universal-bank",
        type=Path,
        default=here / "r3_18_budget6_branch_0_universal_union.cuts.json",
    )
    parser.add_argument(
        "--budget6-summary",
        type=Path,
        default=here / "r3_18_budget6_summary.json",
    )
    parser.add_argument("--supports-json", type=Path)
    parser.add_argument("--solver", default="glucose42")
    parser.add_argument("--replay-solver", default="minisat22")
    parser.add_argument("--conflicts-per-call", type=_positive_int, default=50_000)
    parser.add_argument("--max-conflicts", type=_positive_int, default=2_000_000)
    parser.add_argument("--per-call-seconds", type=_positive_float, default=5.0)
    parser.add_argument("--max-seconds", type=_positive_float, default=300.0)
    parser.add_argument("--global-seconds", type=_positive_float, default=3600.0)
    parser.add_argument("--max-replay-validated-cores", type=_positive_int, default=16)
    parser.add_argument("--no-minimize", action="store_true")
    parser.add_argument(
        "--formula-only",
        action="store_true",
        help="validate and fingerprint the common formula without SAT calls",
    )
    parser.add_argument("--checkpoint", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()

    started = time.perf_counter()
    global_deadline = started + args.global_seconds
    input_sha = sha256(args.matrix)
    rows = read_matrix(args.matrix)
    if sha256(args.budget6_summary) != EXPECTED_BUDGET6_SUMMARY_SHA256:
        raise ValueError("unexpected budget-six summary identity")
    budget6 = json.loads(args.budget6_summary.read_text(encoding="utf-8"))
    validate_budget6_dependency(budget6)
    universal_masks, universal_info = load_universal_bank(args.universal_bank)
    universal_info["path"] = _shareable_path(args.universal_bank)
    formula = build_common_formula(rows, input_sha, universal_masks, universal_info)
    raw_supports, support_source = _load_supports(args.supports_json)
    supports = [
        validate_deletion_support(support, formula.residual_edges)
        for support in raw_supports
    ]
    if len({_support_sha256(support) for support in supports}) != len(supports):
        raise ValueError("support list contains duplicates")

    configuration = {
        "primary_solver": args.solver,
        "replay_solver": args.replay_solver,
        "conflicts_per_call": args.conflicts_per_call,
        "max_conflicts_per_solve": args.max_conflicts,
        "per_call_seconds": args.per_call_seconds,
        "max_seconds_per_solve": args.max_seconds,
        "global_seconds_deadline_starts_before_formula_build": args.global_seconds,
        "installation_wall_semantics": (
            "The deadline is checked before each noninterruptible formula "
            "installation and inside every SAT slice; one installation already "
            "in progress can overrun the deadline."
        ),
        "max_replay_validated_cores": args.max_replay_validated_cores,
        "greedy_minimization": not args.no_minimize,
        "formula_only": args.formula_only,
    }
    result: dict[str, Any] = {
        "schema": SCHEMA,
        "status": "FORMULA_READY",
        "claim_boundary": (
            "PySAT cores and replays are engineering telemetry, not proof "
            "certificates; UNKNOWN never learns."
        ),
        "paper_grade_next_step": (
            "Freeze DIMACS plus assumption units, generate CaDiCaL DRAT/LRAT, "
            "and verify it with an external checker before using a core in a theorem."
        ),
        "input": {
            "matrix": _shareable_path(args.matrix),
            "sha256": input_sha,
            "vertices": len(rows),
            "input_edges": len(formula.original_edges),
        },
        "dependencies": {
            "budget6_summary": _shareable_path(args.budget6_summary),
            "budget6_summary_sha256": sha256(args.budget6_summary),
            "budget6_dependency_proof_verified": True,
            "universal_bank": universal_info,
        },
        "common_formula": formula.metadata,
        "support_source": support_source,
        "supports": [_edge_list(support) for support in supports],
        "configuration": configuration,
        "configuration_sha256": _canonical_sha256(configuration),
        "stop_rule": {
            "first_of": [
                f"{args.max_replay_validated_cores} replay-validated cores",
                f"{args.global_seconds:g} seconds total wall",
                "quarantined primary/replay inconsistency",
                "input support list exhausted",
            ],
            "all_first_16_size_six": (
                "If the first 16 replay-validated greedy cores all have size "
                "six, stop this generalized-core route."
            ),
        },
        "solver_installation_policy": {
            "fresh_primary_per_support": True,
            "fresh_distinct_backend_replay_per_primary_UNSAT": True,
            "replay_formula_contains_only_common_formula_clauses": True,
            "extracted_core_clauses_installed": 0,
        },
        "records": [],
        "counters": {
            "supports_total": len(supports),
            "supports_processed": 0,
            "primary_UNSAT": 0,
            "replay_validated_cores": 0,
            "unknown_learned_cores": 0,
            "core_clauses_installed_into_common_formula": 0,
        },
        "elapsed_seconds": time.perf_counter() - started,
        "provenance": {
            "script": _shareable_path(Path(__file__)),
            "script_sha256": sha256(Path(__file__)),
            "runtime": _runtime_provenance(args.solver, args.replay_solver),
        },
    }
    args.checkpoint.parent.mkdir(parents=True, exist_ok=True)
    args.json.parent.mkdir(parents=True, exist_ok=True)
    atomic_json(args.checkpoint, result)

    if args.formula_only:
        result["status"] = "FORMULA_READY_NO_SOLVES"
        result["elapsed_seconds"] = time.perf_counter() - started
        atomic_json(args.checkpoint, result)
        atomic_json(args.json, result)
        return

    validate_solver_pair(args.solver, args.replay_solver)
    for support in supports:
        if time.perf_counter() >= global_deadline:
            result["status"] = "STOP_GLOBAL_WALL_LIMIT"
            break
        record = evaluate_support(
            support,
            formula,
            args.solver,
            args.replay_solver,
            args.conflicts_per_call,
            args.max_conflicts,
            args.per_call_seconds,
            args.max_seconds,
            global_deadline,
            not args.no_minimize,
        )
        result["records"].append(record)
        counters = result["counters"]
        counters["supports_processed"] += 1
        counters["primary_UNSAT"] += int(
            record.get("primary", {}).get("outcome") == "UNSAT"
        )
        counters["replay_validated_cores"] += int(
            record.get("accepted_core") is not None
        )
        if record.get("status", "").startswith("QUARANTINED"):
            result["status"] = "STOP_QUARANTINED_INCONSISTENCY"
            atomic_json(args.checkpoint, result)
            break
        if counters["replay_validated_cores"] >= args.max_replay_validated_cores:
            result["status"] = (
                "STOP_FIRST_16_REPLAY_CORES_ALL_SIZE_SIX"
                if args.max_replay_validated_cores == 16
                and first_completed_cores_are_size_six(result["records"], 16)
                else "STOP_REPLAY_VALIDATED_CORE_LIMIT"
            )
            atomic_json(args.checkpoint, result)
            break
        if time.perf_counter() >= global_deadline:
            result["status"] = "STOP_GLOBAL_WALL_LIMIT"
            atomic_json(args.checkpoint, result)
            break
        result["status"] = "RUNNING"
        result["elapsed_seconds"] = time.perf_counter() - started
        atomic_json(args.checkpoint, result)
    else:
        result["status"] = "PILOT_SUPPORT_LIST_EXHAUSTED"

    result["elapsed_seconds"] = time.perf_counter() - started
    result["counters"]["unknown_learned_cores"] = 0
    result["counters"]["core_clauses_installed_into_common_formula"] = 0
    result["final_record_set_sha256"] = _canonical_sha256(result["records"])
    atomic_json(args.checkpoint, result)
    atomic_json(args.json, result)


if __name__ == "__main__":
    main()
