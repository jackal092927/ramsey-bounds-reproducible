#!/usr/bin/env python3
"""Audit the branch-1 free-addition saturation/maximality WLOG reduction.

Layer A is unconditional: saturate only original nonedges by triangle-safe
additions.  This preserves the exact deletion support in the one-sided metric.
Layer B uses the separately proof-checked radius lower bound to show that every
deleted seed edge is already triangle-blocked, so the Layer-A completion is a
maximal triangle-free graph.

The checker authenticates two complete SAT models, scans maximality violations,
checks deterministic completions, freezes a selector-CNF design, and records
claim boundaries.  It does not solve a new SAT instance.
"""

from __future__ import annotations

import argparse
import collections
import gzip
import hashlib
import itertools
import json
import os
import re
import stat
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence


Edge = tuple[int, int]

SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch1-maximality-wlog-v1"
STATUS = "VERIFIED_MAXIMALITY_WLOG_AND_MODEL_TELEMETRY"
ORDER = 100
PRIMARY_VARIABLES = 4_950
CURRENT_MAXIMUM_VARIABLE = 154_190
COMMON_CLAUSES = 718_452
APLUS_AUGMENTED_CLAUSES = 722_552
FIXED_EDGE: Edge = (97, 99)
SEED_TRIANGLE_EDGES: frozenset[Edge] = frozenset(
    {(97, 98), (97, 99), (98, 99)}
)
FORCED_EDGES: tuple[Edge, ...] = (
    (11, 62),
    (18, 61),
    (18, 64),
    (18, 69),
)

EXPECTED_SEED_SHA256 = (
    "e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e"
)
EXPECTED_BUDGET6_SHA256 = (
    "0abd30457c039c1c5fbba5890153c8a0c5d8558e196e7c0561410cefe37afa6a"
)
EXPECTED_BANK_SHA256 = (
    "91b5709248ff641a315f5a0389b4f3fde3d38514f3b1a8b31b6cad31224f250b"
)
EXPECTED_BANK_ORDERED_SHA256 = (
    "f10690b826b86eb03567a2ffaffb553801fae32af20cfe4337118bddf4e41afa"
)
EXPECTED_HISTORY_SHA256 = (
    "d5100bb5dce48da3ca8ab3810290ff553ebb9d6c87ff9df1f287700563f456b0"
)
EXPECTED_HISTORY_ORDERED_SHA256 = (
    "74b4b99c18e925a7a1bbb0e4a1636dad4bf8741ba67623c2164f3607a65172a8"
)
EXPECTED_APLUS_BATCH_SHA256 = (
    "835137c2df19bc851618761cc0af92400b3fa2677dd00c47101d1074c7406e8b"
)
EXPECTED_APLUS_ORDERED_SHA256 = (
    "a3cff8d8a4c77c6effb49c03e76065a17f754d0a7de727d229652276b6e8cda0"
)
EXPECTED_STRUCTURAL_LEDGER_SHA256 = (
    "25a4120d85b58ac8afc93d6047dee3acf917917647bca447c736cd064ec3ab4d"
)
EXPECTED_STRUCTURAL_RECORD_SHA256 = (
    "06fd57c94c5d21a1a9f9c50845ae0126ccbc5e9e5880fa54db752819afadf617"
)
EXPECTED_NO_ADD_EDGE_LIST_SHA256 = (
    "ff387efadc49230f2920e842972522683d31ddab7d496d8a0380f6a2704b4492"
)
EXPECTED_APLUS_GATE_SHA256 = (
    "d46115036cb6aba0411a50659f7bfca9efcd2dad739ba75d51f3b3286d3d36b3"
)
EXPECTED_AUGMENTED_CNF_SHA256 = (
    "6fbe630343afcf31a5affa9a70a315e3033bc077b24fc9a58d5084e63fdd389f"
)
EXPECTED_LEDGER_SHA256 = (
    "9eeda3123dd0d2095135e10cb2fff40c37c0a7d6592fcfa3c2403ac0fb12eed7"
)

COMMON_MODEL_DELETIONS: tuple[Edge, ...] = (
    (2, 97),
    (5, 97),
    (8, 97),
    (13, 37),
    (13, 97),
    (18, 98),
    (97, 99),
)
COMMON_MODEL_ADDITIONS: tuple[Edge, ...] = (
    (13, 61),
    (18, 97),
    (86, 97),
    (89, 97),
    (94, 97),
)
APLUS_MODEL_DELETIONS: tuple[Edge, ...] = (
    (1, 97),
    (16, 40),
    (16, 98),
    (17, 98),
    (35, 99),
    (44, 99),
    (97, 99),
)
APLUS_MODEL_ADDITIONS: tuple[Edge, ...] = (
    (16, 99),
    (17, 97),
    (51, 99),
)

_MASK_RE = re.compile(r"[0-9a-f]{25}\Z", flags=re.ASCII)


class AuditError(ValueError):
    """A fail-closed maximality audit failure."""


@dataclass(frozen=True)
class ModelProfile:
    label: str
    gzip_sha256: str
    gzip_bytes: int
    raw_sha256: str
    raw_bytes: int
    projection_sha256: str
    deletions: tuple[Edge, ...]
    additions: tuple[Edge, ...]


