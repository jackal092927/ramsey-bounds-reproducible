# Second-round adversarial review of the repaired lower-bound component

Date: 2026-08-30  
Review mode: read-only mathematical audit; no source component was edited  
Files reviewed:

- `papers/lower/sections/02_setup.tex`
- `papers/lower/sections/03_rigidity.tex`
- `papers/lower/sections/04_residual.tex` (needed to close the dependency chain)
- `papers/lower/sections/05_ledger.tex`
- `papers/lower/sections/06_induction.tex`
- `papers/lower/sections/07_rate.tex`
- `papers/lower/appendices/A_full_source_proof.tex`
- `papers/lower/appendices/B_bridge_record.tex`
- `routes/lower/HISTORY_WEIGHT_OPTIMIZATION_NEXT.md`
- `routes/lower/history_weight_optimization_next_check.py`

The pinned HMS and Lin--Niu source snapshots were downloaded afresh through
`scripts/fetch_external_sources.py`.  Their SHA-256 values agree with the
manifest and the manuscript:

- HMS v2: `b72958ac35554eccb94dedab5800349d2c021af7d60f767125cb46998e0fd54a`;
- Lin--Niu v2: `dbf1bfa2c7603c81b2e56a97028b138ccf9a9299a3d1f20c0b08cf489136f429`.

The route ledger and checker also reproduce their printed hashes:

- ledger: `2234a769d7798a79174cbfb362ada64f5d760aefbe7e6d4fb8763cd5633a0312`;
- checker: `616040b91aad4becf92dcfbe13b7e6d49a3c9c73f0f222ba56114104f1c7d554`.

The checker was rerun.  All four large-$C$ snapshots, the controlled
recursion, residual-gradient identity, exact $K_r$ identity, sampled Hessian,
sampled exact-CGF increment, and approach to
$64\log(C)\widehat H(C)=1$ passed.  As its own docstring correctly says, this
is an arithmetic/sample check and not a verification of the source
reverse-induction interface.

## Executive verdict

| Original issue | Post-repair status | Short reason |
|---|---|---|
| L1: undefined source quantities and circular interface | **PARTIAL** | The analytic parameters are now defined, and the interface no longer imports the Ramsey conclusion.  However, the source probability state and weighted induction invariant are still not defined formally enough to be a theorem hypothesis. |
| L2: $p_C$ versus $p$ cutoff mismatch | **CLOSED** | Every occurrence relevant to the window now uses $p=p_C+1/C$, and the open-window order $w\downarrow\omega_0$ is stated correctly. |
| L3: three-factor H\"older and same-history bridge | **PARTIAL** | The local factorization, exponents, $16/3$ cost, three CGF error terms, and one-charge separation are correct.  The bridge from the pinned source's pre-Cauchy allocation to the new weighted invariant is still asserted in prose rather than stated as an exact imported invariant. |
| L4: extraction and red--blue crossing | **PARTIAL** | The restoration inequalities, binomial sum, first moments, and $5/12+o(1)$ gap are now derived correctly.  The external events/probabilities used by (S4)--(S5) remain undefined, and the source-line map for (S4) is inaccurate. |
| L7: exact-merge uniqueness/rescaling | **PARTIAL** | The effective triangular array is uniquely determined, and the unsupported edge-dependent claim has been removed.  The remaining global-scalar sentence is ambiguous and its proof, as written, conflates a normalized array with an effective scaled coefficient. |
| L8: narrow $1/64$ cap | **PARTIAL** | The pointwise optimization is correct and the constructed residual attains it to leading order.  The quantified objective called “leading contribution” is not formally defined, and the admissible-class conditions refer back to construction-specific bounds without a normalized functional. |

The repairs close the numerical and local analytic gaps.  They do **not** yet
turn the lower component into a standalone publication-grade proof, because
the exact source-to-weighted-induction implication remains a prose interface.

## 1. Audit of (S1)--(S5)

### 1.1 Non-circularity

