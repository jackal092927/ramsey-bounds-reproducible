#!/usr/bin/env python3
"""Proof-carrying bounded branch search for the R(3,18) 100-vertex near miss.

The input has one triangle.  Every triangle-free completion with at most five
deletions of input edges deletes at least one of its three edges.  We create
three exhaustive branches, fix one triangle edge absent, and permit at most
four further input-edge deletions.  Every input nonedge remains a free final
edge variable, so additions are unrestricted.

Each branch preloads deterministic independent-18 hitting clauses from the
fixed-deletion base and then separates all further I18 witnesses exactly.  A
Glucose UNSAT answer is frozen with its final DIMACS and DRAT trace.  Limited
calls support hard conflict and wall-clock endpoints; UNKNOWN is never
promoted to UNSAT.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
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
        bounded_cadical_replay,
        deterministic_gzip_text,
        dimacs_lines,
        masks_hash,
        proof_lines,
        sha256,
        verify_drat_trace,
    )
    from .graph_utils import enumerate_cliques, write_matrix
    from .new_basin_search import (
        bounded_cegar_loop,
        edge_present,
        normalized_edge,
        rows_from_edge_model,
        triangle_tuples,
    )
    from .verify_ramsey import complement, read_matrix, verify
except ImportError:  # pragma: no cover - direct execution
    from bounded_deletion_sat_cegar import build_variables
    from budget8_next import (
        bounded_cadical_replay,
        deterministic_gzip_text,
        dimacs_lines,
        masks_hash,
        proof_lines,
        sha256,
        verify_drat_trace,
    )
    from graph_utils import enumerate_cliques, write_matrix
    from new_basin_search import (
        bounded_cegar_loop,
        edge_present,
        normalized_edge,
        rows_from_edge_model,
        triangle_tuples,
    )
    from verify_ramsey import complement, read_matrix, verify


SCHEMA = "ramsey-r3-18-n100-budget5-branch-v1"
EXPECTED_INPUT_SHA256 = (
    "e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e"
)
EXPECTED_TRIANGLE = (97, 98, 99)
EXPECTED_DRAT_TRIM_COMMIT = "2e3b2dc0ecf938addbd779d42877b6ed69d9a985"


def mask_vertices(mask: int, n: int) -> list[int]:
    return [v for v in range(n) if (mask >> v) & 1]


def hitting_clause(
    mask: int, n: int, variables: dict[tuple[int, int], int]
) -> list[int]:
    vertices = mask_vertices(mask, n)
    return [
        variables[normalized_edge(u, v)]
        for u, v in itertools.combinations(vertices, 2)
    ]


def delete_edge(rows: list[int], edge: tuple[int, int]) -> list[int]:
    u, v = edge
    result = rows.copy()
    result[u] &= ~(1 << v)
    result[v] &= ~(1 << u)
    return result


def fixed_base_i18_prefix(
    initial: list[int], edge: tuple[int, int], limit: int
) -> list[int]:
    """Enumerate a deterministic prefix of all I18 created by deleting edge.

    The original graph has no I18.  Hence every I18 created by deleting one
    edge contains both endpoints.  Its other 16 vertices form an independent
    set in the common original non-neighbourhood of the endpoints.
    """
    n = len(initial)
    u, v = edge
    candidates = ((1 << n) - 1) & ~(
        initial[u] | initial[v] | (1 << u) | (1 << v)
    )
    prefix16 = enumerate_cliques(
        complement(initial), 16, candidates=candidates, limit=limit
    )
    endpoint_mask = (1 << u) | (1 << v)
    return [mask | endpoint_mask for mask in prefix16]


def validate_i18_clause_bank(
    masks: Iterable[int],
    n: int,
    original_edges: set[tuple[int, int]],
    fixed_edge: tuple[int, int],
) -> None:
    for mask in masks:
        if mask.bit_count() != 18:
            raise AssertionError("preloaded mask is not an 18-set")
        vertices = mask_vertices(mask, n)
        present = {
            normalized_edge(u, v)
            for u, v in itertools.combinations(vertices, 2)
            if normalized_edge(u, v) in original_edges
        }
        if present != {fixed_edge}:
            raise AssertionError(
                f"preloaded I18 has original edges {present}, expected only {fixed_edge}"
            )


def structural_decomposition(rows: list[int], budget: int) -> dict[str, Any]:
    triangles = triangle_tuples(rows)
    if triangles != [EXPECTED_TRIANGLE]:
        raise ValueError(f"expected unique triangle {EXPECTED_TRIANGLE}, found {triangles}")
    edges = [
        normalized_edge(u, v)
        for u, v in itertools.combinations(EXPECTED_TRIANGLE, 2)
    ]
    for edge in edges:
        if not edge_present(rows, *edge):
            raise AssertionError(f"triangle edge {edge} is absent")
    return {
        "input_triangle_count": 1,
        "unique_input_triangle": list(EXPECTED_TRIANGLE),
        "triangle_edges": [list(edge) for edge in edges],
        "branch_count": 3,
        "case_split_exhaustive": True,
        "reason": (
            "Every triangle-free final graph must omit at least one edge of "
            "the unique input triangle.  Each of the three branches fixes one "
            f"such edge absent and leaves {budget - 1} residual deletions."
        ),
    }


def branch_formula(
    initial: list[int],
    variables: dict[tuple[int, int], int],
    pairs: list[tuple[int, int]],
    original_edges: set[tuple[int, int]],
    fixed_edge: tuple[int, int],
    residual_budget: int,
    preload_limit: int,
) -> tuple[list[list[int]], int, list[int], dict[str, Any]]:
    n = len(initial)
    preload_started = time.perf_counter()
    masks = fixed_base_i18_prefix(initial, fixed_edge, preload_limit)
    validate_i18_clause_bank(masks, n, original_edges, fixed_edge)
    preload_seconds = time.perf_counter() - preload_started

    triangle_clauses = [
        [-variables[(a, b)], -variables[(a, c)], -variables[(b, c)]]
        for a, b, c in itertools.combinations(range(n), 3)
    ]
    pool = IDPool(start_from=len(pairs) + 1)
    residual_edges = sorted(original_edges - {fixed_edge})
    cardinality = CardEnc.atmost(
        lits=[-variables[edge] for edge in residual_edges],
        bound=residual_budget,
        vpool=pool,
        encoding=EncType.seqcounter,
    ).clauses
    fixed_unit = [[-variables[fixed_edge]]]
    blue_clauses = [hitting_clause(mask, n, variables) for mask in masks]
    clauses = triangle_clauses + cardinality + fixed_unit + blue_clauses
    metadata = {
        "fixed_deleted_edge": list(fixed_edge),
        "fixed_edge_negative_unit_clause": True,
        "fixed_deleted_edge_cannot_be_readded": True,
        "residual_deletion_budget": residual_budget,
        "edge_variables": len(pairs),
        "auxiliary_variables": pool.top - len(pairs),
        "maximum_variable": pool.top,
        "triangle_clauses": len(triangle_clauses),
        "residual_cardinality_clauses": len(cardinality),
        "fixed_unit_clauses": 1,
        "preloaded_fixed_base_I18_clauses": len(blue_clauses),
        "preloaded_bank_complete": False,
        "preloaded_fixed_base_I18_sha256": masks_hash(masks),
        "preload_enumeration_seconds": preload_seconds,
        "initial_clause_count": len(clauses),
    }
    return clauses, pool.top, masks, metadata


def solve_branch(
    index: int,
    fixed_edge: tuple[int, int],
    initial: list[int],
    variables: dict[tuple[int, int], int],
    pairs: list[tuple[int, int]],
    original_edges: set[tuple[int, int]],
    args: argparse.Namespace,
) -> dict[str, Any]:
    residual_budget = args.budget - 1
    clauses, maximum_variable, preloaded, formula = branch_formula(
        initial,
        variables,
        pairs,
        original_edges,
        fixed_edge,
        residual_budget,
        args.preload_i18,
    )
    known_masks = set(preloaded)
    lazy_masks: list[int] = []
    accepted: list[int] | None = None

    def separate(model: list[int]) -> list[list[int]]:
        nonlocal accepted
        candidate = rows_from_edge_model(model, len(initial), variables)
        masks = enumerate_cliques(
            complement(candidate), 18, limit=args.blue_batch_size
        )
        if not masks:
            accepted = candidate
            return []
        new_masks = [mask for mask in masks if mask not in known_masks]
        if not new_masks:
            raise RuntimeError("SAT model violates only installed I18 clauses")
        known_masks.update(new_masks)
        lazy_masks.extend(new_masks)
        new_clauses = [
            hitting_clause(mask, len(initial), variables) for mask in new_masks
        ]
        clauses.extend(new_clauses)
        return new_clauses

    phases = [
        variables[edge] if edge in original_edges else -variables[edge]
        for edge in pairs
    ]
    phases[variables[fixed_edge] - 1] = -variables[fixed_edge]

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
        "fixed_deleted_edge": list(fixed_edge),
        "status": status,
        "formula": formula,
        "lazy_I18_clauses_added": len(lazy_masks),
        "lazy_I18_masks_sha256": masks_hash(lazy_masks),
        "run": run,
    }

    prefix = args.artifact_dir / f"r3_18_budget5_branch_{index}"
    if status == "UNSAT":
        if not proof:
            raise RuntimeError("Glucose returned UNSAT without a proof trace")
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
            else {"status": "NOT_RUN", "reason": "No checker supplied."}
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
        verification = verify(output, 3, 18)
        if not verification["valid_ramsey_certificate"]:
            raise RuntimeError("independent verifier rejected SAT candidate")
        final_edges = {edge for edge in pairs if edge_present(accepted, *edge)}
        deleted = sorted(original_edges - final_edges)
        added = sorted(final_edges - original_edges)
        if len(deleted) > args.budget or fixed_edge not in deleted:
            raise RuntimeError("SAT reconstruction violates deletion semantics")
        result.update(
            {
                "output": str(output.resolve()),
                "output_sha256": sha256(output),
                "deleted_edges": [list(edge) for edge in deleted],
                "added_edges": [list(edge) for edge in added],
                "independent_bitset_verification": verification,
                "global_ramsey_implication": "R(3,18) >= 101",
            }
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--budget", type=int, default=5)
    parser.add_argument("--preload-i18", type=int, default=4096)
    parser.add_argument("--conflicts-per-call", type=int, default=20_000)
    parser.add_argument("--max-conflicts-per-branch", type=int, default=2_000_000)
    parser.add_argument("--per-call-seconds", type=float, default=10.0)
    parser.add_argument("--max-seconds-per-branch", type=float, default=300.0)
    parser.add_argument("--cross-solver-seconds", type=float, default=60.0)
    parser.add_argument("--drat-trim", type=Path)
    parser.add_argument("--drat-trim-source-commit")
    parser.add_argument("--drat-check-seconds", type=float, default=300.0)
    parser.add_argument("--blue-batch-size", type=int, default=512)
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()

    if args.budget != 5:
        parser.error("this decomposition is frozen specifically for budget five")
    if min(
        args.preload_i18,
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
    if args.drat_trim is not None:
        if not args.drat_trim.is_file():
            parser.error("--drat-trim must name an executable file")
        if args.drat_trim_source_commit != EXPECTED_DRAT_TRIM_COMMIT:
            parser.error("proof mode requires the pinned drat-trim commit")

    args.artifact_dir.mkdir(parents=True, exist_ok=True)
    initial = read_matrix(args.matrix)
    if len(initial) != 100:
        raise ValueError("the budget-five route requires a 100-vertex seed")
    input_hash = sha256(args.matrix)
    if input_hash != EXPECTED_INPUT_SHA256:
        raise ValueError(f"unexpected seed hash {input_hash}")
    seed_check = verify(args.matrix, 3, 18)
    if seed_check["searches"]["forbidden_independent_set"]["exists"]:
        raise ValueError("seed unexpectedly contains an I18")
    structural = structural_decomposition(initial, args.budget)
    branch_edges = [tuple(edge) for edge in structural["triangle_edges"]]
    variables, pairs = build_variables(len(initial))
    original_edges = {edge for edge in pairs if edge_present(initial, *edge)}

    started = time.perf_counter()
    branches: list[dict[str, Any]] = []
    for index, edge in enumerate(branch_edges):
        branch = solve_branch(
            index,
            edge,
            initial,
            variables,
            pairs,
            original_edges,
            args,
        )
        branches.append(branch)
        print(
            f"branch {index} {edge}: {branch['status']}; "
            f"preload={branch['formula']['preloaded_fixed_base_I18_clauses']}; "
            f"lazy={branch['lazy_I18_clauses_added']}; "
            f"seconds={branch['run']['elapsed_seconds']:.3f}",
            flush=True,
        )
        if branch["status"] == "SAT":
            break

    statuses = [branch["status"] for branch in branches]
    proof_statuses = [
        branch.get("drat_check", {}).get("status") for branch in branches
    ]
    if any(status == "SAT" for status in statuses):
        global_status = "SAT_VERIFIED"
        conclusion = (
            "A branch produced a 100-vertex triangle-free/I18-free graph "
            "accepted by the independent bitset verifier."
        )
        global_claim: str | None = "R(3,18) >= 101"
    elif statuses == ["UNSAT"] * 3 and proof_statuses == ["VERIFIED"] * 3:
        global_status = "UNSAT_PROOF_VERIFIED"
        conclusion = (
            "All three exhaustive fixed-triangle-edge branches have checked "
            "UNSAT proofs.  This fixed seed has no completion with at most "
            "five input-edge deletions, even with arbitrary additions."
        )
        global_claim = None
    elif statuses == ["UNSAT"] * 3:
        global_status = "UNKNOWN_PROOF_UNCHECKED"
        conclusion = (
            "Every solver returned UNSAT, but not every proof was accepted by "
            "the pinned checker; no proof-carrying endpoint is claimed."
        )
        global_claim = None
    else:
        global_status = "UNKNOWN_LIMIT"
        conclusion = (
            "At least one exhaustive branch reached a resource limit; no "
            "budget-five SAT or UNSAT conclusion is justified."
        )
        global_claim = None

    result = {
        "schema": SCHEMA,
        "status": global_status,
        "claim_scope": (
            "Fixed 100-vertex input; arbitrary input-nonedge additions are "
            "allowed, and at most five input edges may be deleted."
        ),
        "input": str(args.matrix.resolve()),
        "input_sha256": input_hash,
        "target": {"r": 3, "s": 18, "n": 100},
        "deletion_budget": args.budget,
        "arbitrary_original_nonedge_additions_allowed": True,
        "original_edges": len(original_edges),
        "seed_bitset_verification": seed_check,
        "structural_decomposition": structural,
        "limits": {
            "preloaded_I18_per_branch": args.preload_i18,
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
        "global_ramsey_claim": global_claim,
        "elapsed_seconds": time.perf_counter() - started,
        "environment": {
            "python": os.sys.version,
            "pysat_solvers": ["glucose42", "cadical195"],
            "drat_trim_source_commit": args.drat_trim_source_commit,
            "expected_drat_trim_source_commit": EXPECTED_DRAT_TRIM_COMMIT,
        },
    }
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

