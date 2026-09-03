# True normalized persistence: an exact-kernel transfer lemma

Date: 2026-09-02. Bounded independent probe; no manuscript or external service changed.

**Reading order after the round-2 audit:** the abstract lemma and padding proof below are retained. The unsupported general-integer-palette inference and the ordinary Hadamard-pair implementation in Section G are superseded by [the explicit weighted-history palette addendum](UNARY_PALETTE_ADDENDUM.md). Use its bounds $1/(8L^2)$ and $1/(120L^3)$ for that implementation. [Review resolution](REVIEW_RESOLUTION.md) separates the logical Hamiltonian from the geometric Laplacian and records the independent review's objections. The final scope is a restricted fixed-gate, standard-threshold reduction, not unrestricted SDQC1 hardness.

## Verdict

**NARROW / pursue one dependency audit, not a new gadget program yet.** There is a concrete route to true normalized persistence that does not require coefficient-sensitive output gadgets or exact equality of harmonic representatives. The key is an exact topological injection plus a low-energy **dimension** bound. Below is a complete abstract proof; applying it to every gadget in the required verifier palette remains to be certified. The follow-up appendix supplies an independent padding repair and restricts the source to a supported exact finite gate set with standard thresholds; it does **not** establish the July paper's unrestricted conjecture or novelty.

The June gap argument contains a stated-domain mismatch: its Lemma 11 concerns simulated-register states, while Lemma 7 invokes it for an arbitrary low-energy state. The argument below is a potential repair using the original arbitrary-state estimates, not an assumption that this mismatch is harmless.

## Source target, precisely