The revised interface is materially better than the previous version.  In
particular, (S1)--(S5) do not explicitly assume (1.1), the new residual term,
the first-moment conversion, or the red--blue comparison.  Thus there is no
literal assumption of the displayed Ramsey conclusion.

There remains a closure problem distinct from literal circularity.  An exact
conditional induction statement is not among (S1)--(S5).  In particular,
(S3) imports “the source scalar terms whose empty-state target is (2.12)” and
says that the projection identity is linear in future coefficients, but it
does not display:

1. the red-perfect event and filtration;
2. the conditional state being bounded at exposure $i$;
3. the weighted projection potential in that state;
4. the precise induction hypothesis for every target $r$ and every
   deterministic triangular array $T$;
5. the one-step identity that turns the future coefficients $T_{jq}$ and
   boundary coefficients $T_{ij}$ into the next state; or
6. the base-state formula whose scalar part is exactly $\mathcal H_C(r)$.

Linearity makes the proposed generalization plausible and, after reconstructing
the HMS calculation, I found no sign obstruction.  Nevertheless, a reader
cannot derive (6.3) from the literal text of (S3).  The missing object is a
formal weighted reverse-induction lemma, not another numerical estimate.

### 1.2 Precision of each source item

**(S1): PARTIAL.**  The cutoff distribution and the corrected $p$-based
window are stated.  The inequalities agree with HMS red-perfectness and the
cutoff approximation.  However, $h_{ij}$ is never defined in the paper, nor
are the filtration, the range of $i,j,r$, and the exact conditioning event.
The phrase “on a red-perfect exposure history” is not a mathematical
definition.

**(S2): PARTIAL.**  Conditional independence, centering, and the
$1$-subgaussian proxy are the correct scaled source facts.  The sentence that
the square-MGF estimate is valid “at every argument used below” is not an
exact quantified hypothesis.  The usable imported statement should instead
give the inequality

$$
\log \mathbb E e^{x\zeta_j^2}\le \frac{16}{3}x,
\qquad 0\le x\le\frac18,
$$

under the named conditioning, together with the uniform-quadratic estimate
used for the $Q_0$ factor.  The latter is currently stated only later as “the
unchanged HMS factor.”

**(S3): PARTIAL and the principal theorem-closure blocker.**  It is not
logically circular, but it is not exact enough.  The local paper verifies the
gradient, Hessian, H\"older, and deterministic mass calculations.  It does not
write the source conditional invariant to which those calculations are
attached.  A formal lemma with the full weighted projection exponent is the
minimal repair.

**(S4): PARTIAL.**  Once the displayed inequality is granted, the manuscript's
restoration and subset sum are correct.  But $p_I$ and $P^*_{R,q}$ are not
defined as events/probabilities, and the admissible range of $u$ and the
retained-order relabeling are not part of the assumption.  Moreover, Appendix
B cites HMS lines 400--410 and 1294--1321 for this statement.  Lines
1294--1321 are final bookkeeping and do not contain the optimized red failure
factor.  The relevant optimized change is at HMS lines 955--971, combined
with the extraction argument at lines 385--410.  The claimed
$(p/10)^{10\ell u}$ factor is consistent with those passages, but the printed
source-line map is wrong.

**(S5): PARTIAL.**  The displayed blue probability exponent agrees with the
pinned source after the $d^{-1/5}\binom q2+q$ terms are absorbed into
$o_C(\ell^2)$.  However, $P_{B,q}$ and the underlying random-coloring event
are not defined, and the quantifier/uniformity represented by $o_C(\ell^2)$
is not stated.  This is repairable by defining the probability space and
writing, for each fixed $C$, an explicit error sequence
$\epsilon_{C,\ell}\to0$.

### 1.3 Remaining undefined symbols and states

The deterministic analytic notation is now largely complete.  In particular,
$p,c,a,D,D_\ell,m,v,K_b,\psi_b,B_R,B_B,G_*,\widehat H_*$ are all defined.
The remaining source-state notation that must be defined before publication
is:

