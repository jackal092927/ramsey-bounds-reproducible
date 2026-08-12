#!/usr/bin/env python3
"""Proof-carrying budget-ten search around the frozen non-star 61 seed.

The complete edit family allows arbitrary additions of input nonedges and at
most ten deletions of input edges.  It is split by the status of the hub edge
(28,60).

If the hub is absent, the remaining input triangle (37,46,60) supplies three
exhaustive second-deletion branches, each with eight residual deletions.  If
the hub is present, ten pairwise-disjoint spoke pairs already consume the full
budget.  The remaining triangle then forces deletion of (37,60).  One merged
CNF represents all 2^9 choices in the other spoke pairs.

Every branch contains all triangle clauses, an exact input-edge deletion
counter, and all independent 13-sets of its fixed-deletion base.  SAT models
are separated exactly until an independent bitset verifier accepts them.
UNSAT is promoted to a proof-carrying conclusion only after every frozen DRAT
trace is accepted by a separately invoked checker.  Resource limits always
produce UNKNOWN.
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


SCHEMA = "ramsey-r3-13-n61-nonstar-budget10-complete-v1"
EXPECTED_DRAT_TRIM_COMMIT = "2e3b2dc0ecf938addbd779d42877b6ed69d9a985"
REMAINDER_TRIANGLE = (37, 46, 60)


def structural_decomposition(rows: list[int]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Validate the exhaustive hub-absent/hub-present decomposition."""
    triangles = triangle_tuples(rows)
    through_hub = [triangle for triangle in triangles if set(HUB).issubset(triangle)]
    outside_hub = [triangle for triangle in triangles if not set(HUB).issubset(triangle)]
    third_vertices = [
        next(vertex for vertex in triangle if vertex not in HUB)
        for triangle in through_hub
    ]
    spoke_pairs = [
        (
            normalized_edge(HUB[0], vertex),
            normalized_edge(HUB[1], vertex),
        )
        for vertex in third_vertices
    ]

    if len(triangles) != 11:
        raise ValueError(f"expected 11 input triangles, found {len(triangles)}")
    if len(through_hub) != 10 or len(set(third_vertices)) != 10:
        raise ValueError("the ten hub triangles do not have disjoint spoke pairs")
    flattened_spokes = [edge for pair in spoke_pairs for edge in pair]
    if len(set(flattened_spokes)) != 20:
        raise ValueError("spoke pairs are not pairwise edge-disjoint")
    if outside_hub != [REMAINDER_TRIANGLE]:
        raise ValueError(f"unexpected non-hub triangle family: {outside_hub}")

    remainder_edges = [
        normalized_edge(u, v)
        for u, v in itertools.combinations(REMAINDER_TRIANGLE, 2)
    ]
    overlap = sorted(set(flattened_spokes).intersection(remainder_edges))
    forced_retained_case_deletion = normalized_edge(37, 60)
    if overlap != [forced_retained_case_deletion]:
        raise ValueError(f"unexpected spoke/remainder overlap: {overlap}")
    for edge in [HUB, *remainder_edges, *flattened_spokes]:
        if not edge_present(rows, *edge):
            raise ValueError(f"structural edge {edge} is absent from the seed")

    branches: list[dict[str, Any]] = []
    for edge in remainder_edges:
        branches.append(
            {
                "case": "hub_deleted",
                "fixed_deleted_edges": [HUB, edge],
                "fixed_retained_edges": [],
                "residual_deletion_budget": 8,
                "exhaustive_reason": (
                    "With the hub deleted, at least one edge of the sole "
                    "remaining input triangle must also be deleted."
                ),
            }
        )
    branches.append(
        {
            "case": "hub_retained_merged_512",
            "fixed_deleted_edges": [forced_retained_case_deletion],
            "fixed_retained_edges": [HUB],
            "residual_deletion_budget": 9,
            "encoded_transversal_count": 2 ** 9,
            "exhaustive_reason": (
                "Retaining the hub forces one deletion in each of ten "
                "edge-disjoint spoke pairs.  Budget ten is therefore fully "
                "consumed.  The only spoke edge in the remaining triangle is "
                "(37,60), so it is forced absent; the other nine spoke pairs "
                "give all 2^9 choices represented by this single CNF."
            ),
        }
    )

    proof = {
        "input_triangle_count": len(triangles),
        "input_triangles": [list(triangle) for triangle in triangles],
        "hub": list(HUB),
        "triangles_through_hub": [list(triangle) for triangle in through_hub],
        "hub_third_vertices": third_vertices,
        "pairwise_disjoint_spoke_pairs": [
            [list(edge) for edge in pair] for pair in spoke_pairs
        ],
        "only_triangle_outside_hub": list(REMAINDER_TRIANGLE),
        "remainder_triangle_edges": [list(edge) for edge in remainder_edges],
        "spoke_remainder_edge_overlap": [list(edge) for edge in overlap],
        "hub_deleted_branch_count": 3,
        "hub_retained_transversal_count": 2 ** 9,
        "total_merged_cnf_branches": len(branches),
        "case_split_exhaustive": True,
    }
    return proof, branches


