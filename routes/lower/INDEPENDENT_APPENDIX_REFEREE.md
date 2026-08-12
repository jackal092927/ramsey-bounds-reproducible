# Independent referee report on `HMS_APPENDIX_BRIDGE.md`

Date: 2026-08-12

## Verdict

**YES for the stated corrected red theorem; NO for a same-Hölder blue
improvement (as the bridge itself says).** I found no fatal gap in the red
appendix bridge, its extraction, or the resulting fixed- \(C\) Ramsey-rate
claim. The first claimed obstruction on the blue side is real.

This is an existential asymptotic result, not an effective numerical theorem:
the source leaves absolute constants inside \(O(\cdot)\) and \(o(1)\)
unwritten. Consequently the audit validates the quantifier

\[
   \exists C_0\ \forall C\ge C_0\ \exists \ell_0(C)\ \forall \ell\ge
   \ell_0(C),
\]

but it does **not** certify a numerical value of \(C_0\).

The earliest fatal gap is therefore: **none in the red theorem as stated**.
The earliest failure of a stronger, two-sided claim is the blue quadratic
moment feasibility condition at HMS lines 1105--1116, compounded by the fact
that the cited Lin--Niu CGF lemma has the wrong one-sided direction for the
lower-truncated blue variable.

## Material checked

I read the complete bridge and its arithmetic script. Their SHA-256 hashes
are, respectively,

- `8d38003528d53d62589eb6ab0e960e29a494788bfe74bf23f871ee81d6732944`;
- `86c8feb83246b986ba41c41ec62091b6efdd3c392cc4f46037ac3ff2d208ecc8`.

I independently downloaded both arXiv v2 source archives. The relevant TeX
files matched the hashes stated in the bridge:

- HMS, `arXiv_version.tex`:
  `b72958ac35554eccb94dedab5800349d2c021af7d60f767125cb46998e0fd54a`;
- Lin--Niu, `off-diagonal-Ramsey-R.tex`:
  `dbf1bfa2c7603c81b2e56a97028b138ccf9a9299a3d1f20c0b08cf489136f429`.

The local script passes, but I used it only as an arithmetic check, not as
evidence for the probabilistic steps.

## Claim-by-claim findings

### 1. Cutoff window and positivity of \(c_R(C)\): YES

For a red-perfect history HMS line 1208 and Cauchy--Schwarz give

\[
 |b_i-c_p|
 \le {\alpha_R^2\ell\over\sqrt d}+d^{-1/5}
 \le {2\alpha_R^2\over D}
 =\omega_C
\]

once \(C\) is fixed and \(\ell\) is sufficiently large. Here the first
projection is onto a subspace of the projection appearing in red-perfectness,
so the use of that event is legitimate. The ceiling in \(d\) only improves
the inequality because \(\sqrt d/\ell=D_\ell\ge D\).

As \(C\to\infty\), writing \(L=\log(1/p)\),

\[
 m_0\sim\sqrt{2L},\qquad
 D\sim4\sqrt2 L^{3/2},\qquad
 \omega_C=O(L^{-1/2}),\qquad Q_C\sim L/2.
\]

Thus the entire cutoff interval tends to \(+\infty\), the truncated variance
there tends uniformly to zero, \(P_C\to1\), and
\(\kappa_C=1-P_Cv_+/2>0\) eventually. This proves the required existential
\(C_0\) for \(c_R(C)>0\). It does not provide a numerical \(C_0\); doing so
would require explicit Mills-ratio inequalities throughout, which the bridge
does not claim to supply.

### 2. Hölder/CGF scaling and the HMS coefficient: YES

Stopping the proof of HMS Lemma 2.6 at lines 906--909, before its last
Cauchy--Schwarz estimate, gives exactly

\[
 H_s=\lambda\mathbb ES+{\lambda^2\over d}\sum_i A_i^2
       +{4|\lambda|k\over d}.
\]

The coefficient of \(\sum_iA_i^2\) is **one**, not one half. The square root
in HMS line 903 turns the exponent \(2\lambda^2\sum A_i^2/d\) into the
displayed coefficient one.

For \(X_i=Z_i/\sqrt d\) truncated at \(Z_i\le-b_i\), its centered part is
\(Y_i/\sqrt d\). Hence the standardized CGF argument is

\[
 u={P_C\lambda A_i\over\sqrt d}>0,
\]

not \(P_C\lambda A_i\). Lin--Niu lines 499--537 apply for every real cutoff
and every positive \(u\), and yield

\[
 {P_C\lambda^2\over2d}\sum_i v_R(b_i)A_i^2.
\]