- $h_{ij}$ and the projection with respect to which it is computed;
- the filtration/exposed matrix state at step $i$;
- “red-perfect” and “blue-perfect” sequences/events;
- $P^*_{R,r}$, $P_{R,r}$, and $P_{B,r}$;
- $p_I$ and the greedy extraction map producing $I$; and
- the exact weighted conditional invariant used in reverse induction.

## 2. L2: the cutoff window

**Status: CLOSED.**

The corrected definitions are

$$
p=p_C+\frac1C,
\qquad
\alpha_R=10\sqrt{\log(10/p)},
\qquad
\omega_0=\frac{100\log(10/p)}D.
$$

These agree with the proof ledger and checker.  The finite-$\ell$ cutoff is
only shown to lie in $[c-w,c+w]$ for fixed $w>\omega_0$, which is the correct
open-window statement.  The proof then fixes $C,w$, sends $\ell\to\infty$,
and only afterwards sends $w\downarrow\omega_0$.  This avoids claiming that
a finite history lies in the closed limiting window.

There is a presentational quantifier slip in Section 7: the phrase “as
$C\to\infty$ and then $w\downarrow\omega_0$” reverses the operational order.
The formula for $\widehat H_*(C)$ itself uses the right order, so this does not
change the value; it should nevertheless be rewritten as: first take the
right limit in $w$ for each fixed $C$, then study $C\to\infty$.

## 3. L3: three-factor H\"older and the same-history deficit

### 3.1 Exact factorization

The identity (5.7)--(5.9) is correct.  With

$$
X_j=\frac{\zeta_j-m(b_j)}{\sqrt d},
\qquad T_{jq}=t_0+\Delta_{jq},
$$

direct expansion gives exactly the deterministic mean term, the centered
linear tilt $u_j^0+\delta u_j$, the uniform quadratic factor, and the
$\Delta$-quadratic factor printed in (5.8).  No cross term is missing.

### 3.2 Conjugate exponents and the $16/3$ constant

The choices

$$
Q_0=\frac d{4t_0k},\qquad
Q_1=\frac d{4R_i},\qquad
\frac1P+\frac1{Q_0}+\frac1{Q_1}=1
$$

are exact.  Under (5.11), $Q_0,Q_1>1$ and $1<P\le2$.  The inequality

$$
-\sum_{j<q}\Delta_{jq}\zeta_j\zeta_q
\le \frac12\sum_jR_j\zeta_j^2
$$

is valid because $\Delta_{jq}\ge0$.  Since
$Q_1R_j/(2d)\le1/8$, conditional independence and the square-MGF bound give

$$
\frac1{Q_1}\sum_j\frac{16}{3}\frac{Q_1R_j}{2d}
=\frac{16}{3}\frac{S_i}{d},
$$

using $\sum_jR_j=2S_i$.  Thus the constant $16/3$ is derived correctly.

### 3.3 The three linear-CGF errors

I checked (5.18)--(5.25) directly.

- $0\le K_b''\le1$ yields
  $[K_b(P(u+\delta))-K_b(Pu)]/P\le2u\delta+\delta^2$ for
  $1<P\le2$.
- Convexity and $K_b(0)=K_b'(0)=0$ yield
  $0\le\partial_P[K_b(Pu)/P]\le u^2$ (indeed a factor $1/2$ would also
  suffice).
- $P-P^0=PP^0/Q_1\le16R_i/d$ follows from $P,P^0\le2$.
- The bounds on $\sum\delta u_j$, $\max\delta u_j$, and
  $\sum(u_j^0)^2$ give exactly the three summands of
  $\widehat L_w(C)$.

I found no reversed inequality or missing constant in this local comparison.

### 3.4 Same-history separation

The local separation is now convincing: (5.16)--(5.17) account for the old
uniform exact-CGF deficit, (5.26) accounts for the new $\Delta$ factor and
the change $P^0\to P$, and (4.6) pays the residual gradient.  Hence there is
no local double counting of $G_*(C)$.

