# Joint correlation / retained-spine search log

Date: 2026-08-12

## Pre-registered decision rule

Promote a new theorem-linked candidate only if both conditions hold:

1. the rigorous safe base is strictly below `3.7806870`; and
2. every proof-critical positive margin explicitly designated in the final
   checker is at least $10^{-9}$.

Otherwise retain only a numerical frontier or an obstruction report.

## Source-level change

The frozen specialized separator used the analytic root-filter envelope on
the whole half-line beginning at $u_0=2.9$.  The new route separates the
domain:

- exact root filters plus a cellwise derivative proof on
  $[619/250,29/10]$;
- the monotone analytic envelope only on $[29/10,\infty)$.

This permits $u_0=619/250$, changing the growth constant from
$C=11.62088$ to $C=9.9247984$.  The exact generalized separator pair is

$$
(\beta,C)=\left(\frac1{4000000},\frac{6202999}{625000}\right).
$$

The proof is in `HYBRID_CORRELATION_SHARPENING.md`; it is not inferred from
the exploratory optimizer.

## Joint exploration

`search_joint_correlation_spine.py` records the initial whole-tail-envelope
search.  `search_joint_hybrid_correlation_spine.py` records the later hybrid
search.  Both scripts use double precision and are explicitly heuristic.
They served only to locate rational candidates for Arb replay.

The final clean tuple is

$$
(\eta,p,\delta,\lambda_0,\tau)
=(0.028688,0.471310,0.0000525,13580,0.000665).
$$

## Frozen exponent-gap decision

For the same clean tuple, the author Arb formulas were mechanically replayed
at nearby simple gaps.  The red-page margin is the binding proof-critical
margin.

| $\Delta$ | red-page lower margin | decision |
|---:|---:|---|
| $3.350\cdot10^{-6}$ | $2.2047\cdot10^{-8}$ | feasible but weaker |
| $3.355\cdot10^{-6}$ | $1.2044\cdot10^{-8}$ | **frozen** |
| $3.359\cdot10^{-6}$ | $4.0430\cdot10^{-9}$ | feasible but less robust |
| $3.360\cdot10^{-6}$ | $2.0426\cdot10^{-9}$ | too close to the gate for promotion |

The frozen choice $\Delta=3.355\cdot10^{-6}$ is the strongest tested simple
decimal retaining more than an order of magnitude of slack over the
$10^{-9}$ threshold in the binding page inequality.  No global optimality
claim is attached to this choice.

## Frozen result and margins

The 384-bit author checker and 512-bit separate implementation both obtain

$$
\exp(U(1)-\Delta)
=3.7806857435741762369\ldots
<3.780685745<3.7806870.
$$

The final proof-critical positive margins are:

| check | rigorous lower margin |
|---|---:|
| retained minimum-degree slack | $1.3300\cdot10^{-9}$ |
| red page | $1.2044\cdot10^{-8}$ |
| blue page | $3.3687\cdot10^{-6}$ |
| reservoir | $7.8016\cdot10^{-4}$ |
| decimal rounding | $1.4258\cdot10^{-9}$ |

Thus the pre-registered promotion gate passes.  Independent mathematical
referee review remains a separate requirement before canonical replacement.

