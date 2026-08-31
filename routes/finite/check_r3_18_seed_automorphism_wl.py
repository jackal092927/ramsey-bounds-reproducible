#!/usr/bin/env python3
"""Certify trivial seed automorphism group by deterministic 1-WL refinement."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any, Sequence


ORDER = 100
SEED_SHA256 = "e6527601f72ebb2d3aed11adcdd2ffb0c6aab5e326d81d439c10ee468844e85e"


class AuditError(ValueError):
    """Raised when the seed or refinement record is malformed."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_seed(path: Path, expected_sha256: str | None = SEED_SHA256) -> list[list[int]]:
    metadata = os.lstat(path)
    if not stat.S_ISREG(metadata.st_mode):
        raise AuditError("seed must be a non-symlink regular file")
    raw = path.read_bytes()
    if expected_sha256 is not None and hashlib.sha256(raw).hexdigest() != expected_sha256:
        raise AuditError("seed SHA-256 mismatch")
    try:
        rows = [[int(token) for token in line.split()] for line in raw.decode("ascii").splitlines()]
    except (UnicodeDecodeError, ValueError) as error:
        raise AuditError("seed is not an ASCII zero-one matrix") from error
    if len(rows) != ORDER or any(len(row) != ORDER for row in rows):
        raise AuditError("seed dimensions are not 100 by 100")
    if any(value not in (0, 1) for row in rows for value in row):
        raise AuditError("seed contains a non-Boolean entry")
    if any(rows[v][v] for v in range(ORDER)):
        raise AuditError("seed diagonal is nonzero")
    if any(rows[u][v] != rows[v][u] for u in range(ORDER) for v in range(u)):
        raise AuditError("seed matrix is asymmetric")
    return rows


def canonicalize(signatures: Sequence[Any]) -> list[int]:
    palette = {signature: color for color, signature in enumerate(sorted(set(signatures)))}
    return [palette[signature] for signature in signatures]


def refine(matrix: list[list[int]]) -> tuple[list[int], list[dict[str, Any]]]:
    colors = [sum(row) for row in matrix]
    rounds = [
        {
            "classes": len(set(colors)),
            "index": 0,
            "largest_class": max(Counter(colors).values()),
            "meaning": "degree initialization",
            "size_histogram": dict(sorted(Counter(Counter(colors).values()).items())),
        }
    ]
    for index in range(1, ORDER + 1):
        signatures = []
        for vertex in range(ORDER):
            neighbour_colors = tuple(
                sorted(colors[other] for other in range(ORDER) if matrix[vertex][other])
            )
            signatures.append((colors[vertex], neighbour_colors))
        updated = canonicalize(signatures)
        sizes = Counter(updated)
        rounds.append(
            {
                "classes": len(sizes),
                "index": index,
                "largest_class": max(sizes.values()),
                "meaning": "one-dimensional Weisfeiler-Leman refinement",
                "size_histogram": dict(sorted(Counter(sizes.values()).items())),
            }
        )
        colors = updated
        if len(sizes) == ORDER or rounds[-1]["classes"] == rounds[-2]["classes"]:
            break
    return colors, rounds


def audit(seed: Path) -> dict[str, Any]:
    matrix = parse_seed(seed)
    colors, rounds = refine(matrix)
    if [entry["classes"] for entry in rounds[:3]] != [3, 15, 100]:
        raise AuditError("seed does not have the frozen 3,15,100 refinement profile")
    if len(set(colors)) != ORDER:
        raise AuditError("1-WL did not individualize every seed vertex")
    return {
        "automorphism_group_order": 1,
        "branch_symmetry_transfer_available": False,
        "logic": (
            "Every graph automorphism preserves degree colors and each subsequent "
            "1-WL color.  Since round two has 100 singleton color classes, every "
            "automorphism fixes every vertex."
        ),
        "refinement_rounds": rounds,
        "schema": "ramsey-r3-18-n100-seed-automorphism-wl-audit-v1",
        "seed_sha256": sha256_file(seed),
        "status": "TRIVIAL_AUTOMORPHISM_GROUP_CERTIFIED_BY_1WL",
    }


def atomic_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "w", encoding="ascii", newline="\n") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True, ensure_ascii=True)
            handle.write("\n")
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def main(argv: Sequence[str] | None = None) -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--seed", type=Path, default=here / "certificates" / "r3_18_n100_nearmiss.txt"
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    seed = Path(os.path.abspath(os.fspath(args.seed)))
    result = audit(seed)
    if args.output is not None:
        atomic_json(Path(os.path.abspath(os.fspath(args.output))), result)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