The remaining reason for a **PARTIAL** rather than **CLOSED** status is the
source boundary.  The manuscript must make the source pre-Cauchy allocation
$\sum_j(u_j^0)^2$ and the $Q_0$ uniform-quadratic estimate explicit parts of
the imported conditional invariant.  Appendix B currently asserts that
stopping the HMS calculation at the right line gives this allocation; it
does not state a theorem whose conclusion can be substituted into (5.16).

## 4. L4: reverse induction, extraction, and crossing

### 4.1 Deterministic reverse-induction charge

Conditional on a formal weighted source invariant, the accumulated charge is
correct.  Summing $S_i$ and $e_{ij}^2$ gives

$$
\sum_iS_i\ge2A_0\binom r4+\theta K_r,
\qquad
\sum_{i<j}e_{ij}^2=\theta^2K_r,
$$

so the net exponent is precisely

$$
\mathcal N_{C,w,d}(r)
=\frac1d\left[2\widehat B_wA_0\binom r4+E_wK_r\right].
$$

The discretization envelope $J_{r,d}$ also has the correct sign and order.

### 4.2 Restoration and binomial sum

The old exact-CGF restoration (6.5), the binomial-difference bounds (6.6),
and the source-envelope ratio (6.8) have the correct directions.  For
sufficiently large $C$, both the old and new added deficits cost at most
$\ell u$.  Therefore

$$
\eta_C=10\log(10/p)-\log(1/p)-3>0
$$

and

$$
\sum_{u=1}^{\ell}\binom\ell u e^{-\eta_C\ell u}
=(1+e^{-\eta_C\ell})^\ell-1=o(1)
$$

are exact.  This closes the old missing-binomial-sum objection.

Two small precision repairs remain:

1. (6.7) uses $o_C(1)$ where the discarded $\binom\ell2/d$ contribution is
   naturally $O_C(1/\ell)$ after normalization by $\ell u$.  The limit is
   harmless, but the subscript should be corrected or the exact bound kept.
2. The inequalities $0\le\mathcal N(\ell)-\mathcal N(\ell-u)$ use
   $\widehat B_w,E_w>0$.  Eventual positivity is proved in Section 7, but it
   should be declared before (6.7), by enlarging $C_0$ once.

### 4.3 First moments and red--blue gap

The red and blue first-moment thresholds (7.2) and (7.4) follow from the raw
probability rates with the correct factors of $C$.  The identities involving
$B_R$ and $B_B$ use
$\log p_C=C\log(1-p_C)$ correctly.  The asymptotic comparison

$$
\frac{CB_B(C)}2-
\left(\frac{B_R(C)}2+G_*(C)+\widehat H_*(C)\right)
=\frac5{12}+o(1)>0
$$

provides the required constant-order crossing gap.  The prior argument based
only on an added $o(1)$ has been repaired.

The status remains **PARTIAL** solely because the probabilities and source
events entering (S4)--(S5), and the weighted invariant needed for (6.3), are
not formally defined.  The local extraction and crossing algebra themselves
are closed.

## 5. L7: exact-merge uniqueness and scaling

The core coefficient comparison is sound.  Requiring

$$
\partial_jF_i(c\mathbf1)\sqrt d\,h_{ij}=-W_{ij}h_{ij}
$$

for every boundary variable forces (3.3), and decreasing the first endpoint
makes the system triangular.  Thus the normalized effective array is unique.
The previous unsupported statement about arbitrary edge-dependent rescalings
has been deleted, which is a substantive repair.

The remaining global-scale paragraph should still be changed.  If the entire
potential is multiplied by $\kappa$, that common factor cancels from the
coefficient comparison, so the **normalized** array continues to obey (3.3).
If instead one calls $W=\kappa T$ the effective coefficient, then its affine
recursion has base term $\kappa m_0\sqrt d$, not $m_0\sqrt d$.  The current
proof says both that $W=\kappa T$ and that this effective $W$ again satisfies
(3.3), which is not literally true unless $\kappa=1$ or the connection term
has simultaneously been renormalized and the normalized variable is renamed.

