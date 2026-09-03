# Certified local palette for a weighted unary history

2026-09-02. Bounded source audit and local derivation. This addendum replaces the unsupported “finite integer palette implies a proved gadget” inference in Section G of `NORMALIZED_PERSISTENCE_PROBE.md`. It does not replace the fixed-gadget spectral theorem or claim unrestricted gate-set hardness.

## Verdict and exact source boundary

The unary construction **survives after replacing each Hadamard-pair transition by two explicitly specified transitions**. Every resulting rank-one constraint is a product of computational-basis factors with a previously checked one- or two-qubit state. No general integer-state gadget theorem is needed.

**VERIFIED SOURCE.** [King–Kohler, Section 5 and Lemma 9.1](https://arxiv.org/html/2311.17234v2) distinguishes the conjectural general integer-state construction from the spectral theorem for a correctly implementing Section-8.2 gadget. [Rudolph, Appendix D.1](https://arxiv.org/html/2411.02681v2#A4.SS1) supplies concrete two-qubit states, reports their algebraic homology checks, and proves closure under tensor products by joining the implementing spheres and their maps. Its footnote 17 explicitly warns that the more general construction lacks a correctness proof. [Hayakawa, Lemma 5.4](https://arxiv.org/html/2608.02726v1#S5) likewise uses the concrete family and join closure. These statements support the restricted palette below, not all six-qubit integer states.

Version status: Rudolph was checked in arXiv v2, 11 April 2025. The [current arXiv record](https://arxiv.org/abs/2411.02681) displays no journal reference; no claim of journal-publication verification is made. The August source is a preprint. The published June source and its separate proof-domain issue are audited in `UNWEIGHTING_AUDIT.md`.

## 1. Explicit positive local terms

Write $H=2^{-1/2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$ and $K=\sqrt2H$, so $K=K^\dagger$ and $K^2=2I$. The two active registers below are the changing unary clock bit $c$ and one work bit. Define four normalized forbidden vectors

$$
\begin{aligned}
u_0&=(|00\rangle+|01\rangle-|10\rangle)/\sqrt3,\\
u_1&=(|00\rangle-|01\rangle-|11\rangle)/\sqrt3,\\
d_0&=(|00\rangle-|10\rangle-|11\rangle)/\sqrt3,\\
d_1&=(|01\rangle-|10\rangle+|11\rangle)/\sqrt3.
\end{aligned}
$$

Equivalently,

$$u_z=(|0\rangle K|z\rangle-|1\rangle|z\rangle)/\sqrt3,
\qquad d_z=(|0\rangle|z\rangle-|1\rangle K|z\rangle)/\sqrt3.$$

Each pair is orthonormal: its Gram matrix is $(K^2+I)/3=I$. Therefore $P_\uparrow=\sum_z|u_z\rangle\langle u_z|$ and $P_\downarrow=\sum_z|d_z\rangle\langle d_z|$ are orthogonal projectors, not an indefinite formal propagation expression.

For a two-time state $|0\rangle f_0+|1\rangle f_1$,

$$\langle P_\uparrow\rangle=\|Kf_0-f_1\|^2/3,
\qquad \langle P_\downarrow\rangle=\|f_0-Kf_1\|^2/3.$$

Thus the up edge enforces $f_1=\sqrt2Hf_0$, and the down edge enforces $f_1=Hf_0/\sqrt2$. Apply the up edge on work bit one and then the down edge on work bit two. The composite transfer is exactly $H\otimes H$; the intermediate norm is multiplied by $\sqrt2$ and the final norm returns to its initial value. These are exact identities over rational projector matrices. The gain/loss factorization itself already appears in Rudolph's Appendix D.1 and is credited to that source; our contribution here is its explicit adaptation and analysis for this weighted unary counting history.

For an interior unary transition, tensor the active forbidden vector with $|1\rangle$ on the preceding clock bit and $|0\rangle$ on the following clock bit, and permute tensor factors into the register order. End sentinels are omitted. The resulting Hadamard terms have locality at most four.

For $X$, $\mathrm{CX}$, and $\mathrm{CCX}$, retain the usual vectors

$$ (|0,z\rangle-|1,Uz\rangle)/\sqrt2.$$

For each individual basis string $z$, these gates either leave all work bits unchanged or flip only the target bit. Consequently the vector factors into fixed basis bits and a one-qubit difference, or an active two-qubit two-term state. In particular, a Toffoli term does not require an arbitrary entangled six-qubit gadget. Its fixed controls and two unary guards give total locality at most six. Clock, input, and output penalties are basis projectors.

## 2. Exact match to the checked states; what is being joined

After its fixed factor is removed, Rudolph's displayed $h_{23}$ pair is

$$a=|10\rangle+|11\rangle-|00\rangle,
\qquad b=|10\rangle-|11\rangle-|01\rangle.$$

Our down pair is $-a,-b$, and our up pair is $X_c a,X_c b$, with common normalization $\sqrt3$. Exchanging a logical register's zero and one cycles is a relabeling of its two bowtie petals; a global sign does not change a projector. This identification uses the $h_{23}$ pair and does **not** depend on the apparently inconsistent second vector in the source's displayed $h_{12}$ list.

The tensor-product operation applies to the **implementing spheres and attaching maps**, not to a disjoint union of already filled graphs. If $K_i$ triangulates $S^{2m_i-1}$ and maps to the encoded cycle for $\phi_i$, then $K_1*K_2$ is a clique sphere of dimension $2(m_1+m_2)-1$ and maps to the cycle for $\phi_1\otimes\phi_2$. Applying the standard thickening/coning construction to this joined input implements the product constraint. Basis factors use the elementary one-qubit cycle sphere. Only a constant number of joins is needed for any term.

Therefore this is a fixed, constructible finite family of correctly implementing Section-8.2 gadgets. The imported single-gadget spectral package applies with the **total support locality**, not merely the active two-qubit size. The safe common exponent remains

$$\kappa=4m_{\max}+2=26.$$

This closes the palette-scope gap. It is not a new independent proof of King–Kohler's spectral-sequence theorem or of the source's finite algebraic gadget calculations. Those are explicit literature dependencies, as in the preceding audit.

## 3. Weighted-path gaps and unchanged kernel fractions

This section is a **LOCAL DERIVATION**, algebra-checked independently by the root. Let $L$ count legal clock positions after the split. Let $s_t=\sqrt2$ immediately after an up edge and $s_t=1$ otherwise; no other gate is inserted between the paired up and down edges. Put $Z=\sum_t s_t^2$, so $L\leq Z\leq2L$ and $s_0=s_{L-1}=1$.

Let $V_t$ be the unitary prefix with the scalar factors removed. A history for valid input $v$ is

$$\mathcal Vv=Z^{-1/2}\sum_{t=0}^{L-1}s_t|t\rangle V_tv.$$

This is an isometry because every $V_t$ is unitary and $Z$ is input-independent. Its final prefix equals the original $G_2$ verifier exactly.

For a general legal-clock state write $f_t=s_tV_t\xi_t$. This is a change of variables, not a unitary similarity: the norm becomes weighted. Every split-Hadamard edge contributes $(2/3)\|\xi_t-\xi_{t-1}\|^2$; every ordinary unitary edge contributes $(1/2)\|\xi_t-\xi_{t-1}\|^2$. Indeed, an up edge starts with $s_{t-1}=1$ and ends with $s_t=\sqrt2$, whereas its immediately following down edge starts with $s_{t-1}=\sqrt2$ and ends with $s_t=1$. The gain/loss pair is consecutive, so every ordinary edge has both endpoint scales one. This proves the asserted coefficients without assuming that scalar factors commute with an arbitrary clock reordering.

Put $w_t=s_t^2\in[1,2]$, $W=\sum_tw_t=Z$, and let $A_{\rm in}$ be the sum of invalid initially fixed-bit projectors. For any legal state, its squared norm and quadratic-form energy are exactly

$$N(\xi)=\sum_tw_t\|\xi_t\|^2,\qquad
E(\xi)=\sum_{t=1}^{L-1}c_t\|\xi_t-\xi_{t-1}\|^2
       +\langle\xi_0,A_{\rm in}\xi_0\rangle,
\qquad c_t\in\{1/2,2/3\}.$$

Let $C=\ker A_{\rm in}$ be the clean input subspace and let $B=C^\perp$ be its dirty complement. The input penalty satisfies $A_{\rm in}|_B\succeq I_B$. In these prefix-rotated coordinates, the projectors onto $C$ and $B$ are the same at every time. Thus $\xi_t=\xi_t^C+\xi_t^B$ gives an orthogonal splitting of both $N$ and $E$, although the corresponding work subspaces in the original coordinates are $V_tC$ and $V_tB$.

The zero-energy states are precisely the histories of $v\in C$: every edge forces $\xi_t=v$ and the anchor forces $v\in C$. A legal state orthogonal to all these histories satisfies the **weighted** clean-sector mean condition

$$\sum_tw_t\xi_t^C=0,$$

since its inner product with $\mathcal Vv$ is $W^{-1/2}\langle v,\sum_tw_t\xi_t\rangle$.

For the clean sector, set $D_C=\sum_{t=1}^{L-1}\|\xi_t^C-\xi_{t-1}^C\|^2$. Weighted variance and the path Cauchy--Schwarz inequality give

$$\begin{aligned}
N_C
 &=\frac1{2W}\sum_{i,j}w_iw_j\|\xi_i^C-\xi_j^C\|^2\\
 &\leq\frac{W(L-1)}2D_C
 \leq L^2D_C\leq2L^2E_C.
\end{aligned}$$

Here $\|\xi_i^C-\xi_j^C\|^2\leq |i-j|D_C\leq(L-1)D_C$ and $W\leq2L$. The identity uses the weighted mean condition; ordinary unweighted orthogonality would not suffice.

For the dirty sector put $D_B=\sum_{t=1}^{L-1}\|\xi_t^B-\xi_{t-1}^B\|^2$ and $a=\|\xi_0^B\|^2$. For every $t$,

$$\|\xi_t^B\|^2\leq2a+2(L-1)D_B.$$

Consequently, for $L\geq1$,

$$N_B\leq4La+4L(L-1)D_B
       \leq8L^2(a+D_B/2)\leq8L^2E_B.$$

No mean condition is used here. Adding the two sectors proves $N\leq8L^2E$ on the orthogonal complement of the entire legal kernel, including if $C=0$. Hence the safe bound is

$$\gamma_+(H_1)\geq1/(8L^2).$$

The local clock guards preserve the legal-clock subspace; Hermiticity preserves its orthogonal complement. Illegal clock strings have energy at least one from the clock penalty, so they cannot weaken this bound or supply extra zeros.

Let $D$ be the valid input dimension, $M$ its acceptance operator, and $S=\ker(I-M)$. Then

$$\dim\ker H_1=D,\qquad \dim\ker H_2=\dim S,
\qquad \mathcal V^\dagger H_{\rm out}\mathcal V=(I-M)/Z.$$

Under $M|_{S^\perp}\preceq I/3$, the latter has positive eigenvalues at least $\alpha=1/(3L)$. For completeness, the following argument proves the required two-kernel bound and does not assume $S\neq0$.

Let $\mathcal K=\ker H_1$, let $R=H_{\rm out}$ be the output-penalty orthogonal projector, and put $\mathcal S=\mathcal K\cap\ker R=\mathcal V S$. Positivity gives $\ker(H_1+R)=\mathcal S$ exactly. Write $g_1=1/(8L^2)\leq1$. For any unit $\psi\perp\mathcal S$, decompose $\psi=x+y$ with $x\in\mathcal K\ominus\mathcal S$ and $y\perp\mathcal K$, and put $e=\langle\psi,(H_1+R)\psi\rangle$. Then

$$\|y\|^2\leq e/g_1,\qquad \|R\psi\|^2\leq e,$$

$$\alpha\|x\|^2\leq\|Rx\|^2
 \leq2\|R\psi\|^2+2\|Ry\|^2
 \leq2e+2e/g_1.$$

Therefore

$$1\leq e\frac{2g_1+2+\alpha}{\alpha g_1}
 \leq e\frac{2g_1+3}{\alpha g_1},\qquad
e\geq\frac{\alpha g_1}{2g_1+3}\geq\frac{\alpha g_1}{5}.$$

If $S=0$, the same argument applies to every unit $\psi$ and gives a lower bound on the minimum eigenvalue, not merely a gap above an existing zero eigenvalue. Thus

$$\gamma_+(H_2)\geq1/(120L^3).$$

The source's initial valid input dimension $D$ is positive, as required to normalize the initial guide. The final common kernel may have dimension zero; neither the spectral proof nor the persistence numerator requires it to be nonzero.

Hence the rank-fraction thresholds from that note are unchanged: if $p=\operatorname{Tr}M/D$, then $f\leq p\leq1/3+(2/3)f$ for $f=\dim S/D$. The promises $p\geq2/3$ and $p\leq1/3$ imply respectively $f\geq1/2$ and $f\leq1/3$.

## 4. Guide preparation and error budget

The normalized initial-history projector is prepared by taking the maximally mixed valid input, preparing the known clock amplitudes $s_t/\sqrt Z$, and coherently applying the unitary prefixes $V_t$. There are only polynomially many clock positions; clock weights are the integers one and two. This yields polynomial-size BQP preparation to arbitrary inverse-polynomial trace-distance error. The intermediate unitary prefixes contain individual Hadamards; that is harmless for this **approximate BQP preparation circuit**. The original verifier and all Hamiltonian constraints remain the exact fixed-$G_2$ construction. No approximate compilation is used to infer perfect acceptance or exact kernel dimension.

The logical register-to-chain encoding is a tensor product of fixed-size oriented-cycle isometries; orientation signs and register permutations are efficiently computable. Common-copy unweighting is an additional efficiently implemented isometry. Both preserve trace distance.

More explicitly, let $Q$ be the encoded initial-history projector and $P$ the actual initial harmonic projector. The concentration/min--max repair gives equal rank $D$ and $\|P-Q\|\leq\eta$. Principal angles then give

$$\tfrac12\|P/D-Q/D\|_1\leq\eta.$$

Preparing $Q/D$ to trace distance $\varepsilon$ therefore gives distance at most $\eta+\varepsilon$ from $P/D$, before and after the common blow-up. Every measurement probability changes by at most this amount. Choose this sum comfortably below the rank-fraction separation. This is the mixed-guide input for normalized harmonic persistence, **not** a claim that an arbitrary history mixture is the June theorem's pure signed subset guide.

## 5. Honest final scope

The unproved arbitrary-integer-state step is avoidable; the explicit weighted unary construction above provides the missing source-compatible palette while retaining exact multiplicities and polynomial spectral gaps. Combined with the preceding local concentration, filling, and functorial unweighting derivations, it supports a reduction from the precisely specified fixed-$G_2$, perfect-eigenspace-separated circuit promise. It does not establish that an unrestricted formulation of SDQC1 reduces to that source, nor does it establish novelty against the July normalized-persistence paper. No full new clique-gadget simulation was run for this addendum.

**BOUNDED NUMERICAL CHECK, NOT PROOF:** reran the root's `check_weighted_history.py`. Both valid-clock fixtures passed the projector, history-isometry, output-compression, kernel-dimension, and displayed gap checks. They have kernel dimensions $(4,1)$ and $(4,3)$, respectively, with $Z=5,6$. This verifies those small matrix implementations only, not the clique-gadget topology or asymptotic theorem.

A separate 12-dimensional check of the abstract zero-common-kernel case used two work bits, three clock positions, the up/down Hadamard pair, and the projector onto the entire final-time slice. Its initial nullity was four, final nullity zero, and final minimum eigenvalue approximately $0.11808$, above $1/(120\cdot3^3)\approx0.00030864$. This check is included as `check_zero_final_kernel()` in `check_weighted_history.py`. The proof covering this case is Section 3's argument, not that numerical example.
