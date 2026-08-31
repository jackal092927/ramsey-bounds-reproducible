#!/usr/bin/env python3
"""Fail-closed auditor for the historical f24 A+ exploration endpoint.

This program never invokes a SAT solver.  It freezes and authenticates the
historical runner, its gate JSON, and the exact augmented CNF before examining
one completed endpoint.  The old runner's outcome is deliberately not treated
as hardened evidence:

* a SAT model is parsed again, evaluated against every exact CNF clause, and
  converted to a graph that is checked directly for triangles and I18;
* an UNSAT proof is only hashed and bound to a promotion-pending record;
* an UNKNOWN result authenticates the bounded endpoint but makes no SAT/UNSAT
  claim and learns no mask.

The checker identity recorded by the historical runner must be the pinned
CaDiCaL identity.  ``--cadical`` can additionally rehash a local copy of that
binary and its adjacent SOURCE_COMMIT marker; it still does not execute it.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import os
import re
import stat
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

try:
    from .check_r3_18_budget7_branch1_common_sat import parse_complete_model
    from .check_r3_18_budget7_branch1_core_cnf import (
        AuditError,
        lexicographic_edge_variables,
    )
    from .r3_18_budget7_branch1_cegar_gate import evaluate_dimacs_model
    from .verify_ramsey import CliqueTargetSearch, complement
except ImportError:  # pragma: no cover - direct script execution
    from check_r3_18_budget7_branch1_common_sat import parse_complete_model
    from check_r3_18_budget7_branch1_core_cnf import (
        AuditError,
        lexicographic_edge_variables,
    )
    from r3_18_budget7_branch1_cegar_gate import evaluate_dimacs_model
    from verify_ramsey import CliqueTargetSearch, complement


AUDIT_SCHEMA = (
    "ramsey-r3-18-n100-exact-budget7-branch1-cegar-f24-endpoint-audit-v1"
)
GATE_SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch1-cegar-gate-v1"
HISTORICAL_RUNNER_BASENAME = (
    "r3_18_budget7_branch1_cegar_gate_f24ec77_exploration_snapshot.py"
)
HISTORICAL_RUNNER_SHA256 = (
    "f24ec77a4d4a5d516f138c98e7d3117f6438e968dcae5d4ef1bcfaf1c339a69b"
)
PINNED_CADICAL_COMMIT = "c60730422e758ef1cebe7aeddf2dda31c996bf04"
PINNED_CADICAL_SHA256 = (
    "f5e2cf978a3b9ebf17601b9a7a25f298c684c18841846b66bdd6a6e20951fb2a"
)

FROZEN_AUGMENTED_CNF_SHA256 = (
    "6fbe630343afcf31a5affa9a70a315e3033bc077b24fc9a58d5084e63fdd389f"
)
FROZEN_AUGMENTED_CNF_BYTES = 183_161_315
FROZEN_AUGMENTED_CNF_CLAUSES = 722_552
FROZEN_COMMON_CNF_GZIP_SHA256 = (
    "39249ef8378de3f2ef412e514f6283cdaa032bc17fb25fc3448463e5566f5365"
)
FROZEN_COMMON_MODEL_GZIP_SHA256 = (
    "9057db25b785640345e6f724cb1c79313642bb62ec2a19d9f310e25700de024d"
)
FROZEN_BANK_ORDERED_SHA256 = (
    "f10690b826b86eb03567a2ffaffb553801fae32af20cfe4337118bddf4e41afa"
)
FROZEN_HISTORY_FILE_SHA256 = (
    "d5100bb5dce48da3ca8ab3810290ff553ebb9d6c87ff9df1f287700563f456b0"
)
FROZEN_HISTORY_ORDERED_SHA256 = (
    "74b4b99c18e925a7a1bbb0e4a1636dad4bf8741ba67623c2164f3607a65172a8"
)
FROZEN_FIXED_BASE_ORDERED_SHA256 = (
    "1e9f89f40cd97a5f3b6fa93bb3c4835d45cadca8362e9d3150e90d4f385f6d8c"
)
FROZEN_MASK_BATCH_FILE_SHA256 = (
    "835137c2df19bc851618761cc0af92400b3fa2677dd00c47101d1074c7406e8b"
)
FROZEN_MASK_BATCH_ORDERED_SHA256 = (
    "a3cff8d8a4c77c6effb49c03e76065a17f754d0a7de727d229652276b6e8cda0"
)

STATUS_SAT_WITNESS = "SAT_MODEL_VERIFIED_I18_WITNESS_NO_LEARNING"
STATUS_SAT_ESCALATE = "SAT_MODEL_VERIFIED_NO_I18_WITNESS_ESCALATE"
STATUS_UNKNOWN_WALL = "UNKNOWN_SOLVER_WALL_LIMIT_NO_LEARNING"
STATUS_UNKNOWN_ERROR = "UNKNOWN_SOLVER_ERROR_NO_LEARNING"
STATUS_UNKNOWN_SAT = "UNKNOWN_INVALID_SAT_MODEL_NO_LEARNING"
STATUS_UNKNOWN_UNSAT = "UNKNOWN_UNSAT_WITHOUT_COMPLETE_PROOF_NO_LEARNING"
STATUS_UNSAT_UNCHECKED = "UNSAT_PROOF_GENERATED_UNCHECKED"

SAT_STATUSES = frozenset({STATUS_SAT_WITNESS, STATUS_SAT_ESCALATE})
UNKNOWN_STATUSES = frozenset(
    {
        STATUS_UNKNOWN_WALL,
        STATUS_UNKNOWN_ERROR,
        STATUS_UNKNOWN_SAT,
        STATUS_UNKNOWN_UNSAT,
    }
)

EXPECTED_STATE_MACHINE = {
    "NOT_RUN": "AUGMENTED_CNF_READY_SOLVER_NOT_RUN",
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
EXPECTED_CLAIM_BOUNDARY = (
    "This is one finite CEGAR gate. SAT only authenticates a displayed "
    "model/witness; UNKNOWN learns nothing; a generated UNSAT proof is "
    "unchecked until independent drat-trim replay."
)

_SHA256_RE = re.compile(r"[0-9a-f]{64}\Z", flags=re.ASCII)


@dataclass(frozen=True)
class FrozenProfile:
    runner_basename: str = HISTORICAL_RUNNER_BASENAME
    runner_sha256: str = HISTORICAL_RUNNER_SHA256
    cadical_commit: str = PINNED_CADICAL_COMMIT
    cadical_sha256: str = PINNED_CADICAL_SHA256
    order: int = 100
    independent_target: int = 18
    maximum_variable: int = 154_190
    augmented_cnf_sha256: str = FROZEN_AUGMENTED_CNF_SHA256
    augmented_cnf_bytes: int = FROZEN_AUGMENTED_CNF_BYTES
    augmented_cnf_clauses: int = FROZEN_AUGMENTED_CNF_CLAUSES
    common_cnf_sha256: str = FROZEN_COMMON_CNF_GZIP_SHA256
    common_model_sha256: str = FROZEN_COMMON_MODEL_GZIP_SHA256
    bank_masks: int = 251_771
    bank_ordered_sha256: str = FROZEN_BANK_ORDERED_SHA256
    history_masks: int = 64_591
    history_raw_masks: int = 113_448
    history_sources: int = 18
    history_file_sha256: str = FROZEN_HISTORY_FILE_SHA256
    history_ordered_sha256: str = FROZEN_HISTORY_ORDERED_SHA256
    fixed_base_masks: int = 235_504
    fixed_base_ordered_sha256: str = FROZEN_FIXED_BASE_ORDERED_SHA256
    new_masks: int = 4_096
    mask_batch_file_sha256: str = FROZEN_MASK_BATCH_FILE_SHA256
    mask_batch_ordered_sha256: str = FROZEN_MASK_BATCH_ORDERED_SHA256
    positive_edges: tuple[tuple[int, int], ...] = (
        (11, 62),
        (18, 61),
        (18, 64),
        (18, 69),
    )
    positive_units: tuple[int, ...] = (1085, 1672, 1675, 1680)


PRODUCTION_PROFILE = FrozenProfile()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _is_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def _require_sha256(value: Any, description: str) -> str:
    if not isinstance(value, str) or not _SHA256_RE.fullmatch(value):
        raise AuditError(f"{description} is not a lowercase SHA-256 digest")
    return value


def _exact_keys(record: Any, expected: set[str], description: str) -> Mapping[str, Any]:
    if not isinstance(record, dict) or set(record) != expected:
        raise AuditError(f"{description} fields are not exact")
    return record


def _safe_basename(value: Any, description: str) -> str:
    if (
        not isinstance(value, str)
        or not value
        or value in {".", ".."}
        or Path(value).name != value
    ):
        raise AuditError(f"{description} is not a safe basename")
    return value


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


def _stage_regular(source: Path, destination: Path) -> dict[str, Any]:
    """Copy one non-symlink regular file into a private immutable snapshot."""

    flags = os.O_RDONLY
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        descriptor = os.open(source, flags)
    except OSError as error:
        raise AuditError(f"could not open regular input {source.name}") from error
    digest = hashlib.sha256()
    size = 0
    try:
        opened_stat = os.fstat(descriptor)
        if not stat.S_ISREG(opened_stat.st_mode):
            raise AuditError(f"input is not a regular file: {source.name}")
        with os.fdopen(descriptor, "rb", closefd=False) as opened, destination.open(
            "xb"
        ) as sink:
            while True:
                block = opened.read(1024 * 1024)
                if not block:
                    break
                sink.write(block)
                digest.update(block)
                size += len(block)
            sink.flush()
            os.fsync(sink.fileno())
        closed_stat = os.fstat(descriptor)
        if (
            opened_stat.st_dev,
            opened_stat.st_ino,
            opened_stat.st_size,
            opened_stat.st_mtime_ns,
        ) != (
            closed_stat.st_dev,
            closed_stat.st_ino,
            closed_stat.st_size,
            closed_stat.st_mtime_ns,
        ):
            raise AuditError(f"input changed while staged: {source.name}")
    except Exception:
        destination.unlink(missing_ok=True)
        raise
    finally:
        os.close(descriptor)
    return {"basename": source.name, "bytes": size, "sha256": digest.hexdigest()}


def _require_identity(
    record: Mapping[str, Any],
    *,
    expected_sha256: str,
    description: str,
) -> None:
    _exact_keys(dict(record), {"basename", "bytes", "sha256"}, description)
    _safe_basename(record.get("basename"), f"{description} basename")
    if not _is_int(record.get("bytes")) or record["bytes"] <= 0:
        raise AuditError(f"{description} has an invalid byte count")
    if record.get("sha256") != expected_sha256:
        raise AuditError(f"{description} SHA-256 mismatch")


def _validate_gate_inputs(gate: Mapping[str, Any], profile: FrozenProfile) -> None:
    inputs = _exact_keys(
        gate.get("inputs"),
        {
            "common_cnf",
            "common_model",
            "common_model_audit_status",
            "common_model_assignment_literals",
            "universal_bank",
            "historical_exclusion",
            "fixed_branch1_base_exclusion",
            "new_mask_batch",
        },
        "historical gate inputs",
    )
    _require_identity(
        inputs["common_cnf"],
        expected_sha256=profile.common_cnf_sha256,
        description="historical common CNF input",
    )
    _require_identity(
        inputs["common_model"],
        expected_sha256=profile.common_model_sha256,
        description="historical common model input",
    )
    if inputs.get("common_model_audit_status") != (
        "VERIFIED_BRANCH1_COMMON_RELAXATION_SAT_MODEL"
    ):
        raise AuditError("historical common-model audit status mismatch")
    if inputs.get("common_model_assignment_literals") != profile.maximum_variable:
        raise AuditError("historical common-model literal count mismatch")

    bank = _exact_keys(
        inputs.get("universal_bank"),
        {"basename", "masks", "ordered_masks_sha256"},
        "historical universal-bank input",
    )
    _safe_basename(bank.get("basename"), "universal-bank basename")
    if bank.get("masks") != profile.bank_masks or bank.get(
        "ordered_masks_sha256"
    ) != profile.bank_ordered_sha256:
        raise AuditError("historical universal-bank identity mismatch")

    history = _exact_keys(
        inputs.get("historical_exclusion"),
        {
            "basename",
            "bytes",
            "sha256",
            "masks",
            "ordered_masks_sha256",
            "source_checkpoints",
            "source_raw_masks",
            "within_source_duplicates",
        },
        "historical exclusion input",
    )
    _safe_basename(history.get("basename"), "history-exclusion basename")
    if not _is_int(history.get("bytes")) or history["bytes"] <= 0:
        raise AuditError("historical exclusion byte count is invalid")
    if (
        history.get("sha256") != profile.history_file_sha256
        or history.get("masks") != profile.history_masks
        or history.get("ordered_masks_sha256")
        != profile.history_ordered_sha256
        or history.get("source_checkpoints") != profile.history_sources
        or history.get("source_raw_masks") != profile.history_raw_masks
        or history.get("within_source_duplicates") != 0
    ):
        raise AuditError("historical exclusion identity mismatch")

    fixed = _exact_keys(
        inputs.get("fixed_branch1_base_exclusion"),
        {"masks", "ordered_masks_sha256", "membership_check"},
        "historical fixed-base input",
    )
    if (
        fixed.get("masks") != profile.fixed_base_masks
        or fixed.get("ordered_masks_sha256")
        != profile.fixed_base_ordered_sha256
        or fixed.get("membership_check")
        != (
            "direct pairwise independence test in the authenticated seed with "
            "edge (97,99) removed"
        )
    ):
        raise AuditError("historical fixed-base identity mismatch")

    masks = _exact_keys(
        inputs.get("new_mask_batch"),
        {
            "basename",
            "bytes",
            "sha256",
            "masks",
            "ordered_masks_sha256",
            "canonical_hex_width",
            "all_new_relative_to_three_frozen_exclusion_families",
            "all_independent_in_frozen_model",
            "three_family_overlap_counts",
            "three_family_zero_overlap_verified",
        },
        "historical A+ batch input",
    )
    _safe_basename(masks.get("basename"), "A+ batch basename")
    if not _is_int(masks.get("bytes")) or masks["bytes"] <= 0:
        raise AuditError("historical A+ batch byte count is invalid")
    overlap = _exact_keys(
        masks.get("three_family_overlap_counts"),
        {
            "universal_bank",
            "historical_learned_union",
            "exhaustive_fixed_branch1_base_family",
        },
        "historical A+ overlap record",
    )
    if (
        masks.get("sha256") != profile.mask_batch_file_sha256
        or masks.get("masks") != profile.new_masks
        or masks.get("ordered_masks_sha256")
        != profile.mask_batch_ordered_sha256
        or masks.get("canonical_hex_width") != (profile.order + 3) // 4
        or masks.get("all_new_relative_to_three_frozen_exclusion_families")
        is not True
        or masks.get("all_independent_in_frozen_model") is not True
        or dict(overlap)
        != {
            "universal_bank": 0,
            "historical_learned_union": 0,
            "exhaustive_fixed_branch1_base_family": 0,
        }
        or masks.get("three_family_zero_overlap_verified") is not True
    ):
        raise AuditError("historical A+ batch identity mismatch")


def _validate_augmentation(gate: Mapping[str, Any], profile: FrozenProfile) -> None:
    augmentation = _exact_keys(
        gate.get("augmentation"),
        {"positive_edges", "positive_units", "new_I18_clauses", "augmented_cnf"},
        "historical augmentation",
    )
    if augmentation.get("positive_edges") != [
        list(edge) for edge in profile.positive_edges
    ] or augmentation.get("positive_units") != list(profile.positive_units):
        raise AuditError("historical positive-unit augmentation mismatch")
    if augmentation.get("new_I18_clauses") != profile.new_masks:
        raise AuditError("historical A+ clause count mismatch")
    cnf = _exact_keys(
        augmentation.get("augmented_cnf"),
        {
            "basename",
            "bytes",
            "sha256",
            "variables",
            "clauses",
            "header_and_clause_lines",
            "clause_order",
        },
        "historical augmented CNF record",
    )
    expected = {
        "basename": "branch1_cegar_augmented.cnf",
        "bytes": profile.augmented_cnf_bytes,
        "sha256": profile.augmented_cnf_sha256,
        "variables": profile.maximum_variable,
        "clauses": profile.augmented_cnf_clauses,
        "header_and_clause_lines": profile.augmented_cnf_clauses + 1,
        "clause_order": [
            "frozen_common_clauses",
            "four_proved_positive_units",
            "ordered_new_I18_hitting_clauses",
        ],
    }
    if dict(cnf) != expected:
        raise AuditError("historical augmented CNF record mismatch")


def _validate_checker_record(
    checker: Any, profile: FrozenProfile
) -> dict[str, Any]:
    checker = _exact_keys(
        checker,
        {"basename", "sha256", "source_commit", "source_commit_marker_sha256"},
        "historical CaDiCaL checker record",
    )
    _safe_basename(checker.get("basename"), "CaDiCaL basename")
    marker_sha256 = hashlib.sha256(
        (profile.cadical_commit + "\n").encode("ascii")
    ).hexdigest()
    if (
        checker.get("sha256") != profile.cadical_sha256
        or checker.get("source_commit") != profile.cadical_commit
        or checker.get("source_commit_marker_sha256") != marker_sha256
    ):
        raise AuditError("historical endpoint did not bind the pinned CaDiCaL")
    return dict(checker)


def _validate_solver_record(
    solver: Any,
    *,
    root_status: Any,
    expected_wall_seconds: float,
    profile: FrozenProfile,
) -> tuple[dict[str, Any], dict[str, Any]]:
    if not isinstance(solver, dict):
        raise AuditError("historical solver record is not an object")
    status_value = solver.get("status")
    if status_value != root_status or status_value not in (
        SAT_STATUSES | UNKNOWN_STATUSES | {STATUS_UNSAT_UNCHECKED}
    ):
        raise AuditError("historical root/solver endpoint status mismatch")
    if solver.get("learned_masks") != []:
        raise AuditError("historical endpoint learned or reported masks")

    finished_base = {
        "status",
        "exitcode",
        "wall_limit_seconds",
        "elapsed_seconds",
        "stdout_sha256",
        "stderr_sha256",
        "stdout_tail",
        "stderr_tail",
        "checker",
        "learned_masks",
    }
    if status_value in SAT_STATUSES:
        expected_fields = finished_base | {"model", "model_evaluation", "I18_search"}
    elif status_value == STATUS_UNSAT_UNCHECKED:
        expected_fields = finished_base | {
            "proof",
            "proof_checked_by_drat_trim",
            "unsat_claim_accepted",
        }
    elif status_value == STATUS_UNKNOWN_WALL:
        expected_fields = finished_base - {"stdout_tail", "stderr_tail"}
    elif status_value == STATUS_UNKNOWN_SAT:
        expected_fields = finished_base | {"model_audit_error_type", "model_audit_error"}
    elif status_value == STATUS_UNKNOWN_UNSAT:
        proof_error = {"proof_error_type", "proof_error"}
        reason = {"reason"}
        if set(solver) == finished_base | proof_error:
            expected_fields = finished_base | proof_error
        else:
            expected_fields = finished_base | reason
    else:
        startup = {
            "status",
            "reason",
            "error_type",
            "wall_limit_seconds",
            "elapsed_seconds",
            "checker",
            "learned_masks",
        }
        expected_fields = startup if set(solver) == startup else finished_base | {"reason"}
    _exact_keys(solver, expected_fields, "historical solver endpoint")

    wall = solver.get("wall_limit_seconds")
    elapsed = solver.get("elapsed_seconds")
    if (
        not isinstance(wall, (int, float))
        or isinstance(wall, bool)
        or not math.isfinite(wall)
        or float(wall) != float(expected_wall_seconds)
    ):
        raise AuditError("historical endpoint wall limit mismatch")
    if (
        not isinstance(elapsed, (int, float))
        or isinstance(elapsed, bool)
        or not math.isfinite(elapsed)
        or elapsed < 0
        or elapsed > expected_wall_seconds + max(60.0, expected_wall_seconds * 0.02)
    ):
        raise AuditError("historical endpoint elapsed time is invalid")
    if status_value == STATUS_UNKNOWN_WALL and elapsed < max(
        0.0, expected_wall_seconds - 5.0
    ):
        raise AuditError("historical timeout ended before its recorded wall")

    checker = _validate_checker_record(solver.get("checker"), profile)
    if "exitcode" in solver:
        if not _is_int(solver["exitcode"]):
            raise AuditError("historical endpoint exit code is invalid")
        if status_value in SAT_STATUSES and solver["exitcode"] != 10:
            raise AuditError("historical SAT endpoint lacks exit code 10")
        if status_value == STATUS_UNSAT_UNCHECKED and solver["exitcode"] != 20:
            raise AuditError("historical UNSAT endpoint lacks exit code 20")
        if status_value == STATUS_UNKNOWN_WALL and solver["exitcode"] >= 0:
            raise AuditError("historical timeout endpoint was not killed")
    for key in ("stdout_sha256", "stderr_sha256"):
        if key in solver:
            _require_sha256(solver[key], f"historical {key}")
    for key in ("stdout_tail", "stderr_tail"):
        if key in solver and (
            not isinstance(solver[key], str) or len(solver[key]) > 4000
        ):
            raise AuditError(f"historical {key} is invalid")
    return dict(solver), checker


def _validate_gate(
    gate: dict[str, Any], *, expected_wall_seconds: float, profile: FrozenProfile
) -> tuple[dict[str, Any], dict[str, Any]]:
    _exact_keys(
        gate,
        {
            "schema",
            "status",
            "state_machine",
            "claim_boundary",
            "inputs",
            "augmentation",
            "solver",
            "learned_masks",
            "proof_verified",
            "exact_seven_repair_exists",
            "global_ramsey_implication",
        },
        "historical gate root",
    )
    if gate.get("schema") != GATE_SCHEMA:
        raise AuditError("historical gate schema mismatch")
    if gate.get("state_machine") != EXPECTED_STATE_MACHINE:
        raise AuditError("historical gate state machine mismatch")
    if gate.get("claim_boundary") != EXPECTED_CLAIM_BOUNDARY:
        raise AuditError("historical gate claim boundary mismatch")
    if (
        gate.get("learned_masks") != []
        or gate.get("proof_verified") is not False
        or gate.get("exact_seven_repair_exists") is not None
        or gate.get("global_ramsey_implication") is not None
    ):
        raise AuditError("historical gate crossed its claim boundary")
    _validate_gate_inputs(gate, profile)
    _validate_augmentation(gate, profile)
    return _validate_solver_record(
        gate.get("solver"),
        root_status=gate.get("status"),
        expected_wall_seconds=expected_wall_seconds,
        profile=profile,
    )


def _scan_exact_cnf(path: Path, profile: FrozenProfile) -> dict[str, Any]:
    if path.stat().st_size != profile.augmented_cnf_bytes:
        raise AuditError("augmented CNF byte count mismatch")
    if _sha256_file(path) != profile.augmented_cnf_sha256:
        raise AuditError("augmented CNF SHA-256 mismatch")
    expected_header = (
        f"p cnf {profile.maximum_variable} {profile.augmented_cnf_clauses}\n"
    ).encode("ascii")
    with path.open("rb") as source:
        if source.readline() != expected_header:
            raise AuditError("augmented CNF header mismatch")
        clauses = 0
        last_byte = b""
        while True:
            block = source.read(1024 * 1024)
            if not block:
                break
            if b"\r" in block:
                raise AuditError("augmented CNF contains CR bytes")
            clauses += block.count(b"\n")
            last_byte = block[-1:]
    if clauses != profile.augmented_cnf_clauses or last_byte != b"\n":
        raise AuditError("augmented CNF clause count or termination mismatch")
    return {
        "basename": "branch1_cegar_augmented.cnf",
        "bytes": profile.augmented_cnf_bytes,
        "sha256": profile.augmented_cnf_sha256,
        "variables": profile.maximum_variable,
        "clauses": profile.augmented_cnf_clauses,
        "exact_bytes_rehashed": True,
        "header_and_clause_count_checked": True,
    }


def _gzip_identity(path: Path) -> dict[str, Any]:
    compressed_sha256 = _sha256_file(path)
    raw_digest = hashlib.sha256()
    raw_bytes = 0
    try:
        with gzip.open(path, "rb") as source:
            while True:
                block = source.read(1024 * 1024)
                if not block:
                    break
                raw_digest.update(block)
                raw_bytes += len(block)
    except (OSError, EOFError) as error:
        raise AuditError(f"{path.name} is not a complete gzip stream") from error
    return {
        "basename": path.name,
        "bytes": path.stat().st_size,
        "sha256": compressed_sha256,
        "uncompressed_bytes": raw_bytes,
        "uncompressed_sha256": raw_digest.hexdigest(),
    }


def _recorded_gzip_identity(
    record: Any, actual: Mapping[str, Any], description: str
) -> None:
    _exact_keys(
        record,
        {"basename", "bytes", "sha256", "uncompressed_bytes", "uncompressed_sha256"},
        description,
    )
    for key in ("sha256", "uncompressed_sha256"):
        _require_sha256(record.get(key), f"{description} {key}")
    if dict(record) != dict(actual):
        raise AuditError(f"{description} identity mismatch")


def _direct_graph_audit(
    assignment: Sequence[bool | None], profile: FrozenProfile
) -> dict[str, Any]:
    variables, pairs = lexicographic_edge_variables(profile.order)
    if len(pairs) > profile.maximum_variable:
        raise AuditError("edge-variable map exceeds the DIMACS model")
    rows = [0] * profile.order
    for (u, v), variable in variables.items():
        value = assignment[variable]
        if value is None:
            raise AuditError("graph audit reached an unassigned edge variable")
        if value:
            rows[u] |= 1 << v
            rows[v] |= 1 << u

    triangle: list[int] | None = None
    for u in range(profile.order):
        neighbors = rows[u]
        while neighbors:
            bit = neighbors & -neighbors
            v = bit.bit_length() - 1
            neighbors ^= bit
            common = rows[u] & rows[v]
            if common:
                w = (common & -common).bit_length() - 1
                triangle = sorted((u, v, w))
                break
        if triangle is not None:
            break
    if triangle is not None:
        raise AuditError(f"SAT graph contains triangle {triangle}")

    search = CliqueTargetSearch(
        complement(rows), profile.independent_target
    ).run()
    witness = sorted(search.witness) if search.exists and search.witness else None
    if witness is not None:
        if len(witness) != profile.independent_target or len(set(witness)) != len(
            witness
        ):
            raise AuditError("independent-set checker returned malformed witness")
        for index, u in enumerate(witness):
            for v in witness[index + 1 :]:
                if rows[u] & (1 << v):
                    raise AuditError("independent-set checker returned an edge")
    return {
        "vertices": profile.order,
        "edges": sum(row.bit_count() for row in rows) // 2,
        "triangle_exists": False,
        "independent_target": profile.independent_target,
        "independent_set_exists": search.exists,
        "independent_set_witness": witness,
        "search_nodes": search.recursive_nodes,
        "pairwise_witness_check": witness is not None,
    }


def _validate_recorded_i18(record: Any, graph: Mapping[str, Any], profile: FrozenProfile) -> None:
    if not isinstance(record, dict):
        raise AuditError("historical SAT endpoint lacks an I18 record")
    exists = record.get("independent_set_exists")
    if exists is not graph.get("independent_set_exists"):
        raise AuditError("historical and fresh I18 outcomes disagree")
    if not _is_int(record.get("search_nodes")) or record["search_nodes"] <= 0:
        raise AuditError("historical I18 search-node count is invalid")
    if exists is False:
        _exact_keys(
            record,
            {"independent_set_exists", "witness", "mask_hex", "search_nodes"},
            "historical no-I18 record",
        )
        if record.get("witness") is not None or record.get("mask_hex") is not None:
            raise AuditError("historical no-I18 record contains a witness")
        return
    _exact_keys(
        record,
        {
            "independent_set_exists",
            "witness",
            "mask_hex",
            "search_nodes",
            "pairwise_independence_checked",
            "new_relative_to_all_installed_masks",
            "overlap_with_exclusion_families",
            "known_from_historical_learned_union",
            "known_from_exhaustive_fixed_base_family",
            "new_relative_to_three_frozen_exclusion_families",
            "installed_or_learned_by_this_gate",
        },
        "historical I18-witness record",
    )
    witness = record.get("witness")
    if (
        not isinstance(witness, list)
        or len(witness) != profile.independent_target
        or any(not _is_int(v) or not 0 <= v < profile.order for v in witness)
        or witness != sorted(set(witness))
    ):
        raise AuditError("historical I18 witness is malformed")
    if witness != graph.get("independent_set_witness"):
        raise AuditError("historical I18 witness differs from the fresh graph audit")
    mask = sum(1 << vertex for vertex in witness)
    if record.get("mask_hex") != f"{mask:0{(profile.order + 3) // 4}x}":
        raise AuditError("historical I18 witness mask mismatch")
    overlap = _exact_keys(
        record.get("overlap_with_exclusion_families"),
        {
            "universal_bank",
            "historical_learned_union",
            "exhaustive_fixed_branch1_base_family",
            "new_gate_batch",
        },
        "historical I18 overlap record",
    )
    if any(not isinstance(value, bool) for value in overlap.values()):
        raise AuditError("historical I18 overlap flags are not Boolean")
    if (
        overlap["universal_bank"]
        or overlap["new_gate_batch"]
        or record.get("pairwise_independence_checked") is not True
        or record.get("new_relative_to_all_installed_masks") is not True
        or record.get("installed_or_learned_by_this_gate") is not False
        or record.get("known_from_historical_learned_union")
        is not overlap["historical_learned_union"]
        or record.get("known_from_exhaustive_fixed_base_family")
        is not overlap["exhaustive_fixed_branch1_base_family"]
        or record.get("new_relative_to_three_frozen_exclusion_families")
        is not (
            not overlap["universal_bank"]
            and not overlap["historical_learned_union"]
            and not overlap["exhaustive_fixed_branch1_base_family"]
        )
    ):
        raise AuditError("historical I18 overlap logic is inconsistent")


def _reauthenticate_cadical(
    cadical: Path, private: Path, profile: FrozenProfile
) -> dict[str, Any]:
    staged = _stage_regular(cadical, private / "cadical-rehash")
    marker = cadical.resolve().parent / "SOURCE_COMMIT"
    marker_info = _stage_regular(marker, private / "cadical-SOURCE_COMMIT")
    marker_bytes = (private / "cadical-SOURCE_COMMIT").read_bytes()
    if staged["sha256"] != profile.cadical_sha256:
        raise AuditError("local CaDiCaL copy does not have the pinned SHA-256")
    if marker_bytes != (profile.cadical_commit + "\n").encode("ascii"):
        raise AuditError("local CaDiCaL SOURCE_COMMIT mismatch")
    return {
        "binary": staged,
        "source_commit": profile.cadical_commit,
        "source_commit_marker": marker_info,
        "executed_by_auditor": False,
    }


def audit_endpoint(
    *,
    endpoint_dir: Path,
    historical_runner: Path,
    expected_wall_seconds: float = 3600.0,
    cadical: Path | None = None,
    profile: FrozenProfile = PRODUCTION_PROFILE,
) -> dict[str, Any]:
    """Authenticate one completed historical endpoint without running a solver."""

    if (
        not isinstance(expected_wall_seconds, (int, float))
        or isinstance(expected_wall_seconds, bool)
        or not math.isfinite(expected_wall_seconds)
        or expected_wall_seconds <= 0
    ):
        raise AuditError("expected wall seconds must be finite and positive")
    try:
        directory_stat = endpoint_dir.lstat()
    except OSError as error:
        raise AuditError("endpoint directory is unavailable") from error
    if not stat.S_ISDIR(directory_stat.st_mode) or stat.S_ISLNK(directory_stat.st_mode):
        raise AuditError("endpoint path is not a non-symlink directory")

    with tempfile.TemporaryDirectory(prefix="ramsey-f24-endpoint-audit-") as temporary:
        private = Path(temporary)
        runner_info = _stage_regular(historical_runner, private / "f24-runner.py")
        if (
            runner_info["basename"] != profile.runner_basename
            or runner_info["sha256"] != profile.runner_sha256
        ):
            raise AuditError("historical f24 runner snapshot identity mismatch")

        gate_info = _stage_regular(
            endpoint_dir / "branch1_cegar_gate.json", private / "gate.json"
        )
        gate = _strict_json_bytes((private / "gate.json").read_bytes(), "historical gate")
        solver, checker = _validate_gate(
            gate,
            expected_wall_seconds=expected_wall_seconds,
            profile=profile,
        )

        cnf_info = _stage_regular(
            endpoint_dir / "branch1_cegar_augmented.cnf", private / "augmented.cnf"
        )
        if (
            cnf_info["bytes"] != profile.augmented_cnf_bytes
            or cnf_info["sha256"] != profile.augmented_cnf_sha256
        ):
            raise AuditError("staged augmented CNF identity mismatch")
        exact_cnf = _scan_exact_cnf(private / "augmented.cnf", profile)

        local_checker = (
            _reauthenticate_cadical(cadical, private, profile)
            if cadical is not None
            else None
        )
        status_value = solver["status"]
        result: dict[str, Any] = {
            "schema": AUDIT_SCHEMA,
            "status": "",
            "claim_boundary": (
                "This record audits a historical exploration endpoint. It is "
                "not hardened-runner evidence, learns no masks, and never "
                "promotes UNSAT without fresh DRAT and four-singleton replays."
            ),
            "historical_runner": runner_info,
            "historical_gate_json": gate_info,
            "augmented_cnf": exact_cnf,
            "endpoint": {
                "historical_status": status_value,
                "wall_limit_seconds": solver["wall_limit_seconds"],
                "elapsed_seconds": solver["elapsed_seconds"],
                "exitcode": solver.get("exitcode"),
                "learned_masks": [],
            },
            "cadical_record": checker,
            "local_cadical_rehash": local_checker,
            "solver_executed_by_auditor": False,
            "learned_masks": [],
            "proof_verified": False,
            "sat_claim_accepted": False,
            "unsat_claim_accepted": False,
            "exact_seven_repair_exists": None,
            "global_ramsey_implication": None,
        }

        if status_value in SAT_STATUSES:
            model_record = solver.get("model")
            model_basename = _safe_basename(
                model_record.get("basename") if isinstance(model_record, dict) else None,
                "historical SAT-model basename",
            )
            if model_basename != "branch1_cegar_sat.model.gz":
                raise AuditError("historical SAT-model basename mismatch")
            model_info = _stage_regular(
                endpoint_dir / model_basename, private / "sat.model.gz"
            )
            actual_model = _gzip_identity(private / "sat.model.gz")
            actual_model["basename"] = model_basename
            _recorded_gzip_identity(model_record, actual_model, "historical SAT model")
            if (
                model_info["bytes"] != actual_model["bytes"]
                or model_info["sha256"] != actual_model["sha256"]
            ):
                raise AuditError("staged SAT-model identity changed")
            assignment, parsed_model = parse_complete_model(
                private / "sat.model.gz", profile.maximum_variable
            )
            parsed_identity = {
                key: parsed_model.get(key)
                for key in (
                    "basename",
                    "bytes",
                    "sha256",
                    "uncompressed_bytes",
                    "uncompressed_sha256",
                )
            }
            parsed_identity["basename"] = model_basename
            if (
                parsed_identity != actual_model
                or parsed_model.get("assignment_literals")
                != profile.maximum_variable
                or parsed_model.get("status_line") != "s SATISFIABLE"
            ):
                raise AuditError("independent SAT-model parser identity mismatch")
            evaluation = evaluate_dimacs_model(
                private / "augmented.cnf",
                assignment,
                expected_variables=profile.maximum_variable,
                expected_clauses=profile.augmented_cnf_clauses,
                expected_sha256=profile.augmented_cnf_sha256,
            )
            recorded_evaluation = _exact_keys(
                solver.get("model_evaluation"),
                {"all_clauses_satisfied", "clauses_evaluated"},
                "historical model evaluation",
            )
            if dict(recorded_evaluation) != {
                "all_clauses_satisfied": True,
                "clauses_evaluated": profile.augmented_cnf_clauses,
            }:
                raise AuditError("historical model-evaluation record mismatch")
            graph = _direct_graph_audit(assignment, profile)
            _validate_recorded_i18(solver.get("I18_search"), graph, profile)
            expected_status = (
                STATUS_SAT_WITNESS
                if graph["independent_set_exists"]
                else STATUS_SAT_ESCALATE
            )
            if status_value != expected_status:
                raise AuditError("historical SAT status disagrees with fresh graph audit")
            result.update(
                {
                    "status": (
                        "F24_SAT_REAUDITED_I18_WITNESS_NO_LOWER_BOUND"
                        if graph["independent_set_exists"]
                        else "F24_SAT_REAUDITED_RAMSEY_WITNESS_CANDIDATE"
                    ),
                    "sat_model": actual_model,
                    "full_cnf_evaluation": evaluation,
                    "direct_graph_audit": graph,
                    "sat_claim_accepted": True,
                    "exact_seven_repair_exists": (
                        None if graph["independent_set_exists"] else True
                    ),
                    "global_ramsey_implication": (
                        None
                        if graph["independent_set_exists"]
                        else "CANDIDATE_R_3_18_AT_LEAST_101_REQUIRES_PUBLICATION_PROMOTION"
                    ),
                }
            )
        elif status_value == STATUS_UNSAT_UNCHECKED:
            if (
                solver.get("proof_checked_by_drat_trim") is not False
                or solver.get("unsat_claim_accepted") is not False
            ):
                raise AuditError("historical UNSAT endpoint overstates its proof status")
            proof_record = solver.get("proof")
            proof_basename = _safe_basename(
                proof_record.get("basename") if isinstance(proof_record, dict) else None,
                "historical UNSAT-proof basename",
            )
            if proof_basename != "branch1_cegar_unsat.drat.gz":
                raise AuditError("historical UNSAT-proof basename mismatch")
            proof_info = _stage_regular(
                endpoint_dir / proof_basename, private / "unsat.drat.gz"
            )
            actual_proof = _gzip_identity(private / "unsat.drat.gz")
            actual_proof["basename"] = proof_basename
            _recorded_gzip_identity(
                proof_record, actual_proof, "historical generated UNSAT proof"
            )
            if (
                proof_info["bytes"] != actual_proof["bytes"]
                or proof_info["sha256"] != actual_proof["sha256"]
                or actual_proof["uncompressed_bytes"] <= 0
            ):
                raise AuditError("staged UNSAT-proof identity changed or is empty")
            result.update(
                {
                    "status": "F24_UNSAT_ENDPOINT_AUTHENTICATED_PROMOTION_PENDING",
                    "generated_proof": actual_proof,
                    "promotion": {
                        "status": "BLOCKED_PENDING_FRESH_INDEPENDENT_REPLAYS",
                        "proof_gzip_sha256": actual_proof["sha256"],
                        "proof_raw_sha256": actual_proof["uncompressed_sha256"],
                        "required": [
                            "fresh drat-trim replay of this exact proof against this exact augmented CNF",
                            "fresh replay of singleton implications K_a, K_b, K_c, K_d",
                        ],
                        "scoped_unsat_claim_accepted": False,
                        "global_ramsey_implication": None,
                    },
                }
            )
        else:
            result.update(
                {
                    "status": "F24_UNKNOWN_ENDPOINT_AUTHENTICATED_NO_CLAIM",
                    "unknown_boundary": (
                        "The exact bounded endpoint and its pinned-checker record "
                        "are authenticated; no SAT/UNSAT result and no learned cut "
                        "is accepted."
                    ),
                }
            )
        return result


def _write_new_json(path: Path, payload: Mapping[str, Any]) -> None:
    rendered = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    if path.exists():
        raise FileExistsError(f"refusing to overwrite {path.name}")
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        with temporary.open("xb") as sink:
            sink.write(rendered)
            sink.flush()
            os.fsync(sink.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def main(argv: Sequence[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--endpoint-dir", type=Path, required=True)
    parser.add_argument(
        "--historical-runner",
        type=Path,
        default=here / HISTORICAL_RUNNER_BASENAME,
    )
    parser.add_argument("--expected-wall-seconds", type=float, default=3600.0)
    parser.add_argument("--cadical", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    try:
        result = audit_endpoint(
            endpoint_dir=args.endpoint_dir.resolve(),
            historical_runner=args.historical_runner.resolve(),
            expected_wall_seconds=args.expected_wall_seconds,
            cadical=args.cadical.resolve() if args.cadical else None,
        )
        if args.output is not None:
            _write_new_json(args.output.resolve(), result)
    except Exception as error:
        failure = {
            "schema": AUDIT_SCHEMA,
            "status": "FAILED_CLOSED",
            "error_type": type(error).__name__,
            "error": str(error),
            "solver_executed_by_auditor": False,
            "learned_masks": [],
            "proof_verified": False,
            "sat_claim_accepted": False,
            "unsat_claim_accepted": False,
        }
        print(json.dumps(failure, sort_keys=True), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
