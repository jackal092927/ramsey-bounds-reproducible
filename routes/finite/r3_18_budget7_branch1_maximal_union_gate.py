#!/usr/bin/env python3
"""Build the frozen branch-1 maximal-union exact-seven SAT gate.

The gate is a deterministic strengthening of the authenticated branch-1
common relaxation.  It appends, in this order,

1. the four positive edge units proved by singleton DRAT certificates;
2. every *new* member of the deduplicated universal/history/fixed-base/A+
   independent-18 union (the universal family is already in the common CNF);
3. a full maximal-triangle-free existential selector encoding for all 4,950
   vertex pairs.

This module generates and records a formula but never invokes a SAT solver.
The companion checker performs byte-for-byte reconstruction, complete-model
audits, and pinned drat-trim proof promotion.  Any missing, malformed, or
identity-mismatched input is an error; no partial output is retained.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
import os
import re
import stat
import tempfile
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence


Edge = tuple[int, int]

SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch1-maximal-union-gate-v1"
DESIGN_SCHEMA = (
    "ramsey-r3-18-n100-exact-budget7-branch1-maximal-union-design-v1"
)
STATUS_DESIGN = "DESIGN_VERIFIED_SOLVER_NOT_RUN"
STATUS_READY = "MAXIMAL_UNION_CNF_READY_SOLVER_NOT_RUN"

ORDER = 100
TARGET = 18
EDGE_VARIABLES = 4_950
COMMON_VARIABLES = 154_190
COMMON_CLAUSES = 718_452
COMMON_RAW_BYTES = 180_104_600
FIXED_EDGE: Edge = (97, 99)
POSITIVE_EDGES: tuple[Edge, ...] = (
    (11, 62),
    (18, 61),
    (18, 64),
    (18, 69),
)
POSITIVE_UNITS = (1085, 1672, 1675, 1680)

UNIVERSAL_MASKS = 251_771
HISTORY_MASKS = 64_591
FIXED_BASE_MASKS = 235_504
APLUS_MASKS = 4_096
UNION3_MASKS = 526_429
UNION4_MASKS = 530_525
APPENDED_MASKS = 278_754

SELECTOR_PAIRS = EDGE_VARIABLES
WITNESSES_PER_PAIR = ORDER - 2
SELECTOR_AUXILIARIES = SELECTOR_PAIRS * WITNESSES_PER_PAIR
SELECTOR_CLAUSES = SELECTOR_PAIRS * (1 + 2 * WITNESSES_PER_PAIR)
FINAL_VARIABLES = COMMON_VARIABLES + SELECTOR_AUXILIARIES
FINAL_CLAUSES = COMMON_CLAUSES + len(POSITIVE_UNITS) + APPENDED_MASKS + SELECTOR_CLAUSES

EXPECTED_SEED_SHA256 = (
    "e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e"
)
EXPECTED_BUDGET6_SHA256 = (
    "0abd30457c039c1c5fbba5890153c8a0c5d8558e196e7c0561410cefe37afa6a"
)
EXPECTED_SINGLETON_SUMMARY_SHA256 = (
    "8ae4f0d9ea919c915ba642eb03ec3d418b4419a89781377509acbe925d89555a"
)
EXPECTED_COMMON_GZIP_SHA256 = (
    "39249ef8378de3f2ef412e514f6283cdaa032bc17fb25fc3448463e5566f5365"
)
EXPECTED_COMMON_RAW_SHA256 = (
    "9602ef233f5fa95748ce4e7f997457d1bef47cd46453340bf5a44c2e163d3ec7"
)
EXPECTED_UNIVERSAL_SHA256 = (
    "91b5709248ff641a315f5a0389b4f3fde3d38514f3b1a8b31b6cad31224f250b"
)
EXPECTED_UNIVERSAL_ORDERED_SHA256 = (
    "f10690b826b86eb03567a2ffaffb553801fae32af20cfe4337118bddf4e41afa"
)
EXPECTED_HISTORY_SHA256 = (
    "d5100bb5dce48da3ca8ab3810290ff553ebb9d6c87ff9df1f287700563f456b0"
)
EXPECTED_HISTORY_ORDERED_SHA256 = (
    "74b4b99c18e925a7a1bbb0e4a1636dad4bf8741ba67623c2164f3607a65172a8"
)
EXPECTED_FIXED_BASE_ORDERED_SHA256 = (
    "1e9f89f40cd97a5f3b6fa93bb3c4835d45cadca8362e9d3150e90d4f385f6d8c"
)
EXPECTED_APLUS_SHA256 = (
    "835137c2df19bc851618761cc0af92400b3fa2677dd00c47101d1074c7406e8b"
)
EXPECTED_APLUS_ORDERED_SHA256 = (
    "a3cff8d8a4c77c6effb49c03e76065a17f754d0a7de727d229652276b6e8cda0"
)
EXPECTED_UNION3_ORDERED_SHA256 = (
    "f4220088cf6dfccc7b0e8b0aa7c2d1a2ef4a47f5ce31738506eefdd591613258"
)
EXPECTED_UNION4_ORDERED_SHA256 = (
    "f5c1c60877306900c1aa81bd3a7f357c3d16464ad329c676639a6f6bda9a682d"
)
EXPECTED_APPEND_ORDERED_SHA256 = (
    "2242d10f9ea3cefedef7a8c02be9a7df41db3cdb6580733e3fca9391db46d1d4"
)

PINNED_DRAT_TRIM_COMMIT = "2e3b2dc0ecf938addbd779d42877b6ed69d9a985"
PINNED_DRAT_TRIM_SHA256 = (
    "b535cc5334e97fba5b5db6013625c5a0b16ce348a98d59ff91b45a83fa56b39e",
    "31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4",
)

_HEX25 = re.compile(r"[0-9a-f]{25}\Z", flags=re.ASCII)
_SHA256 = re.compile(r"[0-9a-f]{64}\Z", flags=re.ASCII)


class GateError(ValueError):
    """A fail-closed production-gate validation error."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def ordered_masks_sha256(masks: Iterable[int], *, width: int = 25) -> str:
    digest = hashlib.sha256()
    for mask in masks:
        digest.update(f"{mask:0{width}x}\n".encode("ascii"))
    return digest.hexdigest()


