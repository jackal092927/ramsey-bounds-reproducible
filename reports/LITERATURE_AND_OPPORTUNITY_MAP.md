# Ramsey bounds: literature and opportunity map

Snapshot date: 2026-08-12. Scope: classical two-colour graph Ramsey numbers.

## Evidence labels

- **PREPRINT-THEOREM:** theorem stated in the latest primary-source preprint;
- **INDEPENDENT-CERT:** a finite graph matrix reconstructed by a checker not
  taken from its producer;
- **COMPUTER-ASSISTED THEOREM:** the analytic inequalities pass rigorous
  interval arithmetic and the repaired implication has independent proof
  replays; external human review/publication may still be pending;
- **AUDIT GAP:** a cited proof step does not currently imply the claimed next
  step;
- **OPEN:** a proposed mechanism with an unproved lemma.

## Diagonal asymptotics

The classical lower bound remains exponential only at the square-root scale,
whereas the upper bound has base below four.  Campos--Griffiths--Morris--
Sahasrabudhe obtained the first exponential improvement over the
Erdos--Szekeres upper-bound base.  Gupta--Ndiaye--Norin--Wei (GNNW) then
optimized that framework and report a numerical base approximately `3.7992`
in arXiv:2407.19026v1.

Two audits change the usable baseline:

1. GNNW Lemma 14 reverses a comparison in its proof.  The corrected envelope
   makes the first positive-`alpha` update fail at `lambda=1`, so the displayed
   chain to `beta=.03` is a **PREPRINT-CLAIM / AUDIT GAP** rather than a safe
   prior for further optimization.
2. HorizonMath's public Ramsey validator accepts either of two one-sided rate
   conditions.  The definition cited by the proof needs both ordered-pair
   conditions.  A strict union-pass/intersection-fail point is reproduced in
   this workspace, so Horizon's `3.6961` and the local `3.69588` variant are
   withdrawn as theorem-linked candidates.

The repaired route begins from GNNW's elementary `beta=.08` rate, proves that
rate directly with the elementary region `Y=1-X`, and then applies the
corrected two-sided envelope.  The first robust cubic output was

\[
R(k,k)\le(3.7990629773286618741\ldots)^{k+o(k)}.
\]

The frozen higher-order exact-linked descent first strengthens this to

\[
R(k,k)\le(3.7806984277961236988\ldots)^{k+o(k)}.
\]

It is a **LOCAL COMPUTER-ASSISTED THEOREM within this proof package**: the
first three 256-bit stages use 65,536 cells each and stages four through six use
131,072;
both region orientations, an analytic proof on all `0<lambda<=.005`, exact
coefficient links, and a separately written direct-slack Arb replay pass.  The
new tetradecic stage has rigorous main margin `4.81847e-5` and standard direct
margin `1.06281e-6`.  An independent adversarial referee reran the complete
six-stage chain and separately structured direct checker and found no
sixth-stage gap.
The formerly imported GNNW Lemma 11/Theorem 12 core is now proved locally in
`LEMMA11_STANDALONE_PROOF.md`; an independent adversarial referee checked the
discrete-convexity extraction, both induction branches, strict contradiction,
and balanced rounding.  External human review is still appropriate, and the
remaining machine trust boundary includes Arb semantics.
The safe `beta=.03` reconstruction gives `3.799202739615937...` as a positive
control.

A subsequent hybrid with Yang--Mao's retained preliminary spines and book
theorem gives the current recommendation

\[
R(k,k)\le(3.780687577208)^{k+o(k)}.
\]

