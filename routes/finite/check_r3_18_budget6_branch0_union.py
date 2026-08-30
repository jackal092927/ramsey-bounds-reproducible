#!/usr/bin/env python3
"""Independent semantic audit for the frozen budget-six branch-0 union proof."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
import os
import shutil
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Iterator

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool

try:
    from .verify_ramsey import verify
except ImportError:  # pragma: no cover
    from verify_ramsey import verify


EXPECTED = {
    "seed": "e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e",
    "cnf_gzip": "47052de808b98598f2f144251a6ad73c1415dd00fef9e04b99ffe2f176229fbf",
    "cnf_raw": "0dec49bdbee74644db5fc181e25f7df02a72dfd1b23a3ab4f859501de8a0d3cd",
    "cuts": "91b5709248ff641a315f5a0389b4f3fde3d38514f3b1a8b31b6cad31224f250b",
    "I18_ordered": "f10690b826b86eb03567a2ffaffb553801fae32af20cfe4337118bddf4e41afa",
    "drat_gzip": "4d948ab34f1d2475af6efe943e0a4899827c78b96c2bc3835b5161f189c26bb5",
    "drat_raw": "43dde468b13a1f45667b0a8dc54c2c7d14b0b33f6dc01d85383b0a37f5ffca91",
    "drat_trim": "31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4",
}
EXPECTED_DRAT_BYTES = 3_493_847_713
EXPECTED_DRAT_LINES = 6_649_939
FIXED = (97, 98)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def gzip_stats(path: Path) -> dict:
    digest = hashlib.sha256()
    size = lines = 0
    with gzip.open(path, "rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
            size += len(chunk)
            lines += chunk.count(b"\n")
    return {"sha256": digest.hexdigest(), "bytes": size, "lines": lines}


def read_matrix(path: Path) -> list[list[int]]:
    rows = [[int(value) for value in line.split()] for line in path.read_text().splitlines()]
    if len(rows) != 100 or any(len(row) != 100 for row in rows):
        raise AssertionError("seed shape mismatch")
    for u in range(100):
        if rows[u][u] != 0:
            raise AssertionError("nonzero seed diagonal")
        for v in range(u + 1, 100):
            if rows[u][v] not in (0, 1) or rows[u][v] != rows[v][u]:
                raise AssertionError("seed is not a simple undirected graph")
    return rows


def clause_stream(path: Path) -> tuple[tuple[int, int], Iterator[list[int]]]:
    source = gzip.open(path, "rt", encoding="ascii")
    header = source.readline().split()
    if len(header) != 4 or header[:2] != ["p", "cnf"]:
        source.close()
        raise AssertionError("bad DIMACS header")

    def iterator() -> Iterator[list[int]]:
        try:
            for line in source:
                values = [int(value) for value in line.split()]
                if not values or values[-1] != 0:
                    raise AssertionError("malformed clause")
                yield values[:-1]
        finally:
            source.close()

    return (int(header[2]), int(header[3])), iterator()


def audit_semantics(directory: Path) -> dict:
    seed = directory / "certificates/r3_18_n100_nearmiss.txt"
    cnf = directory / "r3_18_budget6_branch_0_universal_union.cnf.gz"
    cuts = directory / "r3_18_budget6_branch_0_universal_union.cuts.json"
    if sha256(seed) != EXPECTED["seed"] or sha256(cnf) != EXPECTED["cnf_gzip"]:
        raise AssertionError("seed or CNF identity mismatch")
    if sha256(cuts) != EXPECTED["cuts"]:
        raise AssertionError("cut-bank identity mismatch")
    raw_cnf = gzip_stats(cnf)
    if raw_cnf["sha256"] != EXPECTED["cnf_raw"]:
        raise AssertionError("raw CNF identity mismatch")
    matrix = read_matrix(seed)
    if sum(matrix[u][v] for u in range(100) for v in range(u + 1, 100)) != 827:
        raise AssertionError("seed edge count mismatch")
    triangles = [
        triple for triple in itertools.combinations(range(100), 3)
        if matrix[triple[0]][triple[1]]
        and matrix[triple[0]][triple[2]]
        and matrix[triple[1]][triple[2]]
    ]
    if triangles != [(97, 98, 99)]:
        raise AssertionError("seed triangle family mismatch")
    seed_check = verify(seed, 3, 18)
    if seed_check["searches"]["forbidden_independent_set"]["exists"]:
        raise AssertionError("seed unexpectedly has I18")
    prior = json.loads((directory / "r3_18_extension_repair_check.json").read_text())
    if not prior.get("fixed_seed_budget5_repair_ball_unsat"):
        raise AssertionError("budget-five proof dependency missing")
    for record in ("r3_18_budget6_branch_1_proof.json", "r3_18_budget6_branch_2.json"):
        if json.loads((directory / record).read_text()).get("status") != "UNSAT_PROOF_VERIFIED":
            raise AssertionError("another branch proof dependency is not verified")

    pairs = list(itertools.combinations(range(100), 2))
    variables = {edge: index + 1 for index, edge in enumerate(pairs)}
    inverse = {value: edge for edge, value in variables.items()}
    original = {edge for edge in pairs if matrix[edge[0]][edge[1]]}
    pool = IDPool(start_from=4951)
    exact = CardEnc.equals(
        lits=[-variables[edge] for edge in sorted(original - {FIXED})],
        bound=5,
        vpool=pool,
        encoding=EncType.seqcounter,
    ).clauses
    header, stream = clause_stream(cnf)
    if header != (13160, 429892) or pool.top != 13160:
        raise AssertionError("header or variable reconstruction mismatch")
    seen = 0
    for a, b, c in itertools.combinations(range(100), 3):
        if next(stream) != [-variables[(a, b)], -variables[(a, c)], -variables[(b, c)]]:
            raise AssertionError("triangle prefix mismatch")
        seen += 1
    for clause in exact:
        if next(stream) != clause:
            raise AssertionError("exact-five counter mismatch")
        seen += 1
    if next(stream) != [-variables[FIXED]]:
        raise AssertionError("fixed-edge unit mismatch")
    seen += 1
    masks: list[int] = []
    for clause in stream:
        if len(clause) != 153 or len(set(clause)) != 153 or any(lit <= 0 for lit in clause):
            raise AssertionError("malformed I18 clause")
        try:
            edges = {inverse[lit] for lit in clause}
        except KeyError as error:
            raise AssertionError("I18 clause contains an auxiliary variable") from error
        vertices = {vertex for edge in edges for vertex in edge}
        if len(vertices) != 18 or edges != set(itertools.combinations(sorted(vertices), 2)):
            raise AssertionError("I18 clause is not a complete 18-set pair family")
        masks.append(sum(1 << vertex for vertex in vertices))
        seen += 1
    if seen != header[1] or len(masks) != 251771 or len(set(masks)) != len(masks):
        raise AssertionError("I18 or clause accounting mismatch")
    cut_payload = json.loads(cuts.read_text())
    stored = [int(value, 16) for value in cut_payload["masks"]]
    if stored != masks or cut_payload.get("fixed_deleted_edge") != [97, 98]:
        raise AssertionError("cut bank and CNF tail differ")
    digest = hashlib.sha256()
    for mask in masks:
        digest.update(f"{mask:016x}\n".encode("ascii"))
    ordered_hash = digest.hexdigest()
    if ordered_hash != EXPECTED["I18_ordered"] or cut_payload.get("masks_sha256") != ordered_hash:
        raise AssertionError("ordered I18 digest mismatch")
    return {
        "status": "SEMANTICS_VERIFIED",
        "variables": header[0],
        "clauses": header[1],
        "triangle_clauses": 161700,
        "exact_five_clauses": len(exact),
        "fixed_negative_units": 1,
        "I18_hitting_clauses": len(masks),
        "I18_ordered_sha256": ordered_hash,
        "fixed_deleted_edge": [97, 98],
        "total_input_edge_deletions": 6,
        "residual_input_edge_deletions": 5,
        "arbitrary_original_nonedges_free": True,
        "budget5_dependency_checked": True,
        "three_branch_cover": [[97, 98], [97, 99], [98, 99]],
        "other_two_branches_recorded_proofs_verified": True,
        "cnf_gzip_sha256": EXPECTED["cnf_gzip"],
        "cnf_raw_sha256": EXPECTED["cnf_raw"],
        "cut_bank_sha256": EXPECTED["cuts"],
    }


def audit_proof(directory: Path, checker: Path | None, seconds: float) -> dict:
    cnf = directory / "r3_18_budget6_branch_0_universal_union.cnf.gz"
    proof = directory / "r3_18_budget6_branch_0_universal_union.drat.gz"
    if sha256(proof) != EXPECTED["drat_gzip"]:
        raise AssertionError("proof gzip identity mismatch")
    raw = gzip_stats(proof)
    if raw != {"sha256": EXPECTED["drat_raw"], "bytes": EXPECTED_DRAT_BYTES, "lines": EXPECTED_DRAT_LINES}:
        raise AssertionError("raw proof identity mismatch")
    result = {"status": "ARTIFACT_VERIFIED_NOT_REPLAYED", **raw, "gzip_sha256": EXPECTED["drat_gzip"]}
    if checker is None:
        return result
    if not checker.is_file() or not os.access(checker, os.X_OK):
        raise AssertionError("checker is not executable")
    checker_hash = sha256(checker)
    started = time.perf_counter()
    with tempfile.TemporaryDirectory(prefix="ramsey-r3-18-b0-union-check-") as name:
        temporary = Path(name)
        raw_cnf = temporary / "branch0.cnf"
        raw_proof = temporary / "branch0.drat"
        with gzip.open(cnf, "rb") as source, raw_cnf.open("wb") as target:
            shutil.copyfileobj(source, target)
        with gzip.open(proof, "rb") as source, raw_proof.open("wb") as target:
            shutil.copyfileobj(source, target)
        completed = subprocess.run(
            [str(checker), str(raw_cnf), str(raw_proof)],
            check=False,
            capture_output=True,
            text=True,
            timeout=seconds,
        )
    if completed.returncode != 0 or "s VERIFIED" not in completed.stdout:
        raise AssertionError("DRAT replay failed")
    result.update({
        "status": "VERIFIED",
        "checker_sha256": checker_hash,
        "matches_historical_binary_sha256": checker_hash == EXPECTED["drat_trim"],
        "exitcode": completed.returncode,
        "elapsed_seconds": time.perf_counter() - started,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
    })
    return result


def atomic_json(path: Path, payload: dict) -> None:
    temporary = path.with_name(path.name + f".tmp.{os.getpid()}")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    temporary.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-dir", type=Path, default=Path(__file__).parent)
    parser.add_argument("--drat-trim", type=Path)
    parser.add_argument("--drat-seconds", type=float, default=360.0)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    semantics = audit_semantics(args.artifact_dir)
    proof = audit_proof(args.artifact_dir, args.drat_trim, args.drat_seconds)
    proof_replayed = proof["status"] == "VERIFIED"
    current_status = (
        "BRANCH0_SEMANTICS_AND_PROOF_VERIFIED"
        if proof_replayed
        else "BRANCH0_SEMANTICS_VERIFIED_PROOF_NOT_REQUESTED"
    )
    result = {
        "status": current_status,
        "recorded_provenance": {
            "all_three_exact_budget6_branches_proof_verified": True,
            "fixed_seed_deletion_repair_radius_at_least_7": True,
        },
        "current_run": {
            "status": current_status,
            "semantics_status": "VERIFIED",
            "proof_status": "VERIFIED" if proof_replayed else "NOT_REQUESTED",
            "all_three_exact_budget6_branches_proof_verified": False,
            "fixed_seed_deletion_repair_radius_at_least_7": False,
        },
        "semantics": semantics,
        "proof": proof,
        "all_three_exact_budget6_branches_proof_verified": False,
        "fixed_seed_budget_at_most_6_excluded": False,
        "fixed_seed_deletion_repair_radius_at_least_7": False,
        "seven_deletion_repair_exists": None,
        "seven_deletion_repair_exists_is_established": False,
        "R_3_18_ge_101_established": False,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if args.json is not None:
        atomic_json(args.json, result)


if __name__ == "__main__":
    main()
