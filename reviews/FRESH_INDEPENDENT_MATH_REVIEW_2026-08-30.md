# Fresh Independent Adversarial Mathematical Review

> **Later closure.** This report is retained as a review of its stated
> snapshot. A subsequent targeted reconstruction proved S3 locally and removed
> it from the assumption boundary; see
> `reviews/LOWER_S3_CLOSURE_2026-08-30.md`. Statements below requiring S3 as an
> extra hypothesis are therefore historical.

**Manuscript:** *Reproducible Ramsey Analysis Across Asymptotic and Finite Regimes: Retained Spines, Gaussian Residuals, and Proof-Carrying Barriers*  
**Artifact reviewed:** `papers/unified/main.pdf` (79 pages) and the corresponding current source and verification code  
**Review date:** 2026-08-30  
**Review mode:** Fresh, read-only, adversarial mathematical audit  
**Independence statement:** The mathematical arguments were rechecked from the manuscript, pinned source interfaces, and proof code. Existing conclusions in `reviews/` were not used as premises for the verdicts below.

Page numbers in this report refer to the current 79-page unified PDF.

## 1. Executive decision

The review found:

- **Fatal issues:** 0
- **Major issues:** 0
- **Minor issues:** 1 terminological issue at two occurrences; both occurrences have now been corrected and rematerialized

No theorem statement, numerical constant, proof architecture, or headline bound required mathematical revision at this snapshot.  The lower S3 scope in the next table is historical: S3 was subsequently proved locally, while S1, S2, S4, and S5 remain source assumptions.  The finite result must still not be promoted to an exact radius or a global improvement of \(R(3,18)\).

## 2. Headline verdicts

| Headline claim | Verdict | Required scope |
|---|---|---|
| Theorem 3.1, \(R(k,k)\le \exp((U(1)-3.4754\times10^{-6})k+o(k))\le(3.780685290)^{k+o(k)}\) | **PROVABLE AS STATED** | Only under source interface 4.2, the repaired BookCor/rate induction, Theorem 5.1, and Arb containment semantics, exactly as stated in the manuscript |
| Theorem 10.1, the fixed-ratio lower bound | **HISTORICAL SNAPSHOT: PROVABLE AS STATED** as the manuscript's conditional theorem | At this stage it required all of source interface 11.2, including S3; the later closure proves S3 locally |
| Theorem 10.1 interpreted without its source boundary as an unconditional Ramsey improvement | **PROVABLE AFTER WEAKENING OR EXTRA ASSUMPTION** | The current safe theorem remains source-relative under S1, S2, S4, and S5, with S3 proved locally |
| Theorem 19.3, the fixed-seed barrier \(\rho(H)\ge7\) | **PROVABLE AS STATED** | Requires the six semantically reconstructed CNFs and their checked DRAT refutations |
| \(\rho(H)=7\), a seven-deletion repair, a 100-vertex \((3,18)\)-Ramsey graph, or \(R(3,18)\ge101\) | **NOT CURRENTLY JUSTIFIED** | All exact-seven branches remain `UNKNOWN` |

## 3. Trust-boundary map

The verdicts above are mathematical verdicts relative to explicitly delimited interfaces. They are not claims of proof-assistant formalization.

| Result | Locally checked mathematical content | Imported or computational trust boundary | Claims not licensed by that boundary |
|---|---|---|---|
| Diagonal upper bound | Exact-diagonal reduction, analytic tail, moment/tail conversion, retained-spine max--min transfer, outer endpoint reductions, and theorem-to-certificate logic | Version-pinned Yang--Mao regularization/book/compatibility interfaces; repaired BookCor induction in Appendix B; six-stage Arb interval containment and exact handoffs | An effective threshold in \(k\), global optimizer status, proof-assistant formalization, or an unconditional result independent of the imported interfaces |
| Fixed-ratio lower bound | Hessian estimate, boundary square completion, nonexchangeable triangular ledger, same-history CGF comparison, multiplicity identities, extraction algebra, red--blue crossing, and the scalar-family cap | **Historical snapshot:** source items (S1), (S2), (S4), and (S5), plus S3 as an extra hypothesis; **current:** the same four source items, local S3 proof, and the non-effective source constant entering \(C_0\) | A source-independent unconditional lower bound, a finite-\(\ell\) threshold, a common-normalization comparison not proved in the paper, or global optimality of \(1/64\) |
| Fixed-seed deletion barrier | CNF implication direction, all-pairs variable semantics, deletion-budget accounting, branch cover, and theorem assembly | Content-addressed seed/cut banks, PySAT equality-counter semantics, the six frozen CNF identities, the six DRAT traces, and the pinned DRAT checker | \(\rho(H)=7\), existence or nonexistence at budget seven, a remote 100-vertex construction, or a new global bound on \(R(3,18)\) |

