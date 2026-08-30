#!/usr/bin/env python3
"""Minimal semantic and optional DRAT checker for the R(3,18) repair audit."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from pathlib import Path
from typing import Iterator

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool

try:
    from .bounded_deletion_sat_cegar import build_variables
    from .budget8_next import verify_drat_trace
    from .new_basin_search import edge_present, triangle_tuples
    from .verify_ramsey import read_matrix, verify
except ImportError:  # pragma: no cover - direct execution
    from bounded_deletion_sat_cegar import build_variables
    from budget8_next import verify_drat_trace
    from new_basin_search import edge_present, triangle_tuples
    from verify_ramsey import read_matrix, verify


BASE_SHA = "3e9d16e29111f3a2f25ae3b992235804c2612de2f6ada5570901d17ceedfca45"
NEAR_SHA = "e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e"
TRIANGLE = (97, 98, 99)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        while True:
            chunk = source.read(1024 * 1024)
            if not chunk:
                return digest.hexdigest()
            digest.update(chunk)


def clauses(path: Path) -> tuple[tuple[int, int], Iterator[list[int]]]:
    source = gzip.open(path, "rt", encoding="ascii")
    header = source.readline().split()
    if len(header) != 4 or header[:2] != ["p", "cnf"]:
        source.close()
        raise AssertionError(f"bad DIMACS header in {path}")

    def iterator() -> Iterator[list[int]]:
        try:
            for line in source:
                values = [int(value) for value in line.split()]
                if not values or values[-1] != 0:
                    raise AssertionError(f"bad DIMACS clause in {path}")
                yield values[:-1]
        finally:
            source.close()

    return (int(header[2]), int(header[3])), iterator()


def assert_hitting_clause(clause: list[int], inverse: dict[int, tuple[int, int]]) -> None:
    if len(clause) != 153 or len(set(clause)) != 153 or any(lit <= 0 for lit in clause):
        raise AssertionError("blue clause is not 153 distinct positive edge literals")
    try:
        pairs = {inverse[lit] for lit in clause}
    except KeyError as error:
        raise AssertionError("blue clause uses a non-edge/auxiliary variable") from error
    vertices = {vertex for pair in pairs for vertex in pair}
    expected = set(itertools.combinations(sorted(vertices), 2))
    if len(vertices) != 18 or pairs != expected:
        raise AssertionError("blue clause is not the full edge set of an 18-set")


def audit_cnf(
    path: Path,
    rows: list[int],
    fixed_edge: tuple[int, int],
    expected_gzip_sha: str,
) -> dict:
    if sha256(path) != expected_gzip_sha:
        raise AssertionError(f"gzip hash mismatch for {path}")
    variables, pairs = build_variables(len(rows))
    inverse = {variable: edge for edge, variable in variables.items()}
    original = {edge for edge in pairs if edge_present(rows, *edge)}

    pool = IDPool(start_from=len(pairs) + 1)
    residual = sorted(original - {fixed_edge})
    cardinality = CardEnc.atmost(
        lits=[-variables[edge] for edge in residual],
        bound=4,
        vpool=pool,
        encoding=EncType.seqcounter,
    ).clauses
    header, stream = clauses(path)
    if header[0] != pool.top:
        raise AssertionError("unexpected maximum variable")

    seen = 0
    for a, b, c in itertools.combinations(range(len(rows)), 3):
        expected = [-variables[(a, b)], -variables[(a, c)], -variables[(b, c)]]
        if next(stream) != expected:
            raise AssertionError("triangle-free prefix differs from reconstruction")
        seen += 1
    for expected in cardinality:
        if next(stream) != expected:
            raise AssertionError("residual deletion counter differs from reconstruction")
        seen += 1
    if next(stream) != [-variables[fixed_edge]]:
        raise AssertionError("fixed edge is not a negative unit")
    seen += 1

    blue = 0
    for clause in stream:
        assert_hitting_clause(clause, inverse)
        blue += 1
        seen += 1
    if seen != header[1] or blue == 0:
        raise AssertionError("DIMACS clause count mismatch or empty I18 bank")
    return {
        "status": "SEMANTICS_VERIFIED",
        "fixed_deleted_edge": list(fixed_edge),
        "maximum_variable": header[0],
        "clauses": header[1],
        "triangle_clauses": len(rows) * (len(rows) - 1) * (len(rows) - 2) // 6,
        "residual_deletion_counter_clauses": len(cardinality),
        "fixed_negative_units": 1,
        "I18_hitting_clauses": blue,
        "arbitrary_original_nonedges_unconstrained_by_deletion_counter": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-dir", type=Path, default=Path(__file__).parent)
    parser.add_argument("--drat-trim", type=Path)
    parser.add_argument("--drat-seconds", type=float, default=120.0)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()

    directory = args.artifact_dir
    base = directory / "certificates/alphaevolve_R3_18_ge_100.txt"
    near = directory / "certificates/r3_18_n100_nearmiss.txt"
    if sha256(base) != BASE_SHA or sha256(near) != NEAR_SHA:
        raise AssertionError("frozen matrix hash mismatch")
    base_rows = read_matrix(base)
    near_rows = read_matrix(near)
    old_mask = (1 << 99) - 1
    if [row & old_mask for row in near_rows[:99]] != base_rows:
        raise AssertionError("near miss does not preserve the entire 99-vertex block")
    if triangle_tuples(near_rows) != [TRIANGLE]:
        raise AssertionError("near miss does not have the claimed unique triangle")
    new_neighborhood = [v for v in range(99) if (near_rows[99] >> v) & 1]
    neighborhood_edges = [
        [u, v]
        for u, v in itertools.combinations(new_neighborhood, 2)
        if edge_present(base_rows, u, v)
    ]
    if neighborhood_edges != [[97, 98]]:
        raise AssertionError("near miss does not have exactly one extension conflict")

    main_result = json.loads(
        (directory / "r3_18_budget5_branch.json").read_text(encoding="utf-8")
    )
    two_stage = json.loads(
        (directory / "r3_18_budget5_branch_0_twostage.json").read_text(encoding="utf-8")
    )
    branch_records = {
        0: {
            "edge": (97, 98),
            "cnf": directory / "r3_18_budget5_branch_0_twostage.cnf.gz",
            "drat": directory / "r3_18_budget5_branch_0_twostage.drat.gz",
            "cnf_sha": two_stage["finite_formula"]["dimacs_gzip_sha256"],
            "recorded_proof_status": two_stage["drat_check"]["status"],
        },
        1: {
            "edge": (97, 99),
            "cnf": directory / "r3_18_budget5_branch_1.cnf.gz",
            "drat": directory / "r3_18_budget5_branch_1.drat.gz",
            "cnf_sha": main_result["branches"][1]["dimacs_gzip_sha256"],
            "recorded_proof_status": main_result["branches"][1]["drat_check"]["status"],
        },
        2: {
            "edge": (98, 99),
            "cnf": directory / "r3_18_budget5_branch_2.cnf.gz",
            "drat": directory / "r3_18_budget5_branch_2.drat.gz",
            "cnf_sha": main_result["branches"][2]["dimacs_gzip_sha256"],
            "recorded_proof_status": main_result["branches"][2]["drat_check"]["status"],
        },
    }

    audited = []
    for index, record in branch_records.items():
        semantic = audit_cnf(record["cnf"], near_rows, record["edge"], record["cnf_sha"])
        if record["recorded_proof_status"] != "VERIFIED":
            raise AssertionError("stored branch lacks a verified proof record")
        proof = {"status": "NOT_REQUESTED"}
        if args.drat_trim is not None:
            proof = verify_drat_trace(
                args.drat_trim,
                record["cnf"],
                record["drat"],
                args.drat_seconds,
            )
            if proof["status"] != "VERIFIED":
                raise AssertionError(f"branch {index} DRAT verification failed")
        audited.append(
            {
                "branch": index,
                "semantics": semantic,
                "recorded_provenance": {
                    "proof_status": "VERIFIED_IN_PINNED_RECORD"
                },
                "current_run": {"proof": proof},
            }
        )

    base_check = verify(base, 3, 18)
    near_check = verify(near, 3, 18)
    if not base_check["valid_ramsey_certificate"]:
        raise AssertionError("frozen 99-vertex certificate is invalid")
    if near_check["searches"]["forbidden_independent_set"]["exists"]:
        raise AssertionError("near miss contains an I18")

    all_replayed = all(
        branch["current_run"]["proof"]["status"] == "VERIFIED"
        for branch in audited
    )
    current_status = (
        "ALL_THREE_BRANCHES_SEMANTICS_AND_PROOFS_VERIFIED"
        if all_replayed
        else "ALL_THREE_BRANCHES_SEMANTICS_VERIFIED_PROOFS_NOT_REQUESTED"
    )
    result = {
        "status": current_status,
        "recorded_provenance": {
            "proof_status": "ALL_THREE_VERIFIED_IN_PINNED_RECORDS",
            "fixed_seed_budget5_repair_ball_unsat": True,
        },
        "current_run": {
            "status": current_status,
            "semantics_status": "ALL_THREE_VERIFIED",
            "proof_status": "ALL_THREE_VERIFIED" if all_replayed else "NOT_REQUESTED",
            "fixed_seed_budget5_repair_ball_unsat": all_replayed,
        },
        "fixed_seed_budget5_repair_ball_unsat": all_replayed,
        "global_ramsey_bound_improvement": False,
        "base_sha256": BASE_SHA,
        "near_miss_sha256": NEAR_SHA,
        "near_miss_new_vertex_neighborhood": new_neighborhood,
        "near_miss_extension_conflict_edges": neighborhood_edges,
        "base_bitset_verification": base_check,
        "near_miss_bitset_verification": near_check,
        "branches": audited,
    }
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.json is not None:
        args.json.write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