COMMON_PROFILE = ModelProfile(
    label="common model",
    gzip_sha256="9057db25b785640345e6f724cb1c79313642bb62ec2a19d9f310e25700de024d",
    gzip_bytes=391_052,
    raw_sha256="51e7832b69a18b29db817d1e180f1a071f771fbb50e358de4fb57a3810cd737e",
    raw_bytes=1_076_352,
    projection_sha256="b4a39182efdf9b1f0513f5e189698c9e7eba46b52df5faee37ccfef66289cfe1",
    deletions=COMMON_MODEL_DELETIONS,
    additions=COMMON_MODEL_ADDITIONS,
)
APLUS_PROFILE = ModelProfile(
    label="A+ model",
    gzip_sha256="19db55d05fe0b907ab77dc9645cf9356fd383bdbb83d91aa7690c6473965ffd3",
    gzip_bytes=384_949,
    raw_sha256="b7adbce4dada7dfeb41f94e36e34b25c57ee4a72a9223bf2c32bbbe4d8b561af",
    raw_bytes=1_066_055,
    projection_sha256="788f1b97ae516df3a435dce0a770e43fa5b52223564a2469fd7b7b960ae78e5f",
    deletions=APLUS_MODEL_DELETIONS,
    additions=APLUS_MODEL_ADDITIONS,
)


def _sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _canonical_sha256(payload: Any) -> str:
    return _sha256(
        json.dumps(
            payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
        ).encode("ascii")
    )


def _strict_regular(path: Path, expected_sha256: str, label: str) -> bytes:
    try:
        metadata = os.lstat(path)
    except OSError as error:
        raise AuditError(f"{label} cannot be inspected") from error
    if not stat.S_ISREG(metadata.st_mode):
        raise AuditError(f"{label} must be a non-symlink regular file")
    try:
        raw = path.read_bytes()
    except OSError as error:
        raise AuditError(f"{label} cannot be read") from error
    if _sha256(raw) != expected_sha256:
        raise AuditError(f"{label} SHA-256 mismatch")
    return raw


def _strict_json(raw: bytes, label: str) -> dict[str, Any]:
    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise AuditError(f"{label} contains a duplicate JSON key")
            result[key] = value
        return result

    try:
        payload = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=reject_duplicates,
            parse_constant=lambda value: (_ for _ in ()).throw(
                AuditError(f"{label} contains a non-finite number")
            ),
        )
    except (UnicodeError, json.JSONDecodeError) as error:
        raise AuditError(f"{label} is not strict UTF-8 JSON") from error
    if not isinstance(payload, dict):
        raise AuditError(f"{label} must be a JSON object")
    return payload


def _edge_lists(edges: Iterable[Edge]) -> list[list[int]]:
    return [list(edge) for edge in sorted(edges)]


def _histogram(values: Iterable[int]) -> dict[str, int]:
    return {
        str(key): value
        for key, value in sorted(collections.Counter(values).items())
    }


def edge_rows(edges: Iterable[Edge], order: int = ORDER) -> list[int]:
    rows = [0] * order
    for u, v in edges:
        if not 0 <= u < v < order:
            raise AuditError("edge lies outside graph order")
        rows[u] |= 1 << v
        rows[v] |= 1 << u
    return rows


def internal_edges(mask: int, rows: Sequence[int]) -> int:
    result = 0
    subset = mask
    while subset:
        bit = subset & -subset
        subset ^= bit
        vertex = bit.bit_length() - 1
        result += (
            rows[vertex] & mask & ~((1 << (vertex + 1)) - 1)
        ).bit_count()
    return result


def projection_sha256(edges: frozenset[Edge], order: int = ORDER) -> str:
    return _sha256(
        bytes(
            1 if (u, v) in edges else 0
            for u in range(order)
            for v in range(u + 1, order)
        )
    )


def triangle_count(rows: Sequence[int]) -> int:
    count = 0
    for u in range(len(rows)):
        later = rows[u] & ~((1 << (u + 1)) - 1)
        while later:
            bit = later & -later
            later ^= bit
            v = bit.bit_length() - 1
            count += (
                rows[u] & rows[v] & ~((1 << (v + 1)) - 1)
            ).bit_count()
    return count


def read_seed(path: Path) -> tuple[frozenset[Edge], dict[str, Any]]:
    raw = _strict_regular(path, EXPECTED_SEED_SHA256, "seed matrix")
    if not raw.endswith(b"\n") or b"\r" in raw:
        raise AuditError("seed matrix must be LF-terminated")
    try:
        lines = raw.decode("ascii").splitlines()
    except UnicodeError as error:
        raise AuditError("seed matrix is not ASCII") from error
    if len(lines) != ORDER:
        raise AuditError("seed matrix row count mismatch")
    matrix: list[list[int]] = []
    for line in lines:
        fields = line.split()
        if len(fields) != ORDER or any(field not in {"0", "1"} for field in fields):
            raise AuditError("seed matrix is not strict 100-by-100 binary data")
        matrix.append([int(field) for field in fields])
    for u in range(ORDER):
        if matrix[u][u]:
            raise AuditError("seed matrix diagonal is nonzero")
        for v in range(u + 1, ORDER):
            if matrix[u][v] != matrix[v][u]:
                raise AuditError("seed matrix is asymmetric")
    edges = frozenset(
        (u, v)
        for u in range(ORDER)
        for v in range(u + 1, ORDER)
        if matrix[u][v]
    )
    rows = edge_rows(edges)
    if (
        len(edges) != 827
        or not SEED_TRIANGLE_EDGES <= edges
        or triangle_count(rows) != 1
        or rows[97] & rows[98] != 1 << 99
    ):
        raise AuditError("seed edge family changed")
    return edges, {
        "basename": path.name,
        "bytes": len(raw),
        "sha256": EXPECTED_SEED_SHA256,
        "edges": len(edges),
        "unique_triangle_vertices": [97, 98, 99],
        "triangles": 1,
    }


