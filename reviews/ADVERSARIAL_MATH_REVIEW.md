# Adversarial mathematical review of the Ramsey manuscript package

Date: 2026-08-30  
Objects reviewed: `papers/upper`, `papers/lower`, `papers/finite`, and the
proof-critical checkers and certificates under `routes/`  
Review posture: attempt to falsify the strongest claims; distinguish a theorem
proved by the manuscript from a theorem that becomes valid only after importing
an exact external interface.

## Status vocabulary

This report uses the proof-writer statuses literally.

- **PROVABLE AS STATED**: the displayed assumptions and supplied proof chain
  suffice for the displayed conclusion.
- **PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION**: the numerical or algebraic
  conclusion survives, but the manuscript must add a precise hypothesis or
  weaken the claim.
- **NOT CURRENTLY JUSTIFIED**: a necessary implication is absent, circular, or
  not recoverable from the text and proof artifacts presently named by the
  manuscript.

## Executive verdict

| Component | Verdict | Does the headline survive? |
|---|---|---|
| Exact-diagonal analytic inequalities in the upper-bound route | **PROVABLE AS STATED**, conditional only on Arb containment semantics for the compact enclosures | Yes |
| Six-stage off-diagonal rate used by the upper-bound route | **PROVABLE AFTER EXTRA ASSUMPTION** in this manuscript; the local route package contains a substantially fuller proof than the paper | Yes, after the certificate theorem and its hypotheses are stated precisely |
| Upper headline `R(k,k) <= (3.780685290)^(k+o(k))` | **PROVABLE AFTER EXTRA ASSUMPTION** | The decimal survives, but the Yang--Mao book interface and the outer certificate are not formally stated in the paper |
| Lower controlled-residual algebra (recursion, Hessian reduction, multiplicities, square completion) | **PROVABLE AS STATED** once the standard inverse-Mills facts are added explicitly | Yes |
| Lower headline source-relative term `Hhat_*(C) ~ 1/(64 log C)` | **PROVABLE AFTER EXTRA ASSUMPTION** | The leading coefficient survives, but the paper does not define its source quantities or prove the probability-ledger bridge at publication standard |
| Claimed exact-merge freedom statement for arbitrary edge-dependent rescalings | **NOT CURRENTLY JUSTIFIED** as written | Only the uniqueness of the effective triangular coefficient array survives without qualification |
| Narrow `1/64` method cap | **PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION** | It must be formulated for a precise uniformly bounded admissible residual class |
| Fixed-seed finite theorem `rho(H) >= 7` | **PROVABLE AS STATED** under the conventional DRAT checker trust boundary | Yes; all six proofs were freshly replayed in this review |
| `R(3,18) >= 101`, existence of an exact-seven repair, or a global Ramsey-bound improvement from the finite computation | **NOT CURRENTLY JUSTIFIED**, and correctly disclaimed by the paper | No such global claim should be added |

The package therefore contains two plausible source-relative asymptotic results
and one fully proof-carrying local finite result, but the asymptotic manuscripts
are not yet submission-ready as standalone proofs.  The principal blockers are
formal interfaces and missing probability/certificate derivations, not a failed
numerical inequality.

## Computations independently replayed during this review

The following checks were run from the repository environment.

1. All four 512-bit upper-bound programs returned `PASS`:
   `check_exact_diagonal_next.py`,
   `check_retained_spine_exact_diagonal_next.py`,
   `independent_check_exact_diagonal_next.py`, and
   `referee_check_exact_diagonal_next.py`.
2. The narrow upper margins were reproduced: degree
   `1.5056762e-9`, red page `5.100670782...e-9`, blue page
   `3.482565843...e-6`, reservoir `6.046877960...e-6`, and rounding
   `1.620359886...e-9`.
3. The independently enclosed upper base was
   `3.780685288379640113352371677...`, which is strictly less than both
   `3.780685288379640114` and the safe decimal `3.780685290`.
4. `history_weight_optimization_next_check.py` passed its recursion,
   Hessian-sample, finite arithmetic, and asymptotic diagnostics.  This is an
   arithmetic check, not a proof of the source probability bridge.
5. All twelve finite compressed artifacts matched the byte counts and SHA-256
   values in `artifacts/MANIFEST.tsv`; all 28 finite unit tests passed.
