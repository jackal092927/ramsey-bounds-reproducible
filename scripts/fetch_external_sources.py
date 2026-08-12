#!/usr/bin/env python3
"""Fetch version-pinned arXiv sources and verify selected TeX members."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import tarfile
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def extract_member(archive: bytes, basename: str) -> bytes:
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:*") as bundle:
        matches = [
            member
            for member in bundle.getmembers()
            if member.isfile() and Path(member.name).name == basename
        ]
        if len(matches) != 1:
            names = [member.name for member in matches]
            raise SystemExit(f"expected one {basename!r} member; found {names}")
        handle = bundle.extractfile(matches[0])
        if handle is None:
            raise SystemExit(f"cannot read {matches[0].name}")
        return handle.read()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        type=Path,
        default=ROOT / "external_sources" / "manifest.json",
    )
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    if args.output_dir is not None:
        args.output_dir.mkdir(parents=True, exist_ok=True)

    for source in manifest["sources"]:
        with urllib.request.urlopen(source["archive_url"]) as response:
            archive = response.read()
        data = extract_member(archive, source["member_basename"])
        actual = digest(data)
        if actual != source["sha256"]:
            raise SystemExit(f"{source['key']}: {actual} != {source['sha256']}")
        if args.output_dir is not None:
            destination = args.output_dir / (
                f"{source['key']}-{source['member_basename']}"
            )
            destination.write_bytes(data)
            location = str(destination)
        else:
            location = "(not written)"
        print(f"OK {source['key']} {actual} {location}")


if __name__ == "__main__":
    main()
