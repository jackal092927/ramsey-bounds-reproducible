# Archived ChatGPT Pro response — generalized rank and zigzag

Captured on 2026-09-02 PDT from the registered broad discussion after visible account verification. External AI brainstorming; all suggested theorems and novelty claims require independent review. This is an assistant-response-only archive; multiple responses, if any, remain separated in source order.

Conversation: [Brainstorm Quantum Algorithms](https://chatgpt.com/c/6a98bf73-70cc-83e8-b4f5-2f4307a89a88)

---

# Overall assessment

The broad problem

$\text{“given a sparse real/complex diagram, output the exact integer }\rho_I\text{”}$

is **not yet a good quantum-algorithm target**. Exact rank is discontinuous, generalized rank already contains ordinary Betti and persistent-Betti queries as special cases, and both your projector formulation and a more chain-level mapping-cone formulation can have exponentially small relevant singular values despite excellent local conditioning.

The most defensible ITCS direction is narrower:

**Estimate a normalized single zigzag generalized-rank query for a genuinely mixed insertion/deletion class, after compiling it into a linear-size chain-level comparison complex, and prove a topology-derived global conditioning or preconditioning theorem for that class.**

The quantum singular-value machinery would then be the last step, not the contribution. I do **not** currently see an unconditional family giving an end-to-end quantum speedup over the strongest same-access classical algorithm. That part is **UNKNOWN**, not merely unfinished exposition.

A second, riskier direction is a native zigzag reflection algorithm that repeatedly renormalizes local kernel/cokernel computations, potentially escaping the exponentially small global angle. It has a sharp first obstruction: one must “recompress” an implicitly represented reflected subspace without either producing a classical basis or multiplying condition numbers across the entire reflection sequence.

---

# 1. Two immediate novelty filters

## 1.1 Generalized rank does not, by itself, create an easier quantum problem

Two specializations are enough to prevent a generic theorem.

- If $I$ has one vertex, then $\rho_I=\dim H_q(K)$.

- If $I$ consists of one forward arrow $K_a\hookrightarrow K_b$, then $\rho_I$ is the ordinary persistent Betti number $\operatorname{rank}(H_q(K_a)\to H_q(K_b))$.

Thus any general generalized-rank algorithm inherits the state-preparation, spectral-gap, and hardness issues already present in quantum homology and ordinary persistence. Recent work makes these qualifications more, not less, important: the streamlined QSVT persistent-Betti algorithm remains gap- and access-dependent and has a quantum-inspired classical comparator that is only quadratically worse under comparable promises; the recent normalized-persistence complexity paper sharply separates proved quasi-harmonic hardness, conditional algorithms for the genuine normalized problem, and hardness statements that remain conjectural. [arXiv+5arXiv+5arXiv+5](https://arxiv.org/html/2209.12887v3)

Hayakawa’s August 2026 result is also a warning against promises that merely say “unweighted clique complex” and “spectrally gapped”: the corresponding gapped clique-homology problem is QMA$_1$-complete. That does not directly rule out your normalized query under stronger preparation promises, but it rules out a generic BQP claim from local sparsity and a Hodge gap alone. [arXiv](https://arxiv.org/abs/2608.02726)

## 1.2 Two large-looking zigzag classes collapse to ordinary Betti queries

Here is a useful derived lemma for screening examples.

**Lemma: one-sided variation.** Consider a zigzag path of simplicial inclusions.

- If the $q$-chain spaces vary but there are no $(q+1)$-cells, then
  $\rho_I=\dim\bigcap_t Z_q(K_t)=\beta_q\!\left(\bigcap_tK_t\right).$

- If the $q$-skeleton and $Z_q$ are fixed and only $(q+1)$-cells vary, then
  $\rho_I=\dim Z_q\Big/\sum_tB_q(K_t)
       =\beta_q\!\left(\bigcup_tK_t\right).$

The first statement follows because the diagram consists of literal subspaces and its limit is their intersection, which injects into the colimit along a path. The second is the dual quotient statement.

Consequences:

- A full-interval $H_1$ query for graph zigzags is just $H_1$ of the intersection graph.

- With a fixed vertex set, the analogous $H_0$ query is the number of components of the union graph.

- A convincing example must mix creation of cycles and creation of fillings.

This also reinforces the classical collision: even the **full** graph zigzag barcode has near-linear classical algorithms, so graph examples are particularly poor evidence for a quantum advantage. [arXiv](https://arxiv.org/abs/2103.07353?utm_source=chatgpt.com)

---

# 2. Independent audit of the proposed algebra

## 2.1 The projector identity is correct

Let

$U=\bigoplus_{v\in I}V_v,\qquad
L=\ker D,\qquad K=\ker B^\dagger.$

Since $K=(\operatorname{im}B)^\perp$, orthogonal projection onto $K$ gives the minimum-norm representative of a colimit class.

For $x=(x_v)_v\in L$, all classes $[J_vx_v]\in\operatorname{coker}B$ agree. Therefore

$[x]=\sum_v[J_vx_v]
   =m[J_rx_r]$

for any fixed root $r$. Consequently, under the orthogonal realization of the colimit,

$\psi(x)=\frac1mP_Kx.$

Hence

$\boxed{\rho_I=\operatorname{rank}(P_KP_L).}$

This is exact over $\mathbb R$ or $\mathbb C$. The factor $1/m$ matters for singular values but not rank.

Also,

$\operatorname{Tr}(P_LP_K)
  =\sum_j\cos^2\theta_j,$

where the $\theta_j$ are principal angles between $L$ and $K$. It is not the number of nonzero principal angles unless all nonzero cosines happen to equal one.

Your scalar-chain calculation is also correct. With maps $a$,

$L=\operatorname{span}(1,a,\ldots ,a^{m-1}),\qquad
K=\operatorname{span}(a^{m-1},\ldots ,a,1),$

and their unique nonzero projector-product singular value is

$\gamma_m
=\frac{m(1-a^2)a^{m-1}}{1-a^{2m}}.$

Meanwhile, the nonzero singular values of the constraint matrices stay in $[1-a,1+a]$. So local solvability of the limit and colimit constraints does not control the global pairing.

## 2.2 The chain-level primal/dual formula is also correct after making the spaces explicit

The notation in the question suppresses distinct source-copy and target-copy edge spaces. Define

$C^V_q=\bigoplus_vC_q(K_v),\qquad
C^{E,t}_q=\bigoplus_{e:u\to v}C_q(K_v),\qquad
C^{E,s}_q=\bigoplus_{e:u\to v}C_q(K_u).$

Let

$(\delta_qx)_e=x_v-F_ex_u,$

and

$\tau_qz=\sum_{e:u\to v}(J_vF_ez_e-J_uz_e).$

Then the primal operator is

$A_q(x,y)=
\left(
\partial_q^Vx,\;
\delta_qx-\partial_{q+1}^{E,t}y
\right).$

For the dual, take $k\in C^V_q$ and $a\in C^{E,s}_{q-1}$:

$A_q^\vee(k,a)=
\left(
\partial_q^Vk,\;
(\partial_{q+1}^V)^\dagger k,\;
\tau_q^\dagger k-(\partial_q^{E,s})^\dagger a
\right).$

The three conditions say:

- each $k_v$ is a cycle;

- each $k_v$ is orthogonal to boundaries;

- for every edge $u\to v$, the two homology functionals agree after transport:
  $F_e^\dagger k_v-k_u\in\operatorname{im}\partial_{q,u}^\dagger.$

Thus the projected $k$-coordinates of $\ker A_q^\vee$ represent $(\operatorname{colim}H_q)^*$, while the projected $x$-coordinates of $\ker A_q$ represent compatible cycle lifts of the limit.

For $(x,y)\in\ker A_q$ and $(k,a)\in\ker A_q^\vee$,

$\langle k_v,x_v\rangle=\langle k_u,x_u\rangle$

along every edge. Indeed, the discrepancy pairs either with a boundary or with $\partial x_u=0$. Therefore

$\sum_v\langle k_v,x_v\rangle
=m\langle \lambda,\psi([x])\rangle,$

where $\lambda$ is the corresponding colimit functional. This proves

$\boxed{
\rho_I=
\operatorname{rank}
\left(
P_{\ker A_q^\vee}\,
\pi_k^\dagger\pi_x\,
P_{\ker A_q}
\right).
}$

So I do not find an algebraic error in the proposed chain-level identity. The caveats are exactly the ones you identified: auxiliary dimensions, preparation, fillings, and global angles.

---

# 3. A cleaner direct chain-level reduction

There is a useful alternative that avoids both a free homology basis and the explicit primal-versus-dual projector product.

## 3.1 Compatibility and relation complexes

Define the **compatibility complex**

$\mathcal L_q=C^V_q\oplus C^{E,t}_{q+1},$

with differential

$d_q^{\mathcal L}(x,y)
=
\left(
\partial x,\;
\delta x-\partial y
\right).$

Define the **relation complex**

$\mathcal C_q=C^V_q\oplus C^{E,s}_{q-1},$

with differential

$d_q^{\mathcal C}(k,z)
=
\left(
\partial k+\tau z,\;
-\partial z
\right).$

The chain-map identities for the $F_e$ imply $(d^\mathcal L)^2=(d^\mathcal C)^2=0$.

Fix any root vertex $r$, and define the sparse chain map

$c_{r,q}:\mathcal L_q\longrightarrow\mathcal C_q,
\qquad
c_{r,q}(x,y)=(J_rx_r,0).$

## 3.2 Exact theorem

**Proposition — derived directly from the canonical limit-to-colimit definition.**

$\boxed{\rho_I=\operatorname{rank}H_q(c_r).}$

This holds over any coefficient field.

**Proof sketch.**

- A cycle $(x,y)\in\mathcal L_q$ consists of vertex cycles satisfying
  $x_v-F_ex_u=\partial y_e.$
  Hence it determines a compatible tuple in $\lim H_q(K_v)$. Every compatible tuple admits such fillings, so
  $H_q(\mathcal L)\twoheadrightarrow\lim H_q(K_v).$

- A colimit class represented by a vertex cycle $x$ maps to $[(x,0)]\in H_q(\mathcal C)$. Colimit relations are boundaries because, for an edge cycle $z$,
  $(\tau z,0)=d^\mathcal C(0,z).$
  Conversely, if $(x,0)$ is a total boundary, the edge component of the preimage must be a tuple of cycles, so $x$ is a sum of ordinary boundaries and colimit relations. Therefore
  $\operatorname{colim}H_q(K_v)\hookrightarrow H_q(\mathcal C).$

- The induced map $H_q(c_r)$ is the composite
  $H_q(\mathcal L)\twoheadrightarrow
\lim H_q
\longrightarrow
\operatorname{colim}H_q
\hookrightarrow
H_q(\mathcal C).$

Surjectivity on the left and injectivity on the right preserve the rank.

This route uses no unfolding theorem.

## 3.3 Reduction to three ordinary matrix ranks

For any chain map $f:A_\bullet\to B_\bullet$, define

$\mathscr R_q(f)=
\begin{bmatrix}
d_q^A&0\\[2mm]
f_q&-d_{q+1}^B
\end{bmatrix}.$

A direct image-space calculation gives

$\boxed{
\operatorname{rank}H_q(f)
=
\operatorname{rank}\mathscr R_q(f)
-\operatorname{rank}d_q^A
-\operatorname{rank}d_{q+1}^B.
}$

Therefore

$\boxed{
\rho_I=
\operatorname{rank}\mathscr R_q(c_r)
-\operatorname{rank}d_q^{\mathcal L}
-\operatorname{rank}d_{q+1}^{\mathcal C}.
}$

For cell-wise simplicial inclusions, these are sparse integer matrices with entries in $\{0,\pm1\}$.

I did not locate this exact chain-level statement in the searched literature. That is **not** evidence of novelty. It is close enough to mapping-cone folklore and to existing interval-multiplicity rank formulas that I would not sell the identity itself. Asashiba–Liu already provide structured formulas and essential-cover methods for interval multiplicities, including zigzag settings. [arXiv+1](https://arxiv.org/pdf/2411.11594)

The potentially new content would be:

- a linear-size topology-level compiler;

- coherent sparse access to the resulting matrices;

- a genuinely topological conditioning or preconditioning theorem.

---

# 4. The conditioning obstruction survives this reduction

The total-complex formulation removes the **particular** projector-product angle, but generic spectral rank estimation merely moves the small singular value into $\mathscr R_q(c_r)$.

## 4.1 A stronger zigzag obstruction

For fixed $d>1$, consider the one-dimensional zigzag module

$V_0\xrightarrow{d}W_1\xleftarrow{1}V_1
\xrightarrow{d}W_2\xleftarrow{1}\cdots
\xrightarrow{d}W_n\xleftarrow{1}V_n.$

It has one full interval. A limit generator is

$\ell=(1,d,d,d^2,d^2,\ldots,d^n,d^n),$

and a colimit-dual generator is

$k=(d^n,d^{n-1},d^{n-1},\ldots,1,1).$

Hence

$\gamma_n=
\frac{(2n+1)d^n}
{\sqrt{
\left(1+2\sum_{i=1}^nd^{2i}\right)
\left(d^{2n}+2\sum_{j=0}^{n-1}d^{2j}\right)
}}
=\Theta(nd^{-n}).$

On the other hand, the row Gram matrix of the limit constraint operator has a $2\times2$ Toeplitz symbol with determinant

$d^2+1-2d\cos\theta\ge(d-1)^2.$

Thus its nonzero singular values, and similarly those of the colimit-relation operator, are bounded below by a positive constant depending only on $d$.

In the total-complex rank formula, choose root $V_0$. In this module-level case,

$\mathscr R_q(c_r)=
\begin{bmatrix}
D&0\\
c_r&-B
\end{bmatrix}$

is square and nonsingular. Taking $x=\ell/\|\ell\|$ and the edge variable zero gives

$\|\mathscr R_q(c_r)(x,0)\|
=\|c_rx\|
=\frac1{\|\ell\|}
=\Theta(d^{-n}).$

Therefore

$\sigma_{\min}\bigl(\mathscr R_q(c_r)\bigr)
=O(d^{-n}).$

Direct elimination also gives

$\left|\det\mathscr R_q(c_r)\right|=d^n.$

Thus even a sparse integer mapping-cone matrix can have exponentially bad spectral conditioning and exponentially large minors.

## 4.2 A small topological realization

This algebraic family has a natural fixed-dimensional topological realization.

Take a fixed simplicial degree-$d$ map

$f:S^1\to S^1$

and a fixed triangulated mapping cylinder $M_f$. The two inclusions

$S^1_{\mathrm{domain}}\hookrightarrow M_f
\hookleftarrow S^1_{\mathrm{target}}$

induce multiplication by $d$ and by $1$, respectively, on $H_1(-;\mathbb R)$. Concatenating copies produces the zigzag above.

Each coarse inclusion can be refined into $O(1)$ elementary simplex additions or deletions because $d$ and the triangulated gadget are fixed. At every intermediate complex, the endpoint circle class remains nonzero: its composite into the final mapping cylinder is injective. Since the endpoint $H_1$ spaces are one-dimensional, the refined zigzag still has generalized rank exactly one.

This provides, modulo writing out one explicit triangulation and update order, the small simplicial-filtration version missing from the original scalar-chain example:

- dimension $2$;

- constant-size local gadgets;

- both $1$- and $2$-simplices change;

- every stage comes from a fixed finite collection of complexes, so all local nonzero Hodge singular values are uniformly bounded below;

- the global generalized-rank angle remains exponentially small.

Barycentric subdivision can make the gadgets flag if a clique-complex formulation is desired.

I regard the algebraic proof as complete. Before using the topological version as a theorem, I would still write and mechanically check one explicit signed boundary/update list.

## 4.3 Consequence for preconditioning

This family kills any theorem of the form

local Hodge gaps + local diagram-constraint gaps

$\Longrightarrow$ polynomial generalized-rank gap.

It also kills naive vertexwise gauge balancing. To reduce the ratio $d:1$ at every mapping-cylinder span, vertex scalings must change geometrically along the zigzag; the scaling condition number is exponential.

A successful preconditioner must therefore use **global combinatorial structure**, not merely local Laplacian inverses or independent basis changes at the vertices.

---

# 5. Relevant collision map

## Classical zigzag and generalized-rank collisions

- **FastZigzag.** Dey–Hou transform a cell-wise zigzag into a same-length cell-wise ordinary filtration of a $\Delta$-complex and transfer the barcode. Their published treatment uses $\mathbb Z_2$; the end-to-end time is $T(m)+O(m)$, hence $O(m^\omega)$ with the theoretical ordinary-persistence bound. A proposal that says “run FastZigzag, then a known quantum persistent-Betti routine” is not novel. A signed $\mathbb R/\mathbb C$ coherent oracle for the transformed complex and preservation of spectral promises are not automatic. [DOI Resolver+2arXiv+2](https://dx.doi.org/10.4230/LIPICS.ESA.2022.43)

- **Two-parameter boundary reduction.** Dey–Kim–Mémoli already identify the generalized rank on a finite two-dimensional interval with that of a boundary-tracing zigzag and obtain an $O(t^\omega)$ algorithm. Thus “use only the boundary of a rectangle and reduce it to a zigzag” is already occupied. [arXiv](https://arxiv.org/abs/2111.15058)

- **Minimal subposets.** Brüstle–Desrochers–Leblanc’s August 2026 revision gives initial/final subcategory conditions preserving generalized rank and studies minimal full subposets. This can reduce the index category, but it gives neither small chain spaces nor a conditioning guarantee. For general module maps, accessing a retained composite morphism may itself be expensive. [arXiv+1](https://arxiv.org/abs/2510.10837)

- **Reflection algorithms.** Reflection and transposition methods already support a full classical zigzag algorithm with explicit representative maintenance and cubic worst-case time. A quantum reflection proposal must contribute more than replacing each local matrix reduction by QSVT. [Geometrica](https://geometrica.saclay.inria.fr/team/Steve.Oudot/papers/mo-zzpvrt-14/mo-zzpvrt-14.pdf?utm_source=chatgpt.com)

## Quantum collisions and barriers

- McArdle–Gilyén–Berta already use normalized projectors and singular-value transformation for persistent Betti estimation, and analyze a closely matched classical comparator. The meaningful quantum benefit is largely in coherent trace/amplitude estimation, not an unexplained speedup for exact rank. [arXiv+1](https://arxiv.org/html/2209.12887v3)

- Gyurik et al.’s guided/kernel-overlap formulation is BQP-hard under suitable promises and is in BQP, but the supplied state or hole is important; they explicitly leave open whether relevant sparse simplicial families give a useful advantage. That is different from discovering an unguided full-bar subspace. [arXiv+1](https://arxiv.org/html/2410.21258v2)

- Black–Maxwell–Nayyeri’s span-program witnesses are governed by effective resistance and capacitance. Those witness sizes can be exponential, giving exactly the kind of hidden global obstruction present here. [arXiv+1](https://arxiv.org/pdf/2307.07073)

- Over finite fields, generic rank is not a free quantum primitive. In the matrix-vector oracle model, Childs–Hung–Li prove linear bounded-error quantum query complexity for rank. [arXiv](https://arxiv.org/pdf/2102.11349)

---

# 6. Route A — compressed space-time comparison complexes

This is the route I would investigate first.

## 6.1 Exact computational problem

Call the preferred problem **Mixed Zigzag Survival Fraction**.

### Input

A cell-wise zigzag

$K_0\leftrightarrow K_1\leftrightarrow\cdots\leftrightarrow K_m$

of finite oriented simplicial complexes, with coefficients in $\mathbb R$ or $\mathbb C$, homological degree $q$, and a specified root stage $r$.

The access model should explicitly provide:

- a reversible event oracle returning the added or removed simplex at step $t$;

- signed boundary and, when needed, coface access;

- a presence-interval or cell-copy indexer;

- coherent row/column state preparation, or bounded row and column sparsity;

- dimensions and padding conventions;

- a reversible indexer for the compressed comparison matrices.

No homology basis, harmonic-state oracle, or precomputed barcode is supplied.

Let $N$ be a known common padded domain size for the matrices occurring in the rank formula.

### Output

Two possible versions:

$r_I=\frac{\rho_I}{N},$

estimated to additive error $\epsilon$; or, preferably,

$\theta_{I,r}
=\frac{\rho_I}{\beta_q(K_r)}.$

For the latter, promise

$\beta_q(K_r)\ge\eta N$

and output $\widehat\theta$ satisfying

$|\widehat\theta-\theta_{I,r}|\le\epsilon$

with probability at least $2/3$.

The clean decision version is

$\theta_{I,r}\le b
\quad\text{versus}\quad
\theta_{I,r}\ge a,
\qquad a-b\ge2\epsilon.$

This is topologically more meaningful than normalization by an arbitrary chain-space dimension.

### Spectral and access promises

After compression and block-encoding normalization, every nonzero singular value of

$d_q^{\widetilde{\mathcal L}},\qquad
d_{q+1}^{\widetilde{\mathcal C}},\qquad
\mathscr R_q(\widetilde c_r)$

is at least $\delta_{\mathrm{st}}$.

For the root Betti denominator, impose the same promise on

$\partial_q(K_r),\qquad\partial_{q+1}(K_r).$

The promise is global and must refer to the actual matrices used by the algorithm. Local stage gaps are insufficient.

## 6.2 Quantum algorithm under those promises

Use singular-value threshold polynomials to block-encode the row-space projector of each matrix. Feed it a maximally mixed state on the padded domain; this can be produced using an EPR pair over computational-basis labels, without preparing a uniform state on homology.

The exact rank identity gives

$\frac{\rho_I}{N}
=
\frac{
\operatorname{rank}\mathscr R_q(c_r)
-\operatorname{rank}d_q^\mathcal L
-\operatorname{rank}d_{q+1}^\mathcal C
}{N}.$

Amplitude estimation of the three normalized traces yields, suppressing logarithmic precision factors,

$\widetilde O\!\left(
\frac{Q_{\mathrm{BE}}}
{\epsilon\,\delta_{\mathrm{st}}}
\right)$

coherent oracle calls for $\rho_I/N$.

For the survival fraction, estimate

$\frac{\beta_q(K_r)}N
=
\frac{\dim C_q(K_r)
-\operatorname{rank}\partial_q
-\operatorname{rank}\partial_{q+1}}N$

as well. Error propagation gives approximately

$\widetilde O\!\left(
\frac{Q_{\mathrm{BE}}}
{\epsilon\,\eta\,\delta_{\mathrm{st}}}
\right).$

This avoids a uniform mixture over a harmonic kernel. It does **not** avoid the need for a singular gap.

To recover the exact integer $\rho_I$, one needs error below $1/(2N)$, giving at least

$\widetilde\Omega\!\left(\frac{N}{\delta_{\mathrm{st}}}\right)$

uses. Exact rank is therefore not the result to lead with.

## 6.3 The actual new mechanism

The contribution cannot be the QSVT trace estimator. It must be the following pair of structural theorems.

### Target theorem A1: linear-size exact compiler

For an elementary zigzag with $M$ cell-presence intervals and incidence events, construct chain complexes

$\widetilde{\mathcal L},\quad
\widetilde{\mathcal C}$

and a chain map $\widetilde c_r$ such that

$\operatorname{rank}H_q(\widetilde c_r)=\rho_I,$

with:

- $O(M)$ rows, columns, and nonzeros up to dimension-dependent factors;

- signed validity over $\mathbb Z$, hence over $\mathbb R/\mathbb C$;

- a reversible coordinate map computable in $\operatorname{polylog}M$ or a clearly stated update-oracle cost;

- no expansion to $\sum_t|K_t|$, which can be quadratic.

The expected construction is to collapse temporal identity strands by unit pivots or discrete Morse cancellations, leaving one variable per contiguous cell-presence interval. But this must be written as an exact chain equivalence preserving $H_q(c_r)$.

FastZigzag is the closest collision. The compiler is only valuable if it provides signed chain maps, direct coherent access, and a conditioning analysis not inherited from that conversion. [DOI Resolver+1](https://dx.doi.org/10.4230/LIPICS.ESA.2022.43)

### Target theorem A2: topology-derived global conditioning

For a natural, genuinely mixed class $\mathfrak Z$, prove that the three compressed matrices admit efficiently accessible preconditioners with controlled condition number, or directly satisfy

$\sigma_{\min}^+\ge M^{-c}$

for a useful exponent $c$.

A useful discrete route is through minors. If an integer rank-$r$ matrix $A$ has every square minor bounded by $\Delta$, then

$\sigma_{\min}^+(A)\ge \frac1{r\Delta}.$

Indeed, select a nonsingular $r\times r$ minor $B$; its determinant has magnitude at least one, while all cofactors are bounded by $\Delta$, so $\|B^{-1}\|\le r\Delta$.

For a totally unimodular matrix,

$\sigma_{\min}^+(A)\ge\frac1r.$

This suggests a **space-time torsion/minor parameter**, not a per-stage torsion parameter. Boundary-matrix total unimodularity is characterized by the absence of torsion in all relevant relative subcomplex pairs, but that criterion applies to the global boundary matrix under consideration; total unimodularity of every individual stage is not obviously preserved by temporal gluing or mapping cones. [arXiv+1](https://arxiv.org/pdf/1001.0338)

A plausible first candidate is:

zigzags whose compressed comparison matrices represent regular matroids, perhaps arising from controlled generalized parallel connections of regular stage-wise pieces.

A more geometric candidate is a sharply restricted surface or cobordism class for which every relevant **space-time** relative pair is torsion-free. Do not assume that “every stage is an orientable surface” suffices.

The degree-$d$ mapping-cylinder family should be outside the positive class: it generates the minor $d^n$.

## 6.4 Why this is not merely “known reduction + QSVT”

Three facts would be new and persistence-specific:

- generalized rank is represented directly by a sparse chain map without homology bases or reliance on the unfolding theorem;

- temporal identity strands are eliminated while preserving coherent access;

- topology controls the global comparison-complex conditioning.

Without item 3, the result is just a generic gapped-rank estimator.

## 6.5 Strongest classical comparisons

The comparison must include all of the following.

- $O(m^\omega)$-type full zigzag barcode computation via FastZigzag, not textbook cubic reduction. [arXiv](https://arxiv.org/pdf/2204.11080)

- $O(t^\omega)$ boundary-zigzag computation for finite two-dimensional intervals. [arXiv](https://arxiv.org/abs/2111.15058)

- Asashiba–Liu’s structured interval-multiplicity formulas and covers. [arXiv+1](https://arxiv.org/pdf/2411.11594)

- Sparse polynomial-filter plus stochastic trace estimation under the same gap and matrix-vector access promises.

- The quantum-inspired comparator analyzed by McArdle–Gilyén–Berta. [arXiv](https://arxiv.org/html/2209.12887v3)

- Near-linear specialized graph algorithms whenever the proposed class accidentally reduces to graphs. [arXiv](https://arxiv.org/abs/2103.07353?utm_source=chatgpt.com)

Under explicit sparse input, a classical Chebyshev/Lanczos trace estimator may already be close to input-linear per probe. The most robust likely quantum gain is quadratic in trace-estimation precision, unless the coherent oracle describes an exponentially larger matrix. A succinct exponentially large example would need a classical lower bound or at least a serious no-shortcut argument.

## 6.6 Concrete advantage family

**Status: UNKNOWN.**

A conditional candidate would have:

- $N$ exponentially larger than the succinct input;

- constant or inverse-polylogarithmic $\delta_{\mathrm{st}}$;

- $\rho_I/\beta_q(K_r)=\Theta(1)$;

- efficient coherent incidence access;

- no Fourier, product, symmetry, or local decomposition giving an equally succinct classical solution.

I do not currently have such a topological family.

A disjoint union of hidden constant-size gadgets would give the standard $1/\epsilon$ versus $1/\epsilon^2$ approximate-counting separation, but that is approximate counting dressed as TDA and is not an adequate ITCS story.

## 6.7 Cheap falsification and stop/go rule

Do these before any simulator.

- **Write the degree-two mapping-cylinder gadget explicitly.** Compute the signed matrices and confirm the exponential global singular value after cell-wise refinement.

- **Perform symbolic temporal elimination.** Derive the claimed $O(M)$ compressed matrices and verify that no dense Schur complement or long-path access is hidden.

- **Enumerate small candidate positive gadgets exactly.** Compute Smith forms and all maximal minors. One determinant $>1$ refutes total unimodularity; a repeatable transfer gadget producing determinant growth refutes polynomial-minor closure.

- **Check the one-sided-collapse filter.** The positive class must contain examples where both $q$-cycle and $(q+1)$-filling spaces change.

- **Compare polynomial degrees, not only asymptotic matrix dimensions.** Use the same $\delta_{\mathrm{st}}$, preparation, and oracle cost for the quantum and stochastic classical algorithms.

**Go** if you obtain both A1 and A2 for a nontrivial mixed class and the resulting exponent beats the strongest same-model classical bound.

**Stop as the main algorithmic paper** if the theorem is only “assuming a global gap, QSVT estimates three ranks,” if the compiler is simply FastZigzag as a black box, or if the positive class collapses to an intersection/union Betti query.

---

# 7. Route B — native reflection with local renormalization

This is the most plausible way to evade the global-angle counterexample rather than merely relocating it.

## 7.1 Exact problem

First formulate it for an explicitly given zigzag module:

$V_0\leftrightarrow V_1\leftrightarrow\cdots\leftrightarrow V_m$

over $\mathbb C$, with sparse block encodings of all arrow matrices and known dimensions.

Output the normalized multiplicity of the full interval,

$\frac{\rho_{[0,m]}}{\dim V_r},$

to additive error $\epsilon$.

For a topology-level theorem, this module-oracle model is insufficient: one must compile the required local operations directly from chain and update oracles without being handed homology bases.

## 7.2 Reflection mechanism

At a sink

$V_{i-1}\xrightarrow{A}V_i\xleftarrow{B}V_{i+1},$

the reflected center is

$V_i'=\ker[A,-B]\subseteq V_{i-1}\oplus V_{i+1},$

with outgoing coordinate maps.

At a source

$V_{i-1}\xleftarrow{A}V_i\xrightarrow{B}V_{i+1},$

the reflected center can be realized orthogonally as

$V_i'=
\ker
\begin{bmatrix}
A\\-B
\end{bmatrix}^{\!\dagger},$

representing the corresponding cokernel.

Reflection/transposition algorithms already exploit these local quiver operations classically. [Geometrica+1](https://geometrica.saclay.inria.fr/team/Steve.Oudot/papers/mo-zzpvrt-14/mo-zzpvrt-14.pdf?utm_source=chatgpt.com)

The proposed quantum algorithm would:

- follow a predetermined reflection sequence that carries the target full interval to a locally detectable simple summand;

- use QSVT only to form each local kernel or orthogonal cokernel;

- estimate the relevant local dimension changes;

- **recompress after every reflection**, preventing condition numbers or polynomial degrees from multiplying across the sequence.

On the scalar degree-$d$ obstruction, each local sink matrix $[d,-1]$ is perfectly well-conditioned, although the global canonical angle is exponentially small. Therefore a truly local reflection algorithm could distinguish itself from the global-projector and global-mapping-cone routes.

## 7.3 The smallest worthwhile theorem

The central theorem is not the reflection identity. It is:

**Reflection recompression lemma.** Given coherent access to the current reflected representation and a local pivot whose nonzero singular values are at least $\delta_{\mathrm{ref}}$, construct coherent access to the next reflected representation with cost polynomial in $1/\delta_{\mathrm{ref}}$ and the inverse active-space density, such that costs add or remain polynomial over the reflection sequence rather than multiplying.

This includes:

- a compact label space for the new kernel/cokernel;

- an isometry between that label space and the implicit reflected subspace;

- block encodings of the new neighboring arrows;

- controlled accumulated approximation error;

- no classical basis output.

A second theorem must track the full interval through the chosen sequence, including the simple summands annihilated by reflection functors.

Without recompression, nested QSVT projectors can have degree or normalization cost comparable to a product of inverse local gaps. Then the route has simply hidden the global obstruction in the expression tree.

## 7.4 Topological version

The topology-level version must operate on the rank-one diamonds produced by simplex additions and deletions. It must not first compute explicit homology matrices.

A potentially valid mechanism is:

- represent each reflected space as homology of a small chain-level kernel/cokernel complex;

- simplify that complex immediately by exact unit-pivot cancellations;

- maintain only an event-sized description and a block encoding of its remaining boundary maps.

However, if this chain-level transformation reconstructs exactly the copied/coned filtration of FastZigzag and then invokes an ordinary persistence algorithm, the novelty disappears.

## 7.5 Concrete advantage family

**Status: UNKNOWN.**

The degree-$d$ mapping-cylinder family is useful because it separates:

- exponentially bad global projector and mapping-cone gaps;

- constant local reflection gaps.

But each vector space in that family is one-dimensional, so its classical computation is trivial. It is a structural separation, not a runtime separation.

The desired high-dimensional family would have:

- constant local reflection gaps throughout a known reflection schedule;

- large reflected spaces with efficient succinct access;

- no efficient classical way to maintain all reflected ranks or bases;

- a global projector angle exponentially smaller than every local reflection gap.

I do not yet have such a family.

## 7.6 Cheap falsification and stop/go rule

- Work out a four- or six-arrow representation symbolically. Track the exact block-encoding normalization after every reflection.

- Test whether preparing a maximally mixed state on the new kernel requires producing a basis or costs the reciprocal square root of a shrinking subspace density.

- Determine whether the query degree is additive or multiplicative in the inverse reflection gaps.

- Run the construction on the degree-$d$ family. It must have polynomial cost there; otherwise it has not escaped the known obstruction.

- Implement the same algebra on one signed mapping-cylinder cell gadget. If the method requires precomputed homology arrow matrices, it is not yet a TDA algorithm.

**Go** only if one reflection can be recompressed without a basis and a sequence has additive rather than multiplicative conditioning cost.

**Stop** if the compact kernel-label oracle is equivalent to outputting a basis, or if the final reflected gap reproduces the original $\gamma_n$.

---

# 8. Audit of the Dey–Xin unfolding dependency

I do not use the unfolding theorem in either main route.

The current v4 paper constructs an Euler-tour-type zigzag by copying module grades, states a convertibility criterion for certain full zigzag bars, and iteratively extracts full summands. [arXiv+3arXiv+3arXiv+3](https://arxiv.org/html/2403.08110v4)

Here is the dependency breakdown.

| Claim from the unfolding route | Audit status | Needed here? |
| --- | --- | --- |
| A connected index poset can be traversed by a zigzag of repeated grades of linear size using a spanning-tree/Euler traversal. | **Checked combinatorially.** | No. |
| Precomposing the module or chain diagram with that traversal gives the stated copied zigzag. | **Checked.** | No. |
| A full interval direct summand of the original module produces a full bar in the copied zigzag. | **Checked.** It follows by precomposition. | No. |
| Every contribution to generalized rank can be recovered from a “convertible” full bar, followed by iterative quotienting. | **Unresolved.** This is the substantive converse, not a formal property of precomposition. | No. |
| The convertibility system and the complement construction preserve the required module direct-sum structure through every iteration. | **Unresolved.** It needs a complete basis-independent proof. | No. |
| Proposition 6.3’s quotient/coning test can treat $M/\mathrm{Fld}(I)$ as a submodule with restricted maps. | **Proof obligation identified.** A quotient by a direct summand is isomorphic to a complementary submodule but is not canonically a literal submodule. Because a direct summand has a module complement, this may be repairable, but an explicit natural splitting must be selected and carried through the construction. [arXiv](https://arxiv.org/html/2403.08110v4) | No. |
| The stated end-to-end running time follows. | **Unresolved**, because it depends on the converse, splitting, iteration, and representative-cost claims. [arXiv+1](https://arxiv.org/html/2403.08110v4) | No. |
| The special $d$-complex/graph consequences hold with the stated bounds. | **Not audited.** [arXiv](https://arxiv.org/html/2403.08110v4) | No. |

This is not a conclusion that the unfolding theorem is false. It means the parts needed to infer generalized rank from full bars of the copied zigzag have not been independently established here.

For arbitrary posets, the direct $\mathcal L\to\mathcal C$ construction works on the original diagram. A separately verified minimal-subposet theorem could be used as a front-end compression, but no unfolding/folding converse is needed.

---

# 9. Why I would not prioritize the suggested fallbacks

## 9.1 AIDA splitting-subspace search

AIDA’s difficult term comes from a finite-Grassmannian search controlled by the maximum number $k$ of same-grade relations; $k$ is not the grid size. The search contribution has the form

$q^{k^2/4+O(k)}$

inside a larger end-to-end algebraic cost. A naive Grover replacement would change this to roughly

$q^{k^2/8+O(k)},$

but would not remove preprocessing, Hom computations, or coherent feasibility-oracle costs. Subsequent general-module work gives a stronger full classical bound, raising the comparison bar further. [DROPS+2DROPS+2](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2025.41)

Together with the linear finite-field matrix-vector lower bound for generic rank, this makes “Grover over splitting subspaces” too weak for the lead project. [arXiv](https://arxiv.org/pdf/2102.11349)

I would revisit it only after finding additional Grassmannian structure—an automorphism quotient, quantum walk with nontrivial spectral gap, or meet-in-the-middle feasibility representation—that improves the **end-to-end** exponent.

## 9.2 Anchored span programs

There is a mathematically clean guided problem:

- given a root cycle $z$, determine whether $[z]$ extends to a compatible section over the entire zigzag;

- and whether its canonical colimit image is nonzero.

The extension condition has the primal witness

$\partial x=0,\qquad
\delta x=\partial y,\qquad
x_r-z=\partial h.$

Colimit triviality has a relation/filling witness, while nontriviality has a dual separator described by $A^\vee$.

This is a good primal/dual certificate system. But it is a **guided** problem, not the unguided rank query. Moreover, the obvious Euclidean extension and separator energies are exponential on the degree-$d$ family: anchoring at one end makes the compatible lift grow like $d^n$; anchoring at the other moves the exponential growth to the dual separator. That is consistent with the effective-resistance/capacitance obstruction in Black–Maxwell–Nayyeri. [arXiv+1](https://arxiv.org/pdf/2307.07073)

I would spend only a small analytic effort on this: derive the exact witness sizes on the mapping-cylinder family. Promote it only if a deletion-aware composition law provably keeps the witness product polynomial where the global angle is exponential.

## 9.3 Local barcode mass and sampling

For

$U=Z_b\cap B_d,\qquad
V=(Z_a\cap B_d)+(Z_b\cap B_c),$

one has $V\subseteq U$, so $P_U-P_V$ is indeed the orthogonal projector onto $U\cap V^\perp$. The algebraic quotient dimension can also be expressed through block-matrix ranks.

But constructing the two projectors has the same intersection, filling, and spectral-gap problems. A correctly normalized sampler additionally needs efficient preparation proportional to the local barcode mass. Chen–Kerber’s output-sensitive long-bar algorithm is the relevant classical baseline, while harmonic and Grassmannian persistence already provide canonical representative-subspace frameworks that must be distinguished from the new proposal. [Stony Brook University+2DOI+2](https://researchconnect.stonybrook.edu/en/publications/an-output-sensitive-algorithm-for-persistent-homology-2/)

This is a sensible application after Route A succeeds, not an independent mechanism.

---

# Final selection

## 1. Investigate first: compressed comparison complex plus space-time conditioning

The first concrete problem is:

**Characterize a nontrivial mixed class of cell-wise zigzags for which the temporally compressed matrices $d^\mathcal L$, $d^\mathcal C$, and $\mathscr R(c_r)$ have polynomially controlled minors or efficiently accessible polynomial-condition preconditioners.**

Start by proving the exact compiler and attacking the total-unimodularity/space-time-torsion closure claim on small gadgets. The principal failure risk is that every natural mixed class already contains repeatable degree-transfer gadgets causing exponential minors. If that happens, do not paper over it with a global-gap promise.

## 2. Investigate second: one-step reflection recompression

The second concrete problem is:

**Can a kernel or orthogonal-cokernel reflection be converted into a fresh compact block-encoded representation with additive conditioning cost and no explicit basis?**

First solve one reflection exactly, then two composed reflections. The principal failure risk is that “recompression” is computationally equivalent to finding the transformed basis or that block-encoding costs multiply.

If the space-time conditioning lemma fails, this reflection route is the correct alternative because it can, in principle, pass the degree-$d$ obstruction. If reflection recompression also fails, the honest conclusion is that no substantive quantum generalized-rank algorithm has yet emerged from these mechanisms. At that point, the strongest result may instead be a negative conditioning theorem for local or block-diagonal preconditioners, paired with the explicit mapping-cylinder family—not Groverized AIDA or FastZigzag followed by generic QSVT.

