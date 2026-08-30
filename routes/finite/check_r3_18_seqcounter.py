#!/usr/bin/env python3
"""Independent sequential-counter audit for the six finite theorem CNFs.

This checker does not import or call PySAT's ``CardEnc``.  It derives the
canonical edge-literal lists from the frozen matrix, generates the
Sinz/Knuth clause schema through :mod:`independent_seqcounter`, and compares
the result clause-for-clause with each stored DIMACS counter block.
"""

from __future__ import annotations

import argparse
import gzip
import itertools
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

try:
    from .independent_seqcounter import (
        AtMostEncoding,
        EqualsEncoding,
        construct_atmost_extension,
        construct_equals_extension,
        dimacs_clause_sha256,
        encode_atmost,
        encode_equals,
    )
except ImportError:  # pragma: no cover - direct execution
    from independent_seqcounter import (
        AtMostEncoding,
        EqualsEncoding,
        construct_atmost_extension,
        construct_equals_extension,
        dimacs_clause_sha256,
        encode_atmost,
        encode_equals,
    )


SEED_SHA256 = "e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e"
PRIMARY_VARIABLES = 4_950
TRIANGLE_CLAUSES = 161_700


@dataclass(frozen=True)
class BranchSpec:
    name: str
    fixed_edge: tuple[int, int]
    mode: str
    bound: int
    counter_clauses: int
    maximum_variable: int
    total_clauses: int
    counter_sha256: str


BRANCHES = (
    BranchSpec(
        "r3_18_budget5_branch_0_twostage.cnf.gz",
        (97, 98),
        "atmost",
        4,
        7_394,
        8_238,
        169_382,
        "2afd86055bdc2dd2bb76605b134a577c1e54bba6c1afe3423289ce8ed826af31",
    ),
    BranchSpec(
        "r3_18_budget5_branch_1.cnf.gz",
        (97, 99),
        "atmost",
        4,
        7_394,
        8_238,
        184_967,
        "8244483115c967278d634d538a81af9fd498e4ff3478a287738db74b78060b2c",
    ),
    BranchSpec(
        "r3_18_budget5_branch_2.cnf.gz",
        (98, 99),
        "atmost",
        4,
        7_394,
        8_238,
        177_799,
        "e18df0ecfca43c41f4a4397c91d69dc6d277fcee92318310a4a2db3242a7106f",
    ),
    BranchSpec(
        "r3_18_budget6_branch_0_universal_union.cnf.gz",
        (97, 98),
        "equals",
        5,
        16_420,
        13_160,
        429_892,
        "e9ef2c53257f368f00398a246c357b3ad27e7c404dc922d4e00bed8a7d32a987",
    ),
    BranchSpec(
        "r3_18_budget6_branch_1.cnf.gz",
        (97, 99),
        "equals",
        5,
        16_420,
        13_160,
        242_064,
        "618a95f7a11f8e8d02f66b66a6ec29322b15d1f60593dd722e2dcf826cadf588",
    ),
    BranchSpec(
        "r3_18_budget6_branch_2.cnf.gz",
        (98, 99),
        "equals",
        5,
        16_420,
        13_160,
        183_543,
        "77d4558228fb16d054352b2feb075a31afffd5c414645c0a42e8554ddf1aba6c",
    ),
)


def sha256(path: Path) -> str:
    import hashlib

    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def read_matrix(path: Path) -> list[list[int]]:
    rows = [[int(value) for value in line.split()] for line in path.read_text().splitlines()]
    if len(rows) != 100 or any(len(row) != 100 for row in rows):
        raise AssertionError("the frozen seed is not a 100 by 100 matrix")
    for u in range(100):
        if rows[u][u] != 0:
            raise AssertionError("the frozen seed has a nonzero diagonal")
        for v in range(u + 1, 100):
            if rows[u][v] not in (0, 1) or rows[u][v] != rows[v][u]:
                raise AssertionError("the frozen seed is not a simple undirected graph")
    return rows


def clause_stream(path: Path) -> tuple[tuple[int, int], Iterator[list[int]]]:
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
                    raise AssertionError(f"malformed DIMACS clause in {path}")
                yield values[:-1]
        finally:
            source.close()

    return (int(header[2]), int(header[3])), iterator()


def primary_assignment(
    variables: dict[tuple[int, int], int],
    residual: list[tuple[int, int]],
    deletions: int,
) -> dict[int, bool]:
    values = {variable: True for variable in variables.values()}
    for edge in residual[:deletions]:
        values[variables[edge]] = False
    return values


def build_schema(
    spec: BranchSpec,
    variables: dict[tuple[int, int], int],
    original_edges: list[tuple[int, int]],
) -> tuple[AtMostEncoding | EqualsEncoding, list[tuple[int, int]]]:
    residual = [edge for edge in original_edges if edge != spec.fixed_edge]
    if len(residual) != 826:
        raise AssertionError("the residual edge list does not have length 826")
    deletion_literals = [-variables[edge] for edge in residual]
    if spec.mode == "atmost":
        encoding: AtMostEncoding | EqualsEncoding = encode_atmost(
            deletion_literals, spec.bound, PRIMARY_VARIABLES
        )
    elif spec.mode == "equals":
        encoding = encode_equals(deletion_literals, spec.bound, PRIMARY_VARIABLES)
    else:  # pragma: no cover - frozen table invariant
        raise AssertionError(f"unknown branch mode {spec.mode}")
    if len(encoding.clauses) != spec.counter_clauses:
        raise AssertionError(f"independent counter clause count mismatch for {spec.name}")
    if encoding.top_id != spec.maximum_variable:
        raise AssertionError(f"independent maximum variable mismatch for {spec.name}")
    if dimacs_clause_sha256(encoding.clauses) != spec.counter_sha256:
        raise AssertionError(f"independent counter digest mismatch for {spec.name}")
    return encoding, residual


