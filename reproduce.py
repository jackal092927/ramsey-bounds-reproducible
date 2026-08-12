#!/usr/bin/env python3
"""Tiered, non-destructive reproduction entry point."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
UPPER = ROOT / "routes" / "upper"
MANIFEST = ROOT / "artifacts" / "MANIFEST.tsv"
CHAIN = [
    "certificate-higher-order-quintic-v1.json",
    "certificate-higher-order-quintic-chain-v2.json",
    "certificate-higher-order-sextic-chain-v3.json",
    "certificate-higher-order-octic-chain-v4.json",
    "certificate-higher-order-decic-chain-v5.json",
    "certificate-higher-order-tetradecic-chain-v6.json",
]


def run(command: list[str], *, cwd: Path = ROOT, timeout: float | None = None) -> None:
    print("\n>>> " + " ".join(command), flush=True)
    environment = os.environ.copy()
    environment["PYTHON"] = sys.executable
    subprocess.run(
        command,
        cwd=cwd,
        env=environment,
        check=True,
        timeout=timeout,
    )


def quick() -> None:
    run([sys.executable, "scripts/verify_repository.py"])
    run(["bash", "scripts/reproduce_upper.sh"])
    run([sys.executable, "routes/lower/history_weight_optimization_next_check.py"])
    run(["bash", "scripts/reproduce_finite_light.sh"])
    print("\nQUICK_REPRODUCTION_PASS")


def full() -> None:
    quick()
    chain_paths = [str(UPPER / name) for name in CHAIN]
    run([sys.executable, "verify_chain_arb.py", *chain_paths], cwd=UPPER)
    for path in chain_paths:
        run([sys.executable, "verify_region_direct_arb.py", path], cwd=UPPER)
    run([sys.executable, "audit_tests.py"], cwd=UPPER)
    run(["bash", "scripts/reproduce_lower.sh"])
    print("\nFULL_REPRODUCTION_PASS")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def manifest_entries() -> list[tuple[str, int, str]]:
    entries: list[tuple[str, int, str]] = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        digest, size, name = line.split("\t")
        entries.append((digest, int(size), name))
    return entries


def check_assets(directory: Path) -> dict[str, Path]:
    found: dict[str, Path] = {}
    failures: list[str] = []
    for expected_hash, expected_size, name in manifest_entries():
        path = directory / name
        if not path.is_file():
            failures.append(f"missing {path}")
            continue
        size = path.stat().st_size
        digest = sha256(path)
        if size != expected_size:
            failures.append(f"{name}: {size} bytes != {expected_size}")
        if digest != expected_hash:
            failures.append(f"{name}: sha256 {digest} != {expected_hash}")
        found[name] = path
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"ARTIFACT_HASHES_VERIFIED ({len(found)} files)")
    return found


def inflate(source: Path, destination: Path) -> None:
    with gzip.open(source, "rb") as compressed, destination.open("wb") as raw:
        shutil.copyfileobj(compressed, raw, length=16 * 1024 * 1024)


def finite_heavy(directory: Path, drat_trim: Path | None) -> None:
    assets = check_assets(directory)
    if drat_trim is None:
        print("Proof replay skipped: pass --drat-trim /path/to/drat-trim.")
        return
    if not drat_trim.is_file():
        raise SystemExit(f"drat-trim executable not found: {drat_trim}")

    stems = [
        "r3_18_budget5_branch_0_twostage",
        "r3_18_budget5_branch_1",
        "r3_18_budget5_branch_2",
        "r3_18_budget6_branch_0_universal_union",
        "r3_18_budget6_branch_1",
        "r3_18_budget6_branch_2",
    ]
    for stem in stems:
        with tempfile.TemporaryDirectory(prefix=f"ramsey-{stem}-") as tmp:
            temporary = Path(tmp)
            cnf = temporary / f"{stem}.cnf"
            drat = temporary / f"{stem}.drat"
            inflate(assets[f"{stem}.cnf.gz"], cnf)
            inflate(assets[f"{stem}.drat.gz"], drat)
            completed = subprocess.run(
                [str(drat_trim), str(cnf), str(drat)],
                cwd=ROOT,
                check=False,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
            )
            print("\n".join(completed.stdout.splitlines()[-25:]))
            if completed.returncode != 0 or "s VERIFIED" not in completed.stdout:
                raise SystemExit(f"DRAT replay failed for {stem}")
            print(f"DRAT_VERIFIED {stem}")
    print("FINITE_HEAVY_REPRODUCTION_PASS")


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="tier", required=True)
    subparsers.add_parser("quick")
    subparsers.add_parser("full")
    heavy = subparsers.add_parser("finite-heavy")
    heavy.add_argument(
        "--artifact-dir",
        type=Path,
        default=ROOT / "artifacts" / "downloads",
    )
    heavy.add_argument("--drat-trim", type=Path)
    args = parser.parse_args()

    if args.tier == "quick":
        quick()
    elif args.tier == "full":
        full()
    else:
        finite_heavy(args.artifact_dir.resolve(), args.drat_trim)


if __name__ == "__main__":
    main()
