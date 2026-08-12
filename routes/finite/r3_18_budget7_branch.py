#!/usr/bin/env python3
"""Recoverable exact-seven repair search for the frozen R(3,18) near miss.

Each branch fixes one edge of the unique input triangle absent and requires
exactly six further input-edge deletions.  Original nonedges remain free.
The checked budget-six universal I18 bank is reused only as a collection of
universally necessary hitting clauses.  Discovery is hard wall bounded;
UNKNOWN is never promoted.  A finite-bank UNSAT label is promoted only after
a fresh external DRAT is accepted by pinned drat-trim.  A separated SAT model
is promoted only after independent bitset and SAT certificate checks.
"""

from __future__ import annotations

import argparse
import itertools
import json
import multiprocessing
import os
import time
from pathlib import Path
from typing import Any, Iterable

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Solver

try:
    from .bounded_deletion_sat_cegar import build_variables
    from .budget8_next import (
        deterministic_gzip_text,
        masks_hash,
        sha256,
        verify_drat_trace,
    )
    from .graph_utils import enumerate_cliques, write_matrix
    from .new_basin_search import edge_present, rows_from_edge_model
    from .r3_18_branch0_two_stage import atomic_json, run_external_proof
    from .r3_18_budget5_branch import (
        EXPECTED_INPUT_SHA256,
        EXPECTED_TRIANGLE,
        hitting_clause,
        structural_decomposition,
    )
    from .verify_ramsey import complement, read_matrix, verify
    from .verify_ramsey_sat import sat_contains_clique
except ImportError:  # pragma: no cover - direct execution
    from bounded_deletion_sat_cegar import build_variables
    from budget8_next import (
        deterministic_gzip_text,
        masks_hash,
        sha256,
        verify_drat_trace,
    )
    from graph_utils import enumerate_cliques, write_matrix
    from new_basin_search import edge_present, rows_from_edge_model
    from r3_18_branch0_two_stage import atomic_json, run_external_proof
    from r3_18_budget5_branch import (
        EXPECTED_INPUT_SHA256,
        EXPECTED_TRIANGLE,
        hitting_clause,
        structural_decomposition,
    )
    from verify_ramsey import complement, read_matrix, verify
    from verify_ramsey_sat import sat_contains_clique


SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch-v1"
SUMMARY_SCHEMA = "ramsey-r3-18-n100-exact-budget7-summary-v1"
BRANCH_EDGES = tuple(itertools.combinations(EXPECTED_TRIANGLE, 2))
TOTAL_DELETIONS = 7
RESIDUAL_DELETIONS = 6
EXPECTED_UNIVERSAL_BANK_SHA256 = (
    "91b5709248ff641a315f5a0389b4f3fde3d38514f3b1a8b31b6cad31224f250b"
)
EXPECTED_UNIVERSAL_MASKS = 251_771
EXPECTED_BUDGET6_SUMMARY_SHA256 = (
    "0abd30457c039c1c5fbba5890153c8a0c5d8558e196e7c0561410cefe37afa6a"
)
EXPECTED_BUDGET6_REFEREE_SHA256 = (
    "1bb634ed1a6181064ac2ae0277ea6582cd2627a76a92208907cc1532d49bfede"
)
EXPECTED_BUDGET6_BRANCH_PROOFS = (
    {
        "branch": 0,
        "fixed_deleted_edge": [97, 98],
        "cnf_gzip_sha256": "47052de808b98598f2f144251a6ad73c1415dd00fef9e04b99ffe2f176229fbf",
        "drat_gzip_sha256": "4d948ab34f1d2475af6efe943e0a4899827c78b96c2bc3835b5161f189c26bb5",
    },
    {
        "branch": 1,
        "fixed_deleted_edge": [97, 99],
        "cnf_gzip_sha256": "a438c9fef4d99ae516829e4405da8c9f079398501361f9c5f69f46a494ffad14",
        "drat_gzip_sha256": "cfe694fd728903ee9ac9f08a66ade64faf7e68763246d1d52ca29a85727494ec",
    },
    {
        "branch": 2,
        "fixed_deleted_edge": [98, 99],
        "cnf_gzip_sha256": "c51fed43eeca3becf64bcdfbe747a4fdf3e516ce0e6a02d7d867941b87a99c06",
        "drat_gzip_sha256": "c9648a4e38c17dcdfe97d873095eda002abc689b3b3bd93f02fc8a369198c4b9",
    },
)


