# Pro novelty and theorem-delta review — complete response

Collected 2026-09-03T20:36:43.564Z. The browser showed a completed **GPT-5.6 Pro** response, **Worked for 15m 38s**, after user message 9 and the novelty packet. This is external model review, not independent correctness, exhaustive priority, or paper-readiness certification.

- Conversation: [Audit Quantum Persistence Corollary](https://chatgpt.com/c/6a98c05a-ecf4-83e8-b356-4e20dc3fde3f).
- Request source commit: `6e70274a78872cd891cedd4319145d68195d02fc`.
- Dispatch/archive commit before send: `18a47e92d169d7312355b8f94372a78eccf4b8fe`.
- Actual task: [novelty submission](PRO_NOVELTY_SUBMISSION_2026-09-03.md).
- Input: [PRO_NOVELTY_PACKET_2026-09-03.md](PRO_NOVELTY_PACKET_2026-09-03.md), 72,511 bytes, SHA-256 `220304109773ce44ed91f8cf8846a91d9cecaeab82565df13a0a4c06e8c0c3e1`.
- Assistant message ID: `d2855e9c-808a-4c5d-b7ec-38ff09d08534`; model slug: `gpt-5-6-pro`.
- The visible account remained the previously verified personal Pro identity; the public archive omits account email.
- Exact browser completion time was not exposed; collection time and displayed duration are separate facts.

The response below was transcribed from the rendered DOM. All **70** equation elements were recovered from displayed `data-math-source` attributes, and all **13** visible external links were retained. The browser Copy response action returned stale Markdown from user message 7, failed three content checks, and was rejected. [The capture record](PRO_NOVELTY_REVIEW_CAPTURE_2026-09-03.json) retains the rendered text, exact equation sources, links, and transcription. Adopted conclusions are recorded separately.

---

# Strongest collision

The **degenerate-kernel upgrade itself is almost a one-paragraph King–Kohler corollary**.

In King–Kohler arXiv v2, Theorem 10.1 assumes a positive-definite logical Hamiltonian, but its proof first takes an arbitrary vector in the **full geometric chain space**, expands it into single-gadget sectors, and obtains a master inequality involving simulated-register mass, logical energy, and high/bulk/lifted errors. The assumption \(H\succeq gI\) is used only at the final coercivity step. Their Lemmas 10.2–10.4 are also stated for arbitrary full-chain vectors. [arXiv](https://arxiv.org/html/2311.17234v2)

Consequently, **once a correct arbitrary-chain master estimate is granted**, replacing

$$
H\succeq gI
$$

by

$$
H\succeq g(P-P_K)
$$

immediately yields concentration toward \(K=\ker H\); exact filling plus projection/min–max then yields exact multiplicity and a gap above the entire geometric kernel. Those last steps are not a substantial novelty.

However, the current finite-certificate proof is **not merely a valid invocation of the arXiv-v2 proof**, because King–Kohler’s padded bulk Claim 10.2 is not valid as written. Their proof says that every vertex touching the coordinate bulk has weight \(\lambda\). After join-padding, outside-register vertices have weight one and form cofaces with local bulk simplices. [arXiv](https://arxiv.org/html/2311.17234v2)

Concretely, let \(\tau\) be a local simplex containing the central bulk vertex and let \(\eta\) be an outside-register simplex containing a weight-one vertex \(u\). For the padded simplex \(\tau*\eta\),

$$
\partial(\tau*\eta)
\supseteq
\pm\tau*(\eta\setminus\{u\})
$$

with coefficient \(w(u)=1\). The output still contains the central vertex and therefore remains in the full coordinate bulk. Distinct deleted outside vertices give orthogonal simplex coordinates, so the projected norm is bounded below independently of \(\lambda\), contradicting an \(O(\lambda)\) estimate.

The first potentially new lemma is therefore not “allow \(\ker H\neq0\).” It is:

> **A corrected arbitrary-chain leakage theorem from finite zero-weight data, projected private-pair coercivity, all-bidegree harmonic padding, and shared-register interface control.**

That lemma replaces the defective coordinate-bulk argument, obtains the quadratic structural remainder \(t\lambda^{2}\), and lets \(\lambda\) be chosen independently of \(g\). This is a genuine proof delta relative to arXiv v2, although still close enough to King–Kohler’s architecture that its conceptual novelty is **medium rather than high**. The packet’s intended theorem and its exact scope are stated explicitly. 〔PRO_NOVELTY_PACKET_2026-09-03〕

I accessed the SIAM publication’s metadata and abstract, but its detailed full text was access-restricted. I therefore cannot determine whether the final SIAM Section 10 or appendix repaired Claim 10.2 or added an equivalent arbitrary-chain lemma. The detailed comparison below is against arXiv:2311.17234v2, not a certification of the final published proof. [SIAM](https://epubs.siam.org/doi/10.1137/24M1710243)

# Source-by-source findings

## 1. King–Kohler

**Directly checked:** Theorem 10.1; Claim 10.2; Claim 10.4; Lemmas 10.2–10.4; and the final calculation in Section 10.

Theorem 10.1 chooses

$$
\lambda=ct^{-1}g,\qquad
E=c\lambda^{4m+2}t^{-1}g,
$$

under a lower bound on the entire logical spectrum. The proof already treats arbitrary geometric chains and isolates the logical Hamiltonian term before using positive definiteness. Claim 10.4 also gives exact additivity of the global up-Laplacian over gadgets. [arXiv](https://arxiv.org/html/2311.17234v2)

**Deduction:** If their full arbitrary-chain estimates were accepted unchanged, the degenerate-kernel extension would be routine. The current project’s substantive addition is the replacement leakage proof and its weaker finite local hypotheses—not the final quotient/min–max argument.

**Mathematical issue:** arXiv-v2 Claim 10.2’s full-coordinate padded bulk estimate has the counterexample above.

**Priority uncertainty:** the inaccessible final SIAM proof might contain a correction.

## 2. Gyurik et al.

Gyurik et al. already state a gap above the complete final harmonic space in Lemma 7. The nonempty-kernel case starts with an arbitrary geometric low-energy vector orthogonal to the harmonic space and invokes Lemma 11 to conclude high overlap with the simulated logical kernel. [arXiv](https://arxiv.org/html/2410.21258v2)

But Lemma 11 explicitly assumes

$$
|\sigma\rangle=s(|\varphi\rangle)\in\mathfrak H_{\mathrm{sim}},
$$

rather than an arbitrary full-chain vector. [arXiv](https://arxiv.org/html/2410.21258v2)

Thus:

- Gyurik et al. **already claims** a particular degenerate whole-kernel gap;
- its displayed proof does **not explicitly close** the arbitrary-chain-to-simulated-register bridge;
- this is a proof-domain mismatch, not a counterexample to the theorem;
- the present result should be framed as an **independent repair and generalization**, not the first whole-kernel gap theorem.

The current theorem is stronger in its uniform statement over arbitrary degenerate logical kernels, exact multiplicity, both endpoints, and natural quotient filtrations. But the prior claim sharply limits novelty.

## 3. Lowe–Kim–Bondesan–Hayakawa

Problem 9 already defines the target statistic exactly as

$$
\frac{\beta_d^{1,2}}{\beta_d^1},
$$

with gaps above zero at both endpoints. Conjecture 1 asks for hardness of this true normalized problem. [arXiv](https://arxiv.org/html/2607.03278v1)

Section 7 explicitly says King–Kohler is not sufficient as a black box and formulates Conjecture 2 using exact kernel realization and compatible harmonic isometries across the filtration. [arXiv](https://arxiv.org/html/2607.03278v1)

The quotient route is therefore a **meaningful but restricted bypass**:

$$
H_d(X_A)\cong V/W_A,
\qquad
W_A=\sum_{i\in A}\operatorname{ran}\Pi_i,
$$

and for \(A\subseteq B\), inclusion becomes

$$
V/W_A\twoheadrightarrow V/W_B.
$$

This proves the desired numerical persistent rank without producing one exact compatible harmonic-representative isometry.

That is not already written in Lowe et al.; filtration compatibility is precisely one of their identified missing ingredients. But it resolves only the specially engineered nested-term-set family and the gate-dependent perfect-completeness source. It neither proves Conjecture 2 nor resolves their unrestricted Conjecture 1.

## 4. Hayakawa

Hayakawa’s Lemma 4.2 identifies the block-symmetric sector exactly with the weighted base complex. The common scale \(M\) multiplies the weighted Laplacian by \(M\). Theorem 4.3 gives an asymmetric-sector gap of at least the smallest block multiplicity, and Corollary 4.4 excludes all asymmetric homology. [arXiv](https://arxiv.org/html/2608.02726v1)

With the **same labeled copy block** at every filtration level, the additional argument is one line:

$$
\widehat J_{AB}U_A=U_BJ_{AB}.
$$

Therefore

$$
\widehat P_BU_BJ_{AB}
=
U_BP_BJ_{AB},
$$

and equivalently

$$
\widehat P_B\widehat J_{AB}U_A
=
U_BP_BJ_{AB}.
$$

All harmonic-map singular values and ranks are preserved. The endpoint gap becomes

$$
\min\{M\gamma_A,\min_v f_v\}.
$$

For weights \(\{1,\lambda\}\), dyadic \(\lambda\), and

$$
M=\lambda^{-2},
$$

register blocks have size \(M\), gadget blocks size one, and the blow-up is polynomial whenever \(\lambda^{-1}\) is polynomial. Later gadget vertices may be included initially as isolated vertices; because the target degree is positive, they add no target-degree chains.

So the unweighted filtration result is **mathematically a short direct corollary**, not a blocked theorem and not a main novelty claim. Hayakawa explicitly leaves filtered applications as future work, but his operator theorem already supplies essentially everything needed. [arXiv](https://arxiv.org/html/2608.02726v1)

## 5. Exact multiplicity, normalized persistence, and gadgets

Crichigno–Kohler already give a parsimonious reduction in which satisfying states correspond one-to-one with homology classes. Exact kernel/homology multiplicity is therefore prior art. They also explain that their construction does not establish the required inverse-polynomial Laplacian promise gap. [Nature Communications](https://www.nature.com/articles/s41467-024-54118-z)

Rudolph’s Appendix D.1 already supplies the concrete few-term integer states and join construction used for the finite palette, while warning that the more general gadget construction lacks a correctness proof. The finite certificates add verification and source integration, not conceptual ownership of those gadgets. [arXiv](https://arxiv.org/html/2411.02681v2)

Nearby work on “normalized persistent Betti numbers” commonly uses simplex-count normalization,

$$
\beta_k^{i,j}/n_k,
$$

not Lowe et al.’s initial-Betti normalization. Thus the present statistic is not collided by that terminology—but Lowe et al. already defines the exact statistic under study. [arXiv](https://arxiv.org/html/2404.15407v2)

# Concrete theorem delta

## Proposition 1 — the kernel upgrade is routine

Suppose an arbitrary-chain estimate has already established, for every unit \(x\),

$$
1-\langle x,Px\rangle+\langle x,Hx\rangle\le R(e),
\qquad
e=\langle x,\Delta x\rangle,
$$

where \(H\) is supported on \(V=\operatorname{ran}P\), and

$$
H\succeq g(P-P_K),\qquad 0<g\le1.
$$

Then

$$
\begin{aligned}
g\|(I-P_K)x\|^2
&=
g\bigl(1-\langle x,Px\rangle\bigr)
+
g\langle x,(P-P_K)x\rangle\\
&\le
1-\langle x,Px\rangle+\langle x,Hx\rangle\\
&\le R(e).
\end{aligned}
$$

Hence

$$
\boxed{\|(I-P_K)x\|^2\le R(e)/g.}
$$

If exact filling supplies \(\dim K\) exact geometric zero modes and \(R(E)<g\), projection onto \(K\) is injective on the geometric spectral subspace below \(E\). Therefore that subspace has dimension at most \(\dim K\), proving exact kernel multiplicity and a whole-positive-spectrum gap.

This proposition documents why the kernel/min–max portion cannot carry the novelty claim.

## Theorem 2 — surviving functorial finite-certificate transfer

Assume the packet’s finite zero-weight kernel, projected private-pair, all-bidegree padding, interface, exact filling, and independent-interior hypotheses. I did not independently recompute those finite certificates.

For every finite nested family of term sets \(A\), let

$$
H_A=\sum_{i\in A}\Pi_i,\qquad
K_A=\ker H_A,\qquad
W_A=\sum_{i\in A}\operatorname{ran}\Pi_i,
$$

and suppose

$$
H_A\succeq g_A(P-P_{K_A}).
$$

Then, uniformly for \(\lambda\le c/t_{\max}\), every normalized full geometric chain satisfies

$$
\boxed{
\operatorname{dist}(x,K_A)^2
\le
C\left[
t_A\lambda^2+
\frac{\langle x,\Delta_Ax\rangle}
{g_A\lambda^\kappa}
\right].
}
$$

Moreover, for

$$
E_A\le c'\eta^2g_A\lambda^\kappa,
$$

there are natural isomorphisms

$$
\boxed{H_d(X_A)\cong V/W_A}
$$

simultaneously over the whole term-set diagram, and

$$
\dim\ker\Delta_A=\dim K_A,
\qquad
\operatorname{spec}(\Delta_A)\cap(0,E_A)=\varnothing.
$$

Every arrow \(A\subseteq B\) is the quotient map

$$
V/W_A\twoheadrightarrow V/W_B,
$$

so its rank is \(\dim K_B\). For a chain filtration, all maps are epimorphisms: there are deaths but no new births in this degree.

### Proof

The finite-certificate leakage argument gives

$$
\|(I-P)x\|^2
\le
C\!\left[t_A\lambda^2+
(t_A+\lambda^{-2})\langle x,\Delta_Ax\rangle\right].
$$

Exact filling and the local whole-positive-gap floor imply

$$
\Delta_A^\uparrow
\succeq c\lambda^\kappa H_A^{\mathrm{emb}},
$$

because on local boundary chains the up-Laplacian equals the full Laplacian, and up-columns partition by gadget. Thus

$$
\langle x,(P-P_{K_A})x\rangle
\le
\frac{\langle x,\Delta_Ax\rangle}
{cg_A\lambda^\kappa}.
$$

Adding geometric leakage and forbidden logical mass proves concentration. Exact filling and independent interiors give

$$
B_d(X_A)\cap V=W_A,
$$

hence an injection \(V/W_A\hookrightarrow H_d(X_A)\). Concentration bounds the entire low-energy dimension in the reverse direction. Equality and naturality follow. This is precisely the part of the packet that can plausibly be presented as the reusable theorem, rather than as a specialized final step. 〔PRO_NOVELTY_PACKET_2026-09-03〕

Common-copy blow-up then produces a naturally equivalent unweighted diagram with gap floor \(\min\{ME_A,\min f_v\}\). That last statement is a Hayakawa corollary, not an additional analytic theorem.

# Correct positioning

A defensible title is:

> **Gapped Kernel Realization in Clique Filtrations: Exact Multiplicity and True Normalized Persistence**

The strongest current theorem package is:

- **weighted:** conditional on the packet’s exact finite certificates, a polynomial construction with exact endpoint multiplicities, natural persistent rank, and whole-kernel gaps;
- **complexity:** weighted additive true normalized persistence is hard for the exact gate-dependent class \(\mathsf{BQP}_1^{G_2}\), using the already-audited eight-label source;
- **unweighted:** a direct common-copy corollary conditional on the weighted theorem and Hayakawa’s symmetric/asymmetric decomposition;
- **not established:** ordinary BQP, unrestricted \(\mathsf{SDQC}_1\), gate-independent \(\mathsf{BQP}_1\), or complex-phase coverage.

# Status and value

| Component | Mathematical status | Novelty/impact status |
| --- | --- | --- |
| Degenerate-kernel substitution | Valid | **LOW**; routine once arbitrary-chain control exists |
| Exact multiplicity via quotient/min–max | Valid | **LOW**; standard closure and collided by parsimonious homology |
| Finite-certificate all-chain leakage | Valid under supplied certificates | **MEDIUM**; genuine repair/strengthening of arXiv-v2 proof |
| Gyurik whole-kernel gap | Prior claimed result | Strong collision; displayed arbitrary-chain bridge incomplete |
| Quotient filtration | Valid | **MEDIUM-LOW**; meaningful restricted bypass of Lowe Conjecture 2 |
| Common-copy unweighting | Valid | **LOW**; direct Hayakawa corollary |
| Weighted \(\mathsf{BQP}_1^{G_2}\)-hard NHP | Conditional on geometric package | Meaningful but gate-dependent |
| Padding-generated denominator | Valid | Significant conceptual weakness |
| Gap exponent \(26\) | Inverse polynomial | Theoretically adequate, practically poor |
| Overall project | **MEDIUM, conditional** | Not presently a high-impact breakthrough |

The plausible current venue band is **TQC / Quantum**, with an **ITCS or ICALP borderline case** if the final paper cleanly establishes the unweighted theorem, documents the published-proof repair, and presents the finite-certificate transfer as a reusable result. Without that, the work risks reading as a careful technical completion of King–Kohler plus Gyurik. It is not presently a STOC/FOCS-level delta.

# Finite go/no-go gate

The cheapest decisive falsification test is to obtain the final SIAM text and inspect the published analogues of Claim 10.2 and Appendix B:

- If it already replaces coordinate bulk by local bulk tensored with outside harmonics—or proves an equivalent zero-weight/private-pair arbitrary-chain leakage estimate with quadratic \(t\lambda^2\) error—then the main analytic novelty largely collapses. **No-go as a standalone transfer paper.**
- If the final proof retains the arXiv-v2 bulk argument, the current theorem is a documented repair and strengthening. **Go**, but headline the finite-certificate leakage theorem and restricted quotient realization, not the elementary kernel/min–max or unweighting corollaries.

Priority beyond these directly checked sources remains unresolved; search nonappearance is not evidence of novelty.
