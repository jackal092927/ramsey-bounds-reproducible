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


def verify_chain(paths: list[Path]) -> list[dict]:
    if not paths:
        raise AssertionError("the certificate chain is empty")

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
    parser.add_argument("certificates", nargs="+", type=Path)
    args = parser.parse_args()
    reports = verify_chain(args.certificates)
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
