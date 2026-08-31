#!/usr/bin/env python3
"""Fail-closed audit of the bounded maximal-union UNKNOWN endpoint."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import stat
import tempfile
from pathlib import Path
from typing import Any, Sequence


SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch1-maximal-union-probe-v1"
STATUS = "MAXIMAL_UNION_TIMEOUT_UNKNOWN_NO_CUT"
CNF_SHA256 = "09e1784c3f43c4901dc6f6b4749fc5a74b025b08f74be58133edd1ed1096ebdb"
SOLVER_SHA256 = "bd054bcc5864fd20c9ff117f8fff94f810f5b210014ff33971a6c1db1d0eca45"
PROOF_PREFIX_SHA256 = (
    "a6693fe2b3bab57f9d0e9ebe39bd7baa3883bfe2af15a5eb33b0aded972b5438"
)


class AuditError(ValueError):
    """Raised when the retained endpoint does not match its frozen record."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def regular_bytes(path: Path, label: str) -> bytes:
    try:
        metadata = os.lstat(path)
    except OSError as error:
        raise AuditError(f"cannot inspect {label}") from error
    if not stat.S_ISREG(metadata.st_mode):
        raise AuditError(f"{label} must be a non-symlink regular file")
    try:
        return path.read_bytes()
    except OSError as error:
        raise AuditError(f"cannot read {label}") from error


def strict_json(raw: bytes, label: str) -> dict[str, Any]:
    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise AuditError(f"{label} contains duplicate key {key!r}")
            result[key] = value
        return result

    try:
        payload = json.loads(raw, object_pairs_hook=reject_duplicates)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise AuditError(f"{label} is not strict JSON") from error
    if not isinstance(payload, dict):
        raise AuditError(f"{label} root must be an object")

    def reject_nonfinite(value: Any) -> None:
        if isinstance(value, float) and not math.isfinite(value):
            raise AuditError(f"{label} contains a non-finite number")
        if isinstance(value, dict):
            for child in value.values():
                reject_nonfinite(child)
        elif isinstance(value, list):
            for child in value:
                reject_nonfinite(child)

    reject_nonfinite(payload)
    return payload