Minimal repair: state uniqueness after fixing the coefficient of
$\sum_j\log\Phi(-b_j)$ to one.  A global multiplication of the whole
inequality is then only a presentation equivalence and is not a new effective
array.  With that weakening, L7 is **PROVABLE AS STATED**.

## 6. L8: the admissible scalar cap

The pointwise calculation is correct.  For a direct residual $e_{ij}$, an
upper bound of the form

$$
\beta_w(i-1)e_{ij}-\frac{e_{ij}^2}{2\mu}
\le\frac{\mu\beta_w^2}{2}(i-1)^2
$$

is valid.  Within the scalar proof device,
$\beta_w\le m_0^2[1+o(1)]$ and any uniform scalar concavity constant obeys
$\mu\le1+o(1)$.  The feedback operator has norm $\rho=o(1)$ under the stated
growth control, so it changes the $m_0^4r^4$ numerator only by $o(1)$ in
relative terms.  Adding the baseline numerator $m_0^4$ and the optimal
residual numerator $m_0^4/2$ gives the claimed $3m_0^4/2$, hence $1/64$.
The concrete choice $e_{ij}=m_0^2(i-1)$ attains this asymptotically.

The proposition is nevertheless not yet a formal extremal theorem:

1. “leading contribution” is not defined as a limit or limsup functional of
   a family $e^{(C,\ell,r)}$;
2. (A2) refers to recursion (4.2), where $e_{ij}$ was already fixed to the
   particular choice $\theta(i-1)$, rather than stating the generalized
   recursion with a variable admissible input;
3. (A3) refers to (5.11) and its construction-specific $a_+$ rather than
   giving a uniform row-norm condition for the general family; and
4. (A4) assumes the extraction loss has the desired order, but the constant
   and its uniformity over $r,u,\ell$ are not quantified.

These are scope/formalization gaps rather than a counterexample to the
$1/64$ calculation.  A minimal corrected proposition should define the
normalized residual contribution, take a supremum over families satisfying
explicit constants independent of $C,\ell,r$, and state the generalized
recursion.  Under that correction, the proof supports the cap.

## 7. Checker boundary

The checker is internally consistent with the repaired formulas and passed
unchanged.  It should not be described as certifying any of the following:

- the HMS or Lin--Niu source-line implications;
- the weighted reverse-induction invariant;
- all cutoff histories or the full Hessian box (it samples one nonconstant
  configuration; the full-box result is analytic);
- the extraction union over source events;
- the first-moment conversion or red--blue crossing; or
- the method cap over an infinite admissible class.

The manuscript's current statement that the checker is an arithmetic witness
rather than a replacement for the probabilistic proof is accurate.

## 8. Minimal repair set

No new numerical search is needed.  The smallest proof-level repair is:

1. Define the Gaussian probability space, red/blue clique events,
   red/blue-perfect events, filtration, $h_{ij}$, $P^*_{R,r}$,
   $P_{R,r}$, $P_{B,r}$, and $p_I$.
2. Replace (S3) by a formal weighted reverse-induction interface displaying
   the full conditional invariant and projection identity for arbitrary
   deterministic triangular $T$ fixed before exposure.
3. Put the pre-Cauchy allocation $\sum_j(u_j^0)^2$, the $Q_0$ quadratic
   estimate, and their exact ranges into (S2)--(S3).
4. Correct the (S4) source-line map to include HMS 955--971 and define its
   retained-set quantifiers.
5. Replace the $o_C(1)$ in (6.7) by an exact or correctly subscripted term and
   declare $\widehat B_w,E_w>0$ before using monotonicity.
6. Normalize the global-scalar uniqueness statement.
7. Define the limiting functional and generalized admissible class in the
   method-cap proposition.

## 9. Final proof-writer verdict

### Source-relative Ramsey theorem (1.1)

**PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION.**

The numerical value and the local residual proof survive.  A complete theorem
follows after replacing the prose source interface by an exact weighted
reverse-induction hypothesis and defining its probability states.  Under that
formal interface, the repaired H\"older ledger, extraction, and first-moment
steps prove