def solve_branch(
    index: int,
    specification: dict[str, Any],
    initial: list[int],
    variables: dict[tuple[int, int], int],
    pairs: list[tuple[int, int]],
    original_edges: set[tuple[int, int]],
    args: argparse.Namespace,
) -> dict[str, Any]:
    fixed_deleted = {
        tuple(edge) for edge in specification["fixed_deleted_edges"]
    }
    fixed_retained = {
        tuple(edge) for edge in specification["fixed_retained_edges"]
    }
    if fixed_deleted.intersection(fixed_retained):
        raise ValueError("an edge cannot be fixed both absent and present")
    if not fixed_deleted.union(fixed_retained).issubset(original_edges):
        raise ValueError("every fixed edge must be an input edge")

    residual_budget = args.budget - len(fixed_deleted)
    if residual_budget != specification["residual_deletion_budget"]:
        raise AssertionError("branch residual budget does not match its specification")
    clauses, maximum_variable, base_masks, formula = branch_formula(
        initial,
        variables,
        pairs,
        original_edges,
        fixed_deleted,
        residual_budget,
    )
    positive_units = [[variables[edge]] for edge in sorted(fixed_retained)]
    clauses.extend(positive_units)
    formula.update(
        {
            "fixed_retained_edges": [list(edge) for edge in sorted(fixed_retained)],
            "fixed_positive_unit_clauses": len(positive_units),
            "initial_clause_count": len(clauses),
        }
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
            raise RuntimeError("SAT model violates only installed I13 clauses")
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
    for edge in fixed_deleted:
        phases[variables[edge] - 1] = -variables[edge]
    for edge in fixed_retained:
        phases[variables[edge] - 1] = variables[edge]

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
        "case": specification["case"],
        "fixed_deleted_edges": [list(edge) for edge in sorted(fixed_deleted)],
        "fixed_retained_edges": [list(edge) for edge in sorted(fixed_retained)],
        "status": status,
        "formula": formula,
        "lazy_I13_clauses_added": len(lazy_masks),
        "lazy_I13_masks_sha256": masks_hash(lazy_masks),
        "run": run,
    }
    if "encoded_transversal_count" in specification:
        result["encoded_transversal_count"] = specification[
            "encoded_transversal_count"
        ]

    prefix = args.artifact_dir / f"budget10_search_branch_{index}"
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
        added = sorted(final_edges - original_edges)
        if len(deleted) > args.budget:
            raise RuntimeError("SAT reconstruction exceeds deletion budget")
        if not fixed_deleted.issubset(set(deleted)):
            raise RuntimeError("SAT reconstruction violates a fixed deletion")
        if not fixed_retained.issubset(final_edges):
            raise RuntimeError("SAT reconstruction violates a fixed retention")
        result.update(
            {
                "output": str(output.resolve()),
                "output_sha256": sha256(output),
                "final_edges": len(final_edges),
                "deleted_edges": [list(edge) for edge in deleted],
                "added_edges": [list(edge) for edge in added],
                "independent_bitset_verification": verification,
                "global_ramsey_implication": "R(3,13) >= 62",
            }
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--budget", type=int, default=10)
    parser.add_argument("--conflicts-per-call", type=int, default=20_000)
    parser.add_argument("--max-conflicts-per-branch", type=int, default=3_000_000)
    parser.add_argument("--per-call-seconds", type=float, default=10.0)
    parser.add_argument("--max-seconds-per-branch", type=float, default=900.0)
    parser.add_argument("--cross-solver-seconds", type=float, default=300.0)
    parser.add_argument("--drat-trim", type=Path)
    parser.add_argument("--drat-trim-source-commit")
    parser.add_argument("--drat-check-seconds", type=float, default=600.0)
    parser.add_argument("--blue-batch-size", type=int, default=1024)
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()

    if args.budget != 10:
        parser.error("this complete search is frozen specifically for budget ten")
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
    if args.drat_trim is not None:
        if not args.drat_trim.is_file():
            parser.error("--drat-trim must name an existing executable file")
        if args.drat_trim_source_commit != EXPECTED_DRAT_TRIM_COMMIT:
            parser.error(
                "proof-carrying mode requires the pinned drat-trim source commit"
            )

    args.artifact_dir.mkdir(parents=True, exist_ok=True)
    initial = read_matrix(args.matrix)
    if len(initial) != 61:
        raise ValueError("budget-ten route requires the frozen 61-vertex seed")
    structural_proof, branch_specifications = structural_decomposition(initial)
    variables, pairs = build_variables(len(initial))
    original_edges = {edge for edge in pairs if edge_present(initial, *edge)}

    started = time.perf_counter()
    branches: list[dict[str, Any]] = []
    for index, specification in enumerate(branch_specifications):
        branch = solve_branch(
            index,
            specification,
            initial,
            variables,
            pairs,
            original_edges,
            args,
        )
        branches.append(branch)
        print(
            f"branch {index} {branch['case']}: {branch['status']}; "
            f"I13={branch['formula']['preloaded_fixed_base_I13_clauses']}; "
            f"lazy={branch['lazy_I13_clauses_added']}; "
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
            "A fully separated candidate passed independent bitset "
            "verification, proving R(3,13) >= 62."
        )
        global_ramsey_claim: str | None = "R(3,13) >= 62"
    elif len(branches) == 4 and statuses == ["UNSAT"] * 4 and proof_statuses == [
        "VERIFIED"
    ] * 4:
        global_status = "UNSAT_PROOF_VERIFIED"
        conclusion = (
            "The exhaustive hub-deleted and hub-retained cases all have "
            "checked UNSAT proofs.  Every completion in this fixed-seed edit "
            "family therefore needs at least eleven input-edge deletions."
        )
        global_ramsey_claim = None
    elif len(branches) == 4 and statuses == ["UNSAT"] * 4:
        global_status = "UNKNOWN_PROOF_UNCHECKED"
        conclusion = (
            "All four solvers returned UNSAT, but not every trace was accepted "
            "by the pinned checker; no proof-carrying endpoint is claimed."
        )
        global_ramsey_claim = None
    else:
        global_status = "UNKNOWN_LIMIT"
        conclusion = (
            "At least one exhaustive case hit a resource limit; no SAT or "
            "UNSAT conclusion is justified."
        )
        global_ramsey_claim = None

    result = {
        "schema": SCHEMA,
        "status": global_status,
        "claim_scope": (
            "Fixed input graph; arbitrary additions are allowed, but at most "
            "ten edges present in the input may be deleted."
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
            "The structural/formula encoding, independent bitset verifier, and "
            "DRAT checker implementation remain in the trust boundary."
        ),
        "global_ramsey_claim": global_ramsey_claim,
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
