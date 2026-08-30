#!/usr/bin/env python3
"""Fail when the canonical LaTeX build log contains unresolved references."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOG = ROOT / "papers" / "unified" / "main.log"
FORBIDDEN = (
    r"LaTeX Error",
    r"Citation [`'].+[`'] .* undefined",
    r"Reference [`'].+[`'] .* undefined",
    r"There were undefined references",
    r"There were undefined citations",
    r"multiply defined",
)


def main() -> None:
    if not LOG.is_file():
        raise SystemExit(f"missing canonical build log: {LOG}")
    text = LOG.read_text(encoding="utf-8", errors="replace")
    failures = [pattern for pattern in FORBIDDEN if re.search(pattern, text)]
    if failures:
        raise SystemExit("unresolved LaTeX diagnostics: " + ", ".join(failures))
    print("CANONICAL_LATEX_REFERENCES_RESOLVED")


if __name__ == "__main__":
    main()
