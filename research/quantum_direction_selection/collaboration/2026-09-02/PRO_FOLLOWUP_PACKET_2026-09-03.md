# Focused Pro follow-up packet — September 3, 2026

This is a frozen concatenation of the new proof/certificate material for the existing TDA conversation. The accompanying submission message records the exact Git snapshot and this packet SHA-256. It supersedes older parameter choices and the old two-bidegree enumeration; it does not modify the prior a46f408 packet. Complete guarded-palette integration and priority remain open.

Read the request, finite-certificate theorem, intermediate proof, and certificate narrative first. Full graph/certificate data and the source-replay checker follow. All included file bodies are verbatim.

## Frozen included-file manifest

```json
[
  {
    "path_relative_to_collaboration_directory": "PRO_FOLLOWUP_REQUEST_2026-09-03.md",
    "bytes": 6457,
    "sha256": "b7437e4fefa711e8ef5bb4edbb11d59dd92f94a84853577df780afed120904f2"
  },
  {
    "path_relative_to_collaboration_directory": "FINITE_CERTIFICATE_CONCENTRATION.md",
    "bytes": 11147,
    "sha256": "b6c910bdb2cfb2ccecca6b82892bb811575aa33567a29fa396eb0c8180c6020b"
  },
  {
    "path_relative_to_collaboration_directory": "EXACT_FILLING_COERCIVITY.md",
    "bytes": 13733,
    "sha256": "d9037fdd84e2c8582b92e0541be6c0f5fd8d1cfe7483e2a182927a9ba9e866c8"
  },
  {
    "path_relative_to_collaboration_directory": "REPRESENTATIVE_GADGET_CERTIFICATE.md",
    "bytes": 8691,
    "sha256": "5c937ee054bf21b840d8ec78fc10fcbf9ae0291106be9d9d483f2f8e0c79fd46"
  },
  {
    "path_relative_to_collaboration_directory": "RUDOLPH_REPRESENTATIVE_BULK_CERTIFICATE.json",
    "bytes": 105288,
    "sha256": "916819fb8a9e371b322a1fab1161b1fc2686ad7fdaf9cf785f52fc2fcb0cae3a"
  },
  {
    "path_relative_to_collaboration_directory": "certify_representative_bulk.py",
    "bytes": 19462,
    "sha256": "dbc7e03bfc2d9d6884c318d759af26dd5f706cd1974e4f018aee66af0c56c551"
  },
  {
    "path_relative_to_collaboration_directory": "PRO_REVIEW_DISPOSITION_2026-09-03.md",
    "bytes": 9449,
    "sha256": "3a6207b9bd2b0fcba25da802678ab63718a72dc31d7785e3ebac8161da62e39e"
  },
  {
    "path_relative_to_collaboration_directory": "SOURCE_LEDGER.md",
    "bytes": 8195,
    "sha256": "137b57a0f133e96ba15ce77f26e48d8b962d455e79ea2a33d4fdcea563eb22a1"
  },
  {
    "path_relative_to_collaboration_directory": "../../round2/UNARY_PALETTE_ADDENDUM.md",
    "bytes": 14654,
    "sha256": "3583f697747ec81793d15130803c7e50fe9586a23c8bec7c9dc4b30ec28947e1"
  }
]
```


<!-- BEGIN INCLUDED FILE: PRO_FOLLOWUP_REQUEST_2026-09-03.md -->

# Included file 1: PRO_FOLLOWUP_REQUEST_2026-09-03.md

# Focused Pro follow-up: attack the stronger proof and finish the finite palette

Prepared September 3, 2026. Destination: the existing **Audit Quantum Persistence Corollary** conversation, Chat / Pro 5/5. This is a continuation of the user's authorized review-and-advance task, not a new unrelated topic.

We collected your full answer to snapshot a46f408 and independently dispositioned it. There is substantial new work, including an actual exact certificate. The supplied follow-up packet is governing for this round; the old packet remains a historical snapshot.

## Deliverables, in order

1. **Hostile proof audit.** Check FINITE_CERTIFICATE_CONCENTRATION.md line by line, then the intermediate EXACT_FILLING_COERCIVITY.md. The proposed stronger all-chain inequality is
   \[
   \|(I-P_K)x\|^2\le C[t\lambda^2+e/(g\lambda^\kappa)].
   \]
   Lambda can be chosen independently of g. For m<=6 and lambda=Theta(eta/t), the stated lower-bound scales are weighted Omega(eta^28 g/t^26), and, under the separate common-copy theorem, unweighted Omega(eta^26 g/t^24). Either provide a concrete counterexample satisfying the exact hypotheses, identify and repair the first invalid inference, or give a rigorous checked proof. Do not substitute a counterexample that violates exact filling, the projected bulk condition, independent interiors, or the zero-weight kernel identity.

2. **Resolve the smallest remaining substantive gate.** The packet includes the actual graph and checker for Rudolph's state_00m10m11, source commit 30ac70e5dacdecce97c38d801c128ec3ed93a96a. Independently inspect/reproduce what you can. Prove that every needed basis, one-/two-term active state, and the three-term pair satisfies the finite criterion, using graph symmetries where exact. Then prove closure for computational-basis guards via the joined implementing sphere and attaching map, or produce exact finite certificates for the remaining family through total locality six. A join of already filled complexes is not the intended guard construction. If closure fails, exhibit the explicit first obstruction and the smallest corrected criterion.

3. **Push the surviving theorem further.** Once the audit is settled, seek an actual stronger theorem: improved structural dependence on term count/interface overlap, a complete finite-certificate realization theorem, or a defensible computational consequence for the explicit perfect-eigenspace-separated source. State and prove the strongest useful result you can obtain, with sharp scope. Do not stop at a list of proposed future tasks.

4. **Assess collision and value against primary sources.** In particular, is exact filling plus the finite zero-weight argument already explicit or an immediate known lemma? Search for the strongest collision and cite exact theorem/lemma/page locations and accessible source links. Distinguish a primary statement you opened from inference, supplied-ledger repetition, and a failed search. If the main result is an obvious corollary or too weak for a strong TCS paper, give a concrete stop/narrow decision and develop the strongest surviving direction using this work.

## Specific audit points

- For each local binary-weight boundary,
  \(\partial_{w,k}=W_{k-1}^{-1}\partial_{1,k}W_k\).
  We use nonzero singular-value scaling, Hodge decomposition and fixed dimension to obtain the lower bound c lambda^(2d_a+4). No optimal valuation or leading coefficient is required.
- The finite criterion is ker D_0=V_a direct-sum Q_a, T=lambda T_1, T_1 V_a=0, and injectivity on Q_a. The actual graph has rank D_0=902 in a 1082-dimensional target space, with a known kernel of dimension 180=4+176.
- The central link Gram has size 176 and determinant 797443 modulo the prime 1000003. Exact boundary ranks are 40,282,632,447,30; an archived 382-term integer chain fills ket00-ket10-ket11; three independent register cosets survive.
- The actual graph has degree-5 simplices although the logical target degree is 3. The old assertion that only two bidegrees occur is false. The new proof handles every bidegree and uses the outside gap outside the unique outside-harmonic degree. Check this carefully.
- Shared-register L_i have orthogonal inputs and shared outputs. Retain private mass U in the interference remainder chi lambda^2 U, then absorb using chi=O(t^2). The projected T_i outputs retain gadget-private vertices and are orthogonal across gadgets; these are different maps.
- Exact filling gives Delta_i^up>=delta_i Pi_i by Hodge subspace order. Sum before using the logical gap; do not divide all geometric leakage by g.
- The zero-weight route avoids approximate harmonic-projector estimates entirely until after min-max. Initial and final H are logical; Delta is the full geometric Laplacian.

## Corrections to your previous response

The aggregate lifted-sector bound was already written in the old packet; the loose final t factor also came from a termwise bulk bound. Your generic projector-error example does not rule out the stronger differential-based argument. In the angle formula a=sqrt(1-eta_A^2)sqrt(1-eta_B^2)-eta_A eta_B, use max(0,a)^2 unless a>=0; the packet contains an explicit counterexample to squaring a negative bound. We accept the two-projector sharpening g2>=1/(27L^3), with g chosen as the certified first-gap floor.

Mémoli–Wan–Wang's Theorem 5.1 proof already contains ordinary-to-persistent Laplacian domination. The earlier inequality's novelty emphasis is retracted. A preparation budget must include eta between logical-history and actual harmonic mixtures. D=1 gives only a conditional perfect-completeness, normalization-degenerate hardness consequence. No unrestricted SDQC1/BQP inference is authorized.

Your visible source panel exposed only the packet, a pasted document, and its GitHub copy; it did not give independent paper-reading receipts. Please provide actual source locations and distinguish new verification explicitly.

## Output requested

Give a concise verdict first, then a claim-status table, the full strongest surviving theorem/proof, finite-certificate or closure evidence, counterexamples/negative results, and a precise remaining gate. Preserve intermediate lemmas and failed approaches that change the research decision. Do not certify a complete reduction or paper readiness merely because the abstract inequalities pass. Target a substantial, impactful theoretical computer science paper through concrete mathematics.


<!-- END INCLUDED FILE: PRO_FOLLOWUP_REQUEST_2026-09-03.md -->


<!-- BEGIN INCLUDED FILE: FINITE_CERTIFICATE_CONCENTRATION.md -->

# Included file 2: FINITE_CERTIFICATE_CONCENTRATION.md

# All-chain concentration from finite zero-weight certificates

2026-09-03. **INDEPENDENT LOCAL DERIVATION; COMPLETE PALETTE NOT YET CERTIFIED.** This sharpens and simplifies [the spectral-sector derivation](EXACT_FILLING_COERCIVITY.md). One actual source representative passes every finite check below; closure for the complete guarded circuit palette is a separate open gate. No optimal spectral valuation or priority is asserted.

The candidate result is
\[
\boxed{\|(I-P_K)x\|^2\le C\left(t\lambda^2+
\frac{\langle x,\Delta x\rangle}{g\lambda^\kappa}\right)}.
\tag{A}
\]
Here H is the logical sum of projectors, P_K projects onto its embedded kernel, and Delta is the full geometric Laplacian. This is an estimate for every normalized geometric chain. The positive logical gap g does not enter the choice of gadget weight.

## 1. Exact finite local data

An active gadget has a weight-one register R_a of top degree d_a, a finite set of new vertices of weight lambda, and its full clique complex Y_a. Work in the canonical Euclidean coordinates for normalized chains, so its degree-d_a differential pair is
\[
D_a(\lambda)=
\begin{bmatrix}\partial_{d_a}(\lambda)\\
\partial_{d_a+1}(\lambda)^*\end{bmatrix}
=D_{a,0}+\lambda D_{a,1}.
\]
The value at zero is a matrix limit; no invertible weight gauge at zero is assumed.

Let V_a=Z_{d_a}(R_a), with projector P_a. A certificate supplies a coordinate subspace Q_a supported on private simplices and an output projection R_a^{out}. Require:

1. **Exact topology at positive weight:** at lambda=1,
   \[
   B_{d_a}(Y_a)\cap V_a=\operatorname{ran}\Pi_a
   \]
   for the intended logical projector Pi_a.
2. **Zero-weight kernel:**
   \[
   \ker D_{a,0}=V_a\oplus Q_a.
   \]
   The summands are orthogonal.
3. **Projected private differential:** with T_a(lambda)=R_a^{out}D_a(lambda),
   \[
   T_a(\lambda)=\lambda T_{a,1},\quad T_{a,1}P_a=0,\quad
   \|T_{a,1}Q_a z\|\ge b\|Q_a z\|.
   \]
   All retained output simplices contain a private vertex of this gadget.

Every matrix is of fixed size. Thus the positive gap of D_{a,0}^*D_{a,0}, the norms of D_{a,1} and T_{a,1}, and b>0 have constants uniform over a finite certified palette. No spectral-projector convergence or identification of a lifted eigenvector is assumed.

For integer matrices these properties admit finite exact certificates: rank lower bounds modulo a prime, matching rational upper bounds from explicitly known kernels, exact filling chains, and nonzero determinants of Gram matrices. This establishes a theorem for the specified finite graphs, not for every integer-state gadget.

## 2. A local positive-gap lower bound without spectral valuation

For a positive vertex weight w, let W_k be the diagonal matrix of products of weights on degree-k simplices. In the stated coordinates,
\[
\partial_{w,k}=W_{k-1}^{-1}\partial_{1,k}W_k.
\]
For 0<lambda<=1 with weights in {1,lambda},
\[
\sigma_{\min}(W_{k-1}^{-1})\ge1,\qquad
\sigma_{\min}(W_k)\ge\lambda^{k+1}.
\]
The singular-value inequality for invertible left and right scalings, at the fixed nonzero rank of the boundary, gives
\[
\sigma_{\min}^+(\partial_{w,k})\ge
\lambda^{k+1}\sigma_{\min}^+(\partial_{1,k}).
\]
Zero-rank boundary blocks can be omitted. The Hodge decomposition gives
\[
\gamma_+(\Delta_{a,d_a}(\lambda))
\ge c_a\lambda^{2d_a+4}.
\tag{B}
\]
For a finite palette with d_a=2m_a-1 and m_a<=m, take
\(\kappa=4m+2\) and a common c_a>=c>0. This is a lower bound, not a claim of equality, optimal order, or a leading coefficient.

One explicit constant is available directly from the unweighted integer Laplacian: if its rank is r>0 and its operator norm is at most an integer B>=1, the product of its nonzero eigenvalues is a nonzero integer coefficient of its characteristic polynomial. Thus
\[
\gamma_+(\Delta_a(1))\ge B^{-(r-1)}.
\]
The weight gauge also preserves the exact boundary intersection with V_a, because every register simplex has weight one.

## 3. Padding and independent attachment hypotheses

Pad an active gadget by joining with the unused register. Use reduced chain complexes for joins, including degree -1. The outside register has reduced homology only in its top degree q, and has a positive gap bounded below by a constant on all other modes. The join Laplacian is
\[
\Delta_{Y_a*R_{out}}=\Delta_{Y_a}\otimes I+
I\otimes\Delta_{R_{out}}
\]
on the direct sum of the appropriate bidegrees.

At the global target degree d=d_a+q+1, the only **outside-harmonic** bidegree is (d_a,q). Other bidegrees can and do occur; they have a positive outside gap. It follows that the padded zero-weight kernel is precisely
\[
V\oplus(Q_a\otimes\mathcal H_{out}),
\]
with a uniform positive gap on its complement. The local derivative norms remain uniform because only the fixed active gadget has lambda-dependent entries. Pad the private output projection with the outside harmonic projector; outside differential terms vanish on both sides. Conditions 1--3 and (B) then persist with constants independent of the outside register dimension. The padded exact filling statement follows from the join homology tensor decomposition. In particular, outside padding is different from building a product guard into a new active attaching sphere; the latter still needs a separate finite-family or closure argument.

Attach t>=1 padded gadgets along a common register R of top dimension d. Interiors are independent: there is no simplex using private vertices from different gadgets. Common weights and coordinate embeddings are used throughout. Write
\[
C_d(X)=C_R\oplus\bigoplus_i C_i^{priv},\qquad
x=\omega_0+\sum_i\omega_i,\quad x_i=\omega_0+\omega_i.
\]
For the register-output interface L_i, assume or verify
\[
L_iL_i^*\preceq N_*\lambda^2 I.
\tag{C}
\]
This follows for a fixed vertex palette by expressing removal of each possible private vertex as a signed coordinate partial isometry; only a fixed number of such removals can land entirely in the register. Its constant therefore does not grow with the outside register. Inputs of different L_i are orthogonal; their register outputs are shared.

Let P be the projector onto V=Z_d(R), H=sum_i Pi_i on V, and
\[
H\succeq g(P-P_K),\qquad 0<g\le1.
\]
The logical rank-one active constraints can have higher rank after outside padding.

## 4. Global interface energy

For a normalized x put e=||D_X x||^2, U=sum_i||omega_i||^2, and
\[
\rho=\lambda^{-2}\|[L_1\ \cdots\ L_t]\|^2\le N_*t,\qquad
\chi=(t-2)_+\rho+N_*\le C t^2.
\]
Set a=partial_R omega_0, y_i=L_i omega_i, y=sum_i y_i, and r=a+y. The exact identity
\[
\sum_i\|y-y_i\|^2=(t-2)\|y\|^2+\sum_i\|y_i\|^2
\le\chi\lambda^2 U
\]
also covers t=1. All non-register down outputs split by gadget, as do all up columns. Hence
\[
\sum_i\|D_i(\lambda)x_i\|^2
\le 2t e+2\chi\lambda^2 U.
\tag{D}
\]
The factor U is retained; replacing it by one loses the useful absorption step.

## 5. Leakage from finite zero-weight data

In each padded chain space let A_{i,0}=I-P-Q_i. The certified zero-weight gap and D_i(lambda)=D_{i,0}+lambda D_{i,1} yield
\[
\begin{aligned}
S_A:=\sum_i\|A_{i,0}x_i\|^2
&\le C\sum_i\|D_{i,0}x_i\|^2\\
&\le C\left(te+\chi\lambda^2 U+
\lambda^2\sum_i\|x_i\|^2\right)\\
&\le C(te+\chi\lambda^2 U+t\lambda^2).
\end{aligned}
\tag{E}
\]
Here sum_i||x_i||^2=1+(t-1)||omega_0||^2<=t.

Since T_iP=0,
\[
T_iQ_i x_i=T_i x_i-T_iA_{i,0}x_i.
\]
Bulk injectivity, ||T_i||<=C lambda, and orthogonal retained private output blocks imply
\[
S_Q:=\sum_i\|Q_i x_i\|^2
\le C\left(\frac{\sum_i\|T_i x_i\|^2}{\lambda^2}+S_A\right)
\le C(e/\lambda^2+S_A).
\tag{F}
\]
This output orthogonality concerns T_i; no such assumption is made for L_i.

Put N=||(I-P)x||^2. Orthogonality of V, Q_i and A_{i,0} gives
\[
N\le U+t\|(I-P)\omega_0\|^2=S_A+S_Q.
\]
Substituting (E)--(F), using U<=N, and choosing chi lambda^2 below a fixed palette constant gives
\[
\boxed{N\le C[t\lambda^2+(t+\lambda^{-2})e]}.
\tag{G}
\]
The sufficient choice lambda<=c/t is independent of the logical gap g. No estimate against Delta's unknown kernel entered this proof.

## 6. Logical coercivity and exact multiplicity

Exact filling and (B), applied on the local boundary subspace, imply the elementary operator inequality
\[
\Delta_i^\uparrow\succeq c\lambda^\kappa\Pi_i.
\]
Because R has no degree-(d+1) simplex, up columns partition exactly by gadget:
\[
\Delta^\uparrow=\sum_i\iota_i\Delta_i^\uparrow\iota_i^*
\succeq c\lambda^\kappa H^{emb}.
\tag{H}
\]
Split distance into geometric leakage and forbidden logical mass. Equations (G)--(H) give
\[
\begin{aligned}
\|(I-P_K)x\|^2
&=N+\langle x,(P-P_K)x\rangle\\
&\le C[t\lambda^2+(t+\lambda^{-2})e]
+\frac{e}{c g\lambda^\kappa}\\
&\le C[t\lambda^2+e/(g\lambda^\kappa)].
\end{aligned}
\]
The last step uses lambda<=c/t, kappa>=2, g<=1. This proves (A).

Choose
\[
\lambda\le c\min(t^{-1},\eta/\sqrt t),\qquad
E\le c'\eta^2g\lambda^\kappa,\qquad 0<\eta<1.
\]
Every normalized vector in the geometric spectral subspace below E has nonzero projection into ker H. Its dimension is therefore at most dim ker H. Exact local filling plus independent interior chains gives
\[
B_d(X)\cap V=\sum_i\operatorname{ran}\Pi_i,
\]
so V/sum_i ran Pi_i injects into H_d(X) and supplies at least dim ker H exact zeros. Consequently,
\[
\dim\ker\Delta=\dim\ker H,\quad
\operatorname{spec}(\Delta)\cap(0,E)=\varnothing,\quad
\|P_{\ker\Delta}-P_K\|\le\eta.
\]
The zero-dimensional logical kernel is included. There is no added global relative-acyclicity assumption.