def validate_budget6_summary(path: Path) -> dict[str, Any]:
    raw = _strict_regular(path, EXPECTED_BUDGET6_SHA256, "budget-six summary")
    payload = _strict_json(raw, "budget-six summary")
    if (
        payload.get("schema") != "ramsey-r3-18-n100-budget6-summary-v1"
        or payload.get("status")
        != "ALL_THREE_EXACT_BUDGET6_BRANCHES_UNSAT_PROOF_VERIFIED"
        or payload.get("input_sha256") != EXPECTED_SEED_SHA256
    ):
        raise AuditError("budget-six summary identity/status mismatch")
    scope = payload.get("scope")
    conclusion = payload.get("conclusion")
    branches = payload.get("branches")
    if (
        not isinstance(scope, dict)
        or scope.get("arbitrary_original_nonedge_additions_allowed") is not True
        or scope.get("maximum_input_edge_deletions_under_investigation") != 6
        or not isinstance(conclusion, dict)
        or conclusion.get("fixed_seed_budget_at_most_6_excluded") is not True
        or conclusion.get("fixed_seed_deletion_repair_radius_at_least_7") is not True
        or not isinstance(branches, list)
        or len(branches) != 3
    ):
        raise AuditError("budget-six summary lacks the required global scope")
    if [branch.get("fixed_deleted_edge") for branch in branches] != [
        [97, 98],
        [97, 99],
        [98, 99],
    ]:
        raise AuditError("budget-six branch cover changed")
    if any(
        branch.get("status") != "UNSAT_PROOF_VERIFIED"
        or branch.get("proof", {}).get("checker_status") != "VERIFIED"
        for branch in branches
    ):
        raise AuditError("budget-six branch proof status changed")
    return {
        "basename": path.name,
        "bytes": len(raw),
        "sha256": EXPECTED_BUDGET6_SHA256,
        "status": payload["status"],
        "at_most_six_excluded": True,
        "free_original_nonedge_additions": True,
    }


def _read_mask_array(
    path: Path,
    *,
    expected_file_sha256: str,
    expected_count: int,
    expected_ordered_sha256: str,
    label: str,
    bank_hash_width_16: bool = False,
) -> tuple[frozenset[int], dict[str, Any]]:
    raw = _strict_regular(path, expected_file_sha256, label)
    payload = _strict_json(raw, label)
    values = payload.get("masks")
    if not isinstance(values, list) or len(values) != expected_count:
        raise AuditError(f"{label} mask count mismatch")
    digest = hashlib.sha256()
    masks: list[int] = []
    for value in values:
        if not isinstance(value, str) or not _MASK_RE.fullmatch(value):
            raise AuditError(f"{label} contains a noncanonical mask")
        mask = int(value, 16)
        if mask.bit_count() != 18:
            raise AuditError(f"{label} contains a malformed 18-set")
        masks.append(mask)
        digest.update(
            (f"{mask:016x}\n" if bank_hash_width_16 else value + "\n").encode(
                "ascii"
            )
        )
    if len(masks) != len(set(masks)):
        raise AuditError(f"{label} contains duplicate masks")
    if not bank_hash_width_16 and masks != sorted(masks):
        raise AuditError(f"{label} masks are not sorted")
    if digest.hexdigest() != expected_ordered_sha256:
        raise AuditError(f"{label} ordered digest mismatch")
    return frozenset(masks), {
        "basename": path.name,
        "bytes": len(raw),
        "sha256": expected_file_sha256,
        "masks": len(masks),
        "ordered_masks_sha256": expected_ordered_sha256,
    }


def validate_structural_ledger(path: Path) -> dict[str, Any]:
    raw = _strict_regular(
        path, EXPECTED_STRUCTURAL_LEDGER_SHA256, "structural projection ledger"
    )
    payload = _strict_json(raw, "structural projection ledger")
    closure = payload.get("full_local_no_addition_closure")
    if (
        payload.get("status") != "VERIFIED_BOUNDED_STRUCTURAL_PROJECTION_FACTS"
        or payload.get("record_sha256") != EXPECTED_STRUCTURAL_RECORD_SHA256
        or not isinstance(closure, dict)
        or closure.get("no_addition_units") != 396
        or closure.get("edge_list_sha256") != EXPECTED_NO_ADD_EDGE_LIST_SHA256
    ):
        raise AuditError("structural projection ledger mismatch")
    return {
        "basename": path.name,
        "bytes": len(raw),
        "sha256": EXPECTED_STRUCTURAL_LEDGER_SHA256,
        "record_sha256": EXPECTED_STRUCTURAL_RECORD_SHA256,
        "no_addition_units": 396,
        "no_addition_edge_list_sha256": EXPECTED_NO_ADD_EDGE_LIST_SHA256,
    }


def _edges_from_descriptor(
    seed_edges: frozenset[Edge], profile: ModelProfile
) -> frozenset[Edge]:
    deletions = frozenset(profile.deletions)
    additions = frozenset(profile.additions)
    if (
        len(deletions) != 7
        or not deletions <= seed_edges
        or additions & seed_edges
        or FIXED_EDGE not in deletions
    ):
        raise AuditError(f"{profile.label} descriptor is malformed")
    edges = frozenset((seed_edges - deletions) | additions)
    if projection_sha256(edges) != profile.projection_sha256:
        raise AuditError(f"{profile.label} descriptor projection mismatch")
    return edges


