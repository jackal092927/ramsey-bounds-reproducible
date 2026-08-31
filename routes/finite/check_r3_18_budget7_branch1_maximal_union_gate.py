#!/usr/bin/env python3
"""Independently audit the branch-1 maximal-union exact-seven gate.

The checker has three fail-closed modes:

``cnf``
    Rebuild the four-family mask union and compare every generated DIMACS
    line to an independent clause stream.
``sat``
    Additionally require a complete gzip model, evaluate every exact clause,
    and check the represented graph directly.
``unsat``
    Additionally replay a nonempty proof with an authenticated, commit-pinned
    ``drat-trim`` binary.  Exit code or solver text alone is never accepted.

The checker never learns a cut.  A failure, timeout, malformed model, or
unchecked proof yields no SAT/UNSAT scientific conclusion.
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
import stat
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence


Edge = tuple[int, int]

AUDIT_SCHEMA = (
    "ramsey-r3-18-n100-exact-budget7-branch1-maximal-union-audit-v1"
)
GATE_SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch1-maximal-union-gate-v1"
ORDER = 100
TARGET = 18
COMMON_VARIABLES = 154_190
COMMON_CLAUSES = 718_452
COMMON_RAW_BYTES = 180_104_600
EDGE_VARIABLES = 4_950
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
UNION_MASKS = 530_525
APPENDED_MASKS = 278_754
WITNESSES_PER_PAIR = 98
SELECTOR_AUXILIARIES = EDGE_VARIABLES * WITNESSES_PER_PAIR
SELECTOR_CLAUSES = EDGE_VARIABLES * (1 + 2 * WITNESSES_PER_PAIR)
FINAL_VARIABLES = COMMON_VARIABLES + SELECTOR_AUXILIARIES
FINAL_CLAUSES = COMMON_CLAUSES + 4 + APPENDED_MASKS + SELECTOR_CLAUSES

EXPECTED_SEED_SHA256 = (
    "e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e"
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
EXPECTED_FIXED_ORDERED_SHA256 = (
    "1e9f89f40cd97a5f3b6fa93bb3c4835d45cadca8362e9d3150e90d4f385f6d8c"
)
EXPECTED_APLUS_SHA256 = (
    "835137c2df19bc851618761cc0af92400b3fa2677dd00c47101d1074c7406e8b"
)
EXPECTED_APLUS_ORDERED_SHA256 = (
    "a3cff8d8a4c77c6effb49c03e76065a17f754d0a7de727d229652276b6e8cda0"
)
EXPECTED_UNION_ORDERED_SHA256 = (
    "f5c1c60877306900c1aa81bd3a7f357c3d16464ad329c676639a6f6bda9a682d"
)
EXPECTED_APPEND_ORDERED_SHA256 = (
    "2242d10f9ea3cefedef7a8c02be9a7df41db3cdb6580733e3fca9391db46d1d4"
)
EXPECTED_BUDGET6_SHA256 = (
    "0abd30457c039c1c5fbba5890153c8a0c5d8558e196e7c0561410cefe37afa6a"
)
EXPECTED_SINGLETON_SHA256 = (
    "8ae4f0d9ea919c915ba642eb03ec3d418b4419a89781377509acbe925d89555a"
)
PINNED_DRAT_TRIM_COMMIT = "2e3b2dc0ecf938addbd779d42877b6ed69d9a985"
PINNED_DRAT_TRIM_SHA256 = frozenset(
    {
        "b535cc5334e97fba5b5db6013625c5a0b16ce348a98d59ff91b45a83fa56b39e",
        "31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4",
    }
)

_HEX25 = re.compile(r"[0-9a-f]{25}\Z", flags=re.ASCII)
_SHA = re.compile(r"[0-9a-f]{64}\Z", flags=re.ASCII)


class AuditError(ValueError):
    """A fail-closed independent audit error."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def canonical_sha256(payload: Any) -> str:
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return hashlib.sha256(raw).hexdigest()


def ordered_hash(masks: Iterable[int], width: int = 25) -> str:
    digest = hashlib.sha256()
    for mask in masks:
        digest.update(f"{mask:0{width}x}\n".encode("ascii"))
    return digest.hexdigest()