For nested term sets, compatible quotient maps are surjective; their homology realizations have persistent rank equal to the later logical kernel dimension. An initial history kernel of known dimension D>0 therefore gives the true normalized fraction dim ker H_final/D.

A conservative dyadic lambda=Theta(eta/t) gives, for kappa=26,
\[
E=\Omega(\eta^{28}g/t^{26}).
\]
Under the separately imported common-copy unweighting theorem, F=lambda^{-2} gives a geometric floor min(FE,1), hence an attainable scale
\[
FE=\Omega(\eta^{26}g/t^{24}).
\]
These poor polynomial lower bounds are not practical runtime predictions.

## 7. What has and has not passed

[The actual Rudolph representative certificate](REPRESENTATIVE_GADGET_CERTIFICATE.md) verifies the active data for the projector onto |00>-|10>-|11>. Its source graph has 41 vertices, 322 edges, target degree 3, Betti number 3, zero-weight kernel dimension 180=4+176, and an injective projected central pair.

This is a complete check of the finite inputs needed by this route for that one graph, conditional on the documented graph replay matching the pinned source. The replay, integer matrices, modular arguments and full filling chain are archived. The earlier spectral-sector theorem remains an independent route with stronger imported hypotheses.

Outstanding: every other required active atom, closure under guarded attaching-sphere products through locality six, complete source/priority assessment, and the strongest meaningful exact source-complexity consequence. The current theorem is conditional on the finite family satisfying the listed data. It is not a certification of the full circuit reduction or submission readiness.


<!-- END INCLUDED FILE: FINITE_CERTIFICATE_CONCENTRATION.md -->


<!-- BEGIN INCLUDED FILE: EXACT_FILLING_COERCIVITY.md -->

# Included file 3: EXACT_FILLING_COERCIVITY.md

# Exact filling gives direct logical coercivity

2026-09-03. **LOCAL DERIVATION, CONDITIONAL ON THE EXPLICIT LOCAL PACKAGE BELOW.** This is a new continuation after collecting [the Pro response](PRO_REVIEW_2026-09-03.md). Its abstract proof has been checked locally; the complete supported clique-gadget palette and priority have not been certified. This note is the proposed object of the next focused Pro review.

The strongest improvement here is linear dependence on the promised logical gap. The gadget weight can be chosen without multiplying it by that gap. A second refinement controls mass outside the register by a quadratic, rather than linear, perturbation term. Neither statement identifies geometric harmonic vectors literally with logical ones.

## 1. Setting and exact local inputs

Let R be a register complex of top dimension d, V=Z_d(R), and P its orthogonal projector. Register vertices have weight one. For t>=1, attach gadgets Y_i with disjoint new vertices and no simplex containing new vertices from different gadgets. In normalized chain coordinates,
\[
C_d(X)=C_R\oplus\bigoplus_{i=1}^t C_i^{\rm priv},\qquad C_R=C_d(R).
\]
For x=omega_0+sum_i omega_i write x_i=omega_0+omega_i and let iota_i embed the corresponding single-gadget chain space into C_d(X).

Each logical constraint Pi_i is an orthogonal projector supported on V. Set H=sum_i Pi_i, let P_K project onto ker H inside V, and assume
\[
H\succeq g(P-P_K),\qquad 0<g\le1.
\]
H is logical; Delta is geometric. All constants below depend only on a fixed finite palette. There exist 0<lambda_0<=1 and c_0,C_0>0, with fixed kappa>=2, such that, for 0<lambda<=lambda_0:

1. Exact filling holds: ran Pi_i is contained in B_d(Y_i). For the quotient conclusion use equality B_d(Y_i) intersect V = ran Pi_i. Let K_i be the full single-gadget harmonic projector. Thus K_i Pi_i=0 exactly.
2. The local whole positive gap obeys Delta_i >= c_0 lambda^kappa (I-K_i), and
   \[
   \|K_i-(P-\Pi_i)\|\le C_0\lambda.
   \]
   This is an operator-norm bound after padding, obtained in fixed local dimension before tensoring.
3. There is an orthogonal spectral decomposition I=K_i+F_i+B_i+A_i, with A_i the high sector, B_i the bulk sector, and F_i the lifted constraint sector. Assume
   \[
   \Delta_i\succeq c_0 A_i,\qquad
   \Delta_i^\uparrow\succeq c_0\lambda^\kappa F_i.
   \]
4. For the corrected local-bulk tensor outside-harmonics projector Q_i and the projected differential pair T_i,
   \[
   \|B_i-Q_i\|\le C_0\lambda,\quad
   \|T_i\|\le C_0\lambda,\quad
   \|T_iQ_i z\|\ge c_0\lambda\|Q_i z\|.
   \]
   T_i is a projection of the actual boundary/coboundary pair, so T_iK_i=0. Its output retains a new vertex of gadget i. Consequently
   \[
   \sum_i\|T_i x_i\|^2\le
   e:=\langle x,\Delta x\rangle.
   \]
   This output orthogonality concerns T_i, not the register-output interface.
5. The latter interface is L_i=Pi_reg^{d-1} partial Pi_i^{priv}, with
   \[
   L_iL_i^*\preceq N_*\lambda^2I,\qquad
   \rho=\lambda^{-2}\|[L_1\ \cdots\ L_t]\|^2\le N_*t.
   \]

The normalized chain basis, common weights, and embeddings must agree at every level. Exact filling may be deduced from the local nullity, kernel limit, and weight gauge as in the existing dossier; no global gap is used in that deduction.

## 2. Direct up-Laplacian domination

**Lemma.** If ran Pi_i is a subspace of the local boundary space and the local whole positive gap is at least delta_i, then
\[
\Delta_i^\uparrow\succeq\delta_i\Pi_i.
\]

**Proof.** The Hodge decomposition splits the local chain space orthogonally into boundaries, harmonics, and coboundaries. On boundaries, Delta_i^\uparrow equals Delta_i; on the other two summands Delta_i^\uparrow vanishes. Hence
\[
\Delta_i^\uparrow\succeq
\delta_i P_{B_d(Y_i)}
\succeq\delta_i\Pi_i.
\]
The second inequality uses exact subspace containment, not a perturbative comparison with a lifted eigenvector. No commutation between Pi_i and Delta_i is required. This is a standard PSD consequence of exact filling. ∎

Since R has no (d+1)-simplices and the interiors are independent, all global up-boundary columns are partitioned by gadget:
\[
\Delta^\uparrow=\sum_i\iota_i\Delta_i^\uparrow\iota_i^*.
\]
Taking delta_i>=c_0 lambda^kappa gives
\[
\boxed{\Delta^\uparrow\succeq c_0\lambda^\kappa H^{\rm emb}},
\qquad
\boxed{\langle x,H^{\rm emb}x\rangle\le e/(c_0\lambda^\kappa)}. \tag{1}
\]
There is no factor t in (1). Its filling hypothesis is essential: with Delta^\uparrow=diag(1,0) and Pi=diag(0,1), no positive multiple of Pi is dominated.

This observation already improves the logical-gap dependence if combined with the Pro aggregate concentration estimate. Dropping its nonnegative H term bounds leakage outside V; (1) then bounds the forbidden logical component separately. There is no reason to divide the entire structural remainder by g.

## 3. Keep the actual interior mass in the interface estimate

For normalized x define
\[
U=\sum_i\|\omega_i\|^2,\quad
S=\sum_i\|(I-K_i)x_i\|^2,\quad
\chi=(t-2)_+\rho+N_*\le C t^2.
\]
Let a=partial_R omega_0, y_i=L_i omega_i, and y=sum_i y_i. The global register boundary is r=a+y; all non-register boundary outputs are in disjoint blocks.

The identity
\[
\sum_i\|y-y_i\|^2=(t-2)\|y\|^2+\sum_i\|y_i\|^2
\]
and the block-row bounds imply
\[
\sum_i\|y-y_i\|^2\le\chi\lambda^2 U.
\]
Using a+y_i=r-(y-y_i) and additivity of up energy,
\[
\sum_i\langle x_i,\Delta_i x_i\rangle
\le2t e+2\chi\lambda^2 U.
\]
Therefore
\[
S_A:=\sum_i\|A_i x_i\|^2
\le C(te+\chi\lambda^2U). \tag{2}
\]
The factor U is retained. Replacing it by one prematurely creates an avoidable additive interface error.

## 4. Bulk estimate without an additive kernel-leakage term

For b in ran B_i,
\[
\|T_i b\|
\ge \|T_iQ_i b\|-\|T_i(I-Q_i)b\|
\ge c_0\lambda(1-C_0\lambda)\|b\|-C_0^2\lambda^2\|b\|.
\]
For a sufficiently small fixed lambda_0 this is at least c lambda ||b||.

Apply this to b=B_i x_i. Because T_iK_i=0 exactly,
\[
T_iB_ix_i=T_ix_i-T_iA_ix_i-T_iF_ix_i.
\]
The full norm bound on T_i suffices for the last two terms. Squaring, summing, and using disjoint projected outputs gives
\[
S_B:=\sum_i\|B_ix_i\|^2
\le C(e/\lambda^2+S_A+S_F). \tag{3}
\]
Here
\[
S_F:=\sum_i\|F_ix_i\|^2\le e/(c_0\lambda^\kappa) \tag{4}
\]
by summing the local up-Laplacian inequalities before taking expectation.

Unlike the earlier argument on Q_i x_i, (3) works directly on the bulk spectral component, which is orthogonal to the exact kernel. It does not need a separate estimate on T_i acting on approximate low vectors. Combining (2)--(4),
\[
\boxed{S\le C[(t+\lambda^{-\kappa})e+\chi\lambda^2 U]}. \tag{5}
\]

## 5. Quadratic leakage outside the register

The local limiting projector P-Pi_i has no private support. Thus
\[
\|\omega_i\|^2
\le2\|(I-K_i)x_i\|^2+2C_0^2\lambda^2\|x_i\|^2.
\]
Since sum_i ||x_i||^2=1+(t-1)||omega_0||^2<=t,
\[
U\le2S+2C_0^2t\lambda^2. \tag{6}
\]
For z=(I-P)omega_0, the same argument holds for every i. Averaging gives
\[
\|z\|^2\le2S/t+2C_0^2\lambda^2. \tag{7}
\]
Let N=||(I-P)x||^2=U+||z||^2. If chi lambda^2 is below a sufficiently small palette constant, substitute (6) into (5) and absorb its S term:
\[
S\le C[(t+\lambda^{-\kappa})e+\chi t\lambda^4].
\]
Equations (6)--(7), and chi lambda^2=O(1), then give
\[
\boxed{N\le C[t\lambda^2+(t+\lambda^{-\kappa})e]}. \tag{8}
\]

This does not assert that separate kernel-projector differences have norm O(lambda^2). Their norms can remain O(lambda). Squaring private leakage, retaining U, and absorbing interface feedback yield (8). The Pro shared-output example is consistent with (2), and the generic rotated-projector example does not refute this stronger use of the differential and filling hypotheses.

## 6. Concentration with linear logical-gap dependence

Split the distance to the embedded logical kernel into geometric leakage and forbidden logical mass:
\[
\begin{aligned}
\|(I-P_K)x\|^2
&=N+\langle x,(P-P_K)x\rangle\\
&\le N+g^{-1}\langle x,H^{\rm emb}x\rangle\\
&\le C[t\lambda^2+(t+\lambda^{-\kappa})e]+
e/(c_0g\lambda^\kappa).
\end{aligned}
\]
For lambda<=c/t, kappa>=2 and g<=1, the energy coefficient is bounded by C/(g lambda^kappa). Hence
\[
\boxed{\|(I-P_K)x\|^2\le C[t\lambda^2+e/(g\lambda^\kappa)]}. \tag{9}
\]
This is an all-chain statement. The geometric kernel dimension is not assumed.

Choose
\[
0<\lambda\le c\min\{t^{-1},\eta t^{-1/2}\},
\qquad
0<E\le c'\eta^2g\lambda^\kappa,\qquad 0<\eta<1.
\]
Small palette constants also enforce lambda<=lambda_0. Then every normalized x of energy below E is within eta of the embedded ker H. The weight bound has no g factor.

Exact filling and independent interiors inject V/sum_i ran Pi_i into H_d(X). Projection injectivity on the geometric spectral subspace below E supplies the reverse dimension bound. Consequently
\[
\dim\ker\Delta=\dim\ker H,\qquad
\operatorname{spec}(\Delta)\cap(0,E)=\varnothing,\qquad
\|P_{\ker\Delta}-P_K\|\le\eta.
\]
The conclusion includes ker H=0. Nested term sets with common weights give the same natural quotient maps and true normalized persistent rank as before. These final dimension deductions are standard.

## 7. Explicit conservative scaling

A convenient dyadic choice is lambda=Theta(eta/t), with the fixed proportionality constant small enough for Section 6. Then
\[
E=\Omega(\eta^{\kappa+2}g/t^\kappa).
\]
For kappa=26,
\[
\boxed{E=\Omega(\eta^{28}g/t^{26})}.
\]
For common-copy unweighting with F=lambda^{-2} an integer, the inherited gap floor is min{F E,1}, so the same conservative choice gives
\[
\boxed{F E=\Omega(\eta^{26}g/t^{24})}.
\]
At fixed eta the bounds are Omega(g/t^26) and Omega(g/t^24). With the certified history lower bound g=1/(27L^3), retain both L and t explicitly.

These are attainable lower-bound scales, not claims that the actual spectral gap equals them. The construction still has large polynomial exponents and no near-term practicality claim. The weight and common-copy count can now be chosen independently of g; precision for resolving the final spectrum still depends on g.

## 8. Other corrections retained from the Pro review

The sharp two-projection bound is valid with 0<g<=1 and 0<alpha<=1:
\[
\gamma(g,\alpha)=\frac{g+1-\sqrt{(g+1)^2-4g\alpha}}2
\ge \frac{g\alpha}{g+1}.
\]
In its history application, use the chosen certified g=1/(8L^2), not an upper bound on the unknown actual gap. Alpha=1/(3L) yields
\[
g_2\ge 1/[3L(8L^2+1)]\ge1/(27L^3).
\]

For the harmonic-angle formula
\[
a=\sqrt{1-\eta_A^2}\sqrt{1-\eta_B^2}-\eta_A\eta_B,
\]
the squared-overlap bound requires a>=0. In general replace it by a_+=max{0,a}. Equal errors eta<1/sqrt(2) suffice. Our reduction may simply choose eta<=1/10.

The final preparation budget must include the difference between the preparable logical-history mixture and the actual harmonic mixture: at most eta plus history-preparation error. The total error for the simple overlap estimator includes this term, the O(eta^2) rank/overlap bias, and projection/sampling error.

Restricted BQP1(G_2) hardness obtained at D=1 is a conditional, normalization-degenerate consequence; it does not settle the arbitrary-D source complexity or unrestricted SDQC1 equivalence.

## 9. Source checking performed in this continuation

The following are narrow primary-source checks, not a full spectral-sequence or palette reconstruction:

- [King--Kohler arXiv v2, Lemma 9.1 and Claim 10.4](https://arxiv.org/html/2311.17234v2): checked the stated local spectrum and exact global up-Laplacian sum. Their general perturbation definition still needs conversion in fixed dimension before padding.
- [Hayakawa arXiv v1, Lemma 5.4](https://arxiv.org/html/2608.02726v1#S5): checked that the explicit finite family is given an exact register quotient, using the cited earlier constructions and join closure.
- [Rudolph arXiv v2, Appendix D.1](https://arxiv.org/html/2411.02681v2#A4.SS1): checked the displayed down-gain/loss states, join construction, algebraic two-qubit checks and supplementary-code reference. The numerical higher-locality checks reported there are not newly reproduced certificates.

The direct PSD lemma is an elementary consequence of those abstract assumptions; (2)--(9) are the continuation's independent derivation. Priority for this combination has not been established. The existing packet already summed the lifted-sector bound without t in its padding section; its looser final energy remainder also came from the termwise bulk estimate. The Pro response should not be credited with introducing an aggregate step already present in that packet.

## 10. Further same-day progress and next concrete gate

The actual representative graph has now passed exact topology, filling, central-bulk and zero-weight kernel checks; see [REPRESENTATIVE_GADGET_CERTIFICATE.md](REPRESENTATIVE_GADGET_CERTIFICATE.md). It is separate from the 15 small illustrative fixtures. Complete guarded-palette closure remains open.

A simpler route is written in [FINITE_CERTIFICATE_CONCENTRATION.md](FINITE_CERTIFICATE_CONCENTRATION.md). It replaces local spectral-projector convergence and sector assumptions by a finite zero-weight kernel identity and the projected bulk certificate. Elementary boundary-matrix scaling supplies a sufficient whole-positive-gap floor, without computing an optimal spectral valuation. It reaches (9) with fewer local inputs and a stronger geometric leakage bound. The present derivation is retained as a separate intermediate milestone.

The next focused Pro review should attack both routes under their exact hypotheses, then resolve the guarded attaching-sphere closure or identify the first finite obstruction. Do not upgrade either note to an unconditional full reduction merely because the abstract inequalities survive another review.

<!-- END INCLUDED FILE: EXACT_FILLING_COERCIVITY.md -->


<!-- BEGIN INCLUDED FILE: REPRESENTATIVE_GADGET_CERTIFICATE.md -->

# Included file 4: REPRESENTATIVE_GADGET_CERTIFICATE.md

# Exact certificate for one Rudolph three-term gadget

2026-09-03. **ONE SOURCE GRAPH CERTIFIED; COMPLETE PALETTE OPEN.** The integer calculations below establish the finite inputs of [the zero-weight concentration theorem](FINITE_CERTIFICATE_CONCENTRATION.md) for one actual active gadget. They do not certify all guarded products or the full circuit reduction.

## Provenance and reproduction boundary

The primary code is [Dorian Rudolph, QMA1-gateset-paper, gadget_homology.py](https://github.com/DorianRudolph/QMA1-gateset-paper/blob/30ac70e5dacdecce97c38d801c128ec3ed93a96a/gadget_homology.py), immutable commit
\[
\texttt{30ac70e5dacdecce97c38d801c128ec3ed93a96a}.
\]
The fetched file SHA-256 is
\[
\texttt{c8918f9e037ae79796bb65640170c8e60f31883625d24348f3476f7644dcd29a}.
\]
The upstream license is GPLv2-or-later; its graph construction and original algebraic checks are credited to that source.

[Our checker](certify_representative_bulk.py) fetches the pinned source, checks its hash, and evaluates only the inspected graph-building definitions make_graph, thicken, fill_cycle, join_keep_names, and state_00m10m11. A simple undirected Graph shim implements the called operations. It captures the finished graph at the first clique_complex call, before Sage homology, plotting, or top-level upstream routines execute. Sage was not run. The upstream program is not copied into this repository.

Graph construction itself therefore remains tied to this explicit replay rather than an independent run of Sage. The replayed operations have been compared with the inspected source: sorted undirected edges, thickened layers, specified attaching-map merges, and central coning. After capture, clique enumeration, oriented boundaries, ranks and fillings are independently computed. The complete graph and certificate data are in [RUDOLPH_REPRESENTATIVE_BULK_CERTIFICATE.json](RUDOLPH_REPRESENTATIVE_BULK_CERTIFICATE.json).

Reproduce with Python, NumPy and a configured GitHub CLI:

    python research/quantum_direction_selection/collaboration/2026-09-02/certify_representative_bulk.py

The output certificate includes the graph, orientation/order conventions, prime, integer filling chain, and matrix hash. It does not require trusting a floating-point eigenvalue threshold.

## 1. Exact topology and intended logical projector

The source function encodes
\[
\phi=|00\rangle-|10\rangle-|11\rangle.
\]
Its sign is opposite to the requested representative a=|10>+|11>-|00>, hence the same rank-one projector. Four register cycles are tensor joins of oriented four-edge bowtie petals. They have disjoint edge-simplex support and norm 4; division by 4 gives the explicit isometric logical basis.

| Quantity | Exact result |
| --- | --- |
| Vertices / edges | 41 / 322 |
| Numbers of simplices, degrees 0 through 5 | 41, 322, 914, 1082, 477, 30 |
| Boundary ranks, degrees 1 through 5 | 40, 282, 632, 447, 30 |
| Ordinary rational Betti numbers, degrees 0 through 5 | 1, 0, 0, 3, 0, 0 |
| Target degree | 3 |
| Nonzero terms in an integer filling of phi | 382 |
| Filling denominator | 1 |

The boundary compositions are checked as exact integer zero matrices. Gaussian elimination modulo p=1,000,003 supplies lower bounds on rational ranks. Adjacent chain dimensions and these adjacent lower bounds supply upper bounds:
\[
\operatorname{rank}_{\mathbb Q}\partial_k
\le\min\{n_{k-1}-\operatorname{rank}_{\mathbb F_p}\partial_{k-1},
         n_k-\operatorname{rank}_{\mathbb F_p}\partial_{k+1}\}.
\]
Every recorded lower and upper bound agrees. This proves the ranks over Q; modular rank alone would not give equality.

An integer chain c in C_4, with all 382 nonzero coefficients archived, satisfies
\[
\partial_4 c=\phi
\]
by an exact integer multiplication. The register cycles
\[
|00\rangle+|11\rangle,\quad |10\rangle-|11\rangle,\quad |01\rangle
\]
increase the boundary rank by three modulo p. Since the boundary rank over Q has already been certified, their cosets are independent over Q as well. Thus
\[
B_3(Y)\cap V=\operatorname{span}\{\phi\},\qquad \beta_3(Y)=3.
\]
This conclusion is reproduced from the finite graph. The source already proves the intended topology algebraically; this is verification and a reusable certificate, not a new homology gadget.

For lambda>0, the invertible diagonal weight gauge preserves homology and fixes the weight-one register coordinates, so the boundary intersection is unchanged.

## 2. Central relative bulk

The central vertex v0 has only new neighbors. Its link has simplex counts 26, 114, 176, 88 in degrees 0,1,2,3. Central degree-3 chains correspond to link degree-2 chains. After retaining central output simplices, the local boundary/coboundary pair on this bulk is lambda times
\[
A=\begin{bmatrix}\partial^{link}_2\\(\partial^{link}_3)^*\end{bmatrix}
\]
up to orientation signs.

For the 176-by-176 integer Gram matrix G=A^*A:
\[
\det(G)\equiv797443\ne0\pmod{1000003},\qquad
\|G\|_\infty=14.
\]
Thus G is positive definite over R. Since its determinant is a positive integer and every eigenvalue is at most 14,
\[
\lambda_{\min}(G)\ge14^{-175}.
\]
The archive records the deliberately conservative rational bound
\[
\sigma_{\min}(A)\ge14^{-176}.
\]
Therefore the weighted projected pair is injective with singular value at least lambda times that fixed constant. Padding this pair with outside harmonics preserves this bound; padding with all outside coordinates does not establish the required O(lambda) estimate.

## 3. Zero-weight kernel and elementary positive-gap floor

Set all 14 register vertex weights to one and all 27 new weights to zero. At target degree 3, write the differential pair as D(lambda)=D_0+lambda D_1.

Exact integer checks show:

- D_0 annihilates all four register cycles and all 176 central bulk coordinates.
- These subspaces are independent; the register basis Gram matrix is 16I.
- D_0 has rank 902 modulo p. The explicit 180-dimensional kernel gives the matching rational upper bound 1082-180=902.
- The projected central pair has zero constant term and its lambda coefficient annihilates the register cycles.

Consequently
\[
\ker D_0=V\oplus Q,\qquad \dim V=4,\quad \dim Q=176.
\]
No additional zero-weight sectors are hidden in the full target chain space.

The integer Gram norm bounds are
\[
\|D_0^*D_0\|_\infty=12,\quad
\|D_1^*D_1\|_\infty=15,\quad
\|\Delta_3(1)\|_\infty=21.
\]
The first Gram has rank 902, so its least positive eigenvalue is at least 12^-901. The unweighted Laplacian has rank 1082-3=1079, so its least positive eigenvalue is at least 21^-1078. Section 2 of the concentration theorem's weight-scaling argument then gives
\[
\gamma_+(\Delta_3(\lambda))\ge21^{-1078}\lambda^{10},
\qquad 0<\lambda\le1.
\]
This proves a finite positive-gap lower bound adequate for the new route. It does not prove that lambda^10 is the optimal asymptotic order or compute its leading coefficient. The new proof does not need either fact.

## 4. A genuine correction exposed by the graph

The graph has 30 degree-5 simplices, although its logical target is degree 3. The earlier padding note asserted that only bidegrees (2m-1,q) and (2m,q-1) occur. That enumeration is false for this representative.

The repair is to quantify over every actual bidegree. The outside register has harmonics only in top degree q; consequently the only outside-harmonic summand at the target total degree is (2m-1,q). Every other summand, however high the local dimension, has a positive outside gap. The repaired argument supports the same intended conclusion. This is a mathematical correction to the local exposition, not a counterexample to the repaired padding theorem.

The mutable round-2 note is corrected and cross-linked. The previously transmitted PRO_CONTEXT_PACKET.md remains frozen, so the follow-up explicitly tells Pro about the change.

## 5. Remaining gates

This graph passes the exact topology, zero-weight kernel and projected-bulk injectivity requirements of the new conditional theorem. Still open:

- the other active atom types and their allowed signed/relabeling symmetries;
- a proof of closure under joins of the implementing spheres and attaching maps with computational-basis guards, or finite certificates for every required guarded graph through locality six;
- a complete literature comparison for the all-chain theorem and improved gap dependence;
- a meaningful exact circuit-source complexity consequence beyond the conditional D=1, perfect-completeness specialization.

The certificate and the abstract proof must survive independent review before stronger claims are promoted. No full reduction, unrestricted SDQC1 equivalence, or paper-readiness conclusion is recorded.


<!-- END INCLUDED FILE: REPRESENTATIVE_GADGET_CERTIFICATE.md -->


<!-- BEGIN INCLUDED FILE: RUDOLPH_REPRESENTATIVE_BULK_CERTIFICATE.json -->

# Included file 5: RUDOLPH_REPRESENTATIVE_BULK_CERTIFICATE.json

{
  "status": "PASS",
  "scope": "Exact target homology, intended filling, zero-weight kernel, and central-relative-bulk injectivity for one source graph; not the complete guarded palette",
  "source": {
    "url": "https://github.com/DorianRudolph/QMA1-gateset-paper/blob/30ac70e5dacdecce97c38d801c128ec3ed93a96a/gadget_homology.py",
    "commit": "30ac70e5dacdecce97c38d801c128ec3ed93a96a",
    "sha256": "c8918f9e037ae79796bb65640170c8e60f31883625d24348f3476f7644dcd29a",
    "function": "state_00m10m11",
    "upstream_license": "GPLv2-or-later",
    "execution": "Only inspected graph-building AST definitions; stopped before Sage operations"
  },
  "projector": {
    "integer_amplitudes_00_01_10_11": [
      1,
      0,
      -1,
      -1
    ],
    "relation_to_requested_representative": "Overall minus sign; same rank-one projector"
  },
  "graph": {
    "vertices": [
      "0.a2",
      "0.a2.1",
      "0.a3",
      "0.a3.1",
      "0.a4",
      "0.a4.1",
      "0.b2",
      "0.b2.1",
      "0.b2_.1",
      "0.b3",
      "0.b3.1",
      "0.b3_.1",
      "0.b4",
      "0.b4.1",
      "0.b4_.1",
      "0.xx",
      "0.xx.1",
      "1.a2",
      "1.a2.1",
      "1.a2_.1",
      "1.a3",
      "1.a3.1",
      "1.a3_.1",
      "1.a4",
      "1.a4.1",
      "1.a4_.1",
      "1.b2",
      "1.b2.1",
      "1.b3",
      "1.b3.1",
      "1.b4",
      "1.b4.1",
      "1.xx",
      "1.xx.1",
      "v0",
      "x1.1",
      "x2.1",
      "x3.1",
      "x4.1",
      "x5.1",
      "x6.1"
    ],
    "edges": [
      [
        "0.a2",
        "0.a2.1"
      ],
      [
        "0.a2",
        "0.a3"
      ],
      [
        "0.a2",
        "0.a3.1"
      ],
      [
        "0.a2",
        "0.a4"
      ],
      [
        "0.a2",
        "0.a4.1"
      ],
      [
        "0.a2",
        "1.a2"
      ],
      [
        "0.a2",
        "1.a2.1"
      ],
      [
        "0.a2",
        "1.a3"
      ],
      [
        "0.a2",
        "1.a3.1"
      ],
      [
        "0.a2",
        "1.a4"
      ],
      [
        "0.a2",
        "1.a4.1"
      ],
      [
        "0.a2",
        "1.b2"
      ],
      [
        "0.a2",
        "1.b3"
      ],
      [
        "0.a2",
        "1.b4"
      ],
      [
        "0.a2",
        "1.xx"
      ],
      [
        "0.a2",
        "1.xx.1"
      ],
      [
        "0.a2.1",
        "0.a3.1"
      ],
      [
        "0.a2.1",
        "0.a4.1"
      ],
      [
        "0.a2.1",
        "1.a2.1"
      ],
      [
        "0.a2.1",
        "1.a3.1"
      ],
      [
        "0.a2.1",
        "1.a4.1"
      ],
      [
        "0.a2.1",
        "1.xx.1"
      ],
      [
        "0.a2.1",
        "v0"
      ],
      [
        "0.a3",
        "0.a3.1"
      ],
      [
        "0.a3",
        "0.xx"
      ],
      [
        "0.a3",
        "0.xx.1"
      ],
      [
        "0.a3",
        "1.a2"
      ],
      [
        "0.a3",
        "1.a2.1"
      ],
      [
        "0.a3",
        "1.a3"
      ],
      [
        "0.a3",
        "1.a3.1"
      ],
      [
        "0.a3",
        "1.a4"
      ],
      [
        "0.a3",
        "1.a4.1"
      ],
      [
        "0.a3",
        "1.b2"
      ],
      [
        "0.a3",
        "1.b3"
      ],
      [
        "0.a3",
        "1.b4"
      ],
      [
        "0.a3",
        "1.xx"
      ],
      [
        "0.a3",
        "1.xx.1"
      ],
      [
        "0.a3",
        "x1.1"
      ],
      [
        "0.a3",
        "x2.1"
      ],
      [
        "0.a3.1",
        "0.xx.1"
      ],
      [
        "0.a3.1",
        "1.a2.1"
      ],
      [
        "0.a3.1",
        "1.a3.1"
      ],
      [
        "0.a3.1",
        "1.a4.1"
      ],
      [
        "0.a3.1",
        "1.xx.1"
      ],
      [
        "0.a3.1",
        "v0"
      ],
      [
        "0.a3.1",
        "x1.1"
      ],
      [
        "0.a3.1",
        "x2.1"
      ],
      [
        "0.a4",
        "0.a4.1"
      ],
      [
        "0.a4",
        "0.xx"
      ],
      [
        "0.a4",
        "0.xx.1"
      ],
      [
        "0.a4",
        "1.a2"
      ],
      [
        "0.a4",
        "1.a2.1"
      ],
      [
        "0.a4",
        "1.a3"
      ],
      [
        "0.a4",
        "1.a3.1"
      ],
      [
        "0.a4",
        "1.a4"
      ],
      [
        "0.a4",
        "1.a4.1"
      ],
      [
        "0.a4",
        "1.b2"
      ],
      [
        "0.a4",
        "1.b3"
      ],
      [
        "0.a4",
        "1.b4"
      ],
      [
        "0.a4",
        "1.xx"
      ],
      [
        "0.a4",
        "1.xx.1"
      ],
      [
        "0.a4",
        "x3.1"
      ],
      [
        "0.a4",
        "x4.1"
      ],
      [
        "0.a4.1",
        "0.xx.1"
      ],
      [
        "0.a4.1",
        "1.a2.1"
      ],
      [
        "0.a4.1",
        "1.a3.1"
      ],
      [
        "0.a4.1",
        "1.a4.1"
      ],
      [
        "0.a4.1",
        "1.xx.1"
      ],
      [
        "0.a4.1",
        "v0"
      ],
      [
        "0.a4.1",
        "x3.1"
      ],
      [
        "0.a4.1",
        "x4.1"
      ],
      [
        "0.b2",
        "0.b2.1"
      ],
      [
        "0.b2",
        "0.b2_.1"
      ],
      [
        "0.b2",
        "0.b3"
      ],
      [
        "0.b2",
        "0.b3.1"
      ],
      [
        "0.b2",
        "0.b3_.1"
      ],
      [
        "0.b2",
        "0.b4"
      ],
      [
        "0.b2",
        "0.b4.1"
      ],
      [
        "0.b2",
        "0.b4_.1"
      ],
      [
        "0.b2",
        "1.a2"
      ],
      [
        "0.b2",
        "1.a2_.1"
      ],
      [
        "0.b2",
        "1.a3"
      ],
      [
        "0.b2",
        "1.a3_.1"
      ],
      [
        "0.b2",
        "1.a4"
      ],
      [
        "0.b2",
        "1.a4_.1"
      ],
      [
        "0.b2",
        "1.b2"
      ],
      [
        "0.b2",
        "1.b2.1"
      ],
      [
        "0.b2",
        "1.b3"
      ],
      [
        "0.b2",
        "1.b3.1"
      ],
      [
        "0.b2",
        "1.b4"
      ],
      [
        "0.b2",
        "1.b4.1"
      ],
      [
        "0.b2",
        "1.xx"
      ],
      [
        "0.b2",
        "1.xx.1"
      ],
      [
        "0.b2.1",
        "0.b3.1"
      ],
      [
        "0.b2.1",
        "0.b4.1"
      ],
      [
        "0.b2.1",
        "1.b2.1"
      ],
      [
        "0.b2.1",
        "1.b3.1"
      ],
      [
        "0.b2.1",
        "1.b4.1"
      ],
      [
        "0.b2.1",
        "1.xx.1"
      ],
      [
        "0.b2.1",
        "v0"
      ],
      [
        "0.b2_.1",
        "0.b3_.1"
      ],
      [
        "0.b2_.1",
        "0.b4_.1"
      ],
      [
        "0.b2_.1",
        "1.a2_.1"
      ],
      [
        "0.b2_.1",
        "1.a3_.1"
      ],
      [
        "0.b2_.1",
        "1.a4_.1"
      ],
      [
        "0.b2_.1",
        "1.xx.1"
      ],
      [
        "0.b2_.1",
        "v0"
      ],
      [
        "0.b3",
        "0.b3.1"
      ],
      [
        "0.b3",
        "0.b3_.1"
      ],
      [
        "0.b3",
        "0.xx"
      ],
      [
        "0.b3",
        "0.xx.1"
      ],
      [
        "0.b3",
        "1.a2"
      ],
      [
        "0.b3",
        "1.a2_.1"
      ],
      [
        "0.b3",
        "1.a3"
      ],
      [
        "0.b3",
        "1.a3_.1"
      ],
      [
        "0.b3",
        "1.a4"
      ],
      [
        "0.b3",
        "1.a4_.1"
      ],
      [
        "0.b3",
        "1.b2"
      ],
      [
        "0.b3",
        "1.b2.1"
      ],
      [
        "0.b3",
        "1.b3"
      ],
      [
        "0.b3",
        "1.b3.1"
      ],
      [
        "0.b3",
        "1.b4"
      ],
      [
        "0.b3",
        "1.b4.1"
      ],
      [
        "0.b3",
        "1.xx"
      ],
      [
        "0.b3",
        "1.xx.1"
      ],
      [
        "0.b3",
        "x2.1"
      ],
      [
        "0.b3",
        "x3.1"
      ],
      [
        "0.b3",
        "x5.1"
      ],
      [
        "0.b3",
        "x6.1"
      ],
      [
        "0.b3.1",
        "0.xx.1"
      ],
      [
        "0.b3.1",
        "1.b2.1"
      ],
      [
        "0.b3.1",
        "1.b3.1"
      ],
      [
        "0.b3.1",
        "1.b4.1"
      ],
      [
        "0.b3.1",
        "1.xx.1"
      ],
      [
        "0.b3.1",
        "v0"
      ],
      [
        "0.b3.1",
        "x2.1"
      ],
      [
        "0.b3.1",
        "x3.1"
      ],
      [
        "0.b3_.1",
        "0.xx.1"
      ],
      [
        "0.b3_.1",
        "1.a2_.1"
      ],
      [
        "0.b3_.1",
        "1.a3_.1"
      ],
      [
        "0.b3_.1",
        "1.a4_.1"
      ],
      [
        "0.b3_.1",
        "1.xx.1"
      ],
      [
        "0.b3_.1",
        "v0"
      ],
      [
        "0.b3_.1",
        "x5.1"
      ],
      [
        "0.b3_.1",
        "x6.1"
      ],
      [
        "0.b4",
        "0.b4.1"
      ],
      [
        "0.b4",
        "0.b4_.1"
      ],
      [
        "0.b4",
        "0.xx"
      ],
      [
        "0.b4",
        "0.xx.1"
      ],
      [
        "0.b4",
        "1.a2"
      ],
      [
        "0.b4",
        "1.a2_.1"
      ],
      [
        "0.b4",
        "1.a3"
      ],
      [
        "0.b4",
        "1.a3_.1"
      ],
      [
        "0.b4",
        "1.a4"
      ],
      [
        "0.b4",
        "1.a4_.1"
      ],
      [
        "0.b4",
        "1.b2"
      ],
      [
        "0.b4",
        "1.b2.1"
      ],
      [
        "0.b4",
        "1.b3"
      ],
      [
        "0.b4",
        "1.b3.1"
      ],
      [
        "0.b4",
        "1.b4"
      ],
      [
        "0.b4",
        "1.b4.1"
      ],
      [
        "0.b4",
        "1.xx"
      ],
      [
        "0.b4",
        "1.xx.1"
      ],
      [
        "0.b4",
        "x1.1"
      ],
      [
        "0.b4",
        "x4.1"
      ],
      [
        "0.b4",
        "x5.1"
      ],
      [
        "0.b4",
        "x6.1"
      ],
      [
        "0.b4.1",
        "0.xx.1"
      ],
      [
        "0.b4.1",
        "1.b2.1"
      ],
      [
        "0.b4.1",
        "1.b3.1"
      ],
      [
        "0.b4.1",
        "1.b4.1"
      ],
      [
        "0.b4.1",
        "1.xx.1"
      ],
      [
        "0.b4.1",
        "v0"
      ],
      [
        "0.b4.1",
        "x5.1"
      ],
      [
        "0.b4.1",
        "x6.1"
      ],
      [
        "0.b4_.1",
        "0.xx.1"
      ],
      [
        "0.b4_.1",
        "1.a2_.1"
      ],
      [
        "0.b4_.1",
        "1.a3_.1"
      ],
      [
        "0.b4_.1",
        "1.a4_.1"
      ],
      [
        "0.b4_.1",
        "1.xx.1"
      ],
      [
        "0.b4_.1",
        "v0"
      ],
      [
        "0.b4_.1",
        "x1.1"
      ],
      [
        "0.b4_.1",
        "x4.1"
      ],
      [
        "0.xx",
        "0.xx.1"
      ],
      [
        "0.xx",
        "1.a2"
      ],
      [
        "0.xx",
        "1.a2.1"
      ],
      [
        "0.xx",
        "1.a2_.1"
      ],
      [
        "0.xx",
        "1.a3"
      ],
      [
        "0.xx",
        "1.a3.1"
      ],
      [
        "0.xx",
        "1.a3_.1"
      ],
      [
        "0.xx",
        "1.a4"
      ],
      [
        "0.xx",
        "1.a4.1"
      ],
      [
        "0.xx",
        "1.a4_.1"
      ],
      [
        "0.xx",
        "1.b2"
      ],
      [
        "0.xx",
        "1.b2.1"
      ],
      [
        "0.xx",
        "1.b3"
      ],
      [
        "0.xx",
        "1.b3.1"
      ],
      [
        "0.xx",
        "1.b4"
      ],
      [
        "0.xx",
        "1.b4.1"
      ],
      [
        "0.xx",
        "1.xx"
      ],
      [
        "0.xx",
        "x1.1"
      ],
      [
        "0.xx",
        "x2.1"
      ],
      [
        "0.xx",
        "x3.1"
      ],
      [
        "0.xx",
        "x4.1"
      ],
      [
        "0.xx",
        "x5.1"
      ],
      [
        "0.xx",
        "x6.1"
      ],
      [
        "0.xx.1",
        "1.a2.1"
      ],
      [
        "0.xx.1",
        "1.a2_.1"
      ],
      [
        "0.xx.1",
        "1.a3.1"
      ],
      [
        "0.xx.1",
        "1.a3_.1"
      ],
      [
        "0.xx.1",
        "1.a4.1"
      ],
      [
        "0.xx.1",
        "1.a4_.1"
      ],
      [
        "0.xx.1",
        "1.b2.1"
      ],
      [
        "0.xx.1",
        "1.b3.1"
      ],
      [
        "0.xx.1",
        "1.b4.1"
      ],
      [
        "0.xx.1",
        "v0"
      ],
      [
        "0.xx.1",
        "x1.1"
      ],
      [
        "0.xx.1",
        "x2.1"
      ],
      [
        "0.xx.1",
        "x3.1"
      ],
      [
        "0.xx.1",
        "x4.1"
      ],
      [
        "0.xx.1",
        "x5.1"
      ],
      [
        "0.xx.1",
        "x6.1"
      ],
      [
        "1.a2",
        "1.a2.1"
      ],
      [
        "1.a2",
        "1.a2_.1"
      ],
      [
        "1.a2",
        "1.a3"
      ],
      [
        "1.a2",
        "1.a3.1"
      ],
      [
        "1.a2",
        "1.a3_.1"
      ],
      [
        "1.a2",
        "1.a4"
      ],
      [
        "1.a2",
        "1.a4.1"
      ],
      [
        "1.a2",
        "1.a4_.1"
      ],
      [
        "1.a2.1",
        "1.a3.1"
      ],
      [
        "1.a2.1",
        "1.a4.1"
      ],
      [
        "1.a2.1",
        "v0"
      ],
      [
        "1.a2_.1",
        "1.a3_.1"
      ],
      [
        "1.a2_.1",
        "1.a4_.1"
      ],
      [
        "1.a2_.1",
        "v0"
      ],
      [
        "1.a3",
        "1.a3.1"
      ],
      [
        "1.a3",
        "1.a3_.1"
      ],
      [
        "1.a3",
        "1.xx"
      ],
      [
        "1.a3",
        "1.xx.1"
      ],
      [
        "1.a3",
        "x1.1"
      ],
      [
        "1.a3",
        "x4.1"
      ],
      [
        "1.a3",
        "x5.1"
      ],
      [
        "1.a3.1",
        "1.xx.1"
      ],
      [
        "1.a3.1",
        "v0"
      ],
      [
        "1.a3.1",
        "x1.1"
      ],
      [
        "1.a3.1",
        "x4.1"
      ],
      [
        "1.a3_.1",
        "1.xx.1"
      ],
      [
        "1.a3_.1",
        "v0"
      ],
      [
        "1.a3_.1",
        "x1.1"
      ],
      [
        "1.a3_.1",
        "x5.1"
      ],
      [
        "1.a4",
        "1.a4.1"
      ],
      [
        "1.a4",
        "1.a4_.1"
      ],
      [
        "1.a4",
        "1.xx"
      ],
      [
        "1.a4",
        "1.xx.1"
      ],
      [
        "1.a4",
        "x2.1"
      ],
      [
        "1.a4",
        "x3.1"
      ],
      [
        "1.a4",
        "x4.1"
      ],
      [
        "1.a4",
        "x6.1"
      ],
      [
        "1.a4.1",
        "1.xx.1"
      ],
      [
        "1.a4.1",
        "v0"
      ],
      [
        "1.a4.1",
        "x2.1"
      ],
      [
        "1.a4.1",
        "x3.1"
      ],
      [
        "1.a4_.1",
        "1.xx.1"
      ],
      [
        "1.a4_.1",
        "v0"
      ],
      [
        "1.a4_.1",
        "x4.1"
      ],
      [
        "1.a4_.1",
        "x6.1"
      ],
      [
        "1.b2",
        "1.b2.1"
      ],
      [
        "1.b2",
        "1.b3"
      ],
      [
        "1.b2",
        "1.b3.1"
      ],
      [
        "1.b2",
        "1.b4"
      ],
      [
        "1.b2",
        "1.b4.1"
      ],
      [
        "1.b2.1",
        "1.b3.1"
      ],
      [
        "1.b2.1",
        "1.b4.1"
      ],
      [
        "1.b2.1",
        "v0"
      ],
      [
        "1.b3",
        "1.b3.1"
      ],
      [
        "1.b3",
        "1.xx"
      ],
      [
        "1.b3",
        "1.xx.1"
      ],
      [
        "1.b3",
        "x2.1"
      ],
      [
        "1.b3",
        "x5.1"
      ],
      [
        "1.b3.1",
        "1.xx.1"
      ],
      [
        "1.b3.1",
        "v0"
      ],
      [
        "1.b3.1",
        "x2.1"
      ],
      [
        "1.b3.1",
        "x5.1"
      ],
      [
        "1.b4",
        "1.b4.1"
      ],
      [
        "1.b4",
        "1.xx"
      ],
      [
        "1.b4",
        "1.xx.1"
      ],
      [
        "1.b4",
        "x3.1"
      ],
      [
        "1.b4",
        "x6.1"
      ],
      [
        "1.b4.1",
        "1.xx.1"
      ],
      [
        "1.b4.1",
        "v0"
      ],
      [
        "1.b4.1",
        "x3.1"
      ],
      [
        "1.b4.1",
        "x6.1"
      ],
      [
        "1.xx",
        "1.xx.1"
      ],
      [
        "1.xx",
        "x1.1"
      ],
      [
        "1.xx",
        "x2.1"
      ],
      [
        "1.xx",
        "x3.1"
      ],
      [
        "1.xx",
        "x4.1"
      ],
      [
        "1.xx",
        "x5.1"
      ],
      [
        "1.xx",
        "x6.1"
      ],
      [
        "1.xx.1",
        "v0"
      ],
      [
        "1.xx.1",
        "x1.1"
      ],
      [
        "1.xx.1",
        "x2.1"
      ],
      [
        "1.xx.1",
        "x3.1"
      ],
      [
        "1.xx.1",
        "x4.1"
      ],
      [
        "1.xx.1",
        "x5.1"
      ],
      [
        "1.xx.1",
        "x6.1"
      ],
      [
        "v0",
        "x1.1"
      ],
      [
        "v0",
        "x2.1"
      ],
      [
        "v0",
        "x3.1"
      ],
      [
        "v0",
        "x4.1"
      ],
      [
        "v0",
        "x5.1"
      ],
      [
        "v0",
        "x6.1"
      ],
      [
        "x1.1",
        "x2.1"
      ],
      [
        "x1.1",
        "x4.1"
      ],
      [
        "x1.1",
        "x5.1"
      ],
      [
        "x2.1",
        "x3.1"
      ],
      [
        "x2.1",
        "x5.1"
      ],
      [
        "x3.1",
        "x4.1"
      ],
      [
        "x3.1",
        "x6.1"
      ],
      [
        "x4.1",
        "x6.1"
      ],
      [
        "x5.1",
        "x6.1"
      ]
    ],
    "simplex_counts": {
      "0": 41,
      "1": 322,
      "2": 914,
      "3": 1082,
      "4": 477,
      "5": 30
    },
    "maximum_dimension": 5
  },
  "central_link": {
    "vertices": [
      "0.a2.1",
      "0.a3.1",
      "0.a4.1",
      "0.b2.1",
      "0.b2_.1",
      "0.b3.1",
      "0.b3_.1",
      "0.b4.1",
      "0.b4_.1",
      "0.xx.1",
      "1.a2.1",
      "1.a2_.1",
      "1.a3.1",
      "1.a3_.1",
      "1.a4.1",
      "1.a4_.1",
      "1.b2.1",
      "1.b3.1",
      "1.b4.1",
      "1.xx.1",
      "x1.1",
      "x2.1",
      "x3.1",
      "x4.1",
      "x5.1",
      "x6.1"
    ],
    "edges": [
      [
        "0.a2.1",
        "0.a3.1"
      ],
      [
        "0.a2.1",
        "0.a4.1"
      ],
      [
        "0.a2.1",
        "1.a2.1"
      ],
      [
        "0.a2.1",
        "1.a3.1"
      ],
      [
        "0.a2.1",
        "1.a4.1"
      ],
      [
        "0.a2.1",
        "1.xx.1"
      ],
      [
        "0.a3.1",
        "0.xx.1"
      ],
      [
        "0.a3.1",
        "1.a2.1"
      ],
      [
        "0.a3.1",
        "1.a3.1"
      ],
      [
        "0.a3.1",
        "1.a4.1"
      ],
      [
        "0.a3.1",
        "1.xx.1"
      ],
      [
        "0.a3.1",
        "x1.1"
      ],
      [
        "0.a3.1",
        "x2.1"
      ],
      [
        "0.a4.1",
        "0.xx.1"
      ],
      [
        "0.a4.1",
        "1.a2.1"
      ],
      [
        "0.a4.1",
        "1.a3.1"
      ],
      [
        "0.a4.1",
        "1.a4.1"
      ],
      [
        "0.a4.1",
        "1.xx.1"
      ],
      [
        "0.a4.1",
        "x3.1"
      ],
      [
        "0.a4.1",
        "x4.1"
      ],
      [
        "0.b2.1",
        "0.b3.1"
      ],
      [
        "0.b2.1",
        "0.b4.1"
      ],
      [
        "0.b2.1",
        "1.b2.1"
      ],
      [
        "0.b2.1",
        "1.b3.1"
      ],
      [
        "0.b2.1",
        "1.b4.1"
      ],
      [
        "0.b2.1",
        "1.xx.1"
      ],
      [
        "0.b2_.1",
        "0.b3_.1"
      ],
      [
        "0.b2_.1",
        "0.b4_.1"
      ],
      [
        "0.b2_.1",
        "1.a2_.1"
      ],
      [
        "0.b2_.1",
        "1.a3_.1"
      ],
      [
        "0.b2_.1",
        "1.a4_.1"
      ],
      [
        "0.b2_.1",
        "1.xx.1"
      ],
      [
        "0.b3.1",
        "0.xx.1"
      ],
      [
        "0.b3.1",
        "1.b2.1"
      ],
      [
        "0.b3.1",
        "1.b3.1"
      ],
      [
        "0.b3.1",
        "1.b4.1"
      ],
      [
        "0.b3.1",
        "1.xx.1"
      ],
      [
        "0.b3.1",
        "x2.1"
      ],
      [
        "0.b3.1",
        "x3.1"
      ],
      [
        "0.b3_.1",
        "0.xx.1"
      ],
      [
        "0.b3_.1",
        "1.a2_.1"
      ],
      [
        "0.b3_.1",
        "1.a3_.1"
      ],
      [
        "0.b3_.1",
        "1.a4_.1"
      ],
      [
        "0.b3_.1",
        "1.xx.1"
      ],
      [
        "0.b3_.1",
        "x5.1"
      ],
      [
        "0.b3_.1",
        "x6.1"
      ],
      [
        "0.b4.1",
        "0.xx.1"
      ],
      [
        "0.b4.1",
        "1.b2.1"
      ],
      [
        "0.b4.1",
        "1.b3.1"
      ],
      [
        "0.b4.1",
        "1.b4.1"
      ],
      [
        "0.b4.1",
        "1.xx.1"
      ],
      [
        "0.b4.1",
        "x5.1"
      ],
      [
        "0.b4.1",
        "x6.1"
      ],
      [
        "0.b4_.1",
        "0.xx.1"
      ],
      [
        "0.b4_.1",
        "1.a2_.1"
      ],
      [
        "0.b4_.1",
        "1.a3_.1"
      ],
      [
        "0.b4_.1",
        "1.a4_.1"
      ],
      [
        "0.b4_.1",
        "1.xx.1"
      ],
      [
        "0.b4_.1",
        "x1.1"
      ],
      [
        "0.b4_.1",
        "x4.1"
      ],
      [
        "0.xx.1",
        "1.a2.1"
      ],
      [
        "0.xx.1",
        "1.a2_.1"
      ],
      [
        "0.xx.1",
        "1.a3.1"
      ],
      [
        "0.xx.1",
        "1.a3_.1"
      ],
      [
        "0.xx.1",
        "1.a4.1"
      ],
      [
        "0.xx.1",
        "1.a4_.1"
      ],
      [
        "0.xx.1",
        "1.b2.1"
      ],
      [
        "0.xx.1",
        "1.b3.1"
      ],
      [
        "0.xx.1",
        "1.b4.1"
      ],
      [
        "0.xx.1",
        "x1.1"
      ],
      [
        "0.xx.1",
        "x2.1"
      ],
      [
        "0.xx.1",
        "x3.1"
      ],
      [
        "0.xx.1",
        "x4.1"
      ],
      [
        "0.xx.1",
        "x5.1"
      ],
      [
        "0.xx.1",
        "x6.1"
      ],
      [
        "1.a2.1",
        "1.a3.1"
      ],
      [
        "1.a2.1",
        "1.a4.1"
      ],
      [
        "1.a2_.1",
        "1.a3_.1"
      ],
      [
        "1.a2_.1",
        "1.a4_.1"
      ],
      [
        "1.a3.1",
        "1.xx.1"
      ],
      [
        "1.a3.1",
        "x1.1"
      ],
      [
        "1.a3.1",
        "x4.1"
      ],
      [
        "1.a3_.1",
        "1.xx.1"
      ],
      [
        "1.a3_.1",
        "x1.1"
      ],
      [
        "1.a3_.1",
        "x5.1"
      ],
      [
        "1.a4.1",
        "1.xx.1"
      ],
      [
        "1.a4.1",
        "x2.1"
      ],
      [
        "1.a4.1",
        "x3.1"
      ],
      [
        "1.a4_.1",
        "1.xx.1"
      ],
      [
        "1.a4_.1",
        "x4.1"
      ],
      [
        "1.a4_.1",
        "x6.1"
      ],
      [
        "1.b2.1",
        "1.b3.1"
      ],
      [
        "1.b2.1",
        "1.b4.1"
      ],
      [
        "1.b3.1",
        "1.xx.1"
      ],
      [
        "1.b3.1",
        "x2.1"
      ],
      [
        "1.b3.1",
        "x5.1"
      ],
      [
        "1.b4.1",
        "1.xx.1"
      ],
      [
        "1.b4.1",
        "x3.1"
      ],
      [
        "1.b4.1",
        "x6.1"
      ],
      [
        "1.xx.1",
        "x1.1"
      ],
      [
        "1.xx.1",
        "x2.1"
      ],
      [
        "1.xx.1",
        "x3.1"
      ],
      [
        "1.xx.1",
        "x4.1"
      ],
      [
        "1.xx.1",
        "x5.1"
      ],
      [
        "1.xx.1",
        "x6.1"
      ],
      [
        "x1.1",
        "x2.1"
      ],
      [
        "x1.1",
        "x4.1"
      ],
      [
        "x1.1",
        "x5.1"
      ],
      [
        "x2.1",
        "x3.1"
      ],
      [
        "x2.1",
        "x5.1"
      ],
      [
        "x3.1",
        "x4.1"
      ],
      [
        "x3.1",
        "x6.1"
      ],
      [
        "x4.1",
        "x6.1"
      ],
      [
        "x5.1",
        "x6.1"
      ]
    ],
    "simplex_counts": {
      "0": 26,
      "1": 114,
      "2": 176,
      "3": 88
    },
    "ordered_triangles": [
      [
        "0.a2.1",
        "0.a3.1",
        "1.a2.1"
      ],
      [
        "0.a2.1",
        "0.a3.1",
        "1.a3.1"
      ],
      [
        "0.a2.1",
        "0.a3.1",
        "1.a4.1"
      ],
      [
        "0.a2.1",
        "0.a3.1",
        "1.xx.1"
      ],
      [
        "0.a2.1",
        "0.a4.1",
        "1.a2.1"
      ],
      [
        "0.a2.1",
        "0.a4.1",
        "1.a3.1"
      ],
      [
        "0.a2.1",
        "0.a4.1",
        "1.a4.1"
      ],
      [
        "0.a2.1",
        "0.a4.1",
        "1.xx.1"
      ],
      [
        "0.a2.1",
        "1.a2.1",
        "1.a3.1"
      ],
      [
        "0.a2.1",
        "1.a2.1",
        "1.a4.1"
      ],
      [
        "0.a2.1",
        "1.a3.1",
        "1.xx.1"
      ],
      [
        "0.a2.1",
        "1.a4.1",
        "1.xx.1"
      ],
      [
        "0.a3.1",
        "0.xx.1",
        "1.a2.1"
      ],
      [
        "0.a3.1",
        "0.xx.1",
        "1.a3.1"
      ],
      [
        "0.a3.1",
        "0.xx.1",
        "1.a4.1"
      ],
      [
        "0.a3.1",
        "0.xx.1",
        "x1.1"
      ],
      [
        "0.a3.1",
        "0.xx.1",
        "x2.1"
      ],
      [
        "0.a3.1",
        "1.a2.1",
        "1.a3.1"
      ],
      [
        "0.a3.1",
        "1.a2.1",
        "1.a4.1"
      ],
      [
        "0.a3.1",
        "1.a3.1",
        "1.xx.1"
      ],
      [
        "0.a3.1",
        "1.a3.1",
        "x1.1"
      ],
      [
        "0.a3.1",
        "1.a4.1",
        "1.xx.1"
      ],
      [
        "0.a3.1",
        "1.a4.1",
        "x2.1"
      ],
      [
        "0.a3.1",
        "1.xx.1",
        "x1.1"
      ],
      [
        "0.a3.1",
        "1.xx.1",
        "x2.1"
      ],
      [
        "0.a3.1",
        "x1.1",
        "x2.1"
      ],
      [
        "0.a4.1",
        "0.xx.1",
        "1.a2.1"
      ],
      [
        "0.a4.1",
        "0.xx.1",
        "1.a3.1"
      ],
      [
        "0.a4.1",
        "0.xx.1",
        "1.a4.1"
      ],
      [
        "0.a4.1",
        "0.xx.1",
        "x3.1"
      ],
      [
        "0.a4.1",
        "0.xx.1",
        "x4.1"
      ],
      [
        "0.a4.1",
        "1.a2.1",
        "1.a3.1"
      ],
      [
        "0.a4.1",
        "1.a2.1",
        "1.a4.1"
      ],
      [
        "0.a4.1",
        "1.a3.1",
        "1.xx.1"
      ],
      [
        "0.a4.1",
        "1.a3.1",
        "x4.1"
      ],
      [
        "0.a4.1",
        "1.a4.1",
        "1.xx.1"
      ],
      [
        "0.a4.1",
        "1.a4.1",
        "x3.1"
      ],
      [
        "0.a4.1",
        "1.xx.1",
        "x3.1"
      ],
      [
        "0.a4.1",
        "1.xx.1",
        "x4.1"
      ],
      [
        "0.a4.1",
        "x3.1",
        "x4.1"
      ],
      [
        "0.b2.1",
        "0.b3.1",
        "1.b2.1"
      ],
      [
        "0.b2.1",
        "0.b3.1",
        "1.b3.1"
      ],
      [
        "0.b2.1",
        "0.b3.1",
        "1.b4.1"
      ],
      [
        "0.b2.1",
        "0.b3.1",
        "1.xx.1"
      ],
      [
        "0.b2.1",
        "0.b4.1",
        "1.b2.1"
      ],
      [
        "0.b2.1",
        "0.b4.1",
        "1.b3.1"
      ],
      [
        "0.b2.1",
        "0.b4.1",
        "1.b4.1"
      ],
      [
        "0.b2.1",
        "0.b4.1",
        "1.xx.1"
      ],
      [
        "0.b2.1",
        "1.b2.1",
        "1.b3.1"
      ],
      [
        "0.b2.1",
        "1.b2.1",
        "1.b4.1"
      ],
      [
        "0.b2.1",
        "1.b3.1",
        "1.xx.1"
      ],
      [
        "0.b2.1",
        "1.b4.1",
        "1.xx.1"
      ],
      [
        "0.b2_.1",
        "0.b3_.1",
        "1.a2_.1"
      ],
      [
        "0.b2_.1",
        "0.b3_.1",
        "1.a3_.1"
      ],
      [
        "0.b2_.1",
        "0.b3_.1",
        "1.a4_.1"
      ],
      [
        "0.b2_.1",
        "0.b3_.1",
        "1.xx.1"
      ],
      [
        "0.b2_.1",
        "0.b4_.1",
        "1.a2_.1"
      ],
      [
        "0.b2_.1",
        "0.b4_.1",
        "1.a3_.1"
      ],
      [
        "0.b2_.1",
        "0.b4_.1",
        "1.a4_.1"
      ],
      [
        "0.b2_.1",
        "0.b4_.1",
        "1.xx.1"
      ],
      [
        "0.b2_.1",
        "1.a2_.1",
        "1.a3_.1"
      ],
      [
        "0.b2_.1",
        "1.a2_.1",
        "1.a4_.1"
      ],
      [
        "0.b2_.1",
        "1.a3_.1",
        "1.xx.1"
      ],
      [
        "0.b2_.1",
        "1.a4_.1",
        "1.xx.1"
      ],
      [
        "0.b3.1",
        "0.xx.1",
        "1.b2.1"
      ],
      [
        "0.b3.1",
        "0.xx.1",
        "1.b3.1"
      ],
      [
        "0.b3.1",
        "0.xx.1",
        "1.b4.1"
      ],
      [
        "0.b3.1",
        "0.xx.1",
        "x2.1"
      ],
      [
        "0.b3.1",
        "0.xx.1",
        "x3.1"
      ],
      [
        "0.b3.1",
        "1.b2.1",
        "1.b3.1"
      ],
      [
        "0.b3.1",
        "1.b2.1",
        "1.b4.1"
      ],
      [
        "0.b3.1",
        "1.b3.1",
        "1.xx.1"
      ],
      [
        "0.b3.1",
        "1.b3.1",
        "x2.1"
      ],
      [
        "0.b3.1",
        "1.b4.1",
        "1.xx.1"
      ],
      [
        "0.b3.1",
        "1.b4.1",
        "x3.1"
      ],
      [
        "0.b3.1",
        "1.xx.1",
        "x2.1"
      ],
      [
        "0.b3.1",
        "1.xx.1",
        "x3.1"
      ],
      [
        "0.b3.1",
        "x2.1",
        "x3.1"
      ],
      [
        "0.b3_.1",
        "0.xx.1",
        "1.a2_.1"
      ],
      [
        "0.b3_.1",
        "0.xx.1",
        "1.a3_.1"
      ],
      [
        "0.b3_.1",
        "0.xx.1",
        "1.a4_.1"
      ],
      [
        "0.b3_.1",
        "0.xx.1",
        "x5.1"
      ],
      [
        "0.b3_.1",
        "0.xx.1",
        "x6.1"
      ],
      [
        "0.b3_.1",
        "1.a2_.1",
        "1.a3_.1"
      ],
      [
        "0.b3_.1",
        "1.a2_.1",
        "1.a4_.1"
      ],
      [
        "0.b3_.1",
        "1.a3_.1",
        "1.xx.1"
      ],
      [
        "0.b3_.1",
        "1.a3_.1",
        "x5.1"
      ],
      [
        "0.b3_.1",
        "1.a4_.1",
        "1.xx.1"
      ],
      [
        "0.b3_.1",
        "1.a4_.1",
        "x6.1"
      ],
      [
        "0.b3_.1",
        "1.xx.1",
        "x5.1"
      ],
      [
        "0.b3_.1",
        "1.xx.1",
        "x6.1"
      ],
      [
        "0.b3_.1",
        "x5.1",
        "x6.1"
      ],
      [
        "0.b4.1",
        "0.xx.1",
        "1.b2.1"
      ],
      [
        "0.b4.1",
        "0.xx.1",
        "1.b3.1"
      ],
      [
        "0.b4.1",
        "0.xx.1",
        "1.b4.1"
      ],
      [
        "0.b4.1",
        "0.xx.1",
        "x5.1"
      ],
      [
        "0.b4.1",
        "0.xx.1",
        "x6.1"
      ],
      [
        "0.b4.1",
        "1.b2.1",
        "1.b3.1"
      ],
      [
        "0.b4.1",
        "1.b2.1",
        "1.b4.1"
      ],
      [
        "0.b4.1",
        "1.b3.1",
        "1.xx.1"
      ],
      [
        "0.b4.1",
        "1.b3.1",
        "x5.1"
      ],
      [
        "0.b4.1",
        "1.b4.1",
        "1.xx.1"
      ],
      [
        "0.b4.1",
        "1.b4.1",
        "x6.1"
      ],
      [
        "0.b4.1",
        "1.xx.1",
        "x5.1"
      ],
      [
        "0.b4.1",
        "1.xx.1",
        "x6.1"
      ],
      [
        "0.b4.1",
        "x5.1",
        "x6.1"
      ],
      [
        "0.b4_.1",
        "0.xx.1",
        "1.a2_.1"
      ],
      [
        "0.b4_.1",
        "0.xx.1",
        "1.a3_.1"
      ],
      [
        "0.b4_.1",
        "0.xx.1",
        "1.a4_.1"
      ],
      [
        "0.b4_.1",
        "0.xx.1",
        "x1.1"
      ],
      [
        "0.b4_.1",
        "0.xx.1",
        "x4.1"
      ],
      [
        "0.b4_.1",
        "1.a2_.1",
        "1.a3_.1"
      ],
      [
        "0.b4_.1",
        "1.a2_.1",
        "1.a4_.1"
      ],
      [
        "0.b4_.1",
        "1.a3_.1",
        "1.xx.1"
      ],
      [
        "0.b4_.1",
        "1.a3_.1",
        "x1.1"
      ],
      [
        "0.b4_.1",
        "1.a4_.1",
        "1.xx.1"
      ],
      [
        "0.b4_.1",
        "1.a4_.1",
        "x4.1"
      ],
      [
        "0.b4_.1",
        "1.xx.1",
        "x1.1"
      ],
      [
        "0.b4_.1",
        "1.xx.1",
        "x4.1"
      ],
      [
        "0.b4_.1",
        "x1.1",
        "x4.1"
      ],
      [
        "0.xx.1",
        "1.a2.1",
        "1.a3.1"
      ],
      [
        "0.xx.1",
        "1.a2.1",
        "1.a4.1"
      ],
      [
        "0.xx.1",
        "1.a2_.1",
        "1.a3_.1"
      ],
      [
        "0.xx.1",
        "1.a2_.1",
        "1.a4_.1"
      ],
      [
        "0.xx.1",
        "1.a3.1",
        "x1.1"
      ],
      [
        "0.xx.1",
        "1.a3.1",
        "x4.1"
      ],
      [
        "0.xx.1",
        "1.a3_.1",
        "x1.1"
      ],
      [
        "0.xx.1",
        "1.a3_.1",
        "x5.1"
      ],
      [
        "0.xx.1",
        "1.a4.1",
        "x2.1"
      ],
      [
        "0.xx.1",
        "1.a4.1",
        "x3.1"
      ],
      [
        "0.xx.1",
        "1.a4_.1",
        "x4.1"
      ],
      [
        "0.xx.1",
        "1.a4_.1",
        "x6.1"
      ],
      [
        "0.xx.1",
        "1.b2.1",
        "1.b3.1"
      ],
      [
        "0.xx.1",
        "1.b2.1",
        "1.b4.1"
      ],
      [
        "0.xx.1",
        "1.b3.1",
        "x2.1"
      ],
      [
        "0.xx.1",
        "1.b3.1",
        "x5.1"
      ],
      [
        "0.xx.1",
        "1.b4.1",
        "x3.1"
      ],
      [
        "0.xx.1",
        "1.b4.1",
        "x6.1"
      ],
      [
        "0.xx.1",
        "x1.1",
        "x2.1"
      ],
      [
        "0.xx.1",
        "x1.1",
        "x4.1"
      ],
      [
        "0.xx.1",
        "x1.1",
        "x5.1"
      ],
      [
        "0.xx.1",
        "x2.1",
        "x3.1"
      ],
      [
        "0.xx.1",
        "x2.1",
        "x5.1"
      ],
      [
        "0.xx.1",
        "x3.1",
        "x4.1"
      ],
      [
        "0.xx.1",
        "x3.1",
        "x6.1"
      ],
      [
        "0.xx.1",
        "x4.1",
        "x6.1"
      ],
      [
        "0.xx.1",
        "x5.1",
        "x6.1"
      ],
      [
        "1.a3.1",
        "1.xx.1",
        "x1.1"
      ],
      [
        "1.a3.1",
        "1.xx.1",
        "x4.1"
      ],
      [
        "1.a3.1",
        "x1.1",
        "x4.1"
      ],
      [
        "1.a3_.1",
        "1.xx.1",
        "x1.1"
      ],
      [
        "1.a3_.1",
        "1.xx.1",
        "x5.1"
      ],
      [
        "1.a3_.1",
        "x1.1",
        "x5.1"
      ],
      [
        "1.a4.1",
        "1.xx.1",
        "x2.1"
      ],
      [
        "1.a4.1",
        "1.xx.1",
        "x3.1"
      ],
      [
        "1.a4.1",
        "x2.1",
        "x3.1"
      ],
      [
        "1.a4_.1",
        "1.xx.1",
        "x4.1"
      ],
      [
        "1.a4_.1",
        "1.xx.1",
        "x6.1"
      ],
      [
        "1.a4_.1",
        "x4.1",
        "x6.1"
      ],
      [
        "1.b3.1",
        "1.xx.1",
        "x2.1"
      ],
      [
        "1.b3.1",
        "1.xx.1",
        "x5.1"
      ],
      [
        "1.b3.1",
        "x2.1",
        "x5.1"
      ],
      [
        "1.b4.1",
        "1.xx.1",
        "x3.1"
      ],
      [
        "1.b4.1",
        "1.xx.1",
        "x6.1"
      ],
      [
        "1.b4.1",
        "x3.1",
        "x6.1"
      ],
      [
        "1.xx.1",
        "x1.1",
        "x2.1"
      ],
      [
        "1.xx.1",
        "x1.1",
        "x4.1"
      ],
      [
        "1.xx.1",
        "x1.1",
        "x5.1"
      ],
      [
        "1.xx.1",
        "x2.1",
        "x3.1"
      ],
      [
        "1.xx.1",
        "x2.1",
        "x5.1"
      ],
      [
        "1.xx.1",
        "x3.1",
        "x4.1"
      ],
      [
        "1.xx.1",
        "x3.1",
        "x6.1"
      ],
      [
        "1.xx.1",
        "x4.1",
        "x6.1"
      ],
      [
        "1.xx.1",
        "x5.1",
        "x6.1"
      ],
      [
        "x1.1",
        "x2.1",
        "x5.1"
      ],
      [
        "x3.1",
        "x4.1",
        "x6.1"
      ]
    ]
  },
  "certificate": {
    "target_local_degree": 3,
    "link_degree": 2,
    "gram_dimension": 176,
    "boundary_composition_exact_zero": true,
    "prime": 1000003,
    "determinant_mod_prime": 797443,
    "rank_mod_prime": 176,
    "integer_gram_infinity_norm": 14,
    "integer_gram_sha256": "caf2101ae1790b6f1b6720941c984ad77e04fb835c988bd69870f56fa63a48f7",
    "rational_lower_bound_for_unscaled_pair_singular_value": {
      "numerator": 1,
      "denominator": "5230392486507157795079080170437529358447914267612753228445662703798527415216547216457898032865482089499033072947578764235237217807626177757092964391537213962877943305163209241659098450659326805185396736"
    },
    "proof": "The nonzero determinant modulo a prime implies a nonzero integer determinant. The Gram matrix is positive definite. Its eigenvalues are at most the infinity norm, so its least eigenvalue is at least that bound to power -(dimension-1).",
    "weighted_consequence": "For binary weights, the projected central-bulk pair on degree 3 equals lambda times this link pair, up to orientation signs."
  },
  "topology_certificate": {
    "ordinary_betti_over_Q": {
      "0": 1,
      "1": 0,
      "2": 0,
      "3": 3,
      "4": 0,
      "5": 0
    },
    "boundary_compositions_exact_zero": true,
    "boundary_ranks": {
      "1": {
        "rank_mod_prime": 40,
        "rational_rank_upper_bound": 40
      },
      "2": {
        "rank_mod_prime": 282,
        "rational_rank_upper_bound": 282
      },
      "3": {
        "rank_mod_prime": 632,
        "rational_rank_upper_bound": 632
      },
      "4": {
        "rank_mod_prime": 447,
        "rational_rank_upper_bound": 447
      },
      "5": {
        "rank_mod_prime": 30,
        "rational_rank_upper_bound": 30
      }
    },
    "rank_proof": "Rational ranks are at least ranks modulo the prime. Each rank is at most either adjacent chain dimension minus the adjacent rank. The recorded lower and upper bounds agree.",
    "three_survivors_independent_mod_boundaries": true,
    "survivor_coefficient_columns_00_01_10_11": [
      [
        1,
        0,
        0
      ],
      [
        0,
        0,
        1
      ],
      [
        0,
        1,
        0
      ],
      [
        1,
        -1,
        0
      ]
    ],
    "survivor_proof": "The boundary rank over Q is certified exactly. Appending the three cycle columns increases rank by three modulo the prime, hence also over Q.",
    "exact_filling_denominator": 1,
    "exact_filling_chain": [
      {
        "simplex": [
          "0.a2",
          "0.a2.1",
          "0.a3.1",
          "1.a2.1",
          "1.a3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2",
          "0.a2.1",
          "0.a3.1",
          "1.a2.1",
          "1.a4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2",
          "0.a2.1",
          "0.a3.1",
          "1.a3.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2",
          "0.a2.1",
          "0.a3.1",
          "1.a4.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2",
          "0.a2.1",
          "0.a4.1",
          "1.a2.1",
          "1.a3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2",
          "0.a2.1",
          "0.a4.1",
          "1.a2.1",
          "1.a4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2",
          "0.a2.1",
          "0.a4.1",
          "1.a3.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2",
          "0.a2.1",
          "0.a4.1",
          "1.a4.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2",
          "0.a3",
          "0.a3.1",
          "1.a2.1",
          "1.a3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2",
          "0.a3",
          "0.a3.1",
          "1.a2.1",
          "1.a4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2",
          "0.a3",
          "0.a3.1",
          "1.a3.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2",
          "0.a3",
          "0.a3.1",
          "1.a4.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2",
          "0.a3",
          "1.a2",
          "1.a2.1",
          "1.a3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2",
          "0.a3",
          "1.a2",
          "1.a2.1",
          "1.a4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2",
          "0.a3",
          "1.a2",
          "1.a3",
          "1.a3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2",
          "0.a3",
          "1.a2",
          "1.a4",
          "1.a4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2",
          "0.a3",
          "1.a3",
          "1.a3.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2",
          "0.a3",
          "1.a3",
          "1.xx",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2",
          "0.a3",
          "1.a4",
          "1.a4.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2",
          "0.a3",
          "1.a4",
          "1.xx",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2",
          "0.a4",
          "0.a4.1",
          "1.a2.1",
          "1.a3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2",
          "0.a4",
          "0.a4.1",
          "1.a2.1",
          "1.a4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2",
          "0.a4",
          "0.a4.1",
          "1.a3.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2",
          "0.a4",
          "0.a4.1",
          "1.a4.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2",
          "0.a4",
          "1.a2",
          "1.a2.1",
          "1.a3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2",
          "0.a4",
          "1.a2",
          "1.a2.1",
          "1.a4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2",
          "0.a4",
          "1.a2",
          "1.a3",
          "1.a3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2",
          "0.a4",
          "1.a2",
          "1.a4",
          "1.a4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2",
          "0.a4",
          "1.a3",
          "1.a3.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2",
          "0.a4",
          "1.a3",
          "1.xx",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2",
          "0.a4",
          "1.a4",
          "1.a4.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2",
          "0.a4",
          "1.a4",
          "1.xx",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2.1",
          "0.a3.1",
          "1.a2.1",
          "1.a3.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2.1",
          "0.a3.1",
          "1.a2.1",
          "1.a4.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2.1",
          "0.a3.1",
          "1.a3.1",
          "1.xx.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2.1",
          "0.a3.1",
          "1.a4.1",
          "1.xx.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2.1",
          "0.a4.1",
          "1.a2.1",
          "1.a3.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2.1",
          "0.a4.1",
          "1.a2.1",
          "1.a4.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a2.1",
          "0.a4.1",
          "1.a3.1",
          "1.xx.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a2.1",
          "0.a4.1",
          "1.a4.1",
          "1.xx.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3",
          "0.a3.1",
          "0.xx.1",
          "1.a2.1",
          "1.a3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a3",
          "0.a3.1",
          "0.xx.1",
          "1.a2.1",
          "1.a4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3",
          "0.a3.1",
          "0.xx.1",
          "1.a3.1",
          "x1.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a3",
          "0.a3.1",
          "0.xx.1",
          "1.a4.1",
          "x2.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3",
          "0.a3.1",
          "0.xx.1",
          "x1.1",
          "x2.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a3",
          "0.a3.1",
          "1.a3.1",
          "1.xx.1",
          "x1.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a3",
          "0.a3.1",
          "1.a4.1",
          "1.xx.1",
          "x2.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3",
          "0.a3.1",
          "1.xx.1",
          "x1.1",
          "x2.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3",
          "0.xx",
          "0.xx.1",
          "1.a2.1",
          "1.a3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3",
          "0.xx",
          "0.xx.1",
          "1.a2.1",
          "1.a4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a3",
          "0.xx",
          "0.xx.1",
          "1.a3.1",
          "x1.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3",
          "0.xx",
          "0.xx.1",
          "1.a4.1",
          "x2.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a3",
          "0.xx",
          "0.xx.1",
          "x1.1",
          "x2.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3",
          "0.xx",
          "1.a2",
          "1.a2.1",
          "1.a3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a3",
          "0.xx",
          "1.a2",
          "1.a2.1",
          "1.a4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3",
          "0.xx",
          "1.a2",
          "1.a3",
          "1.a3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3",
          "0.xx",
          "1.a2",
          "1.a4",
          "1.a4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a3",
          "0.xx",
          "1.a3",
          "1.a3.1",
          "x1.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a3",
          "0.xx",
          "1.a3",
          "1.xx",
          "x1.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3",
          "0.xx",
          "1.a4",
          "1.a4.1",
          "x2.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3",
          "0.xx",
          "1.a4",
          "1.xx",
          "x2.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a3",
          "0.xx",
          "1.xx",
          "x1.1",
          "x2.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a3",
          "1.a3",
          "1.a3.1",
          "1.xx.1",
          "x1.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3",
          "1.a3",
          "1.xx",
          "1.xx.1",
          "x1.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a3",
          "1.a4",
          "1.a4.1",
          "1.xx.1",
          "x2.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a3",
          "1.a4",
          "1.xx",
          "1.xx.1",
          "x2.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3",
          "1.xx",
          "1.xx.1",
          "x1.1",
          "x2.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a3.1",
          "0.xx.1",
          "1.a2.1",
          "1.a3.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3.1",
          "0.xx.1",
          "1.a2.1",
          "1.a4.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a3.1",
          "0.xx.1",
          "1.a3.1",
          "v0",
          "x1.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a3.1",
          "0.xx.1",
          "1.a4.1",
          "v0",
          "x2.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3.1",
          "0.xx.1",
          "v0",
          "x1.1",
          "x2.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3.1",
          "1.a3.1",
          "1.xx.1",
          "v0",
          "x1.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a3.1",
          "1.a4.1",
          "1.xx.1",
          "v0",
          "x2.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a3.1",
          "1.xx.1",
          "v0",
          "x1.1",
          "x2.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4",
          "0.a4.1",
          "0.xx.1",
          "1.a2.1",
          "1.a3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a4",
          "0.a4.1",
          "0.xx.1",
          "1.a2.1",
          "1.a4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4",
          "0.a4.1",
          "0.xx.1",
          "1.a3.1",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a4",
          "0.a4.1",
          "0.xx.1",
          "1.a4.1",
          "x3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4",
          "0.a4.1",
          "0.xx.1",
          "x3.1",
          "x4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4",
          "0.a4.1",
          "1.a3.1",
          "1.xx.1",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a4",
          "0.a4.1",
          "1.a4.1",
          "1.xx.1",
          "x3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4",
          "0.a4.1",
          "1.xx.1",
          "x3.1",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a4",
          "0.xx",
          "0.xx.1",
          "1.a2.1",
          "1.a3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4",
          "0.xx",
          "0.xx.1",
          "1.a2.1",
          "1.a4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a4",
          "0.xx",
          "0.xx.1",
          "1.a3.1",
          "x4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4",
          "0.xx",
          "0.xx.1",
          "1.a4.1",
          "x3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a4",
          "0.xx",
          "0.xx.1",
          "x3.1",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a4",
          "0.xx",
          "1.a2",
          "1.a2.1",
          "1.a3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a4",
          "0.xx",
          "1.a2",
          "1.a2.1",
          "1.a4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4",
          "0.xx",
          "1.a2",
          "1.a3",
          "1.a3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4",
          "0.xx",
          "1.a2",
          "1.a4",
          "1.a4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a4",
          "0.xx",
          "1.a3",
          "1.a3.1",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a4",
          "0.xx",
          "1.a3",
          "1.xx",
          "x4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4",
          "0.xx",
          "1.a4",
          "1.a4.1",
          "x3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4",
          "0.xx",
          "1.a4",
          "1.xx",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a4",
          "0.xx",
          "1.a4",
          "x3.1",
          "x4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4",
          "1.a3",
          "1.a3.1",
          "1.xx.1",
          "x4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4",
          "1.a3",
          "1.xx",
          "1.xx.1",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a4",
          "1.a4",
          "1.a4.1",
          "1.xx.1",
          "x3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a4",
          "1.a4",
          "1.xx",
          "1.xx.1",
          "x4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4",
          "1.a4",
          "1.xx.1",
          "x3.1",
          "x4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4.1",
          "0.xx.1",
          "1.a2.1",
          "1.a3.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4.1",
          "0.xx.1",
          "1.a2.1",
          "1.a4.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a4.1",
          "0.xx.1",
          "1.a3.1",
          "v0",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a4.1",
          "0.xx.1",
          "1.a4.1",
          "v0",
          "x3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4.1",
          "0.xx.1",
          "v0",
          "x3.1",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a4.1",
          "1.a3.1",
          "1.xx.1",
          "v0",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.a4.1",
          "1.a4.1",
          "1.xx.1",
          "v0",
          "x3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.a4.1",
          "1.xx.1",
          "v0",
          "x3.1",
          "x4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b2.1",
          "0.b3.1",
          "1.b2.1",
          "1.b3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b2.1",
          "0.b3.1",
          "1.b2.1",
          "1.b4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b2.1",
          "0.b3.1",
          "1.b3.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b2.1",
          "0.b3.1",
          "1.b4.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b2.1",
          "0.b4.1",
          "1.b2.1",
          "1.b3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b2.1",
          "0.b4.1",
          "1.b2.1",
          "1.b4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b2.1",
          "0.b4.1",
          "1.b3.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b2.1",
          "0.b4.1",
          "1.b4.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b2_.1",
          "0.b3_.1",
          "1.a2_.1",
          "1.a3_.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b2_.1",
          "0.b3_.1",
          "1.a2_.1",
          "1.a4_.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b2_.1",
          "0.b3_.1",
          "1.a3_.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b2_.1",
          "0.b3_.1",
          "1.a4_.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b2_.1",
          "0.b4_.1",
          "1.a2_.1",
          "1.a3_.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b2_.1",
          "0.b4_.1",
          "1.a2_.1",
          "1.a4_.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b2_.1",
          "0.b4_.1",
          "1.a3_.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b2_.1",
          "0.b4_.1",
          "1.a4_.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "0.b3.1",
          "1.b2.1",
          "1.b3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "0.b3.1",
          "1.b2.1",
          "1.b4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "0.b3.1",
          "1.b3.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "0.b3.1",
          "1.b4.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "0.b3_.1",
          "1.a2_.1",
          "1.a3_.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "0.b3_.1",
          "1.a2_.1",
          "1.a4_.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "0.b3_.1",
          "1.a3_.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "0.b3_.1",
          "1.a4_.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "1.a2",
          "1.a2_.1",
          "1.a3_.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "1.a2",
          "1.a2_.1",
          "1.a4_.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "1.a2",
          "1.a3",
          "1.a3_.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "1.a2",
          "1.a4",
          "1.a4_.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "1.a3",
          "1.a3_.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "1.a3",
          "1.xx",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "1.a4",
          "1.a4_.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "1.a4",
          "1.xx",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "1.b2",
          "1.b2.1",
          "1.b3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "1.b2",
          "1.b2.1",
          "1.b4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "1.b2",
          "1.b3",
          "1.b3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "1.b2",
          "1.b4",
          "1.b4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "1.b3",
          "1.b3.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "1.b3",
          "1.xx",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "1.b4",
          "1.b4.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b3",
          "1.b4",
          "1.xx",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "0.b4.1",
          "1.b2.1",
          "1.b3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "0.b4.1",
          "1.b2.1",
          "1.b4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "0.b4.1",
          "1.b3.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "0.b4.1",
          "1.b4.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "0.b4_.1",
          "1.a2_.1",
          "1.a3_.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "0.b4_.1",
          "1.a2_.1",
          "1.a4_.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "0.b4_.1",
          "1.a3_.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "0.b4_.1",
          "1.a4_.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "1.a2",
          "1.a2_.1",
          "1.a3_.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "1.a2",
          "1.a2_.1",
          "1.a4_.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "1.a2",
          "1.a3",
          "1.a3_.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "1.a2",
          "1.a4",
          "1.a4_.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "1.a3",
          "1.a3_.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "1.a3",
          "1.xx",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "1.a4",
          "1.a4_.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "1.a4",
          "1.xx",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "1.b2",
          "1.b2.1",
          "1.b3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "1.b2",
          "1.b2.1",
          "1.b4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "1.b2",
          "1.b3",
          "1.b3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "1.b2",
          "1.b4",
          "1.b4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "1.b3",
          "1.b3.1",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "1.b3",
          "1.xx",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "1.b4",
          "1.b4.1",
          "1.xx.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2",
          "0.b4",
          "1.b4",
          "1.xx",
          "1.xx.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2.1",
          "0.b3.1",
          "1.b2.1",
          "1.b3.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2.1",
          "0.b3.1",
          "1.b2.1",
          "1.b4.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2.1",
          "0.b3.1",
          "1.b3.1",
          "1.xx.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2.1",
          "0.b3.1",
          "1.b4.1",
          "1.xx.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2.1",
          "0.b4.1",
          "1.b2.1",
          "1.b3.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2.1",
          "0.b4.1",
          "1.b2.1",
          "1.b4.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2.1",
          "0.b4.1",
          "1.b3.1",
          "1.xx.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2.1",
          "0.b4.1",
          "1.b4.1",
          "1.xx.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2_.1",
          "0.b3_.1",
          "1.a2_.1",
          "1.a3_.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2_.1",
          "0.b3_.1",
          "1.a2_.1",
          "1.a4_.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2_.1",
          "0.b3_.1",
          "1.a3_.1",
          "1.xx.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2_.1",
          "0.b3_.1",
          "1.a4_.1",
          "1.xx.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2_.1",
          "0.b4_.1",
          "1.a2_.1",
          "1.a3_.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2_.1",
          "0.b4_.1",
          "1.a2_.1",
          "1.a4_.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b2_.1",
          "0.b4_.1",
          "1.a3_.1",
          "1.xx.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b2_.1",
          "0.b4_.1",
          "1.a4_.1",
          "1.xx.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.b3.1",
          "0.xx.1",
          "1.b2.1",
          "1.b3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.b3.1",
          "0.xx.1",
          "1.b2.1",
          "1.b4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.b3.1",
          "0.xx.1",
          "1.b3.1",
          "x2.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.b3.1",
          "0.xx.1",
          "1.b4.1",
          "x3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.b3.1",
          "0.xx.1",
          "x2.1",
          "x3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.b3.1",
          "1.b3.1",
          "1.xx.1",
          "x2.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.b3.1",
          "1.b4.1",
          "1.xx.1",
          "x3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.b3.1",
          "1.xx.1",
          "x2.1",
          "x3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.b3_.1",
          "0.xx.1",
          "1.a2_.1",
          "1.a3_.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.b3_.1",
          "0.xx.1",
          "1.a2_.1",
          "1.a4_.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.b3_.1",
          "0.xx.1",
          "1.a3_.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.b3_.1",
          "0.xx.1",
          "1.a4_.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.b3_.1",
          "0.xx.1",
          "x5.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.b3_.1",
          "1.a3_.1",
          "1.xx.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.b3_.1",
          "1.a4_.1",
          "1.xx.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.b3_.1",
          "1.xx.1",
          "x5.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "0.xx.1",
          "1.a2_.1",
          "1.a3_.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "0.xx.1",
          "1.a2_.1",
          "1.a4_.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "0.xx.1",
          "1.a3_.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "0.xx.1",
          "1.a4_.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "0.xx.1",
          "1.b2.1",
          "1.b3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "0.xx.1",
          "1.b2.1",
          "1.b4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "0.xx.1",
          "1.b3.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "0.xx.1",
          "1.b4.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "0.xx.1",
          "x2.1",
          "x3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "0.xx.1",
          "x2.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "0.xx.1",
          "x3.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "0.xx.1",
          "x5.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.a2",
          "1.a2_.1",
          "1.a3_.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.a2",
          "1.a2_.1",
          "1.a4_.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.a2",
          "1.a3",
          "1.a3_.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.a2",
          "1.a4",
          "1.a4_.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.a3",
          "1.a3_.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.a3",
          "1.xx",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.a4",
          "1.a4_.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.a4",
          "1.xx",
          "x2.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.a4",
          "x2.1",
          "x3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.a4",
          "x3.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.b2",
          "1.b2.1",
          "1.b3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.b2",
          "1.b2.1",
          "1.b4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.b2",
          "1.b3",
          "1.b3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.b2",
          "1.b4",
          "1.b4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.b3",
          "1.b3.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.b3",
          "1.xx",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.b4",
          "1.b4.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.b4",
          "1.xx",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.xx",
          "x2.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx",
          "1.xx",
          "x5.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx.1",
          "1.b3.1",
          "x2.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "0.xx.1",
          "1.b4.1",
          "x3.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "1.a3",
          "1.a3_.1",
          "1.xx.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "1.a3",
          "1.xx",
          "1.xx.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "1.a4",
          "1.a4_.1",
          "1.xx.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "1.a4",
          "1.xx",
          "1.xx.1",
          "x2.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "1.a4",
          "1.xx.1",
          "x2.1",
          "x3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "1.a4",
          "1.xx.1",
          "x3.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "1.b3",
          "1.b3.1",
          "1.xx.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "1.b3",
          "1.xx",
          "1.xx.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "1.b3.1",
          "1.xx.1",
          "x2.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "1.b4",
          "1.b4.1",
          "1.xx.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3",
          "1.b4",
          "1.xx",
          "1.xx.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "1.b4.1",
          "1.xx.1",
          "x3.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "1.xx",
          "1.xx.1",
          "x2.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3",
          "1.xx",
          "1.xx.1",
          "x5.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3.1",
          "0.xx.1",
          "1.b2.1",
          "1.b3.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3.1",
          "0.xx.1",
          "1.b2.1",
          "1.b4.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3.1",
          "0.xx.1",
          "1.b3.1",
          "v0",
          "x2.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3.1",
          "0.xx.1",
          "1.b4.1",
          "v0",
          "x3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3.1",
          "0.xx.1",
          "v0",
          "x2.1",
          "x3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3.1",
          "1.b3.1",
          "1.xx.1",
          "v0",
          "x2.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3.1",
          "1.b4.1",
          "1.xx.1",
          "v0",
          "x3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3.1",
          "1.xx.1",
          "v0",
          "x2.1",
          "x3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3_.1",
          "0.xx.1",
          "1.a2_.1",
          "1.a3_.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3_.1",
          "0.xx.1",
          "1.a2_.1",
          "1.a4_.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3_.1",
          "0.xx.1",
          "1.a3_.1",
          "v0",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3_.1",
          "0.xx.1",
          "1.a4_.1",
          "v0",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3_.1",
          "0.xx.1",
          "v0",
          "x5.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3_.1",
          "1.a3_.1",
          "1.xx.1",
          "v0",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b3_.1",
          "1.a4_.1",
          "1.xx.1",
          "v0",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b3_.1",
          "1.xx.1",
          "v0",
          "x5.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.b4.1",
          "0.xx.1",
          "1.b2.1",
          "1.b3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.b4.1",
          "0.xx.1",
          "1.b2.1",
          "1.b4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.b4.1",
          "0.xx.1",
          "1.b3.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.b4.1",
          "0.xx.1",
          "1.b4.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.b4.1",
          "0.xx.1",
          "x5.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.b4.1",
          "1.b3.1",
          "1.xx.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.b4.1",
          "1.b4.1",
          "1.xx.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.b4.1",
          "1.xx.1",
          "x5.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.b4_.1",
          "0.xx.1",
          "1.a2_.1",
          "1.a3_.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.b4_.1",
          "0.xx.1",
          "1.a2_.1",
          "1.a4_.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.b4_.1",
          "0.xx.1",
          "1.a3_.1",
          "x1.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.b4_.1",
          "0.xx.1",
          "1.a4_.1",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.b4_.1",
          "0.xx.1",
          "x1.1",
          "x4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.b4_.1",
          "1.a3_.1",
          "1.xx.1",
          "x1.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.b4_.1",
          "1.a4_.1",
          "1.xx.1",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.b4_.1",
          "1.xx.1",
          "x1.1",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "0.xx.1",
          "1.a2_.1",
          "1.a3_.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "0.xx.1",
          "1.a2_.1",
          "1.a4_.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "0.xx.1",
          "1.a3_.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "0.xx.1",
          "1.a4_.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "0.xx.1",
          "1.b2.1",
          "1.b3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "0.xx.1",
          "1.b2.1",
          "1.b4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "0.xx.1",
          "1.b3.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "0.xx.1",
          "1.b4.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "0.xx.1",
          "x1.1",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "0.xx.1",
          "x1.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "0.xx.1",
          "x4.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "0.xx.1",
          "x5.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.a2",
          "1.a2_.1",
          "1.a3_.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.a2",
          "1.a2_.1",
          "1.a4_.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.a2",
          "1.a3",
          "1.a3_.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.a2",
          "1.a4",
          "1.a4_.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.a3",
          "1.a3_.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.a3",
          "1.xx",
          "x1.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.a3",
          "1.xx",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.a3",
          "1.xx",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.a3",
          "x1.1",
          "x4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.a4",
          "1.a4_.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.a4",
          "1.xx",
          "x4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.a4",
          "x4.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.b2",
          "1.b2.1",
          "1.b3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.b2",
          "1.b2.1",
          "1.b4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.b2",
          "1.b3",
          "1.b3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.b2",
          "1.b4",
          "1.b4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.b3",
          "1.b3.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.b3",
          "1.xx",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.b4",
          "1.b4.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.b4",
          "1.xx",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.xx",
          "x1.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx",
          "1.xx",
          "x5.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx.1",
          "1.a3_.1",
          "x1.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "0.xx.1",
          "1.a4_.1",
          "x4.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "1.a3",
          "1.a3_.1",
          "1.xx.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "1.a3",
          "1.xx",
          "1.xx.1",
          "x1.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "1.a3",
          "1.xx",
          "1.xx.1",
          "x4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "1.a3",
          "1.xx",
          "1.xx.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "1.a3",
          "1.xx.1",
          "x1.1",
          "x4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "1.a3_.1",
          "1.xx.1",
          "x1.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "1.a4",
          "1.a4_.1",
          "1.xx.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "1.a4",
          "1.xx",
          "1.xx.1",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "1.a4",
          "1.xx.1",
          "x4.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "1.a4_.1",
          "1.xx.1",
          "x4.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "1.b3",
          "1.b3.1",
          "1.xx.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "1.b3",
          "1.xx",
          "1.xx.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "1.b4",
          "1.b4.1",
          "1.xx.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4",
          "1.b4",
          "1.xx",
          "1.xx.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "1.xx",
          "1.xx.1",
          "x1.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4",
          "1.xx",
          "1.xx.1",
          "x5.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4.1",
          "0.xx.1",
          "1.b2.1",
          "1.b3.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4.1",
          "0.xx.1",
          "1.b2.1",
          "1.b4.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4.1",
          "0.xx.1",
          "1.b3.1",
          "v0",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4.1",
          "0.xx.1",
          "1.b4.1",
          "v0",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4.1",
          "0.xx.1",
          "v0",
          "x5.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4.1",
          "1.b3.1",
          "1.xx.1",
          "v0",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4.1",
          "1.b4.1",
          "1.xx.1",
          "v0",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4.1",
          "1.xx.1",
          "v0",
          "x5.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4_.1",
          "0.xx.1",
          "1.a2_.1",
          "1.a3_.1",
          "v0"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4_.1",
          "0.xx.1",
          "1.a2_.1",
          "1.a4_.1",
          "v0"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4_.1",
          "0.xx.1",
          "1.a3_.1",
          "v0",
          "x1.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4_.1",
          "0.xx.1",
          "1.a4_.1",
          "v0",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4_.1",
          "0.xx.1",
          "v0",
          "x1.1",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4_.1",
          "1.a3_.1",
          "1.xx.1",
          "v0",
          "x1.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.b4_.1",
          "1.a4_.1",
          "1.xx.1",
          "v0",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.b4_.1",
          "1.xx.1",
          "v0",
          "x1.1",
          "x4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.xx",
          "0.xx.1",
          "1.a3.1",
          "x1.1",
          "x4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.xx",
          "0.xx.1",
          "1.a4.1",
          "x2.1",
          "x3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.xx",
          "0.xx.1",
          "x1.1",
          "x2.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.xx",
          "0.xx.1",
          "x3.1",
          "x4.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.xx",
          "1.a3",
          "1.a3.1",
          "x1.1",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.xx",
          "1.a4",
          "1.a4.1",
          "x2.1",
          "x3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.xx",
          "1.a4",
          "x3.1",
          "x4.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.xx",
          "1.xx",
          "x1.1",
          "x2.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.xx.1",
          "1.a3.1",
          "v0",
          "x1.1",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.xx.1",
          "1.a3_.1",
          "v0",
          "x1.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.xx.1",
          "1.a4.1",
          "v0",
          "x2.1",
          "x3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.xx.1",
          "1.a4_.1",
          "v0",
          "x4.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.xx.1",
          "1.b3.1",
          "v0",
          "x2.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.xx.1",
          "1.b4.1",
          "v0",
          "x3.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "0.xx.1",
          "v0",
          "x1.1",
          "x2.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "0.xx.1",
          "v0",
          "x3.1",
          "x4.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "1.a3",
          "1.a3.1",
          "1.xx.1",
          "x1.1",
          "x4.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "1.a3.1",
          "1.xx.1",
          "v0",
          "x1.1",
          "x4.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "1.a3_.1",
          "1.xx.1",
          "v0",
          "x1.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "1.a4",
          "1.a4.1",
          "1.xx.1",
          "x2.1",
          "x3.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "1.a4",
          "1.xx.1",
          "x3.1",
          "x4.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "1.a4.1",
          "1.xx.1",
          "v0",
          "x2.1",
          "x3.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "1.a4_.1",
          "1.xx.1",
          "v0",
          "x4.1",
          "x6.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "1.b3.1",
          "1.xx.1",
          "v0",
          "x2.1",
          "x5.1"
        ],
        "coefficient": -1
      },
      {
        "simplex": [
          "1.b4.1",
          "1.xx.1",
          "v0",
          "x3.1",
          "x6.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "1.xx",
          "1.xx.1",
          "x1.1",
          "x2.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "1.xx.1",
          "v0",
          "x1.1",
          "x2.1",
          "x5.1"
        ],
        "coefficient": 1
      },
      {
        "simplex": [
          "1.xx.1",
          "v0",
          "x3.1",
          "x4.1",
          "x6.1"
        ],
        "coefficient": 1
      }
    ],
    "filling_equation_verified_over_integers": true,
    "register_intersection": "Exactly the span of ket00-ket10-ket11: that cycle has an explicit rational filling and three complementary register cycles survive independently.",
    "positive_weight_extension": "Invertible diagonal weight gauge preserves homology; weight-one register coordinates preserve the exact register boundary intersection for every lambda>0."
  },
  "zero_weight_certificate": {
    "register_vertices": [
      "0.a2",
      "0.a3",
      "0.a4",
      "0.b2",
      "0.b3",
      "0.b4",
      "0.xx",
      "1.a2",
      "1.a3",
      "1.a4",
      "1.b2",
      "1.b3",
      "1.b4",
      "1.xx"
    ],
    "register_cycle_dimension": 4,
    "register_basis_gram": "16 I_4; divide each cycle by 4 for an isometry",
    "central_bulk_dimension": 176,
    "differential_pair_rank_mod_prime": 902,
    "rational_rank_upper_bound_from_known_kernel": 902,
    "kernel_exactly_register_cycles_plus_central_bulk": true,
    "projected_bulk_pair_zero_constant_term": true,
    "projected_bulk_pair_annihilates_register_cycles": true,
    "central_vertex_has_only_new_neighbors": true,
    "zero_weight_gram_infinity_norm": 12,
    "derivative_gram_infinity_norm": 15,
    "unweighted_gram_infinity_norm": 21,
    "positive_gap_proof": "For an integral PSD Gram matrix of rank r and norm at most B, its nonzero eigenvalue product is a positive integer, so the least positive eigenvalue is at least B^(-(r-1)).",
    "weighted_gap_proof": "For each boundary, partial_w=W_rows^(-1) partial_1 W_columns. The left scaling has minimum singular value at least one; a degree-k column weight is at least lambda^(k+1). Nonzero singular values therefore decrease by at most that factor. At target degree 3 this gives a whole positive Laplacian lower bound c lambda^10.",
    "not_certified": "Leading eigenvalue coefficient, optimal valuation, and guarded-palette closure are not implied by this certificate."
  },
  "not_certified": [
    "Optimal weighted lifted eigenvalue valuation or its leading coefficient",
    "Full guarded-palette closure under the new finite zero-weight criterion",
    "Complete guarded palette through locality six",
    "Full reduction or priority"
  ]
}

<!-- END INCLUDED FILE: RUDOLPH_REPRESENTATIVE_BULK_CERTIFICATE.json -->


<!-- BEGIN INCLUDED FILE: certify_representative_bulk.py -->

# Included file 6: certify_representative_bulk.py

"""Recover the source representative graph and certify its central bulk.

The upstream graph construction is GPLv2-or-later, attributed to Dorian Rudolph.
We fetch its pinned source but do not redistribute it here. Only the inspected
graph-building function definitions are evaluated; the graph shim stops before
Sage homology routines, plotting, or any top-level upstream calls execute.
Outputs are mathematical graph data and a modular certificate for an integer Gram matrix.
"""

import ast
from pathlib import Path
import hashlib
import itertools
import json
import math
from fractions import Fraction
import subprocess

import numpy as np

SOURCE_COMMIT = "30ac70e5dacdecce97c38d801c128ec3ed93a96a"
SOURCE_SHA256 = "c8918f9e037ae79796bb65640170c8e60f31883625d24348f3476f7644dcd29a"
SOURCE_PATH = "gadget_homology.py"
SOURCE_URL = (
    "https://github.com/DorianRudolph/QMA1-gateset-paper/blob/"
    + SOURCE_COMMIT + "/" + SOURCE_PATH
)


class CaptureGraph(Exception):
    def __init__(self, graph):
        self.graph = graph


class Graph:
    def __init__(self, edges=None):
        self.vertices = set()
        self.pairs = set()
        if edges is not None:
            self.add_edges(edges)

    def __iter__(self):
        return iter(sorted(self.vertices))

    def add_edges(self, edges):
        for a, b in edges:
            self.vertices.update((a, b))
            if a != b:
                self.pairs.add(tuple(sorted((a, b))))

    def edges(self, labels=False, sort_vertices=True):
        return sorted(self.pairs)

    def union(self, other):
        result = Graph()
        result.vertices = self.vertices | other.vertices
        result.pairs = self.pairs | other.pairs
        return result

    def delete_edge(self, a, b):
        self.pairs.remove(tuple(sorted((a, b))))

    def merge_vertices(self, vertices):
        target = vertices[0]
        merged = set(vertices)
        result = set()
        for a, b in self.pairs:
            a = target if a in merged else a
            b = target if b in merged else b
            if a != b:
                result.add(tuple(sorted((a, b))))
        self.vertices = (self.vertices - merged) | {target}
        self.pairs = result

    def clique_complex(self):
        raise CaptureGraph(self)


def all_cliques(graph):
    vertices = sorted(graph.vertices)
    adjacent = {v: set() for v in vertices}
    for a, b in graph.pairs:
        adjacent[a].add(b)
        adjacent[b].add(a)
    by_degree = {}

    def extend(prefix, candidates):
        for i, v in enumerate(candidates):
            simplex = prefix + (v,)
            by_degree.setdefault(len(simplex) - 1, []).append(simplex)
            extend(simplex, [w for w in candidates[i + 1:] if w in adjacent[v]])

    extend((), vertices)
    return by_degree


def boundary(cells, degree):
    rows = {s: i for i, s in enumerate(cells.get(degree - 1, []))}
    columns = cells.get(degree, [])
    matrix = np.zeros((len(rows), len(columns)), dtype=np.int64)
    for j, simplex in enumerate(columns):
        for i in range(degree + 1):
            matrix[rows[simplex[:i] + simplex[i + 1:]], j] = (-1) ** i
    return matrix


def weighted_boundary(cells, degree, weights):
    rows = {s: i for i, s in enumerate(cells.get(degree - 1, []))}
    columns = cells.get(degree, [])
    matrix = np.zeros((len(rows), len(columns)), dtype=np.int64)
    for j, simplex in enumerate(columns):
        for i, vertex in enumerate(simplex):
            matrix[rows[simplex[:i] + simplex[i + 1:]], j] = (-1) ** i * weights[vertex]
    return matrix


def det_mod_prime(matrix, prime):
    value = np.remainder(matrix, prime).copy()
    n = len(value)
    determinant = 1
    for column in range(n):
        candidates = np.flatnonzero(value[column:, column])
        if not len(candidates):
            return 0, column
        pivot = column + int(candidates[0])
        if pivot != column:
            value[[column, pivot]] = value[[pivot, column]]
            determinant = -determinant
        pivot_value = int(value[column, column])
        determinant = determinant * pivot_value % prime
        inverse = pow(pivot_value, -1, prime)
        factors = value[column + 1:, column] * inverse % prime
        value[column + 1:, column:] = (
            value[column + 1:, column:]
            - factors[:, None] * value[column, column:][None, :]
        ) % prime
    return determinant % prime, n


def echelon_mod_prime(matrix, prime, rhs=None):
    columns = matrix.shape[1]
    value = np.remainder(
        np.column_stack((matrix, rhs)) if rhs is not None else matrix, prime
    ).copy()
    pivots = []
    row = 0
    for column in range(columns):
        candidates = np.flatnonzero(value[row:, column])
        if not len(candidates):
            continue
        pivot = row + int(candidates[0])
        if pivot != row:
            value[[row, pivot]] = value[[pivot, row]]
        inverse = pow(int(value[row, column]), -1, prime)
        factors = value[row + 1:, column] * inverse % prime
        value[row + 1:, column:] = (
            value[row + 1:, column:]
            - factors[:, None] * value[row, column:][None, :]
        ) % prime
        pivots.append(column)
        row += 1
        if row == len(value):
            break
    return value, pivots


def reconstruct_rational(residue, prime):
    bound = math.isqrt(prime // 2)
    a, b, u, v = prime, int(residue), 0, 1
    while abs(b) > bound:
        quotient = a // b
        a, b, u, v = b, a - quotient * b, v, u - quotient * v
    if not v or abs(v) > bound or (b - int(residue) * v) % prime:
        raise ArithmeticError("Rational reconstruction failed")
    return Fraction(b, v)


def register_basis(cells):
    rows = {simplex: i for i, simplex in enumerate(cells[3])}

    def edges(qubit, bit):
        petal = "b" if bit else "a"
        cycle = [f"{qubit}.xx", f"{qubit}.{petal}3",
                 f"{qubit}.{petal}2", f"{qubit}.{petal}4"]
        return [(cycle[i], cycle[(i + 1) % 4]) for i in range(4)]

    basis = np.zeros((len(rows), 4), dtype=np.int64)
    for first in (0, 1):
        for second in (0, 1):
            for a, b in itertools.product(edges(0, first), edges(1, second)):
                oriented = a + b
                inversions = sum(oriented[i] > oriented[j]
                                 for i in range(4) for j in range(i + 1, 4))
                basis[rows[tuple(sorted(oriented))], 2 * first + second] += (-1) ** inversions
    return basis


def main():
    upstream = subprocess.check_output([
        "gh", "api",
        "repos/DorianRudolph/QMA1-gateset-paper/contents/"
        + SOURCE_PATH + "?ref=" + SOURCE_COMMIT,
        "-H", "Accept: application/vnd.github.raw+json",
    ])
    assert hashlib.sha256(upstream).hexdigest() == SOURCE_SHA256
    wanted = {
        "make_graph", "thicken", "fill_cycle", "join_keep_names",
        "state_00m10m11",
    }
    parsed = ast.parse(upstream.decode())
    definitions = [
        node for node in parsed.body
        if isinstance(node, ast.FunctionDef) and node.name in wanted
    ]
    assert {node.name for node in definitions} == wanted
    namespace = {
        "Graph": Graph, "itertools": itertools, "v0": "v0",
        "vertex_names": "xx, a2, a3, a4, b2, b3, b4".split(", "),
    }
    exec(compile(ast.Module(body=definitions, type_ignores=[]), SOURCE_URL, "exec"), namespace)
    try:
        namespace["state_00m10m11"]()
    except CaptureGraph as captured:
        graph = captured.graph
    else:
        raise AssertionError("Expected capture before source homology computation")

    cells = all_cliques(graph)
    central = "v0"
    neighbors = {
        b if a == central else a
        for a, b in graph.pairs if central in (a, b)
    }
    link = Graph()
    link.vertices = neighbors
    link.pairs = {e for e in graph.pairs if set(e) <= neighbors}
    link_cells = all_cliques(link)
    d2 = boundary(link_cells, 2)
    d3 = boundary(link_cells, 3)
    assert not np.any(d2 @ d3)
    gram = d2.T @ d2 + d3 @ d3.T
    dimension = gram.shape[0]
    assert dimension > 0 and gram.shape[1] == dimension
    prime = 1000003
    assert all(prime % divisor for divisor in range(2, math.isqrt(prime) + 1))
    determinant, rank = det_mod_prime(gram, prime)
    assert determinant != 0 and rank == dimension
    bound = int(np.abs(gram).sum(axis=1).max())
    # A positive integral determinant is >=1; each eigenvalue is <=bound.
    # sigma_min([d2; d3.T]) >= bound^(-(dimension-1)/2) >= bound^(-dimension).
    denominator = str(pow(bound, dimension))
    boundaries = {degree: boundary(cells, degree) for degree in range(1, max(cells) + 1)}
    for degree in range(2, max(cells) + 1):
        assert not np.any(boundaries[degree - 1] @ boundaries[degree])
    basis = register_basis(cells)
    assert np.array_equal(basis.T @ basis, 16 * np.eye(4, dtype=np.int64))
    assert not np.any(boundaries[3] @ basis)
    phi = basis @ np.array([1, 0, -1, -1], dtype=np.int64)
    survivors = basis @ np.array([[1, 0, 0], [0, 0, 1],
                                 [0, 1, 0], [1, -1, 0]], dtype=np.int64)
    echelon4, pivots4 = echelon_mod_prime(
        boundaries[4], prime, np.column_stack((phi, survivors))
    )
    ranks = {}
    for degree, matrix in boundaries.items():
        ranks[degree] = len(pivots4) if degree == 4 else len(echelon_mod_prime(matrix, prime)[1])
    exact_rank_bounds = {}
    for degree, lower in ranks.items():
        upper = min(
            len(cells[degree - 1]) - ranks.get(degree - 1, 0),
            len(cells[degree]) - ranks.get(degree + 1, 0),
        )
        assert lower == upper, (degree, lower, upper)
        exact_rank_bounds[str(degree)] = {"rank_mod_prime": lower, "rational_rank_upper_bound": upper}
    ncols4 = boundaries[4].shape[1]
    assert not np.any(echelon4[len(pivots4):, ncols4])
    survivor_rank = len(echelon_mod_prime(
        echelon4[len(pivots4):, ncols4 + 1:], prime
    )[1])
    assert survivor_rank == 3
    modular_solution = np.zeros(ncols4, dtype=np.int64)
    for row in range(len(pivots4) - 1, -1, -1):
        column = pivots4[row]
        residue = (int(echelon4[row, ncols4])
                   - int(echelon4[row, column + 1:ncols4] @ modular_solution[column + 1:])) % prime
        modular_solution[column] = residue * pow(int(echelon4[row, column]), -1, prime) % prime
    rational_solution = [reconstruct_rational(value, prime) for value in modular_solution]
    filling_denominator = math.lcm(*(value.denominator for value in rational_solution))
    coefficients = np.array([
        value.numerator * (filling_denominator // value.denominator)
        for value in rational_solution
    ], dtype=object)
    assert np.array_equal(
        boundaries[4].astype(object) @ coefficients, filling_denominator * phi.astype(object)
    )
    betti = {str(k): len(cells[k]) - ranks.get(k, 0) - ranks.get(k + 1, 0) for k in cells}
    assert betti["3"] == 3
    register_vertices = {f"{qubit}.{name}" for qubit in (0, 1)
                         for name in namespace["vertex_names"]}
    zero_weights = {v: int(v in register_vertices) for v in graph.vertices}
    one_weights = {v: 1 - zero_weights[v] for v in graph.vertices}
    down0 = weighted_boundary(cells, 3, zero_weights)
    up0 = weighted_boundary(cells, 4, zero_weights)
    down1 = weighted_boundary(cells, 3, one_weights)
    up1 = weighted_boundary(cells, 4, one_weights)
    pair0 = np.vstack((down0, up0.T))
    pair1 = np.vstack((down1, up1.T))
    bulk_indices = [i for i, s in enumerate(cells[3]) if central in s]
    assert len(bulk_indices) == dimension
    assert not np.any(pair0 @ basis)
    assert not np.any(pair0[:, bulk_indices])
    rank0 = len(echelon_mod_prime(pair0, prime)[1])
    known_kernel_dimension = 4 + len(bulk_indices)
    assert rank0 == len(cells[3]) - known_kernel_dimension
    low_bulk_rows = [i for i, s in enumerate(cells[2]) if central in s]
    high_bulk_rows = [i for i, s in enumerate(cells[4]) if central in s]
    t0 = np.vstack((down0[low_bulk_rows, :], up0.T[high_bulk_rows, :]))
    t1 = np.vstack((down1[low_bulk_rows, :], up1.T[high_bulk_rows, :]))
    assert not np.any(t0)
    assert not np.any(t1 @ basis)
    assert all(v not in register_vertices for v in neighbors)
    zero_gram = pair0.T @ pair0
    derivative_gram = pair1.T @ pair1
    unweighted_gram = boundaries[3].T @ boundaries[3] + boundaries[4] @ boundaries[4].T
    gram_bounds = {
        "zero_weight_gram_infinity_norm": int(np.abs(zero_gram).sum(axis=1).max()),
        "derivative_gram_infinity_norm": int(np.abs(derivative_gram).sum(axis=1).max()),
        "unweighted_gram_infinity_norm": int(np.abs(unweighted_gram).sum(axis=1).max()),
    }
    output = {
        "status": "PASS",
        "scope": "Exact target homology, intended filling, zero-weight kernel, and central-relative-bulk injectivity for one source graph; not the complete guarded palette",
        "source": {
            "url": SOURCE_URL, "commit": SOURCE_COMMIT,
            "sha256": hashlib.sha256(upstream).hexdigest(),
            "function": "state_00m10m11", "upstream_license": "GPLv2-or-later",
            "execution": "Only inspected graph-building AST definitions; stopped before Sage operations",
        },
        "projector": {
            "integer_amplitudes_00_01_10_11": [1, 0, -1, -1],
            "relation_to_requested_representative": "Overall minus sign; same rank-one projector",
        },
        "graph": {
            "vertices": sorted(graph.vertices),
            "edges": [list(e) for e in sorted(graph.pairs)],
            "simplex_counts": {str(k): len(v) for k, v in sorted(cells.items())},
            "maximum_dimension": max(cells),
        },
        "central_link": {
            "vertices": sorted(link.vertices),
            "edges": [list(e) for e in sorted(link.pairs)],
            "simplex_counts": {str(k): len(v) for k, v in sorted(link_cells.items())},
            "ordered_triangles": [list(t) for t in link_cells[2]],
        },
        "certificate": {
            "target_local_degree": 3, "link_degree": 2,
            "gram_dimension": dimension,
            "boundary_composition_exact_zero": True,
            "prime": prime, "determinant_mod_prime": determinant,
            "rank_mod_prime": rank, "integer_gram_infinity_norm": bound,
            "integer_gram_sha256": hashlib.sha256(
                json.dumps(gram.tolist(), separators=(",", ":")).encode()
            ).hexdigest(),
            "rational_lower_bound_for_unscaled_pair_singular_value": {
                "numerator": 1, "denominator": denominator,
            },
            "proof": "The nonzero determinant modulo a prime implies a nonzero integer determinant. The Gram matrix is positive definite. Its eigenvalues are at most the infinity norm, so its least eigenvalue is at least that bound to power -(dimension-1).",
            "weighted_consequence": "For binary weights, the projected central-bulk pair on degree 3 equals lambda times this link pair, up to orientation signs.",
        },
        "topology_certificate": {
            "ordinary_betti_over_Q": betti,
            "boundary_compositions_exact_zero": True,
            "boundary_ranks": exact_rank_bounds,
            "rank_proof": "Rational ranks are at least ranks modulo the prime. Each rank is at most either adjacent chain dimension minus the adjacent rank. The recorded lower and upper bounds agree.",
            "three_survivors_independent_mod_boundaries": True,
            "survivor_coefficient_columns_00_01_10_11": [[1, 0, 0], [0, 0, 1], [0, 1, 0], [1, -1, 0]],
            "survivor_proof": "The boundary rank over Q is certified exactly. Appending the three cycle columns increases rank by three modulo the prime, hence also over Q.",
            "exact_filling_denominator": filling_denominator,
            "exact_filling_chain": [
                {"simplex": list(cells[4][j]), "coefficient": int(coefficient)}
                for j, coefficient in enumerate(coefficients) if coefficient
            ],
            "filling_equation_verified_over_integers": True,
            "register_intersection": "Exactly the span of ket00-ket10-ket11: that cycle has an explicit rational filling and three complementary register cycles survive independently.",
            "positive_weight_extension": "Invertible diagonal weight gauge preserves homology; weight-one register coordinates preserve the exact register boundary intersection for every lambda>0.",
        },
        "zero_weight_certificate": {
            "register_vertices": sorted(register_vertices),
            "register_cycle_dimension": 4,
            "register_basis_gram": "16 I_4; divide each cycle by 4 for an isometry",
            "central_bulk_dimension": len(bulk_indices),
            "differential_pair_rank_mod_prime": rank0,
            "rational_rank_upper_bound_from_known_kernel": len(cells[3]) - known_kernel_dimension,
            "kernel_exactly_register_cycles_plus_central_bulk": True,
            "projected_bulk_pair_zero_constant_term": True,
            "projected_bulk_pair_annihilates_register_cycles": True,
            "central_vertex_has_only_new_neighbors": True,
            **gram_bounds,
            "positive_gap_proof": "For an integral PSD Gram matrix of rank r and norm at most B, its nonzero eigenvalue product is a positive integer, so the least positive eigenvalue is at least B^(-(r-1)).",
            "weighted_gap_proof": "For each boundary, partial_w=W_rows^(-1) partial_1 W_columns. The left scaling has minimum singular value at least one; a degree-k column weight is at least lambda^(k+1). Nonzero singular values therefore decrease by at most that factor. At target degree 3 this gives a whole positive Laplacian lower bound c lambda^10.",
            "not_certified": "Leading eigenvalue coefficient, optimal valuation, and guarded-palette closure are not implied by this certificate.",
        },
        "not_certified": [
            "Optimal weighted lifted eigenvalue valuation or its leading coefficient",
            "Full guarded-palette closure under the new finite zero-weight criterion",
            "Complete guarded palette through locality six",
            "Full reduction or priority",
        ],
    }
    folder = Path(__file__).resolve().parent
    destination = folder / "RUDOLPH_REPRESENTATIVE_BULK_CERTIFICATE.json"
    destination.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({
        "status": output["status"], "file": destination.name,
        "source_sha256": output["source"]["sha256"],
        "graph_vertices": len(graph.vertices), "graph_edges": len(graph.pairs),
        "simplex_counts": output["graph"]["simplex_counts"],
        "maximum_dimension": max(cells),
        "central_link_simplex_counts": output["central_link"]["simplex_counts"],
        "gram_dimension": dimension, "prime": prime,
        "determinant_mod_prime": determinant, "infinity_norm": bound,
        "rational_bound_denominator_digits": len(denominator),
        "exact_boundary_ranks_over_Q": ranks, "betti_over_Q": betti,
        "filling_chain_nonzeros": int(np.count_nonzero(coefficients)),
        "filling_denominator": filling_denominator,
        "zero_weight_pair_rank": rank0,
        "zero_weight_kernel_dimension": known_kernel_dimension,
        **gram_bounds,
    }, indent=2))


if __name__ == "__main__":
    main()

<!-- END INCLUDED FILE: certify_representative_bulk.py -->


<!-- BEGIN INCLUDED FILE: PRO_REVIEW_DISPOSITION_2026-09-03.md -->

# Included file 7: PRO_REVIEW_DISPOSITION_2026-09-03.md

# Disposition of the September 3 Pro response

2026-09-03. The full response to source snapshot a46f408 is archived in [PRO_REVIEW_2026-09-03.md](PRO_REVIEW_2026-09-03.md), collected at 10:08:55 UTC after the UI reported “Worked for 155m 30s.” This document separates model proposals, independent deductions, finite computation, primary-source checking, and unresolved claims.

## Claim-by-claim decisions

| Claim / proposal | Decision and independent check | Consequence |
| --- | --- | --- |
| Spectator M'=M tensor I, shared-output horizontal interface, fraction threshold and known initial kernel | **RETAINED.** Direct operator identities and the anchored history construction agree with the existing corrections. | The previously retracted objections remain retracted. |
| All-chain concentration followed by injection/min-max | **CONDITIONAL PROOF SURVIVES.** The analytic hypothesis is distinct from distance to the unknown geometric kernel. | Multiplicity and quotient deductions are standard, not the main contribution. |
| Aggregate lifted-sector bound without t | **VALID; CREDIT CORRECTED.** The frozen packet already contained the aggregate sum in the padding appendix, reproduced in ../../round2/NORMALIZED_PERSISTENCE_PROBE.md. The final loose t factor also arose from a termwise bulk estimate. | Do not attribute the aggregate observation's first appearance in this project to the new Pro answer. |
| Improved Pro floor eta^54 g^27/t^26 | **VALID CONDITIONAL LOWER-BOUND SCALE.** It sharpens the earlier loose t^27 scaling under the imported package. | Superseded by the stronger local continuation below; actual gaps need not equal these powers. |
| Shared-register interface norm can scale as lambda sqrt(t) | **VALID under shared outputs.** Horizontal block-row norm squares sum L_i L_i*. | Does not prove that an additive t^2 lambda^2 error is unavoidable after retaining actual private mass U and absorbing it. |
| Generic projector rotation forces a t lambda term | **INSUFFICIENT AS AN OBSTRUCTION.** It addresses generic projector estimates, not the exact filling/differential structure. | New leakage estimates use squared private mass, exact annihilation and absorption. |
| Sharp two-projector lower bound | **ADOPTED with domains stated.** For 0<g<=1 and 0<alpha<=1, canonical two-projection blocks give gamma=(g+1-sqrt((g+1)^2-4g alpha))/2 >=g alpha/(g+1). | Taking the certified g=1/(8L^2), alpha=1/(3L) gives g2>=1/[3L(8L^2+1)]>=1/(27L^3). |
| Squared principal-angle expression for arbitrary eta<1 | **CORRECTED: MATHEMATICAL ERROR WITHOUT A SIGN CONDITION.** A lower bound a on a nonnegative overlap can be squared only when a>=0. Use max(0,a)^2. | The desired small-error application survives, for example eta<=1/10. |
| Preparation/overlap estimator | **RETAINED WITH COMPLETE ERROR BUDGET.** Include eta between the logical-history and harmonic mixtures, history-preparation error, projection/sampling error, and O(eta^2) overlap bias. | Do not silently treat the exactly known history mixture as the exact geometric harmonic mixture. |
| BQP1(G2) hardness by D=1 | **CONDITIONAL NARROW CONSEQUENCE.** Requires a source allowing the clean work used by the verifier; then the fraction is 0 or 1. | Does not resolve arbitrary-D rank-fraction complexity, BQP hardness, or unrestricted SDQC1 equivalence. |
| Generalized-rank formula for a common quotient diagram | **VALID STANDARD ALGEBRA under its common-quotient and diagram assumptions.** | A secondary structural extension, not a replacement for the global theorem. |
| Persistent-Laplacian extension | **RETAINED AS SECONDARY CONDITIONAL RESULT.** Ordinary-to-persistent domination is already in Mémoli–Wan–Wang's Theorem 5.1 proof. | The earlier novelty emphasis on that inequality is rejected; priority of the complete block theorem remains open. |
| Primary-source reading and absence-of-prior-work assertions | **NOT ADOPTED AS VERIFIED EVIDENCE.** The visible answer's Sources panel contained only the packet, a pasted document, and the GitHub packet. | The model's claimed paper reading and negative literature searches need independent source evidence. |
| Full palette / full reduction / paper readiness | **NOT CERTIFIED.** | A local theorem and one finite certificate are progress, not completion of the paper. |

The two-projection proof can be read directly on each nontrivial canonical block of a projection P onto the first kernel and an output projection R. A compression eigenvalue alpha' in [alpha,1] gives the 2-by-2 block of g(I-P)+R with trace g+1 and determinant g alpha'. Its smaller eigenvalue is bounded below by gamma(g,alpha). The remaining one-dimensional blocks have eigenvalues at least min(g,1); the common zero block is removed. This includes an empty common kernel. We use a chosen certified lower bound g<=1, not an asserted upper bound on the actual first gap.

## Explicit sign-condition counterexample

Take a common reference one-dimensional subspace P=span((1,1)/sqrt(2)), and
\[
Q_A=\operatorname{span}(1,0),\qquad
Q_B=\operatorname{span}(1,99).
\]
Both projector distances to P are below eta=0.8: respectively 1/sqrt(2) and 98/sqrt(19604). The expression
\[
a=\sqrt{1-\eta^2}\sqrt{1-\eta^2}-\eta^2=1-2\eta^2=-0.28
\]
has square 0.0784, while the squared overlap is only 1/9802. Thus squaring the negative lower bound is false. The corrected lower bound is max(0,a)^2. For equal errors eta<1/sqrt(2), a is positive and the intended bound applies.

The [finite fixture record](EXACT_FILLING_COERCIVITY_CHECKS.json) includes this guard and a counterexample to dropping the exact-filling hypothesis in the PSD domination lemma.

## Independent continuation beyond the response

1. **Exact-filling coercivity.** Hodge decomposition and ran Pi_i subset B_d(Y_i) imply Delta_i^up>=delta_i Pi_i, without commutation or comparison to an approximate lifted eigenvector. Summing gives Delta^up>=c lambda^kappa H^emb with no t.
2. **Quadratic geometric leakage.** Retaining actual private mass in the shared-register interference term and absorbing it gives N<=C[t lambda^2+(t+lambda^-kappa)e] under the earlier local spectral package. This is proved in [EXACT_FILLING_COERCIVITY.md](EXACT_FILLING_COERCIVITY.md).
3. **Simpler finite-certificate route.** A zero-weight kernel identity and a projected bulk singular bound yield the stronger leakage form N<=C[t lambda^2+(t+lambda^-2)e]. An elementary diagonal-scaling bound supplies a local positive floor c lambda^(4m+2), without spectral valuation. See [FINITE_CERTIFICATE_CONCENTRATION.md](FINITE_CERTIFICATE_CONCENTRATION.md).
4. **Improved global dependence.** Both routes give distance squared <=C[t lambda^2+e/(g lambda^kappa)]. Choose lambda independently of g. The conservative m<=6 scales are weighted Omega(eta^28 g/t^26) and, under common-copy unweighting, Omega(eta^26 g/t^24).
5. **Actual finite source certificate.** Replayed the pinned Rudolph representative and proved its target homology, intended filling, zero-weight kernel and projected central bulk injectivity with integer/modular calculations. Full evidence is in [REPRESENTATIVE_GADGET_CERTIFICATE.md](REPRESENTATIVE_GADGET_CERTIFICATE.md).
6. **Higher-simplex correction.** That graph has degree-5 simplices at target degree 3. The old two-bidegree enumeration is false; the repaired proof quantifies over every bidegree and uses the positive outside gap whenever the outside degree is not harmonic.

The 15 separate weighted-clique fixtures check the elementary coercivity mechanism, exact up additivity and kernel counts, including zero final kernels. They are not Rudolph/King--Kohler palette certificates. The actual representative calculation is separate, exact, and source pinned.

## Primary checks actually performed in this continuation

- King--Kohler arXiv:2311.17234v2: Lemma 9.1 statement and Claim 10.4's exact up-Laplacian sum. The complete spectral-sequence proof and final SIAM version were not reread.
- Hayakawa arXiv:2608.02726v1, Section 5, especially Lemma 5.4: explicit finite-family register quotient and use of earlier constructions/joins. This is not a new full theorem audit.
- Rudolph arXiv:2411.02681v2, Appendix D.1: displayed active states, sphere-join statement, distinction between algebraic two-qubit and numerical higher-locality checks, and supplementary-code reference.
- The linked source repository at commit 30ac70e5dacdecce97c38d801c128ec3ed93a96a: README/license and the inspected graph-building functions. Exact replay and certificates are documented separately.
- The earlier Mémoli–Wan–Wang check remains recorded in [POST_DISPATCH_SOURCE_UPDATE.md](POST_DISPATCH_SOURCE_UPDATE.md).

These checks support the specified ingredients. They do not establish a global novelty claim, unrestricted source-class equivalence, or that every source theorem has been independently verified.

## Next focused Pro gate

Attack the two new proof routes, with priority on the finite-certificate theorem: diagonal singular scaling, all-bidegree padding, retained-mass interface absorption, and direct logical coercivity. Either give a concrete counterexample under the exact hypotheses, or improve/prove the result. Then resolve the guarded-palette closure or identify the smallest concrete missing atom. Request precise source locations for any priority collision. The new request should include both the certificate graph data and checker, not only a summary.


<!-- END INCLUDED FILE: PRO_REVIEW_DISPOSITION_2026-09-03.md -->


<!-- BEGIN INCLUDED FILE: SOURCE_LEDGER.md -->

# Included file 8: SOURCE_LEDGER.md

# Source ledger and dependency map

The six-item ledger below was supplied by the user as checked locally. Existing local reports contain prior section-level reading notes. This consolidation read those reports; it did not independently reopen and verify every primary source. The wording below records claims to check, not a newly completed literature audit.

| Source | Reported established content | Boundary for the present work |
| --- | --- | --- |
| [Crichigno–Kohler, Nature Communications 2024](https://www.nature.com/articles/s41467-024-54118-z) | Parsimonious quantum-kSAT-to-clique-homology reduction; satisfying states correspond to holes; #BQP counting hardness | Exact multiplicity by itself is old. No inverse-polynomial gap above a degenerate whole kernel is imported from this item. |
| [King–Kohler, arXiv 2311.17234v2](https://arxiv.org/html/2311.17234v2), FOCS 2024 / [SIAM DOI](https://doi.org/10.1137/24M1710243) | Fixed local spectral gadget and many-gadget NO-case gap when logical \(H\succeq gI\) | A general whole-positive-gap theorem over arbitrary degenerate kernels was not located in the supplied reading. This is not proof of absence. The padded coordinate-bulk estimate has the reported outside-weight-one problem. Use only an explicit supported finite palette. |
| [Gyurik et al., PRX Quantum 7, 020361 (2026)](https://journals.aps.org/prxquantum/pdf/10.1103/gvys-hl8h), [arXiv 2410.21258v2](https://arxiv.org/html/2410.21258v2) | BQP1-hard harmonic survival for a specified pure guide; a particular whole-kernel gap argument | This is not uniform-initial-homology survival fraction. A simulated-register estimate is reportedly invoked on an arbitrary low-energy vector; the independent all-chain proof is intended to avoid relying on that invocation. Do not call the published theorem false without a full audit. |
| [Rudolph, arXiv 2411.02681v2, Appendix D.1](https://arxiv.org/html/2411.02681v2#A4.SS1) | Gain/loss Hadamard split, concrete three-term two-qubit states, and sphere-join closure for fixed guards | These are credited prior ingredients. General integer-state correctness is not inferred. Source-match the concrete displayed vectors and attaching maps. |
| [Lowe–Kim–Bondesan–Hayakawa, arXiv 2607.03278v1](https://arxiv.org/html/2607.03278v1) | NHP Problem 9 and Conjecture 1; Conjecture 2 asks multiplicity, compatible exact harmonic isometries and small output coefficient; exact Hamiltonian result under SDQC1; quasi-TDA DQC1 hardness | The normalization itself is old. Equal-complex quasi hard instances have true NHP one when defined. Definition 2 allows arbitrary thresholds and has explicit gate-set dependence; the trace-to-fixed-space-rank inference needs the threshold restriction described in the dossier. No claim to resolve the unrestricted conjecture. |
| [Hayakawa, arXiv 2608.02726v1](https://arxiv.org/html/2608.02726v1) | Common clique-copy unweighting; Lemma 5.4 register quotient for one projector; Lemma 6.1 outside harmonic tensors; Theorem 6.2 NO-case gap | Those local ingredients are not new. Filtered applications were listed as future work. The proposed extension concerns the full persistent-Laplacian restricted domain and low spectrum, subject to checking priority. |

## Local proof obligations, with owning artifacts

| Obligation | Owner / evidence | Current state |
| --- | --- | --- |
| Independent interior-chain decomposition | ../../round2/NORMALIZED_PERSISTENCE_PROBE.md, abstract proof | Local derivation under exact intersections |
| Exact filling for each palette member | Old weight-gauge/nullity argument; new REPRESENTATIVE_GADGET_CERTIFICATE.md | One source graph has an explicit integer filling and certified quotient; full guarded family remains open |
| All-chain concentration with term-count-uniform constants | FINITE_CERTIFICATE_CONCENTRATION.md and EXACT_FILLING_COERCIVITY.md | Two stronger local conditional proofs; independent review pending |
| Central bulk and zero-weight local data | certify_representative_bulk.py and exact JSON certificate | One actual atom certified; other atoms/guard closure open |
| Local whole-positive-gap floor | FINITE_CERTIFICATE_CONCENTRATION.md, diagonal scaling plus Hodge decomposition | Elementary conditional finite-family lower bound; optimal valuation and leading coefficient not needed |
| Older lifted-cycle spectral-sector route | King–Kohler fixed-size package with explicit palette | Retained imported route; full spectral-sequence proof not independently reconstructed |
| Rational projector palette and tensor guards | ../../round2/UNARY_PALETTE_ADDENDUM.md | Explicit local source matching and derivation; imported gadget facts remain |
| Weighted history and both logical gaps | Same addendum, Section 3 | Complete written elementary proof; finite fixtures rerun |
| Mixed-spectator exact single-H extension | RESEARCH_DOSSIER.md, Section 5 | Direct algebra from the supplied definitions |
| Exact positive denominator, preparation error | Palette addendum Sections 3–4 | Construction and explicit approximation budget |
| Natural filtered unweighting | ../../tda_probe/UNWEIGHTING_FIRST_LEMMA.md | Conditional on the stated symmetric/asymmetric spectral package |
| Persistent-Laplacian extension | PERSISTENT_LAPLACIAN_EXTENSION.md | New local conditional synthesis of Pro proposal; priority open |
| Standard-class hardness / impact | Explicit restricted circuit source | Open; not implied by gate names or threshold constants |

Additional sources already identified in the local portfolio include Dey–Xin generalized ranks/unfolding, Dey–Jendrysiak–Kerber decomposition, classical algebraic module-decomposition algorithms, quantum clustering/coreset methods, and cover-based barcode approximation. Their links and exact local model comparisons are retained in the original reports. Pro is asked to verify relevant primary statements, not merely repeat this table.

The completed first Pro response additionally cites [Mémoli–Wan–Wang, persistent Laplacians](https://arxiv.org/abs/2012.02808) and [SIAM DOI](https://doi.org/10.1137/21M1435471). Its claim that the proposed filtered spectral theorem was not found in the literature remains an advisory search report, not established priority.

**Post-dispatch targeted primary check, September 3 PDT:** this task independently reopened arXiv:2012.02808v1, Section 2.2 and the proof of Theorem 5.1 in Section 5.2. The domain decomposition already yields ordinary-to-persistent Laplacian domination. That inequality is prior art; the old Pro answer's novelty emphasis is incorrect. See [POST_DISPATCH_SOURCE_UPDATE.md](POST_DISPATCH_SOURCE_UPDATE.md). This narrow check does not certify the six main sources or priority of the combined filtered corollary.

## Additional primary checks after collecting the new response

September 3, 2026: independently opened King–Kohler arXiv v2's Lemma 9.1 and Claim 10.4, Hayakawa arXiv v1 Section 5/Lemma 5.4, and Rudolph arXiv v2 Appendix D.1. Checked the stated local spectrum and exact up sum, finite-family quotient/joins, displayed active vectors, and algebraic-versus-numerical verification boundary. This is a targeted check, not a full paper or final-SIAM-version reread.

Rudolph's bibliography points to [the public supplementary code](https://github.com/DorianRudolph/QMA1-gateset-paper). We read its README/license and the relevant graph-building functions at immutable commit [30ac70e5dacdecce97c38d801c128ec3ed93a96a](https://github.com/DorianRudolph/QMA1-gateset-paper/tree/30ac70e5dacdecce97c38d801c128ec3ed93a96a). The exact source hash, replay boundary and finite certificate are in [REPRESENTATIVE_GADGET_CERTIFICATE.md](REPRESENTATIVE_GADGET_CERTIFICATE.md). We did not run Sage or the source's higher-locality numerical checks.

The Pro answer's source-panel evidence did not expose its claimed independent primary-paper reading: only the packet, a pasted document, and the same GitHub packet were visible. Its broad source/absence claims remain advisory. The independent checks above are the evidence actually added by this continuation. Priority of either stronger concentration proof remains open.

<!-- END INCLUDED FILE: SOURCE_LEDGER.md -->


<!-- BEGIN INCLUDED FILE: ../../round2/UNARY_PALETTE_ADDENDUM.md -->

# Included file 9: ../../round2/UNARY_PALETTE_ADDENDUM.md

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

<!-- END INCLUDED FILE: ../../round2/UNARY_PALETTE_ADDENDUM.md -->