def read_complete_model(path: Path, profile: ModelProfile) -> frozenset[Edge]:
    compressed = _strict_regular(path, profile.gzip_sha256, profile.label)
    if len(compressed) != profile.gzip_bytes:
        raise AuditError(f"{profile.label} compressed size mismatch")
    try:
        raw = gzip.decompress(compressed)
        text = raw.decode("ascii")
    except (OSError, EOFError, UnicodeError) as error:
        raise AuditError(f"{profile.label} is not complete ASCII gzip") from error
    if len(raw) != profile.raw_bytes or _sha256(raw) != profile.raw_sha256:
        raise AuditError(f"{profile.label} raw identity mismatch")
    if not raw.endswith(b"\n") or b"\r" in raw:
        raise AuditError(f"{profile.label} line endings are malformed")
    lines = text.splitlines()
    if not lines or lines[0] != "s SATISFIABLE":
        raise AuditError(f"{profile.label} lacks exact SAT status")
    tokens: list[int] = []
    for line in lines[1:]:
        if not line.startswith("v "):
            raise AuditError(f"{profile.label} contains a non-assignment line")
        try:
            tokens.extend(int(value) for value in line.split()[1:])
        except ValueError as error:
            raise AuditError(f"{profile.label} contains non-integer data") from error
    if not tokens or tokens[-1] != 0 or any(value == 0 for value in tokens[:-1]):
        raise AuditError(f"{profile.label} terminator is malformed")
    assignment: list[bool | None] = [None] * (CURRENT_MAXIMUM_VARIABLE + 1)
    for literal in tokens[:-1]:
        variable = abs(literal)
        if not 1 <= variable <= CURRENT_MAXIMUM_VARIABLE:
            raise AuditError(f"{profile.label} literal is out of range")
        if assignment[variable] is not None:
            raise AuditError(f"{profile.label} assigns a variable twice")
        assignment[variable] = literal > 0
    if any(value is None for value in assignment[1:]):
        raise AuditError(f"{profile.label} assignment is incomplete")
    pairs = list(itertools.combinations(range(ORDER), 2))
    edges = frozenset(
        edge for variable, edge in enumerate(pairs, 1) if assignment[variable]
    )
    if projection_sha256(edges) != profile.projection_sha256:
        raise AuditError(f"{profile.label} primary projection mismatch")
    return edges


def validate_aplus_gate(path: Path) -> dict[str, Any]:
    raw = _strict_regular(path, EXPECTED_APLUS_GATE_SHA256, "A+ gate record")
    payload = _strict_json(raw, "A+ gate record")
    solver = payload.get("solver")
    augmentation = payload.get("augmentation")
    if (
        payload.get("schema")
        != "ramsey-r3-18-n100-exact-budget7-branch1-cegar-gate-v1"
        or payload.get("status") != "SAT_MODEL_VERIFIED_I18_WITNESS_NO_LEARNING"
        or not isinstance(solver, dict)
        or solver.get("status") != payload.get("status")
        or solver.get("model", {}).get("sha256") != APLUS_PROFILE.gzip_sha256
        or solver.get("model_evaluation")
        != {"all_clauses_satisfied": True, "clauses_evaluated": 722_552}
        or not isinstance(augmentation, dict)
        or augmentation.get("augmented_cnf", {}).get("sha256")
        != EXPECTED_AUGMENTED_CNF_SHA256
        or payload.get("inputs", {}).get("common_model", {}).get("sha256")
        != COMMON_PROFILE.gzip_sha256
        or payload.get("inputs", {}).get("common_model_audit_status")
        != "VERIFIED_BRANCH1_COMMON_RELAXATION_SAT_MODEL"
    ):
        raise AuditError("A+ gate record identity/status mismatch")
    search = solver.get("I18_search")
    if (
        not isinstance(search, dict)
        or search.get("witness") != list(range(81, 98)) + [99]
        or search.get("mask_hex") != "bfffe00000000000000000000"
        or search.get("pairwise_independence_checked") is not True
    ):
        raise AuditError("A+ gate I18 witness changed")
    return {
        "basename": path.name,
        "bytes": len(raw),
        "sha256": EXPECTED_APLUS_GATE_SHA256,
        "status": payload["status"],
        "augmented_cnf_sha256": EXPECTED_AUGMENTED_CNF_SHA256,
        "clauses_evaluated": 722_552,
        "I18_witness_mask": search["mask_hex"],
        "common_model_audit_status": (
            "VERIFIED_BRANCH1_COMMON_RELAXATION_SAT_MODEL"
        ),
    }


def maximality_violations(
    edges: frozenset[Edge], order: int = ORDER
) -> tuple[Edge, ...]:
    rows = edge_rows(edges, order)
    return tuple(
        (u, v)
        for u in range(order)
        for v in range(u + 1, order)
        if (u, v) not in edges and not (rows[u] & rows[v])
    )


def saturate_original_nonedges(
    edges: frozenset[Edge], seed_edges: frozenset[Edge], order: int = ORDER
) -> tuple[frozenset[Edge], tuple[Edge, ...]]:
    result = set(edges)
    added: list[Edge] = []
    while True:
        violations = [
            edge
            for edge in maximality_violations(frozenset(result), order)
            if edge not in seed_edges
        ]
        if not violations:
            break
        edge = violations[0]
        result.add(edge)
        added.append(edge)
    return frozenset(result), tuple(added)


def selector_encoding_counts(pair_count: int, order: int = ORDER) -> dict[str, int]:
    witnesses_per_pair = order - 2
    auxiliaries = pair_count * witnesses_per_pair
    clauses = pair_count * (1 + 2 * witnesses_per_pair)
    return {
        "pairs": pair_count,
        "witnesses_per_pair": witnesses_per_pair,
        "auxiliary_variables": auxiliaries,
        "clauses": clauses,
        "long_clauses": pair_count,
        "binary_implication_clauses": 2 * auxiliaries,
        "maximum_variable_from_current_formula": CURRENT_MAXIMUM_VARIABLE + auxiliaries,
    }


