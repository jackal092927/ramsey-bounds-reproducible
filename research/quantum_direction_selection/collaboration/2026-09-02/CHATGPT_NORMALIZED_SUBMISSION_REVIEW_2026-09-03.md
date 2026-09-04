# Submission-focused review of the Normalized Persistence manuscript

**Review branch:** `chatgpt/normalized-submission-review-2026-09-03`  
**Source branch:** `codex/fill-ramsey-gaps`  
**Source commit locked for this review:** `586811c8e7e3b610f79eec570b7914a62ce1b817`  
**Scope:** `research/quantum_direction_selection`, principally `collaboration/2026-09-02/manuscript_v0`. The unrelated `papers/quantum` subtree was not reviewed or modified.

## Executive verdict

**Verdict: SUBMISSION-CANDIDATE AFTER LISTED FIXES.**

The core mathematical chain survives this review. I found no counterexample to the finite-certificate all-chain concentration argument under its displayed hypotheses. The projection/min–max closure correctly yields exact endpoint kernel multiplicities and an inverse-polynomial floor above the complete positive spectrum. The quotient maps correctly identify the two-level persistent rank, including a zero-dimensional final kernel. The eight-label circuit has the claimed compressed acceptance operator and exact fractions 3/4 and 1/8. The common-copy construction correctly transfers the filtered result to unweighted clique complexes when Hayakawa’s symmetric/asymmetric theorem is imported with identical labeled copy blocks at every level.

The current manuscript is nevertheless **not ready to submit in its present form**. The blockers are formalization and proof integration rather than a missing new theorem. Most importantly:

1. the target promise problem omits the weighted input encoding and several access-model details;
2. the paper presents the finite palette as instantiated but never states and proves a palette-certification proposition inside the paper or an anonymous supplement;
3. the named gate-dependent BQP1 source is not formally defined or normalized with the exact soundness theorem it requires;
4. the reduction does not explicitly produce the dyadic weight and certified gap as encoded outputs;
5. the source-comparison and bibliography language admits that the final King–Kohler article was not checked while the AI disclosure says source attributions were independently checked;
6. the certificate archive cannot be linked in a double-blind submission without de-anonymization.

No manuscript file was edited in this review. The repairs below can be made from the existing archive and do not require stronger mathematics.

---

# I. Prioritized findings

## CRITICAL 1. The target promise problem is not the formal problem used by the reduction

**Pointers**

- `manuscript_v0/sections/2_preliminaries.tex:24-31`, Definition “Gapped true normalized persistence”.
- `manuscript_v0/sections/5_circuit.tex:109-127`, Theorem `thm:weighted-hardness` and proof.
- `manuscript_v0/sections/6_unweighting.tex:1-75`, weighted-to-unweighted transfer.

The definition currently lists graph descriptions, degree d, one common gap number E, the promise β_d(X₁)>0, and an additive accuracy. It omits data used essentially by the weighted reduction:

- the vertex-weight function and its binary encoding;
- a common labeled vertex set and one common weight for every shared vertex;
- whether the graphs are explicit graphs, adjacency circuits, or another kind of “polynomial-size graph description”;
- separate endpoint gap promises, or an explicit convention that one number lower-bounds both;
- approximation success probability;
- the decision-promise version used for hardness;
- the input-size convention, including bit lengths of d, weights, gaps, and accuracy.

As written, `thm:weighted-hardness` does not formally reduce to the problem that was defined.

### Concrete replacement

Replace the current definition by two formal problems. Suggested text:

> **Weighted gapped true normalized persistence.** An input consists of explicit labeled graphs G₁ ⊆ G₂ on a common vertex set V, a common positive dyadic weight function w:V→Q_{>0} encoded in binary, a degree d≥1, rational lower bounds γ₁,γ₂>0, and an accuracy ε>0. Let Xᵢ=Cl(Gᵢ), with the weighted boundary convention fixed in this paper. Promise β_d(X₁)>0 and spec(Δ_{Xᵢ,d}) ⊆ {0} ∪ [γᵢ,∞) for i=1,2. Output q̃ satisfying Pr[|q̃−q_d(X₁,X₂)|≤ε]≥2/3. Input size is the total bit length of the two graph encodings, w,d,γ₁,γ₂,ε.
>
> **Unweighted gapped true normalized persistence.** The preceding problem restricted to w≡1.