def parse_mask(value: Any) -> int:
    if isinstance(value, int):
        return value
    if not isinstance(value, str):
        raise TypeError(f"unsupported mask type: {type(value)!r}")
    stripped = value.strip().lower()
    if stripped.startswith("0x"):
        return int(stripped, 16)
    # Stored universal banks use fixed-width hexadecimal strings.  Decimal
    # checkpoint strings contain only digits and are parsed as decimal.
    return int(stripped, 16 if any(c in "abcdef" for c in stripped) or len(stripped) == 25 else 10)


def validate_masks(values: Iterable[Any]) -> list[int]:
    result: list[int] = []
    seen: set[int] = set()
    for value in values:
        mask = parse_mask(value)
        if mask < 0 or mask.bit_count() != 18 or mask >> 100:
            raise ValueError("cut bank contains a non-18-subset of [100]")
        if mask not in seen:
            seen.add(mask)
            result.append(mask)
    return result


def load_universal_bank(path: Path) -> tuple[list[int], dict[str, Any]]:
    if sha256(path) != EXPECTED_UNIVERSAL_BANK_SHA256:
        raise ValueError("unexpected universal cut-bank identity")
    payload = json.loads(path.read_text(encoding="utf-8"))
    masks = validate_masks(payload.get("masks", []))
    if len(masks) != EXPECTED_UNIVERSAL_MASKS:
        raise ValueError("unexpected universal cut-bank cardinality")
    if masks_hash(masks) != payload.get("masks_sha256"):
        raise ValueError("universal cut-bank ordered digest mismatch")
    return masks, {
        "path": str(path.resolve()),
        "sha256": sha256(path),
        "masks": len(masks),
        "ordered_masks_sha256": masks_hash(masks),
        "universality_reason": (
            "Each mask is an 18-vertex set; its complete positive edge clause "
            "is necessary for every graph with independence number below 18."
        ),
    }


def _extract_new_masks(payload: Any) -> list[Any]:
    if not isinstance(payload, dict):
        return []
    for key in ("new_masks", "additional_masks"):
        if isinstance(payload.get(key), list):
            return payload[key]
    for key in ("last_checkpoint", "discovery"):
        nested = _extract_new_masks(payload.get(key))
        if nested:
            return nested
    return []


def load_incremental_masks(paths: list[Path] | None) -> list[int]:
    values: list[Any] = []
    for path in paths or []:
        if path.is_file():
            values.extend(_extract_new_masks(json.loads(path.read_text(encoding="utf-8"))))
    return validate_masks(values)


def validate_budget6_dependency(payload: dict[str, Any]) -> None:
    if payload.get("status") != "ALL_THREE_EXACT_BUDGET6_BRANCHES_UNSAT_PROOF_VERIFIED":
        raise ValueError("budget-six dependency is not proof-verified")
    branches = payload.get("branches")
    if not isinstance(branches, list) or len(branches) != 3:
        raise ValueError("budget-six dependency does not contain exactly three branches")
    for actual, expected in zip(branches, EXPECTED_BUDGET6_BRANCH_PROOFS):
        if actual.get("branch") != expected["branch"]:
            raise ValueError("budget-six branch ordering/identity mismatch")
        if actual.get("fixed_deleted_edge") != expected["fixed_deleted_edge"]:
            raise ValueError("budget-six fixed-edge identity mismatch")
        if actual.get("status") != "UNSAT_PROOF_VERIFIED":
            raise ValueError("budget-six branch lacks a verified proof")
        if actual.get("formula", {}).get("dimacs_gzip_sha256") != expected["cnf_gzip_sha256"]:
            raise ValueError("budget-six branch CNF identity mismatch")
        proof = actual.get("proof", {})
        if proof.get("drat_gzip_sha256") != expected["drat_gzip_sha256"]:
            raise ValueError("budget-six branch DRAT identity mismatch")
        if proof.get("checker_status") != "VERIFIED":
            raise ValueError("budget-six branch checker status mismatch")