6. I freshly cloned `drat-trim` at commit
   `2e3b2dc0ecf938addbd779d42877b6ed69d9a985`, compiled it, and obtained the
   recorded executable SHA-256
   `31d9e8e04bc76a65f0a18ea212ac44af4cf7bc398629495cec093ced772c50f4`.
   All three budget-five DIMACS/DRAT pairs replayed to `s VERIFIED`.  All
   three exact-six pairs also replayed to `s VERIFIED`: branch 2 used
   182,817,377 resolution steps, branch 1 used 209,897,525, and branch 0 used
   135,152,646.  The branch-0 raw trace was 3,493,847,713 bytes and its fresh
   check completed in about 286 checker-seconds.

Passing these programs establishes the frozen numerical statements under the
programs' semantics.  It does not by itself fill a missing theorem-to-code or
source-to-local-proof implication.

# I. Diagonal upper bound

## I.1 Exact normalized claim

The strongest intended claim is:

> Assume the exact Yang--Mao v1 regularization, positive-moment/tail,
> parameterized-book, and spine-compatibility theorems, and assume the locally
> certified uniform off-diagonal rate `U=F_6`.  Then
> `R(k,k) <= exp((U(1)-3.4754e-6)k+o(k))`, with exponential base below
> `3.780685288379640114`.

This is a conditional theorem.  The unconditional wording in the abstract
should be replaced by wording that displays the source-relative dependency in
the first sentence.

## I.2 Dependency map

1. The six-stage BookCor descent must prove a uniform rate for every
   `1 <= ell <= k`.
2. That rate must be extended symmetrically and homogeneously to every
   residual pair of clique orders used in the retained-spine proof.
3. The exact-diagonal calculation must prove the correlation property
   `G_2^(3)(beta,C)` for exactly the `beta,C` consumed by the book theorem.
4. Yang--Mao regularization must supply two retained preliminary spines, a
   common reservoir, and minimum degrees with the exact losses used locally.
5. The parameterized book theorem must turn two explicit reservoir-size
   inequalities into a monochromatic `tau k` spine and a page set of the
   required size.
6. The outer max--min inequality must cover every preliminary-spine vector and
   both possible book colours.
7. The final interval enclosure must imply the printed safe decimal.

Steps 3 and 7 pass.  Steps 1, 4, 5, and 6 are not stated with enough precision
inside the manuscript to make the paper's proof independently checkable.

## I.3 Major issue U1: the imported book interface is not a usable theorem

**Verdict: PROVABLE AFTER EXTRA ASSUMPTION.**

`papers/upper/sections/02_framework.tex:40-64` gives three prose bullets as the
"retained-spine source interface."  The bullets do not state:

- the exact minimum-degree conclusion after regularization;
- the parameterized book theorem's hypotheses;
- the required lower bounds on the reservoir;
- the size and colour semantics of the returned page set;
- the formulas for the page cost `q` and reservoir cost `Xi`; or
- the scalar gates involving `p`, `delta`, `lambda_0`, `tau`, `beta`, and `C`.

Nevertheless `papers/upper/sections/02_framework.tex:84-92` introduces `q`
and `Xi` as if already defined, and `:123-129` uses them to assert that the
book branch fires.  The implication is therefore not derivable from the
displayed assumption.  A prose statement that a theorem "supplies" a cost is
not enough when the numerical value of that cost is proof-critical.

The missing formulas do exist in the code.  For example,
`routes/upper/independent_check_exact_diagonal_next.py:306-317` computes

```text
q  = log(1/p) + 3 delta/p
     + 6 log(1/delta) log(1/p)/lambda_0,

Xi = 2 log(2/beta) + 4 C lambda_0^(1/3)
     + 12 C log(1/delta)/lambda_0^(2/3).
```

The paper must state these formulas and quote the exact source theorem with
all quantifiers and output sizes.  The smallest safe repair is to replace the
current prose assumption by a formal theorem/assumption whose conclusion is
exactly the pair of size implications used in equations (2.7)--(2.8), plus
the spine-compatibility conclusion.  The source line map should then be
included in an appendix.

## I.4 Major issue U2: the advertised outer certificate is not in the appendix

**Verdict: NOT CURRENTLY JUSTIFIED by the paper text; computationally
supported by the repository.**

The proof of the outer certificate says that the complete partition and
endpoint formulas are listed in Appendix A
(`papers/upper/sections/05_transfer.tex:46-56`).  Appendix A
(`papers/upper/appendices/A_certificate_data.tex:1-26`) contains only the
headline constants, cell counts, and file hashes.  It does not list the
partition, the red/blue boundary reductions, or the endpoint inequalities.