def canonical_sha256(payload: Any) -> str:
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return hashlib.sha256(raw).hexdigest()


def _regular_bytes(path: Path, expected_sha256: str, label: str) -> bytes:
    try:
        metadata = os.lstat(path)
    except OSError as error:
        raise GateError(f"cannot inspect {label}") from error
    if not stat.S_ISREG(metadata.st_mode):
        raise GateError(f"{label} must be a non-symlink regular file")
    try:
        raw = path.read_bytes()
    except OSError as error:
        raise GateError(f"cannot read {label}") from error
    if hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise GateError(f"{label} SHA-256 mismatch")
    return raw


def _strict_json(raw: bytes, label: str) -> dict[str, Any]:
    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise GateError(f"{label} contains duplicate JSON key {key!r}")
            result[key] = value
        return result

    def reject_constant(value: str) -> None:
        raise GateError(f"{label} contains non-finite number {value}")

    try:
        payload = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=reject_duplicates,
            parse_constant=reject_constant,
        )
    except GateError:
        raise
    except (UnicodeError, json.JSONDecodeError) as error:
        raise GateError(f"{label} is not strict UTF-8 JSON") from error
    if not isinstance(payload, dict):
        raise GateError(f"{label} root must be an object")
    return payload


def _artifact(path: Path, expected_sha256: str | None = None) -> dict[str, Any]:
    digest = sha256_file(path)
    if expected_sha256 is not None and digest != expected_sha256:
        raise GateError(f"artifact identity changed: {path.name}")
    return {"basename": path.name, "bytes": path.stat().st_size, "sha256": digest}


def edge_variables(order: int = ORDER) -> tuple[dict[Edge, int], tuple[Edge, ...]]:
    pairs = tuple(itertools.combinations(range(order), 2))
    return {edge: index for index, edge in enumerate(pairs, start=1)}, pairs