def iter_selector_clauses(
    order: int,
    edge_variables: dict[Edge, int],
    scoped_pairs: Sequence[Edge],
    start_variable: int,
) -> Iterator[list[int]]:
    """Emit one-way Tseitin CNF for x_uv or some common-neighbour witness."""

    next_variable = start_variable
    for u, v in sorted(scoped_pairs):
        witnesses: list[tuple[int, int]] = []
        for w in range(order):
            if w in {u, v}:
                continue
            witness = next_variable
            next_variable += 1
            witnesses.append((w, witness))
        yield [edge_variables[(u, v)]] + [witness for _, witness in witnesses]
        for w, witness in witnesses:
            yield [-witness, edge_variables[tuple(sorted((u, w)))]]
            yield [-witness, edge_variables[tuple(sorted((v, w)))]]


def _minimum_local_deletions(
    edge: Edge,
    base_edges: frozenset[Edge],
) -> int | None:
    """Independent membership probe against the previously frozen 396 units."""

    rows = edge_rows(base_edges)
    degrees = [row.bit_count() for row in rows]
    forced = frozenset(FORCED_EDGES)
    u, v = edge
    quotas: dict[int, int] = {98: 1}
    quotas[u] = max(quotas.get(u, 0), degrees[u] + 1 - 17)
    quotas[v] = max(quotas.get(v, 0), degrees[v] + 1 - 17)
    quotas = {vertex: quota for vertex, quota in quotas.items() if quota > 0}
    choices: list[tuple[Edge, ...]] = []
    common = rows[u] & rows[v]
    while common:
        bit = common & -common
        common ^= bit
        w = bit.bit_length() - 1
        options = tuple(
            candidate
            for candidate in (tuple(sorted((u, w))), tuple(sorted((v, w))))
            if candidate not in forced
        )
        if not options:
            return None
        choices.append(options)
    best: int | None = None
    for raw in itertools.product(*choices):
        selected = set(raw)
        deficits = {
            vertex: max(0, quota - sum(vertex in chosen for chosen in selected))
            for vertex, quota in quotas.items()
        }
        required = sorted(deficits)
        internal = [
            (a, b)
            for a, b in itertools.combinations(required, 2)
            if (a, b) in base_edges
            and (a, b) not in forced
            and (a, b) not in selected
        ]
        for bits in range(1 << len(internal)):
            chosen_internal = {
                internal[index]
                for index in range(len(internal))
                if bits & (1 << index)
            }
            remaining = {
                vertex: max(
                    0,
                    deficits[vertex]
                    - sum(vertex in chosen for chosen in chosen_internal),
                )
                for vertex in required
            }
            available = True
            for vertex, deficit in remaining.items():
                outside = 0
                neighbours = rows[vertex]
                while neighbours:
                    bit = neighbours & -neighbours
                    neighbours ^= bit
                    other = bit.bit_length() - 1
                    candidate_edge = tuple(sorted((vertex, other)))
                    if (
                        other not in required
                        and candidate_edge not in forced
                        and candidate_edge not in selected
                        and candidate_edge not in chosen_internal
                    ):
                        outside += 1
                if outside < deficit:
                    available = False
                    break
            if not available:
                continue
            candidate = len(selected) + len(chosen_internal) + sum(remaining.values())
            best = candidate if best is None else min(best, candidate)
    return best


def _mask_membership(
    mask: int,
    bank: frozenset[int],
    history: frozenset[int],
    aplus: frozenset[int],
    base_rows: Sequence[int],
) -> dict[str, bool]:
    return {
        "universal_bank": mask in bank,
        "historical_union": mask in history,
        "Aplus_batch": mask in aplus,
        "fixed_base_family": internal_edges(mask, base_rows) == 0,
    }


