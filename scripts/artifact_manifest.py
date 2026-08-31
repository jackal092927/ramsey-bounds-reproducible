#!/usr/bin/env python3
"""Strict parser for release-artifact manifests.

The release manifest is a trust boundary: its names are later joined to a
caller-supplied directory and its digests are used as publication identities.
Keep all syntax and path validation in this small dependency-free module so
every consumer can apply the same fail-closed rules.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import NamedTuple


SHA256_RE = re.compile(r"[0-9a-f]{64}\Z", flags=re.ASCII)
NONNEGATIVE_INTEGER_RE = re.compile(r"[0-9]+\Z", flags=re.ASCII)
SAFE_BASENAME_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._+-]*\Z", flags=re.ASCII)


class ManifestFormatError(ValueError):
    """Raised when an artifact manifest is not in the canonical safe format."""


class ManifestEntry(NamedTuple):
    """One validated release-artifact identity."""

    checksum: str
    size: int
    name: str


def _error(path: Path, number: int, message: str) -> ManifestFormatError:
    return ManifestFormatError(f"{path}:{number}: {message}")


def load_manifest(path: Path) -> list[ManifestEntry]:
    """Parse *path* using the repository's canonical strict TSV format.

    Blank lines and comment lines beginning with ``#`` are ignored.  Every
    other line must contain exactly ``sha256<TAB>size<TAB>name``.  SHA-256
    values are canonical lowercase hexadecimal, sizes are unsigned decimal
    integers, and names are conservative ASCII basenames (never paths or
    command-line options).  Asset names must be unique.
    """

    entries: list[ManifestEntry] = []
    first_line_by_name: dict[str, int] = {}
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw or raw.startswith("#"):
            continue

        fields = raw.split("\t")
        if len(fields) != 3:
            raise _error(path, number, "expected exactly three tab-separated fields")
        checksum, raw_size, name = fields

        if SHA256_RE.fullmatch(checksum) is None:
            raise _error(path, number, "sha256 must be exactly 64 lowercase hex digits")
        if NONNEGATIVE_INTEGER_RE.fullmatch(raw_size) is None:
            raise _error(path, number, "size must be a non-negative decimal integer")
        if SAFE_BASENAME_RE.fullmatch(name) is None:
            raise _error(path, number, f"unsafe artifact basename {name!r}")
        if name in first_line_by_name:
            first = first_line_by_name[name]
            raise _error(
                path,
                number,
                f"duplicate artifact name {name!r}; first at line {first}",
            )

        first_line_by_name[name] = number
        entries.append(ManifestEntry(checksum, int(raw_size), name))

    return entries
