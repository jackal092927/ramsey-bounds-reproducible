#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python_bin="${repo_root}/.venv/bin/python"
if [[ ! -x "${python_bin}" ]]; then
  python_bin="$(command -v python3)"
fi

# Freeze PDF metadata to the dated manuscript (2026-08-30T07:00:00Z).
# pdfTeX also derives a stable trailer ID from this reproducible-build epoch.
export SOURCE_DATE_EPOCH=1788073200
export FORCE_SOURCE_DATE=1

"${python_bin}" "${repo_root}/scripts/materialize_unified_paper.py"
latexmk -pdf -interaction=nonstopmode -halt-on-error -cd \
  "${repo_root}/papers/unified/main.tex"

echo UNIFIED_PAPER_COMPILED
