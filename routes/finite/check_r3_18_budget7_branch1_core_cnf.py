#!/usr/bin/env python3
"""Independent, PySAT-free checker for branch-1 generalized-core CNFs.

This checker does not import the certificate exporter, the assumption-core
pilot, any production formula builder, or PySAT.  Starting from the frozen
adjacency matrix and the ordered universal-I18 JSON bank, it independently
reconstructs the complete DIMACS byte stream:

* lexicographically numbered edge variables;
* all triangle clauses;
* the exact-six residual-deletion sequential counter;
* the fixed ``-(97,99)`` branch unit;
* one independently encoded degree-at-most-17 block per vertex;
* the ordered universal-I18 clauses; and
* the explicit negative edge units for the proposed set ``K``.

The gzip member is decompressed and compared one canonical clause line at a
time.  A successful result authenticates the CNF construction and its binding
to ``K``; it does not check a DRAT trace and does not establish a global
Ramsey-number bound.
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
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence

try:
    from .independent_seqcounter import encode_atmost, encode_equals
except ImportError:  # pragma: no cover - direct script execution
    from independent_seqcounter import encode_atmost, encode_equals


Edge = tuple[int, int]

SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch1-core-cnf-audit-v1"
FORMULA_SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch1-common-formula-v1"
MANIFEST_SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch1-core-cnf-manifest-v1"
RESULT_SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch1-core-proof-result-v1"

EXPECTED_INPUT_SHA256 = (
    "e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e"
)
EXPECTED_BANK_SHA256 = (
    "91b5709248ff641a315f5a0389b4f3fde3d38514f3b1a8b31b6cad31224f250b"
)
EXPECTED_ORDERED_MASKS_SHA256 = (
    "f10690b826b86eb03567a2ffaffb553801fae32af20cfe4337118bddf4e41afa"
)
EXPECTED_FORMULA_FINGERPRINT = (
    "a6f920afa451174ed05932174951481a63647a2ba603c762379f9357323fa5e2"
)
EXPECTED_MAPPING_SHA256 = (
    "b2408e128c44b361a9b86d3c65b3d52be571e8abcdeeae3e40feb8d47a993730"
)
EXPECTED_STRUCTURAL_SHA256 = (
    "8da0fffeac8c3d6ea839eb836c55889239ab6083e1c9f45634a9987dac8b5311"
)
EXPECTED_DEGREE_SHA256 = (
    "54c75b4fda7be8d3ab997f8af20533a151662cea12aafbc7e8aa2a79bbde1b85"
)

PRODUCTION_ORDER = 100
PRODUCTION_FIXED_EDGE: Edge = (97, 99)
PRODUCTION_RESIDUAL_DELETIONS = 6
PRODUCTION_DEGREE_CAP = 17
PRODUCTION_BANK_SET_SIZE = 18
PRODUCTION_INPUT_EDGES = 827
PRODUCTION_RESIDUAL_EDGES = 826
PRODUCTION_BANK_MASKS = 251_771
PRODUCTION_EDGE_VARIABLES = 4_950
PRODUCTION_STRUCTURAL_CLAUSES = 181_381
PRODUCTION_DEGREE_CLAUSES = 285_300
PRODUCTION_COMMON_CLAUSES = 718_452
PRODUCTION_MAXIMUM_VARIABLE = 154_190

_SAFE_LABEL = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,63}\Z")


class AuditError(ValueError):
    """A fail-closed certificate reconstruction or binding failure."""


@dataclass(frozen=True)
class FormulaSpec:
    order: int
    fixed_edge: Edge
    residual_deletions: int
    degree_cap: int
    bank_set_size: int


@dataclass
class ReconstructionPlan:
    spec: FormulaSpec
    variables: dict[Edge, int]
    pairs: tuple[Edge, ...]
    original_edges: frozenset[Edge]
    residual_edges: tuple[Edge, ...]
    exact_clauses: list[list[int]]
    structural_top: int
    degree_block_clause_counts: tuple[int, ...]
    maximum_variable: int
    triangle_clause_count: int
    structural_clause_count: int
    degree_clause_count: int

    @property
    def common_clause_count_without_bank(self) -> int:
        return self.structural_clause_count + self.degree_clause_count


@dataclass(frozen=True)
class CnfAudit:
    variables: int
    clauses: int
    lines: int
    uncompressed_bytes: int
    uncompressed_sha256: str
    gzip_bytes: int
    gzip_sha256: str
    structural_clauses_sha256: str
    degree_clauses_sha256: str


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


def _safe_artifact(path: Path) -> dict[str, Any]:
    return {
        "basename": path.name,
        "sha256": _sha256_file(path),
        "bytes": path.stat().st_size,
    }


def _atomic_json(path: Path, payload: dict[str, Any], overwrite: bool) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"refusing to overwrite {path.name}")
    path.parent.mkdir(parents=True, exist_ok=True)
    rendered = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    descriptor, temporary = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary_path = Path(temporary)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as sink:
            sink.write(rendered)
            sink.flush()
            os.fsync(sink.fileno())
        os.replace(temporary_path, path)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()


def read_seed_matrix(path: Path, expected_sha256: str | None = None) -> list[int]:
    """Strictly parse a whitespace-separated square symmetric 0/1 matrix."""

    if not path.is_file():
        raise AuditError(f"matrix input is not a regular file: {path.name}")
    if expected_sha256 is not None and _sha256_file(path) != expected_sha256:
        raise AuditError("matrix SHA-256 mismatch")
    try:
        text = path.read_text(encoding="ascii")
    except UnicodeError as error:
        raise AuditError("matrix is not ASCII") from error
    tokens = text.split()
    if any(token not in {"0", "1"} for token in tokens):
        raise AuditError("matrix contains a token other than 0 or 1")
    order = math.isqrt(len(tokens))
    if order * order != len(tokens) or order == 0:
        raise AuditError("matrix entries do not form a nonempty square")
    rows: list[int] = []
    for u in range(order):
        row = 0
        for v, token in enumerate(tokens[u * order : (u + 1) * order]):
            if token == "1":
                row |= 1 << v
        rows.append(row)
    for u, row in enumerate(rows):
        if (row >> u) & 1:
            raise AuditError("matrix diagonal is nonzero")
        for v in range(u):
            if ((row >> v) & 1) != ((rows[v] >> u) & 1):
                raise AuditError("matrix is not symmetric")
    return rows


def _parse_mask(raw: Any) -> int:
    if isinstance(raw, bool):
        raise AuditError("universal bank contains a Boolean mask")
    if isinstance(raw, int):
        return raw
    if not isinstance(raw, str):
        raise AuditError("universal bank contains a non-integer mask")
    value = raw.strip().lower()
    if value.startswith("0x"):
        value = value[2:]
    if not value or any(character not in "0123456789abcdef" for character in value):
        raise AuditError("universal bank contains malformed hexadecimal")
    return int(value, 16)


def _ordered_masks_sha256(masks: Iterable[int]) -> str:
    digest = hashlib.sha256()
    for mask in masks:
        digest.update(f"{mask:016x}\n".encode("ascii"))
    return digest.hexdigest()


def load_ordered_bank(
    path: Path,
    *,
    order: int,
    set_size: int,
    expected_sha256: str | None = None,
    expected_ordered_sha256: str | None = None,
) -> tuple[list[int], str]:
    """Independently parse and preserve the JSON bank's stored mask order."""

    if not path.is_file():
        raise AuditError(f"universal-bank input is not a regular file: {path.name}")
    file_hash = _sha256_file(path)
    if expected_sha256 is not None and file_hash != expected_sha256:
        raise AuditError("universal-bank SHA-256 mismatch")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (UnicodeError, json.JSONDecodeError) as error:
        raise AuditError("universal bank is not valid UTF-8 JSON") from error
    if not isinstance(payload, dict) or not isinstance(payload.get("masks"), list):
        raise AuditError("universal bank lacks an ordered masks array")
    masks = [_parse_mask(raw) for raw in payload["masks"]]
    if len(masks) != len(set(masks)):
        raise AuditError("universal bank contains a duplicate mask")
    for mask in masks:
        if mask < 0 or mask >> order or mask.bit_count() != set_size:
            raise AuditError("universal bank contains a mask of the wrong order/size")
    ordered_hash = _ordered_masks_sha256(masks)
    recorded_hash = payload.get("masks_sha256")
    if recorded_hash is not None and recorded_hash != ordered_hash:
        raise AuditError("universal-bank recorded ordered digest mismatch")
    if expected_ordered_sha256 is not None and ordered_hash != expected_ordered_sha256:
        raise AuditError("universal-bank ordered SHA-256 mismatch")
    return masks, ordered_hash