def _parse_seed(path: Path) -> tuple[list[int], dict[str, Any]]:
    raw = _regular_bytes(path, EXPECTED_SEED_SHA256, "seed matrix")
    if not raw.endswith(b"\n") or b"\r" in raw:
        raise GateError("seed matrix is not canonical LF-terminated ASCII")
    try:
        lines = raw.decode("ascii").splitlines()
    except UnicodeError as error:
        raise GateError("seed matrix is not ASCII") from error
    if len(lines) != ORDER:
        raise GateError("seed matrix row count mismatch")
    rows = [0] * ORDER
    matrix: list[list[int]] = []
    for line in lines:
        fields = line.split()
        if len(fields) != ORDER or any(field not in {"0", "1"} for field in fields):
            raise GateError("seed matrix is not strict 100-by-100 binary data")
        matrix.append([int(field) for field in fields])
    for u in range(ORDER):
        if matrix[u][u]:
            raise GateError("seed matrix has a nonzero diagonal")
        for v in range(u + 1, ORDER):
            if matrix[u][v] != matrix[v][u]:
                raise GateError("seed matrix is asymmetric")
            if matrix[u][v]:
                rows[u] |= 1 << v
                rows[v] |= 1 << u
    edges = sum(row.bit_count() for row in rows) // 2
    triangles = 0
    for u, v, w in itertools.combinations(range(ORDER), 3):
        triangles += int(
            bool(rows[u] & (1 << v))
            and bool(rows[u] & (1 << w))
            and bool(rows[v] & (1 << w))
        )
    if edges != 827 or triangles != 1:
        raise GateError("seed graph edge/triangle identity mismatch")
    if not all(rows[u] & (1 << v) for u, v in ((97, 98), (97, 99), (98, 99))):
        raise GateError("seed graph unique triangle identity mismatch")
    return rows, {
        "basename": path.name,
        "bytes": len(raw),
        "sha256": EXPECTED_SEED_SHA256,
        "edges": edges,
        "triangles": triangles,
    }


def _validate_budget6(path: Path) -> dict[str, Any]:
    raw = _regular_bytes(path, EXPECTED_BUDGET6_SHA256, "budget-six summary")
    payload = _strict_json(raw, "budget-six summary")
    scope = payload.get("scope")
    conclusion = payload.get("conclusion")
    branches = payload.get("branches")
    if (
        payload.get("schema") != "ramsey-r3-18-n100-budget6-summary-v1"
        or payload.get("status")
        != "ALL_THREE_EXACT_BUDGET6_BRANCHES_UNSAT_PROOF_VERIFIED"
        or payload.get("input_sha256") != EXPECTED_SEED_SHA256
        or not isinstance(scope, dict)
        or scope.get("arbitrary_original_nonedge_additions_allowed") is not True
        or scope.get("maximum_input_edge_deletions_under_investigation") != 6
        or not isinstance(conclusion, dict)
        or conclusion.get("fixed_seed_deletion_repair_radius_at_least_7") is not True
        or not isinstance(branches, list)
        or [entry.get("fixed_deleted_edge") for entry in branches]
        != [[97, 98], [97, 99], [98, 99]]
        or any(
            entry.get("status") != "UNSAT_PROOF_VERIFIED"
            or entry.get("proof", {}).get("checker_status") != "VERIFIED"
            for entry in branches
        )
    ):
        raise GateError("budget-six maximality dependency is incomplete")
    return {
        "basename": path.name,
        "bytes": len(raw),
        "sha256": EXPECTED_BUDGET6_SHA256,
        "status": payload["status"],
        "at_most_six_excluded": True,
        "arbitrary_original_nonedge_additions_allowed": True,
    }


def _validate_singletons(path: Path, variables: dict[Edge, int]) -> dict[str, Any]:
    raw = _regular_bytes(
        path, EXPECTED_SINGLETON_SUMMARY_SHA256, "singleton proof summary"
    )
    payload = _strict_json(raw, "singleton proof summary")
    records = payload.get("records")
    expected_negative = [-unit for unit in POSITIVE_UNITS]
    if (
        payload.get("schema")
        != "ramsey-r3-18-n100-exact-budget7-branch1-core-proof-summary-v1"
        or payload.get("status")
        != "FOUR_SINGLETON_NO_GOODS_PROOF_VERIFIED_EXACT_SEVEN_UNKNOWN"
        or payload.get("minimality_claim") is not False
        or payload.get("global_ramsey_implication") is not None
        or not isinstance(records, list)
        or [record.get("label") for record in records]
        != ["K_a", "K_b", "K_c", "K_d"]
        or [record.get("assumption_units") for record in records]
        != [[value] for value in expected_negative]
        or any(record.get("proof_verified") is not True for record in records)
    ):
        raise GateError("singleton proof summary does not justify four units")
    mapped = tuple(variables[edge] for edge in POSITIVE_EDGES)
    if mapped != POSITIVE_UNITS:
        raise GateError("positive edge-variable mapping changed")
    return {
        "basename": path.name,
        "bytes": len(raw),
        "sha256": EXPECTED_SINGLETON_SUMMARY_SHA256,
        "status": payload["status"],
        "positive_edges": [list(edge) for edge in POSITIVE_EDGES],
        "positive_units": list(POSITIVE_UNITS),
        "fresh_core_replay_required_for_publication_promotion": True,
    }


