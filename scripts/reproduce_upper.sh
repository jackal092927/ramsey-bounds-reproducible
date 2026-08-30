#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python_bin="${PYTHON:-${repo_root}/.venv/bin/python}"

if ! "${python_bin}" -c 'import sys; sys.exit(0 if __debug__ else 2)'; then
  echo "refusing optimized Python: proof-critical assertions must remain enabled" >&2
  exit 2
fi

cd "${repo_root}/routes/upper"
"${python_bin}" check_exact_diagonal_next.py
"${python_bin}" check_retained_spine_exact_diagonal_next.py
"${python_bin}" independent_check_exact_diagonal_next.py
"${python_bin}" referee_check_exact_diagonal_next.py

echo UPPER_TRANSFER_CERTIFICATE_REPRODUCED
