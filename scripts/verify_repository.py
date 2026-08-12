#!/usr/bin/env python3
"""Fast integrity and environment audit for the publication repository."""

from __future__ import annotations

import hashlib
import importlib.metadata
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "routes/upper/EXACT_DIAGONAL_NEXT_CANDIDATE.md": "e4ea58def640593690a7545e111c3b38f1bfcf8a5735fe7985600481e0bf36d4",
    "routes/upper/check_exact_diagonal_next.py": "17db00d9374ce3ba3e68a3a4626ec2c51a70ec45a307972dacc245b153382c3e",
    "routes/upper/check_retained_spine_exact_diagonal_next.py": "e2035cbffefcb147141fcee4831cac2af085f26d9183091ee20d90acc89ac87b",
    "routes/upper/independent_check_exact_diagonal_next.py": "fc379e3b861b69054aadaa80ebc3c791cb8358f22c9b0aa01070c56aa131c26c",
    "routes/upper/referee_check_exact_diagonal_next.py": "3c30f72ddc24848f2b72c278f35b5d8bd6296ae8a40b045d30c5b7e087bd7150",
    "routes/upper/INDEPENDENT_EXACT_DIAGONAL_NEXT_REFEREE.md": "a21402a5dad40490bd493201f0cf6579c5d94ee74aa8460d7117298a737d3ef3",
    "routes/lower/HISTORY_WEIGHT_OPTIMIZATION_NEXT.md": "2234a769d7798a79174cbfb362ada64f5d760aefbe7e6d4fb8763cd5633a0312",
    "routes/lower/history_weight_optimization_next_check.py": "616040b91aad4becf92dcfbe13b7e6d49a3c9c73f0f222ba56114104f1c7d554",
    "routes/lower/INDEPENDENT_HISTORY_WEIGHT_OPTIMIZATION_REFEREE.md": "ef6ddbce4f403bdf942a6a6c0ac3ca5ace110f5f2a8cbd0042a3658a9a02f008",
    "routes/finite/R3_18_BUDGET6_AUDIT.md": "a8bd5742317b6842e3572670faba445fc4097d19c5480debf702a86d517d1fe8",
    "routes/finite/INDEPENDENT_R3_18_BUDGET6_COMPLETE_REFEREE.md": "1bb634ed1a6181064ac2ae0277ea6582cd2627a76a92208907cc1532d49bfede",
    "routes/finite/R3_18_BUDGET7_FIRST_ROUND.md": "4819d718a0a91cacde11d3e0e448478bda589fecfee1955def7e124ceefab4be",
    "routes/finite/r3_18_budget7_first_round_summary.json": "c4ddd50664698421c0e64b984af3401b63dd6942c72f4f73a94af4d17c47aaed",
}
VERSIONS = {
    "mpmath": "1.4.1",
    "python-flint": "0.9.0",
    "python-sat": "1.9.dev13",
    "six": "1.17.0",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    failures: list[str] = []
    if sys.version_info[:2] != (3, 11):
        failures.append(f"reference Python is 3.11; found {sys.version.split()[0]}")

    for package, expected in VERSIONS.items():
        try:
            actual = importlib.metadata.version(package)
        except importlib.metadata.PackageNotFoundError:
            failures.append(f"missing package {package}=={expected}")
            continue
        if actual != expected:
            failures.append(f"{package}: {actual} != {expected}")

    for relative, expected in EXPECTED.items():
        path = ROOT / relative
        if not path.is_file():
            failures.append(f"missing frozen file {relative}")
            continue
        actual = sha256(path)
        if actual != expected:
            failures.append(f"hash mismatch {relative}: {actual} != {expected}")

    if failures:
        raise SystemExit("\n".join(failures))
    print(f"REPOSITORY_INTEGRITY_VERIFIED ({len(EXPECTED)} frozen files)")


if __name__ == "__main__":
    main()