def lexicographic_edge_variables(order: int) -> tuple[dict[Edge, int], tuple[Edge, ...]]:
    if order < 2:
        raise AuditError("graph order must be at least two")
    pairs = tuple(itertools.combinations(range(order), 2))
    variables = {edge: index for index, edge in enumerate(pairs, start=1)}
    if list(variables.values()) != list(range(1, len(pairs) + 1)):
        raise AssertionError("lexicographic edge allocation failed")
    return variables, pairs


def _mapping_sha256(variables: dict[Edge, int]) -> str:
    digest = hashlib.sha256()
    for (u, v), variable in sorted(variables.items()):
        digest.update(f"x {u} {v} {variable}\n".encode("ascii"))
    return digest.hexdigest()


def _edge_set(rows: Sequence[int]) -> frozenset[Edge]:
    order = len(rows)
    return frozenset(
        (u, v)
        for u in range(order)
        for v in range(u + 1, order)
        if (rows[u] >> v) & 1
    )


def build_reconstruction_plan(
    rows: Sequence[int], spec: FormulaSpec
) -> ReconstructionPlan:
    """Plan both counter allocations without using IDPool or CardEnc."""

    if len(rows) != spec.order:
        raise AuditError("matrix order differs from formula specification")
    variables, pairs = lexicographic_edge_variables(spec.order)
    original_edges = _edge_set(rows)
    if spec.fixed_edge not in original_edges:
        raise AuditError("fixed branch edge is absent from the matrix")
    residual_edges = tuple(sorted(original_edges - {spec.fixed_edge}))
    if not 0 <= spec.residual_deletions <= len(residual_edges):
        raise AuditError("invalid exact residual-deletion cardinality")

    counter_inputs = tuple(-variables[edge] for edge in residual_edges)
    nonedges = set(pairs) - set(original_edges)
    counter_input_edges = {
        pairs[abs(literal) - 1] for literal in counter_inputs
    }
    if counter_input_edges != set(residual_edges):
        raise AuditError("exact counter does not bind exactly the residual input edges")
    if counter_input_edges & nonedges:
        raise AuditError("an original nonedge entered the exact-deletion counter")
    if spec.fixed_edge in counter_input_edges:
        raise AuditError("the fixed branch deletion entered the residual counter")

    exact = encode_equals(
        counter_inputs, spec.residual_deletions, top_id=len(pairs)
    )
    current_top = exact.top_id
    degree_counts: list[int] = []
    for vertex in range(spec.order):
        literals = tuple(
            variables[(min(vertex, other), max(vertex, other))]
            for other in range(spec.order)
            if other != vertex
        )
        block = encode_atmost(literals, spec.degree_cap, top_id=current_top)
        if block.base_top_id != current_top:
            raise AuditError("degree-counter auxiliary ranges overlap")
        current_top = block.top_id
        degree_counts.append(len(block.clauses))

    triangles = math.comb(spec.order, 3)
    structural = triangles + len(exact.clauses) + 1
    return ReconstructionPlan(
        spec=spec,
        variables=variables,
        pairs=pairs,
        original_edges=original_edges,
        residual_edges=residual_edges,
        exact_clauses=exact.clauses,
        structural_top=exact.top_id,
        degree_block_clause_counts=tuple(degree_counts),
        maximum_variable=current_top,
        triangle_clause_count=triangles,
        structural_clause_count=structural,
        degree_clause_count=sum(degree_counts),
    )


