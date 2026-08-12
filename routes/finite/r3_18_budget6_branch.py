#!/usr/bin/env python3
"""Bounded proof-carrying search of the exact budget-six R(3,18) edit sphere.

The frozen 100-vertex input has one triangle.  A three-way case split fixes
one edge of that triangle absent.  The already checked budget-five theorem
excludes zero through five input-edge deletions, so a genuinely new budget-six
candidate must delete exactly five further input edges in each branch.

Every input nonedge remains a free final-edge variable.  Independent 18-sets
are separated exactly and checkpointed.  Discovery runs in a killable child
process; SAT is accepted only after the independent bitset verifier.  If a
finite cut bank is UNSAT, a standalone pinned CaDiCaL run emits a DRAT trace
which is checked by pinned drat-trim.  A timeout is always UNKNOWN.
"""

from __future__ import annotations

import argparse
import itertools
import json
import multiprocessing
import os
import time
from pathlib import Path
from typing import Any

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Solver

try:
    from .bounded_deletion_sat_cegar import build_variables
    from .budget8_next import (
        deterministic_gzip_text,
        dimacs_lines,
        masks_hash,
        sha256,
        verify_drat_trace,
    )
    from .graph_utils import enumerate_cliques, write_matrix
    from .new_basin_search import edge_present, normalized_edge, rows_from_edge_model
    from .r3_18_branch0_two_stage import atomic_json, run_external_proof
    from .r3_18_budget5_branch import (
        EXPECTED_INPUT_SHA256,
        EXPECTED_TRIANGLE,
        fixed_base_i18_prefix,
        hitting_clause,
        structural_decomposition,
        validate_i18_clause_bank,
    )
    from .verify_ramsey import complement, read_matrix, verify
except ImportError:  # pragma: no cover - direct execution
    from bounded_deletion_sat_cegar import build_variables
    from budget8_next import (
        deterministic_gzip_text,
        dimacs_lines,
        masks_hash,
        sha256,
        verify_drat_trace,
    )
    from graph_utils import enumerate_cliques, write_matrix
    from new_basin_search import edge_present, normalized_edge, rows_from_edge_model
    from r3_18_branch0_two_stage import atomic_json, run_external_proof
    from r3_18_budget5_branch import (
        EXPECTED_INPUT_SHA256,
        EXPECTED_TRIANGLE,
        fixed_base_i18_prefix,
        hitting_clause,
        structural_decomposition,
        validate_i18_clause_bank,
    )
    from verify_ramsey import complement, read_matrix, verify


SCHEMA = "ramsey-r3-18-n100-exact-budget6-branch-v1"
BRANCH_EDGES = tuple(itertools.combinations(EXPECTED_TRIANGLE, 2))
TOTAL_BUDGET = 6
RESIDUAL_DELETIONS = 5


def mask_from_vertices(vertices: list[int]) -> int:
    mask = 0
    for vertex in vertices:
        mask |= 1 << vertex
    return mask


