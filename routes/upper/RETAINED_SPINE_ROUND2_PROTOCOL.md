# Retained-spine round-2 optimization protocol

Date frozen: 2026-08-12, before the round-2 numerical search

## Objective

Starting from the already certified exponent gain

$$
\Delta_1=7\cdot10^{-7},
$$

search the five exact parameters

$$
(\eta,p,\delta,\lambda_0,\tau)
$$

for a larger **rigorously certified** retained-spine gain.  The frozen
Yang--Mao gates, the frozen $P_6$ rate, and the full $[0,1]^2$ variational
domain are unchanged.  Sampled optimization alone is not an accepted result.

## Pre-registered acceptance rule

A round-2 candidate is accepted only if all of the following hold.

1. The candidate consists of one tuple of exact terminating decimals and one
   exact terminating-decimal target $\Delta_2$.
2. The target satisfies
   $$
   \Delta_2\ge 10^{-6}.
   $$
3. A fresh Arb checker verifies every Yang--Mao scalar gate, re-proves strict
   concavity of the frozen $P_6$ rate, and covers the complete square
   $[0,1]^2$ by symmetry, the direct tangent branch, and the weighted wedge.
4. Every proof-critical strict inequality in the weighted-wedge reduction
   has an outward-rounded margin at least $10^{-9}$.  This includes the
   red-page endpoint margin, red-page boundary derivative, blue-page
   monotonicity/diagonal derivative, reservoir margin, and the decimal base
   rounding margin.  Source gates that are exact sign/range conditions are
   reported separately and must be strict where the theorem requires it.
5. The checker pins all frozen upstream inputs by SHA-256 and runs under the
   reviewed `python-flint==0.9.0` environment at at least 384-bit precision.
6. The proof package states only the certified fixed-tuple theorem.  It does
   not infer global five-parameter optimality from the search.

The old optimized certificate and its checkers are immutable inputs to this
round.  Independent referee replay is a later promotion gate and is not
performed by the author checker.

## Failure verdict

If no accepted tuple is found, the round reports a bounded search frontier,
the searched parameter box, and the active obstruction.  It does not turn a
finite numerical failure into a global impossibility claim.