def _mask_value(value: Any, *, strict_25: bool, label: str) -> int:
    if strict_25:
        if not isinstance(value, str) or not _HEX25.fullmatch(value):
            raise GateError(f"{label} contains a noncanonical 25-digit mask")
        mask = int(value, 16)
    else:
        if isinstance(value, bool) or not isinstance(value, (str, int)):
            raise GateError(f"{label} contains a malformed mask")
        if isinstance(value, int):
            mask = value
        else:
            encoded = value.strip().lower()
            if encoded.startswith("0x"):
                encoded = encoded[2:]
            if not encoded or any(character not in "0123456789abcdef" for character in encoded):
                raise GateError(f"{label} contains malformed hexadecimal")
            mask = int(encoded, 16)
    if mask < 0 or mask >> ORDER or mask.bit_count() != TARGET:
        raise GateError(f"{label} contains a mask of the wrong order/size")
    return mask


def _load_mask_file(
    path: Path,
    *,
    expected_file_sha256: str,
    expected_count: int,
    expected_ordered_sha256: str,
    label: str,
    strict_25: bool,
    sorted_required: bool,
    width_16_hash: bool = False,
) -> tuple[list[int], dict[str, Any]]:
    raw = _regular_bytes(path, expected_file_sha256, label)
    payload = _strict_json(raw, label)
    values = payload.get("masks")
    if not isinstance(values, list) or len(values) != expected_count:
        raise GateError(f"{label} mask count mismatch")
    masks = [_mask_value(value, strict_25=strict_25, label=label) for value in values]
    if len(masks) != len(set(masks)):
        raise GateError(f"{label} contains duplicate masks")
    if sorted_required and masks != sorted(masks):
        raise GateError(f"{label} masks are not strictly increasing")
    if width_16_hash:
        digest = ordered_masks_sha256(masks, width=16)
    else:
        digest = ordered_masks_sha256(masks, width=25)
    if digest != expected_ordered_sha256:
        raise GateError(f"{label} ordered mask digest mismatch")
    return masks, {
        "basename": path.name,
        "bytes": len(raw),
        "sha256": expected_file_sha256,
        "masks": len(masks),
        "ordered_masks_sha256": digest,
    }


def _enumerate_cliques(
    rows: Sequence[int], size: int, candidates: int
) -> Iterator[int]:
    """Enumerate fixed-size cliques by deterministic ascending bit DFS."""

    def visit(chosen: int, available: int, needed: int) -> Iterator[int]:
        if needed == 0:
            yield chosen
            return
        while available.bit_count() >= needed:
            bit = available & -available
            available ^= bit
            vertex = bit.bit_length() - 1
            yield from visit(chosen | bit, available & rows[vertex], needed - 1)

    yield from visit(0, candidates, size)


def fixed_base_masks(seed_rows: Sequence[int]) -> list[int]:
    """Independently rebuild every I18 in H-(97,99)."""

    full = (1 << ORDER) - 1
    complement_rows = [full & ~(seed_rows[v] | (1 << v)) for v in range(ORDER)]
    u, v = FIXED_EDGE
    candidates = full & ~(
        seed_rows[u] | seed_rows[v] | (1 << u) | (1 << v)
    )
    endpoint_bits = (1 << u) | (1 << v)
    masks = sorted(
        mask | endpoint_bits
        for mask in _enumerate_cliques(complement_rows, TARGET - 2, candidates)
    )
    if (
        len(masks) != FIXED_BASE_MASKS
        or len(masks) != len(set(masks))
        or ordered_masks_sha256(masks) != EXPECTED_FIXED_BASE_ORDERED_SHA256
    ):
        raise GateError("exhaustive fixed-base mask family identity mismatch")
    return masks


