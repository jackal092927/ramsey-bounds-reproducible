# Ramsey lower-bound route: progress as of 2026-08-12

## Outcome first

**The controlled-residual weighted ledger now supersedes the exact-merge
predecessor, relative to the pinned HMS/Lin--Niu source snapshots and frozen
appendix bridge.**  For every fixed sufficiently large $C$, it proves

$$
\liminf_{\ell\to\infty}\frac1\ell
\log R(\ell,\lfloor C\ell\rfloor)
\ge
-\frac12\log p_C+\frac{B_R(C)}2+G_*(C)+\widehat H_*(C),
$$

and hence the public coarsening with $B_R(C)/2$ replaced by $1/20$, where

$$
\widehat H_*(C)=\frac{1+o(1)}{64\log C}>0.
$$

The exact-merge array is unique and supplies the still-valid immediate
predecessor $H_*(C)=(1+o(1))/(96\log C)$.  The stronger proof retains the
negative full-box strong-concavity term, permits an explicit deterministic
boundary-gradient residual, and pays that residual by square completion.
The exact $K_r$ multiplicities, centered costs, and enlarged
non-exchangeable reverse induction then add $\widehat H_*(C)$ on top of
$G_*(C)$ without double counting.  An independent source-level referee
reconstructs the residual algebra, full cutoff-box Hessian, three-factor
moment comparison, reverse induction, perfect-sequence extraction, and rate
conversion.  Its method-cap scope correction is resolved, and the secondary
result-to-claim gate returns `yes/high`.

The corrected proof, arithmetic checker, and resolved referee SHA-256
identities are

```text
2234a769d7798a79174cbfb362ada64f5d760aefbe7e6d4fb8763cd5633a0312
616040b91aad4becf92dcfbe13b7e6d49a3c9c73f0f222ba56114104f1c7d554
ef6ddbce4f403bdf942a6a6c0ac3ca5ace110f5f2a8cbd0042a3658a9a02f008
```

See
[HISTORY_WEIGHT_OPTIMIZATION_NEXT.md](./HISTORY_WEIGHT_OPTIMIZATION_NEXT.md),
[history_weight_optimization_next_check.py](./history_weight_optimization_next_check.py), and
[INDEPENDENT_HISTORY_WEIGHT_OPTIMIZATION_REFEREE.md](./INDEPENDENT_HISTORY_WEIGHT_OPTIMIZATION_REFEREE.md).
Claim boundary: this is a source-relative local proof-package theorem with
existential large-$C$ quantifiers.  It gives no explicit numerical $C_0$, has
not received external human review, and gives no all-$C$ theorem, finite
Ramsey-number improvement, new blue argument, unconditional source reproof,
novelty, priority, publication, world-best, or global-optimality claim.  The
narrow $1/64$ cap applies only to the explicitly admissible scalar class with
the same recursion, nonnegative deterministic pre-sampling increments,
uniform scalar square completion, and the same three-factor Holder/CGF
comparison; adaptive and higher-order potentials remain outside it.

**The red-appendix history-uniform companion remains the independently
reviewed predecessor.**  Keeping the frozen HMS history and source ledger, the
exact upper-truncated CGF, largest legal step-dependent Holder split, and
limiting cutoff window give an explicit term $G_*(C)$ with

$$
G_*(C)>\frac{c_R(C)}{4D^2},\qquad
G_*(C)=\frac{1+o(1)}{32\log C}.
$$

The strict inequality already holds at the old window and old Holder pair,
so it does not depend on the cutoff limiting argument.  A matching
central-history/Jensen cap shows that $1/32$ is sharp only within the stated
class of deterministic, history-uniform, per-step centered-moment deficits
that are accumulated additively.  It does not constrain history-dependent
couplings or changes to the mean, dimension, blue lemma, or graph model.  The
proof and arithmetic replay are in
[LOWER_HMS_PARAMETER_OPTIMIZATION.md](./LOWER_HMS_PARAMETER_OPTIMIZATION.md),
with an independent source-level PASS in
[INDEPENDENT_HMS_PARAMETER_OPTIMIZATION_REFEREE.md](./INDEPENDENT_HMS_PARAMETER_OPTIMIZATION_REFEREE.md).

**The optimized red-appendix comparator bridge is now locally closed.**  For
every sufficiently large fixed $C$, the proof package establishes the public
checkpoint

