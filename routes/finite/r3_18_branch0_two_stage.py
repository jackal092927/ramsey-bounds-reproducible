#!/usr/bin/env python3
"""Hard-bounded two-stage proof audit for the remaining R(3,18) branch.

Stage 1 uses an incremental CaDiCaL CEGAR process to discover a finite bank
of necessary independent-18 hitting clauses.  The parent process enforces a
hard wall-clock limit.  If that finite CNF is UNSAT, stage 2 invokes a pinned
standalone CaDiCaL binary on the frozen CNF and checks its textual DRAT trace
with a separately pinned drat-trim executable.

This script is deliberately specialized to branch zero: the input edge
(97,98) is fixed absent and cannot be re-added, while at most four of the
other input edges may be deleted.  All input nonedges remain free variables.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import multiprocessing
import os
import shutil
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any

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
    from .graph_utils import write_matrix
    from .new_basin_search import edge_present, rows_from_edge_model
    from .r3_18_budget5_branch import (
        EXPECTED_INPUT_SHA256,
        EXPECTED_TRIANGLE,
        branch_formula,
        hitting_clause,
        structural_decomposition,
    )
    from .verify_ramsey import CliqueTargetSearch, complement, read_matrix, verify
except ImportError:  # pragma: no cover - direct execution
    from bounded_deletion_sat_cegar import build_variables
    from budget8_next import (
        deterministic_gzip_text,
        dimacs_lines,
        masks_hash,
        sha256,
        verify_drat_trace,
    )
    from graph_utils import write_matrix
    from new_basin_search import edge_present, rows_from_edge_model
    from r3_18_budget5_branch import (
        EXPECTED_INPUT_SHA256,
        EXPECTED_TRIANGLE,
        branch_formula,
        hitting_clause,
        structural_decomposition,
    )
    from verify_ramsey import CliqueTargetSearch, complement, read_matrix, verify


SCHEMA = "ramsey-r3-18-n100-budget5-branch0-two-stage-v1"
FIXED_EDGE = (97, 98)


def atomic_json(path: Path, payload: dict[str, Any]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    temporary.replace(path)


def mask_from_witness(witness: list[int]) -> int:
    mask = 0
    for vertex in witness:
        mask |= 1 << vertex
    return mask


def gzip_file_deterministically(source: Path, target: Path) -> dict[str, Any]:
    raw_hash = hashlib.sha256()
    raw_bytes = 0
    raw_lines = 0
    with source.open("rb") as incoming, target.open("wb") as raw_target:
        with gzip.GzipFile(
            filename="", mode="wb", fileobj=raw_target, compresslevel=9, mtime=0
        ) as outgoing:
            while True:
                chunk = incoming.read(1024 * 1024)
                if not chunk:
                    break
                raw_hash.update(chunk)
                raw_bytes += len(chunk)
                raw_lines += chunk.count(b"\n")
                outgoing.write(chunk)
    return {
        "uncompressed_sha256": raw_hash.hexdigest(),
        "gzip_sha256": sha256(target),
        "uncompressed_bytes": raw_bytes,
        "lines": raw_lines,
    }


def _discovery_worker(
    matrix: str,
    preload_limit: int,
    checkpoint: str,
    queue: Any,
) -> None:
    """Incremental exact CEGAR; isolated so the parent can hard-kill solve()."""
    started = time.perf_counter()
    try:
        initial = read_matrix(Path(matrix))
        variables, pairs = build_variables(len(initial))
        original_edges = {
            edge for edge in pairs if edge_present(initial, *edge)
        }
        clauses, maximum_variable, preloaded, formula = branch_formula(
            initial,
            variables,
            pairs,
            original_edges,
            FIXED_EDGE,
            residual_budget=4,
            preload_limit=preload_limit,
        )
        known = set(preloaded)
        lazy: list[int] = []
        phases = [
            variables[edge] if edge in original_edges else -variables[edge]
            for edge in pairs
        ]
        phases[variables[FIXED_EDGE] - 1] = -variables[FIXED_EDGE]

        with Solver(
            name="cadical195", bootstrap_with=clauses
        ) as solver:
            solver.set_phases(phases)
            iterations = 0
            while True:
                iterations += 1
                outcome = solver.solve()
                elapsed = time.perf_counter() - started
                if not outcome:
                    payload = {
                        "status": "UNSAT_FINITE_CUT_BANK",
                        "iterations": iterations,
                        "lazy_masks": lazy,
                        "lazy_masks_sha256": masks_hash(lazy),
                        "elapsed_seconds": elapsed,
                        "solver_stats": solver.accum_stats(),
                        "formula": formula,
                        "maximum_variable": maximum_variable,
                    }
                    atomic_json(Path(checkpoint), payload)
                    queue.put(payload)
                    return

                model = solver.get_model()
                candidate = rows_from_edge_model(
                    model, len(initial), variables
                )
                missed = CliqueTargetSearch(complement(candidate), 18).run()
                if not missed.exists:
                    payload = {
                        "status": "SAT_SEPARATED",
                        "iterations": iterations,
                        "lazy_masks": lazy,
                        "lazy_masks_sha256": masks_hash(lazy),
                        "elapsed_seconds": elapsed,
                        "solver_stats": solver.accum_stats(),
                        "formula": formula,
                        "maximum_variable": maximum_variable,
                        "candidate_rows": candidate,
                    }
                    atomic_json(
                        Path(checkpoint),
                        {key: value for key, value in payload.items()
                         if key != "candidate_rows"},
                    )
                    queue.put(payload)
                    return
                witness = missed.witness or []
                mask = mask_from_witness(witness)
                if mask.bit_count() != 18:
                    raise AssertionError("separator returned a non-I18 witness")
                if mask in known:
                    raise RuntimeError("separator repeated an installed I18 clause")
                known.add(mask)
                lazy.append(mask)
                solver.add_clause(hitting_clause(mask, len(initial), variables))
                if iterations % 25 == 0:
                    atomic_json(
                        Path(checkpoint),
                        {
                            "status": "RUNNING",
                            "iterations": iterations,
                            "lazy_masks": lazy,
                            "lazy_masks_sha256": masks_hash(lazy),
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
    preload_limit: int,
    checkpoint: Path,
    wall_seconds: float,
) -> dict[str, Any]:
    context = multiprocessing.get_context("fork")
    queue = context.Queue()
    process = context.Process(
        target=_discovery_worker,
        args=(str(matrix), preload_limit, str(checkpoint), queue),
    )
    started = time.perf_counter()
    process.start()
    next_report = 30.0
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
                    f"iteration={current.get('iterations')}, "
                    f"cuts={len(current.get('lazy_masks', []))}"
                )
            print(f"discovery {elapsed:.1f}s: {summary}", flush=True)
            next_report += 30.0
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


def run_external_proof(
    cadical: Path,
    cnf_gzip: Path,
    proof_gzip: Path,
    wall_seconds: float,
) -> dict[str, Any]:
    started = time.perf_counter()
    with tempfile.TemporaryDirectory(prefix="ramsey-r3-18-cadical-") as directory:
        temporary = Path(directory)
        cnf = temporary / "branch0.cnf"
        proof = temporary / "branch0.drat"
        with gzip.open(cnf_gzip, "rb") as source, cnf.open("wb") as target:
            shutil.copyfileobj(source, target)
        try:
            completed = subprocess.run(
                [
                    str(cadical),
                    "--no-binary",
                    "--checkproof=0",
                    str(cnf),
                    str(proof),
                ],
                check=False,
                capture_output=True,
                text=True,
                timeout=wall_seconds,
            )
        except subprocess.TimeoutExpired as error:
            return {
                "status": "TIME_LIMIT",
                "wall_limit_seconds": wall_seconds,
                "elapsed_seconds": time.perf_counter() - started,
                "stdout_tail": (error.stdout or "")[-4000:],
                "stderr_tail": (error.stderr or "")[-4000:],
            }
        result: dict[str, Any] = {
            "status": (
                "UNSAT_PROOF_WRITTEN" if completed.returncode == 20
                else "SAT" if completed.returncode == 10
                else "ERROR"
            ),
            "exitcode": completed.returncode,
            "wall_limit_seconds": wall_seconds,
            "elapsed_seconds": time.perf_counter() - started,
            "stdout_tail": completed.stdout[-8000:],
            "stderr_tail": completed.stderr[-8000:],
        }
        if completed.returncode == 20 and proof.is_file():
            result["proof"] = gzip_file_deterministically(proof, proof_gzip)
            result["proof_gzip"] = str(proof_gzip.resolve())
        return result


def finish(payload: dict[str, Any], destination: Path) -> None:
    rendered = json.dumps(payload, indent=2, sort_keys=True)
    print(rendered)
    destination.write_text(rendered + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("matrix", type=Path)
    parser.add_argument("--preload-i18", type=int, default=1)
    parser.add_argument("--discovery-seconds", type=float, default=900.0)
    parser.add_argument("--proof-seconds", type=float, default=600.0)
    parser.add_argument("--drat-check-seconds", type=float, default=600.0)
    parser.add_argument("--cadical", type=Path, required=True)
    parser.add_argument("--cadical-source-commit", required=True)
    parser.add_argument("--drat-trim", type=Path, required=True)
    parser.add_argument("--drat-trim-source-commit", required=True)
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    args = parser.parse_args()

    if args.preload_i18 <= 0:
        parser.error("--preload-i18 must be positive")
    if min(
        args.discovery_seconds,
        args.proof_seconds,
        args.drat_check_seconds,
    ) <= 0:
        parser.error("wall limits must be positive")
    for executable in (args.cadical, args.drat_trim):
        if not executable.is_file() or not os.access(executable, os.X_OK):
            parser.error(f"not an executable: {executable}")

    args.artifact_dir.mkdir(parents=True, exist_ok=True)
    initial = read_matrix(args.matrix)
    if len(initial) != 100 or sha256(args.matrix) != EXPECTED_INPUT_SHA256:
        raise ValueError("unexpected R(3,18) near-miss input")
    structural = structural_decomposition(initial, 5)
    if structural["unique_input_triangle"] != list(EXPECTED_TRIANGLE):
        raise AssertionError("unexpected structural decomposition")
    seed_check = verify(args.matrix, 3, 18)
    if seed_check["searches"]["forbidden_independent_set"]["exists"]:
        raise ValueError("input unexpectedly contains I18")

    prefix = args.artifact_dir / "r3_18_budget5_branch_0_twostage"
    checkpoint = prefix.with_suffix(".checkpoint.json")
    if checkpoint.exists():
        checkpoint.unlink()
    started = time.perf_counter()
    discovery = bounded_discovery(
        args.matrix,
        args.preload_i18,
        checkpoint,
        args.discovery_seconds,
    )
    base: dict[str, Any] = {
        "schema": SCHEMA,
        "input": str(args.matrix.resolve()),
        "input_sha256": sha256(args.matrix),
        "target": {"r": 3, "s": 18, "n": 100},
        "fixed_deleted_edge": list(FIXED_EDGE),
        "fixed_edge_cannot_be_readded": True,
        "residual_input_edge_deletion_budget": 4,
        "total_input_edge_deletion_budget": 5,
        "arbitrary_input_nonedge_additions_allowed": True,
        "structural_decomposition": structural,
        "seed_bitset_verification": seed_check,
        "limits": {
            "discovery_wall_seconds": args.discovery_seconds,
            "proof_wall_seconds": args.proof_seconds,
            "drat_check_wall_seconds": args.drat_check_seconds,
            "preloaded_fixed_base_I18": args.preload_i18,
        },
        "tools": {
            "pysat_discovery_solver": "cadical195",
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
        original_edges = {edge for edge in pairs if edge_present(initial, *edge)}
        final_edges = {edge for edge in pairs if edge_present(candidate, *edge)}
        deleted = sorted(original_edges - final_edges)
        if (
            not checked["valid_ramsey_certificate"]
            or FIXED_EDGE not in deleted
            or len(deleted) > 5
        ):
            raise RuntimeError("separated candidate failed independent semantics")
        base.update(
            {
                "status": "SAT_VERIFIED",
                "candidate": str(output.resolve()),
                "candidate_sha256": sha256(output),
                "deleted_edges": [list(edge) for edge in deleted],
                "added_edges": [
                    list(edge) for edge in sorted(final_edges - original_edges)
                ],
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
                "reason": "cut discovery did not reach SAT or UNSAT within bounds",
                "global_ramsey_implication": None,
                "elapsed_seconds": time.perf_counter() - started,
            }
        )
        finish(base, args.json)
        return

    lazy_masks = discovery.pop("lazy_masks")
    if any(mask.bit_count() != 18 for mask in lazy_masks):
        raise AssertionError("frozen cut bank contains a non-I18 mask")
    if len(set(lazy_masks)) != len(lazy_masks):
        raise AssertionError("frozen cut bank contains duplicate masks")

    variables, pairs = build_variables(len(initial))
    original_edges = {edge for edge in pairs if edge_present(initial, *edge)}
    clauses, maximum_variable, preloaded, formula = branch_formula(
        initial,
        variables,
        pairs,
        original_edges,
        FIXED_EDGE,
        residual_budget=4,
        preload_limit=args.preload_i18,
    )
    clauses.extend(hitting_clause(mask, len(initial), variables) for mask in lazy_masks)
    if maximum_variable != discovery["maximum_variable"]:
        raise AssertionError("non-deterministic variable reconstruction")
    cut_bank = {
        "fixed_deleted_edge": list(FIXED_EDGE),
        "preloaded_masks": [f"{mask:025x}" for mask in preloaded],
        "preloaded_masks_sha256": masks_hash(preloaded),
        "lazy_masks": [f"{mask:025x}" for mask in lazy_masks],
        "lazy_masks_sha256": masks_hash(lazy_masks),
        "all_masks_are_18_sets": True,
    }
    cut_path = prefix.with_suffix(".cuts.json")
    atomic_json(cut_path, cut_bank)
    cnf_path = prefix.with_suffix(".cnf.gz")
    cnf_raw_hash, cnf_gzip_hash, cnf_bytes, cnf_lines = deterministic_gzip_text(
        cnf_path, dimacs_lines(clauses, maximum_variable)
    )
    base["finite_formula"] = {
        **formula,
        "lazy_I18_hitting_clauses": len(lazy_masks),
        "final_clause_count": len(clauses),
        "cut_bank": str(cut_path.resolve()),
        "cut_bank_sha256": sha256(cut_path),
        "dimacs_gzip": str(cnf_path.resolve()),
        "dimacs_uncompressed_sha256": cnf_raw_hash,
        "dimacs_gzip_sha256": cnf_gzip_hash,
        "dimacs_uncompressed_bytes": cnf_bytes,
        "dimacs_lines": cnf_lines,
    }

    proof_path = prefix.with_suffix(".drat.gz")
    proof = run_external_proof(
        args.cadical, cnf_path, proof_path, args.proof_seconds
    )
    base["external_proof_run"] = proof
    if proof["status"] != "UNSAT_PROOF_WRITTEN":
        base.update(
            {
                "status": "UNKNOWN",
                "reason": "finite CNF UNSAT was discovered, but proof run did not finish",
                "global_ramsey_implication": None,
                "elapsed_seconds": time.perf_counter() - started,
            }
        )
        finish(base, args.json)
        return

    drat = verify_drat_trace(
        args.drat_trim, cnf_path, proof_path, args.drat_check_seconds
    )
    base["drat_check"] = drat
    if drat["status"] == "VERIFIED":
        base.update(
            {
                "status": "UNSAT_PROOF_VERIFIED",
                "conclusion": (
                    "The fixed (97,98)-deletion branch has no completion with "
                    "at most four further input-edge deletions, even allowing "
                    "arbitrary additions of input nonedges."
                ),
                "global_ramsey_implication": None,
            }
        )
    else:
        base.update(
            {
                "status": "UNKNOWN",
                "reason": "DRAT checker did not verify the proof within bounds",
                "global_ramsey_implication": None,
            }
        )
    base["elapsed_seconds"] = time.perf_counter() - started
    finish(base, args.json)


if __name__ == "__main__":
    main()