def load_mask_union(
    *,
    seed_path: Path,
    universal_path: Path,
    history_path: Path,
    aplus_path: Path,
) -> tuple[list[int], dict[str, Any], list[int]]:
    seed_rows, seed_info = _parse_seed(seed_path)
    universal, universal_info = _load_mask_file(
        universal_path,
        expected_file_sha256=EXPECTED_UNIVERSAL_SHA256,
        expected_count=UNIVERSAL_MASKS,
        expected_ordered_sha256=EXPECTED_UNIVERSAL_ORDERED_SHA256,
        label="universal bank",
        strict_25=False,
        sorted_required=False,
        width_16_hash=True,
    )
    history, history_info = _load_mask_file(
        history_path,
        expected_file_sha256=EXPECTED_HISTORY_SHA256,
        expected_count=HISTORY_MASKS,
        expected_ordered_sha256=EXPECTED_HISTORY_ORDERED_SHA256,
        label="historical union",
        strict_25=True,
        sorted_required=True,
    )
    aplus, aplus_info = _load_mask_file(
        aplus_path,
        expected_file_sha256=EXPECTED_APLUS_SHA256,
        expected_count=APLUS_MASKS,
        expected_ordered_sha256=EXPECTED_APLUS_ORDERED_SHA256,
        label="A+ batch",
        strict_25=True,
        sorted_required=True,
    )
    fixed = fixed_base_masks(seed_rows)
    families = [set(universal), set(history), set(fixed), set(aplus)]
    union3 = sorted(families[0] | families[1] | families[2])
    union4 = sorted(set(union3) | families[3])
    appended = sorted(set(union4) - families[0])
    if (
        len(union3) != UNION3_MASKS
        or ordered_masks_sha256(union3) != EXPECTED_UNION3_ORDERED_SHA256
        or len(union4) != UNION4_MASKS
        or ordered_masks_sha256(union4) != EXPECTED_UNION4_ORDERED_SHA256
        or len(appended) != APPENDED_MASKS
        or ordered_masks_sha256(appended) != EXPECTED_APPEND_ORDERED_SHA256
    ):
        raise GateError("four-family union identity mismatch")
    overlap = {
        "universal_history": len(families[0] & families[1]),
        "universal_fixed_base": len(families[0] & families[2]),
        "history_fixed_base": len(families[1] & families[2]),
        "universal_history_fixed_base": len(
            families[0] & families[1] & families[2]
        ),
        "Aplus_with_prior_three_union": len(families[3] & set(union3)),
    }
    if overlap != {
        "universal_history": 11_429,
        "universal_fixed_base": 4_460,
        "history_fixed_base": 10_194,
        "universal_history_fixed_base": 646,
        "Aplus_with_prior_three_union": 0,
    }:
        raise GateError("four-family overlap census mismatch")
    info = {
        "seed": seed_info,
        "sources": {
            "universal": universal_info,
            "history": history_info,
            "fixed_base": {
                "derived_from_seed_sha256": EXPECTED_SEED_SHA256,
                "masks": len(fixed),
                "ordered_masks_sha256": EXPECTED_FIXED_BASE_ORDERED_SHA256,
                "complete_enumeration": True,
            },
            "Aplus": aplus_info,
        },
        "overlap_census": overlap,
        "canonical_insertion_new_masks": {
            "universal": UNIVERSAL_MASKS,
            "history": 53_162,
            "fixed_base": 221_496,
            "Aplus": APLUS_MASKS,
        },
        "three_family_union": {
            "masks": len(union3),
            "ordered_masks_sha256": EXPECTED_UNION3_ORDERED_SHA256,
        },
        "four_family_union": {
            "masks": len(union4),
            "ordered_masks_sha256": EXPECTED_UNION4_ORDERED_SHA256,
        },
        "appended_beyond_common_universal_bank": {
            "masks": len(appended),
            "ordered_masks_sha256": EXPECTED_APPEND_ORDERED_SHA256,
        },
    }
    return appended, info, seed_rows


def hitting_clause(mask: int, variables: dict[Edge, int]) -> list[int]:
    vertices = [vertex for vertex in range(ORDER) if mask & (1 << vertex)]
    if len(vertices) != TARGET:
        raise GateError("cannot emit a hitting clause for a malformed mask")
    return [variables[edge] for edge in itertools.combinations(vertices, 2)]


def selector_variable(pair_index: int, witness_rank: int) -> int:
    if not (0 <= pair_index < SELECTOR_PAIRS):
        raise GateError("selector pair index out of range")
    if not (0 <= witness_rank < WITNESSES_PER_PAIR):
        raise GateError("selector witness rank out of range")
    return COMMON_VARIABLES + 1 + pair_index * WITNESSES_PER_PAIR + witness_rank


def iter_selector_clauses(
    variables: dict[Edge, int], pairs: Sequence[Edge]
) -> Iterator[list[int]]:
    if len(pairs) != SELECTOR_PAIRS:
        raise GateError("selector scope must contain every vertex pair")
    for pair_index, (u, v) in enumerate(pairs):
        witnesses = [w for w in range(ORDER) if w not in {u, v}]
        yvars = [
            selector_variable(pair_index, rank)
            for rank in range(WITNESSES_PER_PAIR)
        ]
        yield [variables[(u, v)], *yvars]
        for w, yvar in zip(witnesses, yvars, strict=True):
            yield [-yvar, variables[tuple(sorted((u, w)))]]
            yield [-yvar, variables[tuple(sorted((v, w)))]]