For hardness, state directly the decision promise

`q_d(X₁,X₂) ≥ 3/4` versus `q_d(X₁,X₂) ≤ 1/8`,

or the fixed additive-approximation problem at error 1/24 and success probability at least 2/3. The construction produces explicit polynomial-size graphs. Do not call them “succinct” unless an adjacency-circuit model is intended and proved.

---

## CRITICAL 2. The complete finite palette is asserted, not established in the paper or a submission-ready supplement

**Pointers**

- `manuscript_v0/sections/3_transfer.tex:18-39`, Assumption `ass:local-certificate`.
- `manuscript_v0/sections/3_transfer.tex:40-43`, certification sentence.
- `manuscript_v0/sections/5_circuit.tex:28-36`, assertion that the circuit palette is certified.
- `manuscript_v0/sections/B_source_details.tex:76-105`, atom list and certificate narrative.
- Archive owners: `REPRESENTATIVE_GADGET_CERTIFICATE.md`, `REMAINING_ACTIVE_ATOM_CERTIFICATES.md`, `ACTIVE_HADAMARD_ORBIT.md`, `SELECTED_CYCLE_GUARD_CLOSURE.md`, certificate JSON files, checkers, and offline receipts.

The abstract and hardness theorem read as unconditional statements about an instantiated palette. Inside the paper, however, the only formal transfer theorem is conditional on `ass:local-certificate`. Section 5 says that the named atoms satisfy the assumption, but gives neither a proposition nor enough exact data to check it. The archive contains substantial exact evidence, but a referee cannot infer the hardness theorem from one unsupported sentence.

There is also a precision error at `3_transfer.tex:40-43`: an exact filling chain proves only

`ran Π_a ⊆ B_{d_a}(Y_a) ∩ V_a`.

It does not by itself prove equality. Equality additionally uses certified boundary ranks and independent surviving register cosets, or the selected-cycle connecting-map theorem.

### Concrete replacement

Add an appendix proposition:

> **Proposition (Certified palette).** For every local projector occurring in the history construction, including every computational-basis guard through total locality six, the associated weighted clique gadget satisfies Assumption 3.1. All finite assertions hold over Q and hence over R and C by scalar extension. The constants may be chosen uniformly over this fixed finite family.

The paper and anonymous supplement must expose at least the following exact table and implications.

| Atom | Exact evidence that must be exposed |
|---|---|
| Basis cone | 8 vertices, 12 edges, 4 triangles; boundary ranks 7 and 4; target Betti number 1; zero-pair rank 10, two-dimensional register kernel, Q=0. |
| `|0⟩−|1⟩` | 16 vertices; clique counts (16,40,24); ranks 15,24; Betti numbers (1,1,0); 24-term integer filling; zero-pair rank 30 with kernel 2+8; projected Gram determinant nonzero mod 1000003, residue 512, with the recorded norm bound. |
| `|00⟩−|11⟩` | 33 vertices; clique counts (33,241,646,712,272); ranks 32,209,437,272; Betti numbers (1,0,0,3,0); 248-term integer filling; zero-pair rank 596 with kernel 4+112; projected Gram determinant residue 655970 mod 1000003. |
| `|01⟩−|10⟩` | Exact full-graph signed relabeling of the preceding atom, including private vertices and transported filling. |
| Three-term representative | 41 vertices, 322 edges; clique counts 41,322,914,1082,477,30; ranks 40,282,632,447,30; target Betti number 3; 382-term integer filling; zero-pair rank 902 with kernel 4+176; projected 176×176 Gram determinant residue 797443 mod 1000003. |
| Four Hadamard atoms | Exact signed petal relabelings of the representative, with chain isometries and transported fillings. |
| Selected-cycle guards | Proof of the clique-union identity, relative join-chain decomposition in all degrees, exact boundary intersection, zero-weight kernel Q⊗span{γ_β}, projected-pair injectivity, and iteration through total locality six. |

