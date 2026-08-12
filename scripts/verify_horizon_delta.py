#!/usr/bin/env python3
"""Reproduce an unsound acceptance by the pinned HorizonMath checker.

This script intentionally reuses the public HorizonMath verifier.  Passing it
only reproduces a known orientation-union bug and does not establish a Ramsey
upper bound.  Corrected verifiers must reject this degree-5 artifact.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tarfile
import tempfile
import urllib.request


ARXIV_SOURCE_URL = "https://arxiv.org/e-print/2603.15617v1"
ARXIV_SOURCE_SHA256 = "47de19e5a03948e65416666e85de8d60d784e0ac8c382a2e8490644b75e78c12"
CERTIFICATE_MEMBER = "sections/solution_code3.tex"

HORIZON_REPOSITORY = "https://github.com/ewang26/HorizonMath.git"
HORIZON_COMMIT = "d509c90a75202a45585b01f75762188db4fa2d2d"
VALIDATOR_PATH = Path("validators/ramsey_asymptotic.py")
VALIDATOR_SHA256 = "0c8e144e4c7419774be17608413487448969d58a5636423b2fe4bd46e7a14cc2"

ORIGINAL_A5 = -0.0778
CANDIDATE_A5 = -0.07795


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def require_hash(path: Path, expected: str, label: str) -> None:
    actual = sha256(path)
    if actual != expected:
        raise RuntimeError(f"{label} SHA-256 mismatch: expected {expected}, got {actual}")


def run(command: list[str], *, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=cwd,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def load_published_certificate(source_tar: Path) -> dict:
    with tarfile.open(source_tar, "r:*") as archive:
        member = archive.getmember(CERTIFICATE_MEMBER)
        handle = archive.extractfile(member)
        if handle is None:
            raise RuntimeError(f"Could not read {CERTIFICATE_MEMBER}")
        source = handle.read().decode("utf-8")

    namespace: dict = {}
    exec(compile(source, CERTIFICATE_MEMBER, "exec"), namespace)
    certificate = namespace["proposed_solution"]()
    if certificate["polynomial_coeffs"][-1] != ORIGINAL_A5:
        raise RuntimeError("Pinned source no longer contains the expected original coefficient")
    return certificate


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="ramsey-horizon-") as temp_name:
        temp = Path(temp_name)
        source_tar = temp / "horizon-arxiv-v1.tar"
        repo = temp / "HorizonMath"

        urllib.request.urlretrieve(ARXIV_SOURCE_URL, source_tar)
        require_hash(source_tar, ARXIV_SOURCE_SHA256, "arXiv source archive")

        run(["git", "clone", "--quiet", HORIZON_REPOSITORY, str(repo)])
        run(["git", "checkout", "--quiet", "--detach", HORIZON_COMMIT], cwd=repo)
        require_hash(repo / VALIDATOR_PATH, VALIDATOR_SHA256, "HorizonMath validator")

        certificate = load_published_certificate(source_tar)
        certificate["polynomial_coeffs"][-1] = CANDIDATE_A5
        certificate["notes"] = (
            "Pinned HorizonMath arXiv v1 solution_code3 certificate with only "
            "the degree-5 coefficient changed from -0.0778 to -0.07795."
        )

        candidate_path = temp / "candidate.json"
        candidate_path.write_text(json.dumps(certificate), encoding="utf-8")

        completed = run(
            [sys.executable, "-m", "validators.ramsey_asymptotic", str(candidate_path)],
            cwd=repo,
        )
        print(completed.stdout, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