def audit(record_path: Path, artifact_dir: Path) -> dict[str, Any]:
    record_raw = regular_bytes(record_path, "endpoint record")
    record = strict_json(record_raw, "endpoint record")
    if record.get("schema") != SCHEMA or record.get("status") != STATUS:
        raise AuditError("wrong endpoint schema or status")

    formula = record.get("formula")
    if not isinstance(formula, dict) or formula != {
        "bytes": 408370088,
        "clauses": 1972360,
        "independent_reconstruction_status": (
            "MAXIMAL_UNION_CNF_RECONSTRUCTED_BYTE_EXACT"
        ),
        "sha256": CNF_SHA256,
        "variables": 639290,
    }:
        raise AuditError("formula identity or dimensions changed")

    claim = record.get("claim_boundary")
    if not isinstance(claim, dict) or any(value is not False for value in claim.values()):
        raise AuditError("UNKNOWN endpoint was promoted into a scientific claim")
    stop = record.get("stop_rule")
    if not isinstance(stop, dict) or any(value is not False for value in stop.values()):
        raise AuditError("UNKNOWN stop rule was weakened")

    probe = record.get("probe")
    if not isinstance(probe, dict):
        raise AuditError("missing probe record")
    expected_probe = {
        "exit_code": 124,
        "result_text": "c UNKNOWN",
        "solver_binary_sha256": SOLVER_SHA256,
        "wall_limit_seconds": 300,
        "wall_seconds_reported": 300.0,
    }
    for key, value in expected_probe.items():
        if probe.get(key) != value:
            raise AuditError(f"probe field {key!r} changed")

    proof = record.get("proof_prefix")
    if not isinstance(proof, dict) or proof != {
        "bytes": 922038097,
        "complete": False,
        "deleted_after_hashing": True,
        "replayed": False,
        "sha256": PROOF_PREFIX_SHA256,
        "usable_as_certificate": False,
    }:
        raise AuditError("proof-prefix boundary changed")

    retained = record.get("retained_files")
    if not isinstance(retained, dict) or not retained:
        raise AuditError("missing retained-file ledger")
    observed: dict[str, str] = {}
    for basename, expected_sha256 in sorted(retained.items()):
        if Path(basename).name != basename or not isinstance(expected_sha256, str):
            raise AuditError("unsafe retained-file ledger entry")
        path = artifact_dir / basename
        regular_bytes(path, f"retained file {basename}")
        actual = sha256_file(path)
        if actual != expected_sha256:
            raise AuditError(f"retained file {basename} SHA-256 mismatch")
        observed[basename] = actual

    if (artifact_dir / "solver_proof.drat").exists():
        raise AuditError("incomplete proof prefix must not be retained as a certificate")
    if regular_bytes(artifact_dir / "solver_result.sol", "solver result") != b"c UNKNOWN\n":
        raise AuditError("solver result is not the frozen UNKNOWN text")
    if regular_bytes(artifact_dir / "solver_exit_code.txt", "solver exit") != b"124\n":
        raise AuditError("solver exit is not the timeout code 124")
    if regular_bytes(artifact_dir / "solver.stderr", "solver stderr") != b"":
        raise AuditError("solver stderr is not empty")
    expected_inputs = (
        f"{SOLVER_SHA256}  cadical\n{CNF_SHA256}  branch1_maximal_union.cnf\n"
    ).encode("ascii")
    if regular_bytes(artifact_dir / "solver_inputs.sha256", "solver inputs") != expected_inputs:
        raise AuditError("sanitized solver-input identity changed")
    expected_proof_line = f"{PROOF_PREFIX_SHA256}  solver_proof.drat\n".encode("ascii")
    if regular_bytes(
        artifact_dir / "incomplete_proof.sha256", "proof-prefix hash"
    ) != expected_proof_line:
        raise AuditError("proof-prefix hash record changed")

    stdout = regular_bytes(artifact_dir / "solver.stdout", "solver stdout")
    required = (
        b"Version 3.0.1 c60730422e758ef1cebe7aeddf2dda31c996bf04",
        b"found 'p cnf 639290 1972360' header",
        b"c conflicts:                 13347",
        b"c decisions:                105834",
        b"c propagations:         1216037481",
        b"c total real time since initialization:          300.00    seconds",
        b"c raising signal 15 (SIGTERM)",
    )
    if any(fragment not in stdout for fragment in required):
        raise AuditError("solver stdout lacks frozen timeout telemetry")
    if b"s SATISFIABLE" in stdout or b"s UNSATISFIABLE" in stdout:
        raise AuditError("solver stdout unexpectedly contains a terminal SAT status")

    production = strict_json(
        regular_bytes(artifact_dir / "branch1_maximal_union_gate.json", "production record"),
        "production record",
    )
    audit_record = strict_json(
        regular_bytes(artifact_dir / "cnf_audit.json", "CNF audit"), "CNF audit"
    )
    if production.get("status") != "MAXIMAL_UNION_CNF_READY_SOLVER_NOT_RUN":
        raise AuditError("production formula record changed")
    if audit_record.get("status") != "MAXIMAL_UNION_CNF_RECONSTRUCTED_BYTE_EXACT":
        raise AuditError("independent CNF audit changed")
    for payload in (production.get("generated_cnf"), audit_record.get("cnf")):
        if not isinstance(payload, dict) or payload.get("sha256") != CNF_SHA256:
            raise AuditError("formula records do not bind the exact CNF")

    return {
        "claim": "UNKNOWN_NO_CUT_NO_BRANCH_CLOSURE",
        "endpoint_record_sha256": hashlib.sha256(record_raw).hexdigest(),
        "formula_sha256": CNF_SHA256,
        "proof_prefix_deleted": True,
        "retained_files_verified": len(observed),
        "schema": "ramsey-r3-18-n100-exact-budget7-branch1-maximal-union-probe-audit-v1",
        "solver_exit_code": 124,
        "status": "VERIFIED_MAXIMAL_UNION_TIMEOUT_UNKNOWN_ENDPOINT",
    }


def atomic_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(fd, "w", encoding="ascii", newline="\n") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True, ensure_ascii=True)
            handle.write("\n")
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def _absolute_lexical(path: Path) -> Path:
    """Make a path absolute without dereferencing its final symlink."""
    return Path(os.path.abspath(os.fspath(path)))


def main(argv: Sequence[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--record",
        type=Path,
        default=here / "r3_18_budget7_branch1_maximal_union_probe.json",
    )
    parser.add_argument(
        "--artifact-dir",
        type=Path,
        default=here / "certificates" / "r3_18_budget7_branch1_maximal_union_probe",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    result = audit(
        _absolute_lexical(args.record), _absolute_lexical(args.artifact_dir)
    )
    if args.output is not None:
        atomic_json(_absolute_lexical(args.output), result)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