def structural_formula(
    n: int,
    variables: dict[tuple[int, int], int],
    pairs: list[tuple[int, int]],
    original_edges: set[tuple[int, int]],
    fixed_edge: tuple[int, int],
) -> tuple[list[list[int]], int, dict[str, Any]]:
    if fixed_edge not in original_edges or len(original_edges) != 827:
        raise ValueError("unexpected input-edge family")
    triangles = [
        [-variables[(a, b)], -variables[(a, c)], -variables[(b, c)]]
        for a, b, c in itertools.combinations(range(n), 3)
    ]
    residual_edges = sorted(original_edges - {fixed_edge})
    if len(residual_edges) != 826:
        raise AssertionError("exact-seven counter must contain 826 literals")
    pool = IDPool(start_from=len(pairs) + 1)
    counter = CardEnc.equals(
        lits=[-variables[edge] for edge in residual_edges],
        bound=RESIDUAL_DELETIONS,
        vpool=pool,
        encoding=EncType.seqcounter,
    ).clauses
    clauses = triangles + counter + [[-variables[fixed_edge]]]
    metadata = {
        "edge_variables": len(pairs),
        "auxiliary_variables": pool.top - len(pairs),
        "maximum_variable": pool.top,
        "triangle_clauses": len(triangles),
        "exact_six_residual_counter_literals": len(residual_edges),
        "exact_six_residual_counter_clauses": len(counter),
        "fixed_negative_units": 1,
        "structural_clauses": len(clauses),
        "fixed_deleted_edge": list(fixed_edge),
        "fixed_deleted_edge_cannot_be_readded": True,
        "exact_total_input_edge_deletions": TOTAL_DELETIONS,
        "exact_residual_input_edge_deletions": RESIDUAL_DELETIONS,
        "original_nonedge_variables_in_deletion_counter": 0,
        "arbitrary_original_nonedge_additions_allowed": True,
    }
    return clauses, pool.top, metadata


def _checkpoint_payload(
    status: str,
    branch: int,
    fixed_edge: tuple[int, int],
    base_info: dict[str, Any],
    resume_sources: list[str],
    resumed_count: int,
    new_masks: list[int],
    iterations: int,
    elapsed: float,
    formula: dict[str, Any],
    solver_stats: dict[str, Any],
) -> dict[str, Any]:
    return {
        "schema": SCHEMA,
        "status": status,
        "branch": branch,
        "fixed_deleted_edge": list(fixed_edge),
        "base_universal_bank": base_info,
        "resume_sources": resume_sources,
        "resumed_additional_masks": resumed_count,
        "new_masks": new_masks,
        "new_masks_sha256": masks_hash(new_masks),
        "iterations_this_run": iterations,
        "elapsed_seconds": elapsed,
        "formula": formula,
        "solver_stats": solver_stats,
    }