class _AtomicDimacs:
    def __init__(self, destination: Path, max_bytes: int):
        if destination.exists():
            raise FileExistsError(f"refusing to overwrite {destination}")
        if not isinstance(max_bytes, int) or isinstance(max_bytes, bool) or max_bytes <= 0:
            raise GateError("DIMACS byte cap must be a positive integer")
        destination.parent.mkdir(parents=True, exist_ok=True)
        descriptor, name = tempfile.mkstemp(
            prefix=f".{destination.name}.", suffix=".tmp", dir=destination.parent
        )
        self.destination = destination
        self.temporary = Path(name)
        self.sink = os.fdopen(descriptor, "wb")
        self.max_bytes = max_bytes
        self.bytes = 0
        self.lines = 0
        self.digest = hashlib.sha256()

    def write(self, raw: bytes) -> None:
        if self.bytes + len(raw) > self.max_bytes:
            raise GateError("DIMACS generation exceeded the fixed disk-byte cap")
        self.sink.write(raw)
        self.digest.update(raw)
        self.bytes += len(raw)
        self.lines += raw.count(b"\n")

    def finish(self) -> dict[str, Any]:
        self.sink.flush()
        os.fsync(self.sink.fileno())
        self.sink.close()
        os.replace(self.temporary, self.destination)
        return {
            "basename": self.destination.name,
            "bytes": self.bytes,
            "sha256": self.digest.hexdigest(),
            "variables": FINAL_VARIABLES,
            "clauses": FINAL_CLAUSES,
            "header_and_clause_lines": self.lines,
        }

    def abort(self) -> None:
        try:
            if not self.sink.closed:
                self.sink.close()
        finally:
            self.temporary.unlink(missing_ok=True)


