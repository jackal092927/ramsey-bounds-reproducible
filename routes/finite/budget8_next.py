#!/usr/bin/env python3
"""Strict budget-eight exclusion for the non-star 61-vertex R(3,13) seed.

The eleven input triangles have a forced structural decomposition.  Ten use
the hub edge (28,60), with pairwise disjoint spoke pairs, so a solution with
at most eight deletions must delete the hub.  The only remaining input
triangle is (37,46,60), so at least one of its three edges must also be
deleted.  This script solves those three branches with six residual deletions.

For every branch it preloads *all* independent 13-sets of the graph obtained
after the two forced branch deletions.  These are necessary edge-hitting
clauses for every completion, even when arbitrary original nonedges may be
added.  All triangle clauses and the residual deletion cardinality constraint
are present from the start.  A persistent, interruptible Glucose 4.2 solver
then runs under both conflict and wall-clock limits.  If a branch is UNSAT,
the exact DIMACS formula and its DRAT trace are frozen as deterministic gzip
artifacts; a separately bounded CaDiCaL process supplies a cross-solver replay.

UNKNOWN is never promoted to UNSAT.  SAT is accepted only after exact
reconstruction plus the independent bitset Ramsey verifier.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
import multiprocessing
import os
import shutil
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any, Iterable

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Solver

try:
    from .bounded_deletion_sat_cegar import build_variables
    from .graph_utils import enumerate_cliques, write_matrix
    from .new_basin_search import (
        apply_deletions,
        bounded_cegar_loop,
        edge_present,
        normalized_edge,
        rows_from_edge_model,
        triangle_edge_multiplicity,
        triangle_tuples,
    )
    from .verify_ramsey import complement, read_matrix, verify
except ImportError:  # pragma: no cover - direct script execution
    from bounded_deletion_sat_cegar import build_variables
    from graph_utils import enumerate_cliques, write_matrix
    from new_basin_search import (
        apply_deletions,
        bounded_cegar_loop,
        edge_present,
        normalized_edge,
        rows_from_edge_model,
        triangle_edge_multiplicity,
        triangle_tuples,
    )
    from verify_ramsey import complement, read_matrix, verify


HUB = (28, 60)
REMAINDER_TRIANGLE = (37, 46, 60)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def masks_hash(masks: Iterable[int]) -> str:
    digest = hashlib.sha256()
    for mask in masks:
        digest.update(f"{mask:016x}\n".encode("ascii"))
    return digest.hexdigest()


def structural_decomposition(
    rows: list[int], budget: int
) -> tuple[dict[str, Any], list[tuple[int, int]]]:
    """Validate and serialize the exhaustive three-branch reduction."""
    triangles = triangle_tuples(rows)
    through_hub = [t for t in triangles if set(HUB).issubset(t)]
    outside_hub = [t for t in triangles if not set(HUB).issubset(t)]
    third_vertices = [next(v for v in t if v not in HUB) for t in through_hub]
    spoke_pairs = [
        [list(normalized_edge(HUB[0], v)), list(normalized_edge(HUB[1], v))]
        for v in third_vertices
    ]
    if len(triangles) != 11:
        raise ValueError(f"expected 11 input triangles, found {len(triangles)}")
    if len(through_hub) != 10 or len(set(third_vertices)) != 10:
        raise ValueError("the ten hub triangles do not have disjoint spoke pairs")
    if outside_hub != [REMAINDER_TRIANGLE]:
        raise ValueError(f"unexpected non-hub triangle family: {outside_hub}")
    if not budget < len(through_hub):
        raise ValueError("the requested budget does not force the hub deletion")
    branch_edges = [
        normalized_edge(u, v)
        for u, v in itertools.combinations(REMAINDER_TRIANGLE, 2)
    ]
    for edge in [HUB, *branch_edges]:
        if not edge_present(rows, *edge):
            raise ValueError(f"structural branch edge {edge} is absent")
    proof = {
        "input_triangle_count": len(triangles),
        "input_triangles": [list(t) for t in triangles],
        "hub": list(HUB),
        "triangles_through_hub": [list(t) for t in through_hub],
        "hub_triangle_count": len(through_hub),
        "hub_third_vertices": third_vertices,
        "pairwise_disjoint_spoke_pairs": spoke_pairs,
        "hub_forced_deleted": True,
        "hub_reason": (
            "If the hub is retained, each of its ten triangles needs a "
            "deletion from its own disjoint two-edge spoke pair. Ten "
            f"deletions exceed budget {budget}."
        ),
        "only_triangle_after_hub_deletion": list(REMAINDER_TRIANGLE),
        "exhaustive_second_deletion_branches": [list(edge) for edge in branch_edges],
        "second_deletion_reason": (
            "Deleting edges cannot create triangle-freeness while retaining all "
            "three edges of the remaining input triangle; additions cannot "
            "destroy it. At least one displayed edge is therefore deleted."
        ),
    }
    return proof, branch_edges


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


def deterministic_gzip_text(
    path: Path, lines: Iterable[str]
) -> tuple[str, str, int, int]:
    """Write deterministic gzip text; return raw/gzip hashes and sizes."""
    raw_digest = hashlib.sha256()
    raw_size = 0
    line_count = 0
    with path.open("wb") as raw_file:
        with gzip.GzipFile(
            filename="", mode="wb", fileobj=raw_file, compresslevel=9, mtime=0
        ) as zipped:
            for line in lines:
                payload = line.encode("ascii")
                raw_digest.update(payload)
                raw_size += len(payload)
                line_count += 1
                zipped.write(payload)
    return raw_digest.hexdigest(), sha256(path), raw_size, line_count


def dimacs_lines(clauses: list[list[int]], variables: int) -> Iterable[str]:
    yield f"p cnf {variables} {len(clauses)}\n"
    for clause in clauses:
        yield " ".join(map(str, clause)) + " 0\n"


def proof_lines(proof: list[str]) -> Iterable[str]:
    for line in proof:
        yield line + "\n"


def verify_drat_trace(
    checker: Path,
    cnf_gzip: Path,
    proof_gzip: Path,
    wall_seconds: float,
) -> dict[str, Any]:
    """Decompress into a temporary directory and run a bounded DRAT check."""
    started = time.perf_counter()
    with tempfile.TemporaryDirectory(prefix="ramsey-budget8-drat-") as directory:
        temporary = Path(directory)
        cnf = temporary / "branch.cnf"
        proof = temporary / "branch.drat"
        with gzip.open(cnf_gzip, "rb") as source, cnf.open("wb") as target:
            shutil.copyfileobj(source, target)
        with gzip.open(proof_gzip, "rb") as source, proof.open("wb") as target:
            shutil.copyfileobj(source, target)
        try:
            completed = subprocess.run(
                [str(checker), str(cnf), str(proof)],
                check=False,
                capture_output=True,
                text=True,
                timeout=wall_seconds,
            )
        except subprocess.TimeoutExpired as error:
            return {
                "status": "TIME_LIMIT",
                "checker": str(checker.resolve()),
                "checker_sha256": sha256(checker),
                "wall_limit_seconds": wall_seconds,
                "elapsed_seconds": time.perf_counter() - started,
                "stdout_tail": (error.stdout or "")[-4000:],
                "stderr_tail": (error.stderr or "")[-4000:],
            }
    verified = completed.returncode == 0 and "s VERIFIED" in completed.stdout
    return {
        "status": "VERIFIED" if verified else "FAILED",
        "checker": str(checker.resolve()),
        "checker_sha256": sha256(checker),
        "wall_limit_seconds": wall_seconds,
        "elapsed_seconds": time.perf_counter() - started,
        "exitcode": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    }


def _cadical_worker(clauses: list[list[int]], queue: Any) -> None:
    """Child-process entry point so an unsupported limited solve is killable."""
    started = time.perf_counter()
    try:
        with Solver(name="cadical195", bootstrap_with=clauses) as solver:
            outcome = solver.solve()
            queue.put(
                {
                    "status": "SAT" if outcome else "UNSAT",
                    "elapsed_seconds": time.perf_counter() - started,
                    "solver_stats": solver.accum_stats(),
                }
            )
    except BaseException as error:  # pragma: no cover - defensive subprocess record
        queue.put(
            {
                "status": "ERROR",
                "elapsed_seconds": time.perf_counter() - started,
                "error": repr(error),
            }
        )


def bounded_cadical_replay(
    clauses: list[list[int]], wall_seconds: float
) -> dict[str, Any]:
    """Run CaDiCaL in a separate process with a hard parent wall limit."""
    context = multiprocessing.get_context("fork")
    queue = context.Queue()
    process = context.Process(target=_cadical_worker, args=(clauses, queue))
    started = time.perf_counter()
    process.start()
    process.join(wall_seconds)
    if process.is_alive():
        process.terminate()
        process.join(2.0)
        if process.is_alive():
            process.kill()
            process.join()
        result: dict[str, Any] = {
            "status": "TIME_LIMIT",
            "elapsed_seconds": time.perf_counter() - started,
            "wall_limit_seconds": wall_seconds,
        }
    elif queue.empty():
        result = {
            "status": "ERROR",
            "elapsed_seconds": time.perf_counter() - started,
            "exitcode": process.exitcode,
            "error": "child exited without a result",
        }
    else:
        result = queue.get()
        result["wall_limit_seconds"] = wall_seconds
        result["exitcode"] = process.exitcode
    queue.close()
    return result


def branch_formula(
    initial: list[int],
    variables: dict[tuple[int, int], int],
    pairs: list[tuple[int, int]],
    original_edges: set[tuple[int, int]],
    fixed: set[tuple[int, int]],
    residual_budget: int,
) -> tuple[list[list[int]], int, list[int], dict[str, Any]]:
    """Build an exact branch relaxation and its complete fixed-base I13 bank."""
    n = len(initial)
    reduced = apply_deletions(initial, fixed)
    enumeration_started = time.perf_counter()
    masks = enumerate_cliques(complement(reduced), 13)
    enumeration_seconds = time.perf_counter() - enumeration_started
    hub_pair_mask = (1 << HUB[0]) | (1 << HUB[1])

    # Every enumerated set is independent after exactly the fixed deletions.
    # Assert that it contains no other original edge, so its hitting clause is
    # visibly a necessary addition/fixed-edge-revival condition.
    for mask in masks:
        vertices = mask_vertices(mask, n)
        present_original = {
            normalized_edge(u, v)
            for u, v in itertools.combinations(vertices, 2)
            if normalized_edge(u, v) in original_edges
        }
        if not present_original.issubset(fixed):
            raise AssertionError(
                f"preloaded I13 mask has an undeleted original edge: {present_original-fixed}"
            )

    triangle_clauses = [
        [-variables[(a, b)], -variables[(a, c)], -variables[(b, c)]]
        for a, b, c in itertools.combinations(range(n), 3)
    ]
    pool = IDPool(start_from=len(pairs) + 1)
    residual_edges = sorted(original_edges - fixed)
    cardinality = CardEnc.atmost(
        lits=[-variables[edge] for edge in residual_edges],
        bound=residual_budget,
        vpool=pool,
        encoding=EncType.seqcounter,
    ).clauses
    units = [[-variables[edge]] for edge in sorted(fixed)]
    blue_clauses = [hitting_clause(mask, n, variables) for mask in masks]
    clauses = triangle_clauses + cardinality + units + blue_clauses
    metadata = {
        "fixed_deleted_edges": [list(edge) for edge in sorted(fixed)],
        "residual_deletion_budget": residual_budget,
        "edge_variables": len(pairs),
        "auxiliary_variables": pool.top - len(pairs),
        "maximum_variable": pool.top,
        "triangle_clauses": len(triangle_clauses),
        "residual_cardinality_clauses": len(cardinality),
        "fixed_unit_clauses": len(units),
        "preloaded_fixed_base_I13_clauses": len(blue_clauses),
        "preloaded_I13_containing_both_hub_vertices": sum(
            (mask & hub_pair_mask) == hub_pair_mask for mask in masks
        ),
        "preloaded_fixed_base_I13_sha256": masks_hash(masks),
        "preload_enumeration_seconds": enumeration_seconds,
        "initial_clause_count": len(clauses),
    }
    return clauses, pool.top, masks, metadata


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
    clauses, maximum_variable, seed_masks, formula = branch_formula(
        initial,
        variables,
        pairs,
        original_edges,
        fixed,
        residual_budget,
    )
    all_i13_masks = set(seed_masks)
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
        new_masks = [mask for mask in masks if mask not in all_i13_masks]
        if not new_masks:
            raise RuntimeError("SAT model repeats only already installed I13 cuts")
        for mask in new_masks:
            all_i13_masks.add(mask)
            lazy_masks.append(mask)
        new_clauses = [hitting_clause(mask, len(initial), variables) for mask in new_masks]
        clauses.extend(new_clauses)
        return new_clauses

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

    prefix = args.artifact_dir / f"budget8_next_branch_{index}"
    if status == "UNSAT":
        cnf_path = prefix.with_suffix(".cnf.gz")
        proof_path = prefix.with_suffix(".drat.gz")
        cnf_raw_hash, cnf_gzip_hash, cnf_raw_bytes, cnf_lines = deterministic_gzip_text(
            cnf_path, dimacs_lines(clauses, maximum_variable)
        )
        proof_raw_hash, proof_gzip_hash, proof_raw_bytes, proof_line_count = (
            deterministic_gzip_text(proof_path, proof_lines(proof))
        )
        cadical = bounded_cadical_replay(clauses, args.cross_solver_seconds)
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
                "proof_dependency": (
                    "UNSAT is a Glucose 4.2 solver result. The frozen DRAT trace "
                    "was emitted by PySAT but is not self-authenticating; use a "
                    "trusted DRAT checker on the paired DIMACS artifact."
                ),
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
                "bounded_cadical195_cross_replay": cadical,
            }
        )
    elif status == "SAT":
        if accepted is None or model is None:
            raise RuntimeError("SAT without an independently separated candidate")
        output = prefix.with_suffix(".txt")
        write_matrix(accepted, output)
        verification = verify(output, 3, 13)
        if not verification["valid_ramsey_certificate"]:
            raise RuntimeError("independent bitset verifier rejected SAT candidate")
        final_edges = {
            edge for edge in pairs if edge_present(accepted, *edge)
        }
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
    parser.add_argument("--budget", type=int, default=8)
    parser.add_argument("--conflicts-per-call", type=int, default=10_000)
    parser.add_argument("--max-conflicts-per-branch", type=int, default=200_000)
    parser.add_argument("--per-call-seconds", type=float, default=5.0)
    parser.add_argument("--max-seconds-per-branch", type=float, default=30.0)
    parser.add_argument("--cross-solver-seconds", type=float, default=30.0)
    parser.add_argument("--drat-trim", type=Path)
    parser.add_argument("--drat-trim-source-commit")
    parser.add_argument("--drat-check-seconds", type=float, default=30.0)
    parser.add_argument("--blue-batch-size", type=int, default=1024)
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()
    if args.budget != 8:
        parser.error("this structural decomposition is frozen specifically for budget 8")
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
        raise ValueError("budget-eight route requires the frozen 61-vertex seed")
    proof, branch_edges = structural_decomposition(initial, args.budget)
    variables, pairs = build_variables(len(initial))
    original_edges = {
        edge for edge in pairs if edge_present(initial, *edge)
    }
    started = time.perf_counter()
    branches = []
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
            f"I13={branch['formula']['preloaded_fixed_base_I13_clauses']}; "
            f"seconds={branch['run']['elapsed_seconds']:.3f}",
            flush=True,
        )

    statuses = [branch["status"] for branch in branches]
    drat_statuses = [
        branch.get("drat_check", {}).get("status") for branch in branches
    ]
    if all(status == "UNSAT" for status in statuses):
        global_status = "UNSAT"
        conclusion = (
            "Every at-most-eight-deletion completion lies in one of the three "
            "structural branches, and every branch relaxation is UNSAT. Hence "
            "the fixed-seed edit family has no solution with at most eight "
            "original-edge deletions."
        )
    elif any(status == "SAT" for status in statuses):
        global_status = "SAT"
        conclusion = "At least one branch produced an independently verified candidate."
    else:
        global_status = "UNKNOWN_LIMIT"
        conclusion = (
            "At least one exhaustive branch reached a resource limit; no global "
            "SAT or UNSAT conclusion is justified."
        )

    result = {
        "schema": "ramsey-r3-13-n61-nonstar-budget8-branch-v1",
        "status": global_status,
        "claim_scope": (
            "Fixed input graph; arbitrary additions are allowed, but at most "
            "eight edges present in the input may be deleted."
        ),
        "input": str(args.matrix.resolve()),
        "input_sha256": sha256(args.matrix),
        "target": {"r": 3, "s": 13, "n": 61},
        "deletion_budget": args.budget,
        "arbitrary_original_nonedge_additions_allowed": True,
        "original_edges": len(original_edges),
        "structural_decomposition": proof,
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
            "All three frozen DRAT traces passed the separately invoked checker; "
            "remaining trust is in the structural/formula encoding and the DRAT "
            "checker implementation."
            if drat_statuses == ["VERIFIED", "VERIFIED", "VERIFIED"]
            else
            "The structural reduction and I13 banks are exactly reproducible; "
            "the terminal UNSAT labels depend on SAT solvers for every branch "
            "whose frozen DRAT trace was not independently checked."
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
