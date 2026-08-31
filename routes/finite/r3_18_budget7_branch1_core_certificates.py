#!/usr/bin/env python3
"""Export proof-carrying CNFs for branch-1 generalized deletion cores.

The exporter reconstructs the pinned branch-1 *common relaxation* used by
``r3_18_budget7_branch1_assumption_cores.py``.  The in-memory ``clauses``
field of that module deliberately omits the streamed universal I18 bank, so
this file materializes the bank explicitly, in its recorded order, before
appending one negative edge unit for every proposed deletion in ``K``.

The default candidates are the four size-two sets currently selected for
proof checking::

    K_ab = {(11,62), (18,61)}
    K_ac = {(11,62), (18,64)}
    K_ad = {(11,62), (18,69)}
    K_bd = {(18,61), (18,69)}

Containing PySAT cores, when available, are only provenance anchors.  They do
not prove their subsets.  The CLI also accepts any explicit nonempty set of
residual input edges; absence of a pilot superset does not block export and
does not add evidence.  A candidate is accepted as excluding all exact-six
residual supports containing it only after a pinned standalone CaDiCaL emits
a DRAT trace and a separately pinned drat-trim returns ``s VERIFIED``.  SAT,
timeout, missing proof, and checker failure are all fail-closed.  No output
claims core minimality or a global Ramsey-number theorem.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence

try:
    from .budget8_next import deterministic_gzip_text, sha256, verify_drat_trace
    from .r3_18_branch0_two_stage import atomic_json, run_external_proof
    from .r3_18_budget5_branch import EXPECTED_INPUT_SHA256, hitting_clause
    from .r3_18_budget7_branch import (
        EXPECTED_BUDGET6_SUMMARY_SHA256,
        EXPECTED_UNIVERSAL_BANK_SHA256,
        load_universal_bank,
        validate_budget6_dependency,
    )
    from .r3_18_budget7_branch1_assumption_cores import (
        EXPECTED_VERTICES,
        FORMULA_SCHEMA,
        RESIDUAL_DELETIONS,
        CommonFormula,
        _shareable_path,
        build_common_formula,
    )
    from .verify_ramsey import read_matrix
except ImportError:  # pragma: no cover - direct script execution
    from budget8_next import deterministic_gzip_text, sha256, verify_drat_trace
    from r3_18_branch0_two_stage import atomic_json, run_external_proof
    from r3_18_budget5_branch import EXPECTED_INPUT_SHA256, hitting_clause
    from r3_18_budget7_branch import (
        EXPECTED_BUDGET6_SUMMARY_SHA256,
        EXPECTED_UNIVERSAL_BANK_SHA256,
        load_universal_bank,
        validate_budget6_dependency,
    )
    from r3_18_budget7_branch1_assumption_cores import (
        EXPECTED_VERTICES,
        FORMULA_SCHEMA,
        RESIDUAL_DELETIONS,
        CommonFormula,
        _shareable_path,
        build_common_formula,
    )
    from verify_ramsey import read_matrix


Edge = tuple[int, int]

SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch1-core-export-v1"
MANIFEST_SCHEMA = (
    "ramsey-r3-18-n100-exact-budget7-branch1-core-cnf-manifest-v1"
)
RESULT_SCHEMA = (
    "ramsey-r3-18-n100-exact-budget7-branch1-core-proof-result-v1"
)
CANDIDATE_FILE_SCHEMA = (
    "ramsey-r3-18-n100-exact-budget7-branch1-core-candidates-v1"
)
PILOT_SCHEMA = (
    "ramsey-r3-18-n100-exact-budget7-branch1-assumption-core-pilot-v1"
)
EXPECTED_FORMULA_FINGERPRINT = (
    "a6f920afa451174ed05932174951481a63647a2ba603c762379f9357323fa5e2"
)
EXPECTED_CADICAL_COMMIT = "c60730422e758ef1cebe7aeddf2dda31c996bf04"
EXPECTED_DRAT_TRIM_COMMIT = "2e3b2dc0ecf938addbd779d42877b6ed69d9a985"
REPOSITORY_ROOT = Path(__file__).resolve().parents[2]

DEFAULT_CORES: tuple[tuple[str, tuple[Edge, ...]], ...] = (
    ("K_ab", ((11, 62), (18, 61))),
    ("K_ac", ((11, 62), (18, 64))),
    ("K_ad", ((11, 62), (18, 69))),
    ("K_bd", ((18, 61), (18, 69))),
)

_SAFE_LABEL = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,63}\Z")


@dataclass(frozen=True)
class CandidateCore:
    """A canonical proposed deletion core plus its pilot provenance anchors."""

    label: str
    edges: tuple[Edge, ...]
    assumption_units: tuple[int, ...]
    candidate_sha256: str
    anchor_records: tuple[dict[str, Any], ...]


@dataclass(frozen=True)
class CandidateArtifactPaths:
    """All reserved output names for one candidate, proof requested or not."""

    cnf: Path
    manifest: Path
    result: Path
    drat: Path


def candidate_artifact_paths(
    output_dir: Path, candidate: CandidateCore
) -> CandidateArtifactPaths:
    stem = f"branch1_core_{candidate.label}_size{len(candidate.edges)}"
    return CandidateArtifactPaths(
        cnf=output_dir / f"{stem}.cnf.gz",
        manifest=output_dir / f"{stem}.manifest.json",
        result=output_dir / f"{stem}.result.json",
        drat=output_dir / f"{stem}.drat.gz",
    )


def _require_distinct_resolved_targets(
    named_paths: Sequence[tuple[str, Path]],
) -> None:
    """Reject aliases and symlink collisions before any artifact is written."""

    owners: dict[Path, str] = {}
    for name, path in named_paths:
        resolved = path.resolve()
        previous = owners.get(resolved)
        if previous is not None:
            raise ValueError(
                f"artifact target collision after path resolution: {previous} and {name}"
            )
        owners[resolved] = name


def validate_export_targets(
    summary_json: Path,
    output_dir: Path,
    candidates: Sequence[CandidateCore],
    *,
    protected_inputs: Sequence[Path] = (),
) -> list[CandidateArtifactPaths]:
    """Reserve the complete aggregate/per-candidate output namespace."""

    plans = [candidate_artifact_paths(output_dir, candidate) for candidate in candidates]
    targets: list[tuple[str, Path]] = [("summary_json", summary_json)]
    for candidate, paths in zip(candidates, plans):
        targets.extend(
            [
                (f"{candidate.label}:cnf", paths.cnf),
                (f"{candidate.label}:manifest", paths.manifest),
                (f"{candidate.label}:result", paths.result),
                (f"{candidate.label}:drat", paths.drat),
            ]
        )
    targets.extend(
        (f"protected_input_{index}", path)
        for index, path in enumerate(protected_inputs)
    )
    _require_distinct_resolved_targets(targets)
    return plans


def canonical_sha256(payload: Any) -> str:
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return hashlib.sha256(encoded).hexdigest()


def _edge_lists(edges: Iterable[Edge]) -> list[list[int]]:
    return [list(edge) for edge in edges]


def _require_mapping(payload: Any, description: str) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise ValueError(f"{description} must be a JSON object")
    return payload


def _validate_record_digest(record: dict[str, Any]) -> None:
    recorded = record.get("record_sha256")
    body = {key: value for key, value in record.items() if key != "record_sha256"}
    if recorded != canonical_sha256(body):
        raise ValueError("pilot record digest mismatch")


def validate_pilot(
    payload: dict[str, Any], formula: CommonFormula
) -> list[dict[str, Any]]:
    """Validate the pilot and return proof-neutral accepted-core anchors.

    An anchor establishes only that a proposed candidate came from a subset
    of a recorded engineering core.  It never transfers UNSAT to that subset.
    """

    if payload.get("schema") != PILOT_SCHEMA:
        raise ValueError("unexpected assumption-core pilot schema")
    if payload.get("status") != "PILOT_SUPPORT_LIST_EXHAUSTED":
        raise ValueError("assumption-core pilot is not a completed frozen run")
    input_record = _require_mapping(payload.get("input"), "pilot input")
    if input_record.get("sha256") != EXPECTED_INPUT_SHA256:
        raise ValueError("pilot matrix identity mismatch")
    if input_record.get("vertices") != EXPECTED_VERTICES:
        raise ValueError("pilot matrix order mismatch")
    dependencies = _require_mapping(payload.get("dependencies"), "pilot dependencies")
    if dependencies.get("budget6_summary_sha256") != EXPECTED_BUDGET6_SUMMARY_SHA256:
        raise ValueError("pilot budget-six dependency mismatch")
    if dependencies.get("budget6_dependency_proof_verified") is not True:
        raise ValueError("pilot budget-six dependency is not proof-verified")
    bank = _require_mapping(dependencies.get("universal_bank"), "pilot universal bank")
    if bank.get("sha256") != EXPECTED_UNIVERSAL_BANK_SHA256:
        raise ValueError("pilot universal-bank identity mismatch")

    recorded_formula = _require_mapping(
        payload.get("common_formula"), "pilot common formula"
    )
    if recorded_formula.get("schema") != FORMULA_SCHEMA:
        raise ValueError("pilot formula schema mismatch")
    if recorded_formula.get("formula_fingerprint_sha256") != (
        EXPECTED_FORMULA_FINGERPRINT
    ):
        raise ValueError("pilot formula fingerprint mismatch")
    if formula.metadata.get("formula_fingerprint_sha256") != (
        EXPECTED_FORMULA_FINGERPRINT
    ):
        raise ValueError("rebuilt formula fingerprint mismatch")
    if recorded_formula != formula.metadata:
        raise ValueError("pilot formula metadata differs from rebuilt formula")
    if recorded_formula.get("learned_core_clauses_installed") != 0:
        raise ValueError("pilot formula contains learned core clauses")

    counters = _require_mapping(payload.get("counters"), "pilot counters")
    if counters.get("unknown_learned_cores") != 0:
        raise ValueError("pilot reports a core learned from UNKNOWN")
    if counters.get("core_clauses_installed_into_common_formula") != 0:
        raise ValueError("pilot reports circular core-clause installation")

    records = payload.get("records")
    if not isinstance(records, list) or not records:
        raise ValueError("pilot contains no support records")
    anchors: list[dict[str, Any]] = []
    for raw_record in records:
        record = _require_mapping(raw_record, "pilot support record")
        _validate_record_digest(record)
        accepted = record.get("accepted_core")
        if accepted is None:
            continue
        accepted = _require_mapping(accepted, "pilot accepted core")
        if (
            accepted.get("primary_UNSAT") is not True
            or accepted.get("distinct_backend_replay_UNSAT") is not True
            or accepted.get("engineering_telemetry_not_proof_certificate") is not True
        ):
            raise ValueError("pilot accepted core lacks fail-closed replay metadata")
        edges = _strict_edge_tuple(accepted.get("deletion_edges"), "pilot accepted core")
        if len(edges) != accepted.get("size"):
            raise ValueError("pilot accepted-core size mismatch")
        if not set(edges).issubset(formula.residual_edges):
            raise ValueError("pilot accepted core contains a non-residual edge")
        expected_literals = [-formula.variables[edge] for edge in edges]
        if accepted.get("literals") != expected_literals:
            raise ValueError("pilot accepted-core literal polarity/order mismatch")
        support = _strict_edge_tuple(record.get("support"), "pilot support")
        if not set(edges).issubset(support):
            raise ValueError("pilot accepted core is not a subset of its support")
        anchors.append(
            {
                "record_sha256": record["record_sha256"],
                "accepted_core_edges": _edge_lists(edges),
                "accepted_core_size": len(edges),
                "anchor_is_engineering_provenance_not_subset_proof": True,
            }
        )
    if not anchors:
        raise ValueError("pilot contains no replay-validated core anchors")
    if payload.get("final_record_set_sha256") != canonical_sha256(records):
        raise ValueError("pilot final record-set digest mismatch")
    return anchors


def _strict_edge_tuple(raw: Any, description: str) -> tuple[Edge, ...]:
    if not isinstance(raw, (list, tuple)) or not raw:
        raise ValueError(f"{description} must be a nonempty edge list")
    edges: list[Edge] = []
    for item in raw:
        if not isinstance(item, (list, tuple)) or len(item) != 2:
            raise ValueError(f"{description} contains a malformed edge")
        u, v = item
        if any(not isinstance(x, int) or isinstance(x, bool) for x in (u, v)):
            raise ValueError(f"{description} vertices must be integer JSON numbers")
        if not (0 <= u < v < EXPECTED_VERTICES):
            raise ValueError(f"{description} edges must be canonical pairs in [0,99]")
        edges.append((u, v))
    if len(edges) != len(set(edges)):
        raise ValueError(f"{description} contains duplicate edges")
    if edges != sorted(edges):
        raise ValueError(f"{description} edges must be lexicographically sorted")
    return tuple(edges)


def validate_candidate(
    label: str,
    raw_edges: Any,
    formula: CommonFormula,
    pilot_anchors: Sequence[dict[str, Any]],
) -> CandidateCore:
    if not _SAFE_LABEL.fullmatch(label) or ".." in label:
        raise ValueError("candidate label is not a safe artifact name")
    edges = _strict_edge_tuple(raw_edges, f"candidate {label}")
    if len(edges) > RESIDUAL_DELETIONS:
        raise ValueError("candidate core is larger than a full residual support")
    if not set(edges).issubset(formula.residual_edges):
        raise ValueError("candidate core contains a non-residual input edge")
    matching = [
        anchor
        for anchor in pilot_anchors
        if set(edges).issubset(
            {tuple(edge) for edge in anchor["accepted_core_edges"]}
        )
    ]
    units = tuple(-formula.variables[edge] for edge in edges)
    if any(unit >= 0 for unit in units) or len(units) != len(set(units)):
        raise AssertionError("candidate deletion units have invalid polarity or duplicates")
    identity = {
        "formula_fingerprint_sha256": EXPECTED_FORMULA_FINGERPRINT,
        "deletion_edges": _edge_lists(edges),
        "assumption_units": list(units),
        "semantics": "for every e in K, d_e=true is encoded as unit -x_e",
    }
    return CandidateCore(
        label=label,
        edges=edges,
        assumption_units=units,
        candidate_sha256=canonical_sha256(identity),
        anchor_records=tuple(matching),
    )


def iter_full_clauses(
    formula: CommonFormula, assumption_units: Sequence[int]
) -> Iterator[list[int]]:
    """Yield the exact full clause sequence frozen into DIMACS."""

    for clause in formula.clauses:
        yield clause
    for mask in formula.universal_masks:
        yield hitting_clause(mask, EXPECTED_VERTICES, formula.variables)
    for literal in assumption_units:
        yield [literal]


def full_dimacs_lines(
    formula: CommonFormula, assumption_units: Sequence[int]
) -> Iterator[str]:
    common_count = len(formula.clauses) + len(formula.universal_masks)
    if formula.metadata.get("total_clauses") != common_count:
        raise ValueError("rebuilt common-formula clause count is inconsistent")
    maximum_variable = formula.metadata.get("maximum_variable")
    if not isinstance(maximum_variable, int) or maximum_variable <= 0:
        raise ValueError("rebuilt common formula has invalid maximum variable")
    total = common_count + len(assumption_units)
    yield f"p cnf {maximum_variable} {total}\n"
    emitted = 0
    for clause in iter_full_clauses(formula, assumption_units):
        if not clause or any(
            not isinstance(literal, int)
            or isinstance(literal, bool)
            or literal == 0
            or abs(literal) > maximum_variable
            for literal in clause
        ):
            raise ValueError("formula contains an invalid DIMACS clause")
        emitted += 1
        yield " ".join(map(str, clause)) + " 0\n"
    if emitted != total:
        raise AssertionError("DIMACS clause emission count mismatch")


def _public_tool_result(
    raw: dict[str, Any],
    executable: Path,
    source_commit: str,
    *,
    proof_path: Path | None = None,
) -> dict[str, Any]:
    """Keep proof telemetry while excluding absolute workstation paths."""

    result: dict[str, Any] = {
        "status": raw.get("status"),
        "tool_basename": executable.name,
        "tool_sha256": sha256(executable),
        "source_commit": source_commit,
    }
    for key in ("exitcode", "wall_limit_seconds", "elapsed_seconds"):
        if key in raw:
            result[key] = raw[key]
    for source_key, target_key in (
        ("stdout_tail", "stdout_tail"),
        ("stderr_tail", "stderr_tail"),
        ("stdout", "stdout_tail"),
        ("stderr", "stderr_tail"),
    ):
        if source_key in raw:
            text = str(raw[source_key])[-8000:]
            for path in (REPOSITORY_ROOT, executable.resolve(), executable.resolve().parent):
                text = text.replace(str(path), f"<redacted>/{Path(path).name}")
            text = re.sub(
                r"/\S*/ramsey-(?:r3-18-cadical|budget8-drat)-\S+",
                "<redacted>/temporary-proof-path",
                text,
            )
            result[target_key] = text
    if isinstance(raw.get("proof"), dict):
        result["proof"] = raw["proof"]
    if proof_path is not None and proof_path.is_file():
        result["proof_artifact"] = {
            "path": _shareable_path(proof_path),
            "gzip_sha256": sha256(proof_path),
            "bytes": proof_path.stat().st_size,
        }
    return result


def classify_external_result(
    proof: dict[str, Any], checker: dict[str, Any] | None
) -> tuple[str, bool]:
    """Return a fail-closed public status and its proof-verified bit."""

    proof_status = proof.get("status")
    if proof_status == "SAT":
        return "QUARANTINED_EXTERNAL_SAT_MISMATCH", False
    if proof_status != "UNSAT_PROOF_WRITTEN":
        return "UNKNOWN_EXTERNAL_PROOF_NOT_COMPLETED", False
    if checker is None:
        return "UNKNOWN_PROOF_NOT_CHECKED", False
    if checker.get("status") == "VERIFIED":
        return "UNSAT_PROOF_VERIFIED_LOCAL_BRANCH1_EXACT_SIX_CORE", True
    return "UNKNOWN_PROOF_UNVERIFIED", False


def require_complete_proof_artifact(
    proof: dict[str, Any], proof_path: Path
) -> dict[str, Any]:
    """Downgrade exit-20 telemetry unless its deterministic trace exists."""

    if proof.get("status") != "UNSAT_PROOF_WRITTEN":
        return proof
    proof_metadata = proof.get("proof")
    if proof_path.is_file() and isinstance(proof_metadata, dict):
        if proof_metadata.get("gzip_sha256") == sha256(proof_path):
            return proof
        downgraded = dict(proof)
        downgraded["status"] = "ERROR_PROOF_ARTIFACT_DIGEST_MISMATCH"
        return downgraded
    downgraded = dict(proof)
    downgraded["status"] = "ERROR_UNSAT_WITHOUT_PROOF_ARTIFACT"
    return downgraded


def _validate_toolchain(
    cadical: Path | None,
    cadical_commit: str | None,
    drat_trim: Path | None,
    drat_trim_commit: str | None,
) -> bool:
    values = (cadical, cadical_commit, drat_trim, drat_trim_commit)
    if all(value is None for value in values):
        return False
    if any(value is None for value in values):
        raise ValueError("CaDiCaL, drat-trim, and both source commits are all-or-none")
    assert cadical is not None and drat_trim is not None
    for executable in (cadical, drat_trim):
        if not executable.is_file() or not os.access(executable, os.X_OK):
            raise ValueError(f"proof tool is not executable: {executable.name}")
    if cadical_commit != EXPECTED_CADICAL_COMMIT:
        raise ValueError("unexpected CaDiCaL source commit")
    if drat_trim_commit != EXPECTED_DRAT_TRIM_COMMIT:
        raise ValueError("unexpected drat-trim source commit")
    for executable, expected_commit in (
        (cadical, cadical_commit),
        (drat_trim, drat_trim_commit),
    ):
        marker = executable.parent / "SOURCE_COMMIT"
        if not marker.is_file():
            raise ValueError(
                f"proof tool lacks adjacent SOURCE_COMMIT: {executable.name}"
            )
        try:
            recorded_lines = marker.read_text(encoding="ascii").splitlines()
        except UnicodeError as error:
            raise ValueError(
                f"proof tool has non-ASCII SOURCE_COMMIT: {executable.name}"
            ) from error
        if recorded_lines != [expected_commit]:
            raise ValueError(
                f"proof tool SOURCE_COMMIT mismatch: {executable.name}"
            )
    return True


def export_candidate(
    formula: CommonFormula,
    candidate: CandidateCore,
    input_manifest: dict[str, Any],
    output_dir: Path,
    *,
    overwrite: bool = False,
    cadical: Path | None = None,
    cadical_commit: str | None = None,
    drat_trim: Path | None = None,
    drat_trim_commit: str | None = None,
    proof_seconds: float = 3600.0,
    drat_check_seconds: float = 3600.0,
) -> dict[str, Any]:
    proof_requested = _validate_toolchain(
        cadical, cadical_commit, drat_trim, drat_trim_commit
    )
    paths = candidate_artifact_paths(output_dir, candidate)
    cnf_path = paths.cnf
    manifest_path = paths.manifest
    result_path = paths.result
    proof_path = paths.drat
    _require_distinct_resolved_targets(
        [
            ("cnf", cnf_path),
            ("manifest", manifest_path),
            ("result", result_path),
            ("drat", proof_path),
        ]
    )
    output_dir.mkdir(parents=True, exist_ok=True)
    targets = [cnf_path, manifest_path, result_path]
    if proof_requested:
        targets.append(proof_path)
    existing = [path.name for path in targets if path.exists()]
    if existing and not overwrite:
        raise FileExistsError("refusing to overwrite artifacts: " + ", ".join(existing))
    if proof_requested and overwrite and proof_path.exists():
        # ``run_external_proof`` creates its target only after a completed
        # UNSAT run.  Remove an explicitly overwritten prior trace first so a
        # timeout can never be paired with a stale proof from an older run.
        proof_path.unlink()

    raw_hash, gzip_hash, raw_bytes, line_count = deterministic_gzip_text(
        cnf_path, full_dimacs_lines(formula, candidate.assumption_units)
    )
    common_clauses = len(formula.clauses) + len(formula.universal_masks)
    total_clauses = common_clauses + len(candidate.assumption_units)
    manifest: dict[str, Any] = {
        "schema": MANIFEST_SCHEMA,
        "status": "FROZEN_DIMACS_EXPORTED_UNCHECKED",
        "claim_boundary": (
            "This manifest freezes a local branch-1 relaxation plus K units; "
            "it does not claim UNSAT, core minimality, or a global Ramsey bound."
        ),
        "inputs": input_manifest,
        "common_formula": {
            "schema": formula.metadata["schema"],
            "formula_fingerprint_sha256": formula.metadata[
                "formula_fingerprint_sha256"
            ],
            "maximum_variable": formula.metadata["maximum_variable"],
            "materialized_structural_and_degree_clauses": len(formula.clauses),
            "materialized_universal_I18_clauses": len(formula.universal_masks),
            "common_clause_count": common_clauses,
            "clause_order": [
                "structural clauses including exact-six and fixed branch unit",
                "degree-cap clauses",
                "universal I18 clauses in ordered-bank order",
                "candidate deletion units in lexicographic edge order",
            ],
            "formula_is_relaxation_of_target": True,
            "learned_core_clauses_installed": 0,
        },
        "candidate": {
            "label": candidate.label,
            "deletion_edges": _edge_lists(candidate.edges),
            "size": len(candidate.edges),
            "assumption_units": list(candidate.assumption_units),
            "unit_semantics": "d_e=true is the DIMACS unit -x_e",
            "candidate_sha256": candidate.candidate_sha256,
            "pilot_superset_anchors": list(candidate.anchor_records),
            "pilot_superset_anchor_available": bool(candidate.anchor_records),
            "pilot_anchor_proves_candidate_UNSAT": False,
            "minimality_claim": False,
        },
        "dimacs": {
            "path": _shareable_path(cnf_path),
            "variables": formula.metadata["maximum_variable"],
            "clauses": total_clauses,
            "header_and_clause_lines": line_count,
            "uncompressed_sha256": raw_hash,
            "gzip_sha256": gzip_hash,
            "uncompressed_bytes": raw_bytes,
            "gzip_bytes": cnf_path.stat().st_size,
        },
        "global_ramsey_implication": None,
    }
    if line_count != total_clauses + 1:
        raise AssertionError("DIMACS line count does not match header")
    atomic_json(manifest_path, manifest)

    result: dict[str, Any] = {
        "schema": RESULT_SCHEMA,
        "status": "DIMACS_EXPORTED_PROOF_NOT_REQUESTED",
        "proof_verified": False,
        "claim_boundary": (
            "Only VERIFIED means the frozen local branch-1 core CNF has an "
            "externally checked UNSAT proof; this excludes exact-six residual "
            "supports containing K but claims neither minimality nor a global theorem."
        ),
        "candidate": manifest["candidate"],
        "manifest": {
            "path": _shareable_path(manifest_path),
            "sha256": sha256(manifest_path),
        },
        "dimacs": manifest["dimacs"],
        "external_proof": {"status": "NOT_REQUESTED"},
        "drat_check": {"status": "NOT_REQUESTED"},
        "local_branch1_exact_six_superset_exclusion_proved": False,
        "minimality_claim": False,
        "global_ramsey_implication": None,
    }
    if proof_requested:
        assert cadical is not None and drat_trim is not None
        assert cadical_commit is not None and drat_trim_commit is not None
        try:
            raw_proof = run_external_proof(
                cadical, cnf_path, proof_path, proof_seconds
            )
        except OSError as error:
            raw_proof = {
                "status": "ERROR_TOOL_INVOCATION",
                "error_type": type(error).__name__,
            }
        raw_proof = require_complete_proof_artifact(raw_proof, proof_path)
        result["external_proof"] = _public_tool_result(
            raw_proof,
            cadical,
            cadical_commit,
            proof_path=proof_path,
        )
        raw_check: dict[str, Any] | None = None
        if raw_proof.get("status") == "UNSAT_PROOF_WRITTEN":
            try:
                raw_check = verify_drat_trace(
                    drat_trim,
                    cnf_path,
                    proof_path,
                    drat_check_seconds,
                )
            except OSError as error:
                raw_check = {
                    "status": "ERROR_TOOL_INVOCATION",
                    "error_type": type(error).__name__,
                }
            result["drat_check"] = _public_tool_result(
                raw_check, drat_trim, drat_trim_commit
            )
        else:
            result["drat_check"] = {
                "status": "NOT_RUN_WITHOUT_COMPLETE_UNSAT_PROOF"
            }
        status, verified = classify_external_result(raw_proof, raw_check)
        result["status"] = status
        result["proof_verified"] = verified
        result["local_branch1_exact_six_superset_exclusion_proved"] = verified
    atomic_json(result_path, result)
    return {
        "label": candidate.label,
        "status": result["status"],
        "proof_verified": result["proof_verified"],
        "cnf_gzip": _shareable_path(cnf_path),
        "cnf_gzip_sha256": gzip_hash,
        "manifest": _shareable_path(manifest_path),
        "manifest_sha256": sha256(manifest_path),
        "result": _shareable_path(result_path),
        "result_sha256": sha256(result_path),
        "proof": (
            _shareable_path(proof_path)
            if proof_requested and proof_path.is_file()
            else None
        ),
        "proof_gzip_sha256": (
            sha256(proof_path)
            if proof_requested and proof_path.is_file()
            else None
        ),
    }


def _parse_core_spec(value: str) -> tuple[str, tuple[Edge, ...]]:
    try:
        label, encoded = value.split(":", 1)
        edges = []
        for item in encoded.split(","):
            u, v = item.split("-", 1)
            edges.append((int(u), int(v)))
    except (ValueError, TypeError) as error:
        raise argparse.ArgumentTypeError(
            "core must be NAME:u-v,u-v,... with canonical sorted edges"
        ) from error
    return label, tuple(edges)


def _load_candidate_specs(
    core_specs: Sequence[tuple[str, tuple[Edge, ...]]],
    cores_json: Path | None,
) -> tuple[list[tuple[str, Any]], dict[str, Any]]:
    if core_specs and cores_json is not None:
        raise ValueError("use either --core or --cores-json, not both")
    if cores_json is not None:
        payload = _require_mapping(
            json.loads(cores_json.read_text(encoding="utf-8")),
            "candidate file",
        )
        if payload.get("schema") != CANDIDATE_FILE_SCHEMA:
            raise ValueError("unexpected candidate-file schema")
        if payload.get("formula_fingerprint_sha256") != EXPECTED_FORMULA_FINGERPRINT:
            raise ValueError("candidate-file formula fingerprint mismatch")
        raw = payload.get("cores")
        if not isinstance(raw, list) or not raw:
            raise ValueError("candidate file contains no cores")
        specs = []
        for item in raw:
            item = _require_mapping(item, "candidate-file core")
            specs.append((item.get("label"), item.get("edges")))
        source = {
            "kind": "candidate_json",
            "path": _shareable_path(cores_json),
            "sha256": sha256(cores_json),
        }
        return specs, source
    if core_specs:
        return list(core_specs), {
            "kind": "command_line",
            "formula_fingerprint_sha256": EXPECTED_FORMULA_FINGERPRINT,
        }
    return [(label, edges) for label, edges in DEFAULT_CORES], {
        "kind": "built_in_bounded_probe_targets_pending_external_proof",
        "formula_fingerprint_sha256": EXPECTED_FORMULA_FINGERPRINT,
    }


def _positive_float(value: str) -> float:
    parsed = float(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return parsed


def main() -> None:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--matrix",
        type=Path,
        default=here / "certificates" / "r3_18_n100_nearmiss.txt",
    )
    parser.add_argument(
        "--budget6-summary", type=Path, default=here / "r3_18_budget6_summary.json"
    )
    parser.add_argument(
        "--universal-bank",
        type=Path,
        default=here / "r3_18_budget6_branch_0_universal_union.cuts.json",
    )
    parser.add_argument(
        "--pilot-json",
        type=Path,
        default=here / "r3_18_budget7_branch1_assumption_core_pilot.json",
    )
    parser.add_argument("--core", action="append", default=[], type=_parse_core_spec)
    parser.add_argument("--cores-json", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--summary-json", type=Path, required=True)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--cadical", type=Path)
    parser.add_argument("--cadical-source-commit")
    parser.add_argument("--drat-trim", type=Path)
    parser.add_argument("--drat-trim-source-commit")
    parser.add_argument("--proof-seconds", type=_positive_float, default=3600.0)
    parser.add_argument("--drat-check-seconds", type=_positive_float, default=3600.0)
    args = parser.parse_args()

    if args.summary_json.exists() and not args.overwrite:
        raise FileExistsError(f"refusing to overwrite {args.summary_json.name}")
    if sha256(args.matrix) != EXPECTED_INPUT_SHA256:
        raise ValueError("unexpected frozen near-miss matrix identity")
    if sha256(args.budget6_summary) != EXPECTED_BUDGET6_SUMMARY_SHA256:
        raise ValueError("unexpected budget-six summary identity")
    budget6 = _require_mapping(
        json.loads(args.budget6_summary.read_text(encoding="utf-8")),
        "budget-six summary",
    )
    validate_budget6_dependency(budget6)
    universal_masks, universal_info = load_universal_bank(args.universal_bank)
    rows = read_matrix(args.matrix)
    formula = build_common_formula(
        rows, sha256(args.matrix), universal_masks, universal_info
    )
    pilot = _require_mapping(
        json.loads(args.pilot_json.read_text(encoding="utf-8")), "pilot"
    )
    anchors = validate_pilot(pilot, formula)
    raw_specs, candidate_source = _load_candidate_specs(args.core, args.cores_json)
    candidates = [
        validate_candidate(label, edges, formula, anchors)
        for label, edges in raw_specs
    ]
    if len({candidate.label for candidate in candidates}) != len(candidates):
        raise ValueError("candidate labels are not unique")
    if len({candidate.candidate_sha256 for candidate in candidates}) != len(candidates):
        raise ValueError("candidate core sets are not unique")

    protected_inputs = [
        args.matrix,
        args.budget6_summary,
        args.universal_bank,
        args.pilot_json,
    ]
    if args.cores_json is not None:
        protected_inputs.append(args.cores_json)
    validate_export_targets(
        args.summary_json,
        args.output_dir,
        candidates,
        protected_inputs=protected_inputs,
    )

    input_manifest = {
        "matrix": {
            "path": _shareable_path(args.matrix),
            "sha256": sha256(args.matrix),
        },
        "budget6_summary": {
            "path": _shareable_path(args.budget6_summary),
            "sha256": sha256(args.budget6_summary),
            "proof_verified_dependency": True,
        },
        "universal_bank": {
            "path": _shareable_path(args.universal_bank),
            "sha256": sha256(args.universal_bank),
            "ordered_masks_sha256": universal_info["ordered_masks_sha256"],
            "masks": len(universal_masks),
        },
        "pilot": {
            "path": _shareable_path(args.pilot_json),
            "sha256": sha256(args.pilot_json),
            "engineering_provenance_only": True,
        },
        "candidate_source": candidate_source,
    }
    summaries = [
        export_candidate(
            formula,
            candidate,
            input_manifest,
            args.output_dir,
            overwrite=args.overwrite,
            cadical=args.cadical,
            cadical_commit=args.cadical_source_commit,
            drat_trim=args.drat_trim,
            drat_trim_commit=args.drat_trim_source_commit,
            proof_seconds=args.proof_seconds,
            drat_check_seconds=args.drat_check_seconds,
        )
        for candidate in candidates
    ]
    proof_requested = any(
        item["status"] != "DIMACS_EXPORTED_PROOF_NOT_REQUESTED"
        for item in summaries
    )
    all_verified = bool(summaries) and all(item["proof_verified"] for item in summaries)
    aggregate = {
        "schema": SCHEMA,
        "status": (
            "ALL_LOCAL_BRANCH1_CORE_PROOFS_VERIFIED"
            if all_verified
            else "PROOF_ATTEMPTS_INCOMPLETE_OR_FAILED"
            if proof_requested
            else "DIMACS_EXPORTED_PROOFS_NOT_REQUESTED"
        ),
        "formula_fingerprint_sha256": EXPECTED_FORMULA_FINGERPRINT,
        "candidate_count": len(candidates),
        "results": summaries,
        "all_proof_verified": all_verified,
        "minimality_claim": False,
        "global_ramsey_implication": None,
        "provenance": {
            "script": _shareable_path(Path(__file__)),
            "script_sha256": sha256(Path(__file__)),
        },
    }
    args.summary_json.parent.mkdir(parents=True, exist_ok=True)
    atomic_json(args.summary_json, aggregate)


if __name__ == "__main__":
    main()
