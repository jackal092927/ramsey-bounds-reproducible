#!/usr/bin/env python3
"""Fail-closed replay of the frozen branch-1 generalized-core proofs.

The tracked proof summary is the only record index used by this auditor.  For
every final record it binds the canonical core and its negative DIMACS units
to two explicitly named, content-addressed assets.  It then:

1. invokes the independent, PySAT-free production CNF reconstruction audit;
2. decompresses the authenticated CNF and DRAT into a record-specific
   temporary directory; and
3. accepts the proof only when a fresh ``drat-trim`` process exits zero and
   writes an exact, standalone ``s VERIFIED`` line to standard output.

No historical ``proof_verified`` bit or transcript is accepted in place of
the fresh replay.  Missing, aliased, swapped, truncated, or malformed assets;
timeouts; noncanonical cores or units; duplicate records; non-antichain core
families; and any minimality or global-Ramsey implication all fail closed.
"""

from __future__ import annotations

import argparse
import errno
import gzip
import hashlib
import json
import math
import os
import re
import secrets
import stat
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence

try:
    from .check_r3_18_budget7_branch1_core_cnf import (
        AuditError,
        EXPECTED_FORMULA_FINGERPRINT,
        PRODUCTION_COMMON_CLAUSES,
        PRODUCTION_MAXIMUM_VARIABLE,
        PRODUCTION_ORDER,
        audit_production_cnf,
        lexicographic_edge_variables,
    )
except ImportError:  # pragma: no cover - direct script execution
    from check_r3_18_budget7_branch1_core_cnf import (
        AuditError,
        EXPECTED_FORMULA_FINGERPRINT,
        PRODUCTION_COMMON_CLAUSES,
        PRODUCTION_MAXIMUM_VARIABLE,
        PRODUCTION_ORDER,
        audit_production_cnf,
        lexicographic_edge_variables,
    )


Edge = tuple[int, int]

SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch1-core-proof-replay-v1"
SUMMARY_SCHEMA = (
    "ramsey-r3-18-n100-exact-budget7-branch1-core-proof-summary-v1"
)
EXPECTED_SUMMARY_STATUS = (
    "FOUR_SINGLETON_NO_GOODS_PROOF_VERIFIED_EXACT_SEVEN_UNKNOWN"
)
# This digest is deliberately a publication freeze point, not a value derived
# from the summary at runtime.  Any change to the final record family requires
# a review and an explicit update here.
EXPECTED_SUMMARY_SHA256 = (
    "8ae4f0d9ea919c915ba642eb03ec3d418b4419a89781377509acbe925d89555a"
)
CNF_AUDIT_STATUS = "VERIFIED_INDEPENDENT_CNF_RECONSTRUCTION"
PINNED_DRAT_TRIM_COMMIT = "2e3b2dc0ecf938addbd779d42877b6ed69d9a985"

_SAFE_LABEL = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,63}\Z")
_SAFE_ASSET = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,191}\Z")
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")


@dataclass(frozen=True)
class CoreRecord:
    label: str
    edges: tuple[Edge, ...]
    assumption_units: tuple[int, ...]
    candidate_sha256: str
    cnf_asset: str
    cnf_gzip_bytes: int
    cnf_gzip_sha256: str
    cnf_uncompressed_sha256: str
    proof_asset: str
    proof_gzip_bytes: int
    proof_gzip_sha256: str
    independent_cnf_audit_sha256: str


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _canonical_sha256(payload: Any) -> str:
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise AuditError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_nonfinite_json(value: str) -> None:
    raise AuditError(f"non-finite JSON number: {value}")


def _parse_strict_json_bytes(raw: bytes) -> dict[str, Any]:
    try:
        text = raw.decode("utf-8")
        payload = json.loads(
            text,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite_json,
        )
    except AuditError:
        raise
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise AuditError("summary is unreadable or invalid strict JSON") from error
    if not isinstance(payload, dict):
        raise AuditError("summary root is not a JSON object")
    return payload


def _read_strict_json(path: Path) -> dict[str, Any]:
    if not path.is_file():
        raise AuditError(f"summary is not a regular file: {path}")
    try:
        raw = path.read_bytes()
    except OSError as error:
        raise AuditError("summary is unreadable") from error
    return _parse_strict_json_bytes(raw)


def _load_frozen_summary(
    path: Path, expected_sha256: str
) -> tuple[dict[str, Any], str]:
    """Read the summary once; hash and parse exactly that in-memory snapshot."""

    if not path.is_file():
        raise AuditError(f"summary is not a regular file: {path}")
    try:
        raw = path.read_bytes()
    except OSError as error:
        raise AuditError("summary is unreadable") from error
    digest = hashlib.sha256(raw).hexdigest()
    if digest != expected_sha256:
        raise AuditError("core-proof summary SHA-256 differs from the frozen value")
    return _parse_strict_json_bytes(raw), digest