def validate_core(
    label: str, raw_edges: Sequence[Edge], plan: ReconstructionPlan
) -> tuple[tuple[Edge, ...], tuple[int, ...], str]:
    if not _SAFE_LABEL.fullmatch(label) or ".." in label:
        raise AuditError("expected label is not a safe artifact label")
    edges: list[Edge] = []
    for raw in raw_edges:
        if (
            not isinstance(raw, (list, tuple))
            or len(raw) != 2
            or any(not isinstance(value, int) or isinstance(value, bool) for value in raw)
        ):
            raise AuditError("core contains a malformed edge")
        u, v = raw
        if not (0 <= u < v < plan.spec.order):
            raise AuditError("core edge is not a canonical in-range pair")
        edges.append((u, v))
    if not edges or len(edges) > plan.spec.residual_deletions:
        raise AuditError("core size is outside the exact-budget range")
    if edges != sorted(edges) or len(edges) != len(set(edges)):
        raise AuditError("core edges must be unique and lexicographically sorted")
    if not set(edges).issubset(plan.residual_edges):
        raise AuditError("core contains a non-residual edge")
    units = tuple(-plan.variables[edge] for edge in edges)
    identity = {
        "formula_fingerprint_sha256": EXPECTED_FORMULA_FINGERPRINT,
        "deletion_edges": [list(edge) for edge in edges],
        "assumption_units": list(units),
        "semantics": "for every e in K, d_e=true is encoded as unit -x_e",
    }
    return tuple(edges), units, _canonical_sha256(identity)


