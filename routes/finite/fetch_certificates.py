#!/usr/bin/env python3
"""Fetch the exact pinned certificates in certificate_manifest.json."""

from __future__ import annotations

import argparse
import hashlib
import json
import urllib.parse
import urllib.request
from pathlib import Path


def raw_url(entry: dict) -> str:
    slug = entry["repository"].removeprefix("https://github.com/")
    path = urllib.parse.quote(entry["repository_path"], safe="/")
    return (
        f"https://raw.githubusercontent.com/{slug}/{entry['commit']}/{path}"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    default_manifest = Path(__file__).with_name("certificate_manifest.json")
    parser.add_argument("--manifest", type=Path, default=default_manifest)
    parser.add_argument(
        "--output-dir", type=Path, default=Path(__file__).with_name("certificates")
    )
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    args.output_dir.mkdir(parents=True, exist_ok=True)

    for entry in manifest["certificates"]:
        url = raw_url(entry)
        with urllib.request.urlopen(url) as response:
            data = response.read()
        digest = hashlib.sha256(data).hexdigest()
        if digest != entry["sha256"]:
            raise SystemExit(
                f"hash mismatch for {entry['local_name']}: {digest}"
            )
        destination = args.output_dir / entry["local_name"]
        destination.write_bytes(data)
        print(f"OK {digest} {destination} <- {url}")


if __name__ == "__main__":
    main()