def audit_model(
    profile: ModelProfile,
    seed_edges: frozenset[Edge],
    bank: frozenset[int],
    history: frozenset[int],
    aplus: frozenset[int],
    structural_base_rows: Sequence[int],
    model_path: Path | None,
) -> dict[str, Any]:
    edges = _edges_from_descriptor(seed_edges, profile)
    if model_path is not None and read_complete_model(model_path, profile) != edges:
        raise AuditError(f"{profile.label} artifact differs from descriptor")
    rows = edge_rows(edges)
    degrees = [row.bit_count() for row in rows]
    if triangle_count(rows) or max(degrees) > 17:
        raise AuditError(f"{profile.label} fails triangle/degree semantics")
    if len(seed_edges - edges) != 7 or FIXED_EDGE in edges:
        raise AuditError(f"{profile.label} fails exact-seven branch semantics")
    if not all(edge in edges for edge in FORCED_EDGES):
        raise AuditError(f"{profile.label} violates a retention unit")
    if any(internal_edges(mask, rows) == 0 for mask in bank):
        raise AuditError(f"{profile.label} violates the universal bank")
    if profile is APLUS_PROFILE and any(
        internal_edges(mask, rows) == 0 for mask in aplus
    ):
        raise AuditError("A+ model violates the installed A+ batch")

    violations = maximality_violations(edges)
    free_violations = tuple(edge for edge in violations if edge not in seed_edges)
    seed_violations = tuple(edge for edge in violations if edge in seed_edges)
    details = []
    for edge in violations:
        u, v = edge
        local_minimum = _minimum_local_deletions(edge, frozenset(seed_edges - {FIXED_EDGE}))
        details.append(
            {
                "edge": list(edge),
                "endpoint_degrees": [degrees[u], degrees[v]],
                "edge_type": (
                    "deleted_seed_edge" if edge in seed_edges else "original_nonedge"
                ),
                "fixed_branch_edge": edge == FIXED_EDGE,
                "fixed_base_common_neighbours": (
                    structural_base_rows[u] & structural_base_rows[v]
                ).bit_count(),
                "minimum_local_deletions_for_396_unit_test": local_minimum,
                "belongs_to_frozen_396_no_addition_units": (
                    local_minimum is None or local_minimum > 6
                ),
            }
        )

    completion, completion_additions = saturate_original_nonedges(edges, seed_edges)
    completion_rows = edge_rows(completion)
    completion_degrees = [row.bit_count() for row in completion_rows]
    if triangle_count(completion_rows):
        raise AuditError(f"{profile.label} saturation created a triangle")
    if seed_edges - completion != seed_edges - edges:
        raise AuditError(f"{profile.label} saturation changed deletion support")
    if any(internal_edges(mask, completion_rows) == 0 for mask in bank):
        raise AuditError(f"{profile.label} saturation broke a positive bank clause")
    if profile is APLUS_PROFILE and any(
        internal_edges(mask, completion_rows) == 0 for mask in aplus
    ):
        raise AuditError("A+ saturation broke an installed A+ clause")

    result: dict[str, Any] = {
        "artifact": {
            "gzip_sha256": profile.gzip_sha256,
            "gzip_bytes": profile.gzip_bytes,
            "raw_sha256": profile.raw_sha256,
            "raw_bytes": profile.raw_bytes,
            "maximum_variable": CURRENT_MAXIMUM_VARIABLE,
            "primary_projection_sha256": profile.projection_sha256,
            "canonical_checker_requires_full_artifact": True,
        },
        "edges": len(edges),
        "degree_distribution": _histogram(degrees),
        "maximum_degree": max(degrees),
        "triangle_count": 0,
        "deleted_seed_edges": _edge_lists(seed_edges - edges),
        "added_original_nonedges": _edge_lists(edges - seed_edges),
        "exact_one_sided_deletions": len(seed_edges - edges),
        "universal_bank_violations": 0,
        "Aplus_batch_violations": (
            0 if profile is APLUS_PROFILE else None
        ),
        "maximality_violations": len(violations),
        "layer_A_original_nonedge_violations": len(free_violations),
        "layer_B_deleted_seed_edge_violations": len(seed_violations),
        "exact_assignment_satisfies_layer_A": not free_violations,
        "exact_assignment_satisfies_full_maximality": not violations,
        "violation_details": details,
        "deterministic_layer_A_completion": {
            "added_edges": _edge_lists(completion_additions),
            "additions_count": len(completion_additions),
            "deletion_support_unchanged": True,
            "triangle_free": True,
            "layer_A_saturated": not any(
                edge not in seed_edges for edge in maximality_violations(completion)
            ),
            "full_maximal_triangle_free": not maximality_violations(completion),
            "degree_distribution": _histogram(completion_degrees),
            "maximum_degree": max(completion_degrees),
            "degree_cap_17_preserved_in_this_relaxation_model": (
                max(completion_degrees) <= 17
            ),
            "same_deletion_support_primary_graph_satisfies_relaxation_semantics": (
                max(completion_degrees) <= 17
            ),
            "existing_DIMACS_auxiliary_assignment_reused": False,
            "counter_auxiliary_reextension_materialized_here": False,
            "edge_projection_sha256": projection_sha256(completion),
        },
    }
    if profile is COMMON_PROFILE:
        u, v = violations[0]
        center, other = (u, v) if degrees[u] == 17 else (v, u)
        mask = rows[center] | (1 << other)
        result["domination_cut_from_degree_17_violation"] = {
            "center": center,
            "other": other,
            "mask_hex": f"{mask:025x}",
            "vertices": [vertex for vertex in range(ORDER) if mask & (1 << vertex)],
            "family_membership": _mask_membership(
                mask, bank, history, aplus, structural_base_rows
            ),
        }
    return result