def _regular(path: Path, label: str, expected_sha256: str | None = None) -> bytes:
    try:
        metadata = os.lstat(path)
    except OSError as error:
        raise AuditError(f"cannot inspect {label}") from error
    if not stat.S_ISREG(metadata.st_mode):
        raise AuditError(f"{label} must be a regular non-symlink file")
    try:
        raw = path.read_bytes()
    except OSError as error:
        raise AuditError(f"cannot read {label}") from error
    if expected_sha256 is not None and hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise AuditError(f"{label} SHA-256 mismatch")
    return raw


def _json(raw: bytes, label: str) -> dict[str, Any]:
    def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in pairs:
            if key in result:
                raise AuditError(f"{label} has duplicate key {key!r}")
            result[key] = value
        return result

    try:
        payload = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=reject_duplicates,
            parse_constant=lambda value: (_ for _ in ()).throw(
                AuditError(f"{label} has non-finite number {value}")
            ),
        )
    except AuditError:
        raise
    except (UnicodeError, json.JSONDecodeError) as error:
        raise AuditError(f"{label} is not strict UTF-8 JSON") from error
    if not isinstance(payload, dict):
        raise AuditError(f"{label} root is not an object")
    return payload


def _seed_rows(path: Path) -> list[int]:
    raw = _regular(path, "seed matrix", EXPECTED_SEED_SHA256)
    if not raw.endswith(b"\n") or b"\r" in raw:
        raise AuditError("seed is not canonical LF-terminated data")
    try:
        lines = raw.decode("ascii").splitlines()
    except UnicodeError as error:
        raise AuditError("seed is not ASCII") from error
    if len(lines) != ORDER:
        raise AuditError("seed order mismatch")
    matrix: list[list[int]] = []
    for line in lines:
        fields = line.split()
        if len(fields) != ORDER or any(value not in {"0", "1"} for value in fields):
            raise AuditError("seed is not strict binary matrix data")
        matrix.append([int(value) for value in fields])
    rows = [0] * ORDER
    for u in range(ORDER):
        if matrix[u][u]:
            raise AuditError("seed diagonal is nonzero")
        for v in range(u + 1, ORDER):
            if matrix[u][v] != matrix[v][u]:
                raise AuditError("seed is asymmetric")
            if matrix[u][v]:
                rows[u] |= 1 << v
                rows[v] |= 1 << u
    if sum(row.bit_count() for row in rows) // 2 != 827:
        raise AuditError("seed edge count mismatch")
    return rows


def _cliques(rows: Sequence[int], size: int, candidates: int) -> Iterator[int]:
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


def _fixed_masks(rows: Sequence[int]) -> list[int]:
    full = (1 << ORDER) - 1
    complement = [full & ~(rows[v] | (1 << v)) for v in range(ORDER)]
    u, v = FIXED_EDGE
    candidates = full & ~(rows[u] | rows[v] | (1 << u) | (1 << v))
    endpoints = (1 << u) | (1 << v)
    masks = sorted(
        mask | endpoints
        for mask in _cliques(complement, TARGET - 2, candidates)
    )
    if len(masks) != FIXED_BASE_MASKS or ordered_hash(masks) != EXPECTED_FIXED_ORDERED_SHA256:
        raise AuditError("fixed-base exhaustive family mismatch")
    return masks


def _mask_file(
    path: Path,
    *,
    label: str,
    expected_sha256: str,
    expected_count: int,
    expected_ordered: str,
    universal: bool = False,
) -> list[int]:
    payload = _json(_regular(path, label, expected_sha256), label)
    values = payload.get("masks")
    if not isinstance(values, list) or len(values) != expected_count:
        raise AuditError(f"{label} count mismatch")
    masks: list[int] = []
    for value in values:
        if universal:
            if isinstance(value, bool) or not isinstance(value, (str, int)):
                raise AuditError("universal bank has malformed mask")
            encoded = str(value).strip().lower()
            if encoded.startswith("0x"):
                encoded = encoded[2:]
            if not encoded or any(c not in "0123456789abcdef" for c in encoded):
                raise AuditError("universal bank has malformed hexadecimal")
        else:
            if not isinstance(value, str) or not _HEX25.fullmatch(value):
                raise AuditError(f"{label} has a noncanonical mask")
            encoded = value
        mask = int(encoded, 16)
        if mask >> ORDER or mask.bit_count() != TARGET:
            raise AuditError(f"{label} mask has wrong order/size")
        masks.append(mask)
    if len(masks) != len(set(masks)):
        raise AuditError(f"{label} has duplicate masks")
    if not universal and masks != sorted(masks):
        raise AuditError(f"{label} masks are not sorted")
    if ordered_hash(masks, 16 if universal else 25) != expected_ordered:
        raise AuditError(f"{label} ordered digest mismatch")
    return masks