A source-level specialization of Yang--Mao's root-filter argument first proves
$\mathcal G_2^{(3)}(10^{-6},11.62088)$.  The exact outer transfer is a
two-variable maximum $C_*$ built from that correlation input and the frozen
off-diagonal P6 rate.  The sharpened weighted-wedge certificate proves
$C_*\le F_6(1)-2.87\cdot10^{-6}$, with actual base
`3.7806875772072065...`.  The source and full-square author enclosures pass at
384 bits; an independently structured 512-bit Arb checker reconstructs the
root-filter envelopes, generalized separator/tail proof, P6 concavity,
complete wedge boundary reductions, and decimal upward rounding.  The
referee's two proof-writing requests were resolved and the dedicated
result-to-claim gate passes.  This is an **INDEPENDENTLY REVIEWED LOCAL
COMPUTER-ASSISTED THEOREM**, conditional on Yang--Mao v1
regularization/parameterized book, frozen P6/BookCor, and Arb semantics.  It
still lacks an explicit finite-$k$ threshold, external publication review, a
global parameter optimum, global novelty or publication priority, and a
world-best verification.  The earlier exponent-gain-`7e-7` result with safe
base `3.780695781309` remains the immediate reviewed predecessor.
The current proof note, certificate, independent referee, and claim gate are
[`SPECIALIZED_CORRELATION_SHARPENING.md`](../routes/upper/SPECIALIZED_CORRELATION_SHARPENING.md),
[`RETAINED_SPINE_SHARPENED_CERTIFICATE.md`](../routes/upper/RETAINED_SPINE_SHARPENED_CERTIFICATE.md),
[`INDEPENDENT_RETAINED_SPINE_SHARPENED_REFEREE.md`](../routes/upper/INDEPENDENT_RETAINED_SPINE_SHARPENED_REFEREE.md),
and
[`SHARPENED_RESULT_TO_CLAIM.md`](../routes/upper/SHARPENED_RESULT_TO_CLAIM.md).

## Off-diagonal asymptotic lower bounds

- Hefty--Horn--King--Pfender v3 prove
  `R(3,k)>=(1/2+o(1))k^2/log k`, improving the preceding `1/3` constant.  Their
  abstract records the upper constant `1`, leaving a factor-two constant gap.
- Bradač v3 proves, for every fixed `s>=3`,
  `r(s,k)=Omega_s(k^(s-1)/(log k)^(2s-4))`.  This is substantially stronger
  than v1 and leaves a polylogarithmic, not polynomial-exponent, target.
- Hunter--Milojevic--Sudakov give a Gaussian construction for
  `R(l,C l)`.  Lin--Niu v2 claim a further positive exponent improvement from
  a sharp truncated-Gaussian cumulant bound.

The Lin--Niu/HMS source audit found that the new `P_D -> 1` Hölder companion
has leading linear-MGF coefficient `1/2`, while the literal HMS `P=2` Cauchy
companion has coefficient `1`.  The common-history subtraction has now been
inserted directly into HMS's optimized red appendix, before its coarse error
ledger.  The resulting local proof package gives, for every sufficiently
large fixed `C`,

$$
\liminf_{\ell\to\infty}\ell^{-1}\log R(\ell,\lfloor C\ell\rfloor)
\ge -\tfrac12\log p_C+\tfrac1{20}+\frac{c_R(C)}{4D^2},
$$

with `c_R(C)>0` and
`c_R(C)/(4D^2)=(1+o(1))/(32 log C)`.  The perfect-sequence extraction is
quantified deletion-by-deletion, and the unchanged blue appendix bound remains
strictly above the red rate.  The `1/20` term includes slack already present in
HMS; the `c_R` term is the genuine new same-ledger contribution.  This is a
**LOCAL PROOF-PACKAGE THEOREM pending external review**, not yet a published
result.  The same Hölder device is algebraically blocked on the optimized blue
side, but blue is not the bottleneck for this large-`C` statement.

Two independent source-level reviews, including one adversarial replay of the
most fragile same-history subtraction and extraction steps, found no fatal
gap. The source's unspecified `O/o` constants still make the threshold
existential rather than a certified numerical $C_0$.

A source-faithful optimization of that red companion now yields an explicit
$G_*(C)>c_R(C)/(4D^2)$ for every sufficiently large fixed $C$.  The strict
inequality already follows by replacing the variance proxy with the exact
upper-truncated CGF at the same old window, Holder pair, and history; using the
largest legal step-dependent Holder parameter and approaching the sharp
limiting cutoff window improves it further.  An independent source-level
referee accepts the resulting theorem and

$$
G_*(C)=\frac{1+o(1)}{32\log C}.
$$

A matching central-history/Jensen cap is proved only for deterministic,
history-uniform, per-step centered-moment deficits accumulated additively in
the frozen induction.  Thus tuning CGF/Holder/window inside that class cannot
raise $1/32$ to $1/16$; history-dependent states and changes to the mean,
dimension, blue lemma, or graph model remain open routes.