def build_ledger(
    *,
    seed_path: Path,
    budget6_path: Path,
    bank_path: Path,
    history_path: Path,
    aplus_batch_path: Path,
    structural_ledger_path: Path,
    common_model_path: Path | None = None,
    aplus_model_path: Path | None = None,
    aplus_gate_path: Path | None = None,
) -> dict[str, Any]:
    seed_edges, seed_info = read_seed(seed_path)
    budget6_info = validate_budget6_summary(budget6_path)
    bank, bank_info = _read_mask_array(
        bank_path,
        expected_file_sha256=EXPECTED_BANK_SHA256,
        expected_count=251_771,
        expected_ordered_sha256=EXPECTED_BANK_ORDERED_SHA256,
        label="universal bank",
        bank_hash_width_16=True,
    )
    history, history_info = _read_mask_array(
        history_path,
        expected_file_sha256=EXPECTED_HISTORY_SHA256,
        expected_count=64_591,
        expected_ordered_sha256=EXPECTED_HISTORY_ORDERED_SHA256,
        label="historical union",
    )
    aplus, aplus_info = _read_mask_array(
        aplus_batch_path,
        expected_file_sha256=EXPECTED_APLUS_BATCH_SHA256,
        expected_count=4_096,
        expected_ordered_sha256=EXPECTED_APLUS_ORDERED_SHA256,
        label="A+ batch",
    )
    structural_info = validate_structural_ledger(structural_ledger_path)
    gate_info = (
        validate_aplus_gate(aplus_gate_path)
        if aplus_gate_path is not None
        else {
            "basename": "branch1_cegar_gate.json",
            "sha256": EXPECTED_APLUS_GATE_SHA256,
            "status": "SAT_MODEL_VERIFIED_I18_WITNESS_NO_LEARNING",
            "augmented_cnf_sha256": EXPECTED_AUGMENTED_CNF_SHA256,
            "clauses_evaluated": 722_552,
            "I18_witness_mask": "bfffe00000000000000000000",
            "common_model_audit_status": (
                "VERIFIED_BRANCH1_COMMON_RELAXATION_SAT_MODEL"
            ),
        }
    )
    base_rows = edge_rows(seed_edges - {FIXED_EDGE})
    common = audit_model(
        COMMON_PROFILE,
        seed_edges,
        bank,
        history,
        aplus,
        base_rows,
        common_model_path,
    )
    aplus_model = audit_model(
        APLUS_PROFILE,
        seed_edges,
        bank,
        history,
        aplus,
        base_rows,
        aplus_model_path,
    )
    gate_witness = int(gate_info["I18_witness_mask"], 16)
    completed_aplus_edges = _edges_from_descriptor(seed_edges, APLUS_PROFILE)
    completed_aplus_edges, _ = saturate_original_nonedges(
        completed_aplus_edges, seed_edges
    )
    completed_aplus_rows = edge_rows(completed_aplus_edges)
    if internal_edges(gate_witness, completed_aplus_rows):
        raise AuditError("A+ saturation destroyed the frozen I18 witness")
    gate_witness_membership = _mask_membership(
        gate_witness, bank, history, aplus, base_rows
    )
    if gate_witness_membership != {
        "universal_bank": False,
        "historical_union": True,
        "Aplus_batch": False,
        "fixed_base_family": True,
    }:
        raise AuditError("A+ I18 witness family relationship changed")

    original_nonedges = PRIMARY_VARIABLES - len(seed_edges)
    layer_a_counts = selector_encoding_counts(original_nonedges)
    full_counts = selector_encoding_counts(PRIMARY_VARIABLES)
    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "status": STATUS,
        "inputs": {
            "seed": seed_info,
            "budget6_dependency": budget6_info,
            "universal_bank": bank_info,
            "historical_union": history_info,
            "Aplus_batch": aplus_info,
            "structural_projection_ledger": structural_info,
            "Aplus_gate_record": gate_info,
        },
        "theorem": {
            "layer_A_original_nonedge_saturation": {
                "dependency_on_radius_lower_bound": False,
                "statement": (
                    "From any exact-seven target F, repeatedly add a missing "
                    "original nonedge of H whose endpoints have no common "
                    "neighbour.  Each step preserves triangle-freeness, cannot "
                    "increase alpha, and leaves E(H)\\E(F) unchanged.  The "
                    "finite process ends at a target with the same deletion "
                    "support in which every absent original nonedge is "
                    "triangle-blocked."
                ),
                "exact_deletion_support_preserved": True,
                "alpha_monotonicity": "adding edges cannot create an independent set",
                "degree_cap_reconciliation": (
                    "For a genuine triangle-free target with alpha<18, every "
                    "neighbourhood is independent and hence every degree is at "
                    "most 17.  Therefore a triangle-safe addition cannot create "
                    "degree 18 in a genuine target: that would expose an "
                    "independent 18-neighbourhood, contradicting alpha "
                    "monotonicity.  An incomplete finite-bank relaxation may "
                    "show this degree-18 completion, in which case the original "
                    "assignment is excluded by the WLOG constraint and the "
                    "completion is not claimed to remain a relaxation model."
                ),
                "not_a_necessary_property_of_every_raw_target": True,
                "WLOG_equisatisfiable": True,
            },
            "layer_B_full_maximal_triangle_free": {
                "dependency_budget6_summary_sha256": EXPECTED_BUDGET6_SHA256,
                "statement": (
                    "If a deleted seed edge were triangle-safe to add back, "
                    "the result would still be a target but would have exactly "
                    "six one-sided deletions, contradicting the authenticated "
                    "at-most-six exclusion.  This remains true for the fixed "
                    "branch edge: a safe add-back implies another edge of the "
                    "unique seed triangle is absent, so the six-deletion graph "
                    "is covered by the global three-branch proof.  Layer-A "
                    "additions cannot destroy an existing common neighbour."
                ),
                "full_maximality_equivalence": (
                    "An exact-seven target exists iff an exact-seven maximal "
                    "triangle-free target exists, conditional only on the "
                    "already checked rho_H>=7 dependency."
                ),
                "diameter_two_equivalence": (
                    "For this nontrivial graph order, maximal triangle-free is "
                    "equivalent to every nonedge having a common neighbour, "
                    "which implies connected diameter at most two."
                ),
                "WLOG_not_every_target_necessary": True,
                "fixed_branch_addback_covered_by_global_three_branch_certificate": True,
            },
        },
        "selector_CNF_design": {
            "semantics": (
                "For each scoped pair uv and each w other than u,v, introduce "
                "y_uv_w with implications y_uv_w -> x_uw and y_uv_w -> x_vw, "
                "plus x_uv OR the 98 witnesses.  Reverse Tseitin implications "
                "are unnecessary for existential equisatisfiability."
            ),
            "layer_A_original_nonedges": {
                **layer_a_counts,
                "clauses_with_common_formula": COMMON_CLAUSES
                + layer_a_counts["clauses"],
                "clauses_with_Aplus_augmented_formula": APLUS_AUGMENTED_CLAUSES
                + layer_a_counts["clauses"],
                "recommended_first_encoding": True,
                "rho_dependency": False,
            },
            "layer_B_all_pairs": {
                **full_counts,
                "clauses_with_common_formula": COMMON_CLAUSES
                + full_counts["clauses"],
                "clauses_with_Aplus_augmented_formula": APLUS_AUGMENTED_CLAUSES
                + full_counts["clauses"],
                "rho_dependency": True,
            },
            "one_lazy_pair": selector_encoding_counts(1),
            "frozen_396_unit_subset": {
                **selector_encoding_counts(396),
                "x_uv_is_already_false": True,
                "current_common_or_Aplus_model_directly_excluded": False,
            },
            "lazy_certificate_protocol": (
                "Discovery may instantiate only lexicographically scanned "
                "violating pairs.  Before proof production, freeze the sorted "
                "pair set, densely renumber witnesses after variable 154190, "
                "rebuild one deterministic CNF, and require checked DRAT/LRAT "
                "for UNSAT or complete model plus direct semantic maximality "
                "evaluation for SAT."
            ),
        },
        "models": {
            "common": common,
            "Aplus": {
                **aplus_model,
                "preserved_gate_I18_witness": {
                    "mask_hex": gate_info["I18_witness_mask"],
                    "vertices": list(range(81, 98)) + [99],
                    "still_independent_after_layer_A_completion": True,
                    "family_membership": gate_witness_membership,
                },
            },
        },
        "relationship_to_existing_lifts": {
            "domination": (
                "A degree-17 Layer-A violation immediately exposes the "
                "independent 18-set N(v) union {u}; the common-model pair "
                "(37,86) is exactly the previously frozen domination cut.  "
                "The three A+ violations have degree 16 at both endpoints and "
                "produce no domination cut."
            ),
            "frozen_396_no_addition_units": (
                "The 396 units say selected original nonedges can never be "
                "added; Layer-A saturation therefore requires a common-neighbour "
                "witness for each.  All four observed violation pairs have "
                "independent local deletion minimum two and lie outside the "
                "396-unit family."
            ),
            "ordinary_I18_CEGAR": (
                "Maximality is a WLOG normalization, not an alpha certificate.  "
                "A maximal finite-relaxation model may still contain an I18; "
                "indeed the completed A+ model retains the checked historical/"
                "fixed-base witness.  I18 separation and maximality separation "
                "remain complementary."
            ),
        },
        "bounded_go_no_go": {
            "recommended_pilot": (
                "Layer-A lazy selectors only; install every violation from one "
                "model in lexicographic order, at most one bounded 300-second "
                "solve after deterministic CNF/no-solver audit, and do not "
                "automatically launch a second round."
            ),
            "go": [
                "preprocessing or propagation derives consequences beyond merely setting the three A+ safe additions",
                "a checked SAT endpoint changes the deletion support or yields a genuinely new I18 witness",
                "a checked UNSAT proof is produced for a frozen WLOG-augmented relaxation",
            ],
            "no_go": [
                "the endpoint is the deterministic three-edge maximal completion of the current A+ model",
                "SAT retains only the already historical/fixed-base I18 witness",
                "UNKNOWN, timeout, malformed model, unchecked UNSAT, or proof growth beyond the fixed disk cap",
            ],
            "outcome_claims": {
                "SAT": "telemetry only unless a complete final graph independently verifies alpha<18",
                "UNSAT_checked": "excludes only the frozen branch relaxation covered by the WLOG dependency",
                "UNKNOWN": "no satisfiability or Ramsey claim and no learned scientific conclusion",
            },
        },
        "claim_boundary": {
            "every_raw_target_is_maximal": False,
            "layer_A_requires_rho_lower_bound": False,
            "layer_B_requires_rho_lower_bound": True,
            "maximality_implies_alpha_below_18": False,
            "current_Aplus_assignment_eliminated_by_layer_A": True,
            "current_Aplus_deletion_support_has_semantic_completion": True,
            "branch1_closed": False,
            "exact_seven_closed": False,
            "global_Ramsey_improvement": False,
        },
    }
    payload["record_sha256"] = _canonical_sha256(payload)
    return payload