The certificate proof must state explicitly:

- modular rank is a lower bound on rational rank;
- the displayed rational kernel supplies the matching upper bound;
- a determinant nonzero modulo a prime proves the integer determinant is nonzero;
- exact matrix multiplication verifies each filling;
- independent register cosets establish the reverse inclusion needed for exact filling;
- a finite minimum of all certified constants supplies one uniform palette constant.

A submission supplement should contain only immutable graph data, exact fillings, checker scripts, receipts, a short README, and provenance/license information. Do not point a double-blind submission to the present collaboration directory or its Git history.

Until this proposition and supplement exist, the unconditional hardness theorem is not supported at submission standard. The abstract transfer theorem remains safe as a conditional theorem.

---

## CRITICAL 3. The named BQP1^{G₂} source is used without a complete definition and exact soundness-normalization step

**Pointers**

- `manuscript_v0/sections/5_circuit.tex:84-92`, source verifier promise.
- `manuscript_v0/sections/5_circuit.tex:109-127`, Theorem `thm:weighted-hardness`.
- `manuscript_v0/sections/5_circuit.tex:129-132`, cyclotomic extension.
- `manuscript_v0/references.bib:34-42`, Rudolph entry.

The eight-label algebra is correct. The theorem nevertheless begins with a verifier already satisfying perfect completeness and soundness at most 1/3, then labels the target BQP1^{G₂}-hard. The paper neither defines the exact gate-dependent class nor invokes the exact soundness reduction needed when the source definition begins with an arbitrary inverse-polynomial rejection gap.

The required source interface is Rudolph’s Definition 2.2, Theorem 2.3, and Theorem 3.4: exact uniform clean-input/computational-basis-output circuits; exact soundness reduction inside gate sets containing G₂ while preserving perfect completeness; and the covered power-of-two-cyclotomic gate-family inclusion. Approximate compilation cannot replace these statements.

### Concrete replacement

Insert before `eq:bqp1-promise`:

> For a fixed exact gate set G, BQP1^G is used in Rudolph’s gate-dependent sense: a uniform family of exact G-circuits on a fixed all-zero input, with one computational-basis output measurement, perfect completeness, and an inverse-polynomial rejection gap. By Rudolph, Definition 2.2 and Theorem 2.3, for G=G₂ the soundness can be reduced exactly to at most 1/3, with polynomial overhead, while preserving perfect completeness and remaining inside G₂. We apply that transformation before the following combiner.

After the eight-label calculation, state:

> The map x ↦ (G_in(x),G_out(x),w,d,γ_in,γ_out) is a deterministic polynomial-time many-one reduction to the promise q_d≥3/4 versus q_d≤1/8.

The extension must remain “for each fixed finite gate family covered by Rudolph’s Theorem 3.4, separately.” Do not state gate-independent BQP1-hardness.

---

## CRITICAL 4. The reduction does not explicitly output λ and a certified rational gap promise

**Pointers**

- `manuscript_v0/sections/3_transfer.tex:83-115`, existence of palette constants and parameter inequalities.
- `manuscript_v0/sections/5_circuit.tex:120-127`, statement that the gap is inverse polynomial.
- `manuscript_v0/sections/6_unweighting.tex:7-18,58-65`, F=λ^{-2} and unweighted floor.

A many-one reduction must compute the complete target instance, including the dyadic vertex weight and endpoint gap bounds. The manuscript currently says “take λ=Θ(η/t_max)” and “the gap is inverse polynomial,” but does not output encoded numbers. The hidden constants come from a fixed finite palette, so this is repairable.

### Concrete replacement

Fix η₀=1/10. After the palette appendix supplies hard-coded rational constants c_λ,c_E>0, define

- `t_max = max{1,t_in,t_out}`;
- `b = ceil(log_2(2 t_max/(c_λ η₀)))`;
- `λ = 2^{-b}`;
- `g = min{1/(8L²), 1/[3L(8L²+1)]}`;
- `E = c_E η₀² g λ^{26}`, or a smaller dyadic rational below this expression.

