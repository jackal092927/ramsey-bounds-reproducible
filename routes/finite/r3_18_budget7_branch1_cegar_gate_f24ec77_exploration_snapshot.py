#!/usr/bin/env python3
"""One bounded, certificate-safe CEGAR gate for branch 1 at budget seven.

This gate starts from the frozen common-relaxation CNF and its independently
audited SAT model.  It authenticates both artifacts, checks an ordered batch
of exactly 4096 independent-18 masks against that model, and proves they are
new relative to the universal bank, the complete historical learned-cut
union, and the exhaustive fixed branch-1 base family.  It then adds those
hitting clauses plus the four edge units already proved positive by the
singleton core certificates.  The resulting DIMACS file is emitted in one
deterministic order.

An optional pinned standalone CaDiCaL call is hard wall-clock bounded.  Its
outcomes are deliberately asymmetric:

* SAT is accepted only as a completely assigned model that satisfies every
  emitted clause; any displayed independent-18 set is checked and reported
  but is not installed automatically as another cut.
* timeout, malformed output, and every other UNKNOWN/error learn nothing.
* UNSAT is never promoted from an exit code.  A nonempty DRAT artifact is
  required and is labelled ``UNCHECKED`` until a separate drat-trim replay.

Thus this script is an exploration gate, not a new Ramsey-number certificate.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
import math
import os
import re
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any, Iterable, Sequence

try:
    from .check_r3_18_budget7_branch1_common_sat import (
        audit_common_sat,
        parse_complete_model,
    )
    from .check_r3_18_budget7_branch1_core_cnf import (
        AuditError,
        EXPECTED_BANK_SHA256,
        EXPECTED_INPUT_SHA256,
        EXPECTED_ORDERED_MASKS_SHA256,
        PRODUCTION_BANK_MASKS,
        PRODUCTION_BANK_SET_SIZE,
        PRODUCTION_COMMON_CLAUSES,
        PRODUCTION_MAXIMUM_VARIABLE,
        PRODUCTION_ORDER,
        lexicographic_edge_variables,
        load_ordered_bank,
        read_seed_matrix,
    )
    from .verify_ramsey import CliqueTargetSearch, complement
except ImportError:  # pragma: no cover - direct script execution
    from check_r3_18_budget7_branch1_common_sat import (
        audit_common_sat,
        parse_complete_model,
    )
    from check_r3_18_budget7_branch1_core_cnf import (
        AuditError,
        EXPECTED_BANK_SHA256,
        EXPECTED_INPUT_SHA256,
        EXPECTED_ORDERED_MASKS_SHA256,
        PRODUCTION_BANK_MASKS,
        PRODUCTION_BANK_SET_SIZE,
        PRODUCTION_COMMON_CLAUSES,
        PRODUCTION_MAXIMUM_VARIABLE,
        PRODUCTION_ORDER,
        lexicographic_edge_variables,
        load_ordered_bank,
        read_seed_matrix,
    )
    from verify_ramsey import CliqueTargetSearch, complement


SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch1-cegar-gate-v1"
MASK_BATCH_SCHEMA = (
    "ramsey-r3-18-n100-exact-budget7-branch1-cegar-mask-batch-v1"
)
HISTORY_EXCLUSION_SCHEMA = (
    "ramsey-r3-18-n100-branch1-history-exclusion-v1"
)
MASK_BATCH_SIZE = 4096
HISTORY_EXCLUSION_MASKS = 64_591
HISTORY_EXCLUSION_RAW_MASKS = 113_448
HISTORY_EXCLUSION_SOURCES = 18
HISTORY_EXCLUSION_ORDERED_SHA256 = (
    "74b4b99c18e925a7a1bbb0e4a1636dad4bf8741ba67623c2164f3607a65172a8"
)
FROZEN_HISTORY_EXCLUSION_FILE_SHA256 = (
    "d5100bb5dce48da3ca8ab3810290ff553ebb9d6c87ff9df1f287700563f456b0"
)
FIXED_BRANCH1_BASE_MASKS = 235_504
FIXED_BRANCH1_BASE_ORDERED_SHA256 = (
    "1e9f89f40cd97a5f3b6fa93bb3c4835d45cadca8362e9d3150e90d4f385f6d8c"
)
FIXED_BRANCH1_EDGE = (97, 99)
FROZEN_MASK_BATCH_FILE_SHA256 = (
    "835137c2df19bc851618761cc0af92400b3fa2677dd00c47101d1074c7406e8b"
)
FROZEN_MASK_BATCH_ORDERED_SHA256 = (
    "a3cff8d8a4c77c6effb49c03e76065a17f754d0a7de727d229652276b6e8cda0"
)
PINNED_CADICAL_COMMIT = "c60730422e758ef1cebe7aeddf2dda31c996bf04"
PINNED_CADICAL_SHA256 = (
    "f5e2cf978a3b9ebf17601b9a7a25f298c684c18841846b66bdd6a6e20951fb2a"
)

FROZEN_COMMON_CNF_GZIP_SHA256 = (
    "39249ef8378de3f2ef412e514f6283cdaa032bc17fb25fc3448463e5566f5365"
)
FROZEN_COMMON_CNF_RAW_SHA256 = (
    "9602ef233f5fa95748ce4e7f997457d1bef47cd46453340bf5a44c2e163d3ec7"
)
FROZEN_COMMON_MODEL_GZIP_SHA256 = (
    "9057db25b785640345e6f724cb1c79313642bb62ec2a19d9f310e25700de024d"
)
FROZEN_COMMON_MODEL_RAW_SHA256 = (
    "51e7832b69a18b29db817d1e180f1a071f771fbb50e358de4fb57a3810cd737e"
)

PROVED_POSITIVE_EDGES = ((11, 62), (18, 61), (18, 64), (18, 69))
PROVED_POSITIVE_UNITS = (1085, 1672, 1675, 1680)

STATUS_READY = "AUGMENTED_CNF_READY_SOLVER_NOT_RUN"
STATUS_SAT_WITNESS = "SAT_MODEL_VERIFIED_I18_WITNESS_NO_LEARNING"
STATUS_SAT_ESCALATE = "SAT_MODEL_VERIFIED_NO_I18_WITNESS_ESCALATE"
STATUS_UNKNOWN_WALL = "UNKNOWN_SOLVER_WALL_LIMIT_NO_LEARNING"
STATUS_UNKNOWN_ERROR = "UNKNOWN_SOLVER_ERROR_NO_LEARNING"
STATUS_UNKNOWN_SAT = "UNKNOWN_INVALID_SAT_MODEL_NO_LEARNING"
STATUS_UNKNOWN_UNSAT = "UNKNOWN_UNSAT_WITHOUT_COMPLETE_PROOF_NO_LEARNING"
STATUS_UNSAT_UNCHECKED = "UNSAT_PROOF_GENERATED_UNCHECKED"

STATE_MACHINE = {
    "NOT_RUN": STATUS_READY,
    "SAT": (
        "Require a complete model and direct evaluation of every augmented "
        "clause; report a checked I18 witness or escalate, and learn no cut."
    ),
    "UNKNOWN": (
        "Timeout, nonstandard exit, malformed transcript, or invalid model; "
        "learn no cut and make no satisfiability claim."
    ),
    "UNSAT": (
        "Require a nonempty proof artifact, but keep UNSAT unchecked until an "
        "independent drat-trim replay succeeds."
    ),
}

_SHA256_RE = re.compile(r"[0-9a-f]{64}\Z", flags=re.ASCII)


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _artifact(path: Path, *, raw: bytes | None = None) -> dict[str, Any]:
    result: dict[str, Any] = {
        "basename": path.name,
        "bytes": path.stat().st_size,
        "sha256": _sha256_file(path),
    }
    if raw is not None:
        result.update(
            {
                "uncompressed_bytes": len(raw),
                "uncompressed_sha256": hashlib.sha256(raw).hexdigest(),
            }
        )
    return result


def _strict_json_bytes(raw: bytes, description: str) -> dict[str, Any]:
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


def _stage_exact(source: Path, destination: Path, expected_sha256: str) -> dict[str, Any]:
    """Copy and authenticate one opened input stream into a private snapshot."""

    if not _SHA256_RE.fullmatch(expected_sha256):
        raise AuditError("invalid frozen SHA-256 constant")
    if not source.is_file():
        raise AuditError(f"missing frozen input: {source.name}")
    digest = hashlib.sha256()
    size = 0
    try:
        with source.open("rb") as opened, destination.open("xb") as sink:
            while True:
                block = opened.read(1024 * 1024)
                if not block:
                    break
                sink.write(block)
                digest.update(block)
                size += len(block)
            sink.flush()
            os.fsync(sink.fileno())
    except OSError as error:
        destination.unlink(missing_ok=True)
        raise AuditError(f"could not stage frozen input: {source.name}") from error
    if digest.hexdigest() != expected_sha256:
        destination.unlink(missing_ok=True)
        raise AuditError(f"frozen input SHA-256 mismatch: {source.name}")
    return {"basename": source.name, "bytes": size, "sha256": digest.hexdigest()}


def ordered_masks_sha256(masks: Iterable[int], width: int) -> str:
    digest = hashlib.sha256()
    for mask in masks:
        digest.update(f"{mask:0{width}x}\n".encode("ascii"))
    return digest.hexdigest()


def _canonical_mask_array(
    encoded: Any,
    *,
    description: str,
    order: int,
    set_size: int,
    expected_count: int,
) -> tuple[list[int], int]:
    if not isinstance(encoded, list) or len(encoded) != expected_count:
        raise AuditError(
            f"{description} must contain exactly {expected_count} masks"
        )
    width = (order + 3) // 4
    pattern = re.compile(rf"[0-9a-f]{{{width}}}\Z", flags=re.ASCII)
    masks: list[int] = []
    for index, value in enumerate(encoded):
        if not isinstance(value, str) or not pattern.fullmatch(value):
            raise AuditError(
                f"{description} mask {index} is not canonical "
                f"{width}-digit lowercase hex"
            )
        mask = int(value, 16)
        if mask >> order or mask.bit_count() != set_size:
            raise AuditError(
                f"{description} mask {index} is not an {set_size}-set "
                f"on {order} vertices"
            )
        masks.append(mask)
    if masks != sorted(masks) or len(masks) != len(set(masks)):
        raise AuditError(f"{description} is not strictly increasing and unique")
    return masks, width


def load_history_exclusion(
    path: Path,
    *,
    order: int = PRODUCTION_ORDER,
    set_size: int = PRODUCTION_BANK_SET_SIZE,
    expected_count: int = HISTORY_EXCLUSION_MASKS,
    expected_ordered_sha256: str = HISTORY_EXCLUSION_ORDERED_SHA256,
    expected_sources: int = HISTORY_EXCLUSION_SOURCES,
    expected_raw_masks: int = HISTORY_EXCLUSION_RAW_MASKS,
    expected_file_sha256: str = FROZEN_HISTORY_EXCLUSION_FILE_SHA256,
) -> tuple[list[int], dict[str, Any]]:
    """Authenticate the union of every historically learned branch-1 cut."""

    if not path.is_file():
        raise AuditError(f"history exclusion is not a regular file: {path.name}")
    try:
        raw = path.read_bytes()
    except OSError as error:
        raise AuditError("history exclusion is unreadable") from error
    actual_file_sha256 = hashlib.sha256(raw).hexdigest()
    if not _SHA256_RE.fullmatch(expected_file_sha256):
        raise AuditError("invalid frozen history-exclusion file SHA-256")
    if actual_file_sha256 != expected_file_sha256:
        raise AuditError("history exclusion file SHA-256 differs from frozen value")
    payload = _strict_json_bytes(raw, "history exclusion")
    expected_keys = {
        "schema",
        "masks",
        "masks_count",
        "ordered_masks_sha256",
        "sources",
        "source_raw_count_sum",
        "within_source_duplicates",
        "union_duplicates_removed",
    }
    if set(payload) != expected_keys:
        raise AuditError("history exclusion schema fields are not exact")
    if payload.get("schema") != HISTORY_EXCLUSION_SCHEMA:
        raise AuditError("history exclusion schema mismatch")
    if payload.get("masks_count") != expected_count:
        raise AuditError("history exclusion recorded mask count mismatch")
    if payload.get("source_raw_count_sum") != expected_raw_masks:
        raise AuditError("history exclusion raw source count mismatch")
    if payload.get("within_source_duplicates") != 0:
        raise AuditError("history exclusion records within-source duplicates")
    if payload.get("union_duplicates_removed") != expected_raw_masks - expected_count:
        raise AuditError("history exclusion union duplicate count mismatch")

    masks, width = _canonical_mask_array(
        payload.get("masks"),
        description="history exclusion",
        order=order,
        set_size=set_size,
        expected_count=expected_count,
    )
    actual_ordered = ordered_masks_sha256(masks, width)
    if actual_ordered != expected_ordered_sha256:
        raise AuditError("history exclusion ordered digest differs from frozen value")
    if payload.get("ordered_masks_sha256") != actual_ordered:
        raise AuditError("history exclusion recorded ordered digest mismatch")

    sources = payload.get("sources")
    if not isinstance(sources, list) or len(sources) != expected_sources:
        raise AuditError("history exclusion must bind the exact source ledger")
    seen_paths: set[str] = set()
    raw_count_sum = 0
    for index, source in enumerate(sources):
        if not isinstance(source, dict) or set(source) != {
            "path",
            "file_sha256",
            "field",
            "raw_count",
        }:
            raise AuditError(f"history source {index} has noncanonical fields")
        source_path = source.get("path")
        if (
            not isinstance(source_path, str)
            or not source_path
            or Path(source_path).is_absolute()
            or ".." in Path(source_path).parts
        ):
            raise AuditError(f"history source {index} has an unsafe path")
        if source_path in seen_paths:
            raise AuditError("history exclusion repeats a source path")
        seen_paths.add(source_path)
        if not isinstance(source.get("file_sha256"), str) or not _SHA256_RE.fullmatch(
            source["file_sha256"]
        ):
            raise AuditError(f"history source {index} has an invalid digest")
        if source.get("field") != "strict_state.additional_conditional_masks_hex":
            raise AuditError(f"history source {index} binds the wrong checkpoint field")
        raw_count = source.get("raw_count")
        if not isinstance(raw_count, int) or isinstance(raw_count, bool) or raw_count <= 0:
            raise AuditError(f"history source {index} has an invalid raw count")
        raw_count_sum += raw_count
    if raw_count_sum != expected_raw_masks:
        raise AuditError("history source ledger raw counts do not sum correctly")

    return masks, {
        "basename": path.name,
        "bytes": len(raw),
        "sha256": actual_file_sha256,
        "masks": len(masks),
        "ordered_masks_sha256": actual_ordered,
        "source_checkpoints": len(sources),
        "source_raw_masks": raw_count_sum,
        "within_source_duplicates": 0,
    }


def load_and_validate_mask_batch(
    path: Path,
    *,
    assignment: Sequence[bool | None],
    variables: dict[tuple[int, int], int],
    installed_masks: set[int] | frozenset[int],
    order: int = PRODUCTION_ORDER,
    set_size: int = PRODUCTION_BANK_SET_SIZE,
    expected_count: int = MASK_BATCH_SIZE,
    require_frozen_exclusion_provenance: bool = False,
    expected_base_ordered_sha256: str = EXPECTED_ORDERED_MASKS_SHA256,
    expected_history_ordered_sha256: str = HISTORY_EXCLUSION_ORDERED_SHA256,
    fixed_base_rows: Sequence[int] | None = None,
    expected_fixed_base_ordered_sha256: str = (
        FIXED_BRANCH1_BASE_ORDERED_SHA256
    ),
    expected_file_sha256: str = FROZEN_MASK_BATCH_FILE_SHA256,
    expected_ordered_sha256: str = FROZEN_MASK_BATCH_ORDERED_SHA256,
) -> tuple[list[int], dict[str, Any]]:
    """Read one canonical ordered mask batch and check it against a model."""

    if not path.is_file():
        raise AuditError(f"mask batch is not a regular file: {path.name}")
    try:
        raw = path.read_bytes()
    except OSError as error:
        raise AuditError("mask batch is unreadable") from error
    actual_file_sha256 = hashlib.sha256(raw).hexdigest()
    if require_frozen_exclusion_provenance:
        if not _SHA256_RE.fullmatch(expected_file_sha256):
            raise AuditError("invalid frozen mask-batch file SHA-256")
        if actual_file_sha256 != expected_file_sha256:
            raise AuditError("mask batch file SHA-256 differs from frozen value")
    payload = _strict_json_bytes(raw, "mask batch")
    if require_frozen_exclusion_provenance:
        expected_keys = {
            "schema",
            "masks",
            "masks_count",
            "ordered_masks_sha256",
            "enumeration",
            "exclusions",
        }
        if set(payload) != expected_keys or payload.get("schema") != MASK_BATCH_SCHEMA:
            raise AuditError("final mask batch lacks exact frozen-exclusion provenance")
        if payload.get("masks_count") != expected_count:
            raise AuditError("final mask batch recorded count mismatch")
        if payload.get("enumeration") != "reverse-first":
            raise AuditError("final mask batch did not use reverse-first enumeration")
        exclusions = payload.get("exclusions")
        if not isinstance(exclusions, dict) or set(exclusions) != {
            "base_universal_bank",
            "historical_union",
            "fixed_branch1_base_family",
        }:
            raise AuditError("final mask batch exclusions are incomplete")
        expected_exclusions = {
            "base_universal_bank": {
                "masks": PRODUCTION_BANK_MASKS,
                "ordered_masks_sha256": expected_base_ordered_sha256,
            },
            "historical_union": {
                "masks": HISTORY_EXCLUSION_MASKS,
                "ordered_masks_sha256": expected_history_ordered_sha256,
            },
            "fixed_branch1_base_family": {
                "masks": FIXED_BRANCH1_BASE_MASKS,
                "ordered_masks_sha256": expected_fixed_base_ordered_sha256,
            },
        }
        if exclusions != expected_exclusions:
            raise AuditError("final mask batch exclusion identities mismatch")
    elif set(payload) != {"masks"}:
        raise AuditError("mask batch must contain exactly one masks array")

    masks, width = _canonical_mask_array(
        payload.get("masks"),
        description="mask batch",
        order=order,
        set_size=set_size,
        expected_count=expected_count,
    )
    actual_ordered = ordered_masks_sha256(masks, width)
    if (
        require_frozen_exclusion_provenance
        and actual_ordered != expected_ordered_sha256
    ):
        raise AuditError("mask batch ordered digest differs from frozen value")
    if require_frozen_exclusion_provenance and payload.get(
        "ordered_masks_sha256"
    ) != actual_ordered:
        raise AuditError("final mask batch recorded ordered digest mismatch")

    for index, mask in enumerate(masks):
        if mask in installed_masks:
            raise AuditError(f"mask {index} is already present in a frozen exclusion set")
        vertices = [vertex for vertex in range(order) if mask & (1 << vertex)]
        if require_frozen_exclusion_provenance:
            if fixed_base_rows is None or len(fixed_base_rows) != order:
                raise AuditError("fixed branch-1 base rows were not authenticated")
            if mask_belongs_to_fixed_branch1_base(mask, fixed_base_rows):
                raise AuditError(
                    f"mask {index} belongs to the exhaustive fixed-base I18 family"
                )
        for edge in itertools.combinations(vertices, 2):
            variable = variables[edge]
            if variable >= len(assignment) or assignment[variable] is None:
                raise AuditError("mask validation reached an unassigned edge variable")
            if assignment[variable]:
                raise AuditError(f"mask {index} is not independent in the frozen model")

    return masks, {
        "basename": path.name,
        "bytes": len(raw),
        "sha256": actual_file_sha256,
        "masks": len(masks),
        "ordered_masks_sha256": actual_ordered,
        "canonical_hex_width": width,
        "all_new_relative_to_three_frozen_exclusion_families": True,
        "all_independent_in_frozen_model": True,
    }


def validate_positive_units(
    units: Sequence[int],
    *,
    assignment: Sequence[bool | None],
    variables: dict[tuple[int, int], int],
) -> tuple[int, ...]:
    expected = tuple(variables[edge] for edge in PROVED_POSITIVE_EDGES)
    if expected != PROVED_POSITIVE_UNITS:
        raise AuditError("positive-unit edge mapping changed")
    supplied = tuple(units)
    if supplied != expected:
        raise AuditError("positive units differ from the four proved singleton units")
    for unit in supplied:
        if unit >= len(assignment) or assignment[unit] is not True:
            raise AuditError("a proved positive unit is false in the frozen common model")
    return supplied


def hitting_clause(
    mask: int,
    *,
    order: int,
    variables: dict[tuple[int, int], int],
) -> list[int]:
    vertices = [vertex for vertex in range(order) if mask & (1 << vertex)]
    return [variables[edge] for edge in itertools.combinations(vertices, 2)]


def mask_belongs_to_fixed_branch1_base(
    mask: int, rows: Sequence[int]
) -> bool:
    vertices = [vertex for vertex in range(len(rows)) if mask & (1 << vertex)]
    for edge in itertools.combinations(vertices, 2):
        u, v = edge
        present = bool((rows[u] >> v) & 1)
        if edge == FIXED_BRANCH1_EDGE:
            present = False
        if present:
            return False
    return True


def emit_augmented_cnf(
    common_cnf_gzip: Path,
    destination: Path,
    *,
    variables_count: int,
    common_clause_count: int,
    positive_units: Sequence[int],
    masks: Sequence[int],
    edge_variables: dict[tuple[int, int], int],
    order: int,
) -> dict[str, Any]:
    """Emit common clauses, fixed positive units, then ordered I18 cuts."""

    if destination.exists():
        raise FileExistsError(f"refusing to overwrite {destination.name}")
    total_clauses = common_clause_count + len(positive_units) + len(masks)
    expected_header = f"p cnf {variables_count} {common_clause_count}\n".encode("ascii")
    new_header = f"p cnf {variables_count} {total_clauses}\n".encode("ascii")
    digest = hashlib.sha256()
    size = 0
    lines = 0
    last_byte = b""

    def write(sink: Any, payload: bytes) -> None:
        nonlocal size, lines, last_byte
        sink.write(payload)
        digest.update(payload)
        size += len(payload)
        lines += payload.count(b"\n")
        if payload:
            last_byte = payload[-1:]

    try:
        with gzip.open(common_cnf_gzip, "rb") as source, destination.open("xb") as sink:
            if source.readline() != expected_header:
                raise AuditError("frozen common CNF header changed")
            write(sink, new_header)
            body_lines = 0
            while True:
                block = source.read(1024 * 1024)
                if not block:
                    break
                if b"\r" in block:
                    raise AuditError("common CNF contains noncanonical CR bytes")
                body_lines += block.count(b"\n")
                write(sink, block)
            if body_lines != common_clause_count or last_byte != b"\n":
                raise AuditError("common CNF body line count or termination changed")

            for unit in positive_units:
                if not isinstance(unit, int) or isinstance(unit, bool) or unit <= 0:
                    raise AuditError("augmented CNF contains a non-positive proved unit")
                write(sink, f"{unit} 0\n".encode("ascii"))
            for mask in masks:
                clause = hitting_clause(mask, order=order, variables=edge_variables)
                if not clause:
                    raise AuditError("augmented CNF contains an empty I18 clause")
                write(sink, (" ".join(map(str, clause)) + " 0\n").encode("ascii"))
            sink.flush()
            os.fsync(sink.fileno())
    except Exception:
        destination.unlink(missing_ok=True)
        raise
    if lines != total_clauses + 1:
        destination.unlink(missing_ok=True)
        raise AuditError("augmented CNF emitted the wrong number of lines")
    return {
        "basename": destination.name,
        "bytes": size,
        "sha256": digest.hexdigest(),
        "variables": variables_count,
        "clauses": total_clauses,
        "header_and_clause_lines": lines,
        "clause_order": [
            "frozen_common_clauses",
            "four_proved_positive_units",
            "ordered_new_I18_hitting_clauses",
        ],
    }


def parse_sat_stdout(
    stdout: bytes,
    maximum_variable: int,
) -> tuple[list[bool | None], bytes]:
    """Extract a complete model and return one canonical gzip-ready transcript."""

    try:
        text = stdout.decode("utf-8")
    except UnicodeError as error:
        raise AuditError("CaDiCaL SAT transcript is not UTF-8") from error
    status_lines = [line for line in text.splitlines() if line.startswith("s ")]
    if status_lines != ["s SATISFIABLE"]:
        raise AuditError("CaDiCaL SAT transcript lacks one exact SAT status line")
    value_lines = [line for line in text.splitlines() if line.startswith("v ")]
    if not value_lines:
        raise AuditError("CaDiCaL SAT transcript has no model lines")
    tokens: list[int] = []
    try:
        for line in value_lines:
            fields = line.split()[1:]
            if not fields:
                raise AuditError("CaDiCaL SAT transcript has an empty model line")
            tokens.extend(int(field) for field in fields)
    except ValueError as error:
        raise AuditError("CaDiCaL SAT transcript has a non-integer model token") from error
    if not tokens or tokens[-1] != 0 or any(token == 0 for token in tokens[:-1]):
        raise AuditError("CaDiCaL SAT transcript needs one final zero terminator")

    assignment: list[bool | None] = [None] * (maximum_variable + 1)
    for literal in tokens[:-1]:
        variable = abs(literal)
        if not 1 <= variable <= maximum_variable:
            raise AuditError("CaDiCaL model literal is outside the DIMACS range")
        if assignment[variable] is not None:
            raise AuditError("CaDiCaL model assigns a variable more than once")
        assignment[variable] = literal > 0
    if any(value is None for value in assignment[1:]):
        raise AuditError("CaDiCaL model does not assign every DIMACS variable")

    canonical_literals = [
        variable if assignment[variable] else -variable
        for variable in range(1, maximum_variable + 1)
    ]
    lines = ["s SATISFIABLE\n"]
    chunk_size = 16
    for offset in range(0, len(canonical_literals), chunk_size):
        chunk = canonical_literals[offset : offset + chunk_size]
        suffix = " 0" if offset + chunk_size >= len(canonical_literals) else ""
        lines.append("v " + " ".join(map(str, chunk)) + suffix + "\n")
    return assignment, "".join(lines).encode("ascii")


def deterministic_gzip_bytes(path: Path, raw: bytes) -> dict[str, Any]:
    if path.exists():
        raise FileExistsError(f"refusing to overwrite {path.name}")
    try:
        with path.open("xb") as opened:
            with gzip.GzipFile(
                filename="", mode="wb", fileobj=opened, compresslevel=9, mtime=0
            ) as zipped:
                zipped.write(raw)
            opened.flush()
            os.fsync(opened.fileno())
    except Exception:
        path.unlink(missing_ok=True)
        raise
    return _artifact(path, raw=raw)


def deterministic_gzip_file(source: Path, destination: Path) -> dict[str, Any]:
    if not source.is_file() or source.stat().st_size <= 0:
        raise AuditError("CaDiCaL did not produce a nonempty proof artifact")
    if destination.exists():
        raise FileExistsError(f"refusing to overwrite {destination.name}")
    raw_digest = hashlib.sha256()
    raw_size = 0
    try:
        with source.open("rb") as opened, destination.open("xb") as raw_output:
            with gzip.GzipFile(
                filename="", mode="wb", fileobj=raw_output, compresslevel=9, mtime=0
            ) as zipped:
                while True:
                    block = opened.read(1024 * 1024)
                    if not block:
                        break
                    raw_digest.update(block)
                    raw_size += len(block)
                    zipped.write(block)
            raw_output.flush()
            os.fsync(raw_output.fileno())
    except Exception:
        destination.unlink(missing_ok=True)
        raise
    result = _artifact(destination)
    result.update(
        {
            "uncompressed_bytes": raw_size,
            "uncompressed_sha256": raw_digest.hexdigest(),
        }
    )
    return result


def evaluate_dimacs_model(
    cnf_path: Path,
    assignment: Sequence[bool | None],
    *,
    expected_variables: int,
    expected_clauses: int,
) -> dict[str, Any]:
    """Directly evaluate every clause in the exact emitted DIMACS file."""

    checked = 0
    with cnf_path.open("rb") as source:
        expected_header = f"p cnf {expected_variables} {expected_clauses}\n".encode("ascii")
        if source.readline() != expected_header:
            raise AuditError("augmented CNF header differs from its recorded identity")
        for raw_line in source:
            checked += 1
            if not raw_line.endswith(b"\n") or b"\r" in raw_line:
                raise AuditError("augmented CNF has a noncanonical clause line")
            try:
                tokens = [int(token) for token in raw_line.split()]
            except ValueError as error:
                raise AuditError("augmented CNF has a non-integer literal") from error
            if not tokens or tokens[-1] != 0 or any(token == 0 for token in tokens[:-1]):
                raise AuditError("augmented CNF has a malformed clause terminator")
            satisfied = False
            for literal in tokens[:-1]:
                variable = abs(literal)
                if not 1 <= variable <= expected_variables:
                    raise AuditError("augmented CNF literal is out of range")
                value = assignment[variable]
                if value is None:
                    raise AuditError("augmented CNF evaluation reached an unassigned variable")
                if bool(value) == (literal > 0):
                    satisfied = True
            if not satisfied:
                raise AuditError(f"new SAT model falsifies augmented clause {checked}")
    if checked != expected_clauses:
        raise AuditError("augmented CNF clause count changed during model evaluation")
    return {"all_clauses_satisfied": True, "clauses_evaluated": checked}


def checked_independent_witness(
    assignment: Sequence[bool | None],
    *,
    variables: dict[tuple[int, int], int],
    order: int,
    target: int,
    universal_bank_masks: set[int] | frozenset[int],
    historical_masks: set[int] | frozenset[int],
    new_gate_masks: set[int] | frozenset[int],
    fixed_base_rows: Sequence[int] | None = None,
) -> dict[str, Any]:
    rows = [0] * order
    for (u, v), variable in variables.items():
        if assignment[variable]:
            rows[u] |= 1 << v
            rows[v] |= 1 << u
    search = CliqueTargetSearch(complement(rows), target).run()
    if not search.exists:
        return {
            "independent_set_exists": False,
            "witness": None,
            "mask_hex": None,
            "search_nodes": search.recursive_nodes,
        }
    witness = sorted(search.witness)
    if len(witness) != target or len(witness) != len(set(witness)):
        raise AuditError("independent-set search returned a malformed witness")
    for edge in itertools.combinations(witness, 2):
        if assignment[variables[edge]]:
            raise AuditError("independent-set search returned an adjacent pair")
    mask = sum(1 << vertex for vertex in witness)
    overlap = {
        "universal_bank": mask in universal_bank_masks,
        "historical_learned_union": mask in historical_masks,
        "exhaustive_fixed_branch1_base_family": (
            fixed_base_rows is not None
            and mask_belongs_to_fixed_branch1_base(mask, fixed_base_rows)
        ),
        "new_gate_batch": mask in new_gate_masks,
    }
    if overlap["universal_bank"] or overlap["new_gate_batch"]:
        raise AuditError("new model violates an installed I18 hitting clause")
    new_relative_to_three = not any(
        overlap[key]
        for key in (
            "universal_bank",
            "historical_learned_union",
            "exhaustive_fixed_branch1_base_family",
        )
    )
    width = (order + 3) // 4
    return {
        "independent_set_exists": True,
        "witness": witness,
        "mask_hex": f"{mask:0{width}x}",
        "search_nodes": search.recursive_nodes,
        "pairwise_independence_checked": True,
        "new_relative_to_all_installed_masks": True,
        "overlap_with_exclusion_families": overlap,
        "known_from_historical_learned_union": overlap[
            "historical_learned_union"
        ],
        "known_from_exhaustive_fixed_base_family": overlap[
            "exhaustive_fixed_branch1_base_family"
        ],
        "new_relative_to_three_frozen_exclusion_families": (
            new_relative_to_three
        ),
        "installed_or_learned_by_this_gate": overlap["new_gate_batch"],
    }


def validate_pinned_cadical(cadical: Path, staged: Path) -> dict[str, Any]:
    if not cadical.is_file() or not os.access(cadical, os.X_OK):
        raise AuditError(f"CaDiCaL is not executable: {cadical.name}")
    marker = cadical.resolve().parent / "SOURCE_COMMIT"
    try:
        marker_bytes = marker.read_bytes()
    except OSError as error:
        raise AuditError("CaDiCaL lacks a readable adjacent SOURCE_COMMIT") from error
    if marker_bytes != (PINNED_CADICAL_COMMIT + "\n").encode("ascii"):
        raise AuditError("CaDiCaL SOURCE_COMMIT mismatch")
    staged_info = _stage_exact(cadical, staged, PINNED_CADICAL_SHA256)
    staged.chmod(0o700)
    if _sha256_file(staged) != PINNED_CADICAL_SHA256:
        raise AuditError("staged CaDiCaL changed after authentication")
    return {
        "basename": cadical.name,
        "sha256": staged_info["sha256"],
        "source_commit": PINNED_CADICAL_COMMIT,
        "source_commit_marker_sha256": hashlib.sha256(marker_bytes).hexdigest(),
    }


def run_pinned_cadical(
    cadical: Path,
    cnf_path: Path,
    proof_path: Path,
    wall_seconds: float,
) -> dict[str, Any]:
    """Run an authenticated private checker copy under a process-group wall."""

    if (
        not isinstance(wall_seconds, (int, float))
        or isinstance(wall_seconds, bool)
        or not math.isfinite(wall_seconds)
        or wall_seconds <= 0
    ):
        raise AuditError("CaDiCaL wall limit must be finite and positive")
    proof_path.unlink(missing_ok=True)
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="ramsey-cegar-cadical-") as temporary:
        staged = Path(temporary) / "cadical"
        checker = validate_pinned_cadical(cadical, staged)
        environment = {
            key: value
            for key, value in os.environ.items()
            if not key.startswith(("LD_", "DYLD_", "LDR_"))
            and key not in {"GCONV_PATH", "LIBPATH", "SHLIB_PATH"}
        }
        environment["LC_ALL"] = "C"
        environment["LANG"] = "C"
        try:
            process = subprocess.Popen(
                [
                    str(staged),
                    "--no-binary",
                    "--checkproof=0",
                    str(cnf_path),
                    str(proof_path),
                ],
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                env=environment,
                start_new_session=True,
            )
        except OSError as error:
            return {
                "status": STATUS_UNKNOWN_ERROR,
                "reason": "CaDiCaL could not be started",
                "error_type": type(error).__name__,
                "wall_limit_seconds": wall_seconds,
                "elapsed_seconds": time.monotonic() - started,
                "checker": checker,
                "learned_masks": [],
            }
        try:
            stdout, stderr = process.communicate(timeout=wall_seconds)
        except subprocess.TimeoutExpired:
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            stdout, stderr = process.communicate()
            proof_path.unlink(missing_ok=True)
            return {
                "status": STATUS_UNKNOWN_WALL,
                "exitcode": process.returncode,
                "wall_limit_seconds": wall_seconds,
                "elapsed_seconds": time.monotonic() - started,
                "stdout_sha256": hashlib.sha256(stdout).hexdigest(),
                "stderr_sha256": hashlib.sha256(stderr).hexdigest(),
                "checker": checker,
                "learned_masks": [],
            }

    return {
        "status": "RAW_SOLVER_RESULT",
        "exitcode": process.returncode,
        "wall_limit_seconds": wall_seconds,
        "elapsed_seconds": time.monotonic() - started,
        "stdout_sha256": hashlib.sha256(stdout).hexdigest(),
        "stderr_sha256": hashlib.sha256(stderr).hexdigest(),
        "stdout_tail": stdout.decode("utf-8", errors="replace")[-4000:],
        "stderr_tail": stderr.decode("utf-8", errors="replace")[-4000:],
        "checker": checker,
        "_stdout": stdout,
        "learned_masks": [],
    }


def _exact_status_lines(stdout: bytes) -> list[str]:
    return [
        line
        for line in stdout.decode("utf-8", errors="replace").splitlines()
        if line.startswith("s ")
    ]


def classify_raw_solver_result(
    raw: dict[str, Any], proof_path: Path
) -> dict[str, Any]:
    """Fail-closed exit/status/proof classification before model validation."""

    if raw.get("status") != "RAW_SOLVER_RESULT":
        return raw
    result = {key: value for key, value in raw.items() if key != "_stdout"}
    stdout = raw.get("_stdout")
    if not isinstance(stdout, bytes):
        result["status"] = STATUS_UNKNOWN_ERROR
        result["reason"] = "solver result has no byte transcript"
        return result
    status_lines = _exact_status_lines(stdout)
    exitcode = raw.get("exitcode")
    if exitcode == 10 and status_lines == ["s SATISFIABLE"]:
        result["status"] = "SAT_TRANSCRIPT_PENDING_MODEL_AUDIT"
        result["_stdout"] = stdout
        proof_path.unlink(missing_ok=True)
        return result
    if exitcode == 20 and status_lines == ["s UNSATISFIABLE"]:
        if proof_path.is_file() and proof_path.stat().st_size > 0:
            result["status"] = "UNSAT_PROOF_PENDING_COMPRESSION"
            return result
        result["status"] = STATUS_UNKNOWN_UNSAT
        result["reason"] = "exit 20 lacked a nonempty proof artifact"
        return result
    proof_path.unlink(missing_ok=True)
    result["status"] = STATUS_UNKNOWN_ERROR
    result["reason"] = "noncanonical exit-code/status-line combination"
    return result


def _atomic_json(path: Path, payload: dict[str, Any]) -> None:
    rendered = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    if path.exists() or temporary.exists():
        raise FileExistsError(f"refusing to overwrite {path.name}")
    try:
        with temporary.open("xb") as sink:
            sink.write(rendered)
            sink.flush()
            os.fsync(sink.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def run_gate(
    *,
    common_cnf: Path,
    common_model: Path,
    masks_path: Path,
    history_exclusion_path: Path,
    matrix_path: Path,
    bank_path: Path,
    positive_units: Sequence[int],
    output_dir: Path,
    cadical: Path | None,
    wall_seconds: float,
) -> dict[str, Any]:
    """Authenticate inputs, emit one augmented CNF, and optionally solve it."""

    if output_dir.exists():
        raise FileExistsError(f"refusing existing output directory: {output_dir.name}")
    variables, pairs = lexicographic_edge_variables(PRODUCTION_ORDER)
    if len(pairs) != 4_950:
        raise AuditError("production edge-variable mapping changed")

    with tempfile.TemporaryDirectory(prefix="ramsey-cegar-inputs-") as temporary:
        private = Path(temporary)
        staged_cnf = private / "common.cnf.gz"
        staged_model = private / "common.model.gz"
        cnf_input = _stage_exact(
            common_cnf, staged_cnf, FROZEN_COMMON_CNF_GZIP_SHA256
        )
        model_input = _stage_exact(
            common_model, staged_model, FROZEN_COMMON_MODEL_GZIP_SHA256
        )
        common_audit = audit_common_sat(
            cnf_path=staged_cnf,
            model_path=staged_model,
            matrix_path=matrix_path,
            bank_path=bank_path,
            expected_cnf_raw_sha256=FROZEN_COMMON_CNF_RAW_SHA256,
            expected_cnf_gzip_sha256=FROZEN_COMMON_CNF_GZIP_SHA256,
            expected_model_raw_sha256=FROZEN_COMMON_MODEL_RAW_SHA256,
            expected_model_gzip_sha256=FROZEN_COMMON_MODEL_GZIP_SHA256,
        )
        assignment, parsed_model = parse_complete_model(
            staged_model, PRODUCTION_MAXIMUM_VARIABLE
        )
        units = validate_positive_units(
            positive_units, assignment=assignment, variables=variables
        )
        bank_masks, bank_ordered_sha256 = load_ordered_bank(
            bank_path,
            order=PRODUCTION_ORDER,
            set_size=PRODUCTION_BANK_SET_SIZE,
            expected_sha256=EXPECTED_BANK_SHA256,
            expected_ordered_sha256=EXPECTED_ORDERED_MASKS_SHA256,
        )
        if len(bank_masks) != PRODUCTION_BANK_MASKS:
            raise AuditError("production universal-bank mask count changed")
        bank_mask_set = set(bank_masks)
        seed_rows = read_seed_matrix(matrix_path, EXPECTED_INPUT_SHA256)
        history_masks, history_info = load_history_exclusion(
            history_exclusion_path
        )
        history_mask_set = set(history_masks)
        new_masks, mask_info = load_and_validate_mask_batch(
            masks_path,
            assignment=assignment,
            variables=variables,
            installed_masks=bank_mask_set | history_mask_set,
            require_frozen_exclusion_provenance=True,
            expected_base_ordered_sha256=bank_ordered_sha256,
            expected_history_ordered_sha256=history_info[
                "ordered_masks_sha256"
            ],
            fixed_base_rows=seed_rows,
        )
        new_mask_set = set(new_masks)
        overlap_counts = {
            "universal_bank": len(new_mask_set & bank_mask_set),
            "historical_learned_union": len(new_mask_set & history_mask_set),
            "exhaustive_fixed_branch1_base_family": sum(
                mask_belongs_to_fixed_branch1_base(mask, seed_rows)
                for mask in new_masks
            ),
        }
        if any(overlap_counts.values()):
            raise AuditError("new mask batch overlaps a frozen exclusion family")
        mask_info["three_family_overlap_counts"] = overlap_counts
        mask_info["three_family_zero_overlap_verified"] = True

        output_dir.mkdir(parents=True, exist_ok=False)
        augmented = output_dir / "branch1_cegar_augmented.cnf"
        cnf_info = emit_augmented_cnf(
            staged_cnf,
            augmented,
            variables_count=PRODUCTION_MAXIMUM_VARIABLE,
            common_clause_count=PRODUCTION_COMMON_CLAUSES,
            positive_units=units,
            masks=new_masks,
            edge_variables=variables,
            order=PRODUCTION_ORDER,
        )

    base: dict[str, Any] = {
        "schema": SCHEMA,
        "status": STATUS_READY,
        "state_machine": STATE_MACHINE,
        "claim_boundary": (
            "This is one finite CEGAR gate. SAT only authenticates a displayed "
            "model/witness; UNKNOWN learns nothing; a generated UNSAT proof is "
            "unchecked until independent drat-trim replay."
        ),
        "inputs": {
            "common_cnf": cnf_input,
            "common_model": model_input,
            "common_model_audit_status": common_audit.get("status"),
            "common_model_assignment_literals": parsed_model["assignment_literals"],
            "universal_bank": {
                "basename": bank_path.name,
                "masks": len(bank_masks),
                "ordered_masks_sha256": bank_ordered_sha256,
            },
            "historical_exclusion": history_info,
            "fixed_branch1_base_exclusion": {
                "masks": FIXED_BRANCH1_BASE_MASKS,
                "ordered_masks_sha256": FIXED_BRANCH1_BASE_ORDERED_SHA256,
                "membership_check": (
                    "direct pairwise independence test in the authenticated "
                    "seed with edge (97,99) removed"
                ),
            },
            "new_mask_batch": mask_info,
        },
        "augmentation": {
            "positive_edges": [list(edge) for edge in PROVED_POSITIVE_EDGES],
            "positive_units": list(units),
            "new_I18_clauses": len(new_masks),
            "augmented_cnf": cnf_info,
        },
        "solver": {"status": "NOT_RUN"},
        "learned_masks": [],
        "proof_verified": False,
        "exact_seven_repair_exists": None,
        "global_ramsey_implication": None,
    }
    if cadical is None:
        _atomic_json(output_dir / "branch1_cegar_gate.json", base)
        return base

    raw_proof = output_dir / ".branch1_cegar_unsat.drat.raw"
    raw_solver = run_pinned_cadical(
        cadical, augmented, raw_proof, wall_seconds
    )
    solver = classify_raw_solver_result(raw_solver, raw_proof)
    internal_stdout = solver.pop("_stdout", None)
    state = solver.get("status")
    if state == "SAT_TRANSCRIPT_PENDING_MODEL_AUDIT":
        try:
            if not isinstance(internal_stdout, bytes):
                raise AuditError("SAT transcript bytes were lost before model audit")
            new_assignment, canonical_model = parse_sat_stdout(
                internal_stdout, PRODUCTION_MAXIMUM_VARIABLE
            )
            model_path = output_dir / "branch1_cegar_sat.model.gz"
            model_info = deterministic_gzip_bytes(model_path, canonical_model)
            reparsed, _ = parse_complete_model(model_path, PRODUCTION_MAXIMUM_VARIABLE)
            if reparsed != new_assignment:
                raise AuditError("canonical SAT-model round trip changed assignment")
            evaluation = evaluate_dimacs_model(
                augmented,
                new_assignment,
                expected_variables=PRODUCTION_MAXIMUM_VARIABLE,
                expected_clauses=cnf_info["clauses"],
            )
            witness = checked_independent_witness(
                new_assignment,
                variables=variables,
                order=PRODUCTION_ORDER,
                target=PRODUCTION_BANK_SET_SIZE,
                universal_bank_masks=bank_mask_set,
                historical_masks=history_mask_set,
                new_gate_masks=new_mask_set,
                fixed_base_rows=seed_rows,
            )
            solver.update(
                {
                    "status": (
                        STATUS_SAT_WITNESS
                        if witness["independent_set_exists"]
                        else STATUS_SAT_ESCALATE
                    ),
                    "model": model_info,
                    "model_evaluation": evaluation,
                    "I18_search": witness,
                    "learned_masks": [],
                }
            )
        except Exception as error:
            (output_dir / "branch1_cegar_sat.model.gz").unlink(missing_ok=True)
            solver.update(
                {
                    "status": STATUS_UNKNOWN_SAT,
                    "model_audit_error_type": type(error).__name__,
                    "model_audit_error": str(error),
                    "learned_masks": [],
                }
            )
    elif state == "UNSAT_PROOF_PENDING_COMPRESSION":
        proof_path = output_dir / "branch1_cegar_unsat.drat.gz"
        try:
            proof_info = deterministic_gzip_file(raw_proof, proof_path)
        except Exception as error:
            proof_path.unlink(missing_ok=True)
            solver.update(
                {
                    "status": STATUS_UNKNOWN_UNSAT,
                    "proof_error_type": type(error).__name__,
                    "proof_error": str(error),
                    "learned_masks": [],
                }
            )
        else:
            solver.update(
                {
                    "status": STATUS_UNSAT_UNCHECKED,
                    "proof": proof_info,
                    "proof_checked_by_drat_trim": False,
                    "unsat_claim_accepted": False,
                    "learned_masks": [],
                }
            )
    raw_proof.unlink(missing_ok=True)

    base["status"] = solver["status"]
    base["solver"] = solver
    base["proof_verified"] = False
    base["learned_masks"] = []
    _atomic_json(output_dir / "branch1_cegar_gate.json", base)
    return base


def main(argv: Sequence[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--common-cnf", type=Path, required=True)
    parser.add_argument("--common-model", type=Path, required=True)
    parser.add_argument("--masks", type=Path, required=True)
    parser.add_argument("--history-exclusion", type=Path, required=True)
    parser.add_argument(
        "--matrix",
        type=Path,
        default=here / "certificates" / "r3_18_n100_nearmiss.txt",
    )
    parser.add_argument(
        "--universal-bank",
        type=Path,
        default=here / "r3_18_budget6_branch_0_universal_union.cuts.json",
    )
    parser.add_argument(
        "--positive-unit",
        action="append",
        type=int,
        required=True,
        help="repeat exactly four times in canonical order",
    )
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--cadical", type=Path)
    parser.add_argument("--wall-seconds", type=float, default=600.0)
    args = parser.parse_args(argv)

    protected = {
        args.common_cnf.resolve(),
        args.common_model.resolve(),
        args.masks.resolve(),
        args.history_exclusion.resolve(),
        args.matrix.resolve(),
        args.universal_bank.resolve(),
        Path(__file__).resolve(),
        Path(__file__).resolve().with_name(
            "check_r3_18_budget7_branch1_common_sat.py"
        ).resolve(),
        Path(__file__).resolve().with_name(
            "check_r3_18_budget7_branch1_core_cnf.py"
        ).resolve(),
    }
    output_dir = args.output_dir.resolve()
    if output_dir in protected or any(output_dir == path.parent for path in protected):
        parser.error("output directory collides with an authenticated input")

    try:
        result = run_gate(
            common_cnf=args.common_cnf.resolve(),
            common_model=args.common_model.resolve(),
            masks_path=args.masks.resolve(),
            history_exclusion_path=args.history_exclusion.resolve(),
            matrix_path=args.matrix.resolve(),
            bank_path=args.universal_bank.resolve(),
            positive_units=args.positive_unit,
            output_dir=output_dir,
            cadical=args.cadical.resolve() if args.cadical else None,
            wall_seconds=args.wall_seconds,
        )
    except Exception as error:
        failure = {
            "schema": SCHEMA,
            "status": "FAILED_CEGAR_GATE_INPUT_OR_EXPORT_AUDIT",
            "error_type": type(error).__name__,
            "error": str(error),
            "learned_masks": [],
            "proof_verified": False,
        }
        print(json.dumps(failure, sort_keys=True), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