$$
\liminf_{\ell\to\infty}\frac1\ell
\log R(\ell,\lfloor C\ell\rfloor)
\ge -\frac12\log p_C+\frac1{20}+\frac{c_R(C)}{4D^2},
$$

where $c_R(C)>0$ is explicit and

$$
\frac{c_R(C)}{4D^2}=\frac{1+o(1)}{32\log C}.
$$

The pathwise deficit is inserted into the literal HMS Appendix-B red
induction before coarsening, then survives a deletion-by-deletion quantified
perfect-sequence extraction.  The unchanged blue bound has sufficient margin.
The $1/20$ term contains HMS's own unused slack; only the $c_R$ term is the
new same-ledger gain.  Full proof, claim separation, source hashes, and the
blue Hölder obstruction are in
[HMS_APPENDIX_BRIDGE.md](./HMS_APPENDIX_BRIDGE.md), with arithmetic checks in
[hms_appendix_bridge_check.py](./hms_appendix_bridge_check.py).  Status:
**local proof-package theorem pending external human review**.

The newest Bradač-side result is deliberately negative but rigorous.  Beyond
the earlier rank-two singleton example, there are now
$k_q=\lfloor(t-1)q\log q/12\rfloor$-step families in the actual
`D^*(t,q)` tuple tree for which **every** step is unmarked with $r=\ell=0$.
Their geometric branching base is at least
$(3/16)q^{t+0.9(t-1)}$, so the uniform all-length record proposal with only
$\exp(O_t(q\log q))$ records and $(C_tq^t)^u$ preimages is false.  A positive
bounded-multiplicity fact also survives: any fixed first coordinate occurs in
at most $t$ unmarked steps.  This is an **obstruction to one mechanism, not a
new lower bound or an impossibility theorem**; it does not rule out a
sufficiently late-tail or weighted argument.  See
[TRANSVERSE_ENCODING_ATTEMPT.md](./TRANSVERSE_ENCODING_ATTEMPT.md) and its
independent acceptance in
[INDEPENDENT_TRANSVERSE_REFEREE.md](./INDEPENDENT_TRANSVERSE_REFEREE.md).

The earlier exact companion audit found a source-level coefficient mismatch.
Lin--Niu's $\gamma/8$ quartic gain is valid relative to a newly introduced
$P_D\to1$ unit-proxy Hölder companion, whereas the literal HMS
Cauchy--Schwarz ($P=2$) expansion has leading linear-MGF coefficient $1$
rather than $1/2$.

The second-stage audit now closes the missing common-history propagation for
fixed $p,C$: retaining the exact $A_i=\sum_{j\ne i}\mu_j$ until the two moment
envelopes are subtracted yields a uniform group deficit and a valid reverse
induction relative to one frozen, source-faithful HMS main-body ledger. The
red saving against that ledger is

$$
\frac{(1+\gamma_R)a^4}{8p^4}\frac{r^4}{d}
+O_{p,C}\left(\frac{r^4}{Dd}+\frac{r^3}{d}\right),
$$

with the analogous fixed-$C$ blue coefficient
$(1+\gamma_B)a^4/[8(1-p)^4]$. The proof and executable sanity check are in
[PAIRED_COMPANION_ATTEMPT.md](./PAIRED_COMPANION_ATTEMPT.md) and
[paired_companion_check.py](./paired_companion_check.py).

The blue lower-truncated induction and perfect-sequence extraction are now
complete relative to the unit-Hölder companion. Conditional on that baseline,
the normalized two-sided exponent gains

$$
\frac{(1-\lambda_C)C^3\beta_B(p_C)}{D^2}+O_C(D^{-3})
$$

beyond the one-sided variance refinement. The transverse-crossing calculation
is proved in [DOUBLE_TRUNCATION_LEMMA.md](./DOUBLE_TRUNCATION_LEMMA.md), and the
coefficients are recomputed by
[double_truncation_gain.py](./double_truncation_gain.py).