def rebuild_appended_masks(
    *,
    seed: Path,
    universal: Path,
    history: Path,
    aplus: Path,
) -> list[int]:
    rows = _seed_rows(seed)
    base = _mask_file(
        universal,
        label="universal bank",
        expected_sha256=EXPECTED_UNIVERSAL_SHA256,
        expected_count=UNIVERSAL_MASKS,
        expected_ordered=EXPECTED_UNIVERSAL_ORDERED_SHA256,
        universal=True,
    )
    historical = _mask_file(
        history,
        label="historical union",
        expected_sha256=EXPECTED_HISTORY_SHA256,
        expected_count=HISTORY_MASKS,
        expected_ordered=EXPECTED_HISTORY_ORDERED_SHA256,
    )
    plus = _mask_file(
        aplus,
        label="A+ batch",
        expected_sha256=EXPECTED_APLUS_SHA256,
        expected_count=APLUS_MASKS,
        expected_ordered=EXPECTED_APLUS_ORDERED_SHA256,
    )
    fixed = _fixed_masks(rows)
    base_set = set(base)
    union = sorted(base_set | set(historical) | set(fixed) | set(plus))
    appended = sorted(set(union) - base_set)
    if (
        len(union) != UNION_MASKS
        or ordered_hash(union) != EXPECTED_UNION_ORDERED_SHA256
        or len(appended) != APPENDED_MASKS
        or ordered_hash(appended) != EXPECTED_APPEND_ORDERED_SHA256
    ):
        raise AuditError("independently rebuilt mask union mismatch")
    return appended


def _variables() -> tuple[dict[Edge, int], tuple[Edge, ...]]:
    pairs = tuple(itertools.combinations(range(ORDER), 2))
    return {edge: index for index, edge in enumerate(pairs, start=1)}, pairs


def _hitting(mask: int, variables: dict[Edge, int]) -> bytes:
    vertices = [v for v in range(ORDER) if mask & (1 << v)]
    clause = [variables[edge] for edge in itertools.combinations(vertices, 2)]
    return (" ".join(map(str, clause)) + " 0\n").encode("ascii")


def _selector_lines(
    variables: dict[Edge, int], pairs: Sequence[Edge]
) -> Iterator[bytes]:
    for pair_index, (u, v) in enumerate(pairs):
        witnesses = [w for w in range(ORDER) if w not in {u, v}]
        first = COMMON_VARIABLES + 1 + pair_index * WITNESSES_PER_PAIR
        yvars = list(range(first, first + WITNESSES_PER_PAIR))
        yield (
            " ".join(map(str, [variables[(u, v)], *yvars])) + " 0\n"
        ).encode("ascii")
        for w, yvar in zip(witnesses, yvars, strict=True):
            yield f"{-yvar} {variables[tuple(sorted((u, w)))]} 0\n".encode("ascii")
            yield f"{-yvar} {variables[tuple(sorted((v, w)))]} 0\n".encode("ascii")


def validate_record(record_path: Path, cnf_path: Path, common_cnf: Path) -> dict[str, Any]:
    raw = _regular(record_path, "gate record")
    payload = _json(raw, "gate record")
    recorded_digest = payload.get("record_sha256")
    basis = dict(payload)
    basis.pop("record_sha256", None)
    if not isinstance(recorded_digest, str) or canonical_sha256(basis) != recorded_digest:
        raise AuditError("gate record canonical digest mismatch")
    generated = payload.get("generated_cnf")
    formula = payload.get("formula")
    common = payload.get("common_cnf")
    if (
        payload.get("schema") != GATE_SCHEMA
        or payload.get("status") != "MAXIMAL_UNION_CNF_READY_SOLVER_NOT_RUN"
        or payload.get("proof_verified") is not False
        or payload.get("learned_masks") != []
        or payload.get("exact_seven_repair_exists") is not None
        or payload.get("global_ramsey_implication") is not None
        or not isinstance(generated, dict)
        or generated.get("variables") != FINAL_VARIABLES
        or generated.get("clauses") != FINAL_CLAUSES
        or generated.get("header_and_clause_lines") != FINAL_CLAUSES + 1
        or not isinstance(formula, dict)
        or formula.get("final_variables") != FINAL_VARIABLES
        or formula.get("final_clauses") != FINAL_CLAUSES
        or formula.get("raw_cnf_sha256") != generated.get("sha256")
        or formula.get("raw_cnf_bytes") != generated.get("bytes")
        or not isinstance(common, dict)
        or common.get("sha256") != EXPECTED_COMMON_GZIP_SHA256
        or common.get("uncompressed_sha256") != EXPECTED_COMMON_RAW_SHA256
        or common.get("uncompressed_bytes") != COMMON_RAW_BYTES
    ):
        raise AuditError("gate record status/formula boundary mismatch")
    if generated.get("basename") != cnf_path.name or common.get("basename") != common_cnf.name:
        raise AuditError("gate record basenames do not bind supplied artifacts")
    if (
        not isinstance(generated.get("sha256"), str)
        or not _SHA.fullmatch(generated["sha256"])
        or generated.get("bytes") != cnf_path.stat().st_size
        or sha256_file(cnf_path) != generated["sha256"]
    ):
        raise AuditError("generated CNF identity mismatch")
    return payload