## 4. Upper-bound audit

### 4.1 Exact-diagonal reduction

Lemma 6.3 appears on p.14, equations (U4.8)--(U4.10). Its sign split is complete.

- If both inputs are negative, both odd parts are negative, so \(F(x,y)<0=F(0,0)\).
- If \(x<0\le y\), the term \(G(x)H(y)\) is nonpositive. The root-filter estimate gives \(H(x)\le2\), hence
  
  \[
  F(x,y)\le G(y)H(x)\le2G(y)\le2G(y)H(y)=F(y,y).
  \]
- If \(0\le x\le y\), monotonicity of \(G\) and \(H\) bounds both summands by \(G(y)H(y)\).

Thus the two-dimensional envelope reduces validly to

\[
F(z,z)=2G(z)H(z)=H(z)^2-H(z)H(-z),\qquad z\ge0.
\tag{U4.10}
\]

No sign case or boundary case is missing.

### 4.2 Lemma 6.4: compact interval and analytic half-line

Lemma 6.4 is on p.15, equations (U4.11)--(U4.12). Set \(z=u^3\), \(w=(u^3+u_0^3)^{1/3}\), and

\[
D_0=\frac{88053}{10^9}.
\]

The compact interval \(0\le u\le20\) is an explicitly computational obligation: 131,072 exact rational cells are evaluated at 512-bit precision with outward-rounded Arb balls, with reported minimum slack greater than \(4.2687\times10^{-6}\). This part is valid relative to Arb's containment semantics.

For the half-line \(u\ge20\), write \(H(u^3)=1+aP(u)^2\). Since

\[
H(-u^3)=1+aE(-u^3)^2\ge1,
\]

one has

\[
\begin{aligned}
H(u^3)^2-H(u^3)H(-u^3)
&=H(u^3)\bigl(H(u^3)-H(-u^3)\bigr)\\
&\le H(u^3)\bigl(H(u^3)-1\bigr)\\
&=aP(u)^2+a^2P(u)^4.
\end{aligned}
\]

Using

\[
|P(u)|\le\frac{e^u}{3}\left(1+2e^{-3u/2}\right),
\qquad w\ge u,
\]

gives exactly (U4.12):

\[
\frac{H(u^3)^2-H(u^3)H(-u^3)}{e^{4w}}
\le
\frac a9e^{-2u}\left(1+2e^{-3u/2}\right)^2
+\frac{a^2}{81}\left(1+2e^{-3u/2}\right)^4.
\tag{U4.12}
\]

Both terms are strictly decreasing. For the first term, its logarithmic derivative is

\[
-2-
\frac{6e^{-3u/2}}{1+2e^{-3u/2}}<0;
\]

the derivative of the second term is also strictly negative because it is a positive fourth power of \(1+2e^{-3u/2}\). At \(u=20\), the right-hand side is below

\[
8.805216326983\times10^{-5}<D_0,
\]

with strict slack greater than \(8.3673\times10^{-10}\). Therefore the endpoint closes the complete half-line.

**Verdict for Lemma 6.4:** **PROVABLE AS STATED**, with the compact part explicitly inside the manuscript's Arb trust boundary. No fatal or major issue was found.

### 4.3 Separator and moment-to-tail conversion