def iter_expected_clauses(
    plan: ReconstructionPlan,
    masks: Sequence[int],
    assumption_units: Sequence[int],
) -> Iterator[tuple[str, list[int]]]:
    """Yield the exact production clause order from independent components."""

    variables = plan.variables
    order = plan.spec.order
    for a, b, c in itertools.combinations(range(order), 3):
        yield "triangles", [
            -variables[(a, b)],
            -variables[(a, c)],
            -variables[(b, c)],
        ]
    for clause in plan.exact_clauses:
        yield "exact_residual_deletions", clause
    yield "fixed_branch_unit", [-variables[plan.spec.fixed_edge]]

    current_top = plan.structural_top
    for vertex in range(order):
        literals = tuple(
            variables[(min(vertex, other), max(vertex, other))]
            for other in range(order)
            if other != vertex
        )
        block = encode_atmost(literals, plan.spec.degree_cap, top_id=current_top)
        if len(block.clauses) != plan.degree_block_clause_counts[vertex]:
            raise AuditError("degree-counter reconstruction is nondeterministic")
        current_top = block.top_id
        for clause in block.clauses:
            yield f"degree_atmost_vertex_{vertex}", clause
    if current_top != plan.maximum_variable:
        raise AuditError("degree-counter terminal variable changed during replay")

    for mask in masks:
        vertices = [vertex for vertex in range(order) if (mask >> vertex) & 1]
        if len(vertices) != plan.spec.bank_set_size:
            raise AuditError("universal mask size changed during clause replay")
        yield "ordered_universal_I18", [
            variables[(u, v)] for u, v in itertools.combinations(vertices, 2)
        ]
    for literal in assumption_units:
        yield "candidate_units", [literal]


def _canonical_clause_line(clause: Sequence[int]) -> bytes:
    if not clause or any(
        not isinstance(literal, int) or isinstance(literal, bool) or literal == 0
        for literal in clause
    ):
        raise AuditError("independent reconstruction emitted an invalid clause")
    return (" ".join(map(str, clause)) + " 0\n").encode("ascii")


def compare_gzip_dimacs(
    cnf_path: Path,
    plan: ReconstructionPlan,
    masks: Sequence[int],
    assumption_units: Sequence[int],
) -> CnfAudit:
    """Compare the decompressed DIMACS bytes to the independent clause stream."""

    if not cnf_path.is_file():
        raise AuditError(f"CNF is not a regular file: {cnf_path.name}")
    total_clauses = (
        plan.common_clause_count_without_bank + len(masks) + len(assumption_units)
    )
    expected_header = f"p cnf {plan.maximum_variable} {total_clauses}\n".encode("ascii")
    raw_digest = hashlib.sha256()
    structural_digest = hashlib.sha256()
    degree_digest = hashlib.sha256()
    raw_bytes = 0
    lines = 0

    try:
        with gzip.open(cnf_path, "rb") as source:
            header = source.readline()
            raw_digest.update(header)
            raw_bytes += len(header)
            lines += 1
            if header != expected_header:
                raise AuditError(
                    "DIMACS header mismatch: expected "
                    f"{expected_header.decode('ascii').strip()!r}"
                )
            for clause_index, (block, clause) in enumerate(
                iter_expected_clauses(plan, masks, assumption_units), start=1
            ):
                if any(abs(literal) > plan.maximum_variable for literal in clause):
                    raise AuditError("reconstructed literal exceeds the DIMACS header")
                expected = _canonical_clause_line(clause)
                actual = source.readline()
                raw_digest.update(actual)
                raw_bytes += len(actual)
                lines += 1
                if actual != expected:
                    raise AuditError(
                        f"DIMACS clause mismatch at index {clause_index} in {block}"
                    )
                if block in {
                    "triangles",
                    "exact_residual_deletions",
                    "fixed_branch_unit",
                }:
                    structural_digest.update(b"c " + expected)
                elif block.startswith("degree_atmost_vertex_"):
                    degree_digest.update(b"c " + expected)
            extra = source.readline()
            if extra:
                raise AuditError("DIMACS contains extra clauses or trailing bytes")
    except (OSError, EOFError) as error:
        raise AuditError("CNF is not a valid complete gzip stream") from error

    if lines != total_clauses + 1:
        raise AuditError("DIMACS line count differs from its clause count")
    return CnfAudit(
        variables=plan.maximum_variable,
        clauses=total_clauses,
        lines=lines,
        uncompressed_bytes=raw_bytes,
        uncompressed_sha256=raw_digest.hexdigest(),
        gzip_bytes=cnf_path.stat().st_size,
        gzip_sha256=_sha256_file(cnf_path),
        structural_clauses_sha256=structural_digest.hexdigest(),
        degree_clauses_sha256=degree_digest.hexdigest(),
    )