def check_constructive_projection(
    spec: BranchSpec,
    encoding: AtMostEncoding | EqualsEncoding,
    variables: dict[tuple[int, int], int],
    residual: list[tuple[int, int]],
) -> None:
    if spec.mode == "atmost":
        if not isinstance(encoding, AtMostEncoding):
            raise AssertionError("at-most branch received an equality schema")
        satisfying = primary_assignment(variables, residual, spec.bound)
        violating = primary_assignment(variables, residual, spec.bound + 1)
        if construct_atmost_extension(encoding, satisfying) is None:
            raise AssertionError("at-most boundary assignment did not extend")
        if construct_atmost_extension(encoding, violating) is not None:
            raise AssertionError("at-most violating assignment unexpectedly extended")
    else:
        if not isinstance(encoding, EqualsEncoding):
            raise AssertionError("equality branch received an at-most schema")
        for count in (spec.bound - 1, spec.bound, spec.bound + 1):
            values = primary_assignment(variables, residual, count)
            extends = construct_equals_extension(encoding, values) is not None
            if extends != (count == spec.bound):
                raise AssertionError("equality boundary projection check failed")


def audit_actual_cnf(
    directory: Path,
    spec: BranchSpec,
    encoding: AtMostEncoding | EqualsEncoding,
    variables: dict[tuple[int, int], int],
) -> int:
    path = directory / spec.name
    header, stream = clause_stream(path)
    if header != (spec.maximum_variable, spec.total_clauses):
        raise AssertionError(f"unexpected DIMACS header for {spec.name}")
    for a, b, c in itertools.combinations(range(100), 3):
        expected = [-variables[(a, b)], -variables[(a, c)], -variables[(b, c)]]
        if next(stream) != expected:
            raise AssertionError(f"triangle prefix mismatch in {spec.name}")
    for expected in encoding.clauses:
        if next(stream) != expected:
            raise AssertionError(f"independent sequential block mismatch in {spec.name}")
    if next(stream) != [-variables[spec.fixed_edge]]:
        raise AssertionError(f"fixed branch unit mismatch in {spec.name}")
    tail = sum(1 for _ in stream)
    expected_tail = spec.total_clauses - TRIANGLE_CLAUSES - spec.counter_clauses - 1
    if tail != expected_tail:
        raise AssertionError(f"post-counter clause accounting mismatch in {spec.name}")
    return tail


def audit(directory: Path, schema_only: bool) -> dict:
    seed = directory / "certificates" / "r3_18_n100_nearmiss.txt"
    if sha256(seed) != SEED_SHA256:
        raise AssertionError("frozen seed hash mismatch")
    matrix = read_matrix(seed)
    pairs = list(itertools.combinations(range(100), 2))
    variables = {edge: index + 1 for index, edge in enumerate(pairs)}
    original_edges = [edge for edge in pairs if matrix[edge[0]][edge[1]]]
    if len(original_edges) != 827:
        raise AssertionError("frozen seed edge count mismatch")

    checked = []
    for spec in BRANCHES:
        encoding, residual = build_schema(spec, variables, original_edges)
        check_constructive_projection(spec, encoding, variables, residual)
        hitting_clauses = None
        if not schema_only:
            hitting_clauses = audit_actual_cnf(directory, spec, encoding, variables)
        checked.append(
            {
                "artifact": spec.name,
                "mode": spec.mode,
                "bound": spec.bound,
                "residual_literals": len(residual),
                "counter_clauses": len(encoding.clauses),
                "maximum_variable": encoding.top_id,
                "counter_sha256": spec.counter_sha256,
                "actual_dimacs_block_compared": not schema_only,
                "post_counter_hitting_clauses": hitting_clauses,
            }
        )
    return {
        "schema": "ramsey-r3-18-independent-seqcounter-audit-v1",
        "status": "INDEPENDENT_SEQCOUNTER_SCHEMA_VERIFIED",
        "pysat_cardenc_imported": False,
        "seed_sha256": SEED_SHA256,
        "canonical_pair_order": "lexicographic",
        "canonical_residual_edge_order": "lexicographic seed-edge subsequence",
        "branches": checked,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--artifact-dir", type=Path, default=Path(__file__).resolve().parent
    )
    parser.add_argument(
        "--schema-only",
        action="store_true",
        help=(
            "verify the independent large-instance schemas and frozen digests "
            "without release CNFs"
        ),
    )
    args = parser.parse_args()
    result = audit(args.artifact_dir.resolve(), args.schema_only)
    print(json.dumps(result, indent=2, sort_keys=True))
    print("INDEPENDENT_SEQCOUNTER_SCHEMA_VERIFIED")


if __name__ == "__main__":
    main()