This is not merely a stylistic omission: the smallest margin is about
`1.5e-9`, so the exact formula and the enclosure domain are part of the proof.
The code and the independent adaptive replay do verify the wedge, but the
manuscript's claim about what its appendix contains is false.

Minimum repair:

1. state the ordered wedge and its three vertices explicitly;
2. derive the direct gain `x A + (y-x) E` from concavity;
3. derive the red boundary derivative and its monotonicity;
4. derive the blue diagonal reduction and its monotonicity;
5. state the reservoir monotonicity;
6. list the exact rational parameters, checker hashes, interval precision, and
   lower endpoints returned for all four gates.

After those additions, Proposition 5.1 is supported by the current checkers.

## I.5 Major issue U3: the displayed proof does not prove the stronger
unrounded decimal it claims

**Verdict: NOT CURRENTLY JUSTIFIED by the displayed inequality; easily
repairable.**

The theorem claims an unrounded base below
`3.780685288379640114` in
`papers/upper/sections/01_introduction.tex:39-40`.  The final proof displays
only

```text
exp(U(1)-Delta) < 3.780685288380
```

at `papers/upper/sections/05_transfer.tex:64-69`.  That is a weaker upper
bound and does not imply the longer decimal.  The numerical checker does prove
the stronger value, with upper enclosure
`3.780685288379640113352...`.  Replace the displayed inequality by an
outward-rounded interval with enough digits, and report its lower rounding
margin.  Until then, the sentence "This proves ... the stronger unrounded
statement" is logically incorrect.

## I.6 Major issue U4: the six-stage rate is asserted more fully than it is
specified

**Verdict: PROVABLE AFTER EXTRA ASSUMPTION / certificate specification.**

`papers/upper/sections/03_rate.tex:33-44` states a uniform theorem.  The
following paragraphs describe cell counts and margins, but the manuscript does
not state the analytic descent lemma, its complete hypotheses, or the exact
predicate checked on each certificate cell.  Appendix C records the sixth
stage and command output; it does not reproduce the six formal certificate
obligations.  Appendix B gives the combinatorial BookCor core, but that alone
does not define the theorem-to-JSON implication.

The local route package contains the missing information and multiple
replays, so I found no numerical counterexample.  For publication, add a
formal "certificate correctness theorem": define the JSON schema, state each
continuum inequality and endpoint/tail obligation, prove that successful
verification yields the next rate, and then state an exact-linked induction
over the six certificate hashes.

## I.7 Endpoint and notation defects

These do not change the intended asymptotic base but must be repaired.

1. `papers/upper/sections/02_framework.tex:17-33` writes
   `R(floor(xk),floor(yk))` for `x,y` that may be zero, without defining Ramsey
   numbers with a zero clique order.  Define residual order at most zero as an
   already completed clique (cost one), or restrict the lemma to positive
   orders and state the boundary convention separately.
2. The proof's sentence that continuity and compact subdivision make the
   sublinear-parameter error uniform is not a proof.  Either cite the exact
   uniform epsilon statement already established by the rate package or add a
   short split argument.
3. `papers/upper/sections/05_transfer.tex:5` contains `,qquad` rather than
   `,\qquad`; the compiled mathematical display therefore contains unintended
   letters.

## I.8 Analytic correlation certificate

**Verdict: PROVABLE AS STATED.**

I checked the following potential failure points and found no sign or
inequality reversal.

- The root-filter identities `E(u^3)=P(u)` and `E(-u^3)=N(u)` are correct.
- The separator identity
  `F(-t,y)=H(-t)((2-R)H(y)-H(-y))/2` is exact.
- The three sign regions in the diagonal reduction are exhaustive.
- For `A_i >= -1`, the exponent in the diagonal envelope is exactly
  `4 u_0 (max(A_1,A_2)+1)^(1/3)` when the maximum is nonnegative; when it is
  negative the left side is at most zero and the positive envelope is
  automatic.
- The tail upper bound is monotone and its limiting floor is `exp(-2u_0)/81`.
- The exact cost-credit difference in the moment/tail step is positive.

The compact and tail enclosures were independently replayed.  The narrowest
inner analytic-tail slack is about `8.3673e-10`, so the exact file hashes and
outward rounding are indispensable.