Adjust c_λ once so that λ≤c₀/t_max and t_max λ² is below the structural-error budget. State that b=O(log t_max), the bit lengths of λ and E are polynomial, F=λ^{-2}=2^{2b} is polynomial, and the same λ is used at both levels.

Distinguish t_max, the number of global projector terms/gadgets, from the original circuit-gate count and from the ranks of padded projectors.

---

## CRITICAL 5. Source comparison and bibliography are inconsistent with the disclosure

**Pointers**

- `manuscript_v0/sections/7_related_work.tex:9-17`, version-specific King–Kohler criticism and admission that the final SIAM proof was not checked.
- `manuscript_v0/sections/B_source_details.tex:102-105`, repeated unresolved published-version check.
- `manuscript_v0/references.bib:12-21`, only arXiv v2 is cited.
- `manuscript_v0/main.tex:43-49`, disclosure asserting independent checking of source attributions.

The King–Kohler paper is published in *SIAM Journal on Computing* (online 2 January 2026, DOI 10.1137/24M1710243, pages FOCS24-137–FOCS24-235). The manuscript criticizes a specific arXiv-v2 argument while admitting that the final published proof was not checked. That is acceptable only if the discussion is explicitly version-scoped and makes no priority claim. It is inconsistent with the disclosure’s unconditional statement that all source attributions were independently checked.

### Concrete replacement

The preferred repair is to inspect the final SIAM text. If access is unavailable before submission, replace the disputed paragraph by:

> King and Kohler prove a many-gadget spectral reduction under a positive-definite logical promise. Our theorem is formulated independently from finite zero-weight certificates and yields a uniform all-chain estimate for possibly degenerate logical kernels. In arXiv version 2, the displayed padded coordinate-bulk estimate does not cover deletion of a weight-one outside-register vertex. Our proof does not use that estimate: it projects the fixed local private pair onto outside harmonics in every bidegree. We make no claim here about whether an equivalent repair appears in the final published version.

Update the bibliography to include the published SIAM article. If the arXiv-v2 issue remains, retain a separately keyed arXiv-v2 entry and cite it only for the version-specific sentence.

Unless all checks are completed, replace the disclosure’s verification sentence by:

> The authors reviewed and take full responsibility for every mathematical claim, citation, and statement in the final submission.

Do not claim independent verification of a source that the paper says was not checked.

---

## CRITICAL 6. The certificate material cannot be submitted through the current repository without breaking anonymity

**Pointers**

- `manuscript_v0/main.tex:24`, `Anonymous Authors`.
- `manuscript_v0/sections/5_circuit.tex:32-36` and `B_source_details.tex:76-105`, which require external certificate support.
- The present repository path, Git history, archived model reviews, dispositions, and unrelated projects.

The manuscript source itself is anonymized. The repository and collaboration archive are not. Linking the current branch as supplementary evidence would reveal authorship and expose irrelevant material. This is submission-blocking because the finite palette needs a checkable supplement.

### Concrete replacement

Create an immutable anonymous supplement containing only:

1. graph/certificate JSON files;
2. the authors’ independent checker scripts;
3. offline receipts;
4. a short reproduction README with exact commands and hashes;
5. provenance crediting Rudolph’s upstream construction and recording its immutable commit/hash;
6. applicable license notices.

Remove usernames, absolute paths, identifying internal dates, Git history, model-review transcripts, repository links, and unrelated research. Check the final PDF metadata with `pdfinfo` and inspect every supplementary archive before upload.

---

## MAJOR 1. “Rank-one projector” is inconsistent between the active local atom and the padded global term

**Pointers**

- `manuscript_v0/sections/2_preliminaries.tex:34-43`.
- `manuscript_v0/sections/3_transfer.tex:7-23`.
- `manuscript_v0/sections/3_transfer.tex:55-70`.

