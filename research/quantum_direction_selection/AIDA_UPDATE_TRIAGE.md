# AIDA candidate-exchange update triage

Date: 2026-09-02 PDT. Bounded analytic follow-up, approximately five minutes. No AIDA implementation or existing project files were changed. Independent algebra check was performed by a second agent.

## Verdict

**A one-direction candidate-subspace exchange does not give a rank-$O(1)$ coefficient-matrix update in general.** Even after eliminating the old-column variables and passing to the actual $\alpha$-local Hom spaces, the update can have rank $\Theta(\dim X_{b,\alpha})$. An explicit minimal presentation with an indecomposable target block attains this bound. The useful replacement parameter is an **evaluation rank**, not the rank of the changed candidate matrix.

The result is a first analytic obstruction, not an impossibility theorem for all quantum walks or an implementation benchmark.

## Source equations actually checked

Primary source: [Dey, Jendrysiak and Kerber, SoCG 2025, sections 3–6](https://drops.dagstuhl.de/storage/00lipics/lipics-vol332-socg2025/html/LIPIcs.SoCG.2025.41/LIPIcs.SoCG.2025.41.html).

Their BlockReduce equations are

$$Q_cM_c+M_bP_c=0\quad(c\ne b),\tag{*}$$
$$N_b+\sum_{c\ne b}Q_cN_c+M_bU=0.\tag{**}$$

The Hom variant caches a basis solving $(*)$ and repeatedly solves $(**)$ in that basis. Column sweeps eliminate the old-relation image; $\operatorname{Hom}^{\alpha}$ discards maps zero at $\alpha$. Candidate enumeration uses subspaces of $\mathbb F_q^k$, not all bases redundantly; automorphism-invariant decomposition further uses $\alpha$-Hom strongly connected components and a smaller extension parameter $\kappa$. These are existing classical reductions, not new proposed quantum preprocessing.

The dimensions below use $P_c\in\mathbb F_q^{r_b\times r_c}$, as required by the products. The displayed general-version input in the HTML appears to have a dimension typo for $P_c$; the preceding operation definition and the Hom definition give the compatible dimensions.

## Precise local update lemma

### Status

**PROVABLE AS STATED.** The stronger rank-$O(1)$ claim is false without an extra bounded-evaluation-rank hypothesis.

### Assumptions and notation

Fix one block-reduction test and keep $M_{\mathcal B}$, grading, and the cached Hom basis unchanged. Let $g_b$ be the number of target-block generators. Write $Q_1,\ldots,Q_h$ for all relevant cached row-map components, with the corresponding source matrices denoted $N_{c(i)}$. Let $T\in\mathbb F_q^{k\times\ell}$ be a full-rank candidate basis. Its coefficients in the reduction system are scalars $\lambda_i$; the old-column variable $U$ is a matrix with $\ell$ columns.

Assume the best-case aligned exchange

$$T'=T+u e_j^\top.$$

This is stronger than merely saying the subspaces meet in dimension $\ell-1$: their represented bases must be aligned. The lower bound below therefore survives even a favorable basis representation.

### Proof and exact rank formula

1. Under column-wise vectorization, the coefficient matrix for $(**)$ after substituting the Hom basis is

$$C_b(T)=\left[\operatorname{vec}(Q_1N_{c(1)}T)\ \cdots\ \operatorname{vec}(Q_hN_{c(h)}T)\ \middle|\ I_\ell\otimes M_b\right].$$

2. Put

$$V_b(u)=\left[Q_1N_{c(1)}u\ \cdots\ Q_hN_{c(h)}u\right].$$

Since $\operatorname{vec}(ze_j^\top)=e_j\otimes z$,

$$C_b(T')-C_b(T)=\left[(e_j\otimes I_{g_b})V_b(u)\mid0\right].$$

The left factor is injective, so

$$\boxed{\operatorname{rank}\Delta C_b=\operatorname{rank}V_b(u)\le\min(g_b,h).}$$

3. Let $L_b$ be the quotient map by the old relation image at $\alpha$. Eliminating $U$ and using $\alpha$-local maps gives instead

$$\boxed{\operatorname{rank}\Delta\overline C_b
=\operatorname{rank}\left[L_bQ_iN_{c(i)}u\right]_i.}$$

This is the dimension of the span of the Hom-evaluation images of the changed relation direction, bounded above by $\dim X_{b,\alpha}$, not by one. Appending the changing right-hand side adds at most one to this rank; the example below has an unchanged right-hand side. $\square$

### Kronecker warning before Hom reduction

For unrestricted $Q_c$, the map $Q_c\mapsto Q_cN_cT$ has coefficient $(N_cT)^\top\otimes I_{g_b}$. If $N_cu\ne0$, the update rank is exactly $g_b$ because

$$\operatorname{rank}\left((e_j(N_cu)^\top)\otimes I_{g_b}\right)=g_b.$$

Likewise $AX=XB$, with $X\in\mathbb F_q^{m\times n}$, has coefficient $I_n\otimes A-B^\top\otimes I_m$. A nonzero rank-one change $B'=B+uv^\top$ changes this coefficient by $-(vu^\top)\otimes I_m$, of rank exactly $m$. Rank-one data changes and rank-one linearized-system changes are different statements.

## Sharpness with a valid indecomposable target block

For any $t\ge1$, work over any finite field and use two grading parameters. Let $b$ have $t+1$ generators born at pairwise incomparable grades

$$\beta_i=(i,t+2-i),\quad i=1,\ldots,t+1,$$

and one old relation with all coefficients equal to one at $\gamma=(t+2,t+2)$. Let $c$ be a free rank-one block born at $\delta=(t+3,t+3)$, and let the new relation degree be $\alpha=(t+4,t+4)$.

**Indecomposability.** Admissible degree-zero maps on the generators of $b$ are diagonal because their grades are incomparable. Preserving the one-dimensional all-ones relation subspace forces all diagonal entries to agree. Thus $\operatorname{End}(b)=\mathbb F_q$, and $b$ is indecomposable.

At $\delta$ and $\alpha$, the fibre $b$ has dimension $t$. Maps from the free block $c$ to $b$ can send its generator to any element of $b_\delta$, so $\operatorname{Hom}^{\alpha}(c,b)$ evaluates surjectively onto $b_\alpha$.

Choose two new columns with

$$N_b=(e_1,0),\qquad N_c=(0,1),\qquad T=e_1,\qquad T'=e_1+e_2.$$

The new relation columns modulo old relations are $([e_1],0)$ and $(0,1)$, hence independent. All generator grades are strictly below $\alpha$, so the presentation is minimal. Both candidate bases have rank one. Their difference has rank one, with $u=e_2$, and $N_bu=0$, so the right-hand side does not change. But $N_cu=1$, and the evaluated $\alpha$-Hom basis spans all of $b_\alpha$. Therefore

$$\boxed{\operatorname{rank}\Delta\overline C_b=t.}$$

This is a counterexample inside the graded/minimal/indecomposable setting, not just an unrestricted-matrix example.

## What an $\alpha$-local endomorphism/idempotent alternative must do

A decomposition corresponds to orthogonal idempotents in the **actual module endomorphism algebra**. For a final presentation $D$, compute the graded chain-map equations $QD=DP$ and quotient out maps inducing zero on the module. Their solution space is linear; the additional idempotency condition is quadratic. An arbitrary invariant subspace of the fibre $X_\alpha$ is not automatically a module direct summand.

Evaluation gives an algebra map $\operatorname{End}(X)\to\operatorname{End}(X_\alpha)$. Its image is a compressed algebra, not generally the full matrix algebra. Any approach through this image must retain its multiplication and lifting information, and separately recover summands invisible at $\alpha$. For instance, the projection onto a summand with zero $\alpha$-fibre is a nonzero idempotent in the evaluation kernel, so that kernel need not be nilpotent. This is not a claim that idempotents fail to lift in finite-dimensional algebras; Artinian rings have idempotent-lifting theory. It is a warning against silently replacing the full decomposition problem by unconstrained fibre idempotents or assuming the evaluation kernel is the Jacobson radical.

The polynomial-algebra baseline already exists: [Chistov, Ivanyos and Karpinski, ISSAC 1997](https://doi.org/10.1145/258726.258751), with [author-hosted paper](https://theory.cs.uni-bonn.de/marek/publications/85169-cs.pdf), gives polynomial-time module-decomposition algorithms over finite fields. Therefore a square-root reduction of AIDA's exhaustive candidate count is not an exponential improvement over the best theoretical classical algorithm. A new result needs an explicit sparse/presentation-sensitive cost regime, including conversion and algebra-construction costs, in which it improves the relevant classical bound.

## Narrow next gate

Define $r_{\rm eval}$ as the largest rank of the evaluated map $V_b(u)$ after the $\alpha$ quotient along the proposed walk. A legitimate low-rank-update theorem can assume or prove $r_{\rm eval}\le r$ and charge update cost as a function of $r$. It cannot substitute $\operatorname{rank}(T'-T)=1$ for this condition.

For interval targets the fibre dimension is at most one, but ordinary Gaussian reduction is already an AIDA baseline there. Seek a non-interval class with provably small evaluation rank and a classical dynamic-solver comparison. If no such class exists in the intended inputs, stop the constant-update quantum-walk claim. Also account for changes in cached Hom spaces after block merges: the fixed-system identity above does not control those changes.

No code experiment was needed: the update factorization and the arbitrary-$t$ example are exact over every finite field. This short triage does not audit the full AIDA proof or establish quantum-walk setup, checking, update, marked-fraction, spectral-gap, or coherent-data costs.
