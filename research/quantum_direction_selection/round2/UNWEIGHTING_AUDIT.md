# Round 2: unweighting, source parameters, and a proposed gap-proof repair

2026-09-02. Author: bounded independent TDA probe. Other projects were read-only. No external submission was made by this agent.

## Outcome and proof status

**PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION:** the precise target is harmonic survival with a source-compatible **signed** succinct subset guide, not a strictly positive guide in globally sorted simplex coordinates, and not normalized persistent Betti number. The common-multiplicity transfer is proved below. A BQP1-hardness corollary follows from the weighted source theorem; this audit additionally supplies a local repair of its gap argument, reducing its dependencies to the fixed-size King--Kohler gadget package. The repair is a LOCAL DERIVATION, independently algebra-checked by the root and the companion audit in this session; it must not be represented as wording already present in either source. The fixed-gadget source theorem itself remains an imported theorem, not a from-scratch proof completed here.

There is no identified functoriality, integer-parameter, or guide-preparation obstruction for the source hard family. However, the June proof has a real domain mismatch, present in the published PDF, and a literal padded-bulk estimate in the older preprint also needs correction. A bare assertion that the complete imported proof has been independently verified would be inaccurate.

## Sources and dependency boundary

1. Gyurik--Schmidhuber--King--Dunjko--Hayakawa, [PRX Quantum 7, 020361 (16 June 2026)](https://journals.aps.org/prxquantum/pdf/10.1103/gvys-hl8h), DOI **10.1103/gvys-hl8h**; [arXiv v2](https://arxiv.org/html/2410.21258v2). Checked Lemmas 5--9 and Appendix B. In the journal the overlap lemma is B1; in the arXiv HTML it is 11.
2. King--Kohler, [arXiv:2311.17234v2](https://arxiv.org/html/2311.17234v2), especially the fixed-gadget Lemma 9.1, padded Lemma 10.1, Claims 10.1--10.4, and Appendix B. The [journal landing page](https://epubs.siam.org/doi/10.1137/24M1710243) identifies the 2026 SIAM publication, but its full text was not accessible in this bounded check. Do not attribute an arXiv-only defect to the SIAM version without checking that version.
3. Hayakawa, [arXiv:2608.02726v1](https://arxiv.org/html/2608.02726v1), Lemma 4.2 and Theorem 4.3, August 2026 preprint. Its fixed-sector and asymmetric-gap proofs were checked at the operator level, independently of its QMA1 gate-set reduction.

No step uses Dey--Xin arXiv:2403.08110v4. The current QuantumTDA instructions explicitly classify that unfolding preprint as unreviewed and correctness-unverified.

Dependency map:

    fixed finite gadget palette + its local spectral/topological facts
           -> corrected arbitrary-state concentration estimate
           -> min--max YES gap + harmonic/history closeness
    circuit-history Hamiltonian + register product guide
           -> weighted harmonic-survival hardness
    common integer copies + fixed/asymmetric sectors
           -> signed-guide unweighted harmonic-survival hardness

## 1. Precisely specified target

Let UHS denote the following promise problem over real chains (complexification is harmless).

Input: explicit finite graphs $G_1\subseteq G_2$, degree $p\geq1$, an inverse-polynomial lower bound $\gamma_0$ for the nonzero spectrum of $\Delta_p(\mathrm{Cl}(G_2))$, and a polynomial-size classical description/preparation procedure for a unit vector

$$|\psi\rangle=|S|^{-1/2}\sum_{\sigma\in S}\epsilon(\sigma)|\sigma\rangle,
\qquad \epsilon(\sigma)\in\{-1,1\}.$$

Simplex coordinates use globally increasing vertex order; $\epsilon$ is efficiently computable. The guide is promised harmonic in the first clique complex. The source-compatible restricted descriptor is a polynomial-size disjoint union of equal-cardinality products of oriented edge families on disjoint vertex blocks, with copy labels allowed in those families. It permits polynomial-time quantum preparation to any inverse-polynomial error; a mere efficient membership oracle for $S$ is NOT the input model.

Promise: the squared final harmonic overlap is at least $2/3$ or at most $1/3$. Output the corresponding bit. The reduction below has YES overlap at least $0.9$ and NO overlap exactly zero. Equivalently, one may keep the source's inverse-polynomial-versus-exponentially-small norm thresholds, because this special reduction has zero NO overlap even after polynomial graph-size expansion.

**Claim:** UHS is BQP1-hard for the June source's fixed gate set $\{\mathrm{CNOT},U_{\rm Pyth},I\}$, and belongs to BQP. This does not say BQP-complete or BQP1-complete. Its unconditional source-level status is a corollary of the cited weighted theorem and August graph lemmas; its independently repaired proof is conditional on the fixed-gadget facts isolated in Section 3 below.

Membership is standard, not a new algorithm. The explicit graph gives polynomial-time clique and boundary access. In degree $p$, the boundary has at most $p+1$ entries per column and at most $|V|$ cofaces per row; the Hodge Laplacian has polynomial sparsity and polynomial norm. Rescaled Hamiltonian simulation and phase estimation separate zero from $[\gamma_0,\infty)$, and repeated measurement estimates the guide's zero-eigenspace weight to constant error. Preparation and orientation phases are included in the running time. No uniform state over all cliques is needed.

## 2. June audit: exact issue and parameter choices

**Verified version mismatch, not a counterexample to the theorem.** Journal Lemma 7, printed p. 9, applies Appendix-B Lemma B1 to an arbitrary low-energy state orthogonal to the harmonic space. B1, printed p. 16, assumes the state lies in the simulated-qubit subspace. The arXiv version has the same mismatch. The subsequent global subspace-closeness assertion is not supplied merely by its citation to a definition. Replace both steps by the concentration/min--max argument below.

For the source circuit, the history Hamiltonian has a unique zero vector in YES and no zero vector in NO, with a known inverse-polynomial spectral lower bound $g_0\leq1$ after polynomial pre-idling. Lemma 5's YES argument is valid: positive addition of the output penalty preserves the already unique, perfectly accepting history kernel. One need not compute the actual spectral gap.

Let $t$ be the number of local projector terms, all from the fixed finite integer-state palette with locality at most four. For a chosen overlap-error parameter $\eta\in(0,1/10)$, take a sufficiently small fixed constant $c$ and choose a dyadic number

$$\frac{c\eta^2g_0}{2t}<\lambda=2^{-b}\leq\frac{c\eta^2g_0}{t},
\qquad E=c\eta^2\lambda^{18}g_0/t.$$

For constant or inverse-polynomial $\eta$, $b=O(\log n)$, $\lambda$ and $E$ are inverse polynomial, and both are computable from the reduction's known lower bound. The inequalities, rather than equality with an unknown actual gap, justify the dyadic choice. Distinct sufficiently small constants in $\lambda$ and $E$ may be used.

The source guide is the encoded prehistory: a uniform union of $2L$ distinct computational-clock strings, each mapped to a product of $N$ four-edge register cycles. The $2L$ products have disjoint supports and equal size $4^N$; their signs in sorted coordinates are computable from the edge orientations and permutation parity. All support vertices have weight one. It is harmonic because it is a cycle in the top degree $p=2N-1$ of the register join. These facts are independent of the subsequent gap repair.

Pre-idling gives squared prehistory/history overlap $L/(L+T)$. Choose, for example, $L\geq100T$, then choose $\eta$ small enough in the displayed parameter bounds. The resulting final overlap is comfortably above $2/3$. To obtain $1-1/\mathrm{poly}(n)$ overlap, enlarge $L/T$ and decrease $\eta$ inverse-polynomially; both changes preserve polynomial reduction size.

## 3. Fixed-gadget hypotheses and corrected padding

This section states exactly the local source package used. All constants depend only on the finite palette, not on the number of qubits, number of terms, or an exponential chain dimension.

For the gadget on $m_i\leq4$ qubits, write $d_i=2m_i-1$. Its degree-$d_i$ spectrum splits into a harmonic sector, a one-state lifted-constraint sector of energy $\Theta(\lambda^{4m_i+2})$, a bulk sector of energy $\Theta(\lambda^2)$, and a remaining sector bounded below by a constant. The first two sectors together are $O(\lambda)$-close in projector norm to the local simulated-qubit space. The bulk sector is $O(\lambda)$-close to the local degree-$d_i$ central-bulk space. The lifted constraint is a cycle. The central-bulk projected boundary/coboundary pair is injective in this degree, with singular values bounded below by $c\lambda$.

These are the fixed-gadget Lemma 9.1 and its local bulk/cycle consequences. Since the local matrices have constant dimension, basiswise $O(\lambda)$ perturbation implies projector-norm $O(\lambda)$ without an input-size-dependent factor. This argument must be made BEFORE padding; basiswise closeness alone does not give a dimension-free projector bound for arbitrary growing-rank subspaces.

For gadget $i$, let $q_i=2(N-m_i)-1$ and let $P_{\rm out,i}$ project onto top-degree harmonics of the unaffected-qubit register join. Use augmented chains if there are no unaffected qubits. Its positive spectrum, including all lower-degree sectors, is bounded below by a constant: the augmented join Laplacian is a sum of fixed bowtie Laplacians.

The full join decomposition is

$$C_k(Y_i)=\bigoplus_{r+s=k-1} C_r(Y_i^{\rm loc})\otimes C_s(R_i^{\rm out}).$$

One must not replace this by a single tensor summand. In degree $p=2N-1$, the possible summands are $(r,s)=(2m_i-1,q_i)$ and $(2m_i,q_i-1)$. All modes outside the local-low-energy sectors tensored with $P_{\rm out,i}$ have a constant spectral lower bound and belong to the high sector $A_i$.

Define corrected bulk projections in every relevant degree by

$$Q_i^k=P_{\rm bulk,loc}^{\,k-q_i-1}\otimes P_{\rm out,i},$$

zero on the other bidegrees. The local bulk estimate now pads correctly. In fact,

$$R_i=(Q_i^{p-1}\partial_i,\;Q_i^{p+1}d_i),
\qquad \|R_i\|\leq C\lambda,
\qquad \|R_i Q_i^p x\|\geq c\lambda\|Q_i^p x\|.\tag{1}$$

Proof: the outside harmonic projector annihilates both outside differentials on either side. In the join differential only the local differential survives, and the local bulk vertices all have weight $\lambda$. The lower bound is the fixed local injectivity bound tensored with an orthogonal projector. In particular it is uniform even when the outside harmonic rank is exponential. Although $Q_i^k$ need not be a coordinate projector, its range is supported on simplices in gadget $i$; projected boundary/coboundary outputs cannot receive contributions from a different gadget.

**Why this correction matters.** KK arXiv Claim 10.2 literally asserts (1)'s upper bound with the full coordinate bulk projector and arbitrary padded inputs. Take a normalized local bulk simplex $\tau$ and join it with a single outside unit-weight register edge $[u,v]$. The boundary has terms $\tau*[v]-\tau*[u]$ of norm $\sqrt2$, still supported in the bulk. It is not $O(\lambda)$ as $\lambda\to0$. This is an analytic counterexample to the literal padded claim, not to the corrected harmonic-outside projection nor to the hardness theorem.

## 4. Arbitrary-state concentration: detailed proposed repair

Let $\Pi_0$ project onto register chains, $\Pi_i$ onto chains containing vertices of gadget $i$, and $P$ onto the embedded $N$-qubit harmonic space. There are no edges between different gadgets, so $\Pi_0+\sum_i\Pi_i=I$. Put $x_i=(\Pi_0+\Pi_i)\sigma$ for any normalized full-chain state of energy at most $E$.

Write $A_i,B_i,\widehat\Phi_i,K_i$ for the mutually orthogonal single-gadget high, bulk, lifted-constraint, and kernel projectors. Thus

$$A_i+B_i+\widehat\Phi_i+K_i=\Pi_0+\Pi_i,
\quad \|K_i-(P-\Phi_i)\|\leq C\lambda,
\quad \|B_i-Q_i^p\|\leq C\lambda,\tag{2}$$

where $\sum_i\Phi_i=sHs^\dagger$. All projector differences in (2) follow in constant dimension and then tensor with $P_{\rm out,i}$.

1. **High-sector bound.** Up-Laplacian energy splits by gadgets. The off-register part of $\partial_i x_i$ also has norm at most $\sqrt E$. The only discrepancy in the register boundary is interference from the other gadgets. The interface map

   $$T_j=\Pi_0^{p-1}\partial\Pi_j^p$$

   removes the unique gadget vertex of a simplex; its coefficient is $\lambda$. More explicitly, partition the domain by that vertex $u$. On each orthogonal piece the deletion is a signed partial isometry $\lambda D_u$, so $T_jT_j^\dagger=\lambda^2\sum_uD_uD_u^\dagger\preceq\lambda^2N_jI$, where $N_j$ is the constant number of new vertices of that palette gadget. This verifies the bound on every outside bidegree without requiring a common tensor decomposition across gadgets. Cauchy--Schwarz and $\sum_j\|\Pi_j\sigma\|^2\leq1$ give

   $$\left\|\sum_{j\ne i}T_j\Pi_j\sigma\right\|\leq C\lambda\sqrt t.$$

   Therefore the single-gadget energy of $x_i$ is at most $C(E+\lambda^2t)$, and

   $$\|A_ix_i\|\leq C(\sqrt E+\lambda\sqrt t).\tag{3}$$

2. **Bulk-sector bound.** Let $F_i=\widehat\Phi_i+K_i$ and $Q=Q_i^p$. The identity

   $$I=Q+(I-Q)A_i+(I-Q)B_i+F_i-QF_i$$

   holds on the single-gadget chain space. Apply $R_i$ and use (1)--(3). The full-state energy controls $\|R_ix_i\|\leq\sqrt E$. Further, $\|(I-Q)B_i\|,\|QF_i\|\leq C\lambda$ and $\|R_iF_i\|\leq C\lambda^{2m_i+1}$, by the local low-energy spectrum. Consequently

   $$c\lambda\|Qx_i\|\leq\sqrt E+C\lambda\|A_ix_i\|+C\lambda^2,
   \qquad
   \|B_ix_i\|^2\leq C(E/\lambda^2+\lambda^2t).\tag{4}$$

3. **Lifted constraints.** Each lifted-constraint sector is a cycle and has up energy at least $c\lambda^{18}$. Since the global up Laplacian is the sum of the single-gadget up Laplacians,

   $$\sum_i\langle\sigma,\widehat\Phi_i\sigma\rangle\leq CE/\lambda^{18}.$$

   The weaker bound $CtE/\lambda^{18}$ is sufficient and matches the following uniform bookkeeping.

4. **Concentration inequality.** Sum (2) in the complete-projector identity, then insert (3)--(4). Dropping the nonpositive term $-(t-1)\langle\Pi_0-P\rangle$ gives

   $$1\leq\langle\sigma,P\sigma\rangle-\langle\sigma,sHs^\dagger\sigma\rangle
      +C\left(t\lambda+t^2\lambda^2+tE/\lambda^{18}\right).\tag{5}$$

   Let $S$ project onto $s(\ker H)$, allowing $S=0$ in NO. If the nonzero spectrum of $H$ is at least $g_0\leq1$, then

   $$\boxed{\quad\|(I-S)\sigma\|^2
   \leq \frac C{g_0}\left(t\lambda+t^2\lambda^2+tE/\lambda^{18}\right).\quad}\tag{6}$$

   Indeed, with $a=\|(I-P)\sigma\|^2$ and $b=\|(P-S)\sigma\|^2$, (5) implies $a+g_0b\leq R$, whence $a+b\leq R/g_0$. No assumption $\sigma\in\operatorname{im}s$ is used.

5. **Gap and guide.** Choose parameters in Section 2 so the right side of (6) is at most $\eta^2<1$. Every vector in the spectral subspace $L_{<E}$ satisfies (6), so restriction of $S$ to that space is injective and $\dim L_{<E}\leq\dim\ker H$. In NO, this excludes both zero and sub-$E$ eigenvalues. In the source YES family $\dim\ker H=1$, while the exact gadget topology supplies at least one nonzero surviving homology class; hence $\dim\ker\Delta=1$ and the next eigenvalue is at least $E$. Applying (6) to its unit harmonic vector gives projector distance from the encoded history line at most $\eta$. Thus for the prehistory guide $\psi$,

   $$\langle\psi,P_{\ker\Delta}\psi\rangle
       \geq |\langle\psi,\sigma_{\rm hist}\rangle|^2-\eta
       =L/(L+T)-\eta.$$

This repairs the specific domain/closeness steps without assuming exact equality of encoded and harmonic vectors. It also avoids a general many-dimensional global topology assertion for the June hard family: the one-dimensional case needs only existence of one surviving class. The independent companion note analyzes the more general dimension-$r$ version.

## 5. Unweighting proof and exact size/gap bookkeeping

Set $M=\lambda^{-2}=2^{2b}$. Replace every register vertex by a clique of size $M$, and every added gadget vertex by a singleton. Across both filtration levels use the same copies. More generally, for a finite inclusion diagram with common positive weights and common integers $f_v=Mw(v)^2$, replace $v$ by a clique of $f_v$ copies.

On normalized weighted simplex coordinates define

$$U_{i,k}|\sigma\rangle_w
   =\left(\prod_{v\in\sigma}f_v\right)^{-1/2}
      \sum_{\text{one copy of each }v\in\sigma}|\widehat\sigma\rangle.$$

Orient each lift consistently with its base simplex. Distinct base simplices have disjoint lift supports. Termwise counting proves

$$U_i^\dagger U_i=I,\qquad \widehat J_{ij}U_i=U_jJ_{ij},
\qquad \widehat dU=\sqrt M\,Ud_w,\qquad
\widehat\Delta U=M U\Delta_w.$$

There is no inclusion normalization factor. The $\sqrt M$ factor belongs to the differential and becomes $M$ for the Laplacian. In raw weighted coordinates the isometry carries the degree factor $M^{-(k+1)/2}$, which cancels between same-degree inclusions.

The block-permutation fixed space consists exactly of these orbit averages: a simplex with two vertices in one block changes orientation under their transposition and contributes no fixed vector. Repeated-block coboundary contributions cancel. The asymmetric gap follows by orthogonally splitting according to the first block whose averaging projector vanishes. Such vectors live in the expanded star of that block. The augmented join Laplacian splits as the complete-block Laplacian plus the nonnegative link Laplacian; the former is $f_vI$ away from its empty-block component, which is absent in that asymmetric sector. In degree zero, the augmentation correction vanishes on the asymmetric sector. This proves, for an arbitrary base clique complex,

$$\widehat\Delta|_{T^\perp}\succeq\min_v f_v,
\quad \widehat P_i=U_iP_iU_i^\dagger,
\quad \gamma_+(\widehat\Delta_i)\geq
\min\{M\gamma_+(\Delta_i),\min_vf_v\}.$$

For the hard family, $\min f_v=1$ and the final gap is at least $\min\{ME,1\}$. The graph has $N_{\rm reg}M+N_{\rm gadget}$ vertices, polynomial in the original instance length; the lower bound is inverse polynomial in this new size as well. Ordinary Hamiltonian normalization adds only polynomial factors.

Every guide simplex uses $p+1$ register vertices, so it has exactly $M^{p+1}$ lifts and the lifted amplitudes have equal magnitude. Append $p+1$ independent $[M]$ copy coordinates and retain the source orientation sign. Since $M$ is a power of two, this adds $(p+1)\log_2M$ Hadamards and copy bits, plus polynomial reversible relabeling. Alternatively expand each four-edge factor to its $4M^2$ copied oriented edges; this still has polynomial description size. No exponential simplex listing is performed.

The initial guide is still exactly harmonic: both differential identities apply even though the blown-up initial complex now contains many higher-dimensional simplices inside copy blocks. Their symmetric coboundary contributions cancel. If a target requires equal vertex sets, absent future gadget vertices can be inserted initially as isolated vertices; $p\geq1$ makes them irrelevant to the guide and its degree-$p$ Laplacian.

## 6. Whole-diagram preservation and limits on novelty

For each arrow, the harmonic map $A_{ij}=P_jJ_{ij}|_{\ker\Delta_i}$ satisfies

$$\widehat A_{ij}U_i=U_jA_{ij}.$$

Thus the entire harmonic representation is unitarily naturally isomorphic: every arrow singular value, guided overlap, and algebraic rank invariant is preserved. This holds for an arbitrary finite inclusion diagram, including zigzags and finite-poset diagrams with compatible fixed weights. It is not an algorithm for efficiently reading all those invariants.

This extension beyond one pair is useful but elementary. Enlarging every multiplicity by the same factor scales the symmetric Laplacian and the asymmetric lower bound while also enlarging the graph; it does not by itself improve a normalized computational condition parameter. Routine perturbation theory could add weight-rounding tolerance under all-level gap promises, but exact rank and a strictly harmonic uniform guide need additional care. No substantial new robustness theorem was proved here.

**Novelty assessment:** likely a short functorial corollary to June plus August, with a technically worthwhile source-proof repair, not presently a strong standalone ITCS direction. The August paper itself discusses harmonic-persistence unweighting as an outlook; this bounded audit has not established the absence of a later resolution. Distinguish two normalizations: dividing by the full simplex count can change exponentially after blow-up, whereas the July normalized harmonic-persistence ratio $\beta^{1,2}_p/\beta^1_p$ IS preserved by this natural isomorphism when its denominator is nonzero. Nevertheless, the guided hard family alone is not a hardness reduction for that rank ratio; unweighting cannot turn an equal-complex quasi-hard instance into a nontrivial rank-ratio instance. Do not claim an algorithm for generalized rank or full indecomposable decomposition from this corollary.

The exponent $18$ in Sections 2--5 is specific to the June finite palette with $m\leq4$. A different circuit-Hamiltonian construction of locality $m$ must instead use $\kappa=4m+2$ throughout the lifted-constraint and energy bounds; locality five or six cannot silently inherit exponent eighteen.

## 7. Remaining checks and completed checks

Completed: exact normalized-chain convention; common-copy inclusion; fixed/asymmetric-sector argument; source weights and guide support; dyadic computability; polynomial graph/preparation size; complex-versus-real compatibility; NO-overlap threshold bookkeeping; published June domain mismatch. The proof-writer discipline led to isolating the fixed-size gadget assumptions and writing the concentration inequality instead of repeating the unsupported global-closeness citation.

Independent session checks: the root checked the Section 4 concentration/min--max algebra; the companion audit checked the interface bound and the spectral-to-exact-filling argument in Section 8. No remaining cross-support interference flaw was identified, conditional on the isolated local facts. Pending: source-version comparison against the inaccessible SIAM full text and a from-first-principles audit of the single-gadget spectral-sequence theorem, which was inspected and imported rather than fully re-proved here. These are explicit source dependencies, not a demonstrated fatal obstruction to the unweighted theorem.

Earlier tiny numerical conventions check: `tda_probe/check_common_blowup.py` verifies path-to-triangle inclusions with unequal fixed copy multiplicities. The new `round2/check_padded_bulk.py` checks the exact rational coefficients in Section 3's counterexample and their cancellation for a harmonic outside cycle. It is not a check of the global gadget spectrum. No large simulation was run.

## 8. Exact filling follows from the same single-gadget package

**LOCAL DERIVATION; a stronger dependency simplification.** A new Section-8 relative-homology theorem is unnecessary for the exact relation $B_p(Y_j)\cap V=\operatorname{ran}\Phi_j$. It follows from the already used single-gadget nullity and kernel-projector limit. Here $R$ is the register complex, $V=Z_p(R)=H_p(R)$ is its top-degree cycle space, and $Y_j$ is the register with just gadget $j$ added and padded.

1. **Weight invariance on register boundaries.** Identify each normalized chain basis with the ordinary coordinate basis. Let $W_k(\lambda)$ be diagonal with entry $\prod_{v\in\sigma}w(v)$ on simplex $\sigma$. The stipulated boundary convention gives

   $$\partial_{w,k}=W_{k-1}^{-1}\partial_{1,k}W_k,
   \qquad B_p(Y_j,w)=W_p^{-1}B_p(Y_j,1).$$

   Since every register vertex has weight one, $W_pv=v$ for every $v\in V$. Consequently

   $$\mathcal W_j:=B_p(Y_j,w)\cap V=B_p(Y_j,1)\cap V$$

   is exactly independent of $\lambda>0$ on the fixed gadget graph.

2. **The kernel limit excludes unintended filled directions.** Every $v\in\mathcal W_j$ is orthogonal to every harmonic vector of $Y_j$ for all sufficiently small positive $\lambda$. The fixed-gadget spectral package, padded by the unaffected harmonic factor, gives

   $$P_{\ker\Delta_p(Y_j,w)}\longrightarrow P_V-\Phi_j\qquad(\lambda\to0).$$

   Therefore $(P_V-\Phi_j)v=0$ and $\mathcal W_j\subseteq\operatorname{ran}\Phi_j$. This argument does not require an exact equality of harmonic vectors at any finite $\lambda$.

3. **Nullity supplies the reverse inclusion by dimension.** The inclusion map from $V$ into $H_p(Y_j,w)$ has kernel exactly $\mathcal W_j$. The same local package gives

   $$\dim H_p(Y_j,w)=(2^{m_j}-1)2^{N-m_j}
      =\dim V-\operatorname{rank}\Phi_j.$$

   Hence rank-nullity implies $\dim\mathcal W_j\geq\operatorname{rank}\Phi_j$. Together with Step 2,

   $$\boxed{B_p(Y_j,w)\cap V=\operatorname{ran}\Phi_j.}$$

4. **Several gadgets and naturality.** Let $Y_A$ contain a subset $A$ of the gadgets. No simplex contains new vertices from different gadgets. Since the register has no $(p+1)$-simplices, any $(p+1)$-chain splits as $b=\sum_{j\in A}b_j$. If $\partial b\in V$, its off-register part vanishes separately in each gadget; thus each $\partial b_j$ is a register cycle, and belongs to $\operatorname{ran}\Phi_j$ by Step 3. The reverse containment is immediate from the individual fillings. Therefore

   $$B_p(Y_A,w)\cap V=\sum_{j\in A}\operatorname{ran}\Phi_j,
   \qquad
   V\big/\sum_{j\in A}\operatorname{ran}\Phi_j\hookrightarrow H_p(Y_A,w).$$

   The injected quotient has dimension $\dim\ker H_A$, where $H_A=\sum_{j\in A}\Phi_j$ on $V$. Under the concentration estimate for $H_A$, min--max gives the reverse dimension inequality, so the injection is an isomorphism and excludes all extra harmonics. For $A\subseteq B$, the same register cycle represents both images; hence these isomorphisms commute exactly with inclusions and the corresponding quotient maps.

This closes the exact-filling/naturality dependency conditional only on the fixed-gadget spectral package and the checked absence of edges between distinct gadgets. It does not validate an arbitrary-gate-set gadget palette: each additional finite palette must satisfy that package, and its maximum locality determines $\kappa=4m+2$. It also does not on its own construct a promise-hard normalized-rank instance; that is a separate reduction task.