def _worker(
    matrix: str,
    branch: int,
    solver_name: str,
    base_masks: list[int],
    base_info: dict[str, Any],
    resume_sources: list[str],
    resumed_masks: list[int],
    batch_size: int,
    checkpoint: str,
    queue: Any,
) -> None:
    started = time.perf_counter()
    try:
        rows = read_matrix(Path(matrix))
        variables, pairs = build_variables(len(rows))
        original = {edge for edge in pairs if edge_present(rows, *edge)}
        fixed_edge = BRANCH_EDGES[branch]
        clauses, maximum_variable, metadata = structural_formula(
            len(rows), variables, pairs, original, fixed_edge
        )
        base_set = set(base_masks)
        resumed = [mask for mask in resumed_masks if mask not in base_set]
        known = base_set | set(resumed)
        new_masks: list[int] = []
        phases = [
            variables[edge] if edge in original else -variables[edge]
            for edge in pairs
        ]
        phases[variables[fixed_edge] - 1] = -variables[fixed_edge]

        with Solver(name=solver_name, bootstrap_with=clauses) as solver:
            for mask in base_masks:
                solver.add_clause(hitting_clause(mask, len(rows), variables))
            for mask in resumed:
                solver.add_clause(hitting_clause(mask, len(rows), variables))
            solver.set_phases(phases)
            formula = {
                **metadata,
                "base_universal_I18_clauses": len(base_masks),
                "resumed_additional_I18_clauses": len(resumed),
                "initial_total_clauses": len(clauses) + len(base_masks) + len(resumed),
                "installed_clauses_are_only_structural_or_universal_I18": True,
            }
            atomic_json(
                Path(checkpoint),
                _checkpoint_payload(
                    "READY", branch, fixed_edge, base_info, resume_sources,
                    len(resumed), new_masks, 0, time.perf_counter() - started,
                    formula, solver.accum_stats(),
                ),
            )
            iterations = 0
            while True:
                iterations += 1
                outcome = solver.solve()
                elapsed = time.perf_counter() - started
                if not outcome:
                    payload = _checkpoint_payload(
                        "UNSAT_FINITE_CUT_BANK", branch, fixed_edge, base_info,
                        resume_sources, len(resumed), new_masks, iterations,
                        elapsed, formula, solver.accum_stats(),
                    )
                    atomic_json(Path(checkpoint), payload)
                    queue.put(payload)
                    return

                model = solver.get_model()
                candidate = rows_from_edge_model(model, len(rows), variables)
                missed = enumerate_cliques(
                    complement(candidate), 18, limit=batch_size
                )
                if not missed:
                    payload = _checkpoint_payload(
                        "SAT_SEPARATED", branch, fixed_edge, base_info,
                        resume_sources, len(resumed), new_masks, iterations,
                        elapsed, formula, solver.accum_stats(),
                    )
                    atomic_json(Path(checkpoint), payload)
                    payload["candidate_rows"] = candidate
                    queue.put(payload)
                    return
                fresh = [mask for mask in missed if mask not in known]
                if not fresh:
                    raise RuntimeError("exact separator returned only installed cuts")
                for mask in fresh:
                    if mask.bit_count() != 18:
                        raise AssertionError("separator returned a non-I18 mask")
                    known.add(mask)
                    new_masks.append(mask)
                    solver.add_clause(hitting_clause(mask, len(rows), variables))
                atomic_json(
                    Path(checkpoint),
                    _checkpoint_payload(
                        "RUNNING", branch, fixed_edge, base_info,
                        resume_sources, len(resumed), new_masks, iterations,
                        elapsed, formula, solver.accum_stats(),
                    ),
                )
    except BaseException as error:  # pragma: no cover - child defense
        queue.put(
            {
                "schema": SCHEMA,
                "status": "ERROR",
                "branch": branch,
                "elapsed_seconds": time.perf_counter() - started,
                "error": repr(error),
            }
        )


