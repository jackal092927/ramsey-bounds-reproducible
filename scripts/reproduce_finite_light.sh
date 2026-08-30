#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
python_bin="${PYTHON:-${repo_root}/.venv/bin/python}"

cd "${repo_root}"
"${python_bin}" -m unittest discover -s routes/finite -t . -p 'test_*.py' -v
"${python_bin}" routes/finite/check_r3_18_seqcounter.py --schema-only
"${python_bin}" routes/finite/check_r3_18_budget7.py
"${python_bin}" routes/finite/verify_ramsey.py routes/finite/certificates/alphaevolve_R3_13_ge_61.txt 3 13
"${python_bin}" routes/finite/verify_ramsey.py routes/finite/certificates/alphaevolve_R3_18_ge_100.txt 3 18
"${python_bin}" routes/finite/verify_ramsey.py routes/finite/certificates/alphaevolve_R4_15_ge_159.txt 4 15
"${python_bin}" routes/finite/verify_ramsey.py routes/finite/certificates/scale_R3_17_ge_93.txt 3 17
"${python_bin}" routes/finite/verify_ramsey.py routes/finite/certificates/scale_R4_15_ge_160.txt 4 15

echo FINITE_LIGHT_REPRODUCED