## I.9 Corrected upper theorem suitable for the unified paper

The safe statement is:

> **Conditional upper theorem.**  Assume the exact version-pinned Yang--Mao
> regularization, positive tensor-moment/tail, parameterized-book, and
> spine-compatibility theorems stated in Appendix U, and assume the exact-linked
> six-stage certificate correctness theorem stated in Appendix R.  Under Arb's
> documented containment semantics, the frozen certificates prove
> `R(k,k) <= exp((U(1)-3.4754e-6)k+o(k))`, and the exponential base has an
> outward-rounded upper endpoint less than
> `3.780685288379640114`.  In particular,
> `R(k,k) <= (3.780685290)^(k+o(k))`.

Do not state the decimal without the word "conditional" until the imported
interfaces are reproduced as formal theorem statements and checked against the
pinned source.

# II. Fixed-ratio lower bound

## II.1 Dependency map

1. Define the exact HMS Gaussian parameters `p`, `c`, `D`, the perfect-history
   window, and the source red/blue first-moment ledgers.
2. Import or prove the exact one-sided truncated-Gaussian CGF inequality that
   defines `G_*(C)`.
3. Define the deterministic triangular residual array and prove adaptedness.
4. Prove full-box strong concavity and pay the gradient mismatch by square
   completion.
5. On the same conditional history, apply the three-factor Holder split and
   derive every linear and quadratic comparison constant.
6. Accumulate the deterministic mass and residual penalty through reverse
   induction.
7. Prove that perfect-sequence deletion absorbs the entire new exponent for
   every deletion count.
8. Compare the exact red and blue first-moment thresholds and take limits in
   the order: fixed `C`, then `ell -> infinity`, then `C -> infinity`.

Steps 3, 4, and the combinatorial part of 6 are sound.  The manuscript does
not supply publication-grade versions of Steps 1, 2, 5, 7, or 8.

## II.2 Major issue L1: essential source quantities are undefined

**Verdict: PROVABLE AFTER EXTRA ASSUMPTION; not a closed theorem as written.**

The introduction says that `B_R(C)` and `G_*(C)` are defined precisely in
Section 2 (`papers/lower/sections/01_introduction.tex:29-31`).  They are not.
Section 2 also describes `c(C)` and `D(C)` only by prose
(`papers/lower/sections/02_setup.tex:3-15`).  No equation defines the actual
construction parameters

```text
p = p_C + 1/C,
Phi(-c) = p,
D = 4 phi(c) C/(1-p).
```

The exact definitions of `B_R(C)`, `G_*(C)`, the source envelope
`H_C(r)`, and the red/blue thresholds are likewise absent.  The assumption at
`papers/lower/sections/02_setup.tex:62-70` says that the imported inputs supply
"the unchanged first-moment conversion ... to (1.1)."  That wording is too
close to importing the desired conclusion and is not falsifiable as a theorem
hypothesis.

Minimum repair: reproduce the exact version-pinned source theorem and define
every symbol occurring in the local theorem before stating it.  State the
source red and blue probability bounds, not merely the final Ramsey-rate
conversion, and prove the conversion locally.

## II.3 Major issue L2: the cutoff window disagrees with the proof and checker

**Verdict: requires correction; the leading `1/64` asymptotic survives.**

The paper defines

```text
omega_0 = 100 log(10/p_C)/D
```

at `papers/lower/sections/02_setup.tex:13-15`.  The proof package and checker
use

```text
p = p_C + 1/C,
omega_0 = 100 log(10/p)/D.
```

See `routes/lower/history_weight_optimization_next_check.py:84-90` and
`routes/lower/HISTORY_WEIGHT_OPTIMIZATION_NEXT.md:39-53`.
Thus the checker is not checking the exact quantity displayed by the paper.
Because `p>p_C`, the paper's window is slightly larger; the large-`C` leading
asymptotic is unchanged, and a weaker theorem may still follow by taking the
larger window.  But the exact finite-`C` function `Hhat_*(C)` is not the same
function.  Use `p`, not `p_C`, or explicitly prove and label the larger-window
coarsening.

## II.4 Major issue L3: the three-factor moment comparison is asserted, not
proved

**Verdict: NOT CURRENTLY JUSTIFIED by the manuscript.**

The proof-critical statements

```text
weighted quadratic cost <= (16/3) S_i/d,
three linear-CGF errors <= Lhat_w(C) S_i/d
```

