#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
venv_dir="${repo_root}/.venv"

if ! command -v uv >/dev/null 2>&1; then
  echo "The canonical environment requires uv 0.10.2; no unhashed pip fallback is used." >&2
  echo "Install uv 0.10.2, then rerun scripts/bootstrap.sh." >&2
  exit 2
fi

uv_version="$(uv --version | awk '{print $2}')"
if [[ "${uv_version}" != "0.10.2" ]]; then
  echo "Expected uv 0.10.2; found $(uv --version)." >&2
  exit 2
fi

UV_CACHE_DIR="${repo_root}/.uv-cache" uv sync --frozen --no-dev
"${venv_dir}/bin/python" - <<'PY'
import flint
import mpmath
import pysat
print("python environment ready")
print("python-flint", flint.__version__)
print("mpmath", mpmath.__version__)
print("python-sat", pysat.__version__)
PY