def reconstructed_formula_fingerprint(
    plan: ReconstructionPlan,
    *,
    input_sha256: str,
    bank_sha256: str,
    masks: Sequence[int],
    ordered_masks_sha256: str,
    audit: CnfAudit,
) -> tuple[str, dict[str, Any]]:
    basis = {
        "schema": FORMULA_SCHEMA,
        "input_sha256": input_sha256,
        "order": plan.spec.order,
        "fixed_deleted_edge": list(plan.spec.fixed_edge),
        "residual_deletion_literal_semantics": "d_e := -x_e",
        "exact_residual_deletions": plan.spec.residual_deletions,
        "edge_variable_mapping_sha256": _mapping_sha256(plan.variables),
        "structural_clauses": plan.structural_clause_count,
        "structural_clauses_sha256": audit.structural_clauses_sha256,
        "degree_clauses": plan.degree_clause_count,
        "degree_clauses_sha256": audit.degree_clauses_sha256,
        "universal_I18_bank": {
            "sha256": bank_sha256,
            "masks": len(masks),
            "ordered_masks_sha256": ordered_masks_sha256,
        },
        "maximum_variable": plan.maximum_variable,
        "total_clauses": plan.common_clause_count_without_bank + len(masks),
        "learned_core_clauses_installed": 0,
    }
    return _canonical_sha256(basis), basis