In [Lowe–Kim–Bondesan–Hayakawa, July 2026](https://arxiv.org/html/2607.03278v1), Problem 9 estimates

$$q=\beta_d^{1,2}/\beta_d^1,$$

for a weighted clique filtration, with nonzero initial Betti number and inverse-polynomial gaps above zero at both levels. **Conjecture 1:** this problem is SDQC1-hard. **Conjecture 2:** a polynomial construction transfers nested history Hamiltonians to a clique filtration, preserves whole kernel multiplicities and gaps, and supplies compatible isometries that identify surviving harmonic vectors exactly. Theorem 7 establishes hardness for the Hamiltonian version. Its kernels have dimensions $2^{N-1}$ and $\dim S$, where $S$ is the perfectly accepted input subspace.

Thus normalization by the initial Betti number is **already the source problem**, not a proposed new normalization. Common-multiplicity unweighting preserves both counts and their ratio. The July quasi-hardness construction uses the same complex at both levels and different energy cutoffs; that family has true persistence ratio exactly one whenever its initial Betti number is nonzero.

## Claim and status

**Claim.** For fixed-locality, finite-palette positive-projector Hamiltonians, independent exact-filling gadgets plus a dimension-uniform low-energy estimate imply exact kernel multiplicity, a gap above the entire kernel, and a natural quotient filtration. Consequently the stronger isometric condition in July Conjecture 2 is unnecessary for this rank-transfer step. Establishing its unrestricted rank-hardness Conjecture 1 would additionally require the full source-promise and gate-set reduction, which is not established here.

**Status: PROVABLE AFTER EXPLICIT SOURCE ASSUMPTIONS.** The abstract lemma and its consequences below are proved. The finite-palette gadget assumptions are the remaining source-integration obligation. They must be checked, not replaced by the published decision-hardness theorem.

## Assumptions and notation

Work over $\mathbb C$, in degree $d\geq1$. Let $R$ be a register complex of dimension $d$, and let

$$V=Z_d(R)=H_d(R)\subset C_d(R)$$

have an isometric identification with the simulated Hilbert space. The equality uses $C_{d+1}(R)=0$.

For each index $j$, a gadget complex $Y_j\supset R$ corresponds to an orthogonal projector $P_j$ on $V$, of constant locality. For a term set $A$, form $X_A=\bigcup_{j\in A}Y_j$. Assume:

1. **Independent supports.** Distinct gadgets intersect only inside $R$. In every degree, the chain space is the register plus mutually disjoint non-register gadget coordinates. No simplex uses vertices from two different gadgets.
2. **Exact single-gadget filling.**

   $$B_d(Y_j)\cap V=\operatorname{ran}P_j.$$

3. **Uniform low-energy estimate.** With $t=|A|$, $H_A=\sum_{j\in A}P_j$, and $\Delta_A$ the constructed degree-$d$ Laplacian, every normalized $\sigma$ satisfying $\langle\sigma,\Delta_A\sigma\rangle<E$ obeys

   $$1\leq\langle\sigma,\Pi_V\sigma\rangle-\langle\sigma,H_A^{\rm emb}\sigma\rangle+R(E),$$

   $$R(E)\leq C\left(t\lambda+t^2\lambda^2+tE/\lambda^{4m+2}\right).$$

   Here $H_A^{\rm emb}$ is zero outside $V$, $m$ is a fixed locality bound, and $C$ is independent of the exponentially large register dimension. Polynomial dimension dependence would also suffice after explicitly adjusting parameters.
4. **Hamiltonian promise.** $H_A\succeq g(I_V-P_A)$, where $P_A$ projects onto $K_A=\ker H_A$, and $0<g\leq1$ is a known inverse-polynomial lower bound. This includes $K_A=0$.

The same vertex weights and gadget labels are used at every level. Absent gadget vertices may be isolated initially to obtain a common vertex set; this does not alter degree-$d\geq1$ homology.

**Operator distinction essential to the claim.** $H_A$ acts on the logical register space $V$; $\Delta_A$ acts on the full, larger chain space $C_d(X_A)$. The low-energy assumption concerns *all* vectors of the latter space and their distance to the embedded logical kernel, not their distance to $\ker\Delta_A$, which is initially unknown. The energy threshold depends on $t$, the promised logical gap $g$, and the chosen weight $\lambda$. No term-count-independent gap is asserted.

## Proof strategy and dependency map

Independent gadget boundaries give an exact quotient on register cycles. Low energy forces proximity to the *Hamiltonian* kernel. A subspace larger than that kernel necessarily contains an orthogonal vector; this converts proximity into an exact multiplicity and gap statement. Naturality then follows from quotient maps, without identifying harmonic representatives.

Source facts to audit are limited to assumptions 1–3 and the verifier's fixed projector palette. The remaining linear algebra is below. In [King–Kohler, Sections 8–10](https://arxiv.org/html/2311.17234v2), Section 10.3 explicitly omits inter-gadget edges; the single-gadget construction targets one forbidden subspace; Lemmas 10.2–10.4 state arbitrary-state low-energy bounds. Their combination would imply assumption 3. However, the padding caveat below prevents treating those estimates as independently certified here. That theorem's statement itself only gives a zero-versus-positive-minimum guarantee, not our full multiplicity conclusion.

## Proof

### 1. Positive coefficients can be erased

Let $H_A(a)=\sum_{j\in A}a_jP_j$, with every $a_j>0$, and let $a_{\max}=\max_j a_j$. Positivity gives

$$\ker H_A(a)=\bigcap_{j\in A}\ker P_j=\ker H_A.$$

Indeed, zero energy is equivalent to $\sum_j a_j\|P_jx\|^2=0$. Moreover,

$$H_A\succeq H_A(a)/a_{\max}.$$

The operators have the same kernel, so their positive gaps satisfy

$$\gamma_+(H_A)\geq\gamma_+(H_A(a))/a_{\max}.$$

Therefore polynomially bounded penalty coefficients can be replaced by one without changing kernel counts or destroying an inverse-polynomial gap. No approximation of a small output coefficient is required for exact rank persistence. This argument does not cover negative coefficients or subtraction of an energy shift.

### 2. Independent gadgets give the exact register quotient

Put $W_A=\sum_{j\in A}\operatorname{ran}P_j$. We claim

$$B_d(X_A)\cap V=W_A.$$

The inclusion $\supseteq$ follows from assumption 2. Conversely, if $v\in V$ and $v=\partial c$, decompose $c=\sum_j c_j$ among the non-register $(d+1)$-chains. There are no register $(d+1)$-chains. Since $\partial c$ has no non-register coordinate and those coordinates are disjoint among gadgets, every $\partial c_j$ is supported entirely in $R$. It is a cycle and hence lies in $V$. Assumption 2 yields $\partial c_j\in\operatorname{ran}P_j$, so $v\in W_A$.

Consequently the map $V\to H_d(X_A)$ induced by inclusion has kernel exactly $W_A$. Since

$$K_A=W_A^\perp,$$

this already supplies $r_A=\dim K_A$ linearly independent exact homology classes. By Hodge theory,

$$\dim\ker\Delta_A\geq r_A.$$

This step does **not** assert that the register representatives remain harmonic.

### 3. Low-energy overlap bounds the entire subspace dimension

For any normalized low-energy $\sigma$, assumption 3 gives

$$1-\langle\sigma,\Pi_V\sigma\rangle+\langle\sigma,H_A^{\rm emb}\sigma\rangle\leq R(E).$$

Write $P_A$ also for its embedding into the full chain space. The Hamiltonian gap and $g\leq1$ imply

$$g\bigl(1-\langle\sigma,P_A\sigma\rangle\bigr)\leq R(E).$$

Choose a target $0<\eta<1$, a sufficiently small constant $c$ depending only on $C$, and common parameters satisfying

$$0<\lambda\leq c\eta^2g/t,\qquad E\leq c\eta^2\lambda^{4m+2}g/t.$$

Then $R(E)/g\leq\eta^2$. Every normalized vector in the spectral subspace

$$L_E=\operatorname{ran}{\bf1}_{[0,E)}(\Delta_A)$$

has squared projection at least $1-\eta^2>0$ onto the $r_A$-dimensional space $K_A$. Thus $P_A|_{L_E}$ is injective and

$$\dim L_E\leq r_A.$$

Step 2 supplies at least $r_A$ exact zero modes inside $L_E$. Hence

$$\boxed{\dim\ker\Delta_A=r_A,\qquad\gamma_+(\Delta_A)\geq E.}$$

For $r_A=0$, the same argument says $L_E=0$. This is an exact counting argument; **no near-zero eigenvalue has been relabelled as zero**.

### 4. Nested term sets produce the required true persistence

Step 2's injection $V/W_A\to H_d(X_A)$ is now an isomorphism by the dimension equality. For $A\subseteq B$, the inclusion map therefore fits the natural quotient map

$$V/W_A\longrightarrow V/W_B.$$

It is surjective. In particular,

$$\beta_d(X_A)=\dim K_A,\qquad\beta_d^{A,B}=\dim K_B,$$

and, when $K_A\ne0$,

$$\boxed{\frac{\beta_d^{A,B}}{\beta_d(X_A)}=\frac{\dim\ker H_B}{\dim\ker H_A}.}$$

This is the exact quantity in July's Hamiltonian hardness reduction. Shared parameters may use the maximum number of terms and the minimum promised gap over both levels. A dyadic $\lambda$ within a constant factor of the bound suffices; its denominator is polynomial for fixed locality and inverse-polynomial $\eta,g$.

### 5. Harmonic angles need not be exact, but are controllable

Let $Q_A$ project onto $\ker\Delta_A$. Step 3 implies $\|(I-P_A)Q_A\|\leq\eta$; equal ranks imply $\|Q_A-P_A\|\leq\eta$. For nested term sets, $P_B\leq P_A$. Thus every unit $y\in\operatorname{ran}Q_B$ satisfies

$$\|(I-Q_A)y\|\leq2\eta.$$

Consequently all eigenvalues of $Q_BQ_AQ_B$ on $\operatorname{ran}Q_B$ are at least $1-4\eta^2$. This supplies the large-overlap promise for constant $\eta<1/2$ without asserting $J E_A=E_B$ on surviving vectors.

Efficient preparation of a maximally mixed *harmonic* subspace is a separate input-access promise. A circuit preparing the simulated history mixture is not literally the same circuit. Because $\|Q_A-P_A\|\leq\eta$, their normalized maximally mixed states have trace distance at most $\eta$; choosing inverse-polynomial $\eta$ allows the usual approximate state-preparation convention. An exact-preparation formulation needs an additional construction or a revised promise, and is not silently assumed here.

## Strongest remaining checks

1. **Exact single-gadget kernel, for the complete fixed verifier palette.** Verify $B_d(Y_j)\cap V=\operatorname{ran}P_j$ rather than merely existence/nonexistence of one hole. Tensor padding and the complete gate set must be covered. This is the smallest topological obligation; the many-gadget part is proved above.
2. **Uniform constants and a padding flaw in the local spectral estimates.** The general basiswise perturbation definition in KK Definition 7.7 does not, in growing dimension, by itself imply a dimension-free projector-norm estimate. The fixed-size gadget can avoid that problem: establish the bound in constant dimension and then use $\|A\otimes I\|=\|A\|$. More seriously, the parallel TDA audit found that KK Claim 10.2's literal $O(\lambda)$ bound for the padded coordinate-bulk boundary fails: removing a weight-one outside-register vertex can remain inside that bulk. The candidate repair replaces coordinate bulk by **local bulk tensored with the outside-register harmonic subspace**, so the outside boundary and coboundary vanish. The parallel derivation proposes the slightly weaker remainder $C(t\lambda+t^2\lambda^2+tE/\lambda^{4m+2})$ used above. That repair, including its cross-gadget interface bound, still needs line-by-line certification. The present lemma deliberately assumes the estimate and does not certify it.
3. **Exact source palette and realification.** Coefficient erasure preserves kernels but does not turn arbitrary complex irrational local states into the supported integer-state projectors. Check the SDQC1 verifier construction against the gadget palette, with any multiplicity-doubling realification accounted for in numerator and denominator.
4. **June source repair.** [Lemma 11 and Lemma 7](https://arxiv.org/html/2410.21258v2) have the domain mismatch identified above. The present argument needs the arbitrary-state KK estimates directly, not the restricted Lemma 11. No unreviewed unfolding manuscript was used as a theorem.
5. **Unweighting is downstream.** If the weighted family passes these checks, apply the shared-multiplicity lemma in the local `UNWEIGHTING_FIRST_LEMMA.md`: fixed dyadic weights, common multiplicities, and polynomial blowup preserve the exact harmonic ranks and persistence maps. It cannot repair a failed weighted construction.

## Cheap obstructions to alternative shortcuts

- **Quasi to true by threshold adjustment:** on the existing equal-complex quasi-hard family, true normalized persistence is identically one. Unweighting or duplication does not create a nontrivial filtration map.
- **Low-rank guide in place of a uniform initial mixture:** in $\mathbb C^D$, a guide supported on an $r$-dimensional subspace $G$ gives identical unit overlap with target kernels $G$ and $\mathbb C^D$, whereas their normalized ranks are $r/D$ and $1$. This is an information-theoretic obstruction to recovering the whole rank from those guide overlaps alone, not a graph-oracle lower bound.
- **Positive regularization:** replacing $H$ by $H+\epsilon I$ for any $\epsilon>0$ erases every zero mode. Approximation quality in operator norm does not preserve Betti numbers.
- **Uniform multiplicity replication:** multiplying both kernel counts by the same factor leaves their ratio unchanged. It does not amplify a small normalized counting signal.

## Exact classical baseline

This problem is polynomial-time in the explicitly listed relevant simplices. Let $Z_1$ be a matrix whose columns form a basis of $\ker\partial_d^{X_1}$, embedded in $C_d(X_2)$, and let $B_2$ be the matrix of $\partial_{d+1}^{X_2}$. Then

$$\beta_d^{1,2}=\operatorname{rank}[Z_1\ B_2]-\operatorname{rank}B_2,$$

$$\beta_d^1=\dim\ker\partial_d^{X_1}-\operatorname{rank}\partial_{d+1}^{X_1}.$$

Gaussian elimination gives an unconditional exact $O(S^3)$ arithmetic-operation baseline, with $S$ the total number of relevant simplices; bit complexity must be added for exact arithmetic. For an $n$-vertex graph, enumeration and this linear algebra cost $n^{O(d)}$, so fixed $d$ is polynomial. These are transparent baselines, not a claim to the fastest known classical implementation. Quantum hardness concerns the succinct graph input with growing $d$, and any algorithmic advantage must state its gap, guide-access, and accuracy promises.

## Smallest next lemma / stop rule

Ask for a source-certified **finite-palette register-boundary lemma**:

> For every constant-local projector in the exact SDQC1 verifier palette, the KK gadget has $B_d(Y_j)\cap H_d(R)=\operatorname{ran}P_j$, and its padded arbitrary-state low-energy estimate has polynomially uniform constants.

If this holds, the proof above supplies multiplicity, two-level gaps, natural rank persistence, and a constant harmonic-angle promise. If it fails, isolate one explicit unsupported projector or boundary relation before designing a replacement. Do not spend a new project on coefficient-sensitive gadgets until this cheaper route is ruled out. If all dependencies already appear explicitly in the published KK version, the result may be a short corollary resolving the July conjecture rather than a new general mechanism; novelty remains unassessed.

## Follow-up: independent identity-padding repair

Status: **PROVABLE AFTER THE FIXED-SIZE LOCAL GADGET HYPOTHESES.** This section independently checks the many-gadget interference step in the companion `UNWEIGHTING_AUDIT.md`. No simultaneous global outside-register decomposition is assumed. The normalized-persistence conclusion remains conditional on the exact finite projector palette and single-gadget topology.

### A. Single-gadget invariant sectors, not a global decomposition

For gadget $i$ on $m_i$ qubits, put $Y_i=Y_i^{\rm loc}*R_i^{\rm out}$, with $r_i=n-m_i$, $q_i=2r_i-1$, and $p=2n-1$. On augmented chains,

$$C_k(Y_i)=\bigoplus_{a+b=k-1}C_a(Y_i^{\rm loc})\otimes C_b(R_i^{\rm out}),$$

$$\partial(x\otimes y)=\partial_{\rm loc}x\otimes y+(-1)^{a+1}x\otimes\partial_{\rm out}y,$$

$$\Delta_{Y_i}=\Delta_{\rm loc}\otimes I+I\otimes\Delta_{\rm out}.$$

The fixed register factor has augmented harmonic space only in degree one, and has a positive spectral gap $\delta_R>0$ on its orthogonal complement. Tensor-sum positivity shows that the $r_i$-fold register join has harmonics only in degree $q_i$, with the same lower bound $\delta_R$ on every nonharmonic mode, independent of $r_i$. For $r_i=0$, use the augmented join unit in degree $-1$.

In degree $p$, the only possible bidegrees are $(2m_i-1,q_i)$ and $(2m_i,q_i-1)$. Thus every outside-nonharmonic mode belongs to a constant-gap single-gadget sector $A_i$, regardless of its local energy. This assertion concerns $\Delta_{Y_i}$ only. The full many-gadget Laplacian need not commute with gadget $i$'s outside harmonic projector.

### B. Exact interface bound controls every other gadget

Let $\Pi_0^k$ project onto register coordinates and $\Pi_j^k$ onto coordinates containing new vertices of gadget $j$. Define

$$L_j=\Pi_0^{p-1}\partial\Pi_j^p.$$

Only a simplex containing **exactly one** new gadget vertex $u$ can contribute to $L_j$: the boundary must delete $u$ to land in the register. This has coefficient $\lambda$. For a fixed $u$, deletion is a signed partial isometry $D_u$ from an orthogonal input block. Therefore, writing $N_j$ for the number of new vertices of gadget $j$,

$$L_j=\lambda[\,D_u\,]_{u\in V_j^{\rm new}},\qquad
L_jL_j^\dagger=\lambda^2\sum_u D_uD_u^\dagger\preceq\lambda^2N_j I.$$

The fixed finite palette has $N_j\leq N_*$, a constant. Even with overlapping qubit supports and all outside bidegrees present,

$$\left\|[\,L_j\,]_{j\ne i}\right\|\leq\lambda\sqrt{\sum_{j\ne i}N_j}\leq\lambda\sqrt{N_*t}.$$

For a normalized full state $\sigma$ with energy at most $E$, let $x_i=(\Pi_0^p+\Pi_i^p)\sigma$. Up-boundary outputs split by gadget, and non-register down-boundary outputs are disjoint. The register down-boundary discrepancy is exactly $\sum_{j\ne i}L_j\Pi_j^p\sigma$. Hence

$$\langle x_i,\Delta_{Y_i}x_i\rangle\leq C(E+t\lambda^2),\qquad
\|A_i x_i\|\leq C(\sqrt E+\lambda\sqrt t).\tag{A1}$$

This proves the needed control of outside-nonharmonic modes despite cross-gadget mixing; it does not try to rule out that mixing.

### C. Correct projected bulk estimate

Let $P_{{\rm out},i}$ project onto outside harmonics in degree $q_i$. Let $P_{{\rm bulk},i}^{a}$ be the coordinate projector onto local simplices containing the gadget's central vertex. Define

$$Q_i^k=P_{{\rm bulk},i}^{\,k-q_i-1}\otimes P_{{\rm out},i}$$

on that bidegree and zero elsewhere, and put

$$T_i=(Q_i^{p-1}\partial_i,\ Q_i^{p+1}d_i).$$

Harmonicity gives $P_{{\rm out},i}\partial_{\rm out}=P_{{\rm out},i}d_{\rm out}=\partial_{\rm out}P_{{\rm out},i}=d_{\rm out}P_{{\rm out},i}=0$, with degrees understood. Thus the outside differential disappears on both sides. All remaining local matrix entries entering the central bulk have a factor $\lambda$; the local matrix dimension is constant. Consequently

$$\|T_i\|\leq C\lambda.$$

The local central-bulk relative chain complex has no degree-$(2m_i-1)$ homology. Its projected boundary/coboundary pair is therefore injective in that degree. For the fixed palette its least singular value before multiplying by $\lambda$ is a positive constant. Tensoring with outside harmonics preserves singular values, giving

$$\|T_iQ_i^p x\|\geq c\lambda\|Q_i^p x\|.\tag{A2}$$

The ranges of $Q_i^{p\pm1}$ contain a new vertex of gadget $i$. Other gadget chains cannot contribute to them under either differential. Therefore

$$T_i x_i=(Q_i^{p-1}\partial\sigma,\ Q_i^{p+1}d\sigma),\qquad \|T_i x_i\|\leq\sqrt E.$$

This is the exact reason the corrected projection works even when $P_{{\rm out},i}$ and $P_{{\rm out},j}$ refer to different qubit sets.

### D. Closing the bulk and concentration bounds

Use the fixed-size spectral projectors $A_i,B_i,F_i$ for high, bulk, and low sectors, respectively. Here $F_i$ combines the harmonic and lifted-constraint sectors. After padding,

$$A_i+B_i+F_i=I_i,\quad \|B_i-Q_i^p\|\leq C\lambda,\quad
\|Q_i^pF_i\|\leq C\lambda,\quad \|T_iF_i\|\leq C\lambda^{2m_i+1}.$$

The last estimate follows from the full single-gadget low-sector energy, not an assumption that all low vectors are harmonic. Write $Q=Q_i^p$. The identity

$$I_i=Q+(I_i-Q)A_i+(I_i-Q)B_i+F_i-QF_i$$

together with (A1)–(A2) yields

$$c\lambda\|Qx_i\|\leq\sqrt E+C\lambda\|A_ix_i\|+C\lambda^2,$$

$$\|B_ix_i\|\leq C(\sqrt E/\lambda+\lambda\sqrt t).$$

Thus

$$\sum_i\|A_ix_i\|^2\leq C(tE+t^2\lambda^2),\qquad
\sum_i\|B_ix_i\|^2\leq C(tE/\lambda^2+t^2\lambda^2).$$

For the lifted constraint sector, use the exact local cycle property: the one-dimensional first lifted eigenspace has nonzero overlap with the register constraint cycle; its spectral projector preserves cycles, so it consists of cycles. Padding with outside harmonics retains that property. Its energy is therefore entirely up energy. Since up energy splits over gadgets, the sum of lifted-sector masses is at most $CE/\lambda^{4m+2}$, with $m=\max_i m_i$ and $\lambda\leq1$.

Finally the kernel projector for gadget $i$ is within $C\lambda$ of the embedded projector onto $\ker P_i$. This is proved locally in constant dimension and then tensored, never inferred from basiswise closeness in exponential dimension. Summing the complete-projector identity gives exactly

$$1\leq\langle\sigma,\Pi_V\sigma\rangle-\langle\sigma,H^{\rm emb}\sigma\rangle
+C(t\lambda+t^2\lambda^2+tE/\lambda^{4m+2}).$$

This independently establishes assumption 3 from the fixed-size local spectral and relative-bulk hypotheses. The literal full-coordinate padded Claim 10.2 is unnecessary and remains false. No additional global sector-invariance assumption was introduced.

## Follow-up: restrict the hardness source and remove amplification

The exact gate set matters. For the normalized-counting target, fix the rational real set $G_2=\{X,\mathrm{CX},\mathrm{CCX},H\otimes H\}$ and the corresponding finite integer-state projector palette. Do not conclude hardness for every gate-set-dependent formulation of SDQC1. This is distinct from the June harmonic-guide reduction's four-local Pythagorean palette. The construction below has locality at most six; use $4m+2$, not the June exponent $18$.

### E. The correct acceptance-to-rank thresholds

Let $M$ be the acceptance operator on the $D$-dimensional valid input space. Assume $S=\ker(I-M)$ is its perfectly accepted subspace, and that $M|_{S^\perp}\preceq rI$. Put $f=\dim S/D$ and $p=\operatorname{Tr}M/D$. Then

$$f\leq p\leq r+(1-r)f.$$

If YES has $p\geq a$ and NO has $p\leq b$, exact kernel fractions separate only when

$$\frac{a-r}{1-r}>b.$$

An inverse-polynomial $a-b$ by itself is insufficient. In particular, with the standard promise

$$a=2/3,\quad b=1/3,\quad r=1/3,$$

we get YES $f\geq1/2$ and NO $f\leq1/3$, a gap of $1/6$. An additive rank-ratio estimate with error less than $1/12$ decides this restricted source promise. No amplification or gate-palette change is needed. For thresholds below $r$, two distinct acceptance probabilities can both have $S=0$ and identical zero kernel fraction.

### F. Direct both-kernel gap for the history Hamiltonians

Here is an elementary general lemma. Suppose $H_1\succeq g_1(I-P_K)$ with $0<g_1\leq1$, $Q$ is an orthogonal projector, $S=K\cap\ker Q$, and

$$P_KQP_K\succeq\alpha(P_K-P_S),\qquad 0<\alpha\leq1.$$

Then

$$\ker(H_1+Q)=S,\qquad
\gamma_+(H_1+Q)\geq\frac{\alpha g_1}{2g_1+3}\geq\frac{\alpha g_1}{5}.$$

Proof: for a unit $\psi\perp S$, write $\psi=x+y$ with $x\in K\ominus S$, $y\perp K$, and set $e=\langle\psi,(H_1+Q)\psi\rangle$. Then $g_1\|y\|^2\leq e$ and $\|Q\psi\|^2\leq e$. Also

$$\alpha\|x\|^2\leq\|Qx\|^2\leq2\|Q\psi\|^2+2\|Qy\|^2\leq2e+2e/g_1.$$

Thus $1\leq e(2g_1+2+\alpha)/(\alpha g_1)$, giving the displayed bound. Positivity gives the exact kernel identity.

For a uniform history encoding with $L$ legal clock positions, $K$ is the space of valid input histories and

$$P_K H_{\rm out}P_K\cong (I-M)/L.$$

The restricted source promise gives $\alpha=(1-r)/L=2/(3L)$ off $S$, so the second Hamiltonian has an inverse-polynomial positive gap whenever $H_1$ does, regardless of $\dim S$. The following explicit implementation supplies the needed locality and first gap.

### G. Explicit six-local unary-clock implementation

**Superseded as a source-certified palette.** This ordinary unitary-clock calculation explains locality but the fact that its vectors have integer amplitudes does not prove that all needed gadgets exist. Use `UNARY_PALETTE_ADDENDUM.md` for the certified replacement: consecutive gain/loss Hadamard steps from Rudolph's construction, explicit supported three-term states, and the adjusted weighted-path bounds. Do not use the unmodified Hadamard-pair vectors as an imported gadget theorem.

For $T$ circuit gates, let $L=T+1$ and use legal clock strings $|t\rangle=|1^t0^{T-t}\rangle$, $0\leq t\leq T$. Set

$$H_{\rm clock}=\sum_{j=1}^{T-1}|01\rangle\langle01|_{j,j+1}.$$

For interior transition $t$, the clock block on positions $(t-1,t,t+1)$ changes from $100$ to $110$. Introduce rank-one local propagation projectors onto

$$|\phi_{t,z}\rangle=\frac{|100\rangle|z\rangle-|110\rangle U_t|z\rangle}{\sqrt2},$$

for every computational basis string $z$ on the at-most-three work qubits of gate $U_t$. At the ends, fix sentinel clock bits $b_0=1$, $b_{T+1}=0$ and omit them from the actual support. The vectors are orthonormal for fixed $t$, so their sum gives the usual positive propagation term. The legal clock span is invariant under each term; Hermiticity makes its orthogonal complement invariant as well. Illegal strings have clock energy at least one.

All matrices in $G_2$ have rational entries. The finitely many vectors $\phi_{t,z}$ therefore become integer-amplitude vectors after multiplying by a common denominator and renormalizing. Their locality is at most three clock plus three work qubits, hence $m\leq6$. Clock, input, and output terms are computational-basis projectors of smaller locality. The resulting gadget palette is finite and independent of circuit length.

Penalize each invalid initially fixed work bit, conditioned on clock bit one being zero; within the legal clock span this is exactly time zero. Penalize rejection conditioned on the last clock bit being one; within the legal span this is exactly time $T$. These terms are diagonal in the clock and preserve the legal/illegal split.

After conjugating the legal block by $\sum_t|t\rangle\langle t|\otimes U_t\cdots U_1$, the first Hamiltonian is

$$H_1^{\rm legal}=\frac12\sum_{t=1}^{T}(|t\rangle-|t-1\rangle)(\langle t|-\langle t-1|)\otimes I
+|0\rangle\langle0|\otimes A_{\rm in},$$

where $A_{\rm in}$ is the sum of invalid-input-bit projectors and has eigenvalues zero or at least one. Its zero space is precisely the uniform clock tensored with valid inputs. The unanchored path has positive gap at least $c/L^2$. On an invalid-input sector, for any clock-vector sequence $f_t$,

$$\sum_{t=0}^{T}\|f_t\|^2\leq2L\|f_0\|^2+2LT\sum_{t=1}^{T}\|f_t-f_{t-1}\|^2
\leq4L^2\left(\|f_0\|^2+\frac12\sum_{t=1}^{T}\|f_t-f_{t-1}\|^2\right).$$

Together with the illegal sector bound this gives the explicit safe lower bound

$$g_1\geq\frac1{4L^2}.$$

Using the lemma in Section F with $\alpha=2/(3L)$ gives

$$g_2\geq\frac1{30L^3}.$$

Both bounds hold above the entire kernel, including exponentially degenerate kernels. The exact kernel fractions distinguish the restricted source thresholds in Section E without amplification. For the unweighting/concentration step one may take $m=6$, producing the safe exponent $4m+2=26$; a smaller locality should be claimed only after an explicit alternate clock construction.

### H. Exact filling follows from the same local spectral package

The parallel TDA audit supplied the following additional observation, independently checked here. It removes a separate surgery-proof obligation from assumption 2, conditional on the same fixed-size nullity and kernel-limit facts already used for the spectral argument.

For one padded gadget, write $W_k(\lambda)$ for the diagonal operator multiplying a simplex by the product of its vertex weights. Weighted boundary matrices satisfy

$$\partial_w=W_{p-1}^{-1}\partial_1W_p,\qquad B_p(w)=W_p^{-1}B_p(1).$$

All register weights are one, so $W_p|_V=I$. Thus the subspace

$$Z_j=B_p(w)\cap V$$

is independent of $\lambda>0$. Every $v\in Z_j$ is orthogonal to the single-gadget harmonic space for every $\lambda$. The fixed-size kernel convergence, padded with outside harmonics, is

$$P_{\ker\Delta_j(\lambda)}\longrightarrow\Pi_V-\Phi_j\quad\text{as }\lambda\to0,$$

where $\Phi_j$ is the embedded forbidden projector. Passing to the limit shows $Z_j\subseteq\operatorname{ran}\Phi_j$. On the other hand, the known single-gadget nullity is $\dim V-\operatorname{rank}\Phi_j$. The inclusion map $V\to H_p(Y_j)$ must therefore have a kernel of dimension at least $\operatorname{rank}\Phi_j$. Its kernel is exactly $Z_j$. Hence

$$Z_j=\operatorname{ran}\Phi_j,$$

and the register map is surjective. This proves exact single-gadget filling from local nullity, local kernel convergence, and the weight gauge. It neither sets $\lambda=0$ in the graph problem nor labels any positive eigenvalue as zero.

**Final round-2 boundary:** the companion weighted-history addendum replaces the unsupported generic palette by explicitly supported small states and their product guards. The fixed-gadget spectral/nullity/relative-bulk results remain cited literature dependencies; the many-gadget repair and exact filling deduction are local arguments. The arbitrary-threshold/gate-set extension remains explicitly excluded. This is a reduction from a precisely stated fixed-gate circuit promise, conditional on those imported local results, not an assertion of the unrestricted SDQC1-hardness conjecture. Novelty and full source integration remain to be independently reviewed.