The active projector on V_a is rank one. After padding unused register factors, the global term is generally `Π_j = π_a ⊗ I_out` and can have high rank. The global proofs need only an orthogonal projector. Calling every global Π_j rank one is false and obscures term-count bookkeeping.

**Replacement:**

> Each active local atom is a rank-one projector π_a on its active logical register V_a. After padding unused logical factors, the global term is the orthogonal projector Π_j=π_a⊗I_out, which need not have rank one. The global transfer argument uses only positivity and projectivity.

---

## MAJOR 2. The wording for Q_a can exclude the selected-cycle guard actually used

**Pointers**

- `manuscript_v0/sections/3_transfer.tex:18-36`.
- `manuscript_v0/sections/5_circuit.tex:32-36`.

“Private-coordinate subspace” can be read as a coordinate span. The selected-cycle guard has `Q′=Q⊗span{γ_β}`, which is contained in private coordinates but is not generally spanned by individual simplex vectors.

**Replacement:**

> Q_a is an orthogonal subspace contained in the span of private simplex coordinates; it need not itself be a coordinate subspace or possess a simplex basis.

This matches the proof, which uses only private support, orthogonality, and projected-pair injectivity.

---

## MAJOR 3. The rank-deficient singular-value scaling lemma is used but not proved

**Pointer:** `manuscript_v0/sections/3_transfer.tex:44-53`.

The scaling is correct even when a boundary is rank deficient. Add:

> **Lemma.** If A is rectangular and L,R are invertible, then σ_min^+(LAR) ≥ σ_min(L) σ_min^+(A) σ_min(R). Zero-rank matrices are omitted.
>
> **Proof.** Put K=ker A. If ||x||=1 and x is orthogonal to ker(LAR)=R^{-1}K, then
> dist(Rx,K)=inf_{z∈R^{-1}K} ||R(x−z)|| ≥ σ_min(R).
> Since A vanishes on K, ||ARx|| ≥ σ_min^+(A) dist(Rx,K); left multiplication by L proves the claim.

Then derive the two boundary exponents in degree d_a and take the worse value `2d_a+4=4m_a+2`.

---

## MAJOR 4. All-bidegree padding is too compressed for a load-bearing repair

**Pointer:** `manuscript_v0/sections/3_transfer.tex:55-70`.

The statement is correct, but this is where an earlier false two-bidegree enumeration failed. The representative graph has degree-5 simplices although its target degree is 3. Display the full reduced join decomposition:

> In augmented reduced chains,
> `C_d(Y_a*R_out) = ⊕_{r+s=d−1} C_r(Y_a)⊗C_s(R_out)`,
> and on each summand
> `Δ = Δ_{Y_a,r}⊗I + I⊗Δ_{R_out,s}`.
> If R_out has augmented harmonics only in top degree q and a uniform positive gap elsewhere, and d=d_a+q+1, then the only outside-harmonic bidegree is (d_a,q). Every other actual bidegree, including r>d_a, has positive outside energy. The statement includes the empty outside factor in degree −1.

Explain that the zero-weight kernel and private projected pair are tensored only with the outside harmonic space.

---

## MAJOR 5. The history-gap proof does not fully expose the illegal-clock sector or endpoint scale

**Pointers**

- `manuscript_v0/sections/5_circuit.tex:38-58`.
- `manuscript_v0/sections/B_source_details.tex:1-36`.

The legal weighted-path calculation is sound, but the whole-Hamiltonian claim needs an explicit legal/illegal decomposition. State the unary clock, guarded propagation terms, invariance of the legal span, and unit penalty on illegal clocks. Also state that every gain edge is immediately followed by its loss edge, so `s_0=s_{L−1}=1`; otherwise the output compression acquires a final weight factor.

**Required insertion:**

> The legal unary clock states are |t⟩=|1^t0^{T−t}⟩ and H_clock=Σ_{j=1}^{T−1}|01⟩⟨01|_{j,j+1}. Propagation, input, and output projectors include the standard neighboring clock guards and preserve the legal-clock span; by Hermiticity its orthogonal complement is invariant. Every illegal computational-basis clock string has H_clock energy at least one. Hence the whole-space gap is the minimum of one and the legal weighted-path bound. Each gain step is immediately followed by its matching loss step, no gate is inserted between them, and s_0=s_{L−1}=1.

