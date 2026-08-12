#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python_bin="${PYTHON:-${repo_root}/.venv/bin/python}"

cd "${repo_root}"
"${python_bin}" routes/lower/hms_appendix_bridge_check.py
"${python_bin}" routes/lower/hms_parameter_optimization_check.py
"${python_bin}" routes/lower/history_dependent_ledger_check.py
"${python_bin}" routes/lower/history_weight_optimization_next_check.py

echo LOWER_THEOREM_REPRODUCED