$$
\liminf_{\ell\to\infty}\frac1\ell
\log R(\ell,\lfloor C\ell\rfloor)
\ge -\frac12\log p_C+\frac{B_R(C)}2+G_*(C)+\widehat H_*(C).
$$

### Local controlled-residual contribution

**PROVABLE AS STATED, conditional on the formal source invariant.**

The recursion, full-box Hessian bound, square completion, deterministic mass,
three-factor comparison, same-history separation, and asymptotic calculation
support

$$
\widehat H_*(C)=\frac{1+o(1)}{64\log C}>0.
$$

### Exact-merge claim

**PROVABLE AFTER WEAKENING.**  Fix the normalization of the connection term
and claim uniqueness of the resulting triangular coefficient array.  Do not
identify a globally scaled effective array with a solution of the same affine
recursion without also scaling its base term.

### Narrow scalar method cap

**PROVABLE AFTER WEAKENING / FORMAL DEFINITION.**  The $1/64$ pointwise cap is
supported for the intended scalar class, but the class and its normalized
leading functional must be stated independently of the particular optimizer.

### Overall publication decision for the lower component

**NOT YET ACCEPTABLE AS A STANDALONE PROOF; ACCEPTABLE AS A SOURCE-RELATIVE
CONDITIONAL RESULT AFTER THE MINIMAL INTERFACE REPAIR ABOVE.**  I found no
arithmetic or local analytic counterexample to the $1/64$ coefficient.  The
remaining blocker is theorem closure at the pinned source boundary, not the
controlled-residual calculation itself.

---

## Round-2 repair disposition (2026-08-30)

This disposition records the state after implementing the minimal repair set
above.  It supersedes the issue statuses in the earlier read-only audit, but
does not erase that audit's historical findings.  The repair deliberately
does **not** turn the source-relative theorem into an unconditional theorem.

### S1--S5 and the weighted invariant

| Item | Disposition after repair | Exact boundary |
|---|---|---|
| S1 | **CLOSED AS A FORMAL SOURCE HYPOTHESIS** | The Gaussian/Bartlett space, diagonal-first filtration, $h_{ij}$, $A_i^R$, exact $b_{ij}$, and the red-admissible history event $\mathfrak H^R_{r,s}$ are defined with all $r,i,j,s$ quantifiers. |
| S2 | **CLOSED AS A FORMAL SOURCE HYPOTHESIS** | The conditioning is named; the centered variables are defined; the square-MGF range $0\le x\le1/8$, the $Q_0$ estimate, and the pre-Cauchy allocation $\sum_j(u_j^0)^2$ are displayed. |
| S3 | **CLOSED AS A FORMAL EXTRA ASSUMPTION** | Equations (2.32)--(2.41) define $\mathcal P_s^T$, $\mathcal K_i^T$, the one-step premise, the full conditional invariant, the law of total probability, both projection identities, and the scalar baseline.  S3 is still explicitly identified as a weighted extension, not as a theorem stated verbatim in HMS or Lin--Niu. |
| S4 | **CLOSED AS A FORMAL SOURCE HYPOTHESIS** | $\Gamma_R$, $p_I$, $P^*_{R,r}$, the retained-order relabeling, and every $0\le u\le\ell$ are defined. |
| S5 | **CLOSED AS A FORMAL SOURCE HYPOTHESIS** | $P_{B,r}$ and the blue clique event are defined, and the old $o_C(\ell^2)$ is replaced by an explicit sequence $\epsilon_{C,\ell}\to0$ for fixed $C$. |

The reverse-induction state is now

$$
\mathbb P(I_s\cap B^R_r\mid\mathcal F_s)
\le \mathcal H_C(r-s)
\exp\!\left[-\mathcal P_s^T-
\sum_{i=s+1}^{r-1}\lambda_i\right].
$$