appear at `papers/lower/sections/05_ledger.tex:51-73`.  Appendix A
(`papers/lower/appendices/A_full_source_proof.tex:116-152`) repeats the three
error terms and gives only a one-sentence indication for the hardest term.
It never defines the conditional random variables, the old and new centered
linear tilts, or the cumulant function to which Holder is applied.  It also
does not show that `G_*(C)` and the new increment arise from two disjoint
summands of one exact same-history decomposition.

This is the central probability step.  It cannot be replaced by a numerical
checker.  The longer route files contain a plausible derivation, but that
derivation must be incorporated into the paper.  At minimum, the paper must:

1. display the conditional factorization of the weighted exponent;
2. define the three conjugate exponents and prove `1/P+1/Q_0+1/Q_1=1` with
   all of them greater than one;
3. state the exact square-MGF lemma and verify its argument range;
4. derive `16/3`, not quote it;
5. state the positive-direction truncated CGF lemma;
6. derive each of the three terms in `Lhat_w(C)`; and
7. write the same-history identity showing that `G_*(C)` is charged exactly
   once.

Until then, the lower headline is not proved by the manuscript itself.

## II.5 Major issue L4: extraction and red--blue crossing are underproved

**Verdict: PROVABLE AFTER EXTRA ASSUMPTION / missing derivation.**

`papers/lower/sections/06_induction.tex:30-46` says that the source failure
factor `(p/10)^(10 ell u)` dominates the restoration cost, old extraction
costs, and the discretization error.  Neither `p` nor the complete restoration
exponent is defined in the paper, and the sum over all deleted subsets is not
shown.  Appendix A, lines 169--182, again asserts the domination without the
actual binomial sum.

Similarly, `papers/lower/sections/07_rate.tex:39-42` says that an added
`o(1)` term leaves the red--blue crossing unchanged.  Smallness alone is not
enough; one needs a positive limiting gap.  Appendix B, lines 44--48, asserts a
constant-order gap but does not display the two thresholds.

Minimum repair: give the exact deletion-cost inequality for every
`0 <= u <= ell`, prove

```text
sum_{u=1}^ell binom(ell,u) exp(-eta_C ell u) = o(1),
```

and display the exact red and blue first-moment rates before taking their
minimum.  The detailed route audit indicates that the red bonus tends to
`1/12` while the blue bonus tends to `1/2`, which would provide ample gap,
but the unified paper must prove this in its own notation.

## II.6 Controlled residual algebra that survives review

**Verdict: PROVABLE AS STATED, with explicit standard facts added.**

The following local steps are correct.

1. Processing first endpoints in decreasing order makes the recursion
   triangular and adapted.
2. Direct differentiation gives
   `partial_j F_i(c 1) = -(T_ij-e_ij)/sqrt(d)`.
3. If `m'' >= 0`, `T_ij >= 0`, and the displayed row-sum bound holds,
   Gershgorin gives the stated full-box Hessian lower bound.
4. Expanding `delta_j=sqrt(d)h_ij+epsilon_ij` shows that the apparent
   `e epsilon` term is already included in `e delta/sqrt(d)`; no residual is
   missing from the square completion.
5. The exact identity
   `K_r = sum_{i=1}^{r-1}(r-i)(i-1)^2 = binom(r,3)+2binom(r,4)` is correct.
6. The future-feedback contribution counts each ordered quadruple twice,
   yielding `2 A_0 binom(r,4)`.
7. Given the source asymptotics
   `m_0^2~2log C` and `D^2~32(log C)^3`, the displayed numerator is
   `(6+o(1))(log C)^2`; division by `12D^2` gives
   `(1+o(1))/(64 log C)`.

The paper should nevertheless state or prove the inverse-Mills facts
`m'>0` and `m''>=0` on the cutoff interval rather than leaving them implicit.

## II.7 Exact-merge uniqueness and rescaling overclaim

The coefficient comparison and triangular recursion in
`papers/lower/sections/03_rigidity.tex:18-39` uniquely determine the
**effective coefficient array** required for exact boundary merge.  That part
is **PROVABLE AS STATED**.

The sentence that arbitrary edge-dependent potential rescaling "likewise only
rename[s] the effective coefficients" is **NOT CURRENTLY JUSTIFIED**.  An
edge-dependent rescaling can change which coefficients appear in different
gradient rows unless the admissible rescaling is defined to preserve exactly
the same effective weighted-pair potential.  The smallest repair is to delete
the edge-dependent sentence and state uniqueness only modulo a global scalar
reparameterization, or give a formal equivalence relation and prove it.

