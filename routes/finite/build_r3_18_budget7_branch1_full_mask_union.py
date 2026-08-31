#!/usr/bin/env python3
"""Audit and deterministically build the branch-1 full I18-mask union CNF.

This module is deliberately solver-free.  It independently authenticates the
frozen universal, historical, and A+ JSON mask files, reconstructs the
fixed-branch-base family from the pinned near-miss matrix, proves the exact
set-overlap ledger, and optionally emits or re-audits one plain DIMACS CNF.

The common CNF already contains the universal family.  The emitted extension
therefore consists of the four independently proved positive edge units and
the sorted masks in

    (universal union history union fixed-base union A+) minus universal.

Every mask is only a vertex-set encoding.  Its soundness does not depend on
the model or branch in which it was found: if ``alpha(G) < 18``, every
18-subset S satisfies ``OR_{uv in binom(S,2)} x_uv``.  Constructing this
finite relaxation proves neither SAT nor UNSAT of exact seven.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
import os
import stat
import sys
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence


SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch1-full-mask-union-audit-v1"
STATUS_PLAN = "FULL_MASK_UNION_AUDITED_CNF_NOT_EMITTED_SOLVER_NOT_RUN"
STATUS_CNF = "FULL_MASK_UNION_CNF_BYTE_AUDITED_SOLVER_NOT_RUN"

ORDER = 100
SET_SIZE = 18
FIXED_EDGE = (97, 99)
EXPECTED_INPUT_EDGES = 827
EXPECTED_TRIANGLES = ((97, 98, 99),)
EXPECTED_INPUT_SHA256 = (
    "e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e"
)
EXPECTED_SEED_VERIFICATION_SHA256 = (
    "9e5d98390608a4623d64d7ffaf91f9edd5da63f1e236e07ab7ba87fb8ffa5a39"
)

UNIVERSAL_FILE_SHA256 = (
    "91b5709248ff641a315f5a0389b4f3fde3d38514f3b1a8b31b6cad31224f250b"
)
UNIVERSAL_COUNT = 251_771
UNIVERSAL_ORDERED_SHA256 = (
    "f10690b826b86eb03567a2ffaffb553801fae32af20cfe4337118bddf4e41afa"
)
HISTORY_FILE_SHA256 = (
    "d5100bb5dce48da3ca8ab3810290ff553ebb9d6c87ff9df1f287700563f456b0"
)
HISTORY_COUNT = 64_591
HISTORY_RAW_COUNT = 113_448
HISTORY_ORDERED_SHA256 = (
    "74b4b99c18e925a7a1bbb0e4a1636dad4bf8741ba67623c2164f3607a65172a8"
)
FIXED_BASE_COUNT = 235_504
FIXED_BASE_ORDERED_SHA256 = (
    "1e9f89f40cd97a5f3b6fa93bb3c4835d45cadca8362e9d3150e90d4f385f6d8c"
)
APLUS_FILE_SHA256 = (
    "835137c2df19bc851618761cc0af92400b3fa2677dd00c47101d1074c7406e8b"
)
APLUS_COUNT = 4_096
APLUS_ORDERED_SHA256 = (
    "a3cff8d8a4c77c6effb49c03e76065a17f754d0a7de727d229652276b6e8cda0"
)
APLUS_ENDPOINT_AUDIT_SHA256 = (
    "b1f1732dfcdd1274c84c83aa7237d8385156c260b1f5e78f90b39a3e4f24ab82"
)
APLUS_ENDPOINT_WITNESS_MASK = int("bfffe00000000000000000000", 16)

EXPECTED_THREE_UNION_COUNT = 526_429
EXPECTED_THREE_UNION_SHA256 = (
    "f4220088cf6dfccc7b0e8b0aa7c2d1a2ef4a47f5ce31738506eefdd591613258"
)
EXPECTED_FULL_UNION_COUNT = 530_525
EXPECTED_FULL_UNION_SHA256 = (
    "f5c1c60877306900c1aa81bd3a7f357c3d16464ad329c676639a6f6bda9a682d"
)
EXPECTED_EXTRA_COUNT = 278_754
EXPECTED_EXTRA_SHA256 = (
    "2242d10f9ea3cefedef7a8c02be9a7df41db3cdb6580733e3fca9391db46d1d4"
)
EXPECTED_MEMBERSHIP_PATTERN = {
    "A+": 4_096,
    "fixed_base": 221_496,
    "history": 43_614,
    "history+fixed_base": 9_548,
    "universal": 236_528,
    "universal+fixed_base": 3_814,
    "universal+history": 10_783,
    "universal+history+fixed_base": 646,
}

CORE_SUMMARY_SHA256 = (
    "8ae4f0d9ea919c915ba642eb03ec3d418b4419a89781377509acbe925d89555a"
)
PROVED_POSITIVE_EDGES = ((11, 62), (18, 61), (18, 64), (18, 69))
PROVED_POSITIVE_UNITS = (1085, 1672, 1675, 1680)

COMMON_CNF_GZIP_SHA256 = (
    "39249ef8378de3f2ef412e514f6283cdaa032bc17fb25fc3448463e5566f5365"
)
COMMON_CNF_GZIP_BYTES = 18_919_093
COMMON_CNF_RAW_SHA256 = (
    "9602ef233f5fa95748ce4e7f997457d1bef47cd46453340bf5a44c2e163d3ec7"
)
COMMON_CNF_RAW_BYTES = 180_104_600
COMMON_VARIABLES = 154_190
COMMON_CLAUSES = 718_452
FINAL_CLAUSES = COMMON_CLAUSES + len(PROVED_POSITIVE_UNITS) + EXPECTED_EXTRA_COUNT

# Frozen by the first solver-free deterministic construction and enforced on
# every subsequent production emission and line-by-line audit.
FULL_CNF_BYTES = 390_604_816
FULL_CNF_SHA256 = (
    "4f7e8f5b724a657888c7814d2c25cac41c283c3db356fb8f1a15f4c7322c375d"
)


class AuditError(ValueError):
    """Fail-closed input, combinatorial, or byte-reconstruction failure."""


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def ordered_masks_sha256(masks: Iterable[int], width: int = 25) -> str:
    digest = hashlib.sha256()
    for mask in masks:
        digest.update(f"{mask:0{width}x}\n".encode("ascii"))
    return digest.hexdigest()


def read_regular_bytes(path: Path) -> bytes:
    """Read one stable final-component regular file without following links."""

    if path.is_symlink():
        raise AuditError(f"refusing symlink input: {path.name}")
    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError as error:
        raise AuditError(f"cannot safely open input: {path.name}") from error
    try:
        opened = os.fstat(descriptor)
        current = os.stat(path, follow_symlinks=False)
        if (
            not stat.S_ISREG(opened.st_mode)
            or not stat.S_ISREG(current.st_mode)
            or (opened.st_dev, opened.st_ino) != (current.st_dev, current.st_ino)
        ):
            raise AuditError(f"input is not one stable regular file: {path.name}")
        chunks: list[bytes] = []
        while True:
            block = os.read(descriptor, 1024 * 1024)
            if not block:
                break
            chunks.append(block)
        final = os.fstat(descriptor)
        if (opened.st_dev, opened.st_ino, opened.st_size) != (
            final.st_dev,
            final.st_ino,
            final.st_size,
        ):
            raise AuditError(f"input changed while being read: {path.name}")
        return b"".join(chunks)
    finally:
        os.close(descriptor)


def strict_json_bytes(raw: bytes, description: str) -> dict[str, Any]:
    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise AuditError(f"{description} contains duplicate key {key!r}")
            result[key] = value
        return result

    def reject_constant(value: str) -> None:
        raise AuditError(f"{description} contains non-finite number {value}")

    try:
        payload = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=reject_duplicates,
            parse_constant=reject_constant,
        )
    except AuditError:
        raise
    except (UnicodeError, json.JSONDecodeError) as error:
        raise AuditError(f"{description} is not strict UTF-8 JSON") from error
    if not isinstance(payload, dict):
        raise AuditError(f"{description} root is not an object")
    return payload


def artifact_identity(path: Path, raw: bytes) -> dict[str, Any]:
    return {
        "basename": path.name,
        "bytes": len(raw),
        "sha256": sha256_bytes(raw),
    }


def canonical_mask_array(
    values: Any,
    *,
    description: str,
    expected_count: int,
    require_sorted: bool,
) -> list[int]:
    if not isinstance(values, list) or len(values) != expected_count:
        raise AuditError(f"{description} mask count mismatch")
    masks: list[int] = []
    for index, value in enumerate(values):
        if (
            not isinstance(value, str)
            or len(value) != 25
            or any(character not in "0123456789abcdef" for character in value)
        ):
            raise AuditError(f"{description} mask {index} is not canonical hex")
        mask = int(value, 16)
        if mask >> ORDER or mask.bit_count() != SET_SIZE:
            raise AuditError(f"{description} mask {index} is not an I18 vertex set")
        masks.append(mask)
    if len(masks) != len(set(masks)):
        raise AuditError(f"{description} contains duplicate masks")
    if require_sorted and masks != sorted(masks):
        raise AuditError(f"{description} masks are not strictly increasing")
    return masks


def load_universal(path: Path) -> tuple[list[int], dict[str, Any]]:
    raw = read_regular_bytes(path)
    if sha256_bytes(raw) != UNIVERSAL_FILE_SHA256:
        raise AuditError("universal file SHA-256 mismatch")
    payload = strict_json_bytes(raw, "universal bank")
    if set(payload) != {
        "all_masks_are_18_sets",
        "fixed_deleted_edge",
        "masks",
        "masks_sha256",
        "schema",
    }:
        raise AuditError("universal bank fields are not exact")
    if payload.get("all_masks_are_18_sets") is not True:
        raise AuditError("universal bank does not assert I18 shape")
    masks = canonical_mask_array(
        payload.get("masks"),
        description="universal bank",
        expected_count=UNIVERSAL_COUNT,
        require_sorted=False,
    )
    digest = ordered_masks_sha256(masks, 16)
    if digest != UNIVERSAL_ORDERED_SHA256 or payload.get("masks_sha256") != digest:
        raise AuditError("universal ordered-mask digest mismatch")
    return masks, {
        **artifact_identity(path, raw),
        "masks": len(masks),
        "ordered_masks_sha256": digest,
        "ordered_digest_hex_width": 16,
    }


def load_history(path: Path) -> tuple[list[int], dict[str, Any]]:
    raw = read_regular_bytes(path)
    if sha256_bytes(raw) != HISTORY_FILE_SHA256:
        raise AuditError("history file SHA-256 mismatch")
    payload = strict_json_bytes(raw, "history union")
    if set(payload) != {
        "masks",
        "masks_count",
        "ordered_masks_sha256",
        "schema",
        "source_raw_count_sum",
        "sources",
        "union_duplicates_removed",
        "within_source_duplicates",
    }:
        raise AuditError("history union fields are not exact")
    if (
        payload.get("masks_count") != HISTORY_COUNT
        or payload.get("source_raw_count_sum") != HISTORY_RAW_COUNT
        or payload.get("within_source_duplicates") != 0
        or payload.get("union_duplicates_removed") != HISTORY_RAW_COUNT - HISTORY_COUNT
    ):
        raise AuditError("history union ledger mismatch")
    sources = payload.get("sources")
    if not isinstance(sources, list) or len(sources) != 18:
        raise AuditError("history source ledger count mismatch")
    seen_paths: set[str] = set()
    raw_sum = 0
    for source in sources:
        if not isinstance(source, dict) or set(source) != {
            "field",
            "file_sha256",
            "path",
            "raw_count",
        }:
            raise AuditError("history source fields are not exact")
        source_path = source.get("path")
        if (
            not isinstance(source_path, str)
            or not source_path
            or Path(source_path).is_absolute()
            or ".." in Path(source_path).parts
            or source_path in seen_paths
        ):
            raise AuditError("history source path is unsafe or duplicated")
        seen_paths.add(source_path)
        count = source.get("raw_count")
        if not isinstance(count, int) or isinstance(count, bool) or count <= 0:
            raise AuditError("history source raw count is invalid")
        raw_sum += count
    if raw_sum != HISTORY_RAW_COUNT:
        raise AuditError("history source raw counts do not sum")
    masks = canonical_mask_array(
        payload.get("masks"),
        description="history union",
        expected_count=HISTORY_COUNT,
        require_sorted=True,
    )
    digest = ordered_masks_sha256(masks)
    if digest != HISTORY_ORDERED_SHA256 or payload.get("ordered_masks_sha256") != digest:
        raise AuditError("history ordered-mask digest mismatch")
    return masks, {
        **artifact_identity(path, raw),
        "masks": len(masks),
        "ordered_masks_sha256": digest,
        "source_checkpoints": len(sources),
        "source_raw_masks": raw_sum,
        "union_duplicates_removed": HISTORY_RAW_COUNT - HISTORY_COUNT,
    }


def load_aplus(path: Path) -> tuple[list[int], dict[str, Any]]:
    raw = read_regular_bytes(path)
    if sha256_bytes(raw) != APLUS_FILE_SHA256:
        raise AuditError("A+ file SHA-256 mismatch")
    payload = strict_json_bytes(raw, "A+ batch")
    if set(payload) != {
        "enumeration",
        "exclusions",
        "masks",
        "masks_count",
        "ordered_masks_sha256",
        "schema",
    }:
        raise AuditError("A+ fields are not exact")
    if payload.get("enumeration") != "reverse-first" or payload.get("masks_count") != APLUS_COUNT:
        raise AuditError("A+ enumeration or count mismatch")
    expected_exclusions = {
        "base_universal_bank": {
            "masks": UNIVERSAL_COUNT,
            "ordered_masks_sha256": UNIVERSAL_ORDERED_SHA256,
        },
        "historical_union": {
            "masks": HISTORY_COUNT,
            "ordered_masks_sha256": HISTORY_ORDERED_SHA256,
        },
        "fixed_branch1_base_family": {
            "masks": FIXED_BASE_COUNT,
            "ordered_masks_sha256": FIXED_BASE_ORDERED_SHA256,
        },
    }
    if payload.get("exclusions") != expected_exclusions:
        raise AuditError("A+ exclusion identities mismatch")
    masks = canonical_mask_array(
        payload.get("masks"),
        description="A+ batch",
        expected_count=APLUS_COUNT,
        require_sorted=True,
    )
    digest = ordered_masks_sha256(masks)
    if digest != APLUS_ORDERED_SHA256 or payload.get("ordered_masks_sha256") != digest:
        raise AuditError("A+ ordered-mask digest mismatch")
    return masks, {
        **artifact_identity(path, raw),
        "masks": len(masks),
        "ordered_masks_sha256": digest,
        "distinct_role": (
            "new reverse-first batch; required to have zero overlap with all "
            "three pre-existing families"
        ),
    }


def read_seed_matrix(path: Path) -> tuple[list[int], dict[str, Any]]:
    raw = read_regular_bytes(path)
    if sha256_bytes(raw) != EXPECTED_INPUT_SHA256:
        raise AuditError("near-miss matrix SHA-256 mismatch")
    try:
        tokens = raw.decode("ascii").split()
    except UnicodeError as error:
        raise AuditError("near-miss matrix is not ASCII") from error
    if len(tokens) != ORDER * ORDER or any(token not in {"0", "1"} for token in tokens):
        raise AuditError("near-miss matrix is not a canonical 100x100 bit matrix")
    rows: list[int] = []
    for u in range(ORDER):
        row = 0
        for v, token in enumerate(tokens[u * ORDER : (u + 1) * ORDER]):
            if token == "1":
                row |= 1 << v
        rows.append(row)
    for u, row in enumerate(rows):
        if row & (1 << u):
            raise AuditError("near-miss matrix has a loop")
        for v in range(u):
            if bool(row & (1 << v)) != bool(rows[v] & (1 << u)):
                raise AuditError("near-miss matrix is asymmetric")
    edges = sum(row.bit_count() for row in rows) // 2
    triangles = tuple(
        (a, b, c)
        for a, b, c in itertools.combinations(range(ORDER), 3)
        if rows[a] & (1 << b) and rows[a] & (1 << c) and rows[b] & (1 << c)
    )
    if edges != EXPECTED_INPUT_EDGES or triangles != EXPECTED_TRIANGLES:
        raise AuditError("near-miss matrix edge or triangle identity mismatch")
    return rows, {**artifact_identity(path, raw), "vertices": ORDER, "edges": edges}


def validate_seed_verification(path: Path) -> dict[str, Any]:
    raw = read_regular_bytes(path)
    if sha256_bytes(raw) != EXPECTED_SEED_VERIFICATION_SHA256:
        raise AuditError("seed-verification file SHA-256 mismatch")
    payload = strict_json_bytes(raw, "seed verification")
    forbidden = payload.get("searches", {}).get("forbidden_independent_set", {})
    if (
        payload.get("sha256") != EXPECTED_INPUT_SHA256
        or payload.get("vertices") != ORDER
        or payload.get("edges") != EXPECTED_INPUT_EDGES
        or forbidden.get("target") != SET_SIZE
        or forbidden.get("exists") is not False
        or forbidden.get("witness") is not None
    ):
        raise AuditError("seed verification does not bind the no-I18 premise")
    return {
        **artifact_identity(path, raw),
        "forbidden_independent_set_target": SET_SIZE,
        "forbidden_independent_set_exists": False,
    }


def complement_rows(rows: Sequence[int]) -> list[int]:
    all_vertices = (1 << len(rows)) - 1
    return [all_vertices ^ row ^ (1 << vertex) for vertex, row in enumerate(rows)]


def enumerate_k_cliques(
    adjacency: Sequence[int], candidates: int, size: int
) -> tuple[list[int], int]:
    """Complete deterministic low-bit recursion, independent of graph_utils."""

    result: list[int] = []
    nodes = 0

    def visit(available: int, chosen: int, need: int) -> None:
        nonlocal nodes
        nodes += 1
        if need == 0:
            result.append(chosen)
            return
        if available.bit_count() < need:
            return
        while available:
            bit = available & -available
            available ^= bit
            vertex = bit.bit_length() - 1
            visit(available & adjacency[vertex], chosen | bit, need - 1)

    visit(candidates, 0, size)
    return result, nodes


def fixed_base_masks(rows: Sequence[int]) -> tuple[list[int], dict[str, Any]]:
    u, v = FIXED_EDGE
    if not rows[u] & (1 << v):
        raise AuditError("fixed branch edge is absent from the seed")
    all_vertices = (1 << ORDER) - 1
    candidates = all_vertices & ~(rows[u] | rows[v] | (1 << u) | (1 << v))
    residual, nodes = enumerate_k_cliques(
        complement_rows(rows), candidates, SET_SIZE - 2
    )
    endpoint_bits = (1 << u) | (1 << v)
    masks = sorted(mask | endpoint_bits for mask in residual)
    if len(masks) != len(set(masks)) or len(masks) != FIXED_BASE_COUNT:
        raise AuditError("fixed-base family count or uniqueness mismatch")
    digest = ordered_masks_sha256(masks)
    if digest != FIXED_BASE_ORDERED_SHA256:
        raise AuditError("fixed-base family ordered digest mismatch")
    base_rows = list(rows)
    base_rows[u] &= ~(1 << v)
    base_rows[v] &= ~(1 << u)
    for index, mask in enumerate(masks):
        if mask.bit_count() != SET_SIZE or mask >> ORDER or mask & endpoint_bits != endpoint_bits:
            raise AuditError(f"fixed-base mask {index} has invalid shape")
        remaining = mask
        while remaining:
            bit = remaining & -remaining
            remaining ^= bit
            vertex = bit.bit_length() - 1
            if base_rows[vertex] & remaining:
                raise AuditError(f"fixed-base mask {index} is not independent")
    return masks, {
        "masks": len(masks),
        "ordered_masks_sha256": digest,
        "enumeration": (
            "all independent 16-sets in the endpoints' common seed "
            "nonneighbourhood, then adjoin 97 and 99"
        ),
        "recursive_nodes": nodes,
        "all_masks_independent_after_deleting_fixed_edge": True,
        "exhaustiveness_premise": (
            "the pinned seed-verification record excludes an I18 before the "
            "fixed edge is deleted"
        ),
    }


def validate_core_summary(path: Path) -> dict[str, Any]:
    raw = read_regular_bytes(path)
    if sha256_bytes(raw) != CORE_SUMMARY_SHA256:
        raise AuditError("singleton proof-summary SHA-256 mismatch")
    payload = strict_json_bytes(raw, "singleton proof summary")
    if payload.get("status") != "FOUR_SINGLETON_NO_GOODS_PROOF_VERIFIED_EXACT_SEVEN_UNKNOWN":
        raise AuditError("singleton proof-summary status mismatch")
    records = payload.get("records")
    if not isinstance(records, list) or len(records) != len(PROVED_POSITIVE_UNITS):
        raise AuditError("singleton proof-summary record count mismatch")
    actual_units: list[int] = []
    for record in records:
        assumptions = record.get("assumption_units") if isinstance(record, dict) else None
        if (
            not isinstance(assumptions, list)
            or len(assumptions) != 1
            or not isinstance(assumptions[0], int)
            or record.get("proof_verified") is not True
        ):
            raise AuditError("singleton proof-summary record is not verified")
        actual_units.append(-assumptions[0])
    if tuple(actual_units) != PROVED_POSITIVE_UNITS:
        raise AuditError("singleton proof-summary units mismatch")
    variables = lexicographic_edge_variables()
    if tuple(variables[edge] for edge in PROVED_POSITIVE_EDGES) != PROVED_POSITIVE_UNITS:
        raise AuditError("singleton edge-to-variable mapping mismatch")
    return {
        **artifact_identity(path, raw),
        "proved_positive_edges": [list(edge) for edge in PROVED_POSITIVE_EDGES],
        "proved_positive_units": list(PROVED_POSITIVE_UNITS),
        "all_four_proof_verified": True,
    }


def validate_aplus_endpoint_audit(path: Path) -> dict[str, Any]:
    """Authenticate the prior A+ SAT endpoint used only for route comparison."""

    raw = read_regular_bytes(path)
    if sha256_bytes(raw) != APLUS_ENDPOINT_AUDIT_SHA256:
        raise AuditError("A+ endpoint-audit SHA-256 mismatch")
    payload = strict_json_bytes(raw, "A+ endpoint audit")
    direct = payload.get("direct_graph_audit")
    evaluation = payload.get("full_cnf_evaluation")
    endpoint = payload.get("endpoint")
    if (
        payload.get("status") != "F24_SAT_REAUDITED_I18_WITNESS_NO_LOWER_BOUND"
        or payload.get("sat_claim_accepted") is not True
        or payload.get("proof_verified") is not False
        or payload.get("solver_executed_by_auditor") is not False
        or not isinstance(direct, dict)
        or direct.get("independent_set_exists") is not True
        or direct.get("pairwise_witness_check") is not True
        or not isinstance(evaluation, dict)
        or evaluation.get("all_clauses_satisfied") is not True
        or evaluation.get("clauses_evaluated") != 722_552
        or not isinstance(endpoint, dict)
        or endpoint.get("historical_status")
        != "SAT_MODEL_VERIFIED_I18_WITNESS_NO_LEARNING"
    ):
        raise AuditError("A+ endpoint audit does not bind the checked SAT witness")
    witness = direct.get("independent_set_witness")
    if (
        not isinstance(witness, list)
        or len(witness) != SET_SIZE
        or any(
            not isinstance(vertex, int)
            or isinstance(vertex, bool)
            or not 0 <= vertex < ORDER
            for vertex in witness
        )
        or len(set(witness)) != SET_SIZE
    ):
        raise AuditError("A+ endpoint independent-set witness is malformed")
    mask = sum(1 << vertex for vertex in witness)
    if mask != APLUS_ENDPOINT_WITNESS_MASK:
        raise AuditError("A+ endpoint witness mask mismatch")
    return {
        **artifact_identity(path, raw),
        "SAT_model_full_CNF_evaluation_passed": True,
        "independent_18_mask": f"{mask:025x}",
        "auditor_executed_solver": False,
    }


def membership_pattern(
    universal: set[int], history: set[int], fixed: set[int], aplus: set[int]
) -> dict[str, int]:
    result: Counter[str] = Counter()
    for mask in universal | history | fixed | aplus:
        labels: list[str] = []
        if mask in universal:
            labels.append("universal")
        if mask in history:
            labels.append("history")
        if mask in fixed:
            labels.append("fixed_base")
        if mask in aplus:
            labels.append("A+")
        result["+".join(labels)] += 1
    return dict(sorted(result.items()))


def union_ledger(
    universal: Sequence[int],
    history: Sequence[int],
    fixed: Sequence[int],
    aplus: Sequence[int],
) -> tuple[list[int], dict[str, Any]]:
    u, h, f, a = map(set, (universal, history, fixed, aplus))
    pairwise = {
        "universal_history": len(u & h),
        "universal_fixed_base": len(u & f),
        "history_fixed_base": len(h & f),
        "universal_A+": len(u & a),
        "history_A+": len(h & a),
        "fixed_base_A+": len(f & a),
    }
    if pairwise != {
        "universal_history": 11_429,
        "universal_fixed_base": 4_460,
        "history_fixed_base": 10_194,
        "universal_A+": 0,
        "history_A+": 0,
        "fixed_base_A+": 0,
    }:
        raise AuditError("pairwise overlap ledger mismatch")
    triple = len(u & h & f)
    if triple != 646:
        raise AuditError("three-family overlap mismatch")
    pattern = membership_pattern(u, h, f, a)
    if pattern != EXPECTED_MEMBERSHIP_PATTERN:
        raise AuditError("exclusive membership-pattern ledger mismatch")
    union_three = sorted(u | h | f)
    union_full = sorted(set(union_three) | a)
    extra = sorted(set(union_full) - u)
    if (
        len(union_three) != EXPECTED_THREE_UNION_COUNT
        or ordered_masks_sha256(union_three) != EXPECTED_THREE_UNION_SHA256
        or len(union_full) != EXPECTED_FULL_UNION_COUNT
        or ordered_masks_sha256(union_full) != EXPECTED_FULL_UNION_SHA256
        or len(extra) != EXPECTED_EXTRA_COUNT
        or ordered_masks_sha256(extra) != EXPECTED_EXTRA_SHA256
    ):
        raise AuditError("deduplicated union identity mismatch")
    return extra, {
        "pairwise_intersections": pairwise,
        "universal_history_fixed_base_intersection": triple,
        "exclusive_membership_counts": pattern,
        "raw_family_memberships_three_families": len(u) + len(h) + len(f),
        "duplicates_removed_three_families": len(u) + len(h) + len(f) - len(union_three),
        "three_family_union": {
            "masks": len(union_three),
            "ordered_masks_sha256": ordered_masks_sha256(union_three),
        },
        "A+": {
            "masks": len(a),
            "zero_overlap_with_three_family_union": not bool(a & set(union_three)),
        },
        "full_union": {
            "masks": len(union_full),
            "ordered_masks_sha256": ordered_masks_sha256(union_full),
        },
        "extra_beyond_common_universal_bank": {
            "masks": len(extra),
            "ordered_masks_sha256": ordered_masks_sha256(extra),
        },
    }


def lexicographic_edge_variables(order: int = ORDER) -> dict[tuple[int, int], int]:
    return {
        edge: index
        for index, edge in enumerate(itertools.combinations(range(order), 2), start=1)
    }


def hitting_clause_line(mask: int, variables: dict[tuple[int, int], int]) -> bytes:
    if mask.bit_count() != SET_SIZE or mask >> ORDER:
        raise AuditError("cannot emit a non-I18 mask")
    vertices = [vertex for vertex in range(ORDER) if mask & (1 << vertex)]
    literals = [variables[edge] for edge in itertools.combinations(vertices, 2)]
    if len(literals) != 153 or len(set(literals)) != 153 or any(value <= 0 for value in literals):
        raise AuditError("I18 clause did not map to 153 distinct positive variables")
    return (" ".join(map(str, literals)) + " 0\n").encode("ascii")


def inspect_common_cnf_gzip(path: Path) -> tuple[bytes, dict[str, Any]]:
    compressed = read_regular_bytes(path)
    if len(compressed) != COMMON_CNF_GZIP_BYTES or sha256_bytes(compressed) != COMMON_CNF_GZIP_SHA256:
        raise AuditError("common CNF gzip identity mismatch")
    try:
        raw = gzip.decompress(compressed)
    except (OSError, EOFError) as error:
        raise AuditError("common CNF is not a complete gzip stream") from error
    if len(raw) != COMMON_CNF_RAW_BYTES or sha256_bytes(raw) != COMMON_CNF_RAW_SHA256:
        raise AuditError("common CNF raw identity mismatch")
    header = f"p cnf {COMMON_VARIABLES} {COMMON_CLAUSES}\n".encode("ascii")
    if not raw.startswith(header) or b"\r" in raw or not raw.endswith(b"\n"):
        raise AuditError("common CNF header or line encoding mismatch")
    if raw.count(b"\n") != COMMON_CLAUSES + 1:
        raise AuditError("common CNF line count mismatch")
    return raw, {
        **artifact_identity(path, compressed),
        "uncompressed_bytes": len(raw),
        "uncompressed_sha256": sha256_bytes(raw),
        "variables": COMMON_VARIABLES,
        "clauses": COMMON_CLAUSES,
    }


def _install_no_replace(temporary: Path, destination: Path) -> None:
    try:
        os.link(temporary, destination)
    except FileExistsError as error:
        raise FileExistsError(f"refusing to overwrite {destination.name}") from error
    finally:
        temporary.unlink(missing_ok=True)


def write_augmented_cnf_stream(
    sink: Any,
    *,
    raw_common: bytes,
    common_header: bytes,
    final_header: bytes,
    positive_units: Sequence[int],
    extra_masks: Sequence[int],
    variables: dict[tuple[int, int], int],
) -> dict[str, Any]:
    """Write the deterministic header/body/unit/mask sequence to ``sink``.

    This low-level routine is parameterized so its exact byte order can be
    regression-tested without materializing the 390 MB production artifact.
    Production identity checks remain in :func:`emit_full_cnf`.
    """

    if not raw_common.startswith(common_header) or not raw_common.endswith(b"\n"):
        raise AuditError("common CNF payload does not match its declared header")
    if b"\r" in raw_common or not final_header.endswith(b"\n"):
        raise AuditError("CNF payload uses noncanonical line endings")
    if any(
        not isinstance(unit, int) or isinstance(unit, bool) or unit <= 0
        for unit in positive_units
    ):
        raise AuditError("positive-unit sequence is malformed")
    if list(extra_masks) != sorted(set(extra_masks)):
        raise AuditError("extra-mask sequence is not sorted and unique")

    digest = hashlib.sha256()
    written = 0
    lines = 0

    def write(payload: bytes) -> None:
        nonlocal written, lines
        sink.write(payload)
        digest.update(payload)
        written += len(payload)
        lines += payload.count(b"\n")

    write(final_header)
    write(raw_common[len(common_header) :])
    for unit in positive_units:
        write(f"{unit} 0\n".encode("ascii"))
    for mask in extra_masks:
        write(hitting_clause_line(mask, variables))
    return {"bytes": written, "sha256": digest.hexdigest(), "lines": lines}


def emit_full_cnf(common_cnf_gzip: Path, destination: Path, extra_masks: Sequence[int]) -> dict[str, Any]:
    if os.path.lexists(destination):
        raise FileExistsError(f"refusing to overwrite {destination.name}")
    if len(extra_masks) != EXPECTED_EXTRA_COUNT or list(extra_masks) != sorted(set(extra_masks)):
        raise AuditError("extra-mask sequence is not the exact sorted unique family")
    raw_common, common = inspect_common_cnf_gzip(common_cnf_gzip)
    common_header = f"p cnf {COMMON_VARIABLES} {COMMON_CLAUSES}\n".encode("ascii")
    final_header = f"p cnf {COMMON_VARIABLES} {FINAL_CLAUSES}\n".encode("ascii")
    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{destination.name}.", suffix=".tmp", dir=destination.parent
    )
    temporary = Path(temporary_name)
    variables = lexicographic_edge_variables()
    try:
        with os.fdopen(descriptor, "wb", closefd=True) as sink:
            stream = write_augmented_cnf_stream(
                sink,
                raw_common=raw_common,
                common_header=common_header,
                final_header=final_header,
                positive_units=PROVED_POSITIVE_UNITS,
                extra_masks=extra_masks,
                variables=variables,
            )
            sink.flush()
            os.fsync(sink.fileno())
        written = stream["bytes"]
        lines = stream["lines"]
        output_sha256 = stream["sha256"]
        if lines != FINAL_CLAUSES + 1:
            raise AuditError("emitted CNF line count mismatch")
        if FULL_CNF_BYTES is not None and written != FULL_CNF_BYTES:
            raise AuditError("emitted CNF byte count differs from frozen value")
        if FULL_CNF_SHA256 is not None and output_sha256 != FULL_CNF_SHA256:
            raise AuditError("emitted CNF SHA-256 differs from frozen value")
        _install_no_replace(temporary, destination)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return {
        "basename": destination.name,
        "bytes": written,
        "sha256": output_sha256,
        "variables": COMMON_VARIABLES,
        "clauses": FINAL_CLAUSES,
        "header_and_clause_lines": lines,
        "clause_order": [
            "authenticated_common_CNF_including_universal_bank",
            "four_proved_positive_units",
            "sorted_unique_(history_union_fixed-base_union_A+)_minus_universal",
        ],
        "common_input": common,
    }


def iter_regular_lines(path: Path) -> Iterator[bytes]:
    if path.is_symlink():
        raise AuditError(f"refusing symlink CNF: {path.name}")
    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(path, flags)
    except OSError as error:
        raise AuditError(f"cannot safely open CNF: {path.name}") from error
    opened = os.fstat(descriptor)
    if not stat.S_ISREG(opened.st_mode):
        os.close(descriptor)
        raise AuditError("CNF is not a regular file")
    try:
        with os.fdopen(descriptor, "rb", closefd=True) as source:
            for line in source:
                yield line
    finally:
        # fdopen owns the descriptor; this guards only an exception before it.
        pass


def audit_full_cnf(path: Path, extra_masks: Sequence[int]) -> dict[str, Any]:
    """Reconstruct every appended line and the embedded common-CNF identity."""

    if len(extra_masks) != EXPECTED_EXTRA_COUNT or list(extra_masks) != sorted(set(extra_masks)):
        raise AuditError("audit received a noncanonical extra-mask sequence")
    lines = iter_regular_lines(path)
    final_header = f"p cnf {COMMON_VARIABLES} {FINAL_CLAUSES}\n".encode("ascii")
    common_header = f"p cnf {COMMON_VARIABLES} {COMMON_CLAUSES}\n".encode("ascii")
    digest = hashlib.sha256()
    common_digest = hashlib.sha256(common_header)
    total_bytes = 0
    common_bytes = len(common_header)
    total_lines = 0

    def consume(expected: bytes | None = None) -> bytes:
        nonlocal total_bytes, total_lines
        try:
            line = next(lines)
        except StopIteration as error:
            raise AuditError("full-union CNF ended early") from error
        if not line.endswith(b"\n") or b"\r" in line:
            raise AuditError("full-union CNF has noncanonical line endings")
        if expected is not None and line != expected:
            raise AuditError("full-union CNF differs from reconstructed clause order")
        digest.update(line)
        total_bytes += len(line)
        total_lines += 1
        return line

    consume(final_header)
    for _ in range(COMMON_CLAUSES):
        line = consume()
        common_digest.update(line)
        common_bytes += len(line)
    if common_bytes != COMMON_CNF_RAW_BYTES or common_digest.hexdigest() != COMMON_CNF_RAW_SHA256:
        raise AuditError("embedded common CNF body identity mismatch")
    for unit in PROVED_POSITIVE_UNITS:
        consume(f"{unit} 0\n".encode("ascii"))
    variables = lexicographic_edge_variables()
    for mask in extra_masks:
        consume(hitting_clause_line(mask, variables))
    try:
        next(lines)
    except StopIteration:
        pass
    else:
        raise AuditError("full-union CNF has trailing clauses")
    if total_lines != FINAL_CLAUSES + 1:
        raise AuditError("full-union CNF line count mismatch")
    if FULL_CNF_BYTES is not None and total_bytes != FULL_CNF_BYTES:
        raise AuditError("full-union CNF byte count differs from frozen value")
    if FULL_CNF_SHA256 is not None and digest.hexdigest() != FULL_CNF_SHA256:
        raise AuditError("full-union CNF SHA-256 differs from frozen value")
    return {
        "basename": path.name,
        "bytes": total_bytes,
        "sha256": digest.hexdigest(),
        "variables": COMMON_VARIABLES,
        "clauses": FINAL_CLAUSES,
        "header_and_clause_lines": total_lines,
        "embedded_common_uncompressed_bytes": common_bytes,
        "embedded_common_uncompressed_sha256": common_digest.hexdigest(),
        "every_appended_clause_reconstructed": True,
    }


def audit_production_sources(
    *,
    matrix: Path,
    seed_verification: Path,
    universal: Path,
    history: Path,
    aplus: Path,
    core_summary: Path,
    aplus_endpoint_audit: Path,
) -> tuple[dict[str, Any], list[int]]:
    rows, matrix_identity = read_seed_matrix(matrix)
    seed_identity = validate_seed_verification(seed_verification)
    universal_masks, universal_identity = load_universal(universal)
    history_masks, history_identity = load_history(history)
    aplus_masks, aplus_identity = load_aplus(aplus)
    fixed_masks, fixed_identity = fixed_base_masks(rows)
    core_identity = validate_core_summary(core_summary)
    endpoint_identity = validate_aplus_endpoint_audit(aplus_endpoint_audit)
    extra, overlap = union_ledger(
        universal_masks, history_masks, fixed_masks, aplus_masks
    )
    endpoint_mask = int(endpoint_identity["independent_18_mask"], 16)
    if (
        endpoint_mask in set(universal_masks)
        or endpoint_mask not in set(history_masks)
        or endpoint_mask not in set(fixed_masks)
        or endpoint_mask in set(aplus_masks)
        or endpoint_mask not in set(extra)
    ):
        raise AuditError("A+ endpoint mask family-membership reconstruction mismatch")
    payload = {
        "schema": SCHEMA,
        "status": STATUS_PLAN,
        "claim_boundary": (
            "This authenticates and deduplicates universally necessary I18 "
            "clauses and, if present, byte-audits one finite CNF. It proves "
            "neither satisfiability nor unsatisfiability of exact seven, does "
            "not close branch 1, and has no global Ramsey implication."
        ),
        "mathematical_soundness": {
            "statement": (
                "For every 18-subset S of [100], alpha(G)<18 implies that at "
                "least one of the 153 pairs in S is an edge."
            ),
            "clause": "OR_{uv in binom(S,2)} x_uv",
            "literals_per_mask": 153,
            "all_four_families_are_18_subsets_of_[100]": True,
            "provenance_not_needed_for_clause_validity": True,
            "valid_for_every_exact_seven_target": True,
        },
        "inputs": {
            "matrix": matrix_identity,
            "seed_no_I18_verification": seed_identity,
            "universal": universal_identity,
            "history": history_identity,
            "fixed_base_reconstruction": fixed_identity,
            "A+": aplus_identity,
            "prior_A+_SAT_endpoint_audit": endpoint_identity,
            "singleton_proof_summary": core_identity,
        },
        "deduplication": overlap,
        "formula_plan": {
            "common_cnf_expected": {
                "gzip_bytes": COMMON_CNF_GZIP_BYTES,
                "gzip_sha256": COMMON_CNF_GZIP_SHA256,
                "uncompressed_bytes": COMMON_CNF_RAW_BYTES,
                "uncompressed_sha256": COMMON_CNF_RAW_SHA256,
            },
            "common_variables": COMMON_VARIABLES,
            "common_clauses": COMMON_CLAUSES,
            "common_universal_I18_masks": UNIVERSAL_COUNT,
            "proved_positive_units": list(PROVED_POSITIVE_UNITS),
            "new_unique_I18_clauses": len(extra),
            "all_unique_I18_masks_after_augmentation": EXPECTED_FULL_UNION_COUNT,
            "final_clauses": FINAL_CLAUSES,
            "expected_plain_CNF_bytes": FULL_CNF_BYTES,
            "expected_plain_CNF_sha256": FULL_CNF_SHA256,
            "solver_invoked": False,
        },
        "comparison_with_existing_routes": {
            "existing_A+_gate": {
                "clauses": 722_552,
                "installed_I18_families": "universal plus A+",
                "full_union_adds_clauses": EXPECTED_THREE_UNION_COUNT - UNIVERSAL_COUNT,
                "known_SAT_endpoint_I18_witness": "bfffe00000000000000000000",
                "known_witness_membership": ["history", "fixed_base"],
                "interpretation": (
                    "the historical A+ gate used history/fixed-base only as "
                    "A+ exclusion families; it did not install their clauses"
                ),
            },
            "Benders_universal_plus_all_fixed_base": {
                "deduplicated_masks": len(set(universal_masks) | set(fixed_masks)),
                "full_union_additional_masks": (
                    EXPECTED_FULL_UNION_COUNT
                    - len(set(universal_masks) | set(fixed_masks))
                ),
                "history_only_beyond_universal_and_fixed_base": 43_614,
                "A+_beyond_three_families": APLUS_COUNT,
                "encoding_difference": (
                    "Benders uses projected deletion/addition conditional cuts "
                    "in a master; this route uses full edge-variable clauses"
                ),
                "is_byte_or_formula_duplicate": False,
            },
        },
        "bounded_go_no_go": {
            "decision": "GO_BUILD_AND_AUDIT__NO_GO_LONG_SOLVE_YET",
            "reason": (
                "The union is materially stronger than the A+ CNF and blocks "
                "its known SAT model, but prior master and A+ solves took "
                "minutes to tens of minutes. Construction alone is not "
                "evidence that a long solve will close the branch."
            ),
            "optional_probe": {
                "maximum_wall_seconds": 300,
                "maximum_runs": 1,
                "solver": "one pinned proof-capable backend",
                "no_resume_no_solver_swap_no_cap_increase": True,
                "SAT": (
                    "require a complete model, evaluate all 997210 clauses, "
                    "and independently search for I18; stop after recording it"
                ),
                "UNKNOWN": "stop and learn nothing",
                "UNSAT": (
                    "retain only as unchecked unless an exact final-CNF proof "
                    "is emitted and independently replayed"
                ),
            },
        },
        "exact_seven_repair_exists": None,
        "global_ramsey_implication": None,
    }
    return payload, extra


def main(argv: Sequence[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--matrix",
        type=Path,
        default=here / "certificates" / "r3_18_n100_nearmiss.txt",
    )
    parser.add_argument(
        "--seed-verification",
        type=Path,
        default=here / "r3_18_n100_nearmiss_verification.json",
    )
    parser.add_argument(
        "--universal",
        type=Path,
        default=here / "r3_18_budget6_branch_0_universal_union.cuts.json",
    )
    parser.add_argument(
        "--history",
        type=Path,
        default=here / "r3_18_budget7_branch1_cegar_history_exclusion.json",
    )
    parser.add_argument(
        "--aplus",
        type=Path,
        default=here / "r3_18_budget7_branch1_cegar_Aplus_batch.json",
    )
    parser.add_argument(
        "--core-summary",
        type=Path,
        default=here / "r3_18_budget7_branch1_core_proof_summary.json",
    )
    parser.add_argument(
        "--aplus-endpoint-audit",
        type=Path,
        default=here / "r3_18_budget7_branch1_cegar_Aplus_f24_endpoint_audit.json",
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--emit-cnf", type=Path)
    mode.add_argument("--check-cnf", type=Path)
    parser.add_argument(
        "--common-cnf",
        type=Path,
        help="required only with --emit-cnf; frozen branch1_common.cnf.gz",
    )
    args = parser.parse_args(argv)
    if args.emit_cnf is not None and args.common_cnf is None:
        parser.error("--emit-cnf requires --common-cnf")
    if args.common_cnf is not None and args.emit_cnf is None:
        parser.error("--common-cnf is only accepted with --emit-cnf")

    payload, extra = audit_production_sources(
        matrix=args.matrix,
        seed_verification=args.seed_verification,
        universal=args.universal,
        history=args.history,
        aplus=args.aplus,
        core_summary=args.core_summary,
        aplus_endpoint_audit=args.aplus_endpoint_audit,
    )
    if args.emit_cnf is not None:
        emitted = emit_full_cnf(args.common_cnf, args.emit_cnf, extra)
        checked = audit_full_cnf(args.emit_cnf, extra)
        if {
            key: emitted[key] for key in ("basename", "bytes", "sha256", "variables", "clauses")
        } != {
            key: checked[key] for key in ("basename", "bytes", "sha256", "variables", "clauses")
        }:
            raise AuditError("emitter and independent byte audit disagree")
        payload["status"] = STATUS_CNF
        payload["emitted_cnf"] = checked
        payload["common_cnf_input"] = emitted["common_input"]
    elif args.check_cnf is not None:
        payload["status"] = STATUS_CNF
        payload["emitted_cnf"] = audit_full_cnf(args.check_cnf, extra)
    json.dump(payload, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