def _require_mapping(value: Any, description: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise AuditError(f"{description} is not a JSON object")
    return value


def validate_manifest(
    path: Path,
    *,
    label: str,
    edges: Sequence[Edge],
    units: Sequence[int],
    candidate_sha256: str,
    formula_fingerprint: str,
    matrix_sha256: str,
    bank_sha256: str,
    ordered_masks_sha256: str,
    masks: Sequence[int],
    audit: CnfAudit,
) -> dict[str, Any]:
    try:
        manifest = _require_mapping(
            json.loads(path.read_text(encoding="utf-8")), "manifest"
        )
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise AuditError("manifest is unreadable or invalid JSON") from error
    if manifest.get("schema") != MANIFEST_SCHEMA:
        raise AuditError("manifest schema mismatch")
    if manifest.get("status") != "FROZEN_DIMACS_EXPORTED_UNCHECKED":
        raise AuditError("manifest status mismatch")
    candidate = _require_mapping(manifest.get("candidate"), "manifest candidate")
    expected_candidate = {
        "label": label,
        "deletion_edges": [list(edge) for edge in edges],
        "size": len(edges),
        "assumption_units": list(units),
        "candidate_sha256": candidate_sha256,
    }
    for key, value in expected_candidate.items():
        if candidate.get(key) != value:
            raise AuditError(f"manifest candidate {key} mismatch")
    if candidate.get("unit_semantics") != "d_e=true is the DIMACS unit -x_e":
        raise AuditError("manifest candidate unit semantics mismatch")
    if candidate.get("minimality_claim") is not False:
        raise AuditError("manifest improperly claims candidate minimality")
    if candidate.get("pilot_anchor_proves_candidate_UNSAT") is not False:
        raise AuditError("manifest improperly transfers pilot UNSAT to a subset")

    common = _require_mapping(manifest.get("common_formula"), "manifest formula")
    expected_common = {
        "schema": FORMULA_SCHEMA,
        "formula_fingerprint_sha256": formula_fingerprint,
        "maximum_variable": audit.variables,
        "materialized_structural_and_degree_clauses": (
            PRODUCTION_STRUCTURAL_CLAUSES + PRODUCTION_DEGREE_CLAUSES
        ),
        "materialized_universal_I18_clauses": len(masks),
        "common_clause_count": audit.clauses - len(units),
        "formula_is_relaxation_of_target": True,
        "learned_core_clauses_installed": 0,
    }
    for key, value in expected_common.items():
        if common.get(key) != value:
            raise AuditError(f"manifest common-formula {key} mismatch")
    if common.get("clause_order") != [
        "structural clauses including exact-six and fixed branch unit",
        "degree-cap clauses",
        "universal I18 clauses in ordered-bank order",
        "candidate deletion units in lexicographic edge order",
    ]:
        raise AuditError("manifest clause-order record mismatch")

    dimacs = _require_mapping(manifest.get("dimacs"), "manifest DIMACS")
    expected_dimacs = {
        "variables": audit.variables,
        "clauses": audit.clauses,
        "header_and_clause_lines": audit.lines,
        "uncompressed_sha256": audit.uncompressed_sha256,
        "gzip_sha256": audit.gzip_sha256,
        "uncompressed_bytes": audit.uncompressed_bytes,
        "gzip_bytes": audit.gzip_bytes,
    }
    for key, value in expected_dimacs.items():
        if dimacs.get(key) != value:
            raise AuditError(f"manifest DIMACS {key} mismatch")

    inputs = _require_mapping(manifest.get("inputs"), "manifest inputs")
    matrix = _require_mapping(inputs.get("matrix"), "manifest matrix")
    bank = _require_mapping(inputs.get("universal_bank"), "manifest bank")
    if matrix.get("sha256") != matrix_sha256:
        raise AuditError("manifest matrix digest mismatch")
    if bank.get("sha256") != bank_sha256:
        raise AuditError("manifest bank digest mismatch")
    if bank.get("ordered_masks_sha256") != ordered_masks_sha256:
        raise AuditError("manifest bank-order digest mismatch")
    if bank.get("masks") != len(masks):
        raise AuditError("manifest bank count mismatch")
    if manifest.get("global_ramsey_implication") is not None:
        raise AuditError("manifest improperly records a global Ramsey implication")
    return manifest


def validate_result(
    path: Path,
    *,
    manifest_path: Path | None,
    manifest: dict[str, Any] | None,
) -> dict[str, Any]:
    try:
        result = _require_mapping(
            json.loads(path.read_text(encoding="utf-8")), "result"
        )
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise AuditError("result is unreadable or invalid JSON") from error
    if result.get("schema") != RESULT_SCHEMA:
        raise AuditError("result schema mismatch")
    if manifest is None or manifest_path is None:
        raise AuditError("a result can be checked only together with its manifest")
    if result.get("candidate") != manifest.get("candidate"):
        raise AuditError("result candidate differs from manifest candidate")
    if result.get("dimacs") != manifest.get("dimacs"):
        raise AuditError("result DIMACS record differs from manifest")
    manifest_ref = _require_mapping(result.get("manifest"), "result manifest")
    if manifest_ref.get("sha256") != _sha256_file(manifest_path):
        raise AuditError("result manifest digest mismatch")
    if result.get("minimality_claim") is not False:
        raise AuditError("result improperly claims candidate minimality")
    if result.get("global_ramsey_implication") is not None:
        raise AuditError("result improperly records a global Ramsey implication")
    proof_verified = result.get("proof_verified")
    if not isinstance(proof_verified, bool):
        raise AuditError("result proof_verified is not Boolean")
    local_exclusion = result.get(
        "local_branch1_exact_six_superset_exclusion_proved"
    )
    if not isinstance(local_exclusion, bool):
        raise AuditError("result local exclusion bit is not Boolean")
    if proof_verified:
        if result.get("status") != (
            "UNSAT_PROOF_VERIFIED_LOCAL_BRANCH1_EXACT_SIX_CORE"
        ):
            raise AuditError("verified result has an inconsistent status")
        if local_exclusion is not True:
            raise AuditError("verified result lacks its local exclusion bit")
        external = _require_mapping(result.get("external_proof"), "external proof")
        checker = _require_mapping(result.get("drat_check"), "DRAT check")
        if external.get("status") != "UNSAT_PROOF_WRITTEN":
            raise AuditError("verified result lacks completed UNSAT telemetry")
        if external.get("exitcode") != 20:
            raise AuditError("verified result records a non-UNSAT solver exit code")
        if checker.get("status") != "VERIFIED":
            raise AuditError("verified result lacks a VERIFIED checker status")
        if checker.get("exitcode") != 0:
            raise AuditError("verified result records a nonzero checker exit code")
        transcript = checker.get("stdout_tail")
        if not isinstance(transcript, str) or not any(
            line.strip() == "s VERIFIED" for line in transcript.splitlines()
        ):
            raise AuditError("verified result lacks an exact s VERIFIED transcript line")
    else:
        if result.get("status") == (
            "UNSAT_PROOF_VERIFIED_LOCAL_BRANCH1_EXACT_SIX_CORE"
        ):
            raise AuditError("unverified result uses the verified status")
        if local_exclusion:
            raise AuditError("unverified result improperly claims local exclusion")
        checker = result.get("drat_check")
        if isinstance(checker, dict) and checker.get("status") == "VERIFIED":
            raise AuditError("unverified result records a VERIFIED checker")
    return result


def audit_production_cnf(
    *,
    cnf_path: Path,
    matrix_path: Path,
    bank_path: Path,
    label: str,
    raw_core: Sequence[Edge],
    manifest_path: Path | None = None,
    result_path: Path | None = None,
    expected_raw_sha256: str | None = None,
    expected_gzip_sha256: str | None = None,
) -> dict[str, Any]:
    spec = FormulaSpec(
        order=PRODUCTION_ORDER,
        fixed_edge=PRODUCTION_FIXED_EDGE,
        residual_deletions=PRODUCTION_RESIDUAL_DELETIONS,
        degree_cap=PRODUCTION_DEGREE_CAP,
        bank_set_size=PRODUCTION_BANK_SET_SIZE,
    )
    rows = read_seed_matrix(matrix_path, EXPECTED_INPUT_SHA256)
    masks, ordered_masks_sha256 = load_ordered_bank(
        bank_path,
        order=spec.order,
        set_size=spec.bank_set_size,
        expected_sha256=EXPECTED_BANK_SHA256,
        expected_ordered_sha256=EXPECTED_ORDERED_MASKS_SHA256,
    )
    plan = build_reconstruction_plan(rows, spec)
    if len(plan.original_edges) != PRODUCTION_INPUT_EDGES:
        raise AuditError("production matrix edge count mismatch")
    if len(plan.residual_edges) != PRODUCTION_RESIDUAL_EDGES:
        raise AuditError("production residual edge count mismatch")
    if len(plan.pairs) != PRODUCTION_EDGE_VARIABLES:
        raise AuditError("production edge-variable count mismatch")
    if _mapping_sha256(plan.variables) != EXPECTED_MAPPING_SHA256:
        raise AuditError("production edge-variable mapping digest mismatch")
    if plan.structural_clause_count != PRODUCTION_STRUCTURAL_CLAUSES:
        raise AuditError("production structural-clause count mismatch")
    if plan.degree_clause_count != PRODUCTION_DEGREE_CLAUSES:
        raise AuditError("production degree-clause count mismatch")
    if len(masks) != PRODUCTION_BANK_MASKS:
        raise AuditError("production universal-bank count mismatch")
    if plan.maximum_variable != PRODUCTION_MAXIMUM_VARIABLE:
        raise AuditError("production maximum-variable count mismatch")

    edges, units, candidate_sha256 = validate_core(label, raw_core, plan)
    audit = compare_gzip_dimacs(cnf_path, plan, masks, units)
    if audit.clauses != PRODUCTION_COMMON_CLAUSES + len(units):
        raise AuditError("production total-clause count mismatch")
    if audit.structural_clauses_sha256 != EXPECTED_STRUCTURAL_SHA256:
        raise AuditError("production structural-clause digest mismatch")
    if audit.degree_clauses_sha256 != EXPECTED_DEGREE_SHA256:
        raise AuditError("production degree-clause digest mismatch")
    if expected_raw_sha256 is not None and audit.uncompressed_sha256 != expected_raw_sha256:
        raise AuditError("CNF uncompressed SHA-256 differs from the expected value")
    if expected_gzip_sha256 is not None and audit.gzip_sha256 != expected_gzip_sha256:
        raise AuditError("CNF gzip SHA-256 differs from the expected value")

    formula_fingerprint, fingerprint_basis = reconstructed_formula_fingerprint(
        plan,
        input_sha256=EXPECTED_INPUT_SHA256,
        bank_sha256=EXPECTED_BANK_SHA256,
        masks=masks,
        ordered_masks_sha256=ordered_masks_sha256,
        audit=audit,
    )
    if formula_fingerprint != EXPECTED_FORMULA_FINGERPRINT:
        raise AuditError("independent formula fingerprint mismatch")

    manifest: dict[str, Any] | None = None
    if manifest_path is not None:
        manifest = validate_manifest(
            manifest_path,
            label=label,
            edges=edges,
            units=units,
            candidate_sha256=candidate_sha256,
            formula_fingerprint=formula_fingerprint,
            matrix_sha256=EXPECTED_INPUT_SHA256,
            bank_sha256=EXPECTED_BANK_SHA256,
            ordered_masks_sha256=ordered_masks_sha256,
            masks=masks,
            audit=audit,
        )
    result: dict[str, Any] | None = None
    if result_path is not None:
        result = validate_result(
            result_path, manifest_path=manifest_path, manifest=manifest
        )

    return {
        "schema": SCHEMA,
        "status": "VERIFIED_INDEPENDENT_CNF_RECONSTRUCTION",
        "claim_boundary": (
            "This independently authenticates the local branch-1 CNF and K "
            "binding. It does not itself check DRAT or imply R(3,18)>=101."
        ),
        "candidate": {
            "label": label,
            "deletion_edges": [list(edge) for edge in edges],
            "assumption_units": list(units),
            "candidate_sha256": candidate_sha256,
        },
        "formula": {
            "formula_fingerprint_sha256": formula_fingerprint,
            "edge_variable_mapping_sha256": fingerprint_basis[
                "edge_variable_mapping_sha256"
            ],
            "variables": audit.variables,
            "common_clauses": PRODUCTION_COMMON_CLAUSES,
            "candidate_unit_clauses": len(units),
            "total_clauses": audit.clauses,
            "triangle_clauses": plan.triangle_clause_count,
            "exact_six_counter_clauses": len(plan.exact_clauses),
            "fixed_negative_units": 1,
            "degree_clauses": plan.degree_clause_count,
            "degree_blocks": len(plan.degree_block_clause_counts),
            "universal_I18_clauses": len(masks),
            "original_nonedge_variables_in_deletion_counter": 0,
        },
        "cnf": {
            **_safe_artifact(cnf_path),
            "uncompressed_sha256": audit.uncompressed_sha256,
            "uncompressed_bytes": audit.uncompressed_bytes,
            "header_and_clause_lines": audit.lines,
        },
        "bindings": {
            "matrix": _safe_artifact(matrix_path),
            "universal_bank": {
                **_safe_artifact(bank_path),
                "ordered_masks_sha256": ordered_masks_sha256,
            },
            "manifest_checked": manifest is not None,
            "manifest": _safe_artifact(manifest_path) if manifest_path else None,
            "result_checked": result is not None,
            "result": _safe_artifact(result_path) if result_path else None,
            "result_claim_consistency_checked_not_drat_rechecked": result is not None,
        },
        "provenance": {
            "checker": _safe_artifact(Path(__file__).resolve()),
            "sequential_counter": _safe_artifact(
                Path(__file__).resolve().with_name("independent_seqcounter.py")
            ),
            "pysat_imported": False,
            "production_formula_builder_imported": False,
        },
    }


def _parse_core(value: str) -> tuple[Edge, ...]:
    try:
        edges = []
        for item in value.split(","):
            u, v = item.split("-", 1)
            edges.append((int(u), int(v)))
        return tuple(edges)
    except (TypeError, ValueError) as error:
        raise argparse.ArgumentTypeError(
            "core must be a comma-separated canonical edge list, e.g. 11-62,18-61"
        ) from error


def _hex_sha256(value: str) -> str:
    if not re.fullmatch(r"[0-9a-f]{64}", value):
        raise argparse.ArgumentTypeError("expected a lowercase hexadecimal SHA-256")
    return value


def main() -> None:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cnf", type=Path, required=True)
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
    parser.add_argument("--expected-label", required=True)
    parser.add_argument("--core", type=_parse_core, required=True)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--result", type=Path)
    parser.add_argument("--expected-raw-sha256", type=_hex_sha256)
    parser.add_argument("--expected-gzip-sha256", type=_hex_sha256)
    parser.add_argument("--json-output", type=Path)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    output_path = args.json_output
    if output_path is not None:
        checker_source = Path(__file__).resolve()
        input_paths = [
            args.cnf,
            args.matrix,
            args.universal_bank,
            checker_source,
            checker_source.with_name("independent_seqcounter.py"),
        ]
        input_paths.extend(
            path for path in (args.manifest, args.result) if path is not None
        )
        if output_path.resolve() in {path.resolve() for path in input_paths}:
            raise ValueError("JSON output collides with an input artifact")
        if output_path.exists() and not args.overwrite:
            raise FileExistsError(f"refusing to overwrite {output_path.name}")

    try:
        payload = audit_production_cnf(
            cnf_path=args.cnf,
            matrix_path=args.matrix,
            bank_path=args.universal_bank,
            label=args.expected_label,
            raw_core=args.core,
            manifest_path=args.manifest,
            result_path=args.result,
            expected_raw_sha256=args.expected_raw_sha256,
            expected_gzip_sha256=args.expected_gzip_sha256,
        )
    except Exception as error:
        failed = {
            "schema": SCHEMA,
            "status": "FAILED_INDEPENDENT_CNF_RECONSTRUCTION",
            "error_type": type(error).__name__,
            "error": str(error),
        }
        if output_path is not None:
            _atomic_json(output_path, failed, args.overwrite)
        print(json.dumps(failed, sort_keys=True), file=sys.stderr)
        raise SystemExit(1) from error

    if output_path is not None:
        _atomic_json(output_path, payload, args.overwrite)
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