The appendix should explicitly prove the clean mean-zero and dirty anchored inequalities for the complete legal kernel.

---

## MAJOR 6. The coefficient-field bridge is absent

**Pointers**

- `manuscript_v0/sections/2_preliminaries.tex:1-10`, chains over C.
- `manuscript_v0/sections/3_transfer.tex:40-43` and `B_source_details.tex:76-105`, integer/rational certificates.

Add:

> All graph boundary matrices and certified fillings are defined over Q. Rank, kernel dimension, image intersection, and filling validity are unchanged under scalar extension Q⊂R⊂C. Every real symmetric positive-semidefinite inequality used below complexifies verbatim. We state the homological results over C while certifying finite data over Q.

---

## MAJOR 7. State the exact reduction type and target precision at theorem level

**Pointer:** `manuscript_v0/sections/5_circuit.tex:109-127`.

The theorem should say “deterministic polynomial-time many-one reduction” and name the target decision promise. The threshold and precision arithmetic are correct:

- midpoint: `(3/4+1/8)/2 = 7/16`;
- half-gap: `(3/4−1/8)/2 = 5/16`;
- error 1/24 is safe.

State success probability at least 2/3 and standard repetition if another confidence is desired.

---

## MAJOR 8. The unweighting corollary is sound but needs theorem-level attribution and convention boundaries

**Pointers**

- `manuscript_v0/sections/6_unweighting.tex:1-75`.
- `manuscript_v0/references.bib:52-61`.

The section is correct under Hayakawa’s Lemma 4.2 and Theorem 4.3. Cite those numbers where the symmetric identity and asymmetric floor are invoked. State explicitly:

- the imported theorem is first used over its real chain convention and then complexified;
- identical labeled copy blocks are used at both levels;
- every future private vertex is already present with its final weight but isolated initially;
- λ is the explicit dyadic produced by the reduction;
- the full gap is `min{F E_i,min_v f_v}=min{F E_i,1}`;
- the step is a short corollary of Hayakawa, not a new unweighting mechanism.

---

## MAJOR 9. Polynomial output size is asserted but not costed

**Pointers**

- `manuscript_v0/sections/5_circuit.tex:120-127`.
- `manuscript_v0/sections/6_unweighting.tex:7-18,58-65`.

Add a size lemma. With n logical bowties, t fixed-size active interiors, and constant locality, the weighted graph has O(n+t) vertices and at most O(n²+tn) explicitly generated edges. After blow-up with maximum block size F, a safe bound is O(F(n+t)) vertices and O(F²(n²+tn)) edges. Both are polynomial because F=λ^{-2}=poly(|x|). Give the deterministic label/edge-generation algorithm and do not charge the exponentially many clique simplices as explicit input.

---

## MAJOR 10. Bibliographic records and theorem-specific citations are incomplete

**Pointers**

- `manuscript_v0/references.bib:1-71`.
- `manuscript_v0/sections/7_related_work.tex:1-55`.

Minimum repairs:

1. Add the 2026 *SIAM Journal on Computing* King–Kohler article, DOI 10.1137/24M1710243, pages FOCS24-137–FOCS24-235; retain a separately keyed arXiv-v2 record only for version-specific discussion.
2. Complete Rudolph’s proceedings entry: LIPIcs volume 386, pages 98:1–98:19, editors Michal Koucký and Daniela Petrișan, Schloss Dagstuhl, DOI 10.4230/LIPIcs.MFCS.2026.98; retain the arXiv full version if theorem numbering differs.
3. Record Mémoli–Wan–Wang as *SIAM Journal on Mathematics of Data Science* 4(2):858–884 (2022), DOI 10.1137/21M1435471, rather than only `@misc`.
4. Pin the exact arXiv versions/dates used for Lowe and Hayakawa.