For Bradač, a naive type-sensitive refinement was ruled out: its optimized
entropy cost remains `Theta(q log^2 q)`.  The next two repair attempts now have
rigorous obstructions as well.  Beyond permanent disjoint blocks and a
rank-two singleton history, a counted `Theta_t(q log q)` family has every step
unmarked with `r=ell=0`; its excess path count is
`exp(Omega_t(q log^2 q))` above `(C_tq^t)^k`.  This refutes the uniform
all-length transverse record map.  A follow-up proves a state-conditioned late
tail after every type layer is saturated, but also shows that absolute depth
cannot force saturation and that any recoverable positive scalar potential
pays `exp(Omega_t(q log^2 q))` on the rank-zero family.  The actual
`k>=A_t q log q` tuple bound remains open.  Independent source-level replays
accepted both the counted construction and the late-tail/weight conclusions.
This is a **rigorous mechanism diagnosis, not a new lower bound**.

The follow-up exact cross-type audit proves $U_j'=U_j\setminus R_j$: each promoted
point leaves one cutoff only, so nested cutoffs cannot be charged as repeated
progress.  It also refutes a categorical marked/unsaturated dichotomy and
shows that the exact transfer is Markov only on the full subspace-incidence
state `y -> W(y)`, not on cutoff cardinalities.  A rank-zero path need not
diversify before `floor((t-1)q log q/12)`; diversification after a larger
`A_t q log q` threshold remains open.  These statements passed independent
source-level review after that quantifier boundary was corrected.

The exact full-state continuation now has one positive compression theorem:
projective-orthogonal state orbits form an exact strong lumping of the
pair-labelled transfer, and every positive supersolution may be group-averaged.
For `t=2,q=2` this reduces 23,962 reachable states to 4,243 orbits.  A
constant-dimensional self-incidence profile gives the exact current fanout but
fails strong lumpability on an explicit reachable pair.  This reviewed result
identifies the correct finite operator for a future spectral weight; it does
not yet bound that operator uniformly in `q` and yields no new Ramsey lower
bound.

## Selected finite cells

The April 2026 dynamic survey gives `R(3,13)=61--68`, `R(3,17)=92--109`, and
`R(4,15)=159--364`.  Later public matrices from ScaleAutoResearch were pinned
and independently reconstructed here:

| Cell | Checked witness | Working interval | Status |
|---|---:|---:|---|
| `R(3,13)` | AlphaEvolve, 60 vertices | `61--68` | seed only; no improvement found |
| `R(3,17)` | 92 vertices, `omega=2`, `alpha=16` | `93--109` | **INDEPENDENT-CERT** |
| `R(3,18)` | AlphaEvolve, 99 vertices, `omega=2`, `alpha=17` | `100--120` | **INDEPENDENT-CERT**; independently reviewed budget-five repair exclusion |
| `R(4,15)` | 159 vertices, `omega=3`, `alpha=14` | `160--364` | **INDEPENDENT-CERT** |

The last two are finite mathematical certificates, so their validity does not
depend on peer review; however, they are described as post-survey public
certificates rather than survey-incorporated records.

The local target `R(3,13)>=62` did not succeed.  Exact SAT proved:

- the named 60-vertex seed has no frozen one-vertex extension;
- with zero independent 13-set, the frozen extension has minimum exactly ten
  triangles;
- an 11-triangle hub near miss cannot be repaired with arbitrary additions and
  at most eight deletions.
- at budget nine, the hub is forced and leaves eight residual deletions against
  25,685 independent-set hitting clauses; a Benders master accumulated 24,832
  strict conditional cuts and 81,345 strict pairwise shared-deficit cuts, but
  its bounded replay remains `UNKNOWN` and produced no graph.
- a higher-order follow-up added 57,879 independently replayed strict ternary
  shared-deficit cuts; its bounded replay also remains `UNKNOWN`.
- a deliberately different 61-vertex seed has eleven triangles, no
  independent 13-set, and no edge common to all eleven triangles.  In the
  exact family allowing arbitrary additions, at most ten seed-edge deletions
  are impossible.  Three hub-deleted branches and one exact merged CNF for
  all 512 hub-retained transversals are Glucose- and CaDiCaL-UNSAT; all four
  frozen DRAT traces independently pass `drat-trim`.