The separator is Lemma 6.2 on p.14, equations (U4.6)--(U4.7). The exact identity

\[
F(-t,y)=\frac{H(-t)}2\bigl((2-R)H(y)-H(-y)\bigr)
\]

combined with \(R>2+2\sigma_0\) and \(H(\pm y)\ge1\) yields the stated negative separator. The sign is correct.

Lemma 6.5 and Proposition 6.6, pp.15--16, use nonnegative Taylor coefficients and tensorization to prove

\[
\mathbb E[Z_1^rZ_2^s]
=\left\|\mathbb E\bigl[\sigma_1(U)^{\otimes r}\otimes
\sigma_2(U)^{\otimes s}\bigr]\right\|^2\ge0.
\]

The layer-cake step (U4.16)--(U4.17) has the correct direction: failure of both correlation alternatives supplies an upper tail bound, which forces the positive contribution below the negative separator budget and contradicts nonnegative expectation. The exact rational inequality (U4.15) leaves strict slack.

### 4.4 Retained-spine max--min direction

Theorem 4.3 is on pp.11--12. The relevant definitions are (U2.8)--(U2.13):

\[
C^*=\max_{\sigma\in[0,1]^2}\min\{D(\sigma),B(\sigma)\},
\qquad B(\sigma)=\max\{P(\sigma),Q(\sigma)\}.
\]

For each fixed \(\sigma\):

- If \(D(\sigma)\le B(\sigma)\), then \(D(\sigma)=\min\{D,B\}\le C^*\), so (U2.14) supplies the direct residual Ramsey threshold.
- If \(B(\sigma)<D(\sigma)\), then \(B(\sigma)=\min\{D,B\}\le C^*\). Since \(B=\max\{P,Q\}\), both \(P\le C^*\) and \(Q\le C^*\), supplying the page and reservoir inequalities respectively.

Thus the proof uses `max min` in the correct direction. It neither substitutes `min max` nor reverses the order inequality.

### 4.5 Outer certificate and endpoint derivatives

Proposition 7.1 is on pp.17--18, equations (U5.2)--(U5.6). Concavity at one gives the tangent inequality

\[
U(1)-D(x,y)\ge xA+(y-x)E,
\tag{U5.3}
\]

so the direct branch applies outside the closed triangle \(W\).

For the red page,

\[
\partial_xP_R=c_\eta-U'(z)<0,
\qquad
\partial_yP_R=c_\eta-U(z)+zU'(z)>0.
\]

It is therefore sufficient to follow the sloping side. Its derivative is \(B(z)\), with

\[
B'(z)=(sz-1)U''(z)>0.
\]

Along the side, \(z\) decreases from \(z_a\). Hence \(B(z)\le B(z_a)<0\), and the red-page expression decreases away from \((0,r_a)\). Equation (U5.4) is therefore the correct endpoint.

For the blue page, the negative \(y\)-derivative reduces the maximum to \(y=x\). With \(v=\tau/(1-x)\),

\[
\Gamma'(v)=vU''(1-v)<0.
\]

Since \(v\) increases with \(x\) and \(\Gamma(\tau)<0\), the diagonal expression decreases and is maximized at \(x=0\), as asserted in (U5.5). Finally, \(Q\) is coordinatewise increasing, so its maximum on \(W\) is \(Q(r_d,r_d)\), equation (U5.6).

All endpoint reductions and derivative directions are correct.

### 4.6 Six-stage certificate correctness

Theorem 5.1 is on p.12. The theorem-to-certificate implication is Proposition C.2 on p.62, with the decisive finite-grid argument in (U-C.C.8)--(U-C.C.10).

The audit checked the following logical chain:

1. The small-\(\lambda\) region is closed analytically by the Erdős--Szekeres recursion and Stirling's formula.
2. On a compact interval \(I=[\rho,1]\), the certificate supplies a finite descending grid with the correct one-sided derivative and envelope inequalities.
3. In the high red-density branch, the repaired balanced-book corollary supplies the required red or blue clique.
4. In the complementary branch, a blue neighborhood has at least the next induction threshold, and the induction is taken in the smaller clique order.
5. The first certificate uses an independently established elementary prior.
6. Each of the remaining five stages requires exact target-to-prior equality, not approximate numerical compatibility.
7. The code paths in `routes/upper/verify_arb.py` and `routes/upper/verify_chain_arb.py` implement the same region inequalities, candidate extrema, and exact handoffs used by Proposition C.2.

No circularity, reversed region test, or unproved approximate handoff was found. The six-stage conclusion is therefore valid within the repaired BookCor and Arb containment boundary stated by Theorem 5.1.

## 5. Fixed-ratio lower-bound audit

### 5.1 Logical status of source interface 11.2

Theorem 10.1 is on p.20, equations (L1.1)--(L1.2). Source interface 11.2 is on pp.25--27.

The manuscript correctly distinguishes the source items:

- (S1), (S2), (S4), and (S5) are attributed to the version-pinned HMS and Lin--Niu source material.
- (S3), equations (L2.37)--(L2.40), is explicitly identified as the additional weighted-extension hypothesis required by this manuscript and is not represented as a theorem stated verbatim in either source.

Accordingly, the conditional theorem under (S1)--(S5) is **PROVABLE AS STATED**. Any presentation that deletes (S3), attributes it to HMS or Lin--Niu without proof, or calls (L1.1) an unconditional Ramsey improvement would instead be **PROVABLE AFTER WEAKENING OR EXTRA ASSUMPTION**.

### 5.2 Hessian and boundary residual

Lemma 13.1 is on p.28, equations (L4.4)--(L4.6). The full-box Hessian estimate uses the displayed second derivatives and Gershgorin with the correct signs. The tangent expansion at the boundary retains the negative quadratic term, and scalar square completion gives

\[
e_{ij}\delta_j-\frac{\mu_w}{2}\delta_j^2
\le\frac{e_{ij}^2}{2\mu_w}.
\]

After substituting \(\delta_j=\sqrt d\,h_{ij}+\varepsilon_{ij}\), the full coefficient \(T_{ij}h_{ij}\) merges into the projection potential, while only the explicit square and cutoff residuals remain. The inequality direction in (L4.6) is correct.

### 5.3 Exact multiplicities and three-factor comparison

Lemma 14.1 is on p.29, equations (L5.4)--(L5.5). Exchanging the order of summation gives the exact multiplicities:

\[
K_r=\sum_{i=1}^{r-1}(r-i)(i-1)^2
=\binom r3+2\binom r4,
\]

\[
\sum_{i=1}^{r-1}S_i\ge2A_0\binom r4+\theta K_r,
\qquad
\sum_{1\le i<j\le r}e_{ij}^2=\theta^2K_r.
\]

The future-degree contribution counts each ordered quadruple twice, while \(e_{ij}=\theta(i-1)\) yields the second identity exactly.

The three-factor Hölder split, pp.29--31, uses \(Q_0\), \(Q_1\), and \(P\) with

\[
Q_0^{-1}+Q_1^{-1}<\frac12,
\]

so all exponents exceed one. Nonnegativity of \(\Delta\) gives the square domination (L5.13), and the stated square-MGF bound yields precisely the \(16/3\) cost in (L5.15). No independence is used beyond the conditional independence stated in (S2).

### 5.4 Same-history accounting

The critical accounting appears on pp.31--32:

- old exact-CGF deficit: (L5.16)--(L5.17);
- comparison of \(P^0\) and \(P\): (L5.18)--(L5.25);
- new increment cost: (L5.26).

The old deficit is first defined on the same conditional history and with the same cutoffs \(b_j\):

\[
d_i(b)=\sum_j\left[(u_j^0)^2-
\frac1{P^0}K_{b_j}(P^0u_j^0)\right].
\tag{L5.16}
\]

The cutoff window, monotonicity of \(\psi_b\), and

\[
\sum_{q\ne j}m_q\ge(k-1)m_w
\]