def audit_cnf(
    *,
    cnf: Path,
    common_cnf: Path,
    record: Path,
    seed: Path,
    universal: Path,
    history: Path,
    aplus: Path,
    budget6: Path,
    singleton_summary: Path,
) -> dict[str, Any]:
    _regular(cnf, "generated CNF")
    _regular(common_cnf, "common CNF", EXPECTED_COMMON_GZIP_SHA256)
    _regular(budget6, "budget-six summary", EXPECTED_BUDGET6_SHA256)
    singleton_raw = _regular(
        singleton_summary, "singleton proof summary", EXPECTED_SINGLETON_SHA256
    )
    singleton = _json(singleton_raw, "singleton proof summary")
    if (
        singleton.get("status")
        != "FOUR_SINGLETON_NO_GOODS_PROOF_VERIFIED_EXACT_SEVEN_UNKNOWN"
        or [item.get("assumption_units") for item in singleton.get("records", [])]
        != [[-unit] for unit in POSITIVE_UNITS]
    ):
        raise AuditError("singleton retention dependency mismatch")
    payload = validate_record(record, cnf, common_cnf)
    appended = rebuild_appended_masks(
        seed=seed, universal=universal, history=history, aplus=aplus
    )
    variables, pairs = _variables()
    digest = hashlib.sha256()
    lines = 0
    with cnf.open("rb") as actual, gzip.open(common_cnf, "rb") as base:
        expected_header = f"p cnf {FINAL_VARIABLES} {FINAL_CLAUSES}\n".encode("ascii")
        actual_header = actual.readline()
        digest.update(actual_header)
        lines += 1
        if actual_header != expected_header:
            raise AuditError("generated CNF header mismatch")
        old_header = base.readline()
        if old_header != f"p cnf {COMMON_VARIABLES} {COMMON_CLAUSES}\n".encode("ascii"):
            raise AuditError("common CNF header mismatch")
        base_digest = hashlib.sha256(old_header)
        base_bytes = len(old_header)
        base_lines = 1
        for index in range(1, COMMON_CLAUSES + 1):
            expected = base.readline()
            if not expected or not expected.endswith(b"\n") or b"\r" in expected:
                raise AuditError(f"common CNF malformed at clause {index}")
            base_digest.update(expected)
            base_bytes += len(expected)
            base_lines += 1
            observed = actual.readline()
            digest.update(observed)
            lines += 1
            if observed != expected:
                raise AuditError(f"common body mismatch at clause {index}")
        if base.readline():
            raise AuditError("common CNF has trailing bytes")
        if (
            base_digest.hexdigest() != EXPECTED_COMMON_RAW_SHA256
            or base_bytes != COMMON_RAW_BYTES
            or base_lines != COMMON_CLAUSES + 1
        ):
            raise AuditError("common CNF raw identity mismatch")

        expected_tail: Iterator[bytes] = itertools.chain(
            (f"{unit} 0\n".encode("ascii") for unit in POSITIVE_UNITS),
            (_hitting(mask, variables) for mask in appended),
            _selector_lines(variables, pairs),
        )
        for tail_index, expected in enumerate(expected_tail, start=1):
            observed = actual.readline()
            digest.update(observed)
            lines += 1
            if observed != expected:
                raise AuditError(f"augmented tail mismatch at clause {tail_index}")
        if actual.readline():
            raise AuditError("generated CNF has trailing clauses or bytes")
    generated = payload["generated_cnf"]
    if (
        lines != FINAL_CLAUSES + 1
        or digest.hexdigest() != generated["sha256"]
        or cnf.stat().st_size != generated["bytes"]
    ):
        raise AuditError("generated CNF final identity mismatch")
    return {
        "schema": AUDIT_SCHEMA,
        "status": "MAXIMAL_UNION_CNF_RECONSTRUCTED_BYTE_EXACT",
        "cnf": {
            "basename": cnf.name,
            "bytes": generated["bytes"],
            "sha256": generated["sha256"],
            "variables": FINAL_VARIABLES,
            "clauses": FINAL_CLAUSES,
            "header_and_clause_lines": lines,
        },
        "four_family_union": {
            "masks": UNION_MASKS,
            "ordered_masks_sha256": EXPECTED_UNION_ORDERED_SHA256,
            "appended_beyond_common": APPENDED_MASKS,
            "appended_ordered_masks_sha256": EXPECTED_APPEND_ORDERED_SHA256,
        },
        "full_maximality": {
            "pairs": EDGE_VARIABLES,
            "auxiliary_variables": SELECTOR_AUXILIARIES,
            "clauses": SELECTOR_CLAUSES,
        },
        "solver_invoked": False,
        "learned_masks": [],
        "exact_seven_repair_exists": None,
        "global_ramsey_implication": None,
    }