- a second, genuinely dispersed one-vertex basin has 17 triangles, no
  independent 13-set, maximum triangle-edge multiplicity four, and triangle
  transversal number eight.  Its exact cap-four optimum lies between 10 and
  17 and remains unknown; the object is a near miss, not a certificate.

The old hub basin has certified radius nine; the new non-star basin has
proof-carrying radius eleven.  These statements do not establish
`R(3,13)>=62`.

The separate `R(3,18)>=101` attempt has a sharper local entrance.  The frozen
100-point extension of the checked 99-point certificate has no `I18` and only
one triangle.  Three exhaustive triangle-edge branches, each allowing
arbitrary additions and a total of five input-edge deletions, have
reconstructed CNFs and `drat-trim`-verified UNSAT proofs.  The fixed near miss
therefore needs at least six deletions.  At exact budget six, the branch fixing
`(98,99)` absent has an independently replayed DRAT UNSAT proof; the other two
branches remain `UNKNOWN`.  Hence the complete budget-six ball remains open,
the fixed radius is not raised to seven, and this does not establish
`R(3,18)>=101`.

## Ranked next moves

### 1. External review and archival of the `3.780687577208` upper theorem

The P6 chain, specialized correlation lemma, retained-spine transfer,
sharpened weighted-wedge enclosure, and adversarial numerical reconstruction
are complete locally.  The highest-value next step is external combinatorics
review, immutable public archival of the proof package and logs, and then a
publication-grade statement.  The certified exponent gain is `2.87e-6`;
global correlation and retained-spine parameter optimization is lower priority
than validating the imported interfaces externally.

### 2. External specialist review of the optimized HMS appendix bridge

The red optimized-appendix bridge and its exact-CGF parameter optimization now
close locally and have independent source-level replays.  The immediate next
step is external line-by-line review and immutable archival.  Mathematically,
the next genuine sharpening must leave the proved uniform centered-moment
`1/32` cap, for example through a history-dependent mean ledger or a blue
quadratic-moment estimate that permits a smaller dimension scale.

### 3. Resolve the two remaining budget-six `R(3,18)` branches

Budget five has proof-carrying exclusion.  At exact budget six, the branch
fixing edge `(98,99)` absent now has a checked finite-CNF DRAT proof, while the
other two branches remain `UNKNOWN` after two 600-second solvers each.  Any
future search should focus only on those two branches, preserve proof-carrying
separation, and reconstruct any candidate with the independent bitset checker.

### 4. Resume `R(3,13)>=62` outside the two excluded local radii

Either continue the old hub master beyond eight residual deletions or leave
the non-star seed's now-excluded ten-deletion ball.  Every candidate must be
reconstructed by the independent clique/independence checker.

### 5. Develop a transverse Bradač deficit encoding

This is potentially the highest-impact lower-bound direction but also the
least mature.  The first deliverable should be a finite combinatorial lemma
that survives the explicit low-rank removal-block history and shows
`O(q log q)` encoding/repair cost; until then, asymptotic extrapolation is
speculative.

Closing `R(5,5)` remains a poor first target: either direction requires a much
larger exhaustive proof pipeline than the current workspace provides.

## Primary sources

- Radziszowski, *Small Ramsey Numbers*, Dynamic Survey DS1.18:
  <https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS1/pdf/0>
- Campos--Griffiths--Morris--Sahasrabudhe:
  <https://arxiv.org/abs/2303.09521>
- Gupta--Ndiaye--Norin--Wei:
  <https://arxiv.org/abs/2407.19026>
- HorizonMath paper and public verifier:
  <https://arxiv.org/abs/2603.15617>,
  <https://github.com/ewang26/HorizonMath>
- Hefty--Horn--King--Pfender:
  <https://arxiv.org/abs/2510.19718>
- Bradač:
  <https://arxiv.org/abs/2605.28793>
- Hunter--Milojevic--Sudakov:
  <https://arxiv.org/abs/2512.17718>
- Lin--Niu:
  <https://arxiv.org/abs/2605.25843>
- AlphaEvolve certificates:
  <https://github.com/google-research/google-research/tree/master/ramsey_number_bounds/improved_bounds>
- ScaleAutoResearch public certificates:
  <https://github.com/ypwang61/ScaleAutoResearch-Ramsey>
