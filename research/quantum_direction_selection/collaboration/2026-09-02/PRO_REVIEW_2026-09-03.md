# Pro review and advancement — collected 2026-09-03

- **Status:** completed and collected; raw external-model analysis, not a correctness certificate.
- **Collected at:** 2026-09-03T10:08:55Z.
- **Conversation:** [Audit Quantum Persistence Corollary](https://chatgpt.com/c/6a98c05a-ecf4-83e8-b356-4e20dc3fde3f).
- **Request lineage:** user message 2, [source commit a46f4087693edc088663e0cbf4f6aa9961494325](https://github.com/jackal092927/ramsey-bounds-reproducible/commit/a46f4087693edc088663e0cbf4f6aa9961494325), [frozen context packet](PRO_CONTEXT_PACKET.md).
- **Visible completion:** “Worked for 155m 30s”; two completed-response controls, two user messages, no Stop answering control.
- **Identity:** visible personal account email matched the local channel registry; profile and Pro plan verified. Private email omitted from this public archive.
- **Extraction:** reconstructed from the complete visible assistant response DOM, preserving displayed LaTeX and linked citations. Repeated attachment-citation buttons refer to the frozen packet above; grouped citation pills may expose only their first source link in the prose reconstruction. This is not an independent source audit.
- **Source-panel observation:** the answer body exposed no external hyperlinks. Its Sources panel listed the uploaded packet, a pasted-text document, and the same [GitHub packet](https://github.com/jackal092927/ramsey-bounds-reproducible/blob/a46f4087693edc088663e0cbf4f6aa9961494325/research/quantum_direction_selection/collaboration/2026-09-02/PRO_CONTEXT_PACKET.md). The primary-source reading claims below are model assertions until independently checked; the panel did not provide separate paper-reading receipts.

---

# Adversarial verdict

I verified that the attached file has SHA-256

$91d330f28ac61ad0be3de4169d0ad5b26a899ff723ea9c3f31a22cb81fc77a10,$

and fetched the file at commit `a46f4087693edc088663e0cbf4f6aa9961494325`. I treated the current dossier and corrections as governing, rather than the older appendices or my previous review.

The strongest surviving result is **not** the quotient/min–max multiplicity argument. That part is standard once the right global estimate exists. The real theorem is a finite-palette, arbitrary-geometric-chain concentration statement:

every low-energy chain in the **full clique-chain space**, including arbitrary coherent combinations of all gadget-interior sectors, must concentrate near the embedded logical kernel.

Subject to an explicit finite list of local gadget certificates, that theorem gives:

$\beta_d(X_A)=\dim\ker H_A,$

a whole-positive-spectrum gap, natural rank transfer for $X_A\hookrightarrow X_B$, and hence

$\frac{\beta_d(X_A\to X_B)}{\beta_d(X_A)}
=
\frac{\dim\ker H_B}{\dim\ker H_A}.$

I found two genuine improvements:

- The lifted-sector contribution is
  
$O\!\left(\frac{E}{\lambda^{4m+2}}\right),$
  
**without** the factor $t$ appearing in King–Kohler’s termwise summation.

- Consequently, the geometric gap can be chosen as
  
$E=\Theta\!\left(\eta^2 g\lambda^{4m+2}\right),$
  
rather than $\Theta(\eta^2g\lambda^{4m+2}/t)$. With $\lambda=\Theta(\eta^2g/t)$ and $m=6$, this improves
  
$\frac{\eta^{54}g^{27}}{t^{27}}
\quad\text{to}\quad
\boxed{\frac{\eta^{54}g^{27}}{t^{26}}}.$

There is also a sharper source-Hamiltonian lemma giving

$g_2\ge \frac{1}{27L^3}$

instead of the dossier’s safe $1/(120L^3)$.

The remaining blocker is sharply localized: **the finite supported gadget palette has not yet been converted into a complete exact local certificate**. I do not certify the full reduction or paper readiness.

---

## 1. Claim-status table

| Claim | Status after review | Main reason |
| --- | --- | --- |
| Exact packet/snapshot identification | **Checked** | Local SHA matches; exact commit file fetched |
| Mixed-spectator acceptance operator $M'=M\otimes I$ | **Proved** | Acceptance ignores spectator; parity of the number of Hadamards is irrelevant |
| Fraction sandwich $f\le p\le r+(1-r)f$ | **Proved** | Direct spectral averaging |
| Error $1/24$ separates $q\ge1/2$ from $q\le1/3$ | **Proved** | Threshold $5/12$ leaves $1/24$ margin on both sides |
| Construction-fixed denominator $D>0$ | **Proved conditionally on the written history construction** | $H_1$ has exactly the valid-input history kernel |
| Weighted-history gap $g_1\ge1/(8L^2)$ | **Proof survives** | Weighted path Poincaré plus anchored dirty-sector estimate |
| Final-history gap $g_2\ge1/(120L^3)$ | **Valid but improvable** | Sharpened here to $1/(27L^3)$ |
| Single-gadget exact filling $B_d(Y_j)\cap V=\operatorname{ran}P_j$ | **Proved from the stated local spectral package** | Weight gauge, harmonic-limit inclusion, and exact nullity |
| Many-gadget filling $B_d(X_A)\cap V=\sum_j\operatorname{ran}P_j$ | **Proved** | Independent interior supports |
| Packet’s arbitrary-chain concentration theorem | **Survives conditionally** | Global proof works after corrected padded bulk sector |
| Factor $t$ in the lifted-sector estimate | **Unnecessary** | Global up-Laplacian summation removes it |
| $t^2\lambda^2$ interface term | **Worst-case necessary under present hypotheses** | Explicit shared-output coherent-leakage example |
| Exact multiplicity and gap from concentration | **Proved; standard final step** | Projection injectivity plus quotient lower bound |
| Natural rank transfer and true normalized persistence | **Proved conditionally** | Exact quotient diagram |
| Initial harmonic-mixture preparation | **Conditionally valid** | Equal-rank projector closeness gives normalized-projector trace-distance control |
| Large harmonic-map overlap | **Proved and sharpened** | Principal-angle composition |
| Restricted exact source transfer | **Proved conditionally** | Gives $q=\dim S/D$ exactly |
| Unrestricted SDQC1-hardness | **Not justified** | Exact gate-set and threshold-reduction issues remain |
| BQP-hardness | **Not justified** | Nothing here proves $\mathsf{BQP}=\mathsf{BQP}_1$ or otherwise supplies perfect completeness |
| $\mathsf{BQP}_{1}(G_2)$-hardness | **Conditional consequence** | Take $D=1$; then $q\in\{1,0\}$ |
| Unweighted common-copy transfer | **Valid downstream corollary** | Exact naturality and asymmetric-sector gap |
| Persistent-Laplacian extension | **Valid conditional structural theorem, probably secondary** | Stronger than kernel-only unweighting, but short once the block decomposition is known |
| Net/barcode route | **Mathematically useful oracle theorem, weak main-paper candidate** | Classical net constructions and output-size dependence dominate |
| Generalized-rank projector-overlap route | **Still obstructed** | Möbius example gives exponentially small overlap despite constant local constraint gaps |
| Constant-rank AIDA updates | **False in general** | Reduced update rank can grow with fibre dimension |

The dossier correctly identifies exact zero-mode multiplicity—not quasi-low-energy counting or simplex-normalized Betti numbers—as the target. 

---

# 2. Primary-source and novelty audit

## What I actually checked

| Source | Checked material | What it supports | What it does **not** establish |
| --- | --- | --- | --- |
| Crichigno–Kohler, *Quantum algorithms for topological and geometric analysis of data* / parsimonious clique-homology construction | Official published article and the source description of the parsimonious correspondence | Exact witness/groundspace multiplicity can already be represented as homology; this is prior art, not the new contribution here | A whole-positive-spectrum gap for arbitrary degenerate kernels, or functorial normalized persistence |
| King–Kohler, arXiv:2311.17234v2 | Sections 8–10, Lemma 9.1, Claims 10.1–10.4, Appendix B | Single-gadget spectral sectors, multi-gadget decomposition, up-Laplacian additivity, and the original zero-kernel gap strategy | Their padded full-coordinate bulk estimate cannot be used literally; the arXiv proof also loses a factor $t$ by bounding lifted sectors one at a time |
| Gyurik et al., arXiv:2410.21258v2 / PRX Quantum | Lemmas 6–8 and Appendix B, especially the low-energy statements | Guided harmonic-persistence hardness and the relevant history/gadget interfaces | The cited low-energy statement is initially on the simulated-qubit subspace; it is not by itself the arbitrary-full-chain theorem needed here |
| Rudolph, arXiv:2411.02681v2 | The exact $G_2$ gate-set result and Appendix D.1’s concrete integer states and joins | The finite real/rational active-state palette is plausible and exact gate-set reduction to $G_2$ is source-supported | A general correctness theorem for arbitrary integer-state gadgets; the source itself flags that broader construction issue |
| Lowe et al., arXiv:2607.03278v1 | Definition 2, Lemma 7, Problem 9, Theorem 7, Conjectures 1–2 | The exact distinction between quasi-harmonic and true normalized persistence; BQP containment under preparation/gap/overlap assumptions; true NHP hardness remains conjectural there | An exact reduction from unrestricted SDQC1 to the packet’s fixed $G_2$, fixed-threshold source |
| Hayakawa, arXiv:2608.02726v1 | Lemma 4.2, Theorem 4.3, Sections 6 and 8 | Exact block-unweighting, no extra asymmetric zero modes, and an asymmetric gap | A filtered normalized-persistence reduction; filtered extensions are left open |
| Mémoli–Wan–Wang and later persistent-Laplacian work | Persistent-Laplacian definition, nullity theorem, Schur-complement and simplicial-map extensions | Persistent Laplacians and their nullity/rank interpretation are established prior art | I found no prior block-unweighting direct-sum theorem for persistent Laplacians, but absence claims remain search-limited |

I did not obtain a line-by-line copy of the final SIAM version of King–Kohler. The concrete padded-bulk objection therefore applies to **arXiv v2 as checked**, not automatically to every later editorial version.

## Novelty verdict

The following ingredients are not new:

- parsimonious groundspace-to-homology multiplicity;

- single-gadget weighted clique simulation;

- the common-copy unweighting mechanism;

- the quotient/min–max conclusion once all-chain concentration is known;

- standard persistent-Laplacian nullity and Schur-complement facts.

The candidate new combination is:

a finite-palette, **degenerate-kernel**, arbitrary-full-chain concentration theorem that simultaneously gives exact Betti multiplicity, a whole positive gap, and a functorial quotient realization under adding projector terms.

The removal of the extra factor $t$ from the lifted-sector contribution also appears absent from King–Kohler’s written argument: their Appendix-B route applies the per-gadget bound and then sums, whereas global up-energy additivity permits summing the operator inequalities first.

My literature search did not find a later paper resolving Lowe et al.’s exact normalized-persistence conjecture or stating this arbitrary-kernel filtered realization. That supports an “apparently new” assessment, not a formal proof of novelty. Lowe et al. still present true normalized-persistence hardness as conjectural in the checked July 2026 version.

---

# 3. Strongest imported-source error: the padded bulk projector

The literal padded version of King–Kohler Claim 10.2 is false when “bulk” means the entire coordinate subspace containing a central gadget vertex.

Let $\tau$ be a local bulk simplex containing the central gadget vertex, and let $[u,v]$ be an outside unit-weight edge. For the padded join simplex

$\psi=\tau * [u,v],$

the boundary contains the two outside-deletion terms

$\pm \tau*[v]\mp\tau*[u],$

with coefficient $1$, not $O(\lambda)$. Both terms still contain the central gadget vertex. Hence the norm of the full coordinate-bulk projection of $\partial\psi$ is bounded below by a constant.

So an estimate of the form

$\|P_{\mathrm{all\ coordinate\ bulk}}\partial\|=O(\lambda)$

is false under padding.

The packet’s repair is the right one:

$Q_i
=
Q_{i,\mathrm{local\ bulk}}
\otimes P_{\mathrm{outside\ harmonic}}.$

The outside harmonic factor kills precisely the order-one boundary/coboundary produced by outside nonharmonic tensor directions. The remaining local relative pair is fixed-size, and its relevant singular value is $c_i\lambda$. This is not a cosmetic projector change; it is the distinction that makes arbitrary-chain concentration possible. The dossier’s corrected padding/interface analysis is the load-bearing part of the argument. 

---

# 4. Minimal finite-palette certificate

The global theorem should be stated conditional on the following finite local certificate, rather than vaguely importing “the gadget theorem.”

For every isomorphism type $\phi$ in the supported palette, with locality $m_\phi\le m$, certify constants independent of the large register:

- **Exact topology and nullity**
  
$\dim\ker\Delta_\phi(\lambda)
=
\dim V-\operatorname{rank}\Phi_\phi.$

- **Kernel-projector convergence**
  
$\left\|
K_\phi(\lambda)-(P_V-\Phi_\phi)
\right\|
\le C\lambda.$

- **Lifted constraint sector**
  
$\Delta_\phi^\uparrow
\succeq
c\lambda^{4m_\phi+2}\widehat\Phi_\phi,
\qquad
\operatorname{ran}\widehat\Phi_\phi\subseteq Z_d.$

- **Constant-gap high sector**
  
$\Delta_\phi\succeq cA_\phi.$

- **Correct padded bulk comparison**
  for
  
$Q_\phi=Q_{\phi,\mathrm{local}}\otimes P_{\mathrm{outside\ harmonic}},$
  
including
  
$\|B_\phi-Q_\phi\|\le C\lambda$
  
and the relative boundary/coboundary estimate
  
$c\lambda\|Q_\phi z\|
\le
\|T_\phi Q_\phi z\|.$

- **Low-sector leakage bounds**
  
$\|Q_\phi F_\phi\|\le C\lambda,
\qquad
\|T_\phi F_\phi\|\le C\lambda^{2m_\phi+1},$
  
where $F_\phi=K_\phi+\widehat\Phi_\phi$.

- **Combinatorial independence**
  no simplex contains new vertices from two distinct gadgets.

Because the palette is finite, one may then take the minimum positive lower constants and maximum upper constants. Rudolph’s concrete $G_2$ states and tensor/join construction substantially reduce this to a finite problem, but I did not independently recompute every constant-size boundary matrix or spectral valuation.

---

# 5. Exact filling from asymptotic Hodge control

This part of the dossier is correct and useful because it removes any need for a global relative-acyclicity theorem.

## Lemma 1 — exact single-gadget filling

Let $Y(\lambda)\supset R$, where all register vertices have weight $1$ and gadget vertices have weight depending on $\lambda>0$. Let

$V=Z_d(R)$

and let $\Phi$ be a projector on $V$. Assume:

$\dim\ker\Delta_d(Y(\lambda))
=
\dim V-\operatorname{rank}\Phi$

for all sufficiently small $\lambda$, and

$P_{\ker\Delta_d(Y(\lambda))}
\longrightarrow
P_V-\Phi$

in operator norm as $\lambda\to0$. Then

$\boxed{
B_d(Y)\cap V=\operatorname{ran}\Phi.
}$

### Proof

In the normalized chain basis, weighted and unweighted boundary matrices are related by diagonal gauge matrices:

$\partial_w=W_{d-1}^{-1}\partial_1W_d.$

Thus

$B_d(Y,w)=W_d^{-1}B_d(Y,1).$

Every vector of $V$ is supported entirely on weight-one register simplices, so $W_dv=v$ for $v\in V$. Consequently,

$B_d(Y,w)\cap V=B_d(Y,1)\cap V,$

independent of $\lambda$.

Write

$\mathcal W=B_d(Y)\cap V.$

For every $\lambda$, boundaries are orthogonal to harmonic chains, so

$P_{\ker\Delta_d(Y(\lambda))}v=0
\qquad(v\in\mathcal W).$

Taking $\lambda\to0$,

$(P_V-\Phi)v=0.$

Since $v\in V$,

$v=\Phi v,$

and hence

$\mathcal W\subseteq\operatorname{ran}\Phi.$

Now consider the inclusion-induced map

$V\longrightarrow H_d(Y).$

Its kernel is $\mathcal W$. Therefore

$\dim V-\dim\mathcal W
\le
\dim H_d(Y)
=
\dim V-\operatorname{rank}\Phi.$

Thus

$\dim\mathcal W\ge\operatorname{rank}\Phi.$

Together with $\mathcal W\subseteq\operatorname{ran}\Phi$, this gives equality. ∎

## Lemma 2 — many-gadget filling

Let

$X_A=R\cup\bigcup_{j\in A}Y_j$

and assume distinct gadget interiors have disjoint chain-coordinate supports and no simplex contains new vertices from two gadgets. Then

$\boxed{
B_d(X_A)\cap V
=
\sum_{j\in A}\operatorname{ran}P_j.
}$

### Proof

The inclusion “$\supseteq$” follows from Lemma 1.

For the converse, take a $(d+1)$-chain $c$ with $\partial c\in V$. Since $R$ is top-dimensional, $c$ decomposes as

$c=\sum_{j\in A}c_j,$

where $c_j$ uses only gadget $j$. The non-register coordinates of $\partial c_j$ belong to mutually orthogonal coordinate blocks. Since $\partial c$ has no non-register component, each $\partial c_j$ separately has no non-register component. Hence

$\partial c_j\in B_d(Y_j)\cap V=\operatorname{ran}P_j.$

Summing proves the claim. ∎

Thus, writing

$W_A=\sum_{j\in A}\operatorname{ran}P_j,$

there is an exact injection

$V/W_A\hookrightarrow H_d(X_A).$

The dossier’s dimension argument will later make this an isomorphism. 

---

# 6. Sharpened arbitrary-geometric-chain concentration

This is the main result.

## 6.1 Interface congestion

Let

$C_d(X_A)
=
C_d(R)\oplus\bigoplus_{i=1}^t C_i,$

and write a normalized chain as

$x=\omega_0+\sum_{i=1}^t\omega_i.$

Set

$x_i=\omega_0+\omega_i,$

viewed in the single-gadget complex $R\cup Y_i$.

Define the register-output interface map

$L_i
=
\Pi_R^{d-1}\partial\Pi_i^d$

and the block row

$L=[L_1\;\cdots\;L_t].$

Write

$\boxed{
\rho_A=\lambda^{-2}\|L\|^2.
}$

The packet’s orthogonal-input correction gives

$\rho_A\le N_*t,$

where $N_*$ is the maximum number of relevant new vertices in one fixed palette gadget.

There is also an exact combinatorial interpretation. Partition $L_i$ according to the deleted new vertex $u$:

$L_i=\lambda[D_{i,u}]_u.$

Every $D_{i,u}$ is a signed partial permutation: it sends the simplex

$\tau\cup\{u\}$ to $\pm\tau$. Hence $D_{i,u}D_{i,u}^*$ is a coordinate projector and

$LL^*
=
\lambda^2\sum_{i,u}D_{i,u}D_{i,u}^*.$

Therefore

$\boxed{
\rho_A
=
\max_{\tau\in R_{d-1}}
\#\{(i,u):\tau\cup\{u\}\in X_A^{(d)}\}.
}$

It is the maximum one-new-vertex coface congestion of a register $(d-1)$-simplex.

---

## 6.2 Aggregate single-gadget energy

Let

$e=\langle x,\Delta_Ax\rangle
=
\|\partial x\|^2+\|\partial^*x\|^2.$

Write

$y_i=L_i\omega_i,
\qquad
y=\sum_i y_i.$

Let $a$ be the register boundary of $\omega_0$, and let $z_i$ be the non-register boundary output of $\omega_i$. Then

$\partial x
=
(a+y)\oplus\bigoplus_i z_i,$

whereas the boundary in the $i$-th single-gadget complex is

$\partial_i x_i=(a+y_i)\oplus z_i.$

Put $r=a+y$. Since

$a+y_i=r-(y-y_i),$

we have

$\sum_i\|a+y_i\|^2
\le
2t\|r\|^2
+
2\sum_i\|y-y_i\|^2.$

Moreover,

$\sum_i\|y-y_i\|^2
=
(t-2)\|y\|^2+\sum_i\|y_i\|^2.$

The two interface bounds give

$\|y\|^2\le \rho_A\lambda^2,
\qquad
\sum_i\|y_i\|^2\le N_*\lambda^2.$

The up-boundary outputs of distinct gadgets are orthogonal and exactly partition the global up-boundary output. Consequently,

$\boxed{
\sum_i\langle x_i,\Delta_i x_i\rangle
\le
C\Bigl(
t e+t(1+\rho_A)\lambda^2
\Bigr).
}$

If $A_i$ denotes the constant-gap high sector of gadget $i$, the finite-palette high-sector estimate yields

$\boxed{
\sum_i\|A_i x_i\|^2
\le
C\Bigl(
t e+t(1+\rho_A)\lambda^2
\Bigr).
}$

---

## 6.3 Aggregate bulk bound

Let $B_i$ be the local bulk spectral sector and $Q_i$ the corrected padded bulk subspace. Let $T_i$ collect the projected boundary and coboundary outputs used by the relative bulk estimate.

The local certificate implies

$c\lambda\|Q_i x_i\|
\le
\|T_i x_i\|
+
C\lambda\|A_i x_i\|
+
C\lambda^2\|x_i\|.$

Squaring and summing gives

$\sum_i\|Q_i x_i\|^2
\le
C\left(
\frac{\sum_i\|T_i x_i\|^2}{\lambda^2}
+
\sum_i\|A_i x_i\|^2
+
t\lambda^2
\right).$

The ranges of the $T_i$ contain new vertices from distinct gadgets, so they are orthogonal, and

$\sum_i\|T_i x_i\|^2\le e.$

Using $\|B_i-Q_i\|\le C\lambda$,

$\boxed{
\sum_i\|B_i x_i\|^2
\le
C\left(
\frac{e}{\lambda^2}
+
t e
+
t(1+\rho_A)\lambda^2
\right).
}$

This improves the naïve termwise $t e/\lambda^2$ estimate to $e/\lambda^2$.

---

## 6.4 The factor-$t$ removal for lifted sectors

Let $\widehat\Phi_i$ be the lifted constraint sector. For each palette element,

$\Delta_i^\uparrow
\succeq
c_i\lambda^{\kappa_i}\widehat\Phi_i,
\qquad
\kappa_i=4m_i+2.$

Set

$\kappa=\max_i\kappa_i=4m+2.$

Since $0<\lambda\le1$ and $\kappa_i\le\kappa$,

$\lambda^{\kappa_i}\ge\lambda^\kappa.$

The global up-Laplacian is exactly the sum

$\Delta_A^\uparrow=\sum_i\Delta_i^\uparrow.$

Therefore, as an operator inequality,

$\Delta_A^\uparrow
\succeq
c_*\lambda^\kappa
\sum_i\widehat\Phi_i,
\qquad
c_*=\min_i c_i>0.$

No orthogonality among the $\widehat\Phi_i$ is required. Taking expectation in $x$,

$\boxed{
\sum_i\langle x,\widehat\Phi_i x\rangle
\le
\frac{e}{c_*\lambda^\kappa}.
}$

This is the missing aggregate step. Bounding each term by $e/\lambda^\kappa$ and then summing is unnecessarily lossy.

---

## 6.5 The concentration identity

For the $i$-th single gadget, let

$I_i=A_i+B_i+\widehat\Phi_i+K_i.$

Summing the identities on $x_i$,

$\sum_i\|x_i\|^2
=
1+(t-1)\|\omega_0\|^2.$

The local kernel projector satisfies

$\|K_i-(P_V-\Phi_i)\|\le C\lambda.$

Thus

$\sum_i\langle x_i,K_ix_i\rangle
=
t\langle x,P_Vx\rangle
-
\langle x,H_A^{\mathrm{emb}}x\rangle
+
O(t\lambda).$

Subtracting the repeated register norm gives

$\begin{aligned}
1
={}&
\langle x,P_Vx\rangle
-
\langle x,H_A^{\mathrm{emb}}x\rangle\\
&-(t-1)
\langle\omega_0,(I-P_V)\omega_0\rangle\\
&+\sum_i\|A_ix_i\|^2
+\sum_i\|B_ix_i\|^2
+\sum_i\langle x,\widehat\Phi_i x\rangle
+O(t\lambda).
\end{aligned}$

The second line is nonpositive and may be discarded.

Combining the three aggregate estimates proves:

## Theorem 3 — sharpened arbitrary-chain concentration

Assume the finite-palette certificate above. For every normalized degree-$d$ chain $x$, with

$e=\langle x,\Delta_Ax\rangle,$
$\begin{aligned}
1
\le{}&
\langle x,P_Vx\rangle
-
\langle x,H_A^{\mathrm{emb}}x\rangle\\
&+
C\left[
t\lambda
+t e
+t(1+\rho_A)\lambda^2
+\frac{e}{\lambda^2}
+\frac{e}{\lambda^\kappa}
\right].
\end{aligned}$

If

$\lambda\le\frac1t
\qquad\text{and}\qquad
\kappa\ge2,$

then

$te\le \frac{e}{\lambda^\kappa},
\qquad
\frac{e}{\lambda^2}\le\frac{e}{\lambda^\kappa},$

and hence

$\boxed{
1
\le
\langle x,P_Vx\rangle
-
\langle x,H_A^{\mathrm{emb}}x\rangle
+
C\left(
t\lambda
+t(1+\rho_A)\lambda^2
+\frac{e}{\lambda^\kappa}
\right).
}$

Using only $\rho_A\le N_*t$,

$\boxed{
1
\le
\langle x,P_Vx\rangle
-
\langle x,H_A^{\mathrm{emb}}x\rangle
+
C\left(
t\lambda+t^2\lambda^2+\frac{e}{\lambda^\kappa}
\right).
}$

This is the packet’s desired arbitrary-full-chain estimate, but with the factor $t$ removed from the energy-over-lifted-gap term.

---

# 7. Improved geometric gap

Suppose

$H_A\succeq g(P_V-P_A),$

where $P_A$ projects onto $K_A=\ker H_A$, and $0<g\le1$.

For any normalized $x$,

$\begin{aligned}
g\bigl(1-\langle x,P_Ax\rangle\bigr)
&=
g\langle x,(I-P_V)x\rangle
+
g\langle x,(P_V-P_A)x\rangle\\
&\le
1-\langle x,P_Vx\rangle
+
\langle x,H_A^{\mathrm{emb}}x\rangle.
\end{aligned}$

Therefore Theorem 3 gives

$1-\langle x,P_Ax\rangle
\le
\frac{C}{g}
\left(
t\lambda+t(1+\rho_A)\lambda^2+\frac{e}{\lambda^\kappa}
\right).$

Choose

$\lambda
\le
c\min\left\{
\frac{\eta^2g}{t},
\;
\eta\sqrt{\frac{g}{t(1+\rho_A)}}
\right\}.$

Under the universal bound $\rho_A\le N_*t$, it is enough to take

$\boxed{
\lambda\le c\frac{\eta^2g}{t}.
}$

Then choose

$\boxed{
E\le c\,\eta^2g\,\lambda^\kappa.
}$

Every unit vector of energy below $E$ satisfies

$\langle x,P_Ax\rangle\ge1-\eta^2.$

Let $\mathcal L_{<E}$ be the spectral subspace of $\Delta_A$ below $E$. The map

$P_A:\mathcal L_{<E}\longrightarrow K_A$

is injective, so

$\dim\mathcal L_{<E}\le \dim K_A.$

The quotient injection from Lemmas 1–2 provides at least $\dim K_A$ exact zero modes. Hence:

## Corollary 4 — exact multiplicity and whole-positive-spectrum gap

$\boxed{
\dim\ker\Delta_A=\dim\ker H_A
}$

and

$\boxed{
\Delta_A\big|_{\ker\Delta_A^\perp}\succeq E I.
}$

Moreover, if $Q_A$ is the geometric harmonic projector, then

$\boxed{
\|Q_A-P_A\|\le\eta.
}$

For $m=6$,

$\kappa=4m+2=26.$

With $\lambda=\Theta(\eta^2g/t)$,

$\boxed{
E
=
\Theta\!\left(
\frac{\eta^{54}g^{27}}{t^{26}}
\right).
}$

This is the one-factor-$t$ improvement over the packet’s bound. The global concentration theorem, rather than the quotient argument, is what earns it.

---

# 8. Why the remaining interface term is genuinely worst-case

## 8.1 A simplicial coherent-leakage example

The $t^2\lambda^2$ behavior cannot be removed using only orthogonal input blocks and a shared register output.

Take the triangle-free graph with register vertices $v_0,z,v_1$ and gadget vertices $w_1,\ldots,w_t$. Include edges

$[v_0,z],\ [z,v_1],
\qquad
[v_0,w_i],\ [w_i,v_1]$

and no others. Give register vertices weight $1$ and each $w_i$ weight $\lambda$.

Define normalized 1-chains

$r=\frac{[v_0,z]+[z,v_1]}{\sqrt2},
\qquad
e_i=\frac{[v_0,w_i]+[w_i,v_1]}{\sqrt2}.$

With compatible orientations,

$\partial r=\frac{[v_1]-[v_0]}{\sqrt2},
\qquad
\partial e_i
=
\lambda\frac{[v_1]-[v_0]}{\sqrt2}.$

Set

$x=
-\lambda\sqrt t\,r
+
\frac1{\sqrt t}\sum_{i=1}^t e_i.$

Then

$\partial x=0.$

But the restriction to the $i$-th single-gadget subcomplex is

$x_i=-\lambda\sqrt t\,r+\frac1{\sqrt t}e_i,$

and

$\|\partial x_i\|^2
=
\lambda^2\frac{(t-1)^2}{t}.$

Therefore

$\sum_i\|\partial x_i\|^2
=
\lambda^2(t-1)^2
=
\Theta(t^2\lambda^2).$

After normalizing $x$, the same asymptotic remains whenever $t\lambda^2=O(1)$.

Thus global boundary cancellation can coexist with $\Theta(t^2\lambda^2)$ total single-gadget boundary energy. Any further improvement must exploit special first-order structure of the actual King–Kohler/Rudolph palette, not merely orthogonality of gadget-input blocks.

## 8.2 The $t\lambda$ term is also sharp under operator-norm data alone

Let

$K^0=|e_1\rangle\langle e_1|$

and, for every $i$,

$K_i
=
|v_\theta\rangle\langle v_\theta|,
\qquad
v_\theta=\cos\theta\,e_1+\sin\theta\,e_2.$

Then

$\|K_i-K^0\|=\sin\theta=\Theta(\theta).$

For

$x=\frac{e_1+e_2}{\sqrt2},$
$\langle x,(K_i-K^0)x\rangle
=
\frac{\sin2\theta}{2}
=
\Theta(\theta).$

Thus

$\sum_i\langle x,(K_i-K^0)x\rangle
=
\Theta(t\theta).$

Consequently, the $t\lambda$ term cannot be improved from the separate bounds

$\|K_i-(P_V-\Phi_i)\|=O(\lambda)$

alone. A better $t$-dependence would require proving that the actual palette has no coherently aligned first-order shared-register rotation.

This identifies a precise possible next breakthrough rather than a vague “improve constants” task.

---

# 9. Functorial exact normalized persistence

Let $A\subseteq B$. Define

$W_A=\sum_{j\in A}\operatorname{ran}P_j,
\qquad
K_A=W_A^\perp=\ker H_A.$

The exact filling result and Corollary 4 give natural isomorphisms

$H_d(X_A)\cong V/W_A,
\qquad
H_d(X_B)\cong V/W_B.$

The inclusion-induced map corresponds to the quotient

$V/W_A\longrightarrow V/W_B.$

Since $W_A\subseteq W_B$, this map is surjective. Therefore

$\boxed{
\operatorname{rank}
\bigl[H_d(X_A)\to H_d(X_B)\bigr]
=
\dim V/W_B
=
\dim K_B.
}$

Also

$\beta_d(X_A)=\dim K_A.$

Hence, whenever $\dim K_A>0$,

$\boxed{
q(X_A,X_B)
=
\frac{\beta_d(X_A\to X_B)}{\beta_d(X_A)}
=
\frac{\dim K_B}{\dim K_A}.
}$

This is exact. No approximate harmonic-representative compatibility is needed for the equality of ranks.

---

# 10. Stronger harmonic-angle and trace-to-rank consequence

Exact ranks alone do not tell a quantum algorithm that a projection probability equals the rank fraction. The geometric harmonic maps could, in principle, have tiny nonzero singular values. Concentration prevents that.

Embed $C_d(X_A)$ into $C_d(X_B)$, and extend $Q_A$ by zero. Assume

$\|Q_A-P_A\|\le\eta_A,
\qquad
\|Q_B-P_B\|\le\eta_B,
\qquad
P_B\le P_A.$

Define

$\alpha(\eta_A,\eta_B)
=
\sqrt{1-\eta_A^2}\sqrt{1-\eta_B^2}
-
\eta_A\eta_B.$

## Lemma 5 — principal-angle composition

Every nonzero singular value of the harmonic map

$T_{A,B}=Q_BJQ_A$

is at least

$\boxed{
\alpha(\eta_A,\eta_B).
}$

### Proof

Take a unit $y\in\operatorname{ran}Q_B$. Since $Q_B$ is $\eta_B$-close to $P_B$,

$\|(I-P_B)y\|\le\eta_B.$

Because $P_B\le P_A$,

$\|(I-P_A)y\|\le\eta_B,
\qquad
\|P_Ay\|\ge\sqrt{1-\eta_B^2}.$

Write

$y=p+r,
\qquad
p=P_Ay,\quad r=(I-P_A)y.$

For $p\in\operatorname{ran}P_A$,

$\|Q_Ap\|\ge\sqrt{1-\eta_A^2}\|p\|.$

For $r\perp\operatorname{ran}P_A$,

$\|Q_Ar\|
=
\|(Q_A-P_A)r\|
\le
\eta_A\|r\|.$

Therefore

$\begin{aligned}
\|Q_Ay\|
&\ge
\|Q_Ap\|-\|Q_Ar\|\\
&\ge
\sqrt{1-\eta_A^2}\sqrt{1-\eta_B^2}
-
\eta_A\eta_B.
\end{aligned}$

This bounds the smallest singular value of $T_{A,B}^*$ on

$\operatorname{ran}Q_B$, hence all nonzero singular values of $T_{A,B}$. ∎

For equal errors,

$\boxed{
\alpha(\eta,\eta)=1-2\eta^2.
}$

This slightly sharpens the packet’s $\sqrt{1-4\eta^2}$ lower bound.

## Corollary 6 — true normalized rank from a simple harmonic-overlap probability

Let

$r_A=\dim\operatorname{ran}Q_A,
\qquad
r_B=\dim\operatorname{ran}Q_B,
\qquad
q=\frac{r_B}{r_A}.$

Prepare the maximally mixed initial harmonic state

$\rho_A=\frac{Q_A}{r_A}.$

The probability of projecting into the final harmonic space is

$\tau
=
\operatorname{Tr}(Q_BJ\rho_AJ^*)
=
\frac1{r_A}\operatorname{Tr}(T_{A,B}^*T_{A,B}).$

The map has rank $r_B$, and its $r_B$ nonzero singular values lie in $[\alpha,1]$. Hence

$\boxed{
\alpha^2q\le\tau\le q.
}$

Therefore

$0\le q-\tau\le1-\alpha^2.$

For $\eta_A=\eta_B=\eta$,

$\boxed{
0\le q-\tau
\le
4\eta^2-4\eta^4
\le4\eta^2.
}$

This is algorithmically useful: on the constructed family, a standard final-harmonic projection probability is an additive approximation to the **true rank fraction**, not merely an unrelated squared-overlap statistic.

It also supplies the large-overlap promise needed by the known BQP containment route for normalized harmonic persistence. Lowe et al. explicitly separate the true normalized rank problem from the quasi-harmonic surrogate and require preparation and spectral/overlap conditions for containment.

---

# 11. Sharpened history-Hamiltonian gap

The packet’s $H_1$ gap proof survives. The $H_2$ combination lemma can be strengthened.

## Lemma 7 — optimal two-projection lower bound

Let $H\succeq0$ have kernel $K$ and satisfy

$H\succeq g(I-P_K),
\qquad
0<g\le1.$

Let $Q$ be an orthogonal projector, and put

$S=K\cap\ker Q.$

Assume

$P_KQP_K
\succeq
\alpha(P_K-P_S).$

Then the positive gap of $H+Q$ above $S$ is at least

$\boxed{
\gamma(g,\alpha)
=
\frac{g+1-\sqrt{(g+1)^2-4g\alpha}}{2}.
}$

In particular,

$\boxed{
\gamma(g,\alpha)\ge\frac{g\alpha}{g+1}.
}$

### Proof

Since $H\ge g(I-P_K)$,

$H+Q\ge g(I-P_K)+Q.$

Restrict to $S^\perp$. Use the standard two-projection decomposition for $P_K$ and $Q$. In every nontrivial two-dimensional principal-angle block,

$P_K=
\begin{pmatrix}
1&0\\0&0
\end{pmatrix},
\qquad
Q=
\begin{pmatrix}
c^2&cs\\cs&s^2
\end{pmatrix},$

where $c^2$ is an eigenvalue of $P_KQP_K$ and hence $c^2\ge\alpha$. Therefore

$g(I-P_K)+Q
=
\begin{pmatrix}
c^2&cs\\cs&g+s^2
\end{pmatrix}.$

Its trace is $g+1$ and determinant is $gc^2$. Its smaller eigenvalue is

$\frac{g+1-\sqrt{(g+1)^2-4gc^2}}2,$

which is increasing in $c^2$. Taking $c^2\ge\alpha$ proves the first formula.

The product of the two eigenvalues is at least $g\alpha$, while the larger is at most $g+1$, giving the second bound. The estimate is sharp for a single two-dimensional principal-angle block. ∎

## Application to the packet’s weighted history

The packet proves

$g_1\ge\frac1{8L^2}.$

For the final output projector $R$,

$\mathcal V^\dagger R\mathcal V
=
\frac{I-M}{Z}.$

On $S^\perp$, the source promise gives $M\le1/3$, while $Z\le2L$. Hence

$\alpha\ge \frac{2/3}{2L}=\frac1{3L}.$

Lemma 7 gives

$g_2
\ge
\frac{\alpha g_1}{1+g_1}.$

Since $g_1\le1/8$,

$\boxed{
g_2\ge
\frac{1}{27L^3}.
}$

This replaces the safe but loose $1/(120L^3)$ estimate. The asymptotic $L^{-3}$ is unchanged.

---

# 12. Exact supported source problem

The cleanest source should be named explicitly rather than being called “SDQC1” without qualification.

## Definition — $G_2$ separated perfect-subspace trace

Input is an exact polynomial-size circuit $U$ over

$G_2=\{X,\mathrm{CX},\mathrm{CCX},H\otimes H\}$

with:

- $k$ maximally mixed input qubits;

- clean work qubits initialized through an isometry
  
$J:\mathbb C^{D}\hookrightarrow\mathcal H,
\qquad D=2^k>0;$

- an accepting projector $P_{\mathrm{acc}}$.

Define

$M=J^*U^*P_{\mathrm{acc}}UJ.$

Promise:

$S=\ker(I-M),
\qquad
M|_{S^\perp}\preceq \frac13 I,$

and

$p=\frac{\operatorname{Tr}M}{D}$

satisfies either

$p\ge\frac23$

or

$p\le\frac13.$

Let

$f=\frac{\dim S}{D}.$

Since the eigenvalues on $S$ equal $1$, and all other eigenvalues lie in $[0,1/3]$,

$f\le p\le\frac13+\frac23f.$

Thus

$p\ge\frac23
\quad\Longrightarrow\quad
f\ge\frac12,$

whereas

$p\le\frac13
\quad\Longrightarrow\quad
f\le p\le\frac13.$

This is the exact source-to-fraction sandwich.

The mixed-spectator repair is also exact. For a circuit over

$\{X,\mathrm{CX},\mathrm{CCX},H\}$, replace every $H_j$ by

$H_j\otimes H_a$ on one unmeasured mixed spectator. Then

$U'=U\otimes H_a^h,$

but

$\begin{aligned}
M'
&=(J\otimes I)^*
(U^*\otimes H_a^h)
(P_{\mathrm{acc}}\otimes I)
(U\otimes H_a^h)
(J\otimes I)\\
&=M\otimes I.
\end{aligned}$

This holds for odd and even $h$. Both $D$ and $\dim S$ double, so $f$ is unchanged. 

---

# 13. Conditional circuit-to-normalized-persistence theorem

## Theorem 8 — restricted exact true-NHP transfer

Assume the finite $G_2$ gadget palette satisfies the local certificate in Section 4.

Given an instance of $G_2$ separated perfect-subspace trace, construct the packet’s weighted unary-history Hamiltonians

$H_1
\quad\text{and}\quad
H_2=H_1+H_{\mathrm{out}},$

then the corresponding nested weighted clique complexes

$X_1\subseteq X_2.$

With $D>0$ and $S=\ker(I-M)$,

$\boxed{
\beta_d(X_1)=D,
}$

and

$\boxed{
\beta_d(X_1\to X_2)=\dim S.
}$

Therefore

$\boxed{
q(X_1,X_2)=\frac{\dim S}{D}=f.
}$

The endpoint degree-$d$ positive gaps are inverse polynomial. Using the sharpened source gap

$g\ge\frac1{27L^3}$

and $m=6$, one may take

$\lambda=\Theta\!\left(\frac{\eta^2g}{t}\right)$

and

$E
=
\Theta\!\left(
\frac{\eta^{54}g^{27}}{t^{26}}
\right).$

The source YES/NO cases become

$q\ge\frac12
\qquad\text{versus}\qquad
q\le\frac13.$

An additive-$1/24$ estimate $\widehat q$ distinguishes them with threshold

$\boxed{\frac5{12}}:$
$q\ge\frac12
\Longrightarrow
\widehat q\ge\frac{11}{24},$

and

$q\le\frac13
\Longrightarrow
\widehat q\le\frac9{24}.$

This is the exact requested error budget.

### Computational model

The clean target promise problem should explicitly include:

- succinct graphs defining clique complexes, with growing $d$;

- an inverse-polynomial lower bound on each endpoint Laplacian gap;

- $\beta_d(X_1)>0$;

- coherent sparse-Laplacian access;

- a circuit preparing the normalized initial harmonic mixture to prescribed trace error, or the equivalent preparation oracle used in Lowe et al.;

- a lower bound on nonzero harmonic-map singular values.

The constructed instances satisfy the last condition with a constant near $1$, by Lemma 5. The known normalized-persistence containment result is stated under precisely such preparation, gap, and large-overlap conditions.

Alternatively, on this particular construction one can simply estimate the final harmonic-projection probability $\tau$, because Corollary 6 gives

$|q-\tau|\le4\eta^2.$

Preparation error and phase-estimation/sampling error can be budgeted so that

$4\eta^2+\epsilon_{\mathrm{prep}}+\epsilon_{\mathrm{PE}}+\epsilon_{\mathrm{est}}
\le\frac1{24}.$

---

# 14. Complexity consequence—and its exact limitation

The separated $G_2$ source is in BQP: prepare the maximally mixed valid input, run the circuit, and estimate the constant-gap mean acceptance $p$.

It is also hard for the gate-restricted perfect-completeness class $\mathsf{BQP}_1(G_2)$. Given a pure-input $G_2$ circuit, take $D=1$. Then $M$ is scalar:

- YES: $M=1$, so $\dim S=1$;

- NO: $M\le1/3$, so $\dim S=0$.

Thus the source promise is satisfied and

$q\in\{1,0\}.$

Consequently, conditional on the finite-palette certificate:

$\boxed{
\text{true normalized harmonic persistence is }
\mathsf{BQP}_1(G_2)\text{-hard}.
}$

Rudolph proves exact perfect-completeness simulations into the $G_2$ framework for broad finite cyclotomic gate sets, which makes this more than a purely artificial notation, but the exact class remains gate-set-sensitive.

Two caveats matter:

- The $D=1$ hardness corollary does **not** exploit nontrivial normalization; $q$ is only $0$ or $1$. The arbitrary-$D$ source transfer is mathematically stronger and is the result that actually realizes a surviving fraction.

- Nothing proved here yields unrestricted SDQC1-hardness or BQP-hardness. Fixed trace thresholds do not automatically supply an exact reduction from every published SDQC1 formulation, and approximate circuit amplification or gate synthesis does not preserve exact eigenvalue-$1$ multiplicities.

That boundary should remain explicit in any abstract.

---

# 15. Unweighted corollary

Choose $\lambda$ with $\lambda^{-2}=F\in\mathbb N$. Use one common block assignment at both filtration levels:

- every weight-one register vertex gets $F$ copies;

- every weight-$\lambda$ gadget vertex gets one copy.

Hayakawa’s block decomposition gives

$\widehat\Delta
=
U(F\Delta_w)U^*
\oplus R_{\mathrm{asym}},
\qquad
R_{\mathrm{asym}}\succeq I.$

Because the same blocks are used at both levels,

$\widehat J\,U_1=U_2J.$

Thus:

- harmonic dimensions are unchanged;

- persistent ranks are unchanged;

- harmonic-map singular values are unchanged;

- normalized harmonic mixtures map isometrically;

- $q$ is unchanged;

- the unweighted endpoint gap is at least
  
$\min\{FE,1\}.$

With the improved weighted $E$,

$FE
=
\Theta(\eta^2g\lambda^{\kappa-2}).$

For $m=6$,

$\boxed{
FE
=
\Theta\!\left(
\frac{\eta^{50}g^{25}}{t^{24}}
\right).
}$

This remains a poor polynomial and will suffer further normalization factors if the Laplacian is rescaled for block encoding. It is nevertheless inverse polynomial.

The graph-theoretic block result and asymmetric gap are Hayakawa’s contribution; filtered naturality is the short additional observation.

---

# 16. A stronger TDA consequence: quotient diagrams beyond a pair

The functorial construction gives more than one persistence query, although the additional algebra is elementary.

Let $\mathcal I$ be any finite connected inclusion diagram, with a term set $A_i$ at each object and

$A_i\subseteq A_j$

for every arrow $i\to j$. Then

$H_d(X_{A_i})\cong V/W_i,
\qquad
W_i=\sum_{k\in A_i}\operatorname{ran}P_k.$

All arrows are the corresponding quotient maps.

## Corollary 9 — generalized rank for the simulated quotient family

Let $\operatorname{grank}$ denote the rank of the canonical map

$\varprojlim H_d(X_{A_i})
\longrightarrow
\varinjlim H_d(X_{A_i}).$

Then

$\boxed{
\operatorname{grank}
=
\dim V\Big/\sum_{i\in\mathcal I}W_i
=
\dim\ker\left(
\sum_{k\in\cup_iA_i}P_k
\right).
}$

### Proof

Since the diagram is connected and every object is a quotient of the same $V$, its colimit is

$V/\sum_iW_i.$

Indeed, the natural maps $V/W_i\to V/\sum_jW_j$ form a compatible cocone, and the colimit relations identify all copies of a common $v\in V$.

For every $v\in V$, the family

$(v+W_i)_{i\in\mathcal I}$

is a compatible element of the inverse limit. Its image in the colimit is $v+\sum_iW_i$. Thus the limit-to-colimit map is surjective, and its rank is the colimit dimension. Orthogonal complementation gives the kernel formula. ∎

This does **not** overcome the general Möbius or projector-overlap obstruction. It identifies a special epimorphic quotient family in which generalized rank is easy algebraically once the Hamiltonian kernel dimension is known.

For a chain

$A_1\subseteq\cdots\subseteq A_s,$

write $r_i=\dim\ker H_{A_i}$. Then

$\operatorname{rank}[H_d(X_{A_i})\to H_d(X_{A_j})]=r_j
\quad(i\le j),$

and the barcode has only intervals born at level $1$:

$r_j-r_{j+1}$

copies die after level $j$, and $r_s$ copies survive to the end. This is a clean full-barcode description of the constructed monotone family, not a general barcode algorithm.

---

# 17. Persistent-Laplacian proposal

The clique-only persistent-Laplacian direct-sum statement remains valid conditional on using common blocks. In concise form, for an inclusion $K\hookrightarrow L$,

$\widehat\Delta_k^{K,L}
=
U\bigl(F\Delta_{k,w}^{K,L}\bigr)U^*
\oplus R,
\qquad
R\succeq f_{\min}I.$

The proof uses:

- boundary naturality on the symmetric sector;

- invariance of the restricted persistent-boundary domain;

- group symmetry to eliminate symmetric–asymmetric cross terms;

- domination of the persistent Laplacian by the ordinary endpoint Laplacian on the asymmetric sector.

This preserves the entire persistent-Laplacian spectrum below $f_{\min}$, not only the nullity.

I still judge it secondary. Persistent Laplacians, their nullity, and their simplicial-map extensions are established; once Hayakawa’s block decomposition is available, the filtered direct sum is a concise structural corollary. It is useful as a section or proposition, not the likely paper anchor.

---

# 18. Complex-phase boundary

The packet is right not to invoke approximate synthesis while claiming exact kernels. There is a basic field-of-definition obstruction.

## Proposition 10 — rational-gadget field obstruction

Let $\mathbb F\subseteq\mathbb C$ be a subfield. Suppose:

- the boundary matrices of a weighted simplicial gadget have entries in $\mathbb F$;

- the logical register cycle space has an $\mathbb F$-basis.

Then

$B_d(Y;\mathbb C)\cap V_\mathbb C
=
\bigl(B_d(Y;\mathbb F)\cap V_\mathbb F\bigr)
\otimes_\mathbb F\mathbb C.$

In particular, if this intersection is one-dimensional, it has a generator whose coordinate ratios lie in $\mathbb F$.

### Proof

Images, kernels, and intersections of finite-dimensional subspaces defined by matrices over $\mathbb F$ commute with scalar extension to $\mathbb C$, because field extension is flat. Equivalently, Gaussian elimination may be performed over $\mathbb F$. ∎

Therefore a rational/dyadic weighted clique gadget cannot directly fill precisely

$\operatorname{span}\{(1,\alpha)\}$

when $\alpha\notin\mathbb F$, relative to an $\mathbb F$-defined logical encoding.

This is not a no-go theorem for enlarging the encoding or using exact cyclotomic realification. It is a no-go theorem for silently replacing exact phases by approximate gate synthesis while preserving exact boundary or kernel dimensions.

---

# 19. Preserved negative conclusions

The following failures remain genuine and should stay in the paper-development record.

### Möbius projector-overlap obstruction

The fixed Möbius telescope has generalized rank one while the sole nonzero singular value of $P_KP_L$ is

$\Theta(m2^{-m}),$

even though both local constraint systems have uniformly positive nonzero singular gaps. Thus local Laplacian/constraint gaps alone do not control the global limit-to-colimit overlap. This is a structural obstruction, not a quantum lower bound. 

### AIDA update rank

After cached-Hom substitution, a rank-one change of a candidate splitting vector can induce reduced update rank equal to the target fibre dimension. The explicit indecomposable construction in the packet rules out a generic constant-rank reversible update. 

### Classical explicit-simplex baseline

If all relevant $d$- and $(d+1)$-simplices or boundary matrices are explicitly listed, Gaussian elimination computes the required ranks in time polynomial in that explicit size. Any complexity claim therefore concerns succinct graph input with growing $d$ and exponentially many cliques, not an unconditional advantage over explicit sparse linear algebra. 

### Net/barcode route

The packet’s parameter-sensitive net theorem is mathematically legitimate, but classical $\varepsilon$-nets already give similar dimension-dependent covering behavior. Its value is as an oracle consequence for a particular quantum metric-access model, not as the central hardness theorem.

---

# 20. Best paper-level formulation

The strongest defensible main theorem is:

**Finite-palette, functorial, gapped kernel realization.**

A fixed source-certified palette of weighted clique gadgets transforms every nested family of supported positive-projector Hamiltonians into nested clique complexes whose top homology functor is exactly the common quotient functor $V/W_A$, whose Betti dimensions equal logical kernel dimensions, whose entire positive Laplacian spectrum has a known inverse-polynomial gap, and whose harmonic maps are uniformly well conditioned. For the supported weighted-history source, true normalized persistence equals the perfect-acceptance eigenspace fraction.

The main technical lemma is Theorem 3, not the quotient corollary.

The strongest conditional complexity statement is:

$\boxed{
\begin{gathered}
\text{Additive-}1/24\text{ true normalized harmonic persistence}\\
\text{on the resulting unweighted clique filtrations is}\\
\mathsf{BQP}_1(G_2)\text{-hard and lies in BQP}\\
\text{under the stated gap, preparation, and overlap promises.}
\end{gathered}
}$

The nontrivial arbitrary-$D$ result is an exact reduction from the explicitly defined $G_2$ separated perfect-subspace trace problem. Its unrestricted SDQC1 hardness remains open.

This is potentially a serious theoretical-CS paper if the finite palette is closed exactly. Without that closure, it remains a strong conditional theorem package.

---

# 21. Next finite milestone

The next milestone should be a **finite local-certificate release**, not additional global abstraction.

For every isomorphism type actually used by the $G_2$ unary-history source—including fixed computational-basis guards and all joins up to locality six—produce:

- the explicit finite clique graph and oriented boundary matrices over $\mathbb Q(\lambda)$;

- an exact rank/nullity certificate;

- the leading eigenvalue valuation and a rational lower coefficient for the lifted sector;

- exact verification of the corrected local-bulk relative injectivity;

- a certified $O(\lambda)$ kernel-projector bound;

- the first-order shared-register block of
  
$K_\phi(\lambda)-(P_V-\Phi_\phi).$

The milestone has two hard stop rules:

- **Failure stop:** any palette member has the wrong exact nullity, a missing relative-bulk singular value, or a lifted exponent worse than claimed.

- **Exponent-improvement stop:** if two certified first-order shared-register corrections can be aligned as in the $t\lambda$ counterexample, accept $t\lambda$ as sharp and stop seeking a better $t$-exponent. If every first-order correction is purely gadget-private or cancels by a provable palette identity, rerun the global summation; that is the only credible route from $\lambda=\Theta(g/t)$ toward a larger $\lambda$.

Completing that finite milestone would convert the present result from “conditional on a source-mapped palette” into a verifiable theorem. Until then, the global mathematics is substantially advanced, but the full reduction should remain uncertified.
