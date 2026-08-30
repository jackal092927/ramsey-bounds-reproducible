#!/usr/bin/env python3
"""Verify a finite chain of corrected Ramsey-rate descent certificates.

The first certificate must prove its prior with the elementary witness.  Each
later certificate may use the immediately preceding target rate as its prior.
Exact decimal coefficient equality is checked at every link, so an unproved
intermediate rate cannot silently enter the chain.

This script reuses the audited Arb primitives in ``verify_arb.py``.  The
separately written ``verify_region_direct_arb.py`` remains the independent
replay of each stage's two Ramsey-region inequalities.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from decimal import Decimal
from pathlib import Path

from verify_arb import (
    ONE,
    certify_elementary_prior,
    parse,
    prove_prior_concavity,
    prove_small_regime,
    rate,
    verify_segments,
)


PAPER_CHAIN: tuple[tuple[str, str], ...] = (
    ("certificate-higher-order-quintic-v1.json", "2664bc421cd0cb7489289caa283a3a3f22830580f7c21bf0e6cbe092910bc277"),
    ("certificate-higher-order-quintic-chain-v2.json", "b5b595b4dcc9d1bdc2b5714f68fef99ec1c566bbd612d35ca19100d173d41c4d"),
    ("certificate-higher-order-sextic-chain-v3.json", "2052952c3af98074d5442fb736c7a2952146e92051a43fab84e75f099d9e00d7"),
    ("certificate-higher-order-octic-chain-v4.json", "09253d757516dc258396f82c09a442aaaf9d499640c1cc99b5767e6d51d35942"),
    ("certificate-higher-order-decic-chain-v5.json", "4ec4dbbe190a08134efe68c3a76ce4b4fb3aabdad230af703c19a28a03ecf9a9"),
    ("certificate-higher-order-tetradecic-chain-v6.json", "8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8"),
)

PAPER_P6_TARGET: tuple[Decimal, ...] = tuple(
    Decimal(value)
    for value in (
        "-0.250000000000000",
        "0.019891840059418",
        "-0.012275954247190",
        "0.144110816398083",
        "0.006277913420654",
        "-0.066101623491668",
        "-0.002287675993602",
        "-0.058238059505066",
        "0.030675864198693",
        "0.052472201910597",
        "0.043300454861853",
        "-0.042529975074653",
        "-0.055263639426635",
        "0.036695886931268",
    )
)


def exact_coefficients(values: list[object]) -> tuple[Decimal, ...]:
    return tuple(Decimal(str(value)) for value in values)


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_certificate(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema") != "corrected-two-sided-ramsey-v1":
        raise AssertionError(f"{path}: unexpected certificate schema")
    if not payload.get("segments"):
        raise AssertionError(f"{path}: empty segment list")
    return payload


def verify_paper_chain_identity(paths: list[Path]) -> None:
    """Lock the canonical manuscript replay to its six named immutable files."""

    received_names = tuple(path.name for path in paths)
    expected_names = tuple(name for name, _ in PAPER_CHAIN)
    if received_names != expected_names:
        raise AssertionError(
            f"paper chain names/order {received_names} != {expected_names}"
        )
    for path, (_, expected_hash) in zip(paths, PAPER_CHAIN, strict=True):
        actual_hash = file_hash(path)
        if actual_hash != expected_hash:
            raise AssertionError(
                f"paper chain hash mismatch for {path}: {actual_hash} != {expected_hash}"
            )
    final_payload = load_certificate(paths[-1])
    final_target = exact_coefficients(final_payload["target_coefficients"])
    if final_target != PAPER_P6_TARGET:
        raise AssertionError(
            f"paper P6 tuple {final_target} != displayed tuple {PAPER_P6_TARGET}"
        )


def verify_chain(paths: list[Path], *, require_paper_chain: bool = False) -> list[dict]:
    if not paths:
        raise AssertionError("the certificate chain is empty")
    if require_paper_chain:
        verify_paper_chain_identity(paths)

    reports: list[dict] = []
    previous_target: tuple[Decimal, ...] | None = None
    for stage, path in enumerate(paths):
        payload = load_certificate(path)
        prior_exact = exact_coefficients(payload["prior_coefficients"])
        target_exact = exact_coefficients(payload["target_coefficients"])
        if previous_target is not None and prior_exact != previous_target:
            raise AssertionError(
                f"stage {stage}: prior {prior_exact} does not exactly equal "
                f"the preceding target {previous_target}"
            )

        prior = [parse(value) for value in payload["prior_coefficients"]]
        target = [parse(value) for value in payload["target_coefficients"]]
        split = parse(payload["lambda_split"])
        concavity, correction = prove_prior_concavity(prior)

        elementary = None
        if stage == 0:
            prior_small, prior_large = certify_elementary_prior(prior, split)
            elementary = {
                "small_slack_over_lambda": str(prior_small),
                "large_slack": prior_large,
            }

        target_small = prove_small_regime(target, split)
        large = verify_segments(payload, target, prior, split)
        f_one = rate(ONE, target)
        report = {
            "stage": stage,
            "path": str(path),
            "sha256": file_hash(path),
            "prior_coefficients": [str(value) for value in prior_exact],
            "target_coefficients": [str(value) for value in target_exact],
            "prior_concavity_upper": concavity,
            "prior_small_correction_upper": correction,
            "elementary_prior": elementary,
            "target_small_slack_over_lambda": str(target_small),
            **large,
            "F_one": str(f_one),
            "growth_base": str(f_one.exp()),
        }
        reports.append(report)
        previous_target = target_exact

    return reports


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--require-paper-chain",
        action="store_true",
        help="enforce the manuscript's six filenames, SHA-256 values, and P6 tuple",
    )
    parser.add_argument("certificates", nargs="+", type=Path)
    args = parser.parse_args()
    reports = verify_chain(
        args.certificates, require_paper_chain=args.require_paper_chain
    )
    print(f"PASS: verified {len(reports)}-stage Ramsey-rate certificate chain")
    for report in reports:
        print(f"stage {report['stage']}: {report['path']}")
        print(f"  sha256: {report['sha256']}")
        print(f"  prior -> target: {report['prior_coefficients']} -> {report['target_coefficients']}")
        print(f"  target small slack/lambda: {report['target_small_slack_over_lambda']}")
        print(f"  standard region: {report['worst_standard_region_margin']}")
        print(f"  swapped region: {report['worst_swapped_region_margin']}")
        print(f"  large main: {report['worst_large_main_slack']}")
        print(f"  growth base: {report['growth_base']}")


if __name__ == "__main__":
    main()