Use theorem/lemma numbers for load-bearing interfaces: King–Kohler’s many-gadget proof, Gyurik et al.’s whole-kernel and simulated-register lemmas, Lowe et al.’s Problem 9 and Conjectures 1–2, Hayakawa’s Lemma 4.2 and Theorem 4.3, and Rudolph’s Definition 2.2 and Theorems 2.3 and 3.4.

The comparison-table phrase “NO-case focus” is imprecise; replace it with a neutral description of the exact theorem statement.

---

# II. Minor findings

1. Define `γ_+(A)` and the up/down Laplacians explicitly.
2. Do not call g_A “the smallest positive eigenvalue” when H_A=0. Call it a certified coercivity constant satisfying the displayed operator inequality.
3. Protect empty term sets with `t_max=max{1,max_A |A|}`.
4. Replace “Exact filling chains certify (i)” by “fillings prove one inclusion; matching ranks and surviving cosets, or the guard connecting-map theorem, prove equality.”
5. Adapt the AI disclosure and bibliography/appendix order to the venue template.
6. Do not submit historical archive records with stale labels such as “complete palette open”; create one current supplement manifest.
7. State the oriented-simplex convention and note that globally sorted order differs by signed permutation conjugation only.
8. Retain the exclusions of ordinary BQP, unrestricted SDQC1, gate-independent BQP1, arbitrary complex phases, practical performance, and “first quantum persistence.”
9. This review did not independently run `latexmk`, render the PDF, inspect overfull boxes, or inspect PDF metadata. Run the final venue toolchain and archive its log.

---

# III. Mathematical chain audit

## A. Finite-certificate arbitrary-chain transfer

**Status: mathematically sound under the displayed hypotheses; manuscript instantiation incomplete.**

The proof in `sections/A_transfer_proof.tex` correctly separates:

1. shared-register boundary interference, controlled through the block row `[L_1 … L_t]` without assuming shared-output orthogonality;
2. zero-weight leakage away from V⊕Q_j;
3. private-pair coercivity on Q_j, whose retained outputs are gadget-private;
4. absorption of χλ²U while retaining the actual private mass U;
5. direct logical coercivity from exact filling and the local whole-positive gap.

The resulting estimate

`||(I−P_{K_A})x||² ≤ C[t_A λ² + <x,Δ_A x>/(g_A λ^{26})]`

is valid for every unit geometric chain when λ≤c/t_max. No estimate against the unknown geometric harmonic projector enters the leakage proof.

Necessary written repairs are the rank-deficient scaling lemma, all-bidegree padding lemma, non-coordinate interpretation of Q_j, and palette-instantiation proposition.

## B. Exact complete kernel and inverse-polynomial floor

**Status: sound.**

The low-energy subspace argument is exact, not a relabeling of near-zero modes. Projection to K_A is injective on the entire spectral subspace below E_A, giving the upper dimension bound. Exact filling and independent interiors inject V/W_A into homology and supply the matching number of exact zeros. Equality forces

`dim ker Δ_A = dim K_A` and `spec(Δ_A) ∩ (0,E_A) = ∅`.

If K_A=0, the low-energy subspace is zero and the whole spectrum starts at E_A. No global relative-acyclicity assumption is needed once concentration and the quotient injection are both proved.

## C. Quotient naturality

**Status: sound.**

`sections/4_quotient.tex` correctly proves `B_d(X_A)∩V=W_A` using independent private coordinates, then identifies H_d(X_A) with V/W_A after the dimension equality. For A⊆B, both paths send a register cycle v to the same class in X_B, so the map is the natural quotient `V/W_A → V/W_B`. It is surjective and has rank `dim(V/W_B)=dim K_B`, including K_B=0. Exact compatible harmonic representatives are unnecessary for this algebraic rank statement.

## D. Eight-label source

**Status: algebraically sound; source-class formalization must be added.**

Because the label is preserved and the Boolean predicate is computed into a fresh clean decision bit with scratch uncomputed, compression through the clean verifier gives exactly

`M_x = diag(1,p_x,p_x,p_x,p_x,p_x,0,0)`.