give the deterministic same-history lower bound \(d_i(b)\ge d_{k,w,d}\), equation (L5.17).

Only after fixing that old charge does the proof compare the new linear factor with the old term. Equations (L5.18)--(L5.25) separately pay for the change \(P^0\to P\) and for the incremental tilts \(\delta u_j\). Equation (L5.26) then records only the new increment factor and the \(P\)-change:

\[
-\widehat B_w(C)\frac{S_i}{d}.
\tag{L5.26}
\]

The old exact-CGF term, the increment Hölder term, and the boundary square-completion term are therefore disjoint. No contribution is charged twice, and no estimate is transferred between different conditional histories.

### 5.5 Reverse induction and extraction

The deterministic one-step exponent is (L6.2) on p.32:

\[
\lambda_i=d_{k,w,d}
+\widehat B_w(C)\frac{S_i}{d}
-\sum_{j>i}\frac{e_{ij}^2}{2\mu_wd}
-\frac{d^{-1/5}}{\sqrt d}\sum_{j>i}T_{ij}.
\tag{L6.2}
\]

All coefficients are deterministic and fixed before column \(i\) is exposed. The exact projection identities preserve all future \(T_{jq}\), while the boundary estimate contributes each new edge coefficient \(T_{ij}\). Thus the implication in (S3) applies without an exchangeability assumption, producing (L6.3) on p.33.

The deletion/restoration estimates (L6.5)--(L6.12) correctly charge the old CGF term, the new deterministic term, the source envelope, and the specified extraction factor. The binomial summation is in the correct direction and the accumulated restoration cost is \(o_C(\ell^2)\) after the stated fixed-\(C\), \(\ell\to\infty\) limit.

### 5.6 Red--blue crossing and the \(1/64\) coefficient

The red--blue comparison culminates in (L7.9) on p.35. The first-moment thresholds and the red/blue source bonuses are compared in the same normalization; the \(5/12\) asymptotic gap has the correct sign.

The leading asymptotics on p.36 are

\[
m_0^2=(2+o(1))\log C,
\qquad
D^2=(32+o(1))(\log C)^3,
\tag{L7.10}
\]

and

\[
\widehat B_wA_0=(4+o(1))(\log C)^2,
\qquad
E_w=(2+o(1))(\log C)^2.
\tag{L7.11}
\]

Substitution into (L2.23) gives

\[
\widehat H_*(C)
=\frac{(6+o(1))(\log C)^2}
{12(32+o(1))(\log C)^3}
=\frac{1+o(1)}{64\log C}.
\tag{L7.12}
\]

The quantifier order is essential: \(C\) is first fixed and sufficiently large, then \(\ell\to\infty\), and only afterward is the \(C\to\infty\) leading coefficient evaluated. The source constant makes the threshold \(C_0\) existential rather than effective.

### 5.7 Scope of the scalar method cap

Definition 16.1 and Proposition 16.2 appear on pp.36--39. The cap

\[
\limsup_{C\to\infty}64\log C\,M_{M_0,M_{\rm ext}}(C)\le1
\tag{L7.22}
\]

is only over the admissible scalar residual family defined by (A1)--(A5). In particular, the class fixes a deterministic pre-exposure triangular array, uses a common scalar completion coefficient, credits only the displayed scalar \(\beta S_i/d\) term, and imposes the stated extraction stability.

The pointwise completion

\[
\beta(j-1)e_{jq}-\frac{e_{jq}^2}{2\mu}
\le\frac{\mu\beta^2}{2}(j-1)^2
\tag{L7.30}
\]

together with \(\beta\le m_0^2\) and \(\mu\le1+o(1)\) yields (L7.31) and the \(1/64\) cap. The constructed family attains the leading coefficient in (L7.23).

This does **not** prove a global cap over adaptive weights, matrix-valued completion, higher-order potentials, improved quadratic MGFs, or other extraction invariants. The manuscript states this limitation correctly.

## 6. Finite proof-carrying audit

### 6.1 The fixed-seed statement

Definition 19.2 and Theorem 19.3 are on p.42. The distance