The earlier main-body comparison by itself was **not** a new Ramsey lower
bound: HMS's main-body proof only records an unspecified generic error, while
its explicit final large-$C$ constant comes from a different optimized
appendix induction.  `HMS_APPENDIX_BRIDGE.md` supersedes that limitation on
the red side by redoing the optimized appendix against the same history.
The blue reverse induction and unconditional extraction are in
[BLUE_INDUCTION_DRAFT.md](./BLUE_INDUCTION_DRAFT.md). The full source-line
audit, local comparison theorem, exact error scales, and minimal missing lemma
are in [EXACT_COMPANION_AUDIT.md](./EXACT_COMPANION_AUDIT.md). The exact
pre-coarsening coefficient is now propagated against the frozen source
ledger; it has not been identified with Lin--Niu's symbol
$\rho_{\rm HMS}(D)$ or the optimized HMS appendix comparator.

## Evidence labels

- **[PUBLISHED]** peer-reviewed or version-of-record result.
- **[PREPRINT-THEOREM]** theorem in the latest primary-source preprint.
- **[PREPRINT-CLAIM / AUDIT GAP]** claimed theorem whose inspected proof has
  an unresolved source-to-formula alignment gap.
- **[SOURCE-REMARK]** claim or proposed extension stated without a full proof.
- **[DERIVED]** algebra proved in this route from stated assumptions.
- **[COMPUTED]** reproducible numerical output, not a proof.
- **[CONJECTURE]** proposed missing lemma or mechanism.
- **[FAILED]** tested idea with an explicit obstruction.
- **[OBSTRUCTION]** a rigorously excluded proof mechanism, without excluding
  the target theorem by other mechanisms.

## Current primary-source baseline