def exact_branch_formula(
    initial: list[int],
    variables: dict[tuple[int, int], int],
    pairs: list[tuple[int, int]],
    original_edges: set[tuple[int, int]],
    fixed_edge: tuple[int, int],
    preload_limit: int,
    resumed_masks: list[int],
) -> tuple[list[list[int]], int, list[int], dict[str, Any]]:
    """Construct exact-six branch CNF and validate every installed I18 cut."""
    n = len(initial)
    started = time.perf_counter()
    preloaded = fixed_base_i18_prefix(initial, fixed_edge, preload_limit)
    validate_i18_clause_bank(preloaded, n, original_edges, fixed_edge)
    for mask in resumed_masks:
        if mask.bit_count() != 18:
            raise AssertionError("resumed cut is not an 18-set")
    if len(set(resumed_masks)) != len(resumed_masks):
        raise AssertionError("resumed cut bank contains duplicates")

    triangle_clauses = [
        [-variables[(a, b)], -variables[(a, c)], -variables[(b, c)]]
        for a, b, c in itertools.combinations(range(n), 3)
    ]
    pool = IDPool(start_from=len(pairs) + 1)
    residual_edges = sorted(original_edges - {fixed_edge})
    exact_cardinality = CardEnc.equals(
        lits=[-variables[edge] for edge in residual_edges],
        bound=RESIDUAL_DELETIONS,
        vpool=pool,
        encoding=EncType.seqcounter,
    ).clauses
    fixed_unit = [[-variables[fixed_edge]]]

    # A resumed mask need not be independent in the singly-deleted input: it
    # was an exact separator witness for a prior candidate, so its full edge
    # hitting clause is nevertheless necessary for every I18-free graph.
    installed: list[int] = []
    seen: set[int] = set()
    for mask in [*preloaded, *resumed_masks]:
        if mask not in seen:
            installed.append(mask)
            seen.add(mask)
    blue_clauses = [hitting_clause(mask, n, variables) for mask in installed]
    clauses = triangle_clauses + exact_cardinality + fixed_unit + blue_clauses
    metadata = {
        "fixed_deleted_edge": list(fixed_edge),
        "fixed_deleted_edge_cannot_be_readded": True,
        "residual_input_edge_deletions": RESIDUAL_DELETIONS,
        "total_input_edge_deletions": TOTAL_BUDGET,
        "cardinality_semantics": "exactly five residual deletions",
        "budget5_proof_dependency": (
            "The frozen checked budget-five theorem covers all solutions with "
            "at most four residual deletions in every triangle-edge branch."
        ),
        "edge_variables": len(pairs),
        "auxiliary_variables": pool.top - len(pairs),
        "maximum_variable": pool.top,
        "triangle_clauses": len(triangle_clauses),
        "exact_residual_cardinality_clauses": len(exact_cardinality),
        "fixed_unit_clauses": 1,
        "preloaded_fixed_base_I18_clauses": len(preloaded),
        "resumed_I18_clauses": len(resumed_masks),
        "installed_unique_I18_clauses": len(installed),
        "installed_I18_sha256": masks_hash(installed),
        "formula_build_seconds": time.perf_counter() - started,
        "initial_clause_count": len(clauses),
    }
    return clauses, pool.top, installed, metadata


def _discovery_worker(
    matrix: str,
    branch: int,
    solver_name: str,
    preload_limit: int,
    resumed_masks: list[int],
    blue_batch_size: int,
    checkpoint: str,
    queue: Any,
) -> None:
    started = time.perf_counter()
    try:
        initial = read_matrix(Path(matrix))
        fixed_edge = BRANCH_EDGES[branch]
        variables, pairs = build_variables(len(initial))
        original_edges = {edge for edge in pairs if edge_present(initial, *edge)}
        clauses, maximum_variable, installed, formula = exact_branch_formula(
            initial,
            variables,
            pairs,
            original_edges,
            fixed_edge,
            preload_limit,
            resumed_masks,
        )
        known = set(installed)
        newly_discovered: list[int] = []
        phases = [
            variables[edge] if edge in original_edges else -variables[edge]
            for edge in pairs
        ]
        phases[variables[fixed_edge] - 1] = -variables[fixed_edge]

        with Solver(name=solver_name, bootstrap_with=clauses) as solver:
            solver.set_phases(phases)
            iterations = 0
            while True:
                iterations += 1
                outcome = solver.solve()
                elapsed = time.perf_counter() - started
                if not outcome:
                    payload = {
                        "status": "UNSAT_FINITE_CUT_BANK",
                        "iterations_this_run": iterations,
                        "new_masks": newly_discovered,
                        "all_lazy_masks": [*resumed_masks, *newly_discovered],
                        "all_lazy_masks_sha256": masks_hash(
                            [*resumed_masks, *newly_discovered]
                        ),
                        "elapsed_seconds": elapsed,
                        "solver_stats": solver.accum_stats(),
                        "formula": formula,
                        "maximum_variable": maximum_variable,
                    }
                    atomic_json(Path(checkpoint), payload)
                    queue.put(payload)
                    return

                model = solver.get_model()
                candidate = rows_from_edge_model(model, len(initial), variables)
                missed = enumerate_cliques(
                    complement(candidate), 18, limit=blue_batch_size
                )
                if not missed:
                    payload = {
                        "status": "SAT_SEPARATED",
                        "iterations_this_run": iterations,
                        "new_masks": newly_discovered,
                        "all_lazy_masks": [*resumed_masks, *newly_discovered],
                        "all_lazy_masks_sha256": masks_hash(
                            [*resumed_masks, *newly_discovered]
                        ),
                        "elapsed_seconds": elapsed,
                        "solver_stats": solver.accum_stats(),
                        "formula": formula,
                        "maximum_variable": maximum_variable,
                        "candidate_rows": candidate,
                    }
                    atomic_json(
                        Path(checkpoint),
                        {k: v for k, v in payload.items() if k != "candidate_rows"},
                    )
                    queue.put(payload)
                    return
                fresh = [mask for mask in missed if mask not in known]
                if not fresh:
                    raise RuntimeError("separator returned only installed I18 cuts")
                for mask in fresh:
                    if mask.bit_count() != 18:
                        raise AssertionError("separator returned non-I18 witness")
                    known.add(mask)
                    newly_discovered.append(mask)
                    solver.add_clause(hitting_clause(mask, len(initial), variables))
                if iterations % 10 == 0:
                    atomic_json(
                        Path(checkpoint),
                        {
                            "status": "RUNNING",
                            "iterations_this_run": iterations,
                            "new_masks": newly_discovered,
                            "all_lazy_masks": [*resumed_masks, *newly_discovered],
                            "all_lazy_masks_sha256": masks_hash(
                                [*resumed_masks, *newly_discovered]
                            ),
                            "elapsed_seconds": elapsed,
                            "solver_stats": solver.accum_stats(),
                            "formula": formula,
                            "maximum_variable": maximum_variable,
                        },
                    )
    except BaseException as error:  # pragma: no cover - subprocess defense
        queue.put(
            {
                "status": "ERROR",
                "elapsed_seconds": time.perf_counter() - started,
                "error": repr(error),
            }
        )