def parse_complete_model(
    model: Path, maximum_variable: int = FINAL_VARIABLES
) -> tuple[list[bool | None], dict[str, Any]]:
    compressed = _regular(model, "SAT model")
    try:
        raw = gzip.decompress(compressed)
        lines = raw.decode("ascii").splitlines()
    except (OSError, EOFError, UnicodeError) as error:
        raise AuditError("SAT model is not complete ASCII gzip data") from error
    if not raw.endswith(b"\n") or b"\r" in raw or not lines or lines[0] != "s SATISFIABLE":
        raise AuditError("SAT model has noncanonical status/line encoding")
    if any(not line.startswith("v ") for line in lines[1:]):
        raise AuditError("SAT model contains a non-assignment line")
    tokens: list[int] = []
    try:
        for line in lines[1:]:
            fields = line.split()[1:]
            if not fields:
                raise AuditError("SAT model has an empty assignment line")
            tokens.extend(int(field) for field in fields)
    except ValueError as error:
        raise AuditError("SAT model contains a non-integer") from error
    if not tokens or tokens[-1] != 0 or any(value == 0 for value in tokens[:-1]):
        raise AuditError("SAT model needs one final zero terminator")
    assignment: list[bool | None] = [None] * (maximum_variable + 1)
    for literal in tokens[:-1]:
        variable = abs(literal)
        if not 1 <= variable <= maximum_variable or assignment[variable] is not None:
            raise AuditError("SAT model has out-of-range or duplicate assignment")
        assignment[variable] = literal > 0
    if any(value is None for value in assignment[1:]):
        raise AuditError("SAT model does not assign every variable")
    return assignment, {
        "basename": model.name,
        "bytes": len(compressed),
        "sha256": hashlib.sha256(compressed).hexdigest(),
        "uncompressed_bytes": len(raw),
        "uncompressed_sha256": hashlib.sha256(raw).hexdigest(),
        "assignment_literals": maximum_variable,
    }


def evaluate_model(
    cnf: Path,
    assignment: Sequence[bool | None],
    *,
    maximum_variable: int = FINAL_VARIABLES,
    clauses: int = FINAL_CLAUSES,
) -> dict[str, Any]:
    checked = 0
    digest = hashlib.sha256()
    with cnf.open("rb") as source:
        header = source.readline()
        digest.update(header)
        if header != f"p cnf {maximum_variable} {clauses}\n".encode("ascii"):
            raise AuditError("model evaluator saw a different CNF header")
        for line in source:
            digest.update(line)
            checked += 1
            if not line.endswith(b"\n") or b"\r" in line:
                raise AuditError("CNF contains a noncanonical clause line")
            try:
                tokens = [int(token) for token in line.split()]
            except ValueError as error:
                raise AuditError("CNF contains a non-integer literal") from error
            if not tokens or tokens[-1] != 0 or any(value == 0 for value in tokens[:-1]):
                raise AuditError("CNF clause has malformed terminator")
            satisfied = False
            for literal in tokens[:-1]:
                variable = abs(literal)
                if not 1 <= variable <= maximum_variable:
                    raise AuditError("CNF literal exceeds formula variable range")
                value = assignment[variable]
                if value is None:
                    raise AuditError("model evaluation reached missing assignment")
                if bool(value) == (literal > 0):
                    satisfied = True
                    break
            if not satisfied:
                raise AuditError(f"SAT model falsifies clause {checked}")
    if checked != clauses:
        raise AuditError("model evaluator clause count mismatch")
    return {
        "all_clauses_satisfied": True,
        "clauses_evaluated": checked,
        "cnf_sha256_evaluated": digest.hexdigest(),
    }