| Regime | Current result | Proof mechanism | Evidence |
|---|---|---|---|
| $R(3,k)$ | $R(3,k)\ge(1/2+o(1))k^2/\log k$ | two random base graphs, projection/blow-up, then triangle-edge deletion | **[PREPRINT-THEOREM]** Hefty--Horn--King--Pfender, [arXiv:2510.19718v3](https://arxiv.org/abs/2510.19718) |
| fixed $s\ge3$ | $r(s,k)\ge\Omega_s(k^{s-1}/(\log k)^{2s-4})$ | polarity graph, $T_s$-free digraph, count forward-independent tuples, sample | **[PREPRINT-THEOREM]** Bradač, [arXiv:2605.28793v3](https://arxiv.org/abs/2605.28793) |
| $R(\ell,C\ell)$, fixed $C>1$ | first exponential improvement over Erdős | random sphere graph | **[PREPRINT-THEOREM]** Ma--Shen--Xie, [arXiv:2507.12926v2](https://arxiv.org/abs/2507.12926); later sources report Inventiones acceptance, not independently used here |
| same regime | cleaner Gaussian construction and better quantitative bound; for large $C$, base $e^{1/24+o(1)}p_C^{-1/2}$ | Gaussian random geometric graph, reverse Bartlett induction | **[PREPRINT-THEOREM]** Hunter--Milojević--Sudakov, [arXiv:2512.17718](https://arxiv.org/abs/2512.17718) |
| same regime | claims that red upper-truncation improves the HMS exponent by a positive $D^{-2}$ term | sharp cumulant generating function plus a $P_D\to1$ Hölder split | **[PREPRINT-CLAIM / AUDIT GAP]** Lin--Niu, [arXiv:2605.25843v2](https://arxiv.org/abs/2605.25843); their claimed HMS $1/2$ companion disagrees with the HMS source coefficient $1$ |

### Baseline correction that mattered

The May 2026 v1 abstract of Bradač gave only $k^{s-2+o(1)}$. The authoritative
June 16 v3 theorem is stronger:

$$
r(s,k)\ge\Omega_s\!\left(\frac{k^{s-1}}{(\log k)^{2s-4}}\right).
$$

Therefore “recover the missing polynomial exponent” is stale. The fixed-$s$
target is now the polylogarithmic loss.

## Cut A: complete the omitted blue truncated-Gaussian refinement

### Invariant object

The object which survives both colors is

$$
\rho_D(p)=\min\{\rho_R(p,D),\rho_B(p,D)\},
$$

the smaller normalized clique-avoidance exponent. Improving one color alone
moves the balancing density $p$; improving both raises the crossing itself.

### Exact local quantities

Let $\Phi(-c_C)=p_C$, $a_C=\phi(c_C)$, and

$$
\lambda_C=\frac{Cp_C}{Cp_C+1-p_C}.
$$

The upper- and lower-truncation variance deficits are, respectively,

$$
\gamma_R=\frac{a_C}{p_C}\left(\frac{a_C}{p_C}-c_C\right),
\qquad
\gamma_B=\frac{a_C}{1-p_C}\left(\frac{a_C}{1-p_C}+c_C\right).
$$

Both are positive. With

$$
\beta_R=\frac{\gamma_Ra_C^4}{8p_C^4},
\qquad
\beta_B=\frac{\gamma_Ba_C^4}{8(1-p_C)^4},
$$

the two-sided $D^{-2}$ coefficient is

$$
K_2(C)=\lambda_C\beta_R+(1-\lambda_C)C^3\beta_B.
$$

This $K_2$ is the **variance-only coefficient relative to the new
unit-Hölder baseline**. The exact HMS source audit instead gives the local
candidate

$$
\widetilde K_2(C)
=\lambda_C\frac{(1+\gamma_R)a_C^4}{8p_C^4}
+(1-\lambda_C)C^3
\frac{(1+\gamma_B)a_C^4}{8(1-p_C)^4}.
$$

**[DERIVED PATHWISE, RELATIVE TO A FROZEN HMS MAIN-BODY LEDGER]** The extra
$1$ in each numerator is the gain from replacing HMS's $P=2$ Cauchy split by
$P_D\to1$. The paired reverse induction is proved in
**PAIRED_COMPANION_ATTEMPT.md**. Turning $\widetilde K_2$ into a comparison
with a published final HMS constant still requires the open comparator
bridge; it is not included in the numerical table below.

**[DERIVED]** The $C^3$, rather than $C^4$, follows because the blue
probability term $-\beta_B(C\ell)^4/d$ is normalized by $C\ell^2$. The
crossing weights follow from the slopes $-1/(2p_C)$ and
$C/(2(1-p_C))$.

### Numerical size of the omitted term

The following values come from **double_truncation_gain.py**. Each coefficient
multiplies $D^{-2}$.

| $C$ | red contribution $\lambda_C\beta_R$ | omitted blue contribution $(1-\lambda_C)C^3\beta_B$ | blue/red |
|---:|---:|---:|---:|
| 1.01 | 0.01639870 | 0.01633730 | 0.9963 |
| 1.1 | 0.01891102 | 0.01824348 | 0.9647 |
| 1.5 | 0.03107429 | 0.02664817 | 0.8576 |
| 2 | 0.04784829 | 0.03669592 | 0.7669 |
| 5 | 0.15933563 | 0.08264847 | 0.5187 |
| 10 | 0.33940692 | 0.12381434 | 0.3648 |
| 100 | 2.08342501 | 0.14455211 | 0.0694 |

**[COMPUTED]** These values compare against the new unit-Hölder companion,
not against the literal HMS $P=2$ expansion. Near $C=1$, the continuous limit has
$\beta_R=\beta_B=1/\pi^3$ and equal crossing weights, so using both colors
doubles the second-order improvement. For finite moderate $C$, the omitted
blue term remains material. This table does not establish uniformity as
$C\to\infty$.

### Sign and normalization audit

1. **[DERIVED]** Blue adjacency conditions on $Z\ge-c_C$, so the relevant law
   is lower truncated; its variance is strictly below one.
2. **[DERIVED]** The HMS blue quadratic exponential has a positive
   coefficient. Replacing the unit subgaussian proxy by the smaller centered
   variance reduces its upper bound, hence produces a negative correction in
   log clique probability and a positive correction in the Ramsey exponent.
3. **[SOURCE-REMARK]** Lin--Niu state the local lower-truncated CGF lemma and
   the coefficient $\beta_B=\gamma_Ba^4/[8(1-p)^4]$, but do not write the
   induction.
4. **[DERIVED]** In the blue Hölder decomposition, every standardized linear
   tilt is $O_{p,C}(D^{-1})$, so the lower-truncated CGF window applies for
   fixed $C$. The resulting perfect-sequence reverse induction is written in
   **BLUE_INDUCTION_DRAFT.md**.
5. **[DERIVED]** The standard greedy extraction preserves the order-$r^4/d$
   gain for $r=\Theta_C(\ell)$: discarded-vector probabilities are
   exponentially small in $\ell$, while the quartic replacement costs only
   $O_{p,C}(\ell u/D^2)$ for $u$ discarded vertices.
6. **[DERIVED]** The exact source comparison fails at the claimed baseline:
   HMS has coefficient $1$, while the Lin--Niu unit-Hölder companion has
   coefficient $1/2$. The local saving relative to HMS is therefore
   $(1+\gamma_B)a^4/[8(1-p)^4]$, not merely
   $\gamma_Ba^4/[8(1-p)^4]$.
7. **[DERIVED, FROZEN-LEDGER COMPARATOR]** The exact local comparison
   propagates through a pathwise paired reverse induction when the exact
   $A_i$ are retained and all common order-$r^4/d$ terms are charged once.
   **[OPEN]** Identify this ledger with a unique published/final HMS
   comparator, especially the optimized appendix constant.

### Perfect-sequence proposition now obtained

Prove the following fixed-$C$ proposition:

> **Blue propagation proposition, perfect-event version [DERIVED, relative
> to the unit-Hölder companion].** For
> $d=D^2\ell^2$,
> $1\le r\le C\ell$, and fixed $C,p$, the starred blue clique probability
> $P^*_{\mathrm{blue},r}$ admits its unit-proxy companion expansion with the
> additional term
>
> $$
> -\beta_B(p)\frac{r^4}{d}
> +O_{p,C}(D^{-1})\frac{r^4}{d}
> +o_\ell(r^4/d).
> $$

The induction is proved first for $P_{\mathrm{blue},r}^*$, the blue clique
probability intersected with the perfect-sequence event. For
$r=\Theta_C(\ell)$, the source's greedy extraction removes the star with only
a $1+o(1)$ multiplicative factor. It requires no new construction. The paired
HMS-versus-refined companion lemma now closes against a frozen main-body
ledger. The remaining theorem-level issue is that simply naming that ledger
“the HMS final constant” is unsupported: the published comparator is not
uniquely defined at this precision, and the optimized appendix follows a
different induction.

## Cut B: reduce Bradač's fixed-$s$ logarithmic loss

### Where the loss is created

Set $t=s-1$. In Bradač's forward-independent-tuple tree, the proof has

$$
\Delta\asymp q^{2t-1},\qquad h\asymp_t q^t,
\qquad w\asymp_t q\log q,
$$

and uses the generic tree estimate

$$
N_k\le 2^k\Delta^w h^{k-w}.
$$

The overhead is

$$
(\Delta/h)^w=\exp(\Theta_t(q\log^2q)).
$$

It can be absorbed into $O_t(1)^k$ only when
$k\gtrsim_t q(\log q)^2$. Choosing $q\asymp k/(\log k)^2$ then gives the
published $(\log k)^{2s-4}$ denominator.

### Tested type-sensitive potential and its obstruction

Suppose an unmarked step of type $\ell$ has fanout

$$
O_t(q^{t-\ell}|U_\ell|),
$$

while its potential shrinks as

$$
|U_\ell(i)|\le q^t e^{-ci/q}.
$$

Relative to the marked fanout $h\asymp q^t$, $j$ such steps contribute at most

$$
\exp\left((t-\ell)j\log q-\frac{c}{2q}j(j-1)\right).
$$

The exponent is maximized at

$$
j=(1+o(1))\frac{t-\ell}{c}q\log q
$$

and its value is

$$
(1+o(1))\frac{(t-\ell)^2}{2c}q\log^2q.
$$

**[FAILED]** Thus the naive type-sensitive multiplicative potential still has
exactly the old $q\log^2q$ entropy. The calculation is reproduced by
[bradac_entropy_obstruction.py](./bradac_entropy_obstruction.py). Potential
decay alone is not a breakthrough.

### The removal-block proposal and its exact obstruction

For an unmarked child of type $\ell$, Bradač's source argument supplies a
literal block

$$
R\subseteq U_\ell^\sigma\setminus U_\ell^{\sigma'},
\qquad |R|\ge |Z_\ell^\sigma|/(16q).
$$

**[DERIVED]** These blocks are permanent and pairwise disjoint along a path.
If $d_R=\dim\operatorname{span}R$, exact projective counting gives only

$$
|R|\le\frac{q^{d_R}-1}{q-1},
\qquad
d_R\ge\left\lceil\log_q((q-1)|R|+1)\right\rceil,
$$

and this conversion is sharp.

**[OBSTRUCTION]** There is an actual consistent `D^*(t,q)` history, for every
prime power $q$ and fixed $t\ge2$, followed by `q` consecutive unmarked
children whose removal blocks are distinct singletons while their union has
rank two.  Thus disjointness, block size, or naive additive rank cannot supply
the missing entropy saving.  See [NEXT_LOWER_BOUND.md](./NEXT_LOWER_BOUND.md)
for the construction and source-line dependency map.

The formerly proposed uniform transverse record lemma is itself now refuted:
there are $\Theta_t(q\log q)$ all-unmarked type-zero paths whose total excess
over $(C_tq^t)^k$ is $\exp(\Omega_t(q\log^2q))$.  A viable replacement would
need a sufficiently large length threshold, a tail-entropy cancellation, or
non-uniform weights.  If such a stronger mechanism were proved, the existing
sampling argument could still conditionally yield

$$
r(s,k)\ge\Omega_s\!\left(\frac{k^{s-1}}{(\log k)^{s-2}}\right).
$$

No such replacement is proved.  The saturation family rules out the literal
removal-block shortcut and the uniform record formulation; it does not show
that the logarithmic target is false.

The follow-up cross-type audit gives the exact transition

$$
U_j^{\sigma(a,b)}=U_j^\sigma\setminus R_j^\sigma(a,b).
$$

Thus a promoted point leaves only its old-rank cutoff; nesting cannot be
charged as simultaneous progress in several layers.  A root child is a strict
counterexample to universal multi-layer contraction, and after one such step
there are still $[t]_q$ marked children while $|U_0|=q^t$, including a
state-neutral loop.  The exact Markov state is the full incidence family
$y\mapsto W(y)$; cutoff cardinalities alone are not closed under transfer.
The rank-zero construction rules out source-type diversification only through
$\lfloor(t-1)q\log q/12\rfloor$; eventual diversification at a larger
$A_tq\log q$ threshold remains open.  These statements passed independent
review after this quantifier boundary was corrected.  See
[CROSS_TYPE_TRANSFER_ATTEMPT.md](./CROSS_TYPE_TRANSFER_ATTEMPT.md) and
[INDEPENDENT_CROSS_TYPE_REFEREE.md](./INDEPENDENT_CROSS_TYPE_REFEREE.md).

## Why $R(3,k)$ is not the first target

Hefty--Horn--King--Pfender explicitly observe that their construction's
independence number and average degree match those of a random graph of the
same density. Any constant above $1/2$ would require a graph that is both
sparser and has smaller independence number than the corresponding random
graph. They and earlier authors conjecture $1/2$ is asymptotically sharp.

**[ASSESSMENT]** A direct attempt to beat $1/2$ is therefore lower priority
than completing the blue Gaussian lemma or reducing Bradač's polylog loss.
The two-stage “ensure one side, then repair forbidden structures” idea remains
useful for finite constructions, but no honest asymptotic constant gain has
been derived from it here.

## Cross-route transfer

- **From finite constructions:** the “other-side first, bounded repair later”
  pattern motivates the compound deficit encoding rather than monotone
  $H$-free maintenance. The current naive potential audit shows exactly why an
  ordered repair certificate is needed.
- **From the upper-bound route:** its strict separation between search and a
  certified verifier should be copied. Here the search object is a candidate
  CGF/charging inequality; the verifier should check interval bounds for
  truncated-normal cumulants or exact finite-$q$ tuple counts independently.
- **Back to finite constructions:** the lower-bound polarity graphs provide
  algebraic seeds and rank/deficit state descriptors that may reduce the
  search space for explicit Ramsey graphs.

## Ranked next actions

### Controlled-residual mean-ledger promotion checkpoint

The residual-gradient identity, strong-concavity square completion, exact
$K_r$ multiplicities, three-factor centered-MGF costs, enlarged reverse
induction, extraction, and
$\widehat H_*(C)\sim1/(64\log C)$ rate term have passed an independent
source-level referee and a secondary `yes/high` result-to-claim gate.  The
remaining community-facing gate is external human review and archival of the
pinned source snapshots and immutable proof package; there is still no
effective numerical $C_0$ or priority claim.

1. **Highest probability:** obtain an external line-by-line referee replay of
   **HISTORY_WEIGHT_OPTIMIZATION_NEXT.md**, its exact-merge predecessor, and
   **HMS_APPENDIX_BRIDGE.md**, then archive the proof and source snapshots.
2. **Highest upside:** seek a quotient or domination inequality retaining
   enough of the full $y\mapsto W(y)$ incidence state to control the transfer
   operator, or prove eventual source-type diversification after a sufficiently
   large $A_tq\log q$ threshold.  Cardinality-only and universal common-
   contraction arguments are now ruled out.
3. **Computational bridge:** exact-count small $D^*(2,q)$ and $D^*(3,q)$
   states to identify which extension types dominate and whether bounded
   uphill repair has empirical support.
4. **Claim boundary:** the large-`C` appendix theorem and weighted-ledger
   extension are locally proved but are not externally peer reviewed or
   published; distinguish HMS's latent constant slack from the genuinely new
   $G_*(C)$ and $\widehat H_*(C)$ terms.  The Bradač audits give rigorous
   obstructions to the naive potential, literal removal-block, and uniform
   transverse-record mechanisms, but no improved lower bound and no
   impossibility theorem.

## Cross-route audit: GNNW Lemma 14 and the $.03$ iteration

Full proof and source-line map:
[GNNW_LEMMA14_AUDIT.md](./GNNW_LEMMA14_AUDIT.md). Certified arithmetic:
[gnnw_hull_counterexample.py](./gnnw_hull_counterexample.py).

### Verdict

**[FAILED]** In Gupta--Ndiaye--Norin--Wei,
[arXiv:2407.19026v1](https://arxiv.org/abs/2407.19026v1), source line 460
reverses an algebraic comparison. With $E=e^\alpha$ and
$a=E(1-x)$, the ratio of its alleged left and right sides is

$$
\frac{x^{-k}a^{-\ell}}{x^{-\ell}a^{-k}}
=\left(\frac ax\right)^{k-\ell}\geq1,
$$

not at most one. The exact rational instance
$(\alpha,x,k,\ell)=(0,2/5,2,1)$ gives $125/12>125/18$.

**[DERIVED]** Applying the lemma's premise to *all* $k,\ell$, including its
symmetric orientation, certifies the fixed-pair envelope

$$
Y_{\rm legal}(x)=
\min\{E(1-x),1-x/E\}
=
\begin{cases}
1-x/E,&x\leq E/(1+E),\\
E(1-x),&x\geq E/(1+E).
\end{cases}
$$

The paper/Notebook instead uses $E(1-x)$ below $1/2$ and $1-x/E$ above
$1/2$, i.e. the strictly larger branch on both outer ranges. This proves
that the stated premise does not justify the region curve used in the
positive-$\alpha$ iterations. It does not prove those points are outside the
true Ramsey region.

### Explicit downstream failure

**[COMPUTER-CERTIFIED]** At the first positive-$\alpha$ update

$$
(\alpha_1,\beta_1)=\left(\frac{.09}{e},.045\right),
\qquad \lambda=1,
$$

200-bit Arb arithmetic gives $X=0.2359152801\ldots$ and, with the corrected
branch $Y=1-Xe^{-\alpha_1}$,

$$
\psi_1(1)=-0.0113676165227075063\ldots<0.
$$

The entire Arb ball is negative. Hence the analytic condition on source line
480 fails, whereas the paper's larger branch gives
$\psi_1(1)=0.0001844423\ldots>0$. The recursive $.045\to.033\to.03$ chain
therefore does not start after the hull is corrected; the $.03$ conclusion is
not established by this argument as written. Choosing a smaller allowed $X$
cannot fix this point: on the relevant branch the varying log term is
$\log[X(1-X/e^{\alpha_1})]$, which is increasing throughout
$0<X\leq0.235916<e^{\alpha_1}/2$.

### What remains unaffected

**[DERIVED: dependency audit]** The initial $(\alpha_0,\beta_0)=(0,.08)$
stage does not use Lemma 14. Source line 481 invokes the elementary
$(X,1-X)\in\mathcal R$ observation, and at $\alpha=0$ both candidate branches
equal $1-X$. Thus this particular defect leaves the $.08$ starting stage
unchanged. This is a dependency verdict, not an independent all-$\lambda$
certification of the notebook computation.

### Minimal repair target

Either prove an independent Ramsey-region lemma placing the larger outer
branches in $\mathcal R$, or re-optimize and uniformly certify
$F,\alpha,\beta$ against $Y_{\rm legal}$. Merely changing the cutoff from
$1/2$ to $E/(1+E)$ is insufficient: the branches must also be swapped.