def bounded_discovery(
    matrix: Path,
    branch: int,
    solver_name: str,
    preload_limit: int,
    resumed_masks: list[int],
    blue_batch_size: int,
    checkpoint: Path,
    wall_seconds: float,
) -> dict[str, Any]:
    context = multiprocessing.get_context("fork")
    queue = context.Queue()
    process = context.Process(
        target=_discovery_worker,
        args=(
            str(matrix), branch, solver_name, preload_limit, resumed_masks,
            blue_batch_size, str(checkpoint), queue,
        ),
    )
    started = time.perf_counter()
    process.start()
    next_report = 20.0
    while process.is_alive():
        elapsed = time.perf_counter() - started
        remaining = wall_seconds - elapsed
        if remaining <= 0:
            process.terminate()
            process.join(2.0)
            if process.is_alive():
                process.kill()
                process.join()
            partial: dict[str, Any] = {}
            if checkpoint.is_file():
                partial = json.loads(checkpoint.read_text(encoding="utf-8"))
            queue.close()
            return {
                "status": "UNKNOWN_DISCOVERY_WALL_LIMIT",
                "wall_limit_seconds": wall_seconds,
                "elapsed_seconds": time.perf_counter() - started,
                "last_checkpoint": partial,
            }
        process.join(min(1.0, remaining))
        if elapsed >= next_report:
            summary = "no checkpoint yet"
            if checkpoint.is_file():
                current = json.loads(checkpoint.read_text(encoding="utf-8"))
                summary = (
                    f"iteration={current.get('iterations_this_run')}, "
                    f"all_lazy={len(current.get('all_lazy_masks', []))}"
                )
            print(f"branch {branch} discovery {elapsed:.1f}s: {summary}", flush=True)
            next_report += 20.0
    if queue.empty():
        queue.close()
        return {
            "status": "ERROR",
            "elapsed_seconds": time.perf_counter() - started,
            "exitcode": process.exitcode,
            "error": "discovery child exited without a result",
        }
    result = queue.get()
    result["wall_limit_seconds"] = wall_seconds
    result["exitcode"] = process.exitcode
    queue.close()
    return result


def load_resume_masks(paths: list[Path] | None) -> list[int]:
    """Union one or more independently discovered cut checkpoints."""
    result: list[int] = []
    seen: set[int] = set()
    for path in paths or []:
        if not path.is_file():
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        masks = payload.get("all_lazy_masks")
        if masks is None and payload.get("last_checkpoint"):
            masks = payload["last_checkpoint"].get("all_lazy_masks", [])
        for value in masks or []:
            mask = int(value)
            if mask not in seen:
                seen.add(mask)
                result.append(mask)
    return result


def finish(payload: dict[str, Any], path: Path) -> None:
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    path.write_text(rendered + "\n", encoding="utf-8")


