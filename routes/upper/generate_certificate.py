#!/usr/bin/env python3
"""Generate a candidate witness for the corrected two-sided Ramsey region.

This is a floating-point *search* program.  It is deliberately separate from
``verify_arb.py``, which is the proof-oriented checker.  The elementary GNNW
first-stage rate with beta=0.08 is frozen as the prior rate.  For each lambda cell we
optimize a constant M and choose Y below both supporting-envelope boundaries.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from scipy.optimize import minimize_scalar


PRIOR_BETA = 0.08
TARGET_BETA = 0.03
LAMBDA_SPLIT = 0.001
REGION_BUFFER = 0.00008


def entropy(z: float) -> float:
    return (1.0 + z) * math.log1p(z) - z * math.log(z)


def prior_rate(mu: float) -> float:
    s = -0.25 * mu + PRIOR_BETA * mu**2 + 0.08 * mu**3
    return entropy(mu) + s * math.exp(-mu)


def target_f(lam: float) -> float:
    s = -0.25 * lam + TARGET_BETA * lam**2 + 0.08 * lam**3
    return entropy(lam) + s * math.exp(-lam)


def target_fp(lam: float) -> float:
    s = -0.25 * lam + TARGET_BETA * lam**2 + 0.08 * lam**3
    sp = -0.25 + 2.0 * TARGET_BETA * lam + 0.24 * lam**2
    return math.log((1.0 + lam) / lam) + (sp - s) * math.exp(-lam)


def region_thresholds(a: float) -> tuple[float, float]:
    """Return the two scalar envelope thresholds for b=-log(Y).

    Both are required.  The first certifies a+mu*b >= U(mu), and the second
    certifies b+mu*a >= U(mu), for every 0 < mu <= 1.
    """

    standard = minimize_scalar(
        lambda mu: -(prior_rate(mu) - a) / mu,
        bounds=(1e-13, 1.0),
        method="bounded",
        options={"xatol": 1e-14},
    )
    swapped = minimize_scalar(
        lambda mu: -(prior_rate(mu) - mu * a),
        bounds=(1e-13, 1.0),
        method="bounded",
        options={"xatol": 1e-14},
    )
    endpoint = prior_rate(1.0) - a
    return max(0.0, -standard.fun, endpoint), max(0.0, -swapped.fun, endpoint)


def witness_at(lam: float) -> tuple[float, float, float]:
    red_density = 1.0 - math.exp(-target_fp(lam))

    def negative_slack(logit_m: float) -> float:
        m = 1.0 / (1.0 + math.exp(-logit_m))
        x = (1.0 - m) * red_density ** (1.0 / (1.0 - m))
        a = -math.log(x)
        b_standard, b_swapped = region_thresholds(a)
        b = max(b_standard, b_swapped) + REGION_BUFFER
        slack = target_f(lam) - 0.5 * (a - lam * math.log(m) + lam * b)
        return -slack

    optimum = minimize_scalar(
        negative_slack,
        bounds=(-15.0, 5.0),
        method="bounded",
        options={"xatol": 1e-12},
    )
    m = 1.0 / (1.0 + math.exp(-optimum.x))
    x = (1.0 - m) * red_density ** (1.0 / (1.0 - m))
    a = -math.log(x)
    b_standard, b_swapped = region_thresholds(a)
    b = max(b_standard, b_swapped) + REGION_BUFFER
    return m, math.exp(-b), -optimum.fun


def generate(cells: int) -> dict:
    segments = []
    predicted_worst = (math.inf, None)
    width = (1.0 - LAMBDA_SPLIT) / cells
    for index in range(cells):
        lo = LAMBDA_SPLIT + index * width
        hi = 1.0 if index + 1 == cells else LAMBDA_SPLIT + (index + 1) * width
        mid = (lo + hi) / 2.0
        m, _, slack = witness_at(mid)
        # X (and hence a=-log X) changes across a cell.  Choose Y against
        # both endpoint a-values; concavity reduces each endpoint condition
        # to a one-dimensional envelope, and the Arb checker covers the full
        # interval dependence.
        endpoint_bs = []
        for lam in (lo, hi):
            red_density = 1.0 - math.exp(-target_fp(lam))
            x = (1.0 - m) * red_density ** (1.0 / (1.0 - m))
            a = -math.log(x)
            endpoint_bs.extend(region_thresholds(a))
        y = math.exp(-(max(endpoint_bs) + REGION_BUFFER))
        if slack < predicted_worst[0]:
            predicted_worst = (slack, mid)
        segments.append(
            {
                "lo": str(LAMBDA_SPLIT) if index == 0 else format(lo, ".17g"),
                "hi": format(hi, ".17g"),
                "M": format(m, ".17g"),
                "Y": format(y, ".17g"),
            }
        )

    return {
        "schema": "corrected-two-sided-ramsey-v1",
        "prior_coefficients": ["-0.25", str(PRIOR_BETA), "0.08"],
        "target_coefficients": ["-0.25", str(TARGET_BETA), "0.08"],
        "lambda_split": str(LAMBDA_SPLIT),
        "small_witness": "M=lambda*exp(-lambda), Y=1-X",
        "region_buffer": str(REGION_BUFFER),
        "predicted_worst_slack": format(predicted_worst[0], ".17g"),
        "predicted_worst_lambda": format(predicted_worst[1], ".17g"),
        "segments": segments,
    }


def main() -> None:
    global PRIOR_BETA, TARGET_BETA, LAMBDA_SPLIT, REGION_BUFFER
    parser = argparse.ArgumentParser()
    parser.add_argument("--cells", type=int, default=32768)
    parser.add_argument("--prior-beta", type=float, default=PRIOR_BETA)
    parser.add_argument("--target-beta", type=float, default=TARGET_BETA)
    parser.add_argument("--lambda-split", type=float, default=LAMBDA_SPLIT)
    parser.add_argument("--region-buffer", type=float, default=REGION_BUFFER)
    parser.add_argument("--output", type=Path, default=Path("certificate.json"))
    args = parser.parse_args()
    PRIOR_BETA = args.prior_beta
    TARGET_BETA = args.target_beta
    if not 0.0 < args.lambda_split < 1.0:
        parser.error("--lambda-split must lie strictly between 0 and 1")
    LAMBDA_SPLIT = args.lambda_split
    REGION_BUFFER = args.region_buffer
    payload = generate(args.cells)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(
        f"wrote {len(payload['segments'])} cells; "
        f"predicted worst slack={payload['predicted_worst_slack']} "
        f"at lambda={payload['predicted_worst_lambda']}"
    )


if __name__ == "__main__":
    main()
