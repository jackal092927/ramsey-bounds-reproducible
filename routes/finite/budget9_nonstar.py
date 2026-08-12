#!/usr/bin/env python3
"""Proof-carrying budget-nine search around the frozen non-star 61 seed.

The structural reduction is the same one validated for budget eight: retaining
the hub edge (28,60) requires one deletion in each of ten disjoint spoke pairs,
so budget nine still forces the hub absent.  The remaining input triangle gives
three exhaustive branches.  Each branch fixes two deletions and permits seven
more input-edge deletions, while arbitrary input nonedges remain free.

The initial branch CNF contains every triangle clause, the exact residual
deletion counter, and all independent 13-sets of the fixed-deletion base.  If
that relaxation is SAT, exact CEGAR adds newly exposed independent 13-sets.
UNSAT is reported as a proved endpoint only when every branch's frozen DRAT
trace is accepted by the separately invoked checker.  A bounded outcome is
always recorded as UNKNOWN.
"""

from __future__ import annotations

import argparse
import itertools
import json
import os
import time
from pathlib import Path
from typing import Any

from pysat.solvers import Solver

try:
    from .bounded_deletion_sat_cegar import build_variables
    from .budget8_next import (
        HUB,
        bounded_cadical_replay,
        branch_formula,
        deterministic_gzip_text,
        dimacs_lines,
        hitting_clause,
        masks_hash,
        proof_lines,
        sha256,
        structural_decomposition,
        verify_drat_trace,
    )
    from .graph_utils import enumerate_cliques, write_matrix
    from .new_basin_search import (
        bounded_cegar_loop,
        edge_present,
        rows_from_edge_model,
    )
    from .verify_ramsey import complement, read_matrix, verify
except ImportError:  # pragma: no cover - direct script execution
    from bounded_deletion_sat_cegar import build_variables
    from budget8_next import (
        HUB,
        bounded_cadical_replay,
        branch_formula,
        deterministic_gzip_text,
        dimacs_lines,
        hitting_clause,
        masks_hash,
        proof_lines,
        sha256,
        structural_decomposition,
        verify_drat_trace,
    )
    from graph_utils import enumerate_cliques, write_matrix
    from new_basin_search import (
        bounded_cegar_loop,
        edge_present,
        rows_from_edge_model,
    )
    from verify_ramsey import complement, read_matrix, verify


SCHEMA = "ramsey-r3-13-n61-nonstar-budget9-branch-v1"


