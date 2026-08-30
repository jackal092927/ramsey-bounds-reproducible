#!/usr/bin/env python3
"""Independent semantic and proof audit for exact-budget-six branch 1.

This checker does not trust the discovery checkpoint or its solver label.  It
reconstructs the complete frozen CNF clause by clause, validates the I18 cut
bank, checks the compressed artifact identities, and optionally replays the
complete DRAT with the pinned official checker.
"""

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
except ImportError:  # pragma: no cover - direct execution
    from verify_ramsey import verify


EXPECTED_SEED_SHA256 = (
    "e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e"
)
EXPECTED_CNF_GZIP_SHA256 = (
    "a438c9fef4d99ae516829e4405da8c9f079398501361f9c5f69f46a494ffad14"
)
EXPECTED_CNF_RAW_SHA256 = (
    "ced3fd39370b4c2552cb261638fb7076da173e18d6b871f6fb280668e5a1154a"
)
EXPECTED_CUT_BANK_SHA256 = (
    "f8064f0f226659b4750382f781ba9a862bcc19eb49006eb8cdd2afc002ed227c"
)
EXPECTED_I18_ORDERED_SHA256 = (
    "99b72cd5500c6140d4aca261a1028b9805b9d8209ffc3216596a0fb8fb50edcf"
)
EXPECTED_DRAT_GZIP_SHA256 = (
    "cfe694fd728903ee9ac9f08a66ade64faf7e68763246d1d52ca29a85727494ec"
)
EXPECTED_DRAT_RAW_SHA256 = (
    "fbf7292c3bcbf52ec6f978fca0751d319e2e2029380e7a865a17430baf282902"
)
EXPECTED_DRAT_RAW_BYTES = 2_137_671_968
EXPECTED_DRAT_RAW_LINES = 5_590_150
EXPECTED_DRAT_TRIM_SHA256 = (
    "31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4"
)
EXPECTED_FIXED_EDGE = (97, 99)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def gzip_stats(path: Path) -> dict[str, int | str]:
    digest = hashlib.sha256()
    size = 0
    lines = 0
    with gzip.open(path, "rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
            size += len(chunk)
            lines += chunk.count(b"\n")
    return {"sha256": digest.hexdigest(), "bytes": size, "lines": lines}


def ordered_masks_sha256(masks: list[int]) -> str:
    digest = hashlib.sha256()
    for mask in masks:
        digest.update(f"{mask:016x}\n".encode("ascii"))
    return digest.hexdigest()


def read_matrix(path: Path) -> list[list[int]]:
    rows = [[int(value) for value in line.split()] for line in path.read_text().splitlines()]
    if len(rows) != 100 or any(len(row) != 100 for row in rows):
        raise AssertionError("seed is not a 100-by-100 matrix")
    if any(value not in (0, 1) for row in rows for value in row):
        raise AssertionError("seed matrix is not binary")
    for u in range(100):
        if rows[u][u] != 0:
            raise AssertionError("seed diagonal is nonzero")
        for v in range(u + 1, 100):
            if rows[u][v] != rows[v][u]:
                raise AssertionError("seed matrix is asymmetric")
    return rows


def clause_stream(path: Path) -> tuple[tuple[int, int], Iterator[list[int]]]:
    source = gzip.open(path, "rt", encoding="ascii")
    header = source.readline().split()
    if len(header) != 4 or header[:2] != ["p", "cnf"]:
        source.close()
        raise AssertionError("invalid DIMACS header")

    def iterator() -> Iterator[list[int]]:
        try:
            for line in source:
                values = [int(value) for value in line.split()]
                if not values or values[-1] != 0:
                    raise AssertionError("invalid DIMACS clause")
                yield values[:-1]
        finally:
            source.close()

    return (int(header[2]), int(header[3])), iterator()


def audit_semantics(directory: Path) -> dict:
    seed = directory / "certificates/r3_18_n100_nearmiss.txt"
    cnf = directory / "r3_18_budget6_branch_1.cnf.gz"
    cuts = directory / "r3_18_budget6_branch_1.cuts.json"
    prior = directory / "r3_18_extension_repair_check.json"
    if sha256(seed) != EXPECTED_SEED_SHA256:
        raise AssertionError("seed SHA-256 mismatch")
    if sha256(cnf) != EXPECTED_CNF_GZIP_SHA256:
        raise AssertionError("CNF gzip SHA-256 mismatch")
    if sha256(cuts) != EXPECTED_CUT_BANK_SHA256:
        raise AssertionError("cut-bank SHA-256 mismatch")
    cnf_raw = gzip_stats(cnf)
    if cnf_raw["sha256"] != EXPECTED_CNF_RAW_SHA256:
        raise AssertionError("uncompressed CNF SHA-256 mismatch")

    matrix = read_matrix(seed)
    edge_count = sum(matrix[u][v] for u in range(100) for v in range(u + 1, 100))
    if edge_count != 827:
        raise AssertionError("unexpected seed edge count")
    triangles = [
        triple
        for triple in itertools.combinations(range(100), 3)
        if matrix[triple[0]][triple[1]]
        and matrix[triple[0]][triple[2]]
        and matrix[triple[1]][triple[2]]
    ]
    if triangles != [(97, 98, 99)]:
        raise AssertionError("unexpected seed triangle family")
    seed_check = verify(seed, 3, 18)
    if seed_check["searches"]["forbidden_independent_set"]["exists"]:
        raise AssertionError("seed unexpectedly has an independent 18-set")
    prior_check = json.loads(prior.read_text(encoding="utf-8"))
    if not prior_check.get("fixed_seed_budget5_repair_ball_unsat"):
        raise AssertionError("checked budget-five dependency is absent")

    pairs = list(itertools.combinations(range(100), 2))
    variables = {edge: index + 1 for index, edge in enumerate(pairs)}
    inverse = {value: edge for edge, value in variables.items()}
    original = {edge for edge in pairs if matrix[edge[0]][edge[1]]}
    residual = sorted(original - {EXPECTED_FIXED_EDGE})
    if len(residual) != 826:
        raise AssertionError("unexpected residual input-edge count")
    pool = IDPool(start_from=len(pairs) + 1)
    exact_five = CardEnc.equals(
        lits=[-variables[edge] for edge in residual],
        bound=5,
        vpool=pool,
        encoding=EncType.seqcounter,
    ).clauses

    header, stream = clause_stream(cnf)
    if header != (13160, 242064) or pool.top != 13160:
        raise AssertionError("CNF header or reconstructed variable count mismatch")
    seen = 0
    for a, b, c in itertools.combinations(range(100), 3):
        expected = [-variables[(a, b)], -variables[(a, c)], -variables[(b, c)]]
        if next(stream) != expected:
            raise AssertionError("triangle prefix mismatch")
        seen += 1
    for expected in exact_five:
        if next(stream) != expected:
            raise AssertionError("exact-five sequential counter mismatch")
        seen += 1
    if next(stream) != [-variables[EXPECTED_FIXED_EDGE]]:
        raise AssertionError("fixed deleted-edge unit mismatch")
    seen += 1

    masks: list[int] = []
    for clause in stream:
        if len(clause) != 153 or len(set(clause)) != 153 or any(lit <= 0 for lit in clause):
            raise AssertionError("malformed I18 hitting clause")
        try:
            edges = {inverse[lit] for lit in clause}
        except KeyError as error:
            raise AssertionError("I18 clause contains a counter variable") from error
        vertices = {vertex for edge in edges for vertex in edge}
        if len(vertices) != 18 or edges != set(itertools.combinations(sorted(vertices), 2)):
            raise AssertionError("I18 clause is not a complete 18-set edge family")
        masks.append(sum(1 << vertex for vertex in vertices))
        seen += 1
    if seen != header[1] or len(masks) != 63943 or len(set(masks)) != len(masks):
        raise AssertionError("clause accounting or I18 uniqueness mismatch")

    cut_payload = json.loads(cuts.read_text(encoding="utf-8"))
    stored_masks = [int(value, 16) for value in cut_payload["masks"]]
    if cut_payload.get("fixed_deleted_edge") != [97, 99]:
        raise AssertionError("cut bank names the wrong branch")
    if not cut_payload.get("all_masks_are_18_sets"):
        raise AssertionError("cut bank does not certify its mask sizes")
    if stored_masks != masks or any(mask.bit_count() != 18 for mask in masks):
        raise AssertionError("cut-bank masks differ from the CNF tail")
    digest = ordered_masks_sha256(masks)
    if digest != EXPECTED_I18_ORDERED_SHA256 or cut_payload.get("masks_sha256") != digest:
        raise AssertionError("ordered I18 digest mismatch")

    return {
        "status": "SEMANTICS_VERIFIED",
        "seed_sha256": EXPECTED_SEED_SHA256,
        "seed_edges": edge_count,
        "unique_seed_triangle": [97, 98, 99],
        "seed_has_independent_18_set": False,
        "budget5_dependency_checked": True,
        "fixed_deleted_edge": [97, 99],
        "total_input_edge_deletions": 6,
        "residual_input_edge_deletions": 5,
        "arbitrary_original_nonedges_absent_from_deletion_counter": True,
        "variables": header[0],
        "clauses": header[1],
        "triangle_clauses": 161700,
        "exact_five_clauses": len(exact_five),
        "fixed_negative_units": 1,
        "I18_hitting_clauses": len(masks),
        "I18_ordered_sha256": digest,
        "cnf_gzip_sha256": EXPECTED_CNF_GZIP_SHA256,
        "cnf_raw_sha256": cnf_raw["sha256"],
        "cut_bank_sha256": EXPECTED_CUT_BANK_SHA256,
    }


def audit_proof(directory: Path, checker: Path | None, seconds: float) -> dict:
    cnf = directory / "r3_18_budget6_branch_1.cnf.gz"
    proof = directory / "r3_18_budget6_branch_1.drat.gz"
    if sha256(proof) != EXPECTED_DRAT_GZIP_SHA256:
        raise AssertionError("DRAT gzip SHA-256 mismatch")
    raw = gzip_stats(proof)
    if raw != {
        "sha256": EXPECTED_DRAT_RAW_SHA256,
        "bytes": EXPECTED_DRAT_RAW_BYTES,
        "lines": EXPECTED_DRAT_RAW_LINES,
    }:
        raise AssertionError("uncompressed DRAT identity mismatch")
    result: dict = {
        "status": "ARTIFACT_VERIFIED_NOT_REPLAYED",
        "drat_gzip_sha256": EXPECTED_DRAT_GZIP_SHA256,
        "drat_raw_sha256": raw["sha256"],
        "drat_raw_bytes": raw["bytes"],
        "drat_raw_lines": raw["lines"],
    }
    if checker is None:
        return result
    if not checker.is_file() or not os.access(checker, os.X_OK):
        raise AssertionError("DRAT checker is not executable")
    checker_hash = sha256(checker)
    started = time.perf_counter()
    with tempfile.TemporaryDirectory(prefix="ramsey-r3-18-branch1-check-") as name:
        temporary = Path(name)
        raw_cnf = temporary / "branch1.cnf"
        raw_proof = temporary / "branch1.drat"
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
    verdict_lines = {line.strip() for line in completed.stdout.splitlines()}
    verified = completed.returncode == 0 and "s VERIFIED" in verdict_lines
    result.update(
        {
            "status": "VERIFIED" if verified else "FAILED",
            "checker_sha256": checker_hash,
            "matches_historical_binary_sha256": (
                checker_hash == EXPECTED_DRAT_TRIM_SHA256
            ),
            "checker_exitcode": completed.returncode,
            "elapsed_seconds": time.perf_counter() - started,
            "stdout": completed.stdout,
            "stderr": completed.stderr,
        }
    )
    if not verified:
        raise AssertionError("DRAT replay did not return an exact s VERIFIED line")
    return result


def atomic_json(path: Path, payload: dict) -> None:
    temporary = path.with_name(path.name + f".tmp.{os.getpid()}")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    temporary.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact-dir", type=Path, default=Path(__file__).parent)
    parser.add_argument("--drat-trim", type=Path)
    parser.add_argument("--drat-seconds", type=float, default=300.0)
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    semantics = audit_semantics(args.artifact_dir)
    proof = audit_proof(args.artifact_dir, args.drat_trim, args.drat_seconds)
    current_status = (
            "BRANCH1_EXACT_BUDGET6_PROOF_VERIFIED"
            if proof["status"] == "VERIFIED"
            else "BRANCH1_EXACT_BUDGET6_ARTIFACT_AUDITED_NOT_REPLAYED"
        )
    result = {
        "status": current_status,
        "recorded_provenance": {
            "proof_status": "VERIFIED_IN_PINNED_RECORD",
        },
        "current_run": {
            "status": current_status,
            "semantics_status": "VERIFIED",
            "proof_status": (
                "VERIFIED" if proof["status"] == "VERIFIED" else "NOT_REQUESTED"
            ),
        },
        "semantics": semantics,
        "proof": proof,
        "overall_budget6_three_branch_status": "UNKNOWN_BRANCH_0_ONLY",
        "global_ramsey_bound_improvement": False,
    }
    rendered = json.dumps(result, indent=2, sort_keys=True)
    print(rendered)
    if args.json is not None:
        atomic_json(args.json, result)


if __name__ == "__main__":
    main()