Entanglement of the measured output with verifier workspace is included in the scalar p_x. In YES, the perfect fraction is 6/8=3/4. In NO, only the unconditional block is perfect, giving 1/8, and all other eigenvalues are at most 1/3. Threshold 7/16 and error 1/24 are safe.

The recognized gate-dependent hardness statement requires the class definition and exact Rudolph soundness step in CRITICAL 3.

## E. Weighted-to-unweighted transfer

**Status: sound as a short corollary of Hayakawa, conditional on the weighted theorem.**

For integers `f_v=F w(v)^2`, the normalized orbit isometry obeys `Δ_hat U = F U Δ`. Hayakawa’s asymmetric-sector theorem excludes additional harmonic vectors. Identical labeled blocks at both levels give `J_hat U_1 = U_2 J`, so endpoint kernels and induced rank are preserved. For weights 1 and dyadic λ, `F=λ^{-2}` gives minimum multiplicity one and gap floor `min{FE,1}`. The spectral mechanism is Hayakawa’s; the filtration commuting square is the elementary additional observation.

---

# IV. Frozen safe-claim list

## Safe now as conditional mathematical statements

1. Any fixed palette satisfying exact filling, zero-weight kernel, projected private-pair, outside-harmonic padding, interface, and independent-interior hypotheses obeys the all-chain concentration estimate with κ=4m+2.
2. Under the same hypotheses and logical coercivity, the geometric kernel has exactly the logical-kernel dimension and the remaining spectrum has the displayed floor, including a zero-dimensional logical kernel.
3. For nested term sets, H_d(X_A) is naturally V/W_A and the induced rank is the later logical-kernel dimension.
4. The eight-label compressed operator and fractions 3/4 and 1/8 are exact.
5. Given Hayakawa’s symmetric/asymmetric decomposition and common labeled multiplicities, the weighted and unweighted diagrams have the same endpoint Betti numbers, induced ranks, normalized ratio, and the scaled gap floor.

## Safe as unconditional manuscript claims only after the stated repairs

6. Complete fixed-palette instantiation: after Appendix C and an anonymous exact-certificate supplement establish every atom and guard.
7. Weighted BQP1^{G₂}-hardness: after the class/interface definition, Rudolph exact soundness step, explicit parameter algorithm, and formal target definition are inserted.
8. Unweighted BQP1^{G₂}-hardness: after item 7 and theorem-specific Hayakawa attribution/common-block conventions are formalized.
9. Covered cyclotomic families: only as a separate statement for each fixed finite gate set satisfying Rudolph’s exact Theorem 3.4 hypotheses.

## Claims that must remain excluded

- ordinary BQP-hardness;
- unrestricted SDQC1-hardness;
- gate-independent BQP1-hardness;
- arbitrary complex-phase extension;
- a general integer-state gadget theorem;
- a new unweighting mechanism;
- “first quantum persistence” or “first normalized-persistence problem”;
- an optimal gap exponent or practical quantum advantage.

---

# V. Minimum submission sequence

1. Add the weighted and unweighted target definitions and decision promise.
2. Add the palette-certification proposition, exact table, guard proof, and anonymous supplement manifest.
3. Add the rank-deficient scaling and all-bidegree padding lemmas.
4. Complete the legal/illegal unary-clock proof and state `s_0=s_{L−1}=1`.
5. Define BQP1^{G₂}, cite Rudolph Definition 2.2/Theorems 2.3 and 3.4, and state the exact many-one reduction.
6. Make λ,E,F explicit encoded outputs and add the graph-size lemma.
7. Update King–Kohler source comparison and bibliography; reconcile the AI disclosure.
8. Build an anonymized supplement and inspect PDF/archive metadata.
9. Run final venue compilation and a clean-room certificate replay; archive logs and hashes.
10. Perform a final theorem-by-theorem dependency check against the revised PDF rather than the mutable source tree.

After these repairs, the paper is a coherent submission candidate. Before them, the draft overstates the evidence level of the palette-instantiated hardness theorem and does not define its target problem precisely enough for a complexity submission.