def solve_branch(
    index: int,
    second_edge: tuple[int, int],
    initial: list[int],
    variables: dict[tuple[int, int], int],
    pairs: list[tuple[int, int]],
    original_edges: set[tuple[int, int]],
    args: argparse.Namespace,
) -> dict[str, Any]:
    fixed = {HUB, second_edge}
    residual_budget = args.budget - len(fixed)
    clauses, maximum_variable, base_masks, formula = branch_formula(
        initial,
        variables,
        pairs,
        original_edges,
        fixed,
        residual_budget,
    )
    known_masks = set(base_masks)
    lazy_masks: list[int] = []
    accepted: list[int] | None = None

    def separate(model: list[int]) -> list[list[int]]:
        nonlocal accepted
        candidate = rows_from_edge_model(model, len(initial), variables)
        masks = enumerate_cliques(
            complement(candidate), 13, limit=args.blue_batch_size
        )
        if not masks:
            accepted = candidate
            return []
        new_masks = [mask for mask in masks if mask not in known_masks]
        if not new_masks:
            raise RuntimeError("SAT model violates only already installed I13 clauses")
        known_masks.update(new_masks)
        lazy_masks.extend(new_masks)
        new_clauses = [
            hitting_clause(mask, len(initial), variables) for mask in new_masks
        ]
        clauses.extend(new_clauses)
        return new_clauses

    # Prefer the input graph, except for fixed negative units.  This affects
    # search only; every assignment remains available to the solver.
    phases = [
        variables[edge] if edge in original_edges else -variables[edge]
        for edge in pairs
    ]
    with Solver(
        name="glucose42", with_proof=True, bootstrap_with=clauses
    ) as solver:
        solver.set_phases(phases)
        status, model, run = bounded_cegar_loop(
            solver,
            separate,
            args.conflicts_per_call,
            args.max_conflicts_per_branch,
            args.per_call_seconds,
            args.max_seconds_per_branch,
        )
        proof = solver.get_proof() if status == "UNSAT" else []

    result: dict[str, Any] = {
        "branch": index,
        "second_deleted_edge": list(second_edge),
        "status": status,
        "formula": formula,
        "lazy_I13_clauses_added": len(lazy_masks),
        "lazy_I13_masks_sha256": masks_hash(lazy_masks),
        "run": run,
    }
    prefix = args.artifact_dir / f"budget9_nonstar_branch_{index}"

    if status == "UNSAT":
        cnf_path = prefix.with_suffix(".cnf.gz")
        proof_path = prefix.with_suffix(".drat.gz")
        cnf_raw_hash, cnf_gzip_hash, cnf_raw_bytes, cnf_lines = (
            deterministic_gzip_text(
                cnf_path, dimacs_lines(clauses, maximum_variable)
            )
        )
        proof_raw_hash, proof_gzip_hash, proof_raw_bytes, proof_line_count = (
            deterministic_gzip_text(proof_path, proof_lines(proof))
        )
        drat_check = (
            verify_drat_trace(
                args.drat_trim,
                cnf_path,
                proof_path,
                args.drat_check_seconds,
            )
            if args.drat_trim is not None
            else {
                "status": "NOT_RUN",
                "reason": "No --drat-trim executable was supplied.",
            }
        )
        result.update(
            {
                "dimacs_gzip": str(cnf_path.resolve()),
                "dimacs_uncompressed_sha256": cnf_raw_hash,
                "dimacs_gzip_sha256": cnf_gzip_hash,
                "dimacs_uncompressed_bytes": cnf_raw_bytes,
                "dimacs_lines": cnf_lines,
                "drat_gzip": str(proof_path.resolve()),
                "drat_uncompressed_sha256": proof_raw_hash,
                "drat_gzip_sha256": proof_gzip_hash,
                "drat_uncompressed_bytes": proof_raw_bytes,
                "drat_lines": proof_line_count,
                "drat_check": drat_check,
                "bounded_cadical195_cross_replay": bounded_cadical_replay(
                    clauses, args.cross_solver_seconds
                ),
            }
        )
    elif status == "SAT":
        if accepted is None or model is None:
            raise RuntimeError("SAT without a fully separated candidate")
        output = prefix.with_suffix(".txt")
        write_matrix(accepted, output)
        verification = verify(output, 3, 13)
        if not verification["valid_ramsey_certificate"]:
            raise RuntimeError("independent bitset verifier rejected SAT candidate")
        final_edges = {edge for edge in pairs if edge_present(accepted, *edge)}
        deleted = sorted(original_edges - final_edges)
        if len(deleted) > args.budget:
            raise RuntimeError("SAT reconstruction exceeds deletion budget")
        result.update(
            {
                "output": str(output.resolve()),
                "output_sha256": sha256(output),
                "deleted_edges": [list(edge) for edge in deleted],
                "added_edges": [
                    list(edge) for edge in sorted(final_edges - original_edges)
                ],
                "independent_bitset_verification": verification,
            }
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--budget", type=int, default=9)
    parser.add_argument("--conflicts-per-call", type=int, default=20_000)
    parser.add_argument("--max-conflicts-per-branch", type=int, default=500_000)
    parser.add_argument("--per-call-seconds", type=float, default=10.0)
    parser.add_argument("--max-seconds-per-branch", type=float, default=120.0)
    parser.add_argument("--cross-solver-seconds", type=float, default=120.0)
    parser.add_argument("--drat-trim", type=Path)
    parser.add_argument("--drat-trim-source-commit")
    parser.add_argument("--drat-check-seconds", type=float, default=180.0)
    parser.add_argument("--blue-batch-size", type=int, default=1024)
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()
    if args.budget != 9:
        parser.error("this proof search is frozen specifically for budget nine")
    if min(
        args.conflicts_per_call,
        args.max_conflicts_per_branch,
        args.blue_batch_size,
    ) <= 0:
        parser.error("integer limits must be positive")
    if min(
        args.per_call_seconds,
        args.max_seconds_per_branch,
        args.cross_solver_seconds,
        args.drat_check_seconds,
    ) <= 0:
        parser.error("wall limits must be positive")
    if args.drat_trim is not None and not args.drat_trim.is_file():
        parser.error("--drat-trim must name an existing executable file")

    args.artifact_dir.mkdir(parents=True, exist_ok=True)
    initial = read_matrix(args.matrix)
    if len(initial) != 61:
        raise ValueError("budget-nine route requires the frozen 61-vertex seed")
    structural_proof, branch_edges = structural_decomposition(initial, args.budget)
    variables, pairs = build_variables(len(initial))
    original_edges = {edge for edge in pairs if edge_present(initial, *edge)}

    started = time.perf_counter()
    branches = []
    for index, edge in enumerate(branch_edges):
        branch = solve_branch(
            index, edge, initial, variables, pairs, original_edges, args
        )
        branches.append(branch)
        print(
            f"branch {index} {edge}: {branch['status']}; "
            f"I13={branch['formula']['preloaded_fixed_base_I13_clauses']}; "
            f"seconds={branch['run']['elapsed_seconds']:.3f}",
            flush=True,
        )

    statuses = [branch["status"] for branch in branches]
    proof_statuses = [
        branch.get("drat_check", {}).get("status") for branch in branches
    ]
    if any(status == "SAT" for status in statuses):
        global_status = "SAT"
        conclusion = "At least one branch produced an independently verified candidate."
    elif statuses == ["UNSAT", "UNSAT", "UNSAT"] and proof_statuses == [
        "VERIFIED",
        "VERIFIED",
        "VERIFIED",
    ]:
        global_status = "UNSAT_PROOF_VERIFIED"
        conclusion = (
            "Every at-most-nine-deletion completion lies in one of the three "
            "structural branches, and every branch relaxation has a checked "
            "UNSAT proof.  The fixed-seed family therefore needs at least ten "
            "input-edge deletions."
        )
    elif statuses == ["UNSAT", "UNSAT", "UNSAT"]:
        global_status = "UNKNOWN_PROOF_UNCHECKED"
        conclusion = (
            "All solvers returned UNSAT, but not every frozen trace was accepted "
            "by the requested checker; no proof-carrying endpoint is claimed."
        )
    else:
        global_status = "UNKNOWN_LIMIT"
        conclusion = (
            "At least one exhaustive branch hit a resource limit; no SAT or "
            "UNSAT conclusion is justified."
        )

    result = {
        "schema": SCHEMA,
        "status": global_status,
        "claim_scope": (
            "Fixed input graph; arbitrary additions are allowed, but at most "
            "nine edges present in the input may be deleted."
        ),
        "input": str(args.matrix.resolve()),
        "input_sha256": sha256(args.matrix),
        "target": {"r": 3, "s": 13, "n": 61},
        "deletion_budget": args.budget,
        "arbitrary_original_nonedge_additions_allowed": True,
        "original_edges": len(original_edges),
        "structural_decomposition": structural_proof,
        "limits": {
            "conflicts_per_limited_call": args.conflicts_per_call,
            "max_conflicts_per_branch": args.max_conflicts_per_branch,
            "per_call_wall_seconds": args.per_call_seconds,
            "max_wall_seconds_per_branch": args.max_seconds_per_branch,
            "cross_solver_wall_seconds_per_branch": args.cross_solver_seconds,
            "drat_check_wall_seconds_per_branch": args.drat_check_seconds,
            "lazy_blue_batch_size": args.blue_batch_size,
        },
        "branches": branches,
        "conclusion": conclusion,
        "solver_dependency": (
            "The structural/formula encoding and the independent DRAT checker "
            "implementation remain in the trust boundary."
        ),
        "global_ramsey_claim": None,
        "elapsed_seconds": time.perf_counter() - started,
        "environment": {
            "python": os.sys.version,
            "pysat_solvers": ["glucose42", "cadical195"],
            "drat_trim_source_commit": args.drat_trim_source_commit,
        },
    }
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