The quadratic Hölder factor is legal since, for every \(k\le\ell\),

\[
 4Q_C|\lambda|k
 \le {D\ell\sqrt d\over2}\le d/2<d.
\]

After taking the \(Q_C\)-th root, its remainder is still
\(4|\lambda|k/d\). All powers of \(d\), \(P_C\), and \(Q_C\) in the bridge
are therefore correct.

### 3. Pathwise deficit: YES

Both moment bounds concern the same conditional history, the same means
\(\mu_i\), and the same \(A_i\). Their deterministic mean and quadratic
remainder cancel before either history is coarsened. Therefore

\[
 H_s-R_s={\lambda^2\over d}\sum_i
 \left(1-{P_Cv_R(b_i)\over2}\right)A_i^2.
\]

On the cutoff window all means are negative and
\(|A_i|\ge(k-1)m_-/\sqrt d\). Since \(\lambda^2/d=m_0^2\), this gives exactly

\[
 R_s\le H_s-{c_R(C)\over d}k(k-1)^2.
\]

This is a genuine upper-envelope improvement; it does not incorrectly
subtract the difference of two unrelated upper bounds.

### 4. Reverse induction and indices: YES, with one harmless convention

At induction state \(s\), \(k=r-s\), the already accumulated sum is
\(\sum_{t=1}^{k-1}\mathsf d_t\). Exposing column \(s\) introduces the moment
with exactly \(k\) future variables and therefore \(\mathsf d_k\). The state
at \(s-1\) has \(k+1\) remaining vertices and accumulated sum
\(\sum_{t=1}^{k}\mathsf d_t\). At \(s=0\) this is
\(\sum_{t=1}^{r-1}\mathsf d_t\), as claimed.

The clean base case is \(s=r-1\), \(k=1\), rather than writing a formally
awkward sum ending at \(-1\) for \(k=0\). This is only a presentation repair;
the deficit is zero and the induction is unchanged.

The finite identity

\[
 \sum_{k=1}^{r-1}k(k-1)^2
 ={r(r-1)(r-2)(3r-5)\over12}
\]

is correct.

### 5. Extraction, including every deletion count \(u\): YES

For red extraction the appendix's projection tail supplies, uniformly at
each rejected index, \((p/10)^{10\ell}\); the norm tail using the larger blue
\(\delta\) is smaller. Sequential conditioning justifies multiplying these
uniform rejection probabilities.

For \(u\) deletions,

\[
 \Delta_2\le\ell u,\qquad \Delta_3\le\ell^2u/2,
\]

and

\[
 0\le\mathcal D_C(\ell)-\mathcal D_C(\ell-u)
 \le {4c_R(C)\over D^2}\ell u.
\]

For sufficiently large \(C\), the cubic restoration costs at most
\(\ell u\) and the deficit restoration costs at most \(\ell u\). Together
with the edge cost, the remaining exponent is

\[
 \eta_C\ell u,\qquad
 \eta_C=10\log(10/p)-\log(1/p)-2>0.
\]

Consequently
\((1+e^{-\eta_C\ell})^\ell-1=o(1)\), uniformly over the full sum
\(1\le u\le\ell\).

The bridge now treats the small retained-set endpoints explicitly. HMS's
underlying reverse-induction proposition is stated for every \(r\ge1\), so
the strengthened induction gives (22) directly for \(r=1,2\). For \(r=0\)
the bridge declares
\(P^*_{R,0}=\mathcal H_C(0)=1\) and \(\mathcal D_C(0)=0\). Hence (23e) is
formally available for every \(1\le u\le\ell\); the endpoint issue identified
in the first referee pass is **fixed**.

### 6. Ceiling and floor: YES

With \(d=\lceil D^2\ell^2\rceil\),

\[
 D_\ell={\sqrt d\over\ell}=D+O_C(\ell^{-2}).
\]

All finite-\(\ell\) feasibility inequalities use \(D_\ell\ge D\); all rate
formulas replace \(D_\ell\) by \(D\) only after taking \(\ell\to\infty\).
No gain is lost and no equality at finite \(\ell\) is being assumed.

For \(q_\ell=\lfloor C\ell\rfloor\), HMS's blue proposition applies directly
because \(q_\ell\le C\ell\). Since \(q_\ell/\ell=C+O(\ell^{-1})\), every
quadratic and cubic normalized term changes by \(o(1)\). The floor is thus
legitimate.

### 7. First-moment constants and the bottleneck: YES

Normalizing the red log first moment by \(\ell^2\) gives

\[
 \rho< -{1\over2}\log p_C+{B_R(C)\over2}
       +{c_R(C)\over4D^2},
\]

