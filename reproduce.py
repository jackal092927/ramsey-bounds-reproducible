#!/usr/bin/env python3
"""Tiered, non-destructive reproduction entry point."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
UPPER = ROOT / "routes" / "upper"
FINITE = ROOT / "routes" / "finite"
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
    run([sys.executable, "scripts/test_materialize_unified_paper.py"])
    run(["bash", "scripts/reproduce_upper.sh"])
    run([sys.executable, "routes/lower/history_weight_optimization_next_check.py"])
    run(["bash", "scripts/reproduce_finite_light.sh"])
    print("\nQUICK_REPRODUCTION_PASS")


def full() -> None:
    quick()
    chain_paths = [str(UPPER / name) for name in CHAIN]
    run(
        [
            sys.executable,
            "verify_chain_arb.py",
            "--require-paper-chain",
            *chain_paths,
        ],
        cwd=UPPER,
    )
    for path in chain_paths:
        run([sys.executable, "verify_region_direct_arb.py", path], cwd=UPPER)
    run([sys.executable, "audit_tests.py"], cwd=UPPER)
    run(["bash", "scripts/reproduce_lower.sh"])
    print("\nFULL_REPRODUCTION_PASS")


def sources() -> None:
    """Networked identity check for version-pinned external inputs."""

    run([sys.executable, "scripts/fetch_external_sources.py"])
    with tempfile.TemporaryDirectory(prefix="ramsey-source-graphs-") as tmp:
        run(
            [
                sys.executable,
                "routes/finite/fetch_certificates.py",
                "--output-dir",
                tmp,
            ]
        )
    print("\nEXTERNAL_SOURCE_IDENTITIES_VERIFIED")


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


def build_finite_overlay(assets: dict[str, Path], destination: Path) -> None:
    """Link release assets and tracked semantic metadata into one audit tree."""

    (destination / "certificates").symlink_to(
        FINITE / "certificates", target_is_directory=True
    )
    for metadata in sorted(FINITE.glob("*.json")):
        (destination / metadata.name).symlink_to(metadata)
    for metadata_name in ("INDEPENDENT_R3_18_BUDGET6_COMPLETE_REFEREE.md",):
        metadata = FINITE / metadata_name
        (destination / metadata.name).symlink_to(metadata)
    for name, asset in assets.items():
        (destination / name).symlink_to(asset)


def finite_heavy(directory: Path, drat_trim: Path | None) -> None:
    assets = check_assets(directory)
    if drat_trim is None:
        raise SystemExit("pass --drat-trim /path/to/the/pinned/drat-trim")
    if not drat_trim.is_file() or not os.access(drat_trim, os.X_OK):
        raise SystemExit(f"drat-trim executable not found: {drat_trim}")
    checker_hash = sha256(drat_trim)
    print(f"DRAT_TRIM_EXECUTABLE_SHA256 {checker_hash}")

    drat_auditors = [
        "check_r3_18_extension_repair.py",
        "check_r3_18_budget6_branch0_union.py",
        "check_r3_18_budget6_branch1.py",
        "check_r3_18_budget6.py",
    ]
    with tempfile.TemporaryDirectory(prefix="ramsey-finite-heavy-") as tmp:
        overlay = Path(tmp)
        build_finite_overlay(assets, overlay)
        # The independent counter-schema audit reads the authenticated CNFs
        # but deliberately has no dependency on the DRAT checker.  Keep its
        # command-line contract separate from the proof-replay auditors.
        run(
            [
                sys.executable,
                str(FINITE / "check_r3_18_seqcounter.py"),
                "--artifact-dir",
                str(overlay),
            ]
        )
        for auditor in drat_auditors:
            run(
                [
                    sys.executable,
                    str(FINITE / auditor),
                    "--artifact-dir",
                    str(overlay),
                    "--drat-trim",
                    str(drat_trim),
                    "--drat-seconds",
                    "1800",
                ]
            )
        run([sys.executable, str(FINITE / "check_r3_18_budget7.py"), str(overlay)])
    summary = {
        "schema": "ramsey-finite-heavy-current-run-v1",
        "status": "FINITE_THEOREM_REPRODUCED",
        "current_run": {
            "budget5_formula_semantics": ["VERIFIED"] * 3,
            "budget5_drat_replays": ["VERIFIED"] * 3,
            "exact6_formula_semantics": ["VERIFIED"] * 3,
            "exact6_drat_replays": ["VERIFIED"] * 3,
            "exact7_record_state": "ALL_THREE_UNKNOWN_VERIFIED",
            "fixed_seed_deletion_repair_radius_at_least_7": True,
        },
        "checker_executable_sha256": checker_hash,
        "global_R_3_18_improvement": False,
        "exact7_repair_exists": None,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    print("FINITE_HEAVY_REPRODUCTION_PASS")


def main() -> None:
    if not __debug__:
        raise SystemExit(
            "refusing optimized Python: proof-critical assertions must remain enabled"
        )
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="tier", required=True)
    subparsers.add_parser("quick")
    subparsers.add_parser("full")
    subparsers.add_parser("sources")
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
    elif args.tier == "sources":
        sources()
    else:
        checker = args.drat_trim.resolve() if args.drat_trim is not None else None
        finite_heavy(args.artifact_dir.resolve(), checker)


if __name__ == "__main__":
    main()
