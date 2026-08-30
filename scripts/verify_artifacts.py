#!/usr/bin/env python3
"""Verify external artifact identity against a TSV manifest."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MANIFEST = ROOT / "artifacts" / "MANIFEST.tsv"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_manifest(path: Path) -> list[tuple[str, int, str]]:
    rows: list[tuple[str, int, str]] = []
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw or raw.startswith("#"):
            continue
        fields = raw.split("\t")
        if len(fields) != 3:
            raise ValueError(f"{path}:{number}: expected sha256, size, name")
        checksum, size, name = fields
        rows.append((checksum, int(size), name))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument(
        "--exact",
        action="store_true",
        help="also reject extra files or subdirectories not named by the manifest",
    )
    args = parser.parse_args()

    rows = load_manifest(args.manifest)
    failures: list[str] = []
    expected_names = {name for _, _, name in rows}
    if args.exact:
        if not args.directory.is_dir():
            failures.append(f"NOT_A_DIRECTORY {args.directory}")
        else:
            actual_names = {entry.name for entry in args.directory.iterdir()}
            for name in sorted(actual_names - expected_names):
                failures.append(f"UNEXPECTED {name}")
            for name in sorted(expected_names - actual_names):
                failures.append(f"MISSING {name}")

    for expected_hash, expected_size, name in rows:
        path = args.directory / name
        if not path.is_file():
            if f"MISSING {name}" not in failures:
                failures.append(f"MISSING {name}")
            continue
        actual_size = path.stat().st_size
        actual_hash = sha256(path)
        if actual_size != expected_size:
            failures.append(f"SIZE {name}: {actual_size} != {expected_size}")
        if actual_hash != expected_hash:
            failures.append(f"SHA256 {name}: {actual_hash} != {expected_hash}")
        if actual_size == expected_size and actual_hash == expected_hash:
            print(f"PASS {name}")

    if failures:
        raise SystemExit("\n".join(failures))
    if args.exact:
        print("EXACT_ARTIFACT_MANIFEST_VERIFIED")
    else:
        print("ARTIFACT_MANIFEST_VERIFIED")


if __name__ == "__main__":
    main()
