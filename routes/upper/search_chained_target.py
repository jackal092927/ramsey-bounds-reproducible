#!/usr/bin/env python3
"""Search for a next polynomial in an already certified descent chain.

This program is deliberately only a floating-point constructor.  It solves a
sequence of trust-region linear programs for the polynomial coefficients,
while re-optimising the book witness at a fixed lambda mesh after every step.
Any output must still be passed through ``generate_higher_order_certificate``
and both Arb verifiers before it has mathematical status.
"""

from __future__ import annotations

import argparse
import math

import numpy as np
from scipy.optimize import linprog

from generate_higher_order_certificate import (
    PriorEnvelopeTable,
    rate,
    rate_prime,
    witness_at,
)


def coefficients(text: str) -> np.ndarray:
    result = np.array([float(item.strip()) for item in text.split(",")])
    if result.size == 0 or not np.all(np.isfinite(result)):
        raise argparse.ArgumentTypeError("invalid coefficient tuple")
    return result


def lambda_mesh(split: float, count: int) -> np.ndarray:
    geometric = np.geomspace(split, 0.1, max(24, count // 3))
    linear = np.linspace(0.1, 1.0, max(48, count))
    return np.unique(np.concatenate((geometric, linear)))


def best_slacks(
    target: np.ndarray,
    mesh: np.ndarray,
    envelope: PriorEnvelopeTable,
) -> np.ndarray:
    return np.array(
        [witness_at(float(lam), target, envelope, 0.0)[2] for lam in mesh]
    )


def rate_basis(mesh: np.ndarray, degree: int) -> tuple[np.ndarray, np.ndarray]:
    """Coefficient derivatives of F and F' on the mesh."""
    indices = np.arange(1, degree + 1)
    powers = mesh[:, None] ** indices[None, :]
    exponential = np.exp(-mesh)[:, None]
    f_basis = powers * exponential
    fp_basis = (
        indices[None, :] * mesh[:, None] ** (indices[None, :] - 1) - powers
    ) * exponential
    return f_basis, fp_basis


def search(
    prior: np.ndarray,
    degree: int,
    split: float,
    count: int,
    margin: float,
    iterations: int,
    initial_trust: float,
    initial: np.ndarray | None = None,
) -> np.ndarray:
    if degree < prior.size:
        raise ValueError("target degree cannot be below prior degree")
    if initial is None:
        target = np.pad(prior, (0, degree - prior.size))
    else:
        if initial.size != degree:
            raise ValueError("initial target length must equal --degree")
        if initial[0] != prior[0]:
            raise ValueError(
                "initial target must preserve the prior linear coefficient"
            )
        target = initial.copy()
    envelope = PriorEnvelopeTable(prior)
    mesh = lambda_mesh(split, count)
    f_basis, fp_basis = rate_basis(mesh, degree)
    trust = initial_trust
    # HiGHS' default primal feasibility tolerance is large compared with the
    # 1e-4 construction slacks used here.  Ask the LP for a slightly stronger
    # inequality than the user-facing floor and solve it to tighter tolerance;
    # the nonlinear replay below still accepts only against ``margin`` itself.
    lp_margin = margin + 2e-7

    for iteration in range(iterations):
        slack = best_slacks(target, mesh, envelope)
        step = 2e-6
        jacobian = np.empty((mesh.size, degree))
        # The universal linear coefficient is frozen.  We nevertheless retain
        # a zero first column so the LP bookkeeping stays transparent.
        jacobian[:, 0] = 0.0
        for index in range(1, degree):
            perturbed = target.copy()
            perturbed[index] += step
            jacobian[:, index] = (
                best_slacks(perturbed, mesh, envelope) - slack
            ) / step

        current_f = rate(mesh, target)
        current_fp = rate_prime(mesh, target)
        # J delta >= margin-slack, and preserve comfortable F,F' positivity.
        a_ub = np.vstack((-jacobian, -f_basis, -fp_basis))
        b_ub = np.concatenate(
            (
                slack - lp_margin,
                current_f - 1e-5,
                current_fp - 1e-5,
            )
        )
        bounds = [(0.0, 0.0)] + [(-trust, trust)] * (degree - 1)
        result = linprog(
            np.ones(degree),
            A_ub=a_ub,
            b_ub=b_ub,
            bounds=bounds,
            method="highs",
            options={
                "primal_feasibility_tolerance": 1e-9,
                "dual_feasibility_tolerance": 1e-9,
            },
        )
        if not result.success:
            trust *= 0.5
            print(f"iteration {iteration}: LP failed; trust -> {trust:.3g}")
            continue

        accepted = False
        scale = 1.0
        while scale >= 1 / 128:
            proposal = target + scale * result.x
            proposal[0] = prior[0]
            proposal_slack = best_slacks(proposal, mesh, envelope)
            if float(proposal_slack.min()) >= margin:
                target = proposal
                accepted = True
                break
            scale *= 0.5
        current_slack = best_slacks(target, mesh, envelope)
        base = math.exp(float(rate(1.0, target)))
        print(
            f"iteration {iteration}: accepted={accepted} scale={scale:.5g} "
            f"min_slack={current_slack.min():.9g} "
            f"lambda={mesh[current_slack.argmin()]:.9g} base={base:.15g}"
        )
        print("  " + ",".join(f"{value:.15f}" for value in target))
        if not accepted:
            trust *= 0.5
        else:
            trust = min(initial_trust, trust * 1.15)

    return target


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prior-coefficients", type=coefficients, required=True)
    parser.add_argument("--degree", type=int, default=6)
    parser.add_argument("--lambda-split", type=float, default=0.005)
    parser.add_argument("--mesh-count", type=int, default=180)
    parser.add_argument("--margin", type=float, default=0.00025)
    parser.add_argument("--iterations", type=int, default=8)
    parser.add_argument("--trust", type=float, default=0.01)
    parser.add_argument(
        "--initial-coefficients",
        type=coefficients,
        help="optional warm-start target (exactly --degree entries)",
    )
    args = parser.parse_args()
    target = search(
        args.prior_coefficients,
        args.degree,
        args.lambda_split,
        args.mesh_count,
        args.margin,
        args.iterations,
        args.trust,
        args.initial_coefficients,
    )
    print("final coefficients:")
    print(",".join(f"{value:.15f}" for value in target))


if __name__ == "__main__":
    main()