## II.8 Narrow method cap

**Verdict: PROVABLE AFTER WEAKENING / precise admissibility assumptions.**

The pointwise quadratic optimization in
`papers/lower/sections/07_rate.tex:44-61` correctly selects
`e_ij = mu_w Bhat_w (i-1)` at leading order.  However, the claimed cap for an
entire residual class needs uniform hypotheses ensuring that feedback and
extraction remain lower order for every array in the quantified class.  The
current prose does not specify a growth bound, summability condition, or a
uniform `rho=o(1)` estimate for arbitrary increments.

State an admissible class such as nonnegative deterministic increments with a
uniform `e_ij=O(m_0^2 r)` bound and the exact same scalar Holder/MGF envelope.
Then bound the feedback contribution uniformly before taking the pointwise
maximum.  Without this addition, describe `1/64` as the optimum of the tested
scalar ansatz, not a theorem-level cap.

## II.9 Corrected lower theorem suitable for the unified paper

A defensible statement is:

> **Source-relative lower theorem.**  Define
> `p=p_C+1/C`, `Phi(-c)=p`,
> `D=4 phi(c) C/(1-p)`, and
> `omega_0=100 log(10/p)/D`.  Assume the exact version-pinned HMS red/blue
> probability ledgers, reverse-induction and extraction propositions, and the
> exact version-pinned positive-direction truncated-Gaussian CGF lemma stated in
> Appendix L.  Then there exists `C_0` such that, for every fixed
> `C>=C_0`, the displayed lower Ramsey rate holds with the locally defined
> `Hhat_*(C)>0`, and
> `Hhat_*(C)=(1+o(1))/(64 log C)` as `C->infinity`.

The appendix must define `B_R(C)` and `G_*(C)` exactly and prove the local
same-history, extraction, and first-moment steps.  Until then, do not call the
paper a standalone proof; call it a source-relative proof sketch with a full
proof package in the repository.

# III. Fixed-seed finite computation

## III.1 Exact claim

For the content-addressed 100-vertex graph `H`, let `rho(H)` be the minimum
number of original edges deleted to obtain a triangle-free graph with
independence number below 18, while arbitrary original nonedges may be added
for free.  The claim is `rho(H)>=7`.

## III.2 Dependency map and logical direction

1. Direct checking gives exactly one seed triangle, with edges
   `(97,98)`, `(97,99)`, `(98,99)`.
2. Every triangle-free repair therefore belongs to at least one of three
   branches fixing one of those edges absent.
3. Three checked budget-five CNFs exclude at most five original-edge
   deletions.
4. A putative repair with at most six deletions must therefore have exactly
   six.
5. In a branch whose fixed triangle edge is absent, exactly five of the other
   826 original edges are absent.
6. Triangle clauses and installed independent-18 hitting clauses are necessary
   conditions for every target repair.  Omitting other hitting clauses makes
   the CNF a relaxation, so UNSAT has the required direction.
7. Checked DRAT refutations of all three exact-six relaxations exclude every
   exact-six repair.

Every direction in this chain is correct.  In particular, allowing all 4,123
original nonedges as free primary variables is implemented correctly; none is
counted as a deletion literal.

## III.3 Fresh proof replay verdict

**Verdict: PROVABLE AS STATED under the conventional DRAT trust boundary.**

The fresh checker compiled in this review reproduced all three budget-five
refutations.  It then independently replayed all three exact-six traces:

| branch | clauses | proof lines | resolution steps | result |
|---:|---:|---:|---:|---|
| 0 | 429,892 | 6,649,939 | 135,152,646 | `s VERIFIED` |
| 1 | 242,064 | 5,590,150 | 209,897,525 | `s VERIFIED` |
| 2 | 183,543 | 2,837,771 | 182,817,377 | `s VERIFIED` |

The semantic checkers reconstructed the triangle block, counter, fixed unit,
and every installed 18-set clause for each exact-six formula.  Thus the
fixed-seed theorem does not rely only on stored status strings.

The theorem remains local.  It does not imply `R(3,18)>=101`: `H` itself has
a triangle, and the proof says nothing about remote 100-vertex graphs.  It also
does not establish a repair at exactly seven deletions.  The paper handles both
boundaries correctly.