def _independent_witness(rows: Sequence[int], target: int) -> tuple[int, int]:
    full = (1 << len(rows)) - 1
    complement = [full & ~(rows[v] | (1 << v)) for v in range(len(rows))]
    nodes = 0

    def visit(chosen: int, candidates: int, needed: int) -> int:
        nonlocal nodes
        nodes += 1
        if needed == 0:
            return chosen
        while candidates.bit_count() >= needed:
            bit = candidates & -candidates
            candidates ^= bit
            vertex = bit.bit_length() - 1
            result = visit(chosen | bit, candidates & complement[vertex], needed - 1)
            if result:
                return result
        return 0

    return visit(0, full, target), nodes


def semantic_graph_audit(
    assignment: Sequence[bool | None], seed_rows: Sequence[int]
) -> dict[str, Any]:
    variables, pairs = _variables()
    edges: set[Edge] = {
        edge for edge, variable in variables.items() if assignment[variable] is True
    }
    rows = [0] * ORDER
    for u, v in edges:
        rows[u] |= 1 << v
        rows[v] |= 1 << u
    triangles = 0
    for u, v, w in itertools.combinations(range(ORDER), 3):
        triangles += int((u, v) in edges and (u, w) in edges and (v, w) in edges)
    seed_edges = {
        (u, v)
        for u in range(ORDER)
        for v in range(u + 1, ORDER)
        if seed_rows[u] & (1 << v)
    }
    deletions = sorted(seed_edges - edges)
    degrees = [row.bit_count() for row in rows]
    violations = [
        (u, v)
        for u, v in pairs
        if (u, v) not in edges and not (rows[u] & rows[v])
    ]
    if (
        triangles != 0
        or len(deletions) != 7
        or FIXED_EDGE not in deletions
        or any(edge not in edges for edge in POSITIVE_EDGES)
        or max(degrees) > 17
        or violations
    ):
        raise AuditError("complete SAT model fails direct graph semantics")
    witness_mask, nodes = _independent_witness(rows, TARGET)
    witness = [v for v in range(ORDER) if witness_mask & (1 << v)]
    if witness_mask:
        for u, v in itertools.combinations(witness, 2):
            if (u, v) in edges:
                raise AuditError("independent-set search returned an adjacent pair")
    projection = hashlib.sha256(
        bytes(1 if edge in edges else 0 for edge in pairs)
    ).hexdigest()
    return {
        "primary_projection_sha256": projection,
        "edges": len(edges),
        "triangle_free": True,
        "triangles": triangles,
        "one_sided_seed_deletions": len(deletions),
        "deleted_seed_edges": [list(edge) for edge in deletions],
        "fixed_branch_edge_deleted": True,
        "four_positive_edges_retained": True,
        "maximum_degree": max(degrees),
        "degree_histogram": {
            str(degree): degrees.count(degree) for degree in sorted(set(degrees))
        },
        "maximal_triangle_free": True,
        "nonedges_without_common_neighbor": [],
        "independent_18_exists": bool(witness_mask),
        "independent_18_witness": witness or None,
        "independent_18_mask_hex": f"{witness_mask:025x}" if witness_mask else None,
        "independent_search_nodes": nodes,
    }


