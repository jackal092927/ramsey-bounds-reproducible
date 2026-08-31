#!/usr/bin/env python3
"""Independent, PySAT-free checker for the deletion-covering projection ledger.

The checker intentionally does not import the generator.  It reparses the
frozen matrix, uses a high-label-first independent-set enumeration, rebuilds
the canonical sequential counter with a second implementation, and streams
both formula-body and complete-DIMACS SHA-256 values.  It also enforces the
endpoint rule: timeout output and a deleted partial proof imply UNKNOWN and
cannot justify an exact-seven call.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import itertools
import json
import os
import stat
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence


Edge = tuple[int, int]

LEDGER_SCHEMA = (
    "ramsey-r3-18-n100-branch1-deletion-covering-projection-ledger-v1"
)
ORDER = 100
FIXED_EDGE: Edge = (97, 99)
EXPECTED_SEED_SHA256 = (
    "e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e"
)
EXPECTED_FIXED_COUNT = 235_504
EXPECTED_FIXED_SHA256 = (
    "1e9f89f40cd97a5f3b6fa93bb3c4835d45cadca8362e9d3150e90d4f385f6d8c"
)
EXPECTED_RESIDUAL_SHA256 = (
    "071fe425f750b0e3021b89573a929a15b98ef6449aac2c60c3c1d014eb7df8cd"
)
EXPECTED_EXACT6_CNF_SHA256 = (
    "8611eaab2f01062948ae00e6ea91d265a439a0dcec3e2750f3df8deda5826c0e"
)
FORCED_RETAINED: tuple[Edge, ...] = (
    (11, 62), (18, 61), (18, 64), (18, 69)
)
PROFILES = {"exact-six": (5, False), "exact-seven": (6, True)}


class AuditError(ValueError):
    """A fail-closed ledger or reconstruction error."""


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def canonical_sha256(payload: Any) -> str:
    return sha256_bytes(
        json.dumps(
            payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
        ).encode("ascii")
    )


def mask_digest(masks: Iterable[int]) -> str:
    digest = hashlib.sha256()
    for mask in masks:
        digest.update(f"{mask:016x}\n".encode("ascii"))
    return digest.hexdigest()


def edge_digest(edges: Iterable[Edge], label: str) -> str:
    digest = hashlib.sha256()
    digest.update((label + "\n").encode("ascii"))
    for u, v in edges:
        digest.update(f"{u},{v}\n".encode("ascii"))
    return digest.hexdigest()


def strict_bytes(path: Path, label: str, expected_sha256: str | None = None) -> bytes:
    try:
        metadata = os.lstat(path)
    except OSError as error:
        raise AuditError(f"{label} cannot be inspected") from error
    if not stat.S_ISREG(metadata.st_mode):
        raise AuditError(f"{label} must be a non-symlink regular file")
    raw = path.read_bytes()
    if expected_sha256 is not None and sha256_bytes(raw) != expected_sha256:
        raise AuditError(f"{label} SHA-256 mismatch")
    return raw


def strict_json(path: Path, label: str) -> dict[str, Any]:
    raw = strict_bytes(path, label)

    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise AuditError(f"{label} contains duplicate key {key!r}")
            result[key] = value
        return result

    try:
        payload = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=reject_duplicates,
            parse_constant=lambda value: (_ for _ in ()).throw(
                AuditError(f"{label} contains non-finite {value}")
            ),
        )
    except (UnicodeError, json.JSONDecodeError) as error:
        raise AuditError(f"{label} is not strict UTF-8 JSON") from error
    if not isinstance(payload, dict):
        raise AuditError(f"{label} must be a JSON object")
    return payload


def read_seed(path: Path) -> list[int]:
    raw = strict_bytes(path, "seed", EXPECTED_SEED_SHA256)
    if not raw.endswith(b"\n") or b"\r" in raw:
        raise AuditError("seed line termination mismatch")
    try:
        lines = raw.decode("ascii").splitlines()
    except UnicodeError as error:
        raise AuditError("seed is not ASCII") from error
    if len(lines) != ORDER:
        raise AuditError("seed row count mismatch")
    rows = [0] * ORDER
    matrix: list[list[int]] = []
    for line in lines:
        fields = line.split()
        if len(fields) != ORDER or any(x not in {"0", "1"} for x in fields):
            raise AuditError("seed matrix syntax mismatch")
        matrix.append([int(x) for x in fields])
    for u in range(ORDER):
        if matrix[u][u]:
            raise AuditError("seed diagonal mismatch")
        for v in range(u + 1, ORDER):
            if matrix[u][v] != matrix[v][u]:
                raise AuditError("seed symmetry mismatch")
            if matrix[u][v]:
                rows[u] |= 1 << v
                rows[v] |= 1 << u
    if sum(row.bit_count() for row in rows) // 2 != 827:
        raise AuditError("seed edge count mismatch")
    return rows


def edge_set(rows: Sequence[int]) -> list[Edge]:
    return [
        (u, v)
        for u in range(len(rows))
        for v in range(u + 1, len(rows))
        if rows[u] >> v & 1
    ]


def mask_vertices(mask: int) -> list[int]:
    return [v for v in range(mask.bit_length()) if mask >> v & 1]


def reverse_independent_masks(rows: Sequence[int], candidates: int, size: int) -> list[int]:
    """Independent enumeration with the opposite branching order from generator."""

    result: list[int] = []

    def visit(pool: int, selected: int, needed: int) -> None:
        if needed == 0:
            result.append(selected)
            return
        if pool.bit_count() < needed:
            return
        remaining = pool
        while remaining.bit_count() >= needed:
            vertex = remaining.bit_length() - 1
            bit = 1 << vertex
            remaining ^= bit
            visit(remaining & ~rows[vertex], selected | bit, needed - 1)

    visit(candidates, 0, size)
    result.sort()
    if len(result) != len(set(result)):
        raise AuditError("reverse enumerator produced duplicate masks")
    return result


def allocate_counter_variable(
    table: dict[tuple[int, int], int], coordinate: tuple[int, int], state: list[int]
) -> int:
    if coordinate not in table:
        state[0] += 1
        table[coordinate] = state[0]
    return table[coordinate]


def independent_atmost(
    literals: Sequence[int], bound: int, top: int
) -> tuple[list[list[int]], int]:
    """Second literal-by-literal implementation of the frozen Sinz schema."""

    normalized = tuple(int(x) for x in literals)
    if bound < 0 or any(x == 0 for x in normalized):
        raise AuditError("invalid counter request")
    if len({abs(x) for x in normalized}) != len(normalized):
        raise AuditError("counter variables are not distinct")
    n = len(normalized)
    state = [max([top, *(abs(x) for x in normalized)])]
    clauses: list[list[int]] = []
    if not normalized or bound >= n:
        return clauses, state[0]
    if bound == 0:
        return [[-x] for x in normalized], state[0]
    if bound == n - 1:
        return [[-x for x in normalized]], state[0]
    table: dict[tuple[int, int], int] = {}
    width = n - bound
    for offset in range(width):
        first = allocate_counter_variable(table, (0, offset), state)
        clauses.append([-normalized[offset], first])
        for level in range(bound - 1):
            current = allocate_counter_variable(table, (level, offset), state)
            if offset + 1 < width:
                clauses.append(
                    [-current, allocate_counter_variable(table, (level, offset + 1), state)]
                )
            following = allocate_counter_variable(table, (level + 1, offset), state)
            clauses.append([-normalized[offset + level + 1], -current, following])
        last = allocate_counter_variable(table, (bound - 1, offset), state)
        if offset + 1 < width:
            clauses.append(
                [-last, allocate_counter_variable(table, (bound - 1, offset + 1), state)]
            )
        clauses.append([-normalized[offset + bound], -last])
    return clauses, state[0]


def independent_equals(
    literals: Sequence[int], bound: int, top: int
) -> tuple[list[list[int]], int]:
    lower, middle = independent_atmost([-x for x in literals], len(literals) - bound, top)
    upper, final = independent_atmost(literals, bound, middle)
    return [*lower, *upper], final


def reconstruction(seed_rows: Sequence[int]) -> dict[str, Any]:
    base_edges = edge_set(seed_rows)
    base_edges.remove(FIXED_EDGE)
    base_rows = [0] * ORDER
    for u, v in base_edges:
        base_rows[u] |= 1 << v
        base_rows[v] |= 1 << u
    additions = [
        (u, v)
        for u in range(ORDER)
        for v in range(u + 1, ORDER)
        if not (seed_rows[u] >> v & 1)
    ]
    all_vertices = (1 << ORDER) - 1
    candidates = all_vertices & ~(
        seed_rows[97] | seed_rows[99] | (1 << 97) | (1 << 99)
    )
    residual = reverse_independent_masks(seed_rows, candidates, 16)
    fixed = [mask | (1 << 97) | (1 << 99) for mask in residual]
    if (
        candidates.bit_count() != 65
        or len(fixed) != EXPECTED_FIXED_COUNT
        or mask_digest(residual) != EXPECTED_RESIDUAL_SHA256
        or mask_digest(fixed) != EXPECTED_FIXED_SHA256
    ):
        raise AuditError("independent fixed-base family mismatch")
    dvars = {edge: i + 1 for i, edge in enumerate(base_edges)}
    gvars = {edge: len(dvars) + i + 1 for i, edge in enumerate(additions)}
    return {
        "base_edges": base_edges,
        "base_rows": base_rows,
        "additions": additions,
        "fixed": fixed,
        "dvars": dvars,
        "gvars": gvars,
        "candidate_vertices": mask_vertices(candidates),
        "residual_sha256": mask_digest(residual),
    }


def wedge_requirements(data: dict[str, Any], edge: Edge) -> list[tuple[Edge, Edge]]:
    u, v = edge
    common = data["base_rows"][u] & data["base_rows"][v]
    result: list[tuple[Edge, Edge]] = []
    while common:
        bit = common & -common
        common ^= bit
        w = bit.bit_length() - 1
        result.append((tuple(sorted((u, w))), tuple(sorted((v, w)))))
    return result


def independent_formula(
    data: dict[str, Any], profile: str
) -> tuple[dict[str, Any], str]:
    residual, use_singletons = PROFILES[profile]
    dvars: dict[Edge, int] = data["dvars"]
    gvars: dict[Edge, int] = data["gvars"]
    counter, maximum = independent_equals(
        list(dvars.values()), residual, len(dvars) + len(gvars)
    )
    counts: Counter[str] = Counter()
    literal_counts: Counter[str] = Counter()
    body = hashlib.sha256()
    complete = hashlib.sha256()
    expected_clauses = len(counter) + 1 + 12_832 + EXPECTED_FIXED_COUNT + (4 if use_singletons else 0)
    complete.update(f"p cnf {maximum} {expected_clauses}\n".encode("ascii"))

    def accept(name: str, clause: list[int]) -> None:
        raw = (" ".join(map(str, clause)) + " 0\n").encode("ascii")
        body.update(raw)
        complete.update(raw)
        counts[name] += 1
        literal_counts[name] += len(clause)

    for clause in counter:
        accept("exact_residual_counter", clause)
    accept("vertex_98_degree_hit", [dvars[e] for e in data["base_edges"] if 98 in e])
    if use_singletons:
        for edge in FORCED_RETAINED:
            accept("singleton_deletion_exclusion", [-dvars[edge]])
    for edge in data["additions"]:
        for first, second in wedge_requirements(data, edge):
            accept("local_addition_eligibility", [-gvars[edge], dvars[first], dvars[second]])
    for mask in data["fixed"]:
        clause = [
            gvars[edge]
            for edge in itertools.combinations(mask_vertices(mask), 2)
            if edge in gvars
        ]
        if len(clause) != 152:
            raise AuditError("fixed-cover clause length mismatch")
        accept("fixed_base_I18_cover", clause)
    if sum(counts.values()) != expected_clauses:
        raise AuditError("independent clause count mismatch")
    record = {
        "profile": profile,
        "residual_deletions": residual,
        "singleton_exclusions_installed": use_singletons,
        "deletion_variables": len(dvars),
        "local_eligibility_variables": len(gvars),
        "auxiliary_variables": maximum - len(dvars) - len(gvars),
        "maximum_variable": maximum,
        "clauses": sum(counts.values()),
        "literals": sum(literal_counts.values()),
        "clause_count_by_family": dict(sorted(counts.items())),
        "literal_count_by_family": dict(sorted(literal_counts.items())),
        "ordered_clause_body_sha256": body.hexdigest(),
        "deletion_variable_order_sha256": edge_digest(data["base_edges"], "d"),
        "eligibility_variable_order_sha256": edge_digest(data["additions"], "g"),
    }
    return record, complete.hexdigest()


def audit(seed_path: Path, ledger_path: Path) -> dict[str, Any]:
    ledger = strict_json(ledger_path, "tracked ledger")
    if ledger.get("schema") != LEDGER_SCHEMA:
        raise AuditError("ledger schema mismatch")
    digest_basis = copy.deepcopy(ledger)
    recorded_digest = digest_basis.pop("record_sha256", None)
    if recorded_digest != canonical_sha256(digest_basis):
        raise AuditError("ledger canonical digest mismatch")
    seed_rows = read_seed(seed_path)
    data = reconstruction(seed_rows)
    exact6, exact6_cnf = independent_formula(data, "exact-six")
    exact7, exact7_cnf = independent_formula(data, "exact-seven")
    if ledger.get("formula_reconstruction", {}).get("exact_six") != exact6:
        raise AuditError("ledger exact-six formula record mismatch")
    if ledger.get("formula_reconstruction", {}).get("exact_seven") != exact7:
        raise AuditError("ledger exact-seven formula record mismatch")
    if exact6_cnf != EXPECTED_EXACT6_CNF_SHA256:
        raise AuditError("independent complete exact-six CNF digest mismatch")
    endpoint = ledger.get("exact_six_strength_gate")
    required_endpoint = {
        "solver_status": "UNKNOWN_HARD_WALL_LIMIT",
        "exitcode": 124,
        "status_lines": [],
        "wall_limit_seconds": 300,
        "exact_seven_was_run": False,
    }
    if not isinstance(endpoint, dict) or any(endpoint.get(k) != v for k, v in required_endpoint.items()):
        raise AuditError("endpoint status or stop rule mismatch")
    proof = endpoint.get("partial_proof")
    if not isinstance(proof, dict) or not (
        proof.get("complete") is False
        and proof.get("used_as_evidence") is False
        and proof.get("deleted_after_hashing") is True
        and proof.get("retained") is False
    ):
        raise AuditError("partial-proof quarantine boundary mismatch")
    decision = ledger.get("exact_seven_call_decision")
    if not isinstance(decision, dict) or not (
        decision.get("recommendation") == "DO_NOT_RUN"
        and decision.get("strength_gate_passed") is False
    ):
        raise AuditError("exact-seven call decision mismatch")
    return {
        "schema": "ramsey-r3-18-n100-branch1-deletion-projection-audit-v1",
        "status": "VERIFIED_UNKNOWN_ENDPOINT_AND_STOP_RULE",
        "fixed_base_I18_count": len(data["fixed"]),
        "fixed_base_I18_ordered_sha256": mask_digest(data["fixed"]),
        "exact_six_formula": exact6,
        "exact_six_complete_dimacs_sha256": exact6_cnf,
        "exact_seven_formula": exact7,
        "exact_seven_complete_dimacs_sha256_if_generated": exact7_cnf,
        "solver_endpoint": "UNKNOWN_HARD_WALL_LIMIT",
        "exact_seven_was_run": False,
        "claim_boundary": "No SAT, UNSAT, repair, or Ramsey-bound conclusion follows.",
    }


def main() -> None:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=Path, default=here / "certificates" / "r3_18_n100_nearmiss.txt")
    parser.add_argument("--ledger", type=Path, default=here / "r3_18_budget7_branch1_deletion_projection.json")
    args = parser.parse_args()
    print(json.dumps(audit(args.seed, args.ledger), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
