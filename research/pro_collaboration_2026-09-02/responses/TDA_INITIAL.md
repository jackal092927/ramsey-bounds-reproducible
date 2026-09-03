# Archived ChatGPT Pro response — TDA, first dispatch

Captured from the existing conversation on 2026-09-02 PDT. The visible personal account matched the channel registry; the page showed a completed response (Worked for 51m 8s) and response actions. This is an external AI collaborator's response, not an independently verified theorem or novelty verdict. The account identifier stays in the local channel registry.

Conversation: [Audit Quantum Persistence Corollary](https://chatgpt.com/c/6a98c05a-ecf4-83e8-b356-4e20dc3fde3f)

Extraction: rendered assistant response only, converted to Markdown; LaTeX preserved from rendered math attributes. No hidden reasoning, sidebar history, or account settings are included. See the local disposition for accepted, corrected, and unresolved claims.

---

# Verdict

The **common-multiplicity unweighting argument is mathematically sound**, but its novelty is substantially narrower than a new unweighting mechanism:

| Claim | Assessment |
| --- | --- |
| A weighted Hodge Laplacian appears, up to a factor $M$, in the symmetric sector of a block blow-up | **Existing theorem**: essentially Hayakawa, Lemma 4.2 |
| No extra harmonic or low-energy states occur outside that sector | **Existing theorem**: Hayakawa, Theorem 4.3 |
| Using the same blocks at both filtration levels makes inclusion commute with unweighting | **Correct elementary lemma** |
| Weighted harmonic-persistence overlap is therefore preserved exactly | **Short corollary** |
| The weighted hard family can be made unweighted with polynomial blow-up | **Correct after parameter and access-model repairs** |
| Unweighted Harmonic Persistence is $\mathsf{BQP}_{1}$-hard and in $\mathsf{BQP}$ | **Conditionally justified**, not yet cleanly justified in the canonical positive-subset-state model |
| The same construction unweights every persistent Laplacian in a filtration, including its low nonzero spectrum | **Plausibly new structural TDA theorem**, proved below |

Hayakawa already proves the exact symmetric-sector reduction, the factor-$M$ spectral scaling, the $\min_v f_v$ asymmetric-sector gap, and even an exact integer parameter choice for the King–Kohler reduction. Thus the new ingredient for harmonic persistence is not the spectral gadget; it is the one-line **naturality across an inclusion**, plus checking that the particular guide and promises survive. [arXiv+2arXiv+2](https://arxiv.org/html/2608.02726v1)

The packet correctly warns not to turn this into another generalized-rank projector route or AIDA search proposal.  

---

## 1. Strongest unresolved issue: orientation is part of the input model, not just notation

Gyurik et al. allow every simplex to have an arbitrary fixed vertex ordering and then define the guide as a positive uniform subset state in that oriented simplex basis. But the formal problem input lists the two graphs, the dimension, and a compact subset description; it does not explicitly list an orientation oracle. [arXiv+2arXiv+2](https://arxiv.org/html/2410.21258v2)

This matters. In the usual computational encoding, an oriented simplex is represented using globally sorted vertex labels. In that basis, a nonzero positive 1-cycle cannot exist:

- Let $v$ be the globally least vertex appearing in the support.

- Every incident selected edge has the form $[v,u]$, with
  $\partial[v,u]=[u]-[v].$

- Therefore every positive coefficient contributes with the same sign at $v$, so the boundary cannot cancel.

The bowtie-cycle guide is consequently **necessarily signed** in the globally sorted basis. The same remains true after block blow-up.

This does not affect any spectral identity: changing simplex orientations conjugates every boundary and Laplacian by diagonal sign matrices. But it does affect the promise “the input is a positive subset state.”

The presently safe formulations are therefore:

- **Orientation-aware formulation:** the input supplies an efficiently computable simplex-orientation convention, and the guide is positive relative to that basis; or

- **Canonical-orientation formulation:** the guide may be an efficiently preparable signed subset state.

For this particular hard family, the signed-state repair should be easy: the sign relative to sorted orientation is the product of constant-size local cycle-edge signs and a computable join-order parity. The copy indices add no conceptual difficulty if vertices are labelled block-major. But that sign circuit should be written explicitly. Without it, the exact positive-subset-state classification in a canonical graph-only access model is not fully specified.

This issue is inherited from the weighted source; the unweighting step does not create it. Still, an unqualified statement that the resulting standard unweighted positive-subset problem is $\mathsf{BQP}_{1}$-hard would presently be too strong.

---

## 2. The parameter substitution should be exact, not dyadically rounded

The packet proposes taking a sufficiently small dyadic $\lambda=2^{-L}$ and $M=2^{2L}$.  That is not literally a direct application of the imported theorem: the King–Kohler parameter is set as

$\lambda=c\,t^{-1}g,
\qquad
E=c\,\lambda^{4m+2}t^{-1}g,$

for a sufficiently small constant $c$ and a spectral lower bound $g$. [arXiv](https://arxiv.org/html/2311.17234v2)

There is a cleaner exact repair, with no rounding lemma.

Let

$g_{0}=\frac1{q(n)}$

be an explicitly known lower bound on the relevant history-Hamiltonian gap, where $q$ is taken integer-valued after harmless enlargement. Choose a sufficiently large fixed integer $C$ and set

$Q=Ctq(n),\qquad
\lambda=\frac1Q,\qquad
M=Q^{2}.$

Then $c=1/C$, so

$\lambda=\frac{g_{0}}{Ct} = c\,t^{-1}g_{0}$

holds exactly. The two source weights become

$f_{\mathrm{reg}}=M\cdot1^{2}=Q^{2},
\qquad
f_{\mathrm{gad}}=M\lambda^{2}=1.$

This is exactly the integer-ratio strategy Hayakawa uses in Section 6.3. [arXiv](https://arxiv.org/html/2608.02726v1)

King–Kohler’s theorem already accepts any $g$ satisfying the required spectral lower bound. Gyurik’s overlap lemma is written using the actual gap, but its proof only uses

$H\big|_{\ker(H)^\perp}\succeq g_{0}I$

and that the accumulated errors are at most a sufficiently small multiple of $g_{0}$. With

$\lambda=\Theta(g_{0}/t),
\qquad
E=\Theta(\lambda^{4m+2}g_{0}/t),$

the relevant terms are

$O(\lambda t),\qquad
O(\lambda^{-(4m+2)}Et),\qquad
O(\lambda^{2}t),$

each $O(g_{0})$ after reducing the fixed constant. Thus the proof works with a known lower bound $g_{0}$, which makes the reduction uniform. [arXiv+1](https://arxiv.org/html/2410.21258v2)

A theorem statement should explicitly pin down $q(n)$. Merely asserting that the gap is $1/\operatorname{poly}(n)$ is not enough to define a uniform multiplicity-producing reduction.

---

## 3. Audit of the common-multiplicity commutation lemma

Let $K$ be a weighted simplicial complex with positive vertex weights $w(v)$, using the normalized simplex basis in which

$\partial_w\ket{\sigma}'=
\sum_{i=0}^{k}(-1)^i w(v_i)
\ket{\sigma\setminus v_i}'.$

Choose $M$ such that

$f_v=Mw(v)^2\in\mathbb N$

for every vertex. Replace $v$ by a clique block $B_v$ of $f_v$ copies.

For an oriented simplex $\sigma=(v_0,\ldots,v_k)$, define

$U_k\ket{\sigma}'=
\frac{1}{\sqrt{\prod_{v\in\sigma}f_v}}
\sum_{i_v\in B_v}
\ket{\widetilde\sigma_{\mathbf i}},$

where each lift inherits the base orientation.

### Boundary identity

Taking the ordinary unweighted boundary and grouping all terms that delete a copy of $v_j$,

$\begin{aligned}
\widehat\partial U_k\ket{\sigma}'
&=
\sum_{j=0}^{k}(-1)^j
\sqrt{f_{v_j}}\,
U_{k-1}\ket{\sigma\setminus v_j}'\\
&=
\sqrt M\,
U_{k-1}
\sum_{j=0}^{k}(-1)^j
w(v_j)\ket{\sigma\setminus v_j}'\\
&=
\sqrt M\,U_{k-1}\partial_w\ket{\sigma}'.
\end{aligned}$

Hence

$\boxed{\widehat\partial U=\sqrt M\,U\partial_w.}$

By taking adjoints on the invariant sector,

$\widehat\partial^{*}U=\sqrt M\,U\partial_w^{*},$

and therefore

$\boxed{\widehat\Delta U=M\,U\Delta_w.}$

Hayakawa independently proves that the block-fixed sector is exactly the span of these one-copy-per-block averages: a simplex using two copies from one block has zero group average because transposing those two copies reverses its orientation. He also proves

$\widehat\Delta\big|_{T^\perp}
\succeq
f_{\min}I,
\qquad
f_{\min}:=\min_v f_v.$

Thus there are no additional kernels, and

$\widehat\Delta
=
U(M\Delta_w)U^{*}\oplus R,
\qquad
R\succeq f_{\min}I.$

[arXiv+1](https://arxiv.org/html/2608.02726v1)

In particular, if $P_w$ and $\widehat P$ are the harmonic projectors,

$\boxed{\widehat P=UP_wU^{*}.}$

### Naturality for an inclusion

Now let $K\subseteq L$, with the **same blocks $B_v$** used at both levels. For every simplex $\sigma\in K$, its average over lifts is literally the same chain whether regarded inside $\widehat K$ or $\widehat L$. Therefore

$\boxed{\widehat i\,U_K=U_L\,i.}$

Consequently,

$\begin{aligned}
\left\|
\widehat P_L\,\widehat i\,U_K\psi
\right\|
&=
\left\|
\widehat P_L U_L i\psi
\right\|\\
&=
\left\|
U_L P_L i\psi
\right\|\\
&=
\left\|
P_L i\psi
\right\|.
\end{aligned}$

So the harmonic-persistence overlap is preserved **exactly**, not approximately.

### Common multiplicities really are necessary

Take one base vertex $v$. At the first level use one copy; at the second use two copies. Then

$\widehat i\,U_1\ket v=\ket{v_1},$

whereas

$U_2 i\ket v=
\frac{\ket{v_1}+\ket{v_2}}{\sqrt2}.$

Thus $\widehat iU_1\neq U_2i$. There may be an abstract isometry between the two symmetric sectors, but it is not induced by the required simplicial inclusion. The common-block hypothesis is essential.

---

## 4. Complexity consequence for the special harmonic-persistence family

Once the orientation model and uniform parameter are fixed, the remaining transfer works.

The weighted source has register vertices of weight $1$ and gadget vertices of weight $\lambda$. Its guide is supported entirely on register simplices and has a succinct Cartesian-product subset description. [arXiv+1](https://arxiv.org/html/2410.21258v2)

With

$\lambda=Q^{-1},
\qquad
M=Q^{2},$

the register blocks have $M$ copies and every gadget block has one copy. Every guide $p$-simplex therefore has exactly $M^{p+1}$ lifts, and

$U\ket S
=
\frac1{\sqrt{|S|M^{p+1}}}
\sum_{\widehat\sigma\text{ lifting }\sigma\in S}
\ket{\widehat\sigma}.$

So, relative to inherited orientations, it remains a uniform subset state and retains a compact product-copy description.

The weighted final-level gap is

$\gamma_w
=
\Omega\!\left(\lambda^{18}t^{-1}g_0\right).$

After blow-up,

$\widehat\gamma
\ge
\min\{M\gamma_w,1\}
=
\Omega\!\left(
\lambda^{16}t^{-1}g_0
\right)
=
\frac1{\operatorname{poly}(n)}.$

Because the output graph has only polynomially many vertices, this is also inverse-polynomial in the output size. [arXiv+1](https://arxiv.org/html/2410.21258v2)

The NO-case overlap in the source reduction is exactly zero, so there is no problem converting an $\exp(-n)$ promise to an $\exp(-N_{\rm out})$ promise after a polynomial graph blow-up. The source algorithm needs only the final-level Laplacian gap and gives containment in $\mathsf{BQP}$. [arXiv](https://arxiv.org/html/2410.21258v2)

A small syntactic repair is also needed if $K_1$ originally omits the later gadget vertices, since the formal problem gives $K_1$ and $K_2$ the same vertex count. Add the gadget vertices to $K_1$ as isolated vertices. The target degree is positive and very high, so this does not alter the guide or the relevant harmonic space. The source’s formal input condition and construction otherwise appear slightly misaligned on this point. [arXiv](https://arxiv.org/html/2410.21258v2)

### Safe complexity statement

Under an orientation-aware simplex access model—or, equivalently, after changing the promise to efficiently preparable signed subset states—

$\boxed{
\text{Unweighted }\delta\text{-Harmonic Persistence is }
\mathsf{BQP}_{1}\text{-hard and lies in }\mathsf{BQP}.
}$

This is **not automatically $\mathsf{BQP}$-complete**, because $\mathsf{BQP}_{1}=\mathsf{BQP}$ is not being assumed.

Gyurik et al. explicitly listed unweighted Harmonic Persistence as future work, while Hayakawa explicitly says that his paper only handles the single-complex clique-homology reduction and leaves weighted or filtered extensions open. So the complexity corollary appears new as a written result, but the mechanism is still a short synthesis of the two papers rather than a new spectral construction. [arXiv+1](https://arxiv.org/html/2410.21258v2)

---

## 5. Independent audit of the Möbius obstruction

The supplied construction uses a fixed triangulated Möbius band whose boundary and core are equal-size six-edge circles, with normalized inclusion coefficients $a=2b>0$, and then chains these fixtures into an inclusion zigzag. 

Conditional on those fixture coefficients, the linear algebra is correct.

### Limit and colimit-adjoint kernels

The limit equations are

$y_i=ax_i,
\qquad
y_i=bx_{i+1}.$

Since $a/b=2$,

$x_i=2^i,
\qquad
y_i=a2^i$

generates the one-dimensional limit.

The colimit-adjoint equations are

$k_{C_i}=ak_{M_i},
\qquad
k_{C_{i+1}}=bk_{M_i},$

so

$k_{C_i}=2^{-i},
\qquad
k_{M_i}=\frac{2^{-i}}a$

generates the one-dimensional orthogonal complement of the colimit relations.

Their inner product is

$\sum_{i=0}^{m}2^i2^{-i}
+
\sum_{i=0}^{m-1}
(a2^i)\frac{2^{-i}}a
=
(m+1)+m
=
2m+1.$

The squared norms are exactly

$S_L=
\frac{4^{m+1}-1+a^2(4^m-1)}3,$

and

$S_K=
\frac{
1-4^{-(m+1)}
+
a^{-2}(1-4^{-m})
}{
1-\frac14
}.$

Therefore the unique nonzero singular value of $P_KP_L$ is

$\sigma_m
=
\frac{2m+1}{\sqrt{S_LS_K}}
=
\Theta(m2^{-m}),$

while its rank remains one. For $a^2=41/86$ and $m=32$, this gives

$\sigma_{32}\approx 6.09612247\times10^{-9},$

agreeing with the packet.

### Uniform local constraint gaps

For the limit constraints, the infinite row-Gram symbol can be written as

$G_L(\theta)=
\begin{pmatrix}
1+a^2 & 1+ab\,e^{-i\theta}\\
1+ab\,e^{i\theta} & 1+b^2
\end{pmatrix}.$

For the colimit-adjoint constraints, the corresponding symbol is

$G_K(\theta)=
\begin{pmatrix}
1+a^2 & ab+e^{-i\theta}\\
ab+e^{i\theta} & 1+b^2
\end{pmatrix}.$

Both have

$\operatorname{tr}G=2+a^2+b^2=:T$

and

$\det G
=
a^2+b^2-2ab\cos\theta
\ge
(a-b)^2.$

Hence

$\lambda_{\min}(G(\theta))
\ge
\frac{(a-b)^2}{T}.$

Zero-extending a finite vector and applying the Fourier integral transfers the same quadratic-form lower bound to every finite Toeplitz section. Thus the smallest singular value of either constraint matrix is at least

$\frac{a-b}{\sqrt T}.$

For the stated fixture this is approximately

$0.21427238.$

One terminology correction is important:

- If “constraint gap” means the smallest nonzero **singular value**, the bound is $(a-b)/\sqrt T$.

- If it means the smallest nonzero eigenvalue of the **Gram matrix**, the bound is $(a-b)^2/T$.

The obstruction is therefore valid: uniformly conditioned local constraints do not prevent the limit and colimit-complement lines from becoming exponentially close to orthogonal.

What I cannot independently verify from the supplied text is the fixture-specific claim

$a^2=\frac{41}{86},
\qquad
b^2=\frac{41}{344}.$

The face list, oriented boundary matrices, or harmonic generator are not included. The topological relation $[A]=2[C]$ is standard for a Möbius band, and equal-size boundary/core circles explain $a=2b$, but the exact rational norm requires the concrete triangulation.

Barycentric subdivision should preserve the obstruction and make every object flag: it is functorial, preserves the degree-two homology relation, and subdivides the two equal six-edge circles identically. The exact coefficient $41/86$ will generally change, but the fixed ratio $a/b=2$, a positive constant local gap, and the $\Theta(m2^{-m})$ decay survive.

This remains a **structural obstruction**, not a quantum query or time lower bound.

---

# 6. A genuinely stronger theorem: simultaneous unweighting of persistent Laplacians

The best next theorem is not another harmonic-overlap statement. It is a filtration-level spectral result.

Mémoli–Wan–Wang define the persistent Laplacian for $K\hookrightarrow L$ and prove that its nullity equals the persistent Betti number; they also study its behavior over filtrations. [arXiv+1](https://arxiv.org/html/2012.02808v1)

## Theorem — functorial block unweighting of persistent Laplacians

Let $\{K_\alpha\}_{\alpha\in P}$ be a finite filtration or finite poset diagram of simplicial complexes, with inclusions

$K_\alpha\hookrightarrow K_\beta
\qquad
(\alpha\le\beta).$

Assume that a vertex has one fixed positive weight $w(v)$ at every level where it occurs. Choose $M>0$ such that

$f_v=Mw(v)^2\in\mathbb N$

for every vertex.

For each $v$, choose one block $B_v$ of $f_v$ copies, shared across the entire filtration. Define the unweighted block substitution

$\widehat K_\alpha
=
\left\{
\tau\subseteq\bigsqcup_v B_v:
\operatorname{supp}_B(\tau)\in K_\alpha
\right\},$

where $\operatorname{supp}_B(\tau)$ is the set of base vertices whose blocks meet $\tau$.

When $K_\alpha$ is a clique complex, $\widehat K_\alpha$ is exactly the clique complex of the usual graph block blow-up.

For $\alpha\le\beta$, let

$D_{k+1,w}^{\alpha,\beta}
=
\left\{
z\in C_{k+1}(K_\beta,w):
\partial_w z\in C_k(K_\alpha,w)
\right\},$

and let

$b_{k+1,w}^{\alpha,\beta}
=
\partial_w\big|_{D_{k+1,w}^{\alpha,\beta}}.$

Define the weighted persistent Laplacian

$\Delta_{k,w}^{\alpha,\beta}
=
b_{k+1,w}^{\alpha,\beta}
\bigl(b_{k+1,w}^{\alpha,\beta}\bigr)^*
+
(\partial_{k,w}^{\alpha})^*
\partial_{k,w}^{\alpha}.$

Let $\widehat\Delta_k^{\alpha,\beta}$ be the ordinary unweighted persistent Laplacian of

$\widehat K_\alpha\hookrightarrow\widehat K_\beta.$

Then:

### 1. Natural chain-level embedding

There are isometries

$U_{\alpha,k}:C_k(K_\alpha,w)\longrightarrow
C_k(\widehat K_\alpha)$

onto the block-fixed sectors such that

$\widehat i_{\alpha\beta}U_{\alpha,k}
=
U_{\beta,k}i_{\alpha\beta}$

and

$\widehat\partial\,U_{\alpha,k}
=
\sqrt M\,U_{\alpha,k-1}\partial_w.$

### 2. Exact persistent-Laplacian direct sum

For every $\alpha\le\beta$ and $k$,

$\boxed{
\widehat\Delta_k^{\alpha,\beta}
=
U_{\alpha,k}
\bigl(M\Delta_{k,w}^{\alpha,\beta}\bigr)
U_{\alpha,k}^{*}
\;\oplus\;
R_{\alpha,\beta,k},
}$

where $R_{\alpha,\beta,k}$ acts on the block-asymmetric sector and

$\boxed{
R_{\alpha,\beta,k}
\succeq
f_{\min}(\alpha)I,
\qquad
f_{\min}(\alpha)
=
\min_{v\in V(K_\alpha)}f_v.
}$

### 3. Exact low-spectrum preservation

For every $0<\Lambda\le f_{\min}(\alpha)$,

$\boxed{
\mathbf 1_{[0,\Lambda)}
\!\left(
\widehat\Delta_k^{\alpha,\beta}
\right)
=
U_{\alpha,k}\,
\mathbf 1_{[0,\Lambda/M)}
\!\left(
\Delta_{k,w}^{\alpha,\beta}
\right)
U_{\alpha,k}^{*}.
}$

Thus every persistent-Laplacian eigenvalue below $f_{\min}(\alpha)$ is exactly $M$ times a weighted persistent-Laplacian eigenvalue, with the same multiplicity.

In particular,

$\ker\widehat\Delta_k^{\alpha,\beta}
=
U_{\alpha,k}
\ker\Delta_{k,w}^{\alpha,\beta},$

and if $\gamma_{\alpha,\beta,k}$ is the weighted persistent gap,

$\boxed{
\widehat\gamma_{\alpha,\beta,k}
\ge
\min\left\{
M\gamma_{\alpha,\beta,k},
f_{\min}(\alpha)
\right\}.
}$

---

## Proof

### Step 1: fixed sectors and boundaries

As before, the fixed sector consists precisely of one-copy-per-block orbit averages. The same computation gives

$\widehat\partial U_\alpha
=
\sqrt M\,U_\alpha\partial_w.$

Since the same $B_v$ is used at every level, the orbit average of a simplex is unchanged by moving to a later complex:

$\widehat i_{\alpha\beta}U_\alpha
=
U_\beta i_{\alpha\beta}.$

### Step 2: persistent domains also commute with unweighting

A fixed vector in $C_{k+1}(\widehat K_\beta)$ has the form $U_{\beta,k+1}z$. Now

$\widehat\partial U_{\beta,k+1}z
=
\sqrt M\,U_{\beta,k}\partial_wz.$

Because orbit averages belonging to distinct base simplices are mutually orthogonal,

$U_{\beta,k}\partial_wz
\in C_k(\widehat K_\alpha)$

if and only if

$\partial_wz\in C_k(K_\alpha,w).$

Consequently,

$\left(
\widehat D_{k+1}^{\alpha,\beta}
\right)^{\mathfrak S}
=
U_{\beta,k+1}
D_{k+1,w}^{\alpha,\beta}.$

For the restricted persistent boundary,

$\widehat b_{k+1}^{\alpha,\beta}
U_{\beta,k+1}
=
\sqrt M\,
U_{\alpha,k}
b_{k+1,w}^{\alpha,\beta}.$

Taking adjoints within the invariant sectors shows that both the persistent up term and the ordinary down term scale by $M$. This proves the symmetric block in the direct-sum formula.

### Step 3: why there is no symmetric–asymmetric mixing

The product group

$\mathfrak S=\prod_v S_{B_v}$

preserves $\widehat K_\alpha$, $\widehat K_\beta$, and the persistent domain. Hence the restricted boundary, its adjoint, and the persistent Laplacian commute with the group action. The fixed sector and its orthogonal complement are therefore reducing subspaces. This gives an exact direct sum, not merely an approximate block diagonalization.

### Step 4: persistent Laplacians dominate ordinary Laplacians

The key new inequality is

$\boxed{
\Delta_k^{K,L}\succeq\Delta_k^K.
}$

Let

$D_{k+1}^{L,K}
=
\{z\in C_{k+1}(L):\partial z\in C_k(K)\}$

and let $b:D_{k+1}^{L,K}\to C_k(K)$ be the restricted boundary. Since

$C_{k+1}(K)\subseteq D_{k+1}^{L,K},$

let $J:C_{k+1}(K)\hookrightarrow D_{k+1}^{L,K}$ denote the isometric inclusion. Then

$bJ=\partial_{k+1}^{K},$

and therefore

$J^{*}b^{*}=(\partial_{k+1}^{K})^{*}.$

For every $x\in C_k(K)$,

$\begin{aligned}
\langle x,bb^{*}x\rangle
&=
\|b^{*}x\|^{2}\\
&\ge
\|J^{*}b^{*}x\|^{2}\\
&=
\|(\partial_{k+1}^{K})^{*}x\|^{2}\\
&=
\left\langle
x,\partial_{k+1}^{K}
(\partial_{k+1}^{K})^{*}x
\right\rangle.
\end{aligned}$

The down terms are identical, proving the inequality.

Applying this to the blow-up pair gives

$\widehat\Delta_k^{\alpha,\beta}
\succeq
\widehat\Delta_k^{\alpha,\alpha}.$

### Step 5: asymmetric-sector lower bound

For clique complexes this is directly Hayakawa’s Theorem 4.3. His proof actually extends to the block substitution of an arbitrary simplicial complex:

- Average over the copies in each block and telescope the complement of the fully fixed projector.

- In the first block $B_v$ where a vector is asymmetric, the vector is supported on simplices meeting $B_v$.

- The relevant expanded star is
  $\Delta(B_v)*
\widehat{\operatorname{lk}_{K_\alpha}(v)}.$

- The augmented Laplacian of this join is the tensor sum of the augmented Laplacians of its factors.

- The full simplex $\Delta(B_v)$ has augmented Laplacian
  $f_v I.$

- The link contribution is positive semidefinite.

- In degree zero, the augmentation correction is supported on the constant chain, which is block-symmetric and therefore vanishes on the asymmetric sector.

Hence

$\widehat\Delta_k^{\alpha,\alpha}
\big|_{T_{\alpha,k}^{\perp}}
\succeq
f_{\min}(\alpha)I.$

Together with persistent domination,

$R_{\alpha,\beta,k}
=
\widehat\Delta_k^{\alpha,\beta}
\big|_{T_{\alpha,k}^{\perp}}
\succeq
f_{\min}(\alpha)I.$

This proves the direct-sum and gap claims. The spectral-projector identity follows immediately.

---

## Sharpness and necessary hypotheses

The asymmetric lower bound is sharp. Let $K=L$ consist of one base vertex with $f$ copies. Its blow-up is an $(f-1)$-simplex. In degree zero the constant vector is symmetric and harmonic, while every asymmetric vector has Laplacian eigenvalue exactly $f$.

The theorem also genuinely requires:

- **One weight per vertex across the filtration.**

- **The same block at every level.**

- **Exact commensurability**
  $Mw(v)^2\in\mathbb N.$

Arbitrary irrational weights require an approximate spectral-perturbation theorem; exact finite unweighting is impossible in general.

---

# 7. Novelty and significance of the stronger theorem

The standard persistent-Laplacian literature proves that its kernel recovers persistent Betti numbers and develops Schur-complement, functoriality, monotonicity, and stability results. [SIAM+1](https://epubs.siam.org/doi/10.1137/21M1435471)

Hayakawa proves the single-complex block reduction and explicitly says filtered extensions are not treated. [arXiv](https://arxiv.org/html/2608.02726v1)

I found no source stating the filtration-wide direct sum

$\widehat\Delta_k^{\alpha,\beta}
\cong
M\Delta_{k,w}^{\alpha,\beta}
\oplus R,
\qquad
R\succeq f_{\min}I,$

or its exact low-spectrum projector consequence. My novelty assessment is therefore:

- **The block gadget is not new.**

- **The naturality identity is elementary.**

- **The persistent domination inequality is elementary but useful.**

- **The combined persistent-Laplacian spectral theorem appears genuinely new.**

- Its proof is short enough that it is probably not a standalone major theorem, but it is materially stronger than the harmonic-overlap corollary and could anchor a substantive TDA section.

It preserves not merely harmonic kernels, but the entire persistent-Laplacian spectrum below a controlled threshold. Since persistent-Laplacian nullity equals persistent Betti number, all persistent Betti numbers are preserved. For one-parameter filtrations, the ordinary persistence module and barcode are also preserved by the natural harmonic identifications—but that is an algebraic consequence, not a new barcode algorithm.

---

# 8. What quantum advantage actually follows

The stronger persistent-Laplacian theorem is **structural**, not itself a quantum algorithm or complexity separation.

The harmonic-persistence corollary gives worst-case complexity evidence only in the following succinct model:

- the complexes are clique complexes specified by polynomial-size graph descriptions or adjacency access;

- the target dimension may grow with the input;

- the guide has a succinct product description and an efficiently accessible orientation/sign convention;

- the final Laplacian has the promised inverse-polynomial gap.

In that model, the chain space may be exponentially larger than the graph description. A classical algorithm that is instead given the complete boundary matrix or a complete list of all target-dimensional simplices is operating under a fundamentally larger input model.

The resulting classification rules out a polynomial-time classical algorithm only under an assumption such as

$\mathsf{BQP}_{1}\nsubseteq\mathsf{BPP}.$

It does **not** prove an unconditional classical lower bound, and that class separation by itself does not formally prove a $2^{\Omega(n)}$ lower bound. “Exponential advantage” remains complexity-theoretic terminology rather than a proved exponential classical running-time lower bound.

The block structure is also classically obvious and can be compressed back to the weighted instance. That does not defeat the hardness—the compressed weighted instance is precisely the hard one—but it confirms that the result is a complexity transfer, not a claim that unweighting conceals an intrinsically harder combinatorial object.

The strongest defensible paper package is therefore:

- **Main structural theorem:** simultaneous functorial unweighting of persistent Laplacians and their low spectrum.

- **Complexity corollary:** orientation-aware unweighted Harmonic Persistence is $\mathsf{BQP}_{1}$-hard and in $\mathsf{BQP}$.

- **Obstruction proposition:** the Möbius zigzag shows that uniformly good local constraint gaps do not control generalized-rank projector overlap.

- **Explicit nonclaims:** no full barcode/decomposition algorithm, no generalized-rank quantum speedup, no sparse practical-input advantage, and no unconditional classical lower bound.

