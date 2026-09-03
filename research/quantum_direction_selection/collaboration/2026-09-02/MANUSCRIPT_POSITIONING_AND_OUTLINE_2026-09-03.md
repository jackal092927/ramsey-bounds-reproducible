# Manuscript positioning and restartable outline

September 3, 2026. **WRITING CHECKPOINT; MESSAGE-9 SOURCE AUDIT RUNNING.** This document converts the current proof archive into a focused theory-paper plan. Mathematical correctness, source interfaces and claim boundaries remain hard gates. A HIGH novelty rating is not required to begin the manuscript.

## Working title

Primary:

> Gapped Clique Filtrations for Exact Normalized Persistence

Alternatives:

- Degenerate-Kernel Gadget Reductions for Normalized Persistent Homology
- Exact Persistent Rank from Gapped Logical Kernels
- A Finite-Certificate Transfer Theorem for Normalized Harmonic Persistence

Avoid “first quantum persistence,” “universal,” “SDQC1-complete,” and “practical quantum advantage.”

## One-paragraph positioning

Existing clique-homology reductions can preserve satisfying-space multiplicity, and gapped reductions control the empty-kernel NO case. Guided harmonic persistence follows one specified initial hole. Normalized Harmonic Persistence instead asks for the fraction of the entire initial homology surviving through a filtration and requires gaps above both complete endpoint kernels. We give a finite-certificate transfer theorem for possibly degenerate logical kernels. It controls every low-energy geometric chain relative to the prescribed logical kernel, closes exact geometric multiplicity through quotient injection, and makes nested gadget term sets act by natural quotient maps. Applying it to an exact real-gate perfect-completeness verifier yields a restricted BQP1-hardness theorem for true initial-homology-normalized persistence. The proof isolates and repairs the uniformity needed in prior many-gadget estimates and gives a gap bound linear in the logical gap. A common-copy blow-up transfers the construction to unweighted clique filtrations once its source conventions are fixed.

## Community pain point

The paper should organize the gap between four nearby targets:

1. exact homology multiplicity without a promised gap;
2. simplex-normalized Betti number or quasi-low-energy counting;
3. survival of one succinctly specified harmonic guide;
4. the true ratio \(\beta_d(X_1\to X_2)/\beta_d(X_1)\) with whole-kernel endpoint gaps.

The contribution is a rigorous bridge from a degenerate logical kernel to item 4. The bridge gives later work a reusable list of local certificate conditions and an exact filtered quotient mechanism. This remains useful even if the final complexity corollary is gate dependent and the quantitative gap is poor.

## Proposed theorem stack

### Theorem A: finite-certificate degenerate-kernel transfer

Let \(R\) be a top-dimensional register with \(V=Z_d(R)\). Attach \(t\) clique gadgets with independent private interiors. Assume each member of a fixed finite palette has:

- exact filling \(B_d(Y_j)\cap V=\operatorname{ran}\Pi_j\);
- zero-weight kernel \(V\oplus Q_j\);
- a projected private differential with singular value at least \(b\lambda\) on \(Q_j\);
- a local positive-gap floor \(c\lambda^\kappa\);
- the recorded shared-register interface bound.

For \(H_A=\sum_{j\in A}\Pi_j\succeq g_A(I-P_{K_A})\), prove for every normalized geometric chain
\[
\|(I-P_{K_A})x\|^2
\le C\left[t\lambda^2+
\frac{\langle x,\Delta_Ax\rangle}{g_A\lambda^\kappa}\right].
\]
With suitable \(\lambda,E\), conclude
\[
H_d(X_A)\cong V/W_A,
\quad
\dim\ker\Delta_A=\dim K_A,
\quad
\operatorname{spec}(\Delta_A)\cap(0,E)=\varnothing.
\]

The theorem statement should make the local certificate format algorithmically checkable for a fixed palette. The qualitative dimension closure is a corollary; the all-chain estimate and its instance-uniform proof are the technical center.

### Theorem B: functorial nested-term-set corollary

For \(A\subseteq B\), prove that the isomorphisms in Theorem A identify inclusion-induced homology with
\[
V/W_A\twoheadrightarrow V/W_B.
\]
Hence
\[
\operatorname{rank}[H_d(X_A)\to H_d(X_B)]=\dim\ker H_B.
\]
Emphasize that this obtains the needed persistent rank without literal equality of geometric harmonic representatives.

### Theorem C: fixed-eight weighted hardness