def audit_sat(
    *, cnf_audit: dict[str, Any], cnf: Path, model: Path, seed: Path
) -> dict[str, Any]:
    assignment, model_info = parse_complete_model(model)
    evaluation = evaluate_model(cnf, assignment)
    if evaluation["cnf_sha256_evaluated"] != cnf_audit["cnf"]["sha256"]:
        raise AuditError("model evaluator used a different CNF identity")
    graph = semantic_graph_audit(assignment, _seed_rows(seed))
    has_i18 = graph["independent_18_exists"]
    return {
        "schema": AUDIT_SCHEMA,
        "status": (
            "SAT_MODEL_VERIFIED_I18_WITNESS_NO_LEARNING"
            if has_i18
            else "SAT_EXACT7_TARGET_CANDIDATE_REQUIRES_INDEPENDENT_PROMOTION"
        ),
        "cnf_audit": cnf_audit,
        "model": model_info,
        "clause_evaluation": evaluation,
        "graph_semantics": graph,
        "learned_masks": [],
        "branch1_closed": False,
        "exact_seven_repair_exists": None,
        "global_ramsey_implication": None,
        "claim_boundary": (
            "An I18-bearing SAT model is relaxation telemetry only.  A model "
            "without I18 is a candidate exact-seven target requiring an "
            "independent publication promotion workflow."
        ),
    }


def _stage_executable(source: Path, destination: Path) -> dict[str, Any]:
    raw = _regular(source, "drat-trim executable")
    digest = hashlib.sha256(raw).hexdigest()
    if digest not in PINNED_DRAT_TRIM_SHA256 or not os.access(source, os.X_OK):
        raise AuditError("drat-trim executable is not in the pinned allowlist")
    marker = source.resolve().parent / "SOURCE_COMMIT"
    marker_raw = _regular(marker, "drat-trim SOURCE_COMMIT marker")
    if marker_raw != (PINNED_DRAT_TRIM_COMMIT + "\n").encode("ascii"):
        raise AuditError("drat-trim SOURCE_COMMIT mismatch")
    with destination.open("xb") as sink:
        sink.write(raw)
        sink.flush()
        os.fsync(sink.fileno())
    destination.chmod(0o700)
    if sha256_file(destination) != digest:
        raise AuditError("staged drat-trim identity changed")
    return {
        "basename": source.name,
        "sha256": digest,
        "source_commit": PINNED_DRAT_TRIM_COMMIT,
    }


def _stage_proof(source: Path, destination: Path, max_raw_bytes: int) -> dict[str, Any]:
    compressed = _regular(source, "DRAT proof")
    if not compressed:
        raise AuditError("DRAT proof is empty")
    source_digest = hashlib.sha256(compressed).hexdigest()
    raw_digest = hashlib.sha256()
    raw_bytes = 0
    try:
        input_stream: Any
        if source.suffix == ".gz":
            input_stream = gzip.open(source, "rb")
        else:
            input_stream = source.open("rb")
        with input_stream, destination.open("xb") as sink:
            while True:
                block = input_stream.read(1024 * 1024)
                if not block:
                    break
                raw_bytes += len(block)
                if raw_bytes > max_raw_bytes:
                    raise AuditError("DRAT proof exceeded the fixed raw-byte cap")
                raw_digest.update(block)
                sink.write(block)
            sink.flush()
            os.fsync(sink.fileno())
    except Exception:
        destination.unlink(missing_ok=True)
        raise
    if raw_bytes <= 0:
        destination.unlink(missing_ok=True)
        raise AuditError("DRAT proof decompresses to empty data")
    return {
        "basename": source.name,
        "bytes": len(compressed),
        "sha256": source_digest,
        "uncompressed_bytes": raw_bytes,
        "uncompressed_sha256": raw_digest.hexdigest(),
    }