\[
d_H(F)=|E(H)\setminus E(F)|
\]

charges only deleted input edges. Every original nonedge is free to be added. The theorem claims only

\[
\rho(H)\ge7,
\]

for the specified labelled content-addressed seed \(H\).

### 6.2 CNF implication direction

The CNF encoding is on pp.43--44, especially Proposition 21.1 and (F4.1)--(F4.3). A primary variable exists for every one of the \(\binom{100}{2}=4950\) pairs. Original nonedges are absent from the deletion counter and are not fixed false, so arbitrary additions are represented correctly.

For every installed 18-set \(S\), the positive hitting clause is

\[
C_S=\bigvee_{e\in\binom S2}x_e.
\tag{F4.1}
\]

Every graph with \(\alpha(F)<18\) satisfies every such clause. Installing only a selected finite bank therefore produces a relaxation of the exact Ramsey branch:

\[
F\text{ is a valid counterexample}
\quad\Longrightarrow\quad
\text{the primary assignment extends to a CNF model}.
\]

Consequently, UNSAT of the relaxation implies that the exact branch is empty. This is the required direction; it is not reversed.

### 6.3 Budget-five dependency

Proposition 20.1 is on p.42. Let \(f_0,f_1,f_2\) be the edges of the unique seed triangle. Every triangle-free graph omits at least one \(f_i\). If a candidate has total deletion budget at most five and \(f_i\) is chosen as an omitted triangle edge, then at most four further input edges are deleted. The corresponding branch fixes \(\neg x_{f_i}\) and permits at most four residual deletions.

Thus the three branches cover every candidate of budget at most five. If more than one triangle edge is absent, the candidate belongs to more than one branch or consumes residual budget; overlap does not create a gap.

### 6.4 Exact-six branch cover

Proposition 20.1 first eliminates all candidates of budget at most five. A counterexample to Theorem 19.3 would therefore have exactly six deleted input edges.

Lemma 20.2 on p.43 then chooses any absent seed-triangle edge \(f_i\). Exactly five members of \(E(H)\setminus\{f_i\}\) are absent, so the primary assignment extends to the exact-five sequential counter. If either of the other two triangle edges is also absent, it is an ordinary residual deletion and is counted among those five. Triangle-freeness satisfies the structural clauses, and \(\alpha(F)<18\) satisfies every installed hitting clause.

The three exact-six branches are therefore exhaustive, although they may overlap.

### 6.5 Certificate assembly

Proposition 20.3 asserts that each exact-six branch formula is unsatisfiable. The audit independently reconstructed the semantics of all three budget-five and all three exact-six formulas, including:

- the all-triples triangle prefix;
- the branch unit;
- the at-most-four or exact-five residual deletion counter as appropriate;
- every installed 153-literal hitting clause;
- the fact that all original nonedges remain free.

The six semantic reconstructions pass. Relative to the six corresponding checked DRAT refutations and the pinned checker, Propositions 20.1 and 20.3 combine with Lemma 20.2 to prove Theorem 19.3. No branch-cover or budget-accounting gap was found.

### 6.6 Exact-seven remains unknown

The bounded exact-seven experiment is reported on p.47. Each branch fixes one deleted triangle edge and asks for exactly six residual deletions. The three solver calls reached their 300-second parent-enforced walls without returning a model or a checked refutation.

The only correct endpoint is therefore `UNKNOWN`. In particular:

- zero separation iterations means that no SAT model returned before interruption; it does not mean UNSAT;
- a timeout supplies neither a seven-deletion repair nor its nonexistence;
- no exact value of \(\rho(H)\) follows;
- no 100-vertex \((3,18)\)-Ramsey graph and no improvement \(R(3,18)\ge101\) follows.

The manuscript observes all of these restrictions.

## 7. Minor issue and disposition

### M1. A terminal event was described as a partial history

**Original severity:** Minor.  
**Mathematical effect:** None; the formal source interface already quantified over the correct red-admissible histories.  
**Status:** **RESOLVED** in the current working tree and rematerialized unified paper.