On histories outside $\mathfrak H^R_{r,s}$ its left side is zero.  On an
admissible history, the identities for $\mathcal P_i^T$ and
$\mathcal P_{i-1}^T$ turn the kernel bound into the preceding state by exact
reverse induction.  This closes the former undefined-state objection, while
preserving S3 as an explicit trust-boundary assumption.

### Source-line map disposition

The refreshed, hash-checked source files support the following map:

- HMS 145--170 and 443--498: Gaussian graph, Bartlett representation,
  exposure state, edge/perfect events;
- HMS 955--971 and 1192--1218: optimized red perfectness and cutoff control;
- HMS 330--354 and 878--935: subgaussian, square-MGF, and centered-moment
  inputs;
- HMS 1192--1289: red conditional induction, total probability, and
  projection merge;
- HMS 385--410 together with 955--971: greedy extraction and the optimized
  red failure factor.  The former erroneous extraction citation to
  1294--1321 is not used;
- HMS 977--1181 and 1294--1312, together with 385--410: unchanged blue
  induction and extraction;
- Lin--Niu 359--493 and 499--537: truncated-variance monotonicity and the
  positive-direction cumulant formula/bound.

The Yang--Mao v1 hash was independently checked against the manifest.  It is
an upper-component dependency and supplies no lower-component statement, so
the lower source map intentionally assigns it no line range.

### L7 and L8 disposition

**L7: CLOSED for the normalized claim.**  Proposition 3.1 fixes the
coefficient of $\sum_j\log\Phi(-b_j)$ to one before asserting uniqueness.
Remark 3.2 distinguishes this normalized array from the effective coefficient
$W^{\rm eff}=\kappa W$, whose affine base is
$\kappa m_0\sqrt d$.  No edge-dependent rescaling claim remains.

**L8: CLOSED only for the explicitly delimited conditional class.**
Definition 7.1 now fixes class-wide constants $M_0,M_{\rm ext}$, states the
generalized recursion and row feasibility, requires an exact scalar Hessian
certificate and one-step kernel certificate, defines the normalized
functional $\mathcal G_{\mathcal E}$ and $\operatorname{Lead}_C$, and
quantifies the positive extraction loss.  Proposition 7.2 proves

$$
\limsup_{C\to\infty}64\log C\,
\mathfrak M_{M_0,M_{\rm ext}}(C)\le1
$$

for every fixed pair of admissibility constants, and verifies that the
constructed family attains one for some fixed absolute pair.  This is not a
claim about adaptive weights, matrix-valued completion, higher-order
potentials, sharper source MGFs, or all conceivable Ramsey methods.

### Verification and final proof-writer verdict

The lower component was independently built with

```text
cd papers/lower
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The final build succeeds and produces a 28-page PDF.  Its log has no LaTeX
errors, unresolved references/citations, duplicate labels, PDF-string
warnings, or overfull boxes; all PDF fonts are embedded.  A separate
label/reference set comparison found no missing or duplicate label, and
rendered spot checks covered the title/abstract, probability-state
definitions, method-cap definition, source appendix, and final references.
The full `bash scripts/reproduce_lower.sh` run also passed and ended with
`LOWER_THEOREM_REPRODUCED`.

Final statuses:

- **Source-relative Ramsey theorem (1.1): PROVABLE AFTER WEAKENING / EXTRA
  ASSUMPTION.**  The minimum remaining condition is the explicit S1--S5
  interface, especially the separately stated weighted rule S3 and the frozen
  scalar baseline.  It is not an unconditional theorem.
- **Local controlled-residual ledger, extraction algebra, and red--blue
  crossing: PROVABLE AS STATED, conditional on S1--S5.**
- **Normalized exact-merge uniqueness: PROVABLE AS STATED** in its repaired
  normalization.
- **The $1/64$ method cap: PROVABLE AS STATED only within Definition 7.1 and
  conditional on its one-step/extraction certificates.**  No global
  optimality follows.

Accordingly, the lower component is publication-grade as an explicitly
source-relative conditional result.  It remains unsuitable for presentation
as a source-independent unconditional Ramsey theorem unless S3 and the
version-pinned source hypotheses are proved inside the manuscript.
