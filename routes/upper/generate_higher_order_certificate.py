#!/usr/bin/env python3
"""Generate floating-point witnesses for an arbitrary target polynomial.

This is a search/certificate-construction program, not a proof checker.  The
proof inputs are the emitted exact-decimal coefficients and piecewise-constant
``M,Y`` witnesses; ``verify_arb.py`` and ``verify_region_direct_arb.py`` replay
them independently with Arb arithmetic.

By default the prior is frozen to the already proved elementary rate

    U(lambda) = H(lambda) + (-.25 lambda + .08 lambda^2 + .08 lambda^3)e^-lambda.

For a chained descent, ``--prior-coefficients`` may instead name the exact
target coefficients of an already verified preceding certificate.  The chain
verifier rejects any decimal mismatch.  Both polynomials may have arbitrary
degree.  A dense monotone table
for the two prior envelopes makes construction fast.  Its interpolation is not
trusted: a positive region buffer is added, and the Arb checkers recompute the
continuous envelope from scratch.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import minimize_scalar


PRIOR_COEFFICIENTS_TEXT = ["-0.25", "0.08", "0.08"]
PRIOR_COEFFICIENTS = np.array([float(x) for x in PRIOR_COEFFICIENTS_TEXT])


def parse_coefficients(text: str) -> tuple[list[str], np.ndarray]:
    values = [item.strip() for item in text.split(",")]
    if not values or any(not item for item in values):
        raise argparse.ArgumentTypeError("coefficients must be a comma-separated list")
    try:
        floats = np.array([float(item) for item in values], dtype=float)
    except ValueError as error:
        raise argparse.ArgumentTypeError(str(error)) from error
    if not np.all(np.isfinite(floats)):
        raise argparse.ArgumentTypeError("coefficients must be finite")
    return values, floats


def entropy(z: float | np.ndarray) -> float | np.ndarray:
    return (1.0 + z) * np.log1p(z) - z * np.log(z)


def polynomial(z: float | np.ndarray, coefficients: np.ndarray) -> float | np.ndarray:
    result = np.zeros_like(z, dtype=float) if isinstance(z, np.ndarray) else 0.0
    power = z
    for coefficient in coefficients:
        result = result + coefficient * power
        power = power * z
    return result


def polynomial_prime(
    z: float | np.ndarray, coefficients: np.ndarray
) -> float | np.ndarray:
    result = np.zeros_like(z, dtype=float) if isinstance(z, np.ndarray) else 0.0
    power = np.ones_like(z, dtype=float) if isinstance(z, np.ndarray) else 1.0
    for degree, coefficient in enumerate(coefficients, start=1):
        result = result + degree * coefficient * power
        power = power * z
    return result


def rate(z: float | np.ndarray, coefficients: np.ndarray) -> float | np.ndarray:
    return entropy(z) + polynomial(z, coefficients) * np.exp(-z)


def rate_prime(
    z: float | np.ndarray, coefficients: np.ndarray
) -> float | np.ndarray:
    p = polynomial(z, coefficients)
    pp = polynomial_prime(z, coefficients)
    return np.log((1.0 + z) / z) + (pp - p) * np.exp(-z)


class PriorEnvelopeTable:
    """Fast interpolation of the two exact concave-prior envelopes.

    Concavity gives the standard critical equation
    ``A(mu)=U(mu)-mu U'(mu)=a`` and the swapped critical equation
    ``U'(mu)=a``.  Linear interpolation on a dense monotone grid is used only
    to propose witnesses.  The rigorous verifier does not import this class.
    """

    def __init__(
        self,
        coefficients: np.ndarray = PRIOR_COEFFICIENTS,
        points: int = 200_001,
    ) -> None:
        self.coefficients = np.array(coefficients, dtype=float)
        self.mu = np.linspace(1e-12, 1.0, points)
        self.u = rate(self.mu, self.coefficients)
        self.up = rate_prime(self.mu, self.coefficients)
        self.a = self.u - self.mu * self.up
        self.u1 = float(self.u[-1])
        self.a1 = float(self.a[-1])
        self.up1 = float(self.up[-1])
        if not np.all(np.diff(self.a) > 0.0):
            raise AssertionError("prior A table is not strictly increasing")
        if not np.all(np.diff(self.up) < 0.0):
            raise AssertionError("prior U' table is not strictly decreasing")

    def thresholds(self, a: float) -> tuple[float, float]:
        endpoint = self.u1 - a
        standard = max(0.0, endpoint)
        if a <= self.a1:
            mu = float(np.interp(a, self.a, self.mu))
            standard = max(
                standard, float(rate_prime(mu, self.coefficients))
            )

        swapped = max(0.0, endpoint)
        if a >= self.up1:
            # np.interp requires increasing abscissae.
            mu = float(np.interp(a, self.up[::-1], self.mu[::-1]))
            swapped = max(
                swapped, float(rate(mu, self.coefficients) - mu * a)
            )
        return standard, swapped


def witness_at(
    lam: float,
    target: np.ndarray,
    envelope: PriorEnvelopeTable,
    region_buffer: float,
) -> tuple[float, float, float]:
    f = float(rate(lam, target))
    fp = float(rate_prime(lam, target))
    if not f > 0.0 or not fp > 0.0:
        raise ValueError(f"target F/F' is nonpositive at lambda={lam}")
    red_density = 1.0 - math.exp(-fp)
    if not 0.0 < red_density < 1.0:
        raise ValueError(f"invalid red density at lambda={lam}")

    def negative_slack(logit_m: float) -> float:
        m = 1.0 / (1.0 + math.exp(-logit_m))
        x = (1.0 - m) * red_density ** (1.0 / (1.0 - m))
        a = -math.log(x)
        b = max(envelope.thresholds(a)) + region_buffer
        return -(f - 0.5 * (a - lam * math.log(m) + lam * b))

    optimum = minimize_scalar(
        negative_slack,
        bounds=(-15.0, 5.0),
        method="bounded",
        options={"xatol": 1e-12},
    )
    m = 1.0 / (1.0 + math.exp(-float(optimum.x)))
    x = (1.0 - m) * red_density ** (1.0 / (1.0 - m))
    a = -math.log(x)
    b = max(envelope.thresholds(a)) + region_buffer
    return m, math.exp(-b), -float(optimum.fun)


def generate(
    prior_text: list[str],
    prior: np.ndarray,
    target_text: list[str],
    target: np.ndarray,
    cells: int,
    lambda_split: float,
    region_buffer: float,
) -> dict:
    envelope = PriorEnvelopeTable(prior)
    segments: list[dict[str, str]] = []
    predicted_worst = (math.inf, math.nan)
    width = (1.0 - lambda_split) / cells

    for index in range(cells):
        lo = lambda_split + index * width
        hi = 1.0 if index + 1 == cells else lambda_split + (index + 1) * width
        mid = 0.5 * (lo + hi)
        m, _, slack = witness_at(mid, target, envelope, region_buffer)

        endpoint_bs: list[float] = []
        for lam in (lo, hi):
            fp = float(rate_prime(lam, target))
            red_density = 1.0 - math.exp(-fp)
            x = (1.0 - m) * red_density ** (1.0 / (1.0 - m))
            a = -math.log(x)
            endpoint_bs.extend(envelope.thresholds(a))
        y = math.exp(-(max(endpoint_bs) + region_buffer))

        if slack < predicted_worst[0]:
            predicted_worst = (slack, mid)
        segments.append(
            {
                "lo": format(lambda_split, ".17g") if index == 0 else format(lo, ".17g"),
                "hi": format(hi, ".17g"),
                "M": format(m, ".17g"),
                "Y": format(y, ".17g"),
            }
        )

    return {
        "schema": "corrected-two-sided-ramsey-v1",
        "prior_coefficients": prior_text,
        "target_coefficients": target_text,
        "lambda_split": format(lambda_split, ".17g"),
        "small_witness": "M=lambda*exp(-lambda), Y=1-X",
        "region_buffer": format(region_buffer, ".17g"),
        "predicted_worst_slack": format(predicted_worst[0], ".17g"),
        "predicted_worst_lambda": format(predicted_worst[1], ".17g"),
        "construction_note": (
            "Higher-order floating search; dense interpolated prior envelopes are "
            "not trusted and are replayed continuously by two Arb verifiers."
        ),
        "segments": segments,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--prior-coefficients",
        default=",".join(PRIOR_COEFFICIENTS_TEXT),
        help="exact-decimal proved prior; defaults to the elementary safe prior",
    )
    parser.add_argument("--target-coefficients", required=True)
    parser.add_argument("--cells", type=int, default=65_536)
    parser.add_argument("--lambda-split", type=float, default=0.005)
    parser.add_argument("--region-buffer", type=float, default=0.00012)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    prior_text, prior = parse_coefficients(args.prior_coefficients)
    target_text, target = parse_coefficients(args.target_coefficients)
    if len(target) < 4:
        parser.error("higher-order search requires at least a quartic target")
    if args.cells <= 0:
        parser.error("--cells must be positive")
    if not 0.0 < args.lambda_split < 1.0:
        parser.error("--lambda-split must lie strictly between 0 and 1")
    if not args.region_buffer > 0.0:
        parser.error("--region-buffer must be positive")

    payload = generate(
        prior_text,
        prior,
        target_text,
        target,
        args.cells,
        args.lambda_split,
        args.region_buffer,
    )
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    f1 = float(rate(1.0, target))
    print(f"wrote {len(payload['segments'])} cells")
    print(f"predicted worst slack: {payload['predicted_worst_slack']}")
    print(f"predicted worst lambda: {payload['predicted_worst_lambda']}")
    print(f"F(1): {f1:.17g}")
    print(f"exp(F(1)): {math.exp(f1):.17g}")


if __name__ == "__main__":
    main()
