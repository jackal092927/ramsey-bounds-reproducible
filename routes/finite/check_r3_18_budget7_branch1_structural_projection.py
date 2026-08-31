#!/usr/bin/env python3
"""Independent bounded structural audit for the branch-1 exact-seven route.

The audit deliberately uses only the Python standard library.  It authenticates
the frozen seed and universal I18 bank, then checks combinatorial consequences
that do not require a SAT solver:

* the triangle/degree subsystem's projection onto residual deletion supports;
* the three negative edge units propagated by the four proved positive units;
* common-neighbour no-addition units implied by triangle-freeness and the
  exact-six residual deletion counter;
* direct incidence and residual-literal statistics in the universal I18 bank;
* one explicitly bounded local swap probe.

The audit does not eliminate addition variables globally.  In particular it
does not prove a vertex-18 hit and does not prove that no stronger support
inequality exists.
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
from pathlib import Path
from typing import Any, Iterable, Sequence


Edge = tuple[int, int]

SCHEMA = "ramsey-r3-18-n100-exact-budget7-branch1-structural-projection-v1"
STATUS = "VERIFIED_BOUNDED_STRUCTURAL_PROJECTION_FACTS"
ORDER = 100
DEGREE_CAP = 17
RESIDUAL_DELETIONS = 6
FIXED_EDGE: Edge = (97, 99)
FORCED_POSITIVE_EDGES: tuple[Edge, ...] = (
    (11, 62),
    (18, 61),
    (18, 64),
    (18, 69),
)
EXPECTED_PROPAGATED_NEGATIVE_EDGES: tuple[Edge, ...] = (
    (61, 64),
    (61, 69),
    (64, 69),
)
LOCAL_SWAP_DELETIONS: tuple[Edge, ...] = (
    (2, 97),
    (5, 97),
    (8, 97),
    (13, 37),
    (13, 97),
    (16, 98),
)
LOCAL_SWAP_ADDITIONS: tuple[Edge, ...] = (
    (13, 61),
    (86, 97),
    (89, 97),
    (94, 97),
)
COMMON_MODEL_DELETIONS: tuple[Edge, ...] = (
    (2, 97),
    (5, 97),
    (8, 97),
    (13, 37),
    (13, 97),
    (18, 98),
)
COMMON_MODEL_ADDITIONS: tuple[Edge, ...] = (
    (13, 61),
    (18, 97),
    (86, 97),
    (89, 97),
    (94, 97),
)

EXPECTED_SEED_SHA256 = (
    "e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e"
)
EXPECTED_BANK_SHA256 = (
    "91b5709248ff641a315f5a0389b4f3fde3d38514f3b1a8b31b6cad31224f250b"
)
EXPECTED_BANK_ORDERED_SHA256 = (
    "f10690b826b86eb03567a2ffaffb553801fae32af20cfe4337118bddf4e41afa"
)
EXPECTED_BANK_SCHEMA = (
    "ramsey-r3-18-n100-exact-budget6-branch0-universal-union-v1"
)
EXPECTED_BANK_MASKS = 251_771
EXPECTED_BANK_SET_SIZE = 18
EXPECTED_SEED_EDGES = 827
EXPECTED_HISTORY_SHA256 = (
    "d5100bb5dce48da3ca8ab3810290ff553ebb9d6c87ff9df1f287700563f456b0"
)
EXPECTED_HISTORY_ORDERED_SHA256 = (
    "74b4b99c18e925a7a1bbb0e4a1636dad4bf8741ba67623c2164f3607a65172a8"
)
EXPECTED_HISTORY_SCHEMA = "ramsey-r3-18-n100-branch1-history-exclusion-v1"
EXPECTED_HISTORY_MASKS = 64_591
EXPECTED_APLUS_SHA256 = (
    "835137c2df19bc851618761cc0af92400b3fa2677dd00c47101d1074c7406e8b"
)
EXPECTED_APLUS_ORDERED_SHA256 = (
    "a3cff8d8a4c77c6effb49c03e76065a17f754d0a7de727d229652276b6e8cda0"
)
EXPECTED_APLUS_SCHEMA = (
    "ramsey-r3-18-n100-exact-budget7-branch1-cegar-mask-batch-v1"
)
EXPECTED_APLUS_MASKS = 4_096
EXPECTED_FIXED_BASE_MASKS = 235_504
EXPECTED_FIXED_BASE_ORDERED_SHA256 = (
    "1e9f89f40cd97a5f3b6fa93bb3c4835d45cadca8362e9d3150e90d4f385f6d8c"
)
EXPECTED_COMMON_MODEL_GZIP_SHA256 = (
    "9057db25b785640345e6f724cb1c79313642bb62ec2a19d9f310e25700de024d"
)
EXPECTED_COMMON_MODEL_RAW_SHA256 = (
    "51e7832b69a18b29db817d1e180f1a071f771fbb50e358de4fb57a3810cd737e"
)
EXPECTED_COMMON_MODEL_GZIP_BYTES = 391_052
EXPECTED_COMMON_MODEL_MAXIMUM_VARIABLE = 154_190
EXPECTED_COMMON_MODEL_PROJECTION_SHA256 = (
    "b4a39182efdf9b1f0513f5e189698c9e7eba46b52df5faee37ccfef66289cfe1"
)

_MASK_RE = re.compile(r"[0-9a-f]{25}\Z", flags=re.ASCII)


class AuditError(ValueError):
    """A fail-closed structural-audit failure."""


def _sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _canonical_sha256(payload: Any) -> str:
    raw = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    ).encode("ascii")
    return _sha256_bytes(raw)


def _strict_regular_bytes(path: Path, expected_sha256: str, label: str) -> bytes:
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
    if _sha256_bytes(raw) != expected_sha256:
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
        text = raw.decode("utf-8")
        payload = json.loads(
            text,
            object_pairs_hook=reject_duplicates,
            parse_constant=lambda value: (_ for _ in ()).throw(
                AuditError(f"{label} contains a non-finite JSON number")
            ),
        )
    except (UnicodeError, json.JSONDecodeError) as error:
        raise AuditError(f"{label} is not strict UTF-8 JSON") from error
    if not isinstance(payload, dict):
        raise AuditError(f"{label} must be a JSON object")
    return payload


def _edge_label(edge: Edge) -> str:
    return f"{edge[0]}-{edge[1]}"


def _edge_lists(edges: Iterable[Edge]) -> list[list[int]]:
    return [list(edge) for edge in sorted(edges)]


def _histogram(values: Iterable[int]) -> dict[str, int]:
    return {
        str(key): value
        for key, value in sorted(collections.Counter(values).items())
    }


def read_seed(path: Path) -> tuple[list[int], frozenset[Edge], dict[str, Any]]:
    raw = _strict_regular_bytes(path, EXPECTED_SEED_SHA256, "seed matrix")
    if not raw.endswith(b"\n") or b"\r" in raw:
        raise AuditError("seed matrix must be LF-terminated")
    try:
        lines = raw.decode("ascii").splitlines()
    except UnicodeError as error:
        raise AuditError("seed matrix is not ASCII") from error
    if len(lines) != ORDER:
        raise AuditError("seed matrix has the wrong row count")
    matrix: list[list[int]] = []
    for line in lines:
        fields = line.split()
        if len(fields) != ORDER or any(value not in {"0", "1"} for value in fields):
            raise AuditError("seed matrix is not a strict 100-by-100 0/1 matrix")
        matrix.append([int(value) for value in fields])
    for u in range(ORDER):
        if matrix[u][u] != 0:
            raise AuditError("seed matrix has a nonzero diagonal")
        for v in range(u + 1, ORDER):
            if matrix[u][v] != matrix[v][u]:
                raise AuditError("seed matrix is not symmetric")
    edges = frozenset(
        (u, v)
        for u in range(ORDER)
        for v in range(u + 1, ORDER)
        if matrix[u][v]
    )
    if len(edges) != EXPECTED_SEED_EDGES or FIXED_EDGE not in edges:
        raise AuditError("seed edge family differs from the frozen instance")
    rows = edge_rows(edges, ORDER)
    return rows, edges, {
        "basename": path.name,
        "bytes": len(raw),
        "sha256": EXPECTED_SEED_SHA256,
    }


def read_bank(path: Path) -> tuple[list[int], dict[str, Any]]:
    raw = _strict_regular_bytes(path, EXPECTED_BANK_SHA256, "universal bank")
    payload = _strict_json(raw, "universal bank")
    if set(payload) != {
        "all_masks_are_18_sets",
        "fixed_deleted_edge",
        "masks",
        "masks_sha256",
        "schema",
    }:
        raise AuditError("universal bank fields differ from the frozen schema")
    if (
        payload.get("schema") != EXPECTED_BANK_SCHEMA
        or payload.get("all_masks_are_18_sets") is not True
        or payload.get("fixed_deleted_edge") != [97, 98]
        or payload.get("masks_sha256") != EXPECTED_BANK_ORDERED_SHA256
    ):
        raise AuditError("universal bank metadata mismatch")
    values = payload.get("masks")
    if not isinstance(values, list) or len(values) != EXPECTED_BANK_MASKS:
        raise AuditError("universal bank mask count mismatch")
    masks: list[int] = []
    digest = hashlib.sha256()
    seen: set[int] = set()
    for value in values:
        if not isinstance(value, str) or not _MASK_RE.fullmatch(value):
            raise AuditError("universal bank contains a noncanonical mask")
        mask = int(value, 16)
        if mask.bit_count() != EXPECTED_BANK_SET_SIZE or mask in seen:
            raise AuditError("universal bank contains a repeated or malformed 18-set")
        seen.add(mask)
        masks.append(mask)
        # This is the historical bank's frozen hash convention: hexadecimal
        # integers with a *minimum* width of 16, not fixed-width 100-bit text.
        digest.update(f"{mask:016x}\n".encode("ascii"))
    if digest.hexdigest() != EXPECTED_BANK_ORDERED_SHA256:
        raise AuditError("universal bank ordered-mask digest mismatch")
    return masks, {
        "basename": path.name,
        "bytes": len(raw),
        "sha256": EXPECTED_BANK_SHA256,
        "masks": len(masks),
        "ordered_masks_sha256": EXPECTED_BANK_ORDERED_SHA256,
    }


def read_frozen_mask_set(
    path: Path,
    *,
    label: str,
    expected_file_sha256: str,
    expected_schema: str,
    expected_count: int,
    expected_ordered_sha256: str,
) -> tuple[frozenset[int], dict[str, Any]]:
    raw = _strict_regular_bytes(path, expected_file_sha256, label)
    payload = _strict_json(raw, label)
    if (
        payload.get("schema") != expected_schema
        or payload.get("masks_count") != expected_count
        or payload.get("ordered_masks_sha256") != expected_ordered_sha256
    ):
        raise AuditError(f"{label} metadata mismatch")
    values = payload.get("masks")
    if not isinstance(values, list) or len(values) != expected_count:
        raise AuditError(f"{label} mask count mismatch")
    masks: list[int] = []
    digest = hashlib.sha256()
    for value in values:
        if not isinstance(value, str) or not _MASK_RE.fullmatch(value):
            raise AuditError(f"{label} contains a noncanonical mask")
        mask = int(value, 16)
        if mask.bit_count() != EXPECTED_BANK_SET_SIZE:
            raise AuditError(f"{label} contains a malformed 18-set")
        masks.append(mask)
        digest.update((value + "\n").encode("ascii"))
    if masks != sorted(masks) or len(masks) != len(set(masks)):
        raise AuditError(f"{label} masks are not strictly sorted and unique")
    if digest.hexdigest() != expected_ordered_sha256:
        raise AuditError(f"{label} ordered-mask digest mismatch")
    return frozenset(masks), {
        "basename": path.name,
        "bytes": len(raw),
        "sha256": expected_file_sha256,
        "masks": len(masks),
        "ordered_masks_sha256": expected_ordered_sha256,
        "schema": expected_schema,
    }


def read_common_model_primary_edges(path: Path) -> frozenset[Edge]:
    raw_gzip = _strict_regular_bytes(
        path, EXPECTED_COMMON_MODEL_GZIP_SHA256, "common SAT model"
    )
    if len(raw_gzip) != EXPECTED_COMMON_MODEL_GZIP_BYTES:
        raise AuditError("common SAT model compressed size mismatch")
    try:
        raw = gzip.decompress(raw_gzip)
        text = raw.decode("ascii")
    except (OSError, EOFError, UnicodeError) as error:
        raise AuditError("common SAT model is not a complete ASCII gzip stream") from error
    if _sha256_bytes(raw) != EXPECTED_COMMON_MODEL_RAW_SHA256:
        raise AuditError("common SAT model raw SHA-256 mismatch")
    if not raw.endswith(b"\n") or b"\r" in raw:
        raise AuditError("common SAT model must use LF-terminated lines")
    lines = text.splitlines()
    if not lines or lines[0] != "s SATISFIABLE":
        raise AuditError("common SAT model lacks the exact SAT status")
    tokens: list[int] = []
    for line in lines[1:]:
        if not line.startswith("v "):
            raise AuditError("common SAT model contains a non-assignment line")
        try:
            tokens.extend(int(value) for value in line.split()[1:])
        except ValueError as error:
            raise AuditError("common SAT model contains a non-integer token") from error
    if not tokens or tokens[-1] != 0 or any(value == 0 for value in tokens[:-1]):
        raise AuditError("common SAT model has a malformed zero terminator")
    assignment: list[bool | None] = [None] * (
        EXPECTED_COMMON_MODEL_MAXIMUM_VARIABLE + 1
    )
    for literal in tokens[:-1]:
        variable = abs(literal)
        if not 1 <= variable <= EXPECTED_COMMON_MODEL_MAXIMUM_VARIABLE:
            raise AuditError("common SAT model literal is out of range")
        if assignment[variable] is not None:
            raise AuditError("common SAT model assigns one variable twice")
        assignment[variable] = literal > 0
    if any(value is None for value in assignment[1:]):
        raise AuditError("common SAT model is not a complete assignment")
    pairs = list(itertools.combinations(range(ORDER), 2))
    edges = frozenset(
        edge for variable, edge in enumerate(pairs, start=1) if assignment[variable]
    )
    if _projection_sha256(edges) != EXPECTED_COMMON_MODEL_PROJECTION_SHA256:
        raise AuditError("common SAT model primary projection mismatch")
    return edges


def edge_rows(edges: Iterable[Edge], order: int) -> list[int]:
    rows = [0] * order
    for u, v in edges:
        if not 0 <= u < v < order:
            raise AuditError("edge lies outside the graph order")
        rows[u] |= 1 << v
        rows[v] |= 1 << u
    return rows


def internal_edge_count(mask: int, rows: Sequence[int]) -> int:
    total = 0
    subset = mask
    while subset:
        bit = subset & -subset
        subset ^= bit
        u = bit.bit_length() - 1
        total += (rows[u] & mask & ~((1 << (u + 1)) - 1)).bit_count()
    return total


def triangles(rows: Sequence[int]) -> list[tuple[int, int, int]]:
    result: list[tuple[int, int, int]] = []
    for u in range(len(rows)):
        later_neighbors = rows[u] & ~((1 << (u + 1)) - 1)
        while later_neighbors:
            bit = later_neighbors & -later_neighbors
            later_neighbors ^= bit
            v = bit.bit_length() - 1
            common = rows[u] & rows[v] & ~((1 << (v + 1)) - 1)
            while common:
                common_bit = common & -common
                common ^= common_bit
                result.append((u, v, common_bit.bit_length() - 1))
    return result


def _has_edge(mask: int, edge: Edge) -> bool:
    return bool(mask & (1 << edge[0]) and mask & (1 << edge[1]))


def propagated_negative_edges(positive_edges: Sequence[Edge]) -> tuple[Edge, ...]:
    negatives: set[Edge] = set()
    for first, second in itertools.combinations(positive_edges, 2):
        shared = set(first) & set(second)
        if len(shared) == 1:
            leaves = sorted((set(first) | set(second)) - shared)
            negatives.add((leaves[0], leaves[1]))
    return tuple(sorted(negatives))


def common_neighbour_audit(
    base_rows: Sequence[int], base_edges: frozenset[Edge]
) -> tuple[frozenset[Edge], dict[str, Any]]:
    nonedges = [
        (u, v)
        for u in range(ORDER)
        for v in range(u + 1, ORDER)
        if (u, v) not in base_edges
    ]
    common_counts = {
        edge: (base_rows[edge[0]] & base_rows[edge[1]]).bit_count()
        for edge in nonedges
    }
    derived = frozenset(
        edge for edge, count in common_counts.items() if count > RESIDUAL_DELETIONS
    )
    digest = hashlib.sha256()
    for u, v in sorted(derived):
        digest.update(f"{u} {v}\n".encode("ascii"))
    propagated = set(EXPECTED_PROPAGATED_NEGATIVE_EDGES)
    if FIXED_EDGE in derived:
        raise AuditError("fixed branch edge unexpectedly entered the derived threshold set")
    return derived, {
        "fixed_base_nonedges_including_fixed_unit_edge": len(nonedges),
        "common_neighbour_count_distribution": _histogram(common_counts.values()),
        "threshold": RESIDUAL_DELETIONS + 1,
        "derived_no_addition_units": len(derived),
        "derived_no_addition_units_by_common_neighbours": _histogram(
            common_counts[edge] for edge in derived
        ),
        "derived_edge_list_sha256": digest.hexdigest(),
        "derived_edge_list_hash_format": "sorted ASCII lines: u SP v LF",
        "fixed_edge_common_neighbours": common_counts[FIXED_EDGE],
        "overlap_with_direct_triangle_units": len(derived & propagated),
        "new_beyond_direct_triangle_units": len(derived - propagated),
        "union_with_direct_triangle_units": len(derived | propagated),
        "union_with_direct_and_fixed_negative_units": len(
            derived | propagated | {FIXED_EDGE}
        ),
        "lemma": (
            "If a fixed-base nonedge uv is added, every fixed-base common "
            "neighbour w requires deletion of at least one of the two distinct "
            "wedge edges uw,vw.  More than six common neighbours therefore "
            "contradict the exact-six residual deletion counter."
        ),
        "solver_redundancy": (
            "These units are logical consequences of the installed triangle "
            "clauses and exact-six counter; they strengthen explicit "
            "propagation but do not restrict the target beyond that formula."
        ),
    }


def _minimum_local_deletions_for_addition(
    edge: Edge,
    base_rows: Sequence[int],
    base_edges: frozenset[Edge],
    forced_edges: frozenset[Edge],
) -> int | None:
    """Exact local deletion minimum for adding one fixed-base nonedge.

    ``None`` means one common-neighbour wedge has both edges forced present,
    so the proposed addition creates an unavoidable triangle.  The finite
    minimization includes only consequences of triangle-freeness, endpoint
    degree caps, the independent vertex-98 degree hit, and the four proved
    retention units.  It deliberately does not inspect the I18 bank.
    """

    u, v = edge
    degrees = [row.bit_count() for row in base_rows]
    quotas: dict[int, int] = {98: 1}
    quotas[u] = max(quotas.get(u, 0), degrees[u] + 1 - DEGREE_CAP)
    quotas[v] = max(quotas.get(v, 0), degrees[v] + 1 - DEGREE_CAP)
    quotas = {vertex: quota for vertex, quota in quotas.items() if quota > 0}

    wedge_options: list[tuple[Edge, ...]] = []
    common = base_rows[u] & base_rows[v]
    while common:
        bit = common & -common
        common ^= bit
        w = bit.bit_length() - 1
        options = tuple(
            candidate
            for candidate in (tuple(sorted((u, w))), tuple(sorted((v, w))))
            if candidate not in forced_edges
        )
        if not options:
            return None
        wedge_options.append(options)

    best: int | None = None
    for raw_choices in itertools.product(*wedge_options):
        selected = set(raw_choices)
        deficits = {
            vertex: max(
                0, quota - sum(vertex in chosen for chosen in selected)
            )
            for vertex, quota in quotas.items()
        }
        required_vertices = sorted(deficits)
        internal_candidates = [
            (a, b)
            for a, b in itertools.combinations(required_vertices, 2)
            if (a, b) in base_edges
            and (a, b) not in forced_edges
            and (a, b) not in selected
        ]
        for bits in range(1 << len(internal_candidates)):
            internal = {
                internal_candidates[index]
                for index in range(len(internal_candidates))
                if bits & (1 << index)
            }
            remaining = {
                vertex: max(
                    0,
                    deficits[vertex]
                    - sum(vertex in chosen for chosen in internal),
                )
                for vertex in required_vertices
            }
            # Any remaining quota can be met by distinct edges from that
            # required vertex to vertices outside the at-most-three-vertex
            # quota set.  Check availability instead of assuming it.
            available = True
            for vertex, deficit in remaining.items():
                outside = 0
                neighbours = base_rows[vertex]
                while neighbours:
                    bit = neighbours & -neighbours
                    neighbours ^= bit
                    other = bit.bit_length() - 1
                    candidate = tuple(sorted((vertex, other)))
                    if (
                        other not in required_vertices
                        and candidate not in forced_edges
                        and candidate not in selected
                        and candidate not in internal
                    ):
                        outside += 1
                if outside < deficit:
                    available = False
                    break
            if not available:
                continue
            candidate_size = len(selected) + len(internal) + sum(remaining.values())
            best = candidate_size if best is None else min(best, candidate_size)
    return best


def full_no_addition_audit(
    base_rows: Sequence[int],
    base_edges: frozenset[Edge],
    common_threshold_units: frozenset[Edge],
) -> tuple[frozenset[Edge], dict[str, Any]]:
    forced = frozenset(FORCED_POSITIVE_EDGES)
    nonedges = [
        (u, v)
        for u in range(ORDER)
        for v in range(u + 1, ORDER)
        if (u, v) not in base_edges
    ]
    minima = {
        edge: _minimum_local_deletions_for_addition(
            edge, base_rows, base_edges, forced
        )
        for edge in nonedges
    }
    units = frozenset(
        edge
        for edge, minimum in minima.items()
        if minimum is None or minimum > RESIDUAL_DELETIONS
    )
    digest = hashlib.sha256()
    for u, v in sorted(units):
        digest.update(f"{u} {v}\n".encode("ascii"))
    distribution = collections.Counter(
        "infeasible" if minimum is None else str(minimum)
        for minimum in minima.values()
    )
    direct = frozenset(EXPECTED_PROPAGATED_NEGATIVE_EDGES)
    coupled = units - common_threshold_units - direct
    if not direct <= units:
        raise AuditError("direct triangle units escaped the full no-addition closure")
    return units, {
        "universe": "all 4,124 fixed-base nonedges, including the fixed unit edge",
        "minimum_local_deletions_distribution": {
            key: distribution[key]
            for key in sorted(
                distribution,
                key=lambda value: (value == "infeasible", int(value) if value != "infeasible" else 0),
            )
        },
        "no_addition_units": len(units),
        "edge_list_sha256": digest.hexdigest(),
        "edge_list_hash_format": "sorted ASCII lines: u SP v LF",
        "breakdown": {
            "common_neighbours_greater_than_six": len(common_threshold_units),
            "direct_triangle_units_not_in_common_threshold": len(
                direct - common_threshold_units
            ),
            "coupled_degree_vertex98_budget_units": len(coupled),
        },
        "coupled_degree_vertex98_budget_edges": _edge_lists(coupled),
        "fixed_branch_unit_edge_is_separate": FIXED_EDGE not in units,
        "lemma": (
            "For each candidate added edge uv, minimize residual seed-edge "
            "deletions subject to one hit per common-neighbour wedge, the "
            "degree-cap deletion quotas at u and v, the independent vertex-98 "
            "degree hit, and the four retention units.  If the exact minimum "
            "exceeds six, or a wedge has both edges forced retained, x_uv=0."
        ),
        "claim_boundary": (
            "This is a solver-redundant consequence of existing triangle, "
            "degree, exact-six, fixed-branch, and four retention constraints; "
            "it is not a new restriction on the original Ramsey target."
        ),
    }


def bank_audit(
    masks: Sequence[int],
    original_rows: Sequence[int],
    base_rows: Sequence[int],
    full_no_additions: frozenset[Edge],
) -> dict[str, Any]:
    direct_negative = frozenset(EXPECTED_PROPAGATED_NEGATIVE_EDGES)
    if any(
        (original_rows[u] >> v) & 1 for u, v in direct_negative
    ):
        raise AuditError("a propagated negative edge is not an original nonedge")
    if not direct_negative <= full_no_additions:
        raise AuditError("full no-addition closure omits a direct triangle unit")
    forbidden_rows = edge_rows(full_no_additions, ORDER)

    forced_incidence = {edge: 0 for edge in FORCED_POSITIVE_EDGES}
    positive_multiplicity: list[int] = []
    all_base_counts: list[int] = []
    unresolved_base_counts: list[int] = []
    unresolved_original_counts: list[int] = []
    direct_negative_incidence = {edge: 0 for edge in direct_negative}
    direct_negative_multiplicity: list[int] = []
    forbidden_multiplicity: list[int] = []
    residual_after_direct: list[int] = []
    residual_after_all: list[int] = []
    fixed_unit_incidence = 0

    for mask in masks:
        base_count = internal_edge_count(mask, base_rows)
        all_base_counts.append(base_count)
        positive_count = 0
        for edge in FORCED_POSITIVE_EDGES:
            if _has_edge(mask, edge):
                forced_incidence[edge] += 1
                positive_count += 1
        positive_multiplicity.append(positive_count)
        if positive_count:
            continue

        unresolved_base_counts.append(base_count)
        original_count = internal_edge_count(mask, original_rows)
        unresolved_original_counts.append(original_count)
        if _has_edge(mask, FIXED_EDGE):
            fixed_unit_incidence += 1

        direct_count = 0
        for edge in direct_negative:
            if _has_edge(mask, edge):
                direct_negative_incidence[edge] += 1
                direct_count += 1
        direct_negative_multiplicity.append(direct_count)
        forbidden_count = internal_edge_count(mask, forbidden_rows)
        forbidden_multiplicity.append(forbidden_count)
        residual_after_direct.append(
            math_comb_18_pairs() - original_count - direct_count
        )
        residual_after_all.append(
            math_comb_18_pairs() - original_count - forbidden_count
        )

    if max(positive_multiplicity) != 1:
        raise AuditError("one bank mask contains multiple forced positive edges")
    unresolved = len(unresolved_base_counts)
    if unresolved + sum(value > 0 for value in positive_multiplicity) != len(masks):
        raise AuditError("bank forced-unit partition failed")
    minimum_free = min(residual_after_all)
    minimum_masks = [
        mask
        for mask in masks
        if not any(_has_edge(mask, edge) for edge in FORCED_POSITIVE_EDGES)
        and (
            math_comb_18_pairs()
            - internal_edge_count(mask, original_rows)
            - internal_edge_count(mask, forbidden_rows)
        )
        == minimum_free
    ]
    if len(minimum_masks) != 1:
        raise AuditError("minimum residual-addition bank clause is not unique")
    minimum_mask = minimum_masks[0]
    minimum_base = internal_edge_count(minimum_mask, base_rows)
    minimum_original = internal_edge_count(minimum_mask, original_rows)
    minimum_forbidden = internal_edge_count(minimum_mask, forbidden_rows)
    return {
        "forced_positive_edge_incidence": {
            _edge_label(edge): forced_incidence[edge]
            for edge in FORCED_POSITIVE_EDGES
        },
        "forced_positive_multiplicity": _histogram(positive_multiplicity),
        "clauses_satisfied_by_forced_positive_units": len(masks) - unresolved,
        "unresolved_clauses": unresolved,
        "fixed_negative_unit_incidence_among_unresolved": fixed_unit_incidence,
        "fixed_base_edge_literals_per_mask": _histogram(all_base_counts),
        "fixed_base_edge_literals_per_unresolved_mask": _histogram(
            unresolved_base_counts
        ),
        "original_seed_edge_literal_range_per_unresolved_mask": [
            min(unresolved_original_counts),
            max(unresolved_original_counts),
        ],
        "propagated_negative_edge_incidence_among_unresolved": {
            _edge_label(edge): direct_negative_incidence[edge]
            for edge in sorted(direct_negative)
        },
        "propagated_negative_multiplicity_among_unresolved": _histogram(
            direct_negative_multiplicity
        ),
        "full_396_no_addition_units_per_unresolved_mask": {
            "range": [min(forbidden_multiplicity), max(forbidden_multiplicity)],
            "distribution": _histogram(forbidden_multiplicity),
            "total_incidence": sum(forbidden_multiplicity),
        },
        "residual_original_nonedge_addition_literals_after_direct_units": {
            "range": [min(residual_after_direct), max(residual_after_direct)],
            "clauses_with_zero": sum(value == 0 for value in residual_after_direct),
        },
        "residual_original_nonedge_addition_literals_after_all_local_units": {
            "range": [min(residual_after_all), max(residual_after_all)],
            "clauses_with_zero": sum(value == 0 for value in residual_after_all),
            "minimum_clause": {
                "mask_hex": f"{minimum_mask:025x}",
                "fixed_base_seed_edge_literals": minimum_base,
                "original_seed_edge_literals_including_fixed_unit": minimum_original,
                "forbidden_no_addition_literals": minimum_forbidden,
                "free_addition_literals": minimum_free,
            },
        },
        "support_only_clause_created_by_local_substitution": False,
        "interpretation": (
            "The fixed unit, four positive units, three direct triangle units, "
            "and the complete 396-unit bounded structural closure do not turn "
            "any unresolved bank clause into a deletion-support-only clause."
        ),
    }


def math_comb_18_pairs() -> int:
    return EXPECTED_BANK_SET_SIZE * (EXPECTED_BANK_SET_SIZE - 1) // 2


def _projection_sha256(edges: frozenset[Edge]) -> str:
    projection = bytes(
        1 if (u, v) in edges else 0
        for u in range(ORDER)
        for v in range(u + 1, ORDER)
    )
    return _sha256_bytes(projection)


def local_swap_audit(
    original_edges: frozenset[Edge],
    base_edges: frozenset[Edge],
    base_rows: Sequence[int],
    masks: Sequence[int],
    full_no_additions: frozenset[Edge],
) -> dict[str, Any]:
    deletions = frozenset(LOCAL_SWAP_DELETIONS)
    additions = frozenset(LOCAL_SWAP_ADDITIONS)
    if (
        len(deletions) != RESIDUAL_DELETIONS
        or not deletions <= base_edges
        or additions & original_edges
        or FIXED_EDGE in deletions
    ):
        raise AuditError("local swap edit sets are malformed")
    final_edges = frozenset((base_edges - deletions) | additions)
    final_rows = edge_rows(final_edges, ORDER)
    final_triangles = triangles(final_rows)
    degrees = [row.bit_count() for row in final_rows]
    violations = [mask for mask in masks if internal_edge_count(mask, final_rows) == 0]
    digest = hashlib.sha256()
    for mask in violations:
        digest.update(f"{mask:025x}\n".encode("ascii"))

    direct_repairs: set[Edge] = set()
    for mask in violations:
        vertices = [vertex for vertex in range(ORDER) if mask & (1 << vertex)]
        for u, v in itertools.combinations(vertices, 2):
            edge = (u, v)
            if edge in final_edges:
                raise AuditError("reported bank witness is not independent")
            if degrees[u] >= DEGREE_CAP or degrees[v] >= DEGREE_CAP:
                continue
            if final_rows[u] & final_rows[v]:
                continue
            direct_repairs.add(edge)

    return {
        "fixed_deletion": list(FIXED_EDGE),
        "residual_deletions": _edge_lists(deletions),
        "additions": _edge_lists(additions),
        "final_edges": len(final_edges),
        "edge_projection_sha256": _projection_sha256(final_edges),
        "exact_six_residual_deletions": True,
        "forced_positive_edges_retained": all(
            edge in final_edges for edge in FORCED_POSITIVE_EDGES
        ),
        "deletion_support_hits_vertex_98": any(98 in edge for edge in deletions),
        "deletion_support_hits_vertex_18": any(18 in edge for edge in deletions),
        "triangle_count": len(final_triangles),
        "maximum_degree": max(degrees),
        "degree_distribution": _histogram(degrees),
        "addition_fixed_base_common_neighbour_counts": {
            _edge_label(edge): (base_rows[edge[0]] & base_rows[edge[1]]).bit_count()
            for edge in sorted(additions)
        },
        "violates_full_local_no_addition_closure": bool(
            additions & full_no_additions
        ),
        "universal_bank_satisfied": not violations,
        "violated_universal_bank_masks": [f"{mask:025x}" for mask in violations],
        "violated_universal_bank_masks_count": len(violations),
        "violated_universal_bank_masks_sha256": digest.hexdigest(),
        "single_edge_direct_repairs_preserving_triangle_and_degree_caps": len(
            direct_repairs
        ),
        "direct_repair_definition": (
            "An edge inside a displayed violated I18 mask whose immediate "
            "addition to this fixed graph creates no triangle and leaves both "
            "endpoint degrees at most 17, with no other edit changed."
        ),
        "claim_boundary": (
            "This is a local probe satisfying exact-six support, the four "
            "retention units, triangle-freeness, and the degree cap while not "
            "hitting vertex 18.  It violates 12 installed bank clauses and is "
            "therefore neither a relaxation model nor a counterexample to a "
            "possible vertex-18 hit."
        ),
    }


def domination_lift_audit(
    original_edges: frozenset[Edge],
    base_edges: frozenset[Edge],
    base_rows: Sequence[int],
    universal_masks: frozenset[int],
    history_masks: frozenset[int],
    aplus_masks: frozenset[int],
    common_model_path: Path | None,
) -> dict[str, Any]:
    deletions = frozenset(COMMON_MODEL_DELETIONS)
    additions = frozenset(COMMON_MODEL_ADDITIONS)
    if (
        len(deletions) != RESIDUAL_DELETIONS
        or not deletions <= base_edges
        or additions & original_edges
    ):
        raise AuditError("frozen common-model primary projection descriptor is malformed")
    model_edges = frozenset((base_edges - deletions) | additions)
    if _projection_sha256(model_edges) != EXPECTED_COMMON_MODEL_PROJECTION_SHA256:
        raise AuditError("common-model projection descriptor digest mismatch")
    if common_model_path is not None:
        replayed_edges = read_common_model_primary_edges(common_model_path)
        if replayed_edges != model_edges:
            raise AuditError("common-model artifact differs from its projection descriptor")
    rows = edge_rows(model_edges, ORDER)
    if triangles(rows):
        raise AuditError("common-model primary projection is not triangle-free")
    degrees = [row.bit_count() for row in rows]
    if _histogram(degrees) != {"16": 50, "17": 50}:
        raise AuditError("common-model degree distribution changed")

    z_sets: dict[int, list[int]] = {}
    degree17_violations: list[tuple[int, int, int]] = []
    degree16_violations: list[tuple[int, int, int, int]] = []
    for vertex in range(ORDER):
        z_set = [
            other
            for other in range(ORDER)
            if other != vertex
            and not (rows[vertex] & (1 << other))
            and not (rows[vertex] & rows[other])
        ]
        z_sets[vertex] = z_set
        if degrees[vertex] == 17:
            for other in z_set:
                degree17_violations.append(
                    (vertex, other, rows[vertex] | (1 << other))
                )
        elif degrees[vertex] == 16:
            for first, second in itertools.combinations(z_set, 2):
                if not (rows[first] & (1 << second)):
                    degree16_violations.append(
                        (
                            vertex,
                            first,
                            second,
                            rows[vertex] | (1 << first) | (1 << second),
                        )
                    )
        else:
            raise AuditError("domination audit encountered an unsupported degree")
    if len(degree17_violations) != 1 or degree16_violations:
        raise AuditError("domination lift no longer has the frozen unique violation")
    vertex, isolated_vertex, mask = degree17_violations[0]
    vertices = [candidate for candidate in range(ORDER) if mask & (1 << candidate)]
    if (vertex, isolated_vertex) != (86, 37) or len(vertices) != 18:
        raise AuditError("domination lift violation identity changed")
    if internal_edge_count(mask, rows) != 0:
        raise AuditError("domination lift mask is not independent in the common model")
    universal_violations = sum(
        internal_edge_count(installed, rows) == 0 for installed in universal_masks
    )
    forced_units_retained = all(edge in model_edges for edge in FORCED_POSITIVE_EDGES)
    if universal_violations or not forced_units_retained:
        raise AuditError("common-model graph fails a bank clause or retention unit")
    overlap = {
        "universal_bank": mask in universal_masks,
        "historical_learned_union": mask in history_masks,
        "Aplus_batch": mask in aplus_masks,
        "exhaustive_fixed_base_family": internal_edge_count(mask, base_rows) == 0,
    }
    if any(overlap.values()):
        raise AuditError("domination lift mask is not new relative to frozen families")
    mask_hex = f"{mask:025x}"
    mask_line_sha256 = _sha256_bytes((mask_hex + "\n").encode("ascii"))
    return {
        "lemma": (
            "For a triangle-free graph F and vertex v, let Z_v be the "
            "nonneighbours u of v with N(u) intersect N(v) empty.  N(v) and "
            "every independent set in F[Z_v] have no cross edge, so alpha(F)<18 "
            "implies alpha(F[Z_v]) <= 17-d(v).  Hence d(v)=17 forces Z_v empty; "
            "d(v)=16 forces F[Z_v] to be a clique and triangle-freeness gives "
            "|Z_v|<=2."
        ),
        "source_common_model": {
            "gzip_sha256": EXPECTED_COMMON_MODEL_GZIP_SHA256,
            "raw_sha256": EXPECTED_COMMON_MODEL_RAW_SHA256,
            "gzip_bytes": EXPECTED_COMMON_MODEL_GZIP_BYTES,
            "maximum_variable": EXPECTED_COMMON_MODEL_MAXIMUM_VARIABLE,
            "primary_projection_sha256": EXPECTED_COMMON_MODEL_PROJECTION_SHA256,
            "residual_deletions": _edge_lists(deletions),
            "additions": _edge_lists(additions),
            "full_artifact_replay_supported_by_checker": True,
            "full_artifact_replay_required_for_independent_model_binding": True,
        },
        "degree_distribution": _histogram(degrees),
        "common_model_universal_bank_violations": universal_violations,
        "common_model_forced_positive_units_retained": forced_units_retained,
        "Z_size_distribution_at_degree_17": _histogram(
            len(z_sets[vertex])
            for vertex in range(ORDER)
            if degrees[vertex] == 17
        ),
        "Z_size_distribution_at_degree_16": _histogram(
            len(z_sets[vertex])
            for vertex in range(ORDER)
            if degrees[vertex] == 16
        ),
        "degree_17_violations": 1,
        "degree_16_nonclique_violations": 0,
        "unique_violation": {
            "vertex": vertex,
            "Z_vertex": isolated_vertex,
            "mask_vertices": vertices,
            "mask_hex": mask_hex,
            "mask_line_sha256": mask_line_sha256,
            "common_model_internal_edges": internal_edge_count(mask, rows),
            "fixed_base_internal_edges": internal_edge_count(mask, base_rows),
        },
        "overlap_with_frozen_families": overlap,
        "zero_overlap_verified": not any(overlap.values()),
        "frozen_family_identities": {
            "universal_bank": {
                "masks": EXPECTED_BANK_MASKS,
                "ordered_masks_sha256": EXPECTED_BANK_ORDERED_SHA256,
            },
            "historical_learned_union": {
                "masks": EXPECTED_HISTORY_MASKS,
                "ordered_masks_sha256": EXPECTED_HISTORY_ORDERED_SHA256,
            },
            "Aplus_batch": {
                "masks": EXPECTED_APLUS_MASKS,
                "ordered_masks_sha256": EXPECTED_APLUS_ORDERED_SHA256,
            },
            "exhaustive_fixed_base_family": {
                "masks": EXPECTED_FIXED_BASE_MASKS,
                "ordered_masks_sha256": EXPECTED_FIXED_BASE_ORDERED_SHA256,
                "membership_checked_directly_against_fixed_base": True,
            },
        },
        "strict_common_relaxation_strengthening": True,
        "strengthening_reason": (
            "The displayed mask is independent in the checked common-model "
            "projection, while that graph satisfies the universal bank and "
            "four retention units.  Its universally valid I18 hitting clause "
            "therefore strictly removes that witness from the common "
            "relaxation.  Zero inventory overlap additionally shows the cut is "
            "not already listed in the later frozen families."
        ),
        "claim_boundary": (
            "This is a genuine structural separator for the common incomplete "
            "bank, not a proof that the branch or exact-seven layer is UNSAT.  "
            "Because the A+ clauses already exclude the source common model, "
            "no strict semantic shrinkage of the later A+-augmented formula is "
            "claimed merely from inventory nonmembership.  One cut is not a "
            "complete method."
        ),
    }


def build_audit(
    matrix_path: Path,
    bank_path: Path,
    history_path: Path,
    aplus_path: Path,
    common_model_path: Path | None = None,
) -> dict[str, Any]:
    original_rows, original_edges, seed_info = read_seed(matrix_path)
    masks, bank_info = read_bank(bank_path)
    history_masks, history_info = read_frozen_mask_set(
        history_path,
        label="historical exclusion",
        expected_file_sha256=EXPECTED_HISTORY_SHA256,
        expected_schema=EXPECTED_HISTORY_SCHEMA,
        expected_count=EXPECTED_HISTORY_MASKS,
        expected_ordered_sha256=EXPECTED_HISTORY_ORDERED_SHA256,
    )
    aplus_masks, aplus_info = read_frozen_mask_set(
        aplus_path,
        label="A+ batch",
        expected_file_sha256=EXPECTED_APLUS_SHA256,
        expected_schema=EXPECTED_APLUS_SCHEMA,
        expected_count=EXPECTED_APLUS_MASKS,
        expected_ordered_sha256=EXPECTED_APLUS_ORDERED_SHA256,
    )
    base_edges = frozenset(original_edges - {FIXED_EDGE})
    base_rows = edge_rows(base_edges, ORDER)
    seed_triangles = triangles(original_rows)
    base_triangles = triangles(base_rows)
    degrees = [row.bit_count() for row in base_rows]
    over_cap = [vertex for vertex, degree in enumerate(degrees) if degree > DEGREE_CAP]
    if seed_triangles != [(97, 98, 99)] or base_triangles:
        raise AuditError("seed/fixed-base triangle structure changed")
    if over_cap != [98] or degrees[98] != 18 or max(degrees[:98] + degrees[99:]) > 17:
        raise AuditError("fixed-base degree projection premise changed")
    if not all(edge in base_edges for edge in FORCED_POSITIVE_EDGES):
        raise AuditError("a forced positive edge is absent from the fixed base")

    propagated = propagated_negative_edges(FORCED_POSITIVE_EDGES)
    if propagated != EXPECTED_PROPAGATED_NEGATIVE_EDGES:
        raise AuditError("forced-unit triangle propagation changed")
    if any(edge in original_edges for edge in propagated):
        raise AuditError("a propagated negative edge is an original seed edge")

    common_threshold_units, common_info = common_neighbour_audit(
        base_rows, base_edges
    )
    full_no_additions, full_no_addition_info = full_no_addition_audit(
        base_rows, base_edges, common_threshold_units
    )
    universal_info = bank_audit(
        masks, original_rows, base_rows, full_no_additions
    )
    endpoints = sorted(
        {98} | {vertex for edge in FORCED_POSITIVE_EDGES for vertex in edge}
    )
    payload: dict[str, Any] = {
        "schema": SCHEMA,
        "status": STATUS,
        "inputs": {
            "seed": seed_info,
            "universal_bank": bank_info,
            "historical_exclusion": history_info,
            "Aplus_batch": aplus_info,
        },
        "branch": {
            "fixed_deleted_edge": list(FIXED_EDGE),
            "exact_residual_deletions": RESIDUAL_DELETIONS,
            "degree_cap": DEGREE_CAP,
            "seed_edges": len(original_edges),
            "fixed_base_edges": len(base_edges),
            "forced_positive_edges": _edge_lists(FORCED_POSITIVE_EDGES),
        },
        "triangle_and_degree_projection": {
            "seed_triangles": [list(value) for value in seed_triangles],
            "fixed_base_triangle_count": len(base_triangles),
            "fixed_base_degree_distribution": _histogram(degrees),
            "vertices_above_degree_cap": over_cap,
            "endpoint_degrees": {str(vertex): degrees[vertex] for vertex in endpoints},
            "endpoint_neighbourhoods": {
                str(vertex): [
                    other for other in range(ORDER) if base_rows[vertex] & (1 << other)
                ]
                for vertex in endpoints
            },
            "forced_edge_common_neighbour_counts": {
                _edge_label(edge): (
                    base_rows[edge[0]] & base_rows[edge[1]]
                ).bit_count()
                for edge in FORCED_POSITIVE_EDGES
            },
            "projection_lemma": (
                "For the triangle and degree constraints, every exact-six "
                "residual seed-deletion support that avoids the four forced "
                "edges and hits delta(98) has the completion A=empty: deleting "
                "edges preserves triangle-freeness, and the delta(98) hit "
                "reduces the unique degree-18 vertex to the cap.  Conversely, "
                "the four units and the degree cap require those conditions."
            ),
            "support_conditions_complete_for_triangle_degree_subsystem": True,
            "support_conditions": [
                "exactly six residual seed-edge deletions",
                "do not delete any of the four forced positive edges",
                "delete at least one fixed-base edge incident to vertex 98",
            ],
        },
        "forced_unit_triangle_propagation": {
            "positive_edges": _edge_lists(FORCED_POSITIVE_EDGES),
            "negative_edges": _edge_lists(propagated),
            "negative_units": len(propagated),
            "all_negative_edges_are_original_nonedges": True,
        },
        "common_neighbour_no_addition": common_info,
        "full_local_no_addition_closure": full_no_addition_info,
        "universal_bank_local_substitution": universal_info,
        "local_swap_probe": local_swap_audit(
            original_edges, base_edges, base_rows, masks, full_no_additions
        ),
        "domination_lift": domination_lift_audit(
            original_edges,
            base_edges,
            base_rows,
            frozenset(masks),
            history_masks,
            aplus_masks,
            common_model_path,
        ),
        "claim_boundary": {
            "vertex_18_hit_proved": False,
            "no_stronger_global_support_lift_proved": False,
            "global_addition_elimination_performed": False,
            "safe_claim": (
                "The recorded projection lemma is complete only for the "
                "triangle-and-degree subsystem.  The bank statistics certify "
                "only bounded local substitution.  Any stronger support "
                "inequality still requires global elimination of additions or "
                "proof-carrying fixed-support refutations."
            ),
        },
    }
    payload["record_sha256"] = _canonical_sha256(payload)
    return payload


def load_tracked_ledger(path: Path) -> dict[str, Any]:
    try:
        metadata = os.lstat(path)
    except OSError as error:
        raise AuditError("tracked ledger cannot be inspected") from error
    if not stat.S_ISREG(metadata.st_mode):
        raise AuditError("tracked ledger must be a non-symlink regular file")
    return _strict_json(path.read_bytes(), "tracked ledger")


def main(argv: Sequence[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
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
        "--history-exclusion",
        type=Path,
        default=here / "r3_18_budget7_branch1_cegar_history_exclusion.json",
    )
    parser.add_argument(
        "--Aplus-batch",
        type=Path,
        default=here / "r3_18_budget7_branch1_cegar_Aplus_batch.json",
    )
    parser.add_argument(
        "--common-model",
        type=Path,
        required=True,
        help=(
            "Frozen complete model artifact.  Its full 154,190-variable "
            "assignment is authenticated and its primary "
            "projection must match the compact descriptor used by the ledger."
        ),
    )
    parser.add_argument(
        "--ledger",
        type=Path,
        default=here / "r3_18_budget7_branch1_structural_projection.json",
    )
    parser.add_argument("--print-json", action="store_true")
    args = parser.parse_args(argv)
    try:
        audit = build_audit(
            args.matrix,
            args.universal_bank,
            args.history_exclusion,
            args.Aplus_batch,
            args.common_model,
        )
        tracked = load_tracked_ledger(args.ledger)
        if tracked != audit:
            raise AuditError("tracked ledger differs from independent reconstruction")
    except (AuditError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if args.print_json:
        print(json.dumps(audit, indent=2, sort_keys=True))
    else:
        print(
            f"{STATUS}: record={audit['record_sha256']} "
            f"no_add={audit['full_local_no_addition_closure']['no_addition_units']} "
            f"domination_cuts={audit['domination_lift']['degree_17_violations']} "
            f"local_bank_violations={audit['local_swap_probe']['violated_universal_bank_masks_count']}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
