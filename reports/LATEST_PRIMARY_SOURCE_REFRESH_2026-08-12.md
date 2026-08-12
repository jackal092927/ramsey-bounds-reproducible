# Latest primary-source refresh

Date: 2026-08-12  
Scope: classical graph Ramsey bounds relevant to the live upper, lower, and
finite-number routes.

## Status

The search found no primary-source two-colour diagonal bound numerically
stronger than the workspace theorem (subsequently strengthened during this
refresh)

$$
R(k,k)\leq
(3.780687577208)^{k+o(k)}.
$$

This is a search finding, not a global novelty, publication-priority,
world-best, or claim that an unindexed result cannot exist.

## Source table

| Source | Version checked | Exact relevant statement | Effect on this workspace |
|---|---|---|---|
| Gupta--Ndiaye--Norin--Wei, arXiv:2407.19026 | v1 | reports $R(k,k)\leq(3.8)^{k+o(k)}$ | published/preprint comparison baseline; the workspace uses a separately repaired chain |
| Bradač, arXiv:2605.28793 | v3, 2026-06-16 | $r(s,k)=\Omega_s(k^{s-1}/(\log k)^{2s-4})$ for fixed $s\geq3$ | current fixed-$s$ lower-bound baseline; the live target is a logarithmic improvement |
| Lin--Niu, arXiv:2605.25843 | v2, 2026-07-02 | positive fixed-$C$ Gaussian exponent gain | comparison source for the audited HMS appendix bridge |
| Nagda--Raghavan--Thakurta, arXiv:2603.09172 | v5, 2026-04-21 | includes $R(3,13)\geq61$ and $R(3,18)\geq100$ among its finite lower-bound improvements | checked public seeds for the live $R(3,13)\geq62$ and $R(3,18)\geq101$ searches |
| Yang--Mao, arXiv:2608.01962 | v1, 2026-08-03 | $R_r(k)\leq\exp[-c k/(r^2\log^4(2r))]r^{rk}$ | newest relevant paper, but it explicitly does not optimize fixed small $r$ and states that GNNW is stronger for $r=2$ |
| Radziszowski, *Small Ramsey Numbers* | DS1.18, 2026-04-24 | includes $61\leq R(3,13)\leq68$, $92\leq R(3,17)\leq109$, $100\leq R(3,18)\leq120$, and $R(4,15)\geq159$ | finite-number baseline; later checked public matrices raise the `R(3,17)` and `R(4,15)` lower bounds to 93 and 160 |

The current remote heads of the two finite-certificate sources also remain the
pinned commits already audited here:

```text
ScaleAutoResearch-Ramsey  6d6d76a44c14321882a8640ed9e86d4f791e31d3
google-research           015539128d9a7dbe14b5f5308a198a15da808949
```

Thus this refresh found no later matrix in those authoritative repositories
that supersedes the pinned finite-certificate audit.

The `R(3,18)>=100` matrix was also reconstructed independently.  A frozen
one-point extension has exactly one triangle and no `I18`; a subsequent
proof-carrying local computation excludes every repair using arbitrary
additions and at most five input-edge deletions.  That fixed-seed statement
does not improve the global lower bound.  At exact budget six, one of the
three triangle-edge branches now has an independently replayed DRAT UNSAT
proof, while the other two remain `UNKNOWN`; the full shell is still open.

## Yang--Mao transfer audit

The new multicolour paper has two ingredients:

1. a positive-coefficient root filter giving a higher-order correlation tail
   with exponent $1/d$;
2. retained preliminary colour spines, followed by a one-coordinate relative-
   entropy estimate.

The second ingredient gives, in the paper's notation,

$$
R(b_1,\ldots,b_r)
\leq r^{rk-s-t}\exp\!\left(-\frac{t^2}{64k}\right).
$$

For fixed $r=2$ the paper's displayed growing-colour theorem does not itself
beat the specialised two-colour rate.  Its ingredients can nevertheless be
transferred: retain the two preliminary spines, use the parameterized book
theorem on the common reservoir, and replace the paper's coarse multinomial
page bound by the frozen exact P6 off-diagonal rate.

That transfer is now closed locally.  A source-level specialization of the
paper's root-filter argument proves
$\mathcal G_2^{(3)}(10^{-6},11.62088)$.  The resulting transfer defines an
explicit two-variable maximum $C_*$ and proves
$R(k,k)\le\exp(C_*k+o(k))$.  The sharpened retained-spine tuple and
weighted-wedge proof give
$C_*\le F_6(1)-2.87\cdot10^{-6}$ and the safe decimal base
`3.780687577208`; the actual base is `3.7806875772072065...`.  The 384-bit
author checks and an independently structured 512-bit reconstruction pass,
and the referee's two local proof-writing requests are resolved.  This is a
local computer-assisted theorem conditional on Yang--Mao v1
regularization/parameterized book, the frozen P6/BookCor package, and Arb
semantics; it is not a claim that the paper states this fixed-colour number.
The earlier weighted-wedge gain `7e-7` and safe base `3.780695781309` remain
as the immediate reviewed predecessor.

## Claim boundary

- **Established by this refresh:** no checked primary source found in the
  searched 2026 window supplies a stronger directly comparable two-colour
  numerical base; Yang--Mao is a growing-colour theorem and explicitly defers
  fixed-$r$ numerical optimisation.
- **Not established:** an explicit finite-$k$ threshold, global parameter
  optimality, global novelty, journal priority, a world-best theorem, or
  impossibility of a stronger retained-spine/GNNW hybrid.
- **Next use:** seek external review and archival of the
  specialized-correlation retained-spine/P6 hybrid.  The present certificate
  proves exponent gain `2.87e-6`; no global tuple optimum is claimed.

## Local proof-package links and checks

- Correlation proof:
  [`SPECIALIZED_CORRELATION_SHARPENING.md`](../routes/upper/SPECIALIZED_CORRELATION_SHARPENING.md)
- Sharpened transfer certificate:
  [`RETAINED_SPINE_SHARPENED_CERTIFICATE.md`](../routes/upper/RETAINED_SPINE_SHARPENED_CERTIFICATE.md)
- Independent resolved review:
  [`INDEPENDENT_RETAINED_SPINE_SHARPENED_REFEREE.md`](../routes/upper/INDEPENDENT_RETAINED_SPINE_SHARPENED_REFEREE.md)
- Claim gate:
  [`SHARPENED_RESULT_TO_CLAIM.md`](../routes/upper/SHARPENED_RESULT_TO_CLAIM.md)

```text
routes/upper/.venv/bin/python routes/upper/check_specialized_correlation.py
routes/upper/.venv/bin/python routes/upper/check_retained_spine_sharpened.py
routes/upper/.venv/bin/python routes/upper/independent_check_retained_spine_sharpened.py
```

## Primary links

- <https://arxiv.org/abs/2407.19026v1>
- <https://arxiv.org/abs/2605.28793v3>
- <https://arxiv.org/abs/2605.25843v2>
- <https://arxiv.org/abs/2603.09172v5>
- <https://arxiv.org/abs/2608.01962v1>
- <https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1>
- <https://github.com/ypwang61/ScaleAutoResearch-Ramsey>
- <https://github.com/google-research/google-research/tree/master/ramsey_number_bounds/improved_bounds>