where the factor \(1/2\) in \(B_R/2\) comes from
\(\binom\ell2/\ell^2\), and
\(\mathcal D_C(\ell)/\ell^2\to c_R/(4D^2)\).

For blue cliques, normalizing by \(\ell^2\) and then dividing the first
moment condition by \(q_\ell/\ell\to C\) gives

\[
 \rho< -{1\over2}\log p_C+{C B_B(C)\over2}.
\]

Thus the factors \(C\) in \(B_B\) are correct; there is no missing \(C\) or
extra \(C\). Independently expanding the definitions yields

\[
 B_R(C)=1/6+o(1),\qquad C B_B(C)=1+o(1).
\]

Also

\[
 c_R(C)=(4+o(1))L^2,qquad D^2=(32+o(1))L^3,
\]

so

\[
 {c_R(C)\over4D^2}={1+o(1)\over32\log C}.
\]

The red constraint is therefore strictly smaller than the unchanged blue
constraint for all sufficiently large fixed \(C\). The theorem does not need
a blue improvement.

### 8. Frozen \(O\)-constant: logically sound but non-effective

HMS line 973 explicitly declares the Appendix-B \(O(\cdot)\) constants
absolute. Hence one may take one finite absolute \(K\) dominating the red
one-step estimates and set

\[
 \theta_C=1-K{\sqrt{\log(1/p)}\over D}.
\]

Because \(\sqrt{\log(1/p)}/D=O(1/\log C)\), \(\theta_C>0\) eventually for
every such frozen \(K\). Weighted merging of the one-step cubic errors does
not make \(K\) grow with \(r\) or \(\ell\).

This validates the frozen-ledger theorem (T), but the source never gives a
numerical value for \(K\), and its final red/blue comparisons also retain
unspecified \(o(1)\) terms. Therefore neither this audit nor the bridge can
claim an explicit numerical \(C_0\) without redoing those source estimates
with effective constants. This is the main open quantitative risk, not a
logical gap in the existential claim.

### 9. Blue same-Hölder claim: NO, correctly excluded

At \(r=C\ell\), the optimized HMS tilt is

\[
 \mu=m_B(1-\gamma_B/2).
\]

Quadratic-moment feasibility after a Hölder split forces

\[
 Q\le {1\over1-\gamma_B/2},
\]

whereas positivity of a variance-style deficit relative to the exact HMS
coefficient forces

\[
 Q>{2\over1+\gamma_B}.
\]

These intervals are disjoint when \(0<\gamma_B<1/2\), in particular in the
large-\(C\) regime. This central-history calculation is sufficient to block
the proposed mechanism.

There is an additional directional caveat: reflecting a lower-truncated blue
variable turns the needed positive blue CGF argument into the **negative**
direction for an upper-truncated variable, while Lin--Niu Lemma 499--537 is
only the positive-direction inequality. A local Taylor CGF could address the
direction for fixed parameters, but it cannot repair the incompatible
\(Q\)-interval at HMS's minimal \(D\). Thus the bridge's negative blue verdict
is sound, although calling the feasibility condition the sole "earliest"
issue understates this separate directional prerequisite.

## Exact status and dependencies

1. **Red perfect-history bridge:** proved, conditional only on the two hashed
   v2 source lemmas and the explicit red-perfect cutoff bound.
2. **Passage to unconditional red probability:** proved, including the now
   explicit \(r=0,1,2\) extraction endpoints.
3. **Frozen-ledger theorem (T):** proved for sufficiently large fixed \(C\),
   with existential absolute \(K\).
4. **Public consequence (A) and every fixed \(\eta<1/12\) consequence (C):**
   proved with the same order of quantifiers.
5. **Attributable improvement:** exactly the positive term
   \(c_R(C)/(4D^2)\); the improvement from \(1/24\) to \(1/20\) is pre-existing
   HMS slack and is correctly not attributed to the bridge.
6. **Same-method blue improvement:** not proved and, at minimal \(D\), blocked
   by the displayed feasibility/positivity incompatibility.

## Remaining risks

- No effective numerical \(C_0\) is available until the absolute HMS
  \(O\)-constant and the later \(o(1)\) comparisons are made explicit.
- The source preprints themselves are not peer-reviewed here beyond the
  exact lemmas used in this bridge; this report does not reprove the full
  Gaussian random-graph construction from first principles.
- A future claim of a two-sided improvement would require a genuinely new
  blue quadratic-moment argument or a re-optimization with \(D>4aC/(1-p)\).

Subject to those stated limitations, the red theorem is ready to be cited as
an independently replayed, existential fixed-\(C\) result.