def _require_mapping(value: Any, description: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise AuditError(f"{description} is not a JSON object")
    return value


def _strict_positive_integer(value: Any, description: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        raise AuditError(f"{description} is not a positive integer")
    return value


def _strict_sha256(value: Any, description: str) -> str:
    if not isinstance(value, str) or not _SHA256.fullmatch(value):
        raise AuditError(f"{description} is not a lowercase hexadecimal SHA-256")
    return value


def _strict_asset_name(value: Any, description: str, suffix: str) -> str:
    if (
        not isinstance(value, str)
        or not _SAFE_ASSET.fullmatch(value)
        or ".." in value
        or Path(value).name != value
        or not value.endswith(suffix)
    ):
        raise AuditError(f"{description} is not a safe {suffix} asset basename")
    return value


def _strict_edges(value: Any, label: str) -> tuple[Edge, ...]:
    if not isinstance(value, list) or not value:
        raise AuditError(f"record {label} has no deletion-edge list")
    edges: list[Edge] = []
    for raw in value:
        if not isinstance(raw, list) or len(raw) != 2:
            raise AuditError(f"record {label} contains a malformed edge")
        u, v = raw
        if any(not isinstance(x, int) or isinstance(x, bool) for x in (u, v)):
            raise AuditError(f"record {label} has a non-integer edge endpoint")
        if not (0 <= u < v < PRODUCTION_ORDER):
            raise AuditError(f"record {label} has a noncanonical edge")
        edges.append((u, v))
    if len(edges) > 6:
        raise AuditError(f"record {label} exceeds the exact-six residual budget")
    if edges != sorted(edges) or len(edges) != len(set(edges)):
        raise AuditError(f"record {label} edges are not sorted and unique")
    return tuple(edges)


def _expected_candidate_identity(
    edges: Sequence[Edge], variables: dict[Edge, int]
) -> tuple[tuple[int, ...], str]:
    units = tuple(-variables[edge] for edge in edges)
    identity = {
        "formula_fingerprint_sha256": EXPECTED_FORMULA_FINGERPRINT,
        "deletion_edges": [list(edge) for edge in edges],
        "assumption_units": list(units),
        "semantics": "for every e in K, d_e=true is encoded as unit -x_e",
    }
    return units, _canonical_sha256(identity)


def _strict_record(
    raw: Any, variables: dict[Edge, int]
) -> CoreRecord:
    record = _require_mapping(raw, "summary record")
    label = record.get("label")
    if (
        not isinstance(label, str)
        or not _SAFE_LABEL.fullmatch(label)
        or ".." in label
    ):
        raise AuditError("record label is not a safe canonical label")
    edges = _strict_edges(record.get("deletion_edges"), label)
    expected_units, expected_candidate_sha256 = _expected_candidate_identity(
        edges, variables
    )
    raw_units = record.get("assumption_units")
    if (
        not isinstance(raw_units, list)
        or any(
            not isinstance(unit, int) or isinstance(unit, bool)
            for unit in raw_units
        )
        or tuple(raw_units) != expected_units
    ):
        raise AuditError(f"record {label} has noncanonical deletion units")
    if any(unit >= 0 for unit in raw_units) or len(raw_units) != len(set(raw_units)):
        raise AuditError(f"record {label} deletion units have invalid polarity")
    candidate_sha256 = _strict_sha256(
        record.get("candidate_sha256"), f"record {label} candidate digest"
    )
    if candidate_sha256 != expected_candidate_sha256:
        raise AuditError(f"record {label} candidate identity mismatch")
    if record.get("proof_verified") is not True:
        raise AuditError(f"record {label} proof bit is not exactly true")
    if "minimality_claim" in record and record.get("minimality_claim") is not False:
        raise AuditError(f"record {label} improperly claims minimality")
    if (
        "global_ramsey_implication" in record
        and record.get("global_ramsey_implication") is not None
    ):
        raise AuditError(f"record {label} improperly claims a global implication")

    cnf_asset = _strict_asset_name(
        record.get("cnf_asset"), f"record {label} CNF asset", ".cnf.gz"
    )
    proof_asset = _strict_asset_name(
        record.get("proof_asset"), f"record {label} proof asset", ".drat.gz"
    )
    if not cnf_asset.startswith("branch1_core_") or not proof_asset.startswith(
        "branch1_core_"
    ):
        raise AuditError(f"record {label} asset is outside the branch1_core namespace")
    if cnf_asset == proof_asset:
        raise AuditError(f"record {label} reuses one asset for CNF and proof")
    return CoreRecord(
        label=label,
        edges=edges,
        assumption_units=expected_units,
        candidate_sha256=candidate_sha256,
        cnf_asset=cnf_asset,
        cnf_gzip_bytes=_strict_positive_integer(
            record.get("cnf_gzip_bytes"), f"record {label} CNF byte count"
        ),
        cnf_gzip_sha256=_strict_sha256(
            record.get("cnf_gzip_sha256"), f"record {label} CNF digest"
        ),
        cnf_uncompressed_sha256=_strict_sha256(
            record.get("cnf_uncompressed_sha256"),
            f"record {label} raw CNF digest",
        ),
        proof_asset=proof_asset,
        proof_gzip_bytes=_strict_positive_integer(
            record.get("proof_gzip_bytes"), f"record {label} proof byte count"
        ),
        proof_gzip_sha256=_strict_sha256(
            record.get("proof_gzip_sha256"), f"record {label} proof digest"
        ),
        independent_cnf_audit_sha256=_strict_sha256(
            record.get("independent_cnf_audit_sha256"),
            f"record {label} prior independent-audit digest",
        ),
    )


def validate_summary(payload: dict[str, Any]) -> tuple[CoreRecord, ...]:
    """Validate final records without assuming their count or labels."""

    if payload.get("schema") != SUMMARY_SCHEMA:
        raise AuditError("core-proof summary schema mismatch")
    if payload.get("status") != EXPECTED_SUMMARY_STATUS:
        raise AuditError("core-proof summary status mismatch")
    if payload.get("minimality_claim") is not False:
        raise AuditError("core-proof summary improperly claims minimality")
    if payload.get("global_ramsey_implication") is not None:
        raise AuditError("core-proof summary improperly claims a global implication")
    if (
        "exact_seven_repair_exists" in payload
        and payload.get("exact_seven_repair_exists") is not None
    ):
        raise AuditError("core-proof summary improperly resolves exact seven")

    common = _require_mapping(payload.get("common_formula"), "common formula")
    expected_common = {
        "formula_fingerprint_sha256": EXPECTED_FORMULA_FINGERPRINT,
        "maximum_variable": PRODUCTION_MAXIMUM_VARIABLE,
        "clauses_before_candidate_units": PRODUCTION_COMMON_CLAUSES,
        "original_nonedge_variables_in_deletion_counter": 0,
    }
    for key, value in expected_common.items():
        if common.get(key) != value:
            raise AuditError(f"common-formula {key} mismatch")

    toolchains = _require_mapping(payload.get("external_toolchains"), "toolchains")
    allowed_checker_hashes: set[str] = set()
    for key in ("drat_trim", "independent_arm64_drat_trim"):
        recorded_checker = _require_mapping(toolchains.get(key), key)
        if recorded_checker.get("source_commit") != PINNED_DRAT_TRIM_COMMIT:
            raise AuditError(f"recorded {key} source commit mismatch")
        allowed_checker_hashes.add(
            _strict_sha256(
                recorded_checker.get("binary_sha256"),
                f"recorded {key} binary digest",
            )
        )
    if len(allowed_checker_hashes) != 2:
        raise AuditError("recorded drat-trim binary allowlist contains a duplicate")

    semantic_checker = _require_mapping(
        payload.get("independent_cnf_checker"), "independent CNF checker"
    )
    semantic_script = Path(__file__).resolve().with_name(
        "check_r3_18_budget7_branch1_core_cnf.py"
    )
    if semantic_checker.get("script") != (
        "routes/finite/check_r3_18_budget7_branch1_core_cnf.py"
    ):
        raise AuditError("independent CNF checker path mismatch")
    if semantic_checker.get("script_sha256") != _sha256_file(semantic_script):
        raise AuditError("independent CNF checker digest mismatch")
    if semantic_checker.get("pysat_imported") is not False:
        raise AuditError("summary does not record a PySAT-free checker")
    if semantic_checker.get("production_formula_builder_imported") is not False:
        raise AuditError("summary checker imports the production formula builder")

    raw_records = payload.get("records")
    if not isinstance(raw_records, list) or not raw_records:
        raise AuditError("core-proof summary has no final records")
    variables, _ = lexicographic_edge_variables(PRODUCTION_ORDER)
    records = tuple(_strict_record(raw, variables) for raw in raw_records)

    labels: set[str] = set()
    asset_names: set[str] = set()
    asset_identities: set[tuple[int, str]] = set()
    for record in records:
        if record.label in labels:
            raise AuditError(f"duplicate record label: {record.label}")
        labels.add(record.label)
        for name, size, digest in (
            (record.cnf_asset, record.cnf_gzip_bytes, record.cnf_gzip_sha256),
            (record.proof_asset, record.proof_gzip_bytes, record.proof_gzip_sha256),
        ):
            if name in asset_names:
                raise AuditError(f"duplicate asset basename: {name}")
            asset_names.add(name)
            identity = (size, digest)
            if identity in asset_identities:
                raise AuditError("duplicate content-addressed asset identity")
            asset_identities.add(identity)

    for left_index, left in enumerate(records):
        left_edges = frozenset(left.edges)
        for right in records[left_index + 1 :]:
            right_edges = frozenset(right.edges)
            if left_edges.issubset(right_edges) or right_edges.issubset(left_edges):
                raise AuditError(
                    f"final core family is not an antichain: "
                    f"{left.label}, {right.label}"
                )
    return records


def _stage_authenticated_file(
    source: Path,
    destination: Path,
    *,
    expected_bytes: int | None,
    expected_sha256: str | None,
    description: str,
) -> dict[str, Any]:
    """Copy one opened source stream and authenticate the staged bytes."""

    if not source.is_file():
        raise AuditError(f"missing {description}: {source.name}")
    digest = hashlib.sha256()
    size = 0
    try:
        with source.open("rb") as input_stream, destination.open("xb") as sink:
            while True:
                block = input_stream.read(1024 * 1024)
                if not block:
                    break
                sink.write(block)
                digest.update(block)
                size += len(block)
            sink.flush()
            os.fsync(sink.fileno())
    except OSError as error:
        if destination.exists():
            destination.unlink()
        raise AuditError(f"could not stage {description}: {source.name}") from error
    actual_sha256 = digest.hexdigest()
    if expected_bytes is not None and size != expected_bytes:
        destination.unlink(missing_ok=True)
        raise AuditError(f"asset byte count mismatch: {source.name}")
    if expected_sha256 is not None and actual_sha256 != expected_sha256:
        destination.unlink(missing_ok=True)
        raise AuditError(f"asset SHA-256 mismatch: {source.name}")
    return {"bytes": size, "sha256": actual_sha256}


def _decompress_gzip(source: Path, destination: Path) -> dict[str, Any]:
    digest = hashlib.sha256()
    size = 0
    try:
        with gzip.open(source, "rb") as compressed, destination.open("xb") as sink:
            while True:
                block = compressed.read(1024 * 1024)
                if not block:
                    break
                sink.write(block)
                digest.update(block)
                size += len(block)
            sink.flush()
            os.fsync(sink.fileno())
    except (OSError, EOFError, gzip.BadGzipFile) as error:
        if destination.exists():
            destination.unlink()
        raise AuditError(f"invalid or incomplete gzip asset: {source.name}") from error
    if size == 0:
        raise AuditError(f"decompressed asset is empty: {source.name}")
    return {"bytes": size, "sha256": digest.hexdigest()}


class _DigestingReader:
    """Minimal sequential file wrapper that hashes exactly the bytes read."""

    def __init__(self, source: Any) -> None:
        self.source = source
        self.digest = hashlib.sha256()
        self.bytes = 0

    def read(self, size: int = -1) -> bytes:
        block = self.source.read(size)
        self.digest.update(block)
        self.bytes += len(block)
        return block

    def readable(self) -> bool:
        return True

    def seekable(self) -> bool:
        return False


def _decompress_authenticated_gzip(
    source: Path,
    destination: Path,
    *,
    expected_gzip_bytes: int,
    expected_gzip_sha256: str,
    description: str,
) -> dict[str, Any]:
    """Authenticate compressed bytes while creating one private raw snapshot."""

    if not source.is_file():
        raise AuditError(f"missing {description}: {source.name}")
    raw_digest = hashlib.sha256()
    raw_bytes = 0
    try:
        with source.open("rb") as source_file, destination.open("xb") as sink:
            digesting = _DigestingReader(source_file)
            with gzip.GzipFile(fileobj=digesting, mode="rb") as compressed:
                while True:
                    block = compressed.read(1024 * 1024)
                    if not block:
                        break
                    sink.write(block)
                    raw_digest.update(block)
                    raw_bytes += len(block)
            # Count any bytes not consumed by gzip itself.  A valid complete
            # member normally leaves none, but the content-addressed identity
            # is always over the entire opened source stream.
            while digesting.read(1024 * 1024):
                pass
            sink.flush()
            os.fsync(sink.fileno())
    except (OSError, EOFError, gzip.BadGzipFile) as error:
        destination.unlink(missing_ok=True)
        raise AuditError(f"invalid or incomplete gzip asset: {source.name}") from error
    if digesting.bytes != expected_gzip_bytes:
        destination.unlink(missing_ok=True)
        raise AuditError(f"asset byte count mismatch: {source.name}")
    if digesting.digest.hexdigest() != expected_gzip_sha256:
        destination.unlink(missing_ok=True)
        raise AuditError(f"asset SHA-256 mismatch: {source.name}")
    if raw_bytes == 0:
        destination.unlink(missing_ok=True)
        raise AuditError(f"decompressed asset is empty: {source.name}")
    return {"bytes": raw_bytes, "sha256": raw_digest.hexdigest()}


def replay_drat(
    drat_trim: Path,
    cnf_path: Path,
    proof_path: Path,
    timeout_seconds: float,
) -> dict[str, Any]:
    if not drat_trim.is_file() or not os.access(drat_trim, os.X_OK):
        raise AuditError(f"drat-trim is not executable: {drat_trim}")
    if (
        not isinstance(timeout_seconds, (int, float))
        or isinstance(timeout_seconds, bool)
        or not math.isfinite(timeout_seconds)
        or timeout_seconds <= 0
    ):
        raise AuditError("DRAT replay timeout must be finite and positive")
    started = time.monotonic()
    environment = {
        key: value
        for key, value in os.environ.items()
        if not key.startswith(("LD_", "DYLD_", "LDR_"))
        and key not in {"GCONV_PATH", "LIBPATH", "SHLIB_PATH"}
    }
    environment["LC_ALL"] = "C"
    environment["LANG"] = "C"
    try:
        completed = subprocess.run(
            [str(drat_trim), str(cnf_path), str(proof_path)],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=environment,
            timeout=timeout_seconds,
            check=False,
        )
    except subprocess.TimeoutExpired as error:
        raise AuditError("drat-trim timed out") from error
    except OSError as error:
        raise AuditError("drat-trim could not be executed") from error
    elapsed = time.monotonic() - started
    verified_lines = [
        line for line in completed.stdout.splitlines() if line == "s VERIFIED"
    ]
    if completed.returncode != 0:
        raise AuditError(f"drat-trim exited nonzero: {completed.returncode}")
    if len(verified_lines) != 1:
        raise AuditError("drat-trim did not emit exactly one standalone s VERIFIED line")
    return {
        "status": "VERIFIED",
        "exitcode": 0,
        "elapsed_seconds": elapsed,
        "stdout_sha256": hashlib.sha256(completed.stdout.encode("utf-8")).hexdigest(),
        "stderr_sha256": hashlib.sha256(completed.stderr.encode("utf-8")).hexdigest(),
    }


def _allowed_checker_hashes(payload: dict[str, Any]) -> frozenset[str]:
    toolchains = _require_mapping(payload.get("external_toolchains"), "toolchains")
    return frozenset(
        _strict_sha256(
            _require_mapping(toolchains.get(key), key).get("binary_sha256"),
            f"recorded {key} binary digest",
        )
        for key in ("drat_trim", "independent_arm64_drat_trim")
    )


def stage_runtime_checker(
    drat_trim: Path,
    staged_checker: Path,
    expected_source_commit: str,
    allowed_binary_sha256: frozenset[str],
) -> dict[str, str]:
    """Snapshot and bind the checker to a pinned binary and source revision."""

    if not drat_trim.is_file() or not os.access(drat_trim, os.X_OK):
        raise AuditError(f"drat-trim is not executable: {drat_trim}")
    marker = drat_trim.resolve().parent / "SOURCE_COMMIT"
    if not marker.is_file():
        raise AuditError("drat-trim lacks an adjacent SOURCE_COMMIT marker")
    try:
        marker_bytes = marker.read_bytes()
    except OSError as error:
        raise AuditError("drat-trim SOURCE_COMMIT is unreadable") from error
    if marker_bytes != (expected_source_commit + "\n").encode("ascii"):
        raise AuditError("drat-trim SOURCE_COMMIT mismatch")
    staged = _stage_authenticated_file(
        drat_trim,
        staged_checker,
        expected_bytes=None,
        expected_sha256=None,
        description="drat-trim executable",
    )
    binary_sha256 = staged["sha256"]
    if binary_sha256 not in allowed_binary_sha256:
        staged_checker.unlink(missing_ok=True)
        raise AuditError("drat-trim binary SHA-256 is outside the frozen allowlist")
    staged_checker.chmod(0o700)
    if _sha256_file(staged_checker) != binary_sha256:
        raise AuditError("staged drat-trim changed after authentication")
    return {
        "basename": drat_trim.name,
        "sha256": binary_sha256,
        "source_commit": expected_source_commit,
        "source_commit_marker_sha256": hashlib.sha256(marker_bytes).hexdigest(),
    }


def _validate_semantic_audit(
    audit: Any, record: CoreRecord, cnf_path: Path
) -> None:
    result = _require_mapping(audit, f"record {record.label} semantic audit")
    if result.get("status") != CNF_AUDIT_STATUS:
        raise AuditError(f"record {record.label} CNF semantic audit did not verify")
    candidate = _require_mapping(result.get("candidate"), "semantic-audit candidate")
    if candidate != {
        "label": record.label,
        "deletion_edges": [list(edge) for edge in record.edges],
        "assumption_units": list(record.assumption_units),
        "candidate_sha256": record.candidate_sha256,
    }:
        raise AuditError(f"record {record.label} semantic-audit candidate mismatch")
    cnf = _require_mapping(result.get("cnf"), "semantic-audit CNF")
    if (
        cnf.get("basename") != record.cnf_asset
        or cnf.get("bytes") != record.cnf_gzip_bytes
        or cnf.get("sha256") != record.cnf_gzip_sha256
        or cnf.get("uncompressed_sha256") != record.cnf_uncompressed_sha256
        or cnf_path.name != record.cnf_asset
    ):
        raise AuditError(f"record {record.label} semantic-audit asset mismatch")


def _audit_one_record(
    *,
    record: CoreRecord,
    artifact_dir: Path,
    matrix_path: Path,
    bank_path: Path,
    staged_checker: Path,
    timeout_seconds: float,
) -> dict[str, Any]:
    """Stage, semantically reconstruct, decompress, and replay one record."""

    source_cnf = artifact_dir / record.cnf_asset
    source_proof = artifact_dir / record.proof_asset
    with tempfile.TemporaryDirectory(
        prefix=f"ramsey-core-proof-{record.label}-"
    ) as temporary:
        record_dir = Path(temporary)
        staged_cnf = record_dir / record.cnf_asset
        raw_cnf = record_dir / "formula.cnf"
        raw_proof = record_dir / "proof.drat"
        _stage_authenticated_file(
            source_cnf,
            staged_cnf,
            expected_bytes=record.cnf_gzip_bytes,
            expected_sha256=record.cnf_gzip_sha256,
            description="CNF asset",
        )
        proof_raw = _decompress_authenticated_gzip(
            source_proof,
            raw_proof,
            expected_gzip_bytes=record.proof_gzip_bytes,
            expected_gzip_sha256=record.proof_gzip_sha256,
            description="DRAT asset",
        )

        semantic = audit_production_cnf(
            cnf_path=staged_cnf,
            matrix_path=matrix_path,
            bank_path=bank_path,
            label=record.label,
            raw_core=record.edges,
            expected_raw_sha256=record.cnf_uncompressed_sha256,
            expected_gzip_sha256=record.cnf_gzip_sha256,
        )
        _validate_semantic_audit(semantic, record, staged_cnf)

        cnf_raw = _decompress_gzip(staged_cnf, raw_cnf)
        if cnf_raw["sha256"] != record.cnf_uncompressed_sha256:
            raise AuditError(f"record {record.label} raw CNF digest mismatch")
        staged_cnf.unlink()
        replay = replay_drat(
            staged_checker, raw_cnf, raw_proof, timeout_seconds
        )

    return {
        "label": record.label,
        "deletion_edges": [list(edge) for edge in record.edges],
        "candidate_sha256": record.candidate_sha256,
        "cnf_asset": record.cnf_asset,
        "cnf_gzip_sha256": record.cnf_gzip_sha256,
        "cnf_uncompressed_sha256": record.cnf_uncompressed_sha256,
        "proof_asset": record.proof_asset,
        "proof_gzip_sha256": record.proof_gzip_sha256,
        "proof_uncompressed_sha256": proof_raw["sha256"],
        "proof_uncompressed_bytes": proof_raw["bytes"],
        "semantic_reconstruction": CNF_AUDIT_STATUS,
        "historical_independent_cnf_audit_sha256": (
            record.independent_cnf_audit_sha256
        ),
        "fresh_independent_cnf_audit_canonical_sha256": (
            _canonical_sha256(semantic)
        ),
        "drat_replay": replay,
    }


def audit_core_proofs(
    *,
    summary_path: Path,
    artifact_dir: Path,
    matrix_path: Path,
    bank_path: Path,
    drat_trim: Path,
    timeout_seconds: float,
) -> dict[str, Any]:
    """Authenticate and replay every final record, returning only on success."""

    payload, summary_digest = _load_frozen_summary(
        summary_path, EXPECTED_SUMMARY_SHA256
    )
    records = validate_summary(payload)
    if not artifact_dir.is_dir():
        raise AuditError(f"artifact directory does not exist: {artifact_dir}")
    recorded_toolchain = _require_mapping(
        _require_mapping(payload.get("external_toolchains"), "toolchains").get(
            "drat_trim"
        ),
        "drat-trim",
    )
    resolved_assets: set[Path] = set()
    declared_asset_names = {
        name
        for record in records
        for name in (record.cnf_asset, record.proof_asset)
    }
    for record in records:
        for asset_name in (record.cnf_asset, record.proof_asset):
            resolved = (artifact_dir / asset_name).resolve()
            if resolved in resolved_assets:
                raise AuditError("two declared assets resolve to the same file")
            resolved_assets.add(resolved)
    unexpected_core_assets = {
        child.name
        for child in artifact_dir.iterdir()
        if child.name.startswith("branch1_core_")
        and child.name.endswith((".cnf.gz", ".drat.gz"))
        and child.name not in declared_asset_names
    }
    if unexpected_core_assets:
        raise AuditError(
            "artifact directory contains undeclared branch1-core assets: "
            + ", ".join(sorted(unexpected_core_assets))
        )

    with tempfile.TemporaryDirectory(prefix="ramsey-core-checker-") as checker_tmp:
        staged_checker = Path(checker_tmp) / "drat-trim"
        checker_identity = stage_runtime_checker(
            drat_trim,
            staged_checker,
            recorded_toolchain["source_commit"],
            _allowed_checker_hashes(payload),
        )
        checked = [
            _audit_one_record(
                record=record,
                artifact_dir=artifact_dir,
                matrix_path=matrix_path,
                bank_path=bank_path,
                staged_checker=staged_checker,
                timeout_seconds=timeout_seconds,
            )
            for record in records
        ]

    return {
        "schema": SCHEMA,
        "status": "ALL_FINAL_BRANCH1_CORE_PROOFS_REPLAYED",
        "records_verified": len(checked),
        "assets_verified": 2 * len(checked),
        "summary": {
            "basename": summary_path.name,
            "sha256": summary_digest,
        },
        "checker": checker_identity,
        "records": checked,
        "minimality_claim": False,
        "global_ramsey_implication": None,
        "exact_seven_repair_exists": None,
    }


@dataclass
class StableJsonOutput:
    """An output basename anchored to one preflight-authenticated directory.

    The directory file descriptor stays open across the expensive audit.  A
    hostile rename or symlink replacement of the user-facing parent path can
    therefore neither redirect the final write nor overwrite an authenticated
    input.  The final component is always replaced as a directory entry; it is
    never followed as a symlink.
    """

    directory_fd: int
    basename: str
    display_path: Path
    overwrite: bool

    @classmethod
    def open(
        cls,
        path: Path,
        *,
        protected: set[Path],
        overwrite: bool,
    ) -> "StableJsonOutput":
        basename = path.name
        if not basename or basename in {".", ".."}:
            raise AuditError("JSON output has no safe file basename")

        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            resolved_parent = path.parent.resolve(strict=True)
        except OSError as error:
            raise AuditError("JSON output parent could not be prepared") from error
        if not resolved_parent.is_dir():
            raise AuditError("JSON output parent is not a directory")

        flags = os.O_RDONLY
        flags |= getattr(os, "O_DIRECTORY", 0)
        flags |= getattr(os, "O_CLOEXEC", 0)
        flags |= getattr(os, "O_NOFOLLOW", 0)
        try:
            directory_fd = os.open(resolved_parent, flags)
        except OSError as error:
            raise AuditError("JSON output parent could not be opened safely") from error

        try:
            opened = os.fstat(directory_fd)
            current = os.stat(resolved_parent, follow_symlinks=False)
            if (
                not stat.S_ISDIR(opened.st_mode)
                or not stat.S_ISDIR(current.st_mode)
                or (opened.st_dev, opened.st_ino) != (current.st_dev, current.st_ino)
            ):
                raise AuditError("JSON output parent changed during preflight")

            # Check both the stable lexical destination and any pre-existing
            # final-component symlink.  Once this check finishes, writes use
            # rename/link relative to directory_fd and never follow that entry.
            lexical_target = resolved_parent / basename
            followed_target = lexical_target.resolve(strict=False)
            if lexical_target in protected or followed_target in protected:
                raise AuditError(
                    "JSON output collides with an authenticated replay input"
                )

            if not overwrite:
                try:
                    os.stat(basename, dir_fd=directory_fd, follow_symlinks=False)
                except FileNotFoundError:
                    pass
                except OSError as error:
                    raise AuditError("JSON output target could not be inspected") from error
                else:
                    raise FileExistsError(f"refusing to overwrite {basename}")
        except Exception:
            os.close(directory_fd)
            raise

        return cls(
            directory_fd=directory_fd,
            basename=basename,
            display_path=lexical_target,
            overwrite=overwrite,
        )

    def close(self) -> None:
        if self.directory_fd >= 0:
            os.close(self.directory_fd)
            self.directory_fd = -1

    def write(self, payload: dict[str, Any]) -> None:
        if self.directory_fd < 0:
            raise AuditError("JSON output directory is already closed")
        rendered = (
            json.dumps(payload, indent=2, sort_keys=True) + "\n"
        ).encode("utf-8")

        temporary = ""
        descriptor = -1
        open_flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
        open_flags |= getattr(os, "O_CLOEXEC", 0)
        for _ in range(128):
            candidate = (
                f".{self.basename}.{os.getpid()}."
                f"{secrets.token_hex(12)}.tmp"
            )
            try:
                descriptor = os.open(
                    candidate,
                    open_flags,
                    0o600,
                    dir_fd=self.directory_fd,
                )
            except FileExistsError:
                continue
            except OSError as error:
                raise AuditError("JSON output temporary file could not be created") from error
            temporary = candidate
            break
        if descriptor < 0:
            raise AuditError("could not allocate a private JSON output file")

        installed = False
        try:
            offset = 0
            while offset < len(rendered):
                try:
                    written = os.write(descriptor, rendered[offset:])
                except InterruptedError:
                    continue
                if written <= 0:
                    raise AuditError("short write while creating JSON output")
                offset += written
            os.fsync(descriptor)
            os.close(descriptor)
            descriptor = -1

            if self.overwrite:
                os.replace(
                    temporary,
                    self.basename,
                    src_dir_fd=self.directory_fd,
                    dst_dir_fd=self.directory_fd,
                )
            else:
                try:
                    os.link(
                        temporary,
                        self.basename,
                        src_dir_fd=self.directory_fd,
                        dst_dir_fd=self.directory_fd,
                        follow_symlinks=False,
                    )
                except OSError as error:
                    if error.errno == errno.EEXIST:
                        raise FileExistsError(
                            f"refusing to overwrite {self.basename}"
                        ) from error
                    raise
                os.unlink(temporary, dir_fd=self.directory_fd)
            installed = True
            os.fsync(self.directory_fd)
        except (AuditError, FileExistsError):
            raise
        except OSError as error:
            raise AuditError("JSON output could not be installed atomically") from error
        finally:
            if descriptor >= 0:
                os.close(descriptor)
            if temporary and not installed:
                try:
                    os.unlink(temporary, dir_fd=self.directory_fd)
                except FileNotFoundError:
                    pass


def protected_replay_inputs(
    *,
    summary_path: Path,
    artifact_dir: Path,
    matrix_path: Path,
    bank_path: Path,
    drat_trim: Path,
) -> set[Path]:
    """Resolve every authenticated input before permitting JSON output writes."""

    try:
        payload, _ = _load_frozen_summary(summary_path, EXPECTED_SUMMARY_SHA256)
    except AuditError as error:
        raise AuditError("cannot reserve outputs from an unfrozen proof summary") from error
    records = validate_summary(payload)
    replay_script = Path(__file__).resolve()
    protected = {
        summary_path.resolve(),
        matrix_path.resolve(),
        bank_path.resolve(),
        drat_trim.resolve(),
        (drat_trim.resolve().parent / "SOURCE_COMMIT").resolve(),
        replay_script,
        replay_script.with_name("check_r3_18_budget7_branch1_core_cnf.py").resolve(),
        replay_script.with_name("independent_seqcounter.py").resolve(),
    }
    for record in records:
        protected.add((artifact_dir / record.cnf_asset).resolve())
        protected.add((artifact_dir / record.proof_asset).resolve())
    return protected


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--summary", type=Path)
    parser.add_argument("--matrix", type=Path)
    parser.add_argument("--universal-bank", type=Path)
    parser.add_argument("--drat-trim", type=Path, required=True)
    parser.add_argument("--drat-seconds", type=float, default=1800.0)
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args(argv)

    artifact_dir = args.artifact_dir.resolve()
    summary = (
        args.summary.resolve()
        if args.summary is not None
        else artifact_dir / "r3_18_budget7_branch1_core_proof_summary.json"
    )
    matrix = (
        args.matrix.resolve()
        if args.matrix is not None
        else artifact_dir / "certificates" / "r3_18_n100_nearmiss.txt"
    )
    bank = (
        args.universal_bank.resolve()
        if args.universal_bank is not None
        else artifact_dir / "r3_18_budget6_branch_0_universal_union.cuts.json"
    )
    output = args.json_output
    output_writer: StableJsonOutput | None = None
    if output is not None:
        try:
            protected = protected_replay_inputs(
                summary_path=summary,
                artifact_dir=artifact_dir,
                matrix_path=matrix,
                bank_path=bank,
                drat_trim=args.drat_trim.resolve(),
            )
            output_writer = StableJsonOutput.open(
                output,
                protected=protected,
                overwrite=args.overwrite,
            )
        except Exception as error:
            failure = {
                "schema": SCHEMA,
                "status": "FAILED_BRANCH1_CORE_PROOF_REPLAY",
                "error_type": type(error).__name__,
                "error": str(error),
            }
            print(json.dumps(failure, sort_keys=True), file=sys.stderr)
            return 1

    try:
        try:
            result = audit_core_proofs(
                summary_path=summary,
                artifact_dir=artifact_dir,
                matrix_path=matrix,
                bank_path=bank,
                drat_trim=args.drat_trim.resolve(),
                timeout_seconds=args.drat_seconds,
            )
        except Exception as error:
            failure = {
                "schema": SCHEMA,
                "status": "FAILED_BRANCH1_CORE_PROOF_REPLAY",
                "error_type": type(error).__name__,
                "error": str(error),
            }
            if output_writer is not None:
                try:
                    output_writer.write(failure)
                except Exception as output_error:
                    failure["json_output_error_type"] = type(output_error).__name__
                    failure["json_output_error"] = str(output_error)
            print(json.dumps(failure, sort_keys=True), file=sys.stderr)
            return 1

        if output_writer is not None:
            try:
                output_writer.write(result)
            except Exception as error:
                failure = {
                    "schema": SCHEMA,
                    "status": "FAILED_BRANCH1_CORE_PROOF_REPLAY",
                    "error_type": type(error).__name__,
                    "error": str(error),
                }
                print(json.dumps(failure, sort_keys=True), file=sys.stderr)
                return 1
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    finally:
        if output_writer is not None:
            output_writer.close()


if __name__ == "__main__":
    raise SystemExit(main())
