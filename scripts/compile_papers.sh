#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

for paper in upper lower finite; do
  paper_dir="${repo_root}/papers/${paper}"
  latexmk -pdf -interaction=nonstopmode -halt-on-error -cd "${paper_dir}/main.tex"
done

echo PAPERS_COMPILED