For exact
\[
G_2=\{X,\mathrm{CX},\mathrm{CCX},H\otimes H\}
\]
BQP1 verification, use the eight-label operator
\[
M_x=\operatorname{diag}(1,p_x,p_x,p_x,p_x,p_x,0,0).
\]
Construct nested weighted clique complexes satisfying
\[
\beta_d(X_{\rm in})=8,
\qquad
\beta_d(X_{\rm in}\to X_{\rm out})=
\begin{cases}6,&x\in L,\\1,&x\notin L,
\end{cases}
\]
with inverse-polynomial gaps above both complete endpoint kernels. Therefore additive approximation distinguishes \(3/4\) from \(1/8\), for example at threshold \(7/16\) with error \(1/24\).

State hardness for \(\mathsf{BQP}_1^{G_2}\) and, separately, each fixed cyclotomic gate family covered by Rudolph's exact simulation theorem. Do not collapse these into gate-independent BQP1.

### Corollary D: common-copy unweighting

Use one common vertex set, putting future gadget vertices in the first level as isolated vertices. Choose dyadic \(\lambda\) and \(F=\lambda^{-2}\). Use the same labeled block of \(f_v=Fw(v)^2\) copies at both levels. Prove
\[
\widehat J U_1=U_2J,
\qquad
\widehat\Delta_i|_{\operatorname{ran}U_i}cong F\Delta_i,
\]
and invoke the asymmetric-sector lower bound. This preserves endpoint Betti numbers, the induced rank, and the ratio, with gap at least \(\min\{FE,1\}\).

Current status: the functorial proof and size arithmetic are local; final theorem wording awaits message-9 checking of the exact Hayakawa conventions. Treat it as a sourced corollary, not a new mechanism.

## Section outline

1. **Introduction.** State the four-target distinction, community pain point, theorem stack, and limitations.
2. **Normalized persistence and logical kernels.** Definitions, Hodge identification, source acceptance operator, and exact gate convention.
3. **Why endpoint existence is insufficient.** Degenerate kernels, whole-positive-gap requirement, and failure of a simulated-register-only estimate.
4. **Finite local certificates.** Exact filling, zero-weight decomposition, private differential, padding with outside harmonics, and interface bound.
5. **All-chain transfer theorem.** Prove geometric leakage, logical coercivity, subspace injection, exact multiplicity and whole gap.
6. **Filtered quotient naturality.** Prove the commuting quotient diagram and persistent rank.
7. **Explicit fixed palette and histories.** Bowtie register, exact atoms/guards, gain/loss Hadamard split, and logical gaps.
8. **BQP1 source and normalized-persistence hardness.** Eight-label operator, fixed-eight theorem, precision, and gate dependence.
9. **Unweighted clique filtrations.** Common-copy naturality, asymmetric sector, size and gap bookkeeping.
10. **Related work and limits.** Crichigno--Kohler, King--Kohler, Gyurik et al., Lowe et al., Hayakawa, plus poor exponents and nonintrinsic replicated denominators.
11. **Discussion.** Reusable transfer conditions and open routes to intrinsic growing-denominator or broader source classes.

Appendices should contain the finite certificate tables, selected-cycle guard proof, exact history-gap derivations, uniform-perturbation counterexample, and reproduction instructions.

## Claim firewall for v0

Safe claims, once dependencies are cited:

- true initial-homology-normalized persistence, not simplex normalization;
- exact endpoint multiplicities and gaps above the whole kernels;
- fixed-eight weighted \(\mathsf{BQP}_1^{G_2}\)-hardness under the proved transfer theorem;
- quotient naturality for the constructed nested term sets;
- a quantitative all-chain estimate linear in the logical gap;
- unweighted corollary only at the exact source-verified status reached after message 9.

Withhold:

- unrestricted \(\mathsf{SDQC}_1\), ordinary BQP, DQC1, QMA1, #BQP or gate-independent BQP1;
- exact compatible harmonic isometries in general filtrations;
- an intrinsic exponentially growing denominator;
- practical speedup or useful numerical gap;
- priority or “first” claims based only on search absence.

## Writing and verification sequence

1. Collect message 9 and archive its complete source links and formulas.
2. Write an independent disposition against the post-dispatch King-boundary note.
3. Freeze the exact weighted and unweighted theorem statuses.
4. Start `manuscript_v0.tex` immediately; write Introduction, theorem statements, and the all-chain proof first.
5. Move certificate enumeration and long calculations to appendices.
6. Run a notation/dependency audit and compile locally.
7. Obtain one hostile mathematical review of the assembled v0; use it to correct the manuscript, not to reopen indefinite direction selection.

## Current stop rule

Stop only for a mathematical counterexample, an unmet source interface needed by the theorem, or a failed finite certificate. A LOW or MEDIUM novelty assessment changes title, venue and emphasis; it does not stop v0 writing. No additional broad ideation round is required before drafting.