def emit_cnf(
    *,
    common_cnf_gzip: Path,
    destination: Path,
    appended_masks: Sequence[int],
    max_output_bytes: int,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Stream one exact raw DIMACS formula and return input/output identities."""

    _regular_bytes(common_cnf_gzip, EXPECTED_COMMON_GZIP_SHA256, "common CNF")
    if len(appended_masks) != APPENDED_MASKS:
        raise GateError("appended mask family count mismatch")
    if ordered_masks_sha256(appended_masks) != EXPECTED_APPEND_ORDERED_SHA256:
        raise GateError("appended mask family digest mismatch")
    variables, pairs = edge_variables()
    emitter = _AtomicDimacs(destination, max_output_bytes)
    original_digest = hashlib.sha256()
    original_bytes = 0
    original_lines = 0
    try:
        with gzip.open(common_cnf_gzip, "rb") as source:
            old_header = source.readline()
            expected_header = f"p cnf {COMMON_VARIABLES} {COMMON_CLAUSES}\n".encode(
                "ascii"
            )
            if old_header != expected_header:
                raise GateError("common CNF DIMACS header mismatch")
            original_digest.update(old_header)
            original_bytes += len(old_header)
            original_lines += 1
            emitter.write(f"p cnf {FINAL_VARIABLES} {FINAL_CLAUSES}\n".encode("ascii"))
            while True:
                line = source.readline()
                if not line:
                    break
                if not line.endswith(b"\n") or b"\r" in line:
                    raise GateError("common CNF has noncanonical clause bytes")
                original_digest.update(line)
                original_bytes += len(line)
                original_lines += 1
                emitter.write(line)
        if (
            original_digest.hexdigest() != EXPECTED_COMMON_RAW_SHA256
            or original_bytes != COMMON_RAW_BYTES
            or original_lines != COMMON_CLAUSES + 1
        ):
            raise GateError("decompressed common CNF identity mismatch")
        for unit in POSITIVE_UNITS:
            emitter.write(f"{unit} 0\n".encode("ascii"))
        for mask in appended_masks:
            clause = hitting_clause(mask, variables)
            emitter.write((" ".join(map(str, clause)) + " 0\n").encode("ascii"))
        for clause in iter_selector_clauses(variables, pairs):
            emitter.write((" ".join(map(str, clause)) + " 0\n").encode("ascii"))
        if emitter.lines != FINAL_CLAUSES + 1:
            raise GateError("generated DIMACS line count mismatch")
        output = emitter.finish()
    except Exception:
        emitter.abort()
        destination.unlink(missing_ok=True)
        raise
    common = {
        **_artifact(common_cnf_gzip, EXPECTED_COMMON_GZIP_SHA256),
        "uncompressed_bytes": original_bytes,
        "uncompressed_sha256": original_digest.hexdigest(),
        "variables": COMMON_VARIABLES,
        "clauses": COMMON_CLAUSES,
    }
    return output, common


def build_design(
    *,
    seed_path: Path,
    budget6_path: Path,
    singleton_summary_path: Path,
    universal_path: Path,
    history_path: Path,
    aplus_path: Path,
) -> tuple[dict[str, Any], list[int]]:
    variables, pairs = edge_variables()
    if len(pairs) != EDGE_VARIABLES or max(variables.values()) != EDGE_VARIABLES:
        raise GateError("edge-variable mapping changed")
    budget6 = _validate_budget6(budget6_path)
    singleton = _validate_singletons(singleton_summary_path, variables)
    appended, union_info, _ = load_mask_union(
        seed_path=seed_path,
        universal_path=universal_path,
        history_path=history_path,
        aplus_path=aplus_path,
    )
    design: dict[str, Any] = {
        "schema": DESIGN_SCHEMA,
        "status": STATUS_DESIGN,
        "inputs": {
            **union_info,
            "budget6_maximality_dependency": budget6,
            "singleton_retention_dependency": singleton,
        },
        "formula": {
            "common_relaxation": {
                "variables": COMMON_VARIABLES,
                "clauses": COMMON_CLAUSES,
                "universal_I18_clauses_already_installed": UNIVERSAL_MASKS,
            },
            "four_positive_units": len(POSITIVE_UNITS),
            "additional_deduplicated_I18_clauses": len(appended),
            "total_distinct_I18_masks_installed": UNION4_MASKS,
            "full_maximal_triangle_free_selectors": {
                "scope": "all lexicographic unordered vertex pairs",
                "pairs": SELECTOR_PAIRS,
                "witnesses_per_pair": WITNESSES_PER_PAIR,
                "auxiliary_variables": SELECTOR_AUXILIARIES,
                "long_clauses": SELECTOR_PAIRS,
                "binary_implication_clauses": 2 * SELECTOR_AUXILIARIES,
                "clauses": SELECTOR_CLAUSES,
                "first_auxiliary_variable": COMMON_VARIABLES + 1,
                "last_auxiliary_variable": FINAL_VARIABLES,
                "allocation": (
                    "pair-major lexicographic (u,v), then ascending w with "
                    "w not in {u,v}"
                ),
                "semantics": (
                    "x_uv OR some y_uv_w, together with y_uv_w -> x_uw "
                    "and y_uv_w -> x_vw"
                ),
            },
            "final_variables": FINAL_VARIABLES,
            "final_clauses": FINAL_CLAUSES,
            "clause_order": [
                "authenticated common-relaxation body",
                "four proof-checked positive units",
                "sorted union-minus-universal I18 hitting clauses",
                "full pair-major maximality selector clauses",
            ],
            "raw_cnf_sha256": None,
            "raw_cnf_bytes": None,
            "production_cnf_status": "NOT_BUILT_BY_DESIGN_AUDIT",
        },
        "non_repetition": {
            "versus_Aplus": (
                "A+ appended only 4,096 model-derived masks to the common "
                "formula.  This gate installs the entire four-family union "
                "and full all-pair maximality selectors."
            ),
            "versus_Benders_all_fixed_base_cuts": (
                "The Benders option preloads the exhaustive fixed-base I18 "
                "family into a deletion-support master.  This is a direct "
                "primary-graph CNF over the common relaxation, also includes "
                "universal/history/A+, four retention units, and maximality."
            ),
        },
        "branch_scope": {
            "fixed_deleted_triangle_edge": [97, 99],
            "no_transfer_to_other_triangle_edge_branches": True,
            "symmetry_boundary": (
                "A separate deterministic degree-initialized 1-WL diagnostic "
                "reaches 100 singleton color classes after two refinement "
                "rounds, so the seed automorphism group is necessarily "
                "trivial.  In particular the three triangle-edge branches "
                "cannot be identified by seed symmetry."
            ),
            "diagnostic_is_not_an_additional_formula_dependency": True,
        },
        "state_machine": {
            "NOT_RUN": STATUS_READY,
            "SAT": (
                "Accept only a complete assignment satisfying every exact "
                "clause plus direct graph checks for triangle-freeness, exact "
                "seven one-sided deletions, retention units, degree cap, full "
                "maximality, and an independent-18 search."
            ),
            "UNSAT": (
                "Accept only after fresh replay of a nonempty proof against "
                "this exact raw CNF by a binary pinned to drat-trim commit "
                f"{PINNED_DRAT_TRIM_COMMIT}."
            ),
            "UNKNOWN": (
                "Timeout, disk cap, malformed output, invalid model, unchecked "
                "UNSAT, or any identity mismatch learns nothing."
            ),
        },
        "limits": {
            "generator_is_streaming": True,
            "generator_atomic_install": True,
            "generator_refuses_overwrite": True,
            "solver_invoked": False,
            "learned_masks": [],
        },
        "claim_boundary": {
            "branch1_closed": False,
            "other_triangle_edge_branches_closed": False,
            "exact_seven_resolved": False,
            "global_Ramsey_improvement": False,
            "unchecked_solver_UNSAT_accepted": False,
            "UNKNOWN_learns_any_cut": False,
        },
    }
    design["record_sha256"] = canonical_sha256(design)
    return design, appended


def _atomic_json(path: Path, payload: dict[str, Any]) -> None:
    if path.exists():
        raise FileExistsError(f"refusing to overwrite {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as sink:
            json.dump(payload, sink, indent=2, sort_keys=True)
            sink.write("\n")
            sink.flush()
            os.fsync(sink.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def _absolute_lexical(path: Path) -> Path:
    """Make a path absolute without dereferencing its final symlink."""
    return Path(os.path.abspath(os.fspath(path)))


def main(argv: Sequence[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "mode", choices=("design", "build"), help="authenticate only or emit CNF"
    )
    parser.add_argument(
        "--seed",
        type=Path,
        default=here / "certificates" / "r3_18_n100_nearmiss.txt",
    )
    parser.add_argument(
        "--budget6-summary", type=Path, default=here / "r3_18_budget6_summary.json"
    )
    parser.add_argument(
        "--singleton-summary",
        type=Path,
        default=here / "r3_18_budget7_branch1_core_proof_summary.json",
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
        "--Aplus",
        type=Path,
        default=here / "r3_18_budget7_branch1_cegar_Aplus_batch.json",
    )
    parser.add_argument("--common-cnf", type=Path)
    parser.add_argument("--output-cnf", type=Path)
    parser.add_argument("--output-record", type=Path, required=True)
    parser.add_argument("--max-output-bytes", type=int, default=1_000_000_000)
    args = parser.parse_args(argv)

    design, appended = build_design(
        seed_path=_absolute_lexical(args.seed),
        budget6_path=_absolute_lexical(args.budget6_summary),
        singleton_summary_path=_absolute_lexical(args.singleton_summary),
        universal_path=_absolute_lexical(args.universal),
        history_path=_absolute_lexical(args.history),
        aplus_path=_absolute_lexical(args.Aplus),
    )
    if args.mode == "design":
        if args.common_cnf is not None or args.output_cnf is not None:
            parser.error("design mode does not accept CNF input/output")
        _atomic_json(_absolute_lexical(args.output_record), design)
        print(json.dumps(design, indent=2, sort_keys=True))
        return 0

    if args.common_cnf is None or args.output_cnf is None:
        parser.error("build mode requires --common-cnf and --output-cnf")
    output_cnf = _absolute_lexical(args.output_cnf)
    output_record = _absolute_lexical(args.output_record)
    if output_cnf == output_record:
        parser.error("CNF and record paths must differ")
    cnf, common = emit_cnf(
        common_cnf_gzip=_absolute_lexical(args.common_cnf),
        destination=output_cnf,
        appended_masks=appended,
        max_output_bytes=args.max_output_bytes,
    )
    record = {
        **design,
        "schema": SCHEMA,
        "status": STATUS_READY,
        "common_cnf": common,
        "formula": {
            **design["formula"],
            "raw_cnf_sha256": cnf["sha256"],
            "raw_cnf_bytes": cnf["bytes"],
            "production_cnf_status": "BUILT_AND_IDENTITY_RECORDED",
        },
        "generated_cnf": cnf,
        "solver": {"status": "NOT_RUN"},
        "proof_verified": False,
        "learned_masks": [],
        "exact_seven_repair_exists": None,
        "global_ramsey_implication": None,
    }
    record.pop("record_sha256", None)
    record["record_sha256"] = canonical_sha256(record)
    try:
        _atomic_json(output_record, record)
    except Exception:
        output_cnf.unlink(missing_ok=True)
        raise
    print(json.dumps(record, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