The original wording referred to “a history in \(B_r^R\).” However, \(B_r^R\) is a terminal event. The relevant partial histories are those in

\[
\mathfrak H^R_{r,i-1}
=\{\mathbb P(B_r^R\mid\mathcal F_{i-1})>0\},
\tag{L2.29}
\]

which the manuscript calls red-admissible \(\mathcal F_{i-1}\)-histories.

The two canonical source occurrences have been corrected using the recommended wording:

1. `papers/lower/sections/05_ledger.tex`, formerly lines 53--54:

   > Fix a red-admissible \(\mathcal F_{i-1}\)-history for target \(r\) at exposure step \(i\), and condition further on \(A_i^R\).

2. `papers/lower/appendices/A_full_source_proof.tex`, formerly lines 118--119:

   > Fix a red-admissible \(\mathcal F_{i-1}\)-history for target \(r\), condition further on \(A_i^R\), and write

The materialized unified sources and rebuilt PDF now use the equivalent red-admissible-history terminology at p.29 and p.69. This resolves the event/history mismatch without changing any estimate or quantifier in the proof.

## 8. Minimum publication-safe statements

### Upper bound

> Assuming source interface 4.2, the repaired BookCor/rate induction, Theorem 5.1, and Arb containment semantics, the retained-spine certificate proves
> \[
> R(k,k)\le\exp\!\left((U(1)-3.4754\times10^{-6})k+o(k)\right)
> \le(3.780685290)^{k+o(k)}.
> \]

### Fixed-ratio lower bound

> Under source interface 11.2, including the additional weighted-extension hypothesis (S3), the source-relative fixed-ratio lower bound receives the added term
> \[
> \widehat H_*(C)=\frac{1+o(1)}{64\log C}
> \qquad(C\to\infty).
> \]
> The coefficient \(1/64\) is optimal only within the scalar residual family of Definition 16.1; no unconditional or globally optimal statement is claimed.

### Fixed-seed finite barrier

> For the specified content-addressed labelled seed \(H\), every triangle-free graph \(F\) with \(\alpha(F)<18\) satisfies \(d_H(F)\ge7\), even when all original nonedges may be added freely. The exact value of \(\rho(H)\), the budget-seven layer, and the global value of \(R(3,18)\) remain unresolved.

## 9. Final checklist

- [x] Theorem 3.1 is labelled and discussed as conditional on its source and interval-arithmetic interfaces.
- [x] Lemma 6.4's compact Arb obligation and analytic half-line have both been checked.
- [x] The retained-spine `max min` direction has been checked branch by branch.
- [x] All outer endpoint derivatives and maximizing endpoints have been checked.
- [x] Proposition C.2 supplies a valid theorem-to-six-stage-certificate implication with exact handoffs.
- [x] Theorem 10.1 retains (S1)--(S5), with (S3) identified as an additional hypothesis.
- [x] The same-history old CGF term, new increment term, and boundary residual are disjoint.
- [x] The fixed-\(C\), \(\ell\to\infty\), then \(C\to\infty\) quantifier order for \(1/64\) is explicit.
- [x] Proposition 16.2 is limited to Definition 16.1 and is not advertised as a global method cap.
- [x] All-pairs variables, free additions, CNF relaxation direction, budget-five dependency, and exact-six branch cover are correct.
- [x] The finite theorem states only \(\rho(H)\ge7\).
- [x] The exact-seven layer remains `UNKNOWN` and is not used as evidence for a global Ramsey-number improvement.
- [x] The one minor event/history terminology issue has been corrected at both occurrences and rematerialized.
- [x] No mathematical theorem, constant, or headline numerical value requires revision after this audit.

## 10. Final recommendation

From the standpoint of the mathematical arguments reviewed here, the unified manuscript is suitable to proceed with the three headline results at their existing explicit trust boundaries. The resolved terminology issue was minor and did not affect correctness. Publication metadata, public-release state, licensing, and archival claims are separate factual-review questions and are not certified by this mathematical report.