def load_ledger(path: Path) -> dict[str, Any]:
    raw = _strict_regular(
        path, EXPECTED_LEDGER_SHA256, "tracked maximality ledger"
    )
    return _strict_json(raw, "tracked maximality ledger")


def main(argv: Sequence[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--matrix",
        type=Path,
        default=here / "certificates" / "r3_18_n100_nearmiss.txt",
    )
    parser.add_argument(
        "--budget6-summary",
        type=Path,
        default=here / "r3_18_budget6_summary.json",
    )
    parser.add_argument(
        "--universal-bank",
        type=Path,
        default=here / "r3_18_budget6_branch_0_universal_union.cuts.json",
    )
    parser.add_argument(
        "--history",
        type=Path,
        default=here / "r3_18_budget7_branch1_cegar_history_exclusion.json",
    )
    parser.add_argument(
        "--Aplus-batch",
        type=Path,
        default=here / "r3_18_budget7_branch1_cegar_Aplus_batch.json",
    )
    parser.add_argument(
        "--structural-ledger",
        type=Path,
        default=here / "r3_18_budget7_branch1_structural_projection.json",
    )
    parser.add_argument("--common-model", type=Path, required=True)
    parser.add_argument("--Aplus-model", type=Path, required=True)
    parser.add_argument("--Aplus-gate", type=Path, required=True)
    parser.add_argument(
        "--ledger",
        type=Path,
        default=here / "r3_18_budget7_branch1_maximality_wlog.json",
    )
    parser.add_argument("--print-json", action="store_true")
    args = parser.parse_args(argv)
    try:
        audit = build_ledger(
            seed_path=args.matrix,
            budget6_path=args.budget6_summary,
            bank_path=args.universal_bank,
            history_path=args.history,
            aplus_batch_path=args.Aplus_batch,
            structural_ledger_path=args.structural_ledger,
            common_model_path=args.common_model,
            aplus_model_path=args.Aplus_model,
            aplus_gate_path=args.Aplus_gate,
        )
        if load_ledger(args.ledger) != audit:
            raise AuditError("tracked maximality ledger differs from reconstruction")
    except (AuditError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if args.print_json:
        print(json.dumps(audit, indent=2, sort_keys=True))
    else:
        print(
            f"{STATUS}: record={audit['record_sha256']} "
            f"common_violations={audit['models']['common']['maximality_violations']} "
            f"Aplus_violations={audit['models']['Aplus']['maximality_violations']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