def bounded_discovery(
    matrix: Path,
    branch: int,
    solver_name: str,
    base_masks: list[int],
    base_info: dict[str, Any],
    resume_sources: list[str],
    resumed_masks: list[int],
    batch_size: int,
    checkpoint: Path,
    wall_seconds: float,
) -> dict[str, Any]:
    context = multiprocessing.get_context("fork")
    queue = context.Queue()
    process = context.Process(
        target=_worker,
        args=(
            str(matrix), branch, solver_name, base_masks, base_info,
            resume_sources, resumed_masks, batch_size, str(checkpoint), queue,
        ),
    )
    started = time.perf_counter()
    process.start()
    while process.is_alive():
        remaining = wall_seconds - (time.perf_counter() - started)
        if remaining <= 0:
            process.terminate()
            process.join(2.0)
            if process.is_alive():
                process.kill()
                process.join()
            last = (
                json.loads(checkpoint.read_text(encoding="utf-8"))
                if checkpoint.is_file() else {}
            )
            queue.close()
            return {
                "schema": SCHEMA,
                "status": "UNKNOWN_DISCOVERY_WALL_LIMIT",
                "branch": branch,
                "wall_limit_seconds": wall_seconds,
                "elapsed_seconds": time.perf_counter() - started,
                "last_checkpoint": last,
            }
        process.join(min(1.0, remaining))
    if queue.empty():
        queue.close()
        return {
            "schema": SCHEMA,
            "status": "ERROR",
            "branch": branch,
            "elapsed_seconds": time.perf_counter() - started,
            "exitcode": process.exitcode,
            "error": "child exited without a result",
        }
    result = queue.get()
    result["wall_limit_seconds"] = wall_seconds
    result["exitcode"] = process.exitcode
    queue.close()
    return result


def cnf_lines(
    structural: list[list[int]],
    masks: list[int],
    variables: dict[tuple[int, int], int],
    maximum_variable: int,
) -> Iterable[str]:
    yield f"p cnf {maximum_variable} {len(structural) + len(masks)}\n"
    for clause in structural:
        yield " ".join(map(str, clause)) + " 0\n"
    for mask in masks:
        yield " ".join(map(str, hitting_clause(mask, 100, variables))) + " 0\n"


