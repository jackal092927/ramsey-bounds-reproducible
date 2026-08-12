#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
venv_dir="${repo_root}/.venv"

if command -v uv >/dev/null 2>&1; then
  UV_CACHE_DIR="${repo_root}/.uv-cache" uv sync --frozen --no-dev
else
  python3 -m venv "${venv_dir}"
  "${venv_dir}/bin/python" -m pip install --upgrade pip
  "${venv_dir}/bin/python" -m pip install -r "${repo_root}/requirements-repro.txt"
fi
"${venv_dir}/bin/python" - <<'PY'
import flint
import mpmath
import pysat
print("python environment ready")
print("python-flint", flint.__version__)
print("mpmath", mpmath.__version__)
print("python-sat", pysat.__version__)
PY