def replay_unsat(
    *,
    cnf_audit: dict[str, Any],
    cnf: Path,
    proof: Path,
    drat_trim: Path,
    wall_seconds: float,
    max_proof_raw_bytes: int,
) -> dict[str, Any]:
    if (
        not isinstance(wall_seconds, (int, float))
        or isinstance(wall_seconds, bool)
        or not math.isfinite(wall_seconds)
        or wall_seconds <= 0
    ):
        raise AuditError("proof replay wall limit must be finite and positive")
    cnf_sha = cnf_audit["cnf"]["sha256"]
    if sha256_file(cnf) != cnf_sha:
        raise AuditError("CNF changed before proof replay")
    with tempfile.TemporaryDirectory(prefix="ramsey-maximal-union-proof-") as name:
        private = Path(name)
        checker_path = private / "drat-trim"
        proof_path = private / "proof.drat"
        checker = _stage_executable(drat_trim, checker_path)
        proof_info = _stage_proof(proof, proof_path, max_proof_raw_bytes)
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
                [str(checker_path), str(cnf), str(proof_path)],
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                start_new_session=True,
                env=environment,
            )
            try:
                stdout, stderr = process.communicate(timeout=wall_seconds)
            except subprocess.TimeoutExpired as error:
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                process.communicate()
                raise AuditError("drat-trim replay timed out; result is UNKNOWN") from error
        except OSError as error:
            raise AuditError("could not execute staged drat-trim") from error
    if sha256_file(cnf) != cnf_sha:
        raise AuditError("CNF changed during proof replay")
    verified = [line for line in stdout.splitlines() if line == "s VERIFIED"]
    if process.returncode != 0 or verified != ["s VERIFIED"]:
        raise AuditError("drat-trim did not return one checked s VERIFIED endpoint")
    return {
        "schema": AUDIT_SCHEMA,
        "status": "UNSAT_PROOF_VERIFIED_SCOPED_BRANCH1_MAXIMAL_UNION_RELAXATION",
        "cnf_audit": cnf_audit,
        "proof": proof_info,
        "checker": {
            **checker,
            "exitcode": process.returncode,
            "verified_lines": verified,
            "stdout_sha256": hashlib.sha256(stdout.encode()).hexdigest(),
            "stderr_sha256": hashlib.sha256(stderr.encode()).hexdigest(),
        },
        "proof_verified": True,
        "branch1_closed_by_this_result": True,
        "other_triangle_edge_branches_closed_by_this_result": False,
        "exact_seven_all_branches_closed": False,
        "global_ramsey_implication": None,
        "learned_masks": [],
        "claim_boundary": (
            "This endpoint applies only to fixed deletion (97,99).  No seed "
            "automorphism or branch symmetry transfers it to the (97,98) or "
            "(98,99) branches."
        ),
    }


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
    parser.add_argument("mode", choices=("cnf", "sat", "unsat"))
    parser.add_argument("--cnf", type=Path, required=True)
    parser.add_argument("--record", type=Path, required=True)
    parser.add_argument("--common-cnf", type=Path, required=True)
    parser.add_argument(
        "--seed",
        type=Path,
        default=here / "certificates" / "r3_18_n100_nearmiss.txt",
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
    parser.add_argument(
        "--budget6-summary", type=Path, default=here / "r3_18_budget6_summary.json"
    )
    parser.add_argument(
        "--singleton-summary",
        type=Path,
        default=here / "r3_18_budget7_branch1_core_proof_summary.json",
    )
    parser.add_argument("--model", type=Path)
    parser.add_argument("--proof", type=Path)
    parser.add_argument("--drat-trim", type=Path)
    parser.add_argument("--wall-seconds", type=float, default=86_400.0)
    parser.add_argument("--max-proof-raw-bytes", type=int, default=50_000_000_000)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)

    common = dict(
        cnf=_absolute_lexical(args.cnf),
        common_cnf=_absolute_lexical(args.common_cnf),
        record=_absolute_lexical(args.record),
        seed=_absolute_lexical(args.seed),
        universal=_absolute_lexical(args.universal),
        history=_absolute_lexical(args.history),
        aplus=_absolute_lexical(args.Aplus),
        budget6=_absolute_lexical(args.budget6_summary),
        singleton_summary=_absolute_lexical(args.singleton_summary),
    )
    cnf_audit = audit_cnf(**common)
    if args.mode == "cnf":
        result = cnf_audit
    elif args.mode == "sat":
        if args.model is None:
            parser.error("sat mode requires --model")
        result = audit_sat(
            cnf_audit=cnf_audit,
            cnf=_absolute_lexical(args.cnf),
            model=_absolute_lexical(args.model),
            seed=_absolute_lexical(args.seed),
        )
    else:
        if args.proof is None or args.drat_trim is None:
            parser.error("unsat mode requires --proof and --drat-trim")
        result = replay_unsat(
            cnf_audit=cnf_audit,
            cnf=_absolute_lexical(args.cnf),
            proof=_absolute_lexical(args.proof),
            drat_trim=_absolute_lexical(args.drat_trim),
            wall_seconds=args.wall_seconds,
            max_proof_raw_bytes=args.max_proof_raw_bytes,
        )
    if args.output is not None:
        _atomic_json(_absolute_lexical(args.output), result)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
