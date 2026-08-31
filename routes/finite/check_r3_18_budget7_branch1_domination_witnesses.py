#!/usr/bin/env python3
"""Independently audit degree--distance-two domination witnesses.

For a triangle-free graph ``F`` with ``alpha(F) < 18``, put

``Z_v = {u != v : uv is absent and N(u) intersect N(v) is empty}``.

Then ``N(v)`` can be joined to every independent set in ``F[Z_v]``.  Hence
``deg(v) + alpha(F[Z_v]) <= 17``.  In particular:

* if ``deg(v) == 17``, every ``u in Z_v`` gives the forbidden independent
  18-set ``N(v) union {u}``;
* if ``deg(v) == 16``, every nonedge ``ut`` in ``F[Z_v]`` gives the forbidden
  independent 18-set ``N(v) union {u,t}``.

This checker deliberately does not import the production formula builder,
PySAT, or the existing common-model checker.  It parses the complete DIMACS
model, reconstructs the first 4,950 lexicographic edge variables, regenerates
the witnesses, verifies them directly, authenticates all three frozen mask
files by exact digest and count, and classifies overlap. A successful audit
describes one SAT model of an incomplete relaxation; it proves neither
existence nor nonexistence of an exact-seven repair.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import stat
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence


SCHEMA = "ramsey-r3-18-branch1-domination-witness-audit-v1"
STATUS = "VERIFIED_DOMINATION_WITNESS_AUDIT"
ORDER = 100
MAXIMUM_VARIABLE = 154_190
EDGE_VARIABLES = ORDER * (ORDER - 1) // 2
TARGET_SET_SIZE = 18
FIXED_BRANCH_EDGE = (97, 99)
EXPECTED_MODEL_GZIP_SHA256 = (
    "9057db25b785640345e6f724cb1c79313642bb62ec2a19d9f310e25700de024d"
)
EXPECTED_MATRIX_SHA256 = (
    "e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e"
)
EXPECTED_UNIVERSAL_FILE_SHA256 = (
    "91b5709248ff641a315f5a0389b4f3fde3d38514f3b1a8b31b6cad31224f250b"
)
EXPECTED_HISTORY_FILE_SHA256 = (
    "d5100bb5dce48da3ca8ab3810290ff553ebb9d6c87ff9df1f287700563f456b0"
)
EXPECTED_APLUS_FILE_SHA256 = (
    "835137c2df19bc851618761cc0af92400b3fa2677dd00c47101d1074c7406e8b"
)
EXPECTED_UNIVERSAL_MASKS = 251_771
EXPECTED_HISTORY_MASKS = 64_591
EXPECTED_APLUS_MASKS = 4_096


class AuditError(ValueError):
    """A fail-closed input or semantic audit error."""


@dataclass(frozen=True, order=True)
class DominationWitness:
    """One reconstructible forbidden independent 18-set."""

    mask: int
    kind: str
    center: int
    z_vertices: tuple[int, ...]

    @property
    def vertices(self) -> tuple[int, ...]:
        return tuple(index for index in range(ORDER) if self.mask >> index & 1)

    @property
    def mask_hex(self) -> str:
        return f"{self.mask:025x}"


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def read_regular_bytes(path: Path) -> bytes:
    """Read one regular file without following a final symlink."""

    if path.is_symlink():
        raise AuditError(f"input is unreadable or a symlink: {path.name}")
    flags = os.O_RDONLY
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    try:
        descriptor = os.open(path, flags)
    except OSError as error:
        raise AuditError(f"input is unreadable or a symlink: {path.name}") from error
    try:
        metadata = os.fstat(descriptor)
        if not stat.S_ISREG(metadata.st_mode):
            raise AuditError(f"input is not a regular file: {path.name}")
        blocks: list[bytes] = []
        while True:
            block = os.read(descriptor, 1024 * 1024)
            if not block:
                break
            blocks.append(block)
        return b"".join(blocks)
    finally:
        os.close(descriptor)


def strict_json_bytes(raw: bytes, name: str) -> Any:
    """Parse UTF-8 JSON while rejecting duplicate object keys."""

    def pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
        result: dict[str, Any] = {}
        for key, value in items:
            if key in result:
                raise AuditError(f"duplicate JSON key: {key}")
            result[key] = value
        return result

    try:
        return json.loads(raw.decode("utf-8"), object_pairs_hook=pairs)
    except (UnicodeError, json.JSONDecodeError) as error:
        raise AuditError(f"unreadable JSON file: {name}") from error


def strict_json(path: Path) -> Any:
    return strict_json_bytes(read_regular_bytes(path), path.name)


def parse_complete_model_bytes(
    compressed: bytes, maximum_variable: int = MAXIMUM_VARIABLE
) -> tuple[list[bool | None], dict[str, Any]]:
    """Parse one strict gzip CaDiCaL model and require complete assignment."""

    try:
        raw = gzip.decompress(compressed)
        text = raw.decode("ascii")
    except (OSError, EOFError, UnicodeError) as error:
        raise AuditError("model is not a complete ASCII gzip stream") from error
    if not raw.endswith(b"\n") or b"\r" in raw:
        raise AuditError("model must use complete LF-terminated lines")
    lines = text.splitlines()
    if not lines or lines[0] != "s SATISFIABLE":
        raise AuditError("model lacks the exact SAT status line")
    if any(not line.startswith("v ") for line in lines[1:]):
        raise AuditError("model contains a non-assignment line")

    tokens: list[int] = []
    for line in lines[1:]:
        fields = line.split()[1:]
        if not fields:
            raise AuditError("model contains an empty assignment line")
        try:
            tokens.extend(int(field) for field in fields)
        except ValueError as error:
            raise AuditError("model contains a non-integer token") from error
    if not tokens or tokens[-1] != 0 or any(token == 0 for token in tokens[:-1]):
        raise AuditError("model must contain one final zero terminator")

    assignment: list[bool | None] = [None] * (maximum_variable + 1)
    for literal in tokens[:-1]:
        variable = abs(literal)
        if not 1 <= variable <= maximum_variable:
            raise AuditError("model literal lies outside the DIMACS range")
        if assignment[variable] is not None:
            raise AuditError("model assigns a variable more than once")
        assignment[variable] = literal > 0
    if any(value is None for value in assignment[1:]):
        raise AuditError("model does not assign every DIMACS variable")
    return assignment, {
        "gzip_bytes": len(compressed),
        "gzip_sha256": sha256_bytes(compressed),
        "raw_bytes": len(raw),
        "raw_sha256": sha256_bytes(raw),
        "assignment_literals": len(tokens) - 1,
    }


def lexicographic_pairs(order: int) -> list[tuple[int, int]]:
    return [(u, v) for u in range(order) for v in range(u + 1, order)]


def graph_from_assignment(
    assignment: Sequence[bool | None], order: int = ORDER
) -> list[int]:
    pairs = lexicographic_pairs(order)
    if order == ORDER and len(pairs) != EDGE_VARIABLES:
        raise AssertionError("lexicographic edge count mismatch")
    if len(assignment) <= len(pairs):
        raise AuditError("assignment omits primary edge variables")
    rows = [0] * order
    for variable, (u, v) in enumerate(pairs, start=1):
        value = assignment[variable]
        if value is None:
            raise AuditError("primary edge variable is unassigned")
        if value:
            rows[u] |= 1 << v
            rows[v] |= 1 << u
    return rows


def validate_rows(rows: Sequence[int]) -> None:
    order = len(rows)
    full = (1 << order) - 1
    for u, row in enumerate(rows):
        if row < 0 or row & ~full:
            raise AuditError("adjacency row contains an out-of-range bit")
        if row >> u & 1:
            raise AuditError("graph has a loop")
        for v in range(u + 1, order):
            if ((row >> v) & 1) != ((rows[v] >> u) & 1):
                raise AuditError("graph is not symmetric")


def triangle_witness(rows: Sequence[int]) -> tuple[int, int, int] | None:
    for u, row in enumerate(rows):
        later = row & ~((1 << (u + 1)) - 1)
        while later:
            bit = later & -later
            later ^= bit
            v = bit.bit_length() - 1
            common = rows[u] & rows[v] & ~((1 << (v + 1)) - 1)
            if common:
                w = (common & -common).bit_length() - 1
                return (u, v, w)
    return None


def is_independent(rows: Sequence[int], mask: int) -> bool:
    remaining = mask
    while remaining:
        bit = remaining & -remaining
        remaining ^= bit
        vertex = bit.bit_length() - 1
        if rows[vertex] & remaining:
            return False
    return True


def z_vertices(rows: Sequence[int], center: int) -> list[int]:
    neighborhood = rows[center]
    return [
        other
        for other in range(len(rows))
        if other != center
        and not (neighborhood >> other & 1)
        and not (neighborhood & rows[other])
    ]


def domination_witnesses(
    rows: Sequence[int], *, d16_limit: int | None = None
) -> tuple[list[DominationWitness], dict[str, Any]]:
    """Generate all degree-17 and a bounded prefix of degree-16 witnesses."""

    validate_rows(rows)
    triangle = triangle_witness(rows)
    if triangle is not None:
        raise AuditError(f"model graph contains triangle {triangle}")
    order = len(rows)
    if order < TARGET_SET_SIZE:
        return [], {
            "degree_histogram": {},
            "degree17_candidates": 0,
            "degree16_candidates_total": 0,
            "degree16_candidates_emitted": 0,
            "degree16_truncated": False,
            "nonempty_z": [],
        }
    if d16_limit is not None and d16_limit < 0:
        raise AuditError("degree-16 witness limit must be nonnegative")

    records: dict[int, DominationWitness] = {}
    degree_histogram: dict[str, int] = {}
    nonempty_z: list[dict[str, Any]] = []
    degree17_candidates = 0
    degree16_candidates_total = 0
    degree16_candidates_emitted = 0
    degree16_truncated = False

    for center, neighborhood in enumerate(rows):
        degree = neighborhood.bit_count()
        degree_histogram[str(degree)] = degree_histogram.get(str(degree), 0) + 1
        if degree not in (16, 17):
            continue
        zset = z_vertices(rows, center)
        if zset:
            nonempty_z.append({"center": center, "degree": degree, "z": zset})
        if degree == 17:
            for other in zset:
                degree17_candidates += 1
                mask = neighborhood | (1 << other)
                if mask.bit_count() != TARGET_SET_SIZE or not is_independent(rows, mask):
                    raise AuditError("invalid degree-17 domination witness")
                records.setdefault(
                    mask,
                    DominationWitness(mask, "degree17", center, (other,)),
                )
            continue

        for first_index, first in enumerate(zset):
            for second in zset[first_index + 1 :]:
                if rows[first] >> second & 1:
                    continue
                degree16_candidates_total += 1
                if d16_limit is not None and degree16_candidates_emitted >= d16_limit:
                    degree16_truncated = True
                    continue
                mask = neighborhood | (1 << first) | (1 << second)
                if mask.bit_count() != TARGET_SET_SIZE or not is_independent(rows, mask):
                    raise AuditError("invalid degree-16 domination witness")
                records.setdefault(
                    mask,
                    DominationWitness(
                        mask, "degree16", center, (first, second)
                    ),
                )
                degree16_candidates_emitted += 1

    witnesses = sorted(records.values())
    return witnesses, {
        "degree_histogram": degree_histogram,
        "degree17_candidates": degree17_candidates,
        "degree16_candidates_total": degree16_candidates_total,
        "degree16_candidates_emitted": degree16_candidates_emitted,
        "degree16_truncated": degree16_truncated,
        "nonempty_z": nonempty_z,
        "distinct_masks": len(witnesses),
    }


def load_mask_family_with_identity(
    path: Path,
    *,
    width: int = 25,
    expected_sha256: str | None = None,
    expected_count: int | None = None,
) -> tuple[set[int], dict[str, Any]]:
    raw = read_regular_bytes(path)
    identity = {
        "basename": path.name,
        "bytes": len(raw),
        "sha256": sha256_bytes(raw),
    }
    if expected_sha256 is not None and identity["sha256"] != expected_sha256:
        raise AuditError(f"mask-family SHA-256 mismatch: {path.name}")
    payload = strict_json_bytes(raw, path.name)
    if not isinstance(payload, dict) or not isinstance(payload.get("masks"), list):
        raise AuditError(f"mask family has no masks list: {path.name}")
    result: set[int] = set()
    for encoded in payload["masks"]:
        if (
            not isinstance(encoded, str)
            or len(encoded) != width
            or encoded.lower() != encoded
            or any(char not in "0123456789abcdef" for char in encoded)
        ):
            raise AuditError(f"noncanonical mask in {path.name}")
        mask = int(encoded, 16)
        if mask in result:
            raise AuditError(f"duplicate mask in {path.name}")
        result.add(mask)
    count = payload.get("masks_count")
    if count is not None and count != len(result):
        raise AuditError(f"mask count mismatch: {path.name}")
    if expected_count is not None and len(result) != expected_count:
        raise AuditError(f"production mask count mismatch: {path.name}")
    identity["masks"] = len(result)
    return result, identity


def load_mask_family(path: Path, *, width: int = 25) -> set[int]:
    result, _ = load_mask_family_with_identity(path, width=width)
    return result


def read_seed_matrix(path: Path) -> tuple[list[int], dict[str, Any]]:
    raw = path.read_bytes()
    try:
        lines = raw.decode("ascii").splitlines()
        matrix = [list(map(int, line.split())) for line in lines if line.strip()]
    except (OSError, UnicodeError, ValueError) as error:
        raise AuditError("seed matrix is unreadable") from error
    order = len(matrix)
    if order != ORDER or any(len(row) != order for row in matrix):
        raise AuditError("seed matrix is not 100 by 100")
    rows = [0] * order
    for u, row in enumerate(matrix):
        for v, value in enumerate(row):
            if value not in (0, 1):
                raise AuditError("seed matrix is not binary")
            if u == v and value:
                raise AuditError("seed matrix has a loop")
            if value != matrix[v][u]:
                raise AuditError("seed matrix is not symmetric")
            if value:
                rows[u] |= 1 << v
    return rows, {"bytes": len(raw), "sha256": sha256_bytes(raw)}


def fixed_base_contains(seed_rows: Sequence[int], mask: int) -> bool:
    base = list(seed_rows)
    u, v = FIXED_BRANCH_EDGE
    base[u] &= ~(1 << v)
    base[v] &= ~(1 << u)
    return mask.bit_count() == TARGET_SET_SIZE and is_independent(base, mask)


def classify_overlaps(
    witnesses: Sequence[DominationWitness],
    *,
    universal: set[int],
    history: set[int],
    aplus: set[int],
    seed_rows: Sequence[int],
) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for witness in witnesses:
        item = asdict(witness)
        item.update(
            {
                "mask": witness.mask_hex,
                "vertices": list(witness.vertices),
                "z_vertices": list(witness.z_vertices),
                "overlap": {
                    "universal": witness.mask in universal,
                    "history": witness.mask in history,
                    "aplus": witness.mask in aplus,
                    "fixed_base": fixed_base_contains(seed_rows, witness.mask),
                },
            }
        )
        result.append(item)
    return result


def audit(
    *,
    model_bytes: bytes,
    seed_path: Path,
    universal_path: Path,
    history_path: Path,
    aplus_path: Path,
    require_production_hashes: bool,
) -> dict[str, Any]:
    assignment, model_info = parse_complete_model_bytes(model_bytes)
    if require_production_hashes and model_info["gzip_sha256"] != EXPECTED_MODEL_GZIP_SHA256:
        raise AuditError("common-model gzip SHA-256 mismatch")
    rows = graph_from_assignment(assignment)
    witnesses, generation = domination_witnesses(rows)
    seed_rows, seed_info = read_seed_matrix(seed_path)
    if require_production_hashes and seed_info["sha256"] != EXPECTED_MATRIX_SHA256:
        raise AuditError("seed-matrix SHA-256 mismatch")
    universal, universal_identity = load_mask_family_with_identity(
        universal_path,
        expected_sha256=(
            EXPECTED_UNIVERSAL_FILE_SHA256 if require_production_hashes else None
        ),
        expected_count=(
            EXPECTED_UNIVERSAL_MASKS if require_production_hashes else None
        ),
    )
    history, history_identity = load_mask_family_with_identity(
        history_path,
        expected_sha256=(
            EXPECTED_HISTORY_FILE_SHA256 if require_production_hashes else None
        ),
        expected_count=(EXPECTED_HISTORY_MASKS if require_production_hashes else None),
    )
    aplus, aplus_identity = load_mask_family_with_identity(
        aplus_path,
        expected_sha256=(
            EXPECTED_APLUS_FILE_SHA256 if require_production_hashes else None
        ),
        expected_count=(EXPECTED_APLUS_MASKS if require_production_hashes else None),
    )
    records = classify_overlaps(
        witnesses,
        universal=universal,
        history=history,
        aplus=aplus,
        seed_rows=seed_rows,
    )
    overlap_counts = {
        name: sum(record["overlap"][name] for record in records)
        for name in ("universal", "history", "aplus", "fixed_base")
    }
    return {
        "schema": SCHEMA,
        "status": STATUS,
        "claim_boundary": (
            "This audit reconstructs structured independent-18 witnesses in "
            "one checked model of an incomplete relaxation. It proves no "
            "exact-seven repair and no branch or global Ramsey result."
        ),
        "model": model_info,
        "seed": seed_info,
        "generation": generation,
        "witnesses": records,
        "overlap_counts": overlap_counts,
        "old_family_counts": {
            "universal": len(universal),
            "history": len(history),
            "aplus": len(aplus),
        },
        "mask_families": {
            "universal": universal_identity,
            "history": history_identity,
            "aplus": aplus_identity,
        },
    }


def _model_bytes(path_text: str) -> bytes:
    if path_text == "-":
        return sys.stdin.buffer.read()
    try:
        return Path(path_text).read_bytes()
    except OSError as error:
        raise AuditError("model file is unreadable") from error


def main(argv: Sequence[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, help="gzip model path, or - for stdin")
    parser.add_argument(
        "--matrix",
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
        "--aplus",
        type=Path,
        default=here / "r3_18_budget7_branch1_cegar_Aplus_batch.json",
    )
    parser.add_argument(
        "--allow-unpinned-inputs",
        action="store_true",
        help="disable production model/matrix hash requirements for fixtures",
    )
    args = parser.parse_args(argv)
    try:
        payload = audit(
            model_bytes=_model_bytes(args.model),
            seed_path=args.matrix.resolve(),
            universal_path=args.universal.resolve(),
            history_path=args.history.resolve(),
            aplus_path=args.aplus.resolve(),
            require_production_hashes=not args.allow_unpinned_inputs,
        )
    except (AuditError, OSError) as error:
        print(
            json.dumps(
                {
                    "schema": SCHEMA,
                    "status": "FAILED_DOMINATION_WITNESS_AUDIT",
                    "error": str(error),
                },
                sort_keys=True,
            )
        )
        return 2
    json.dump(payload, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