def json_safe(value: Any) -> Any:
    """Normalize TimeoutExpired byte tails returned by some macOS builds."""
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    if isinstance(value, dict):
        return {key: json_safe(item) for key, item in value.items()}
    if isinstance(value, list):
        return [json_safe(item) for item in value]
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--branch", type=int, choices=(0, 1, 2), required=True)
    parser.add_argument("--discovery-solver", default="cadical195")
    parser.add_argument("--preload-i18", type=int, default=1)
    parser.add_argument("--blue-batch-size", type=int, default=1)
    parser.add_argument("--discovery-seconds", type=float, default=300.0)
    parser.add_argument("--proof-seconds", type=float, default=600.0)
    parser.add_argument("--drat-check-seconds", type=float, default=600.0)
    parser.add_argument("--resume", type=Path, action="append")
    parser.add_argument(
        "--prove-resume-bank",
        action="store_true",
        help=(
            "Skip CEGAR and send the reconstructed CNF from --resume cuts "
            "directly to the external proof-producing solver."
        ),
    )
    parser.add_argument("--cadical", type=Path, required=True)
    parser.add_argument("--cadical-source-commit", required=True)
    parser.add_argument("--drat-trim", type=Path, required=True)
    parser.add_argument("--drat-trim-source-commit", required=True)
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()
    if min(args.preload_i18, args.blue_batch_size) <= 0:
        parser.error("clause-bank limits must be positive")
    if min(args.discovery_seconds, args.proof_seconds, args.drat_check_seconds) <= 0:
        parser.error("wall limits must be positive")
    for executable in (args.cadical, args.drat_trim):
        if not executable.is_file() or not os.access(executable, os.X_OK):
            parser.error(f"not an executable: {executable}")

    initial = read_matrix(args.matrix)
    if len(initial) != 100 or sha256(args.matrix) != EXPECTED_INPUT_SHA256:
        raise ValueError("unexpected R(3,18) near-miss input")
    structural_decomposition(initial, TOTAL_BUDGET)
    seed_check = verify(args.matrix, 3, 18)
    if seed_check["searches"]["forbidden_independent_set"]["exists"]:
        raise ValueError("input unexpectedly contains I18")
    fixed_edge = BRANCH_EDGES[args.branch]
    resumed = load_resume_masks(args.resume)
    if args.prove_resume_bank and not resumed:
        parser.error("--prove-resume-bank requires at least one nonempty --resume bank")
    args.artifact_dir.mkdir(parents=True, exist_ok=True)
    prefix = args.artifact_dir / f"r3_18_budget6_branch_{args.branch}"
    checkpoint = prefix.with_suffix(".checkpoint.json")
    started = time.perf_counter()
    if args.prove_resume_bank:
        discovery = {
            "status": "UNSAT_FINITE_CUT_BANK",
            "all_lazy_masks": resumed,
            "proof_mode": "DIRECT_EXTERNAL_PROOF_OF_RESUMED_FINITE_CNF",
            "note": (
                "No solver conclusion is imported from the checkpoint; the "
                "reconstructed finite CNF must independently produce and pass DRAT."
            ),
        }
    else:
        discovery = bounded_discovery(
            args.matrix,
            args.branch,
            args.discovery_solver,
            args.preload_i18,
            resumed,
            args.blue_batch_size,
            checkpoint,
            args.discovery_seconds,
        )
    base: dict[str, Any] = {
        "schema": SCHEMA,
        "status": "RUNNING",
        "input": str(args.matrix.resolve()),
        "input_sha256": sha256(args.matrix),
        "target": {"r": 3, "s": 18, "n": 100},
        "branch": args.branch,
        "fixed_deleted_edge": list(fixed_edge),
        "fixed_edge_cannot_be_readded": True,
        "exact_total_input_edge_deletions": TOTAL_BUDGET,
        "exact_residual_input_edge_deletions": RESIDUAL_DELETIONS,
        "arbitrary_input_nonedge_additions_allowed": True,
        "budget5_checked_proof_required_for_at_most6_conclusion": True,
        "seed_bitset_verification": seed_check,
        "resume_sources": [str(path.resolve()) for path in (args.resume or [])],
        "resumed_I18_cuts": len(resumed),
        "limits": {
            "discovery_wall_seconds": args.discovery_seconds,
            "proof_wall_seconds": args.proof_seconds,
            "drat_check_wall_seconds": args.drat_check_seconds,
            "preloaded_fixed_base_I18": args.preload_i18,
            "blue_batch_size": args.blue_batch_size,
        },
        "tools": {
            "pysat_discovery_solver": args.discovery_solver,
            "external_cadical": str(args.cadical.resolve()),
            "external_cadical_sha256": sha256(args.cadical),
            "external_cadical_source_commit": args.cadical_source_commit,
            "drat_trim": str(args.drat_trim.resolve()),
            "drat_trim_sha256": sha256(args.drat_trim),
            "drat_trim_source_commit": args.drat_trim_source_commit,
        },
        "discovery": discovery,
    }

    if discovery["status"] == "SAT_SEPARATED":
        candidate = discovery.pop("candidate_rows")
        output = prefix.with_suffix(".txt")
        write_matrix(candidate, output)
        checked = verify(output, 3, 18)
        variables, pairs = build_variables(len(initial))
        original = {edge for edge in pairs if edge_present(initial, *edge)}
        final = {edge for edge in pairs if edge_present(candidate, *edge)}
        deleted = sorted(original - final)
        added = sorted(final - original)
        if (
            not checked["valid_ramsey_certificate"]
            or fixed_edge not in deleted
            or len(deleted) != TOTAL_BUDGET
        ):
            raise RuntimeError("separated candidate failed exact-six semantics")
        base.update(
            {
                "status": "SAT_VERIFIED",
                "candidate": str(output.resolve()),
                "candidate_sha256": sha256(output),
                "deleted_edges": [list(edge) for edge in deleted],
                "added_edges": [list(edge) for edge in added],
                "independent_bitset_verification": checked,
                "global_ramsey_implication": "R(3,18) >= 101",
                "elapsed_seconds": time.perf_counter() - started,
            }
        )
        finish(base, args.json)
        return

    if discovery["status"] != "UNSAT_FINITE_CUT_BANK":
        base.update(
            {
                "status": "UNKNOWN",
                "reason": "bounded cut discovery did not reach SAT or UNSAT",
                "global_ramsey_implication": None,
                "elapsed_seconds": time.perf_counter() - started,
            }
        )
        finish(base, args.json)
        return

    lazy_masks = [int(mask) for mask in discovery.pop("all_lazy_masks")]
    variables, pairs = build_variables(len(initial))
    original = {edge for edge in pairs if edge_present(initial, *edge)}
    clauses, maximum_variable, installed, formula = exact_branch_formula(
        initial,
        variables,
        pairs,
        original,
        fixed_edge,
        args.preload_i18,
        lazy_masks,
    )
    cut_path = prefix.with_suffix(".cuts.json")
    atomic_json(
        cut_path,
        {
            "fixed_deleted_edge": list(fixed_edge),
            "masks": [f"{mask:025x}" for mask in installed],
            "masks_sha256": masks_hash(installed),
            "all_masks_are_18_sets": all(mask.bit_count() == 18 for mask in installed),
        },
    )
    cnf_path = prefix.with_suffix(".cnf.gz")
    cnf_raw_hash, cnf_gzip_hash, cnf_bytes, cnf_lines = deterministic_gzip_text(
        cnf_path, dimacs_lines(clauses, maximum_variable)
    )
    base["finite_formula"] = {
        **formula,
        "cut_bank": str(cut_path.resolve()),
        "cut_bank_sha256": sha256(cut_path),
        "final_clause_count": len(clauses),
        "dimacs_gzip": str(cnf_path.resolve()),
        "dimacs_uncompressed_sha256": cnf_raw_hash,
        "dimacs_gzip_sha256": cnf_gzip_hash,
        "dimacs_uncompressed_bytes": cnf_bytes,
        "dimacs_lines": cnf_lines,
    }
    proof_path = prefix.with_suffix(".drat.gz")
    proof = json_safe(
        run_external_proof(args.cadical, cnf_path, proof_path, args.proof_seconds)
    )
    base["external_proof_run"] = proof
    if proof["status"] != "UNSAT_PROOF_WRITTEN":
        base.update(
            {
                "status": "UNKNOWN",
                "reason": "finite CNF discovery was UNSAT but proof emission did not finish",
                "global_ramsey_implication": None,
                "elapsed_seconds": time.perf_counter() - started,
            }
        )
        finish(base, args.json)
        return
    drat_check = verify_drat_trace(
        args.drat_trim, cnf_path, proof_path, args.drat_check_seconds
    )
    base["drat_check"] = drat_check
    base.update(
        {
            "status": (
                "UNSAT_PROOF_VERIFIED"
                if drat_check["status"] == "VERIFIED"
                else "UNKNOWN_PROOF_UNVERIFIED"
            ),
            "global_ramsey_implication": None,
            "elapsed_seconds": time.perf_counter() - started,
        }
    )
    finish(base, args.json)


if __name__ == "__main__":
    main()