def independent_candidate_checks(path: Path) -> dict[str, Any]:
    bitset = verify(path, 3, 18)
    rows = read_matrix(path)
    clique_sat = sat_contains_clique(rows, 3, "cadical195")
    independent_sat = sat_contains_clique(complement(rows), 18, "cadical195")
    sat_valid = not clique_sat["exists"] and not independent_sat["exists"]
    return {
        "bitset": bitset,
        "independent_sat": {
            "valid_ramsey_certificate": sat_valid,
            "forbidden_triangle": clique_sat,
            "forbidden_independent_18_set": independent_sat,
        },
        "both_independent_checks_pass": (
            bitset["valid_ramsey_certificate"] and sat_valid
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--branch", type=int, choices=(0, 1, 2), required=True)
    parser.add_argument("--universal-bank", type=Path, required=True)
    parser.add_argument("--budget6-summary", type=Path, required=True)
    parser.add_argument("--budget6-referee", type=Path, required=True)
    parser.add_argument("--resume", type=Path, action="append")
    parser.add_argument("--solver", default="cadical195")
    parser.add_argument("--batch-size", type=int, default=256)
    parser.add_argument("--discovery-seconds", type=float, default=300.0)
    parser.add_argument("--proof-seconds", type=float, default=300.0)
    parser.add_argument("--drat-seconds", type=float, default=360.0)
    parser.add_argument("--cadical", type=Path, required=True)
    parser.add_argument("--cadical-source-commit", required=True)
    parser.add_argument("--drat-trim", type=Path, required=True)
    parser.add_argument("--drat-trim-source-commit", required=True)
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()
    if min(args.batch_size, args.discovery_seconds, args.proof_seconds, args.drat_seconds) <= 0:
        parser.error("all sizes and wall limits must be positive")
    for executable in (args.cadical, args.drat_trim):
        if not executable.is_file() or not os.access(executable, os.X_OK):
            parser.error(f"not executable: {executable}")
    if sha256(args.matrix) != EXPECTED_INPUT_SHA256:
        raise ValueError("unexpected near-miss input")
    if sha256(args.budget6_summary) != EXPECTED_BUDGET6_SUMMARY_SHA256:
        raise ValueError("unexpected budget-six proof dependency")
    if sha256(args.budget6_referee) != EXPECTED_BUDGET6_REFEREE_SHA256:
        raise ValueError("unexpected complete budget-six referee dependency")
    budget6 = json.loads(args.budget6_summary.read_text(encoding="utf-8"))
    validate_budget6_dependency(budget6)

    rows = read_matrix(args.matrix)
    structural_decomposition(rows, TOTAL_DELETIONS)
    seed = verify(args.matrix, 3, 18)
    if seed["searches"]["forbidden_independent_set"]["exists"]:
        raise ValueError("near miss unexpectedly has an I18")
    base_masks, base_info = load_universal_bank(args.universal_bank)
    resumed = load_incremental_masks(args.resume)
    resume_sources = [str(path.resolve()) for path in (args.resume or [])]
    args.artifact_dir.mkdir(parents=True, exist_ok=True)
    prefix = args.artifact_dir / f"r3_18_budget7_branch_{args.branch}"
    checkpoint = prefix.with_suffix(".checkpoint.json")
    started = time.perf_counter()
    discovery = bounded_discovery(
        args.matrix, args.branch, args.solver, base_masks, base_info,
        resume_sources, resumed, args.batch_size, checkpoint,
        args.discovery_seconds,
    )
    result: dict[str, Any] = {
        "schema": SCHEMA,
        "status": "RUNNING",
        "input": str(args.matrix.resolve()),
        "input_sha256": sha256(args.matrix),
        "target": {"r": 3, "s": 18, "n": 100},
        "branch": args.branch,
        "fixed_deleted_edge": list(BRANCH_EDGES[args.branch]),
        "exact_total_input_edge_deletions": TOTAL_DELETIONS,
        "exact_residual_input_edge_deletions": RESIDUAL_DELETIONS,
        "arbitrary_original_nonedge_additions_allowed": True,
        "budget_at_most_6_proof_dependency": {
            "path": str(args.budget6_summary.resolve()),
            "sha256": sha256(args.budget6_summary),
            "status": budget6["status"],
            "complete_referee": str(args.budget6_referee.resolve()),
            "complete_referee_sha256": sha256(args.budget6_referee),
            "all_three_branch_identities_cross_checked": True,
        },
        "universal_cut_bank": base_info,
        "resume_sources": resume_sources,
        "limits": {
            "discovery_wall_seconds": args.discovery_seconds,
            "proof_wall_seconds": args.proof_seconds,
            "drat_wall_seconds": args.drat_seconds,
            "batch_size": args.batch_size,
        },
        "tools": {
            "discovery_solver": args.solver,
            "cadical": str(args.cadical.resolve()),
            "cadical_sha256": sha256(args.cadical),
            "cadical_source_commit": args.cadical_source_commit,
            "drat_trim": str(args.drat_trim.resolve()),
            "drat_trim_sha256": sha256(args.drat_trim),
            "drat_trim_source_commit": args.drat_trim_source_commit,
        },
        "seed_bitset_check": seed,
        "discovery": discovery,
    }

    if discovery["status"] == "SAT_SEPARATED":
        candidate = discovery.pop("candidate_rows")
        candidate_path = prefix.with_suffix(".txt")
        write_matrix(candidate, candidate_path)
        checks = independent_candidate_checks(candidate_path)
        variables, pairs = build_variables(len(rows))
        original = {edge for edge in pairs if edge_present(rows, *edge)}
        final = {edge for edge in pairs if edge_present(candidate, *edge)}
        deleted = sorted(original - final)
        added = sorted(final - original)
        if (
            not checks["both_independent_checks_pass"]
            or BRANCH_EDGES[args.branch] not in deleted
            or len(deleted) != TOTAL_DELETIONS
        ):
            result.update(
                {
                    "status": "ERROR_CANDIDATE_FAILED_INDEPENDENT_CHECK",
                    "candidate": str(candidate_path.resolve()),
                    "candidate_sha256": sha256(candidate_path),
                    "candidate_checks": checks,
                    "global_ramsey_implication": None,
                }
            )
        else:
            verification_path = prefix.with_suffix(".verification.json")
            verification = {
                "candidate": str(candidate_path.resolve()),
                "candidate_sha256": sha256(candidate_path),
                "deleted_edges": [list(edge) for edge in deleted],
                "added_edges": [list(edge) for edge in added],
                "checks": checks,
                "valid_R3_18_n100_certificate": True,
                "certified_lower_bound": "R(3,18) >= 101",
            }
            atomic_json(verification_path, verification)
            result.update(
                {
                    "status": "SAT_WITNESS_INDEPENDENTLY_VERIFIED",
                    "candidate": str(candidate_path.resolve()),
                    "candidate_sha256": sha256(candidate_path),
                    "candidate_verification": str(verification_path.resolve()),
                    "candidate_verification_sha256": sha256(verification_path),
                    "deleted_edges": [list(edge) for edge in deleted],
                    "added_edges": [list(edge) for edge in added],
                    "global_ramsey_implication": "R(3,18) >= 101",
                }
            )
    elif discovery["status"] == "UNSAT_FINITE_CUT_BANK":
        new_masks = validate_masks(discovery.get("new_masks", []))
        all_masks = validate_masks([*base_masks, *resumed, *new_masks])
        variables, pairs = build_variables(len(rows))
        original = {edge for edge in pairs if edge_present(rows, *edge)}
        structural, maximum_variable, formula = structural_formula(
            len(rows), variables, pairs, original, BRANCH_EDGES[args.branch]
        )
        cut_path = prefix.with_suffix(".cuts.json")
        atomic_json(
            cut_path,
            {
                "schema": SCHEMA,
                "branch": args.branch,
                "fixed_deleted_edge": list(BRANCH_EDGES[args.branch]),
                "masks": [f"{mask:025x}" for mask in all_masks],
                "masks_sha256": masks_hash(all_masks),
                "all_masks_are_18_sets": True,
            },
        )
        cnf_path = prefix.with_suffix(".cnf.gz")
        raw_hash, gzip_hash, raw_bytes, lines = deterministic_gzip_text(
            cnf_path,
            cnf_lines(structural, all_masks, variables, maximum_variable),
        )
        result["finite_formula"] = {
            **formula,
            "I18_hitting_clauses": len(all_masks),
            "total_clauses": len(structural) + len(all_masks),
            "cut_bank": str(cut_path.resolve()),
            "cut_bank_sha256": sha256(cut_path),
            "dimacs_gzip": str(cnf_path.resolve()),
            "dimacs_gzip_sha256": gzip_hash,
            "dimacs_uncompressed_sha256": raw_hash,
            "dimacs_uncompressed_bytes": raw_bytes,
            "dimacs_lines": lines,
        }
        proof_path = prefix.with_suffix(".drat.gz")
        proof = run_external_proof(
            args.cadical, cnf_path, proof_path, args.proof_seconds
        )
        result["external_proof"] = proof
        if proof.get("status") == "UNSAT_PROOF_WRITTEN":
            drat = verify_drat_trace(
                args.drat_trim, cnf_path, proof_path, args.drat_seconds
            )
            result["drat_check"] = drat
            result["status"] = (
                "UNSAT_PROOF_VERIFIED"
                if drat.get("status") == "VERIFIED"
                else "UNKNOWN_PROOF_UNVERIFIED"
            )
        else:
            result["status"] = "UNKNOWN_PROOF_NOT_COMPLETED"
        result["global_ramsey_implication"] = None
    else:
        result.update(
            {
                "status": "UNKNOWN",
                "reason": "bounded discovery reached neither a verified SAT witness nor a checked UNSAT proof",
                "global_ramsey_implication": None,
            }
        )

    result["elapsed_seconds"] = time.perf_counter() - started
    atomic_json(args.json, result)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