## III.4 Reproducibility and release boundary

The large artifacts exist locally and match the manifest, but they are ignored
by Git and there is currently no configured Git remote.  Consequently the
sentence "The public repository separates ..." in
`papers/finite/sections/07_reproducibility.tex:3-6` is not yet a statement a
third party can execute from a clean clone.  The theorem is locally
proof-carrying; public reproducibility is pending publication of all twelve
manifest assets under an immutable release tag or archival DOI.

Do not declare the GitHub reproduction complete until a fresh machine can:

1. clone the repository;
2. download all twelve assets named by `artifacts/MANIFEST.tsv`;
3. verify every compressed hash and byte count;
4. build `drat-trim` from the pinned commit; and
5. replay all six proof pairs to `s VERIFIED`.

Two machine-readable status fields are also fragile:

- `check_r3_18_budget6.py` reports a top-level
  `BRANCH2_EXACT_BUDGET6_PROOF_VERIFIED` even when its nested proof status is
  `NOT_RERUN` (`routes/finite/check_r3_18_budget6.py:153-165`).
- the branch-0 checker emits `seven_deletion_repair_exists: false` together
  with `seven_deletion_repair_exists_is_established: false`
  (`routes/finite/check_r3_18_budget6_branch0_union.py:257-266`).

The paper warns readers not to interpret the second field as a theorem, but a
safer schema would use `null` for an unknown existence value and reserve
`PROOF_VERIFIED` for a replay performed in the current run.

# IV. Consequences for a single unified paper

The three components can appear in one paper, but they are logically
independent.  The unified paper should not suggest that the finite computation
supports the asymptotic upper or lower theorem, or that the lower construction
uses the upper certificate.  A defensible organization is:

1. evidence taxonomy and exact status of each theorem;
2. conditional diagonal upper bound;
3. source-relative fixed-ratio lower bound;
4. proof-carrying local finite barrier;
5. common reproducibility protocol and trust boundaries;
6. separate appendices for the upper source interface, upper certificate
   theorem, lower probability bridge, and finite artifact ledger.

The abstract must say explicitly that the first two results are
source-relative/conditional and that the third is local and does not improve
the global interval for `R(3,18)`.

# V. Required repair order

## P0: blockers before submission

1. Replace the upper Yang--Mao prose interface by an exact theorem statement,
   including `q`, `Xi`, all scalar gates, reservoir sizes, page size, colour,
   and compatibility.
2. Add the missing upper outer-wedge derivation and exact certificate table;
   do not claim Appendix A contains data that it does not contain.
3. Define every lower source parameter (`p,c,D,B_R,G_*`, the red/blue
   ledgers) and replace the conclusion-like source assumption by exact
   probability theorems.
4. Insert the complete lower three-factor Hölder/CGF, extraction, and
   red--blue first-moment proofs.
5. Publish all finite CNF/DRAT release assets and demonstrate a clean-clone
   replay.

## P1: claim and formula corrections

1. Fix the upper unrounded decimal proof line.
2. Fix the lower `p_C` versus `p` cutoff-window mismatch.
3. Weaken or formalize the edge-dependent rescaling and `1/64` method-cap
   statements.
4. State the exact conditional/source-relative status in the title page,
   abstract, theorem summaries, and conclusion.

## P2: robustness and presentation

1. Define zero residual clique-order conventions in the homogeneous rate.
2. Fix the `qquad` TeX typo.
3. Use `null/UNKNOWN` rather than a false Boolean for unresolved existence.
4. Make every reproduction tier state whether DRAT was actually replayed in
   the current run.

## Final adversarial assessment

I did not find a numerical counterexample to the upper base, an algebraic
counterexample to the controlled-residual leading coefficient, or a logical
counterexample to the fixed-seed deletion barrier.  The strongest successful
attack is instead on theorem closure: the upper and lower manuscripts omit
proof-critical source interfaces and derivations while presenting their
headlines in a form that reads more unconditional than the actual evidence.

Accordingly:

- retain the upper decimal only as a precisely conditional theorem until the
  imported book interface and certificate theorem are written in full;
- retain the lower `1/64` term only as a source-relative theorem after the
  missing source definitions and probability bridge are inserted; and
- retain the finite `rho(H)>=7` theorem unchanged, while keeping all global
  `R(3,18)` and exact-seven claims explicitly open.
