# Hostile novelty-collision audit for true normalized persistence

September 3, 2026. **TARGETED PRIMARY-SOURCE PASS COMPLETED; MATHEMATICAL PACKAGE REMAINS CONDITIONAL ON ITS RECORDED FINITE CERTIFICATES; PRIORITY IS NOT CERTIFIED.** This audit separates statements found in the cited sources, local mathematical deductions, and absence claims. It is not an exhaustive literature search and does not certify paper readiness.

## Verdict

Current priority/value is **MEDIUM, conditional**. The construction appears capable of resolving a restricted form of exact normalized harmonic persistence hardness for weighted clique complexes, with inverse-polynomial gaps above both complete endpoint kernels. That is a real theorem target. It is not presently a safe high-impact claim because the analytic mechanism lies very close to the many-gadget proof already written by King--Kohler, a particular degenerate whole-kernel gap is already claimed by Gyurik et al., and the eight-label source and quotient/min--max closure are elementary.

The strongest defensible framing is:

> A finite-certificate transfer theorem for degenerate frustration-free logical kernels, yielding exact endpoint multiplicities, an inverse-polynomial gap above the entire geometric kernel, and the natural persistent rank for nested term sets; applied to a fixed exact real gate family to obtain a restricted true-normalized-persistence hardness theorem.

Do not claim the first quantum persistence result, a new normalized-persistence definition, the first exact multiplicity reduction, a proof of the unrestricted normalized-harmonic-persistence conjecture, unrestricted \(\mathsf{SDQC}_1\), ordinary BQP, or a new unweighting mechanism.

## Source collisions and what remains

### 1. Crichigno--Kohler: exact multiplicity is old

The [Nature Communications paper](https://www.nature.com/articles/s41467-024-54118-z) gives a parsimonious quantum-kSAT-to-clique-homology reduction and derives counting hardness from the correspondence between satisfying states and holes. It also explains that the hard instances need not satisfy the gapped promise and points to modifying the reduction as future work.

**Collision:** exact kernel/homology multiplicity alone is not new.

**Remaining delta:** simultaneous exact multiplicity and an inverse-polynomial gap above a possibly degenerate whole kernel, together with a filtered-rank statement.

### 2. King--Kohler: the load-bearing estimate may be a short extension

The formal many-gadget theorem in [arXiv:2311.17234v2](https://arxiv.org/html/2311.17234v2) treats a nonempty logical kernel as a YES witness and proves a lower spectral bound in the NO regime \(H\succeq gI\). It does not state the general conclusion
\[
\dim\ker\Delta=\dim\ker H,
\qquad
\operatorname{spec}(\Delta)\cap(0,E)=\varnothing
\]
for arbitrary degenerate \(\ker H\).

However, its proof starts with an arbitrary normalized geometric chain, identifies the embedded logical energy, and bounds the penalty/bulk sectors before it invokes \(H\succeq gI\). Replacing the final coercivity step by
\[
H\succeq g(I-P_{\ker H})
\]
is therefore close to the existing proof architecture. Our finite-certificate route also repairs the padded-bulk issue and makes the arbitrary-chain statement explicit, but a referee may still judge the degenerate-kernel theorem to be a careful corollary rather than a new mechanism.

**Mathematical status:** no counterexample was found under the displayed finite-certificate, private-support, and independent-interior hypotheses.

**Novelty risk:** high. A line-by-line theorem comparison is the decisive stop/go gate.

### 3. Gyurik et al.: do not claim the first whole-kernel gap

[arXiv:2410.21258v2](https://arxiv.org/html/2410.21258v2) proves BQP1-hard harmonic survival for a specified guide and states a gap above the whole final harmonic space in its particular construction. The displayed proof applies a lemma stated for a simulated-register vector while discussing an arbitrary low-energy geometric chain. That is an apparent domain mismatch, not a demonstrated counterexample to the published theorem.

**Collision:** a particular degenerate whole-kernel gap claim already exists.

**Remaining delta:** an independent arbitrary-chain proof with explicit finite hypotheses, plus uniform initial-homology survival rather than one guided vector.

### 4. Lowe--Kim--Bondesan--Hayakawa: the target and stronger conjecture are prior

[arXiv:2607.03278v1](https://arxiv.org/html/2607.03278v1) already defines Normalized Harmonic Persistence as
\(\beta_d^{1,2}/\beta_d^1\), conjectures \(\mathsf{SDQC}_1\)-hardness, and asks for exact kernel multiplicity, gaps, and compatible harmonic isometries across a filtration.

Our nested-term-set argument does not prove that stronger isometry conjecture. It instead uses exact filling and independent interiors to identify each homology group with
\[
V/W_A
\]
and the inclusion map with the natural quotient \(V/W_A\twoheadrightarrow V/W_B\). This bypasses the need for literal compatible harmonic representatives for this restricted family.

**Genuine but narrow delta:** a quotient-based route to the required persistent rank in a restricted filtration. The quotient dimension and min--max steps themselves are standard.

### 5. Hayakawa: common-copy unweighting is likely available, but not novel

[arXiv:2608.02726v1](https://arxiv.org/html/2608.02726v1) proves the single-level symmetric-sector reduction and asymmetric-sector gap for clique blow-ups. With one common integer multiplicity \(f_v=Fw(v)^2\) for every shared vertex and the same labeled copy block at every filtration level, the normalized orbit isometries obey
\[
\widehat J U_1=U_2J.
\]
Thus endpoint kernels and the induced homology rank are naturally preserved. For the present two-weight construction, dyadic \(\lambda\) permits \(F=\lambda^{-2}\), polynomial blow-up, and gap floor \(\min\{FE,1\}\). Future gadget vertices can be present initially as isolated vertices; since \(d\ge1\), they add no target-degree chains.

**Mathematical status:** no remaining functoriality obstruction is visible, conditional on the cited single-level decomposition and on using a common vertex/block set. The existing local proof should be promoted only after a final convention and size audit.

**Novelty status:** likely a direct corollary, useful for strengthening the target from weighted to unweighted but not a paper's main idea.

## Claim decomposition

| Component | Mathematical status | Novelty status |
| --- | --- | --- |
| Fixed finite clique-gadget palette | Exact local certificates recorded | Credited implementation work; low conceptual novelty |
| Arbitrary-geometric-chain concentration toward embedded \(\ker H\) | Load-bearing theorem, conditional on recorded finite hypotheses | Potentially genuine as a clean repair/general transfer statement; strong King--Kohler collision |
| Exact geometric kernel multiplicity and whole positive gap | Follows from concentration plus injection | Standard dimension/min--max consequence; not the headline novelty |
| Natural filtered rank \(\dim\ker H_B\) | Follows from exact filling and quotient naturality | Useful restricted bypass of compatible-isometry conjecture; algebra itself standard |
| Eight-label \(3/4\)-versus-\(1/8\) BQP1 source | Algebraically accepted | Elementary reduction; supporting lemma only |
| Common-copy unweighting | Local functorial proof appears complete under Hayakawa's theorem | Likely direct corollary |
| Padding-generated denominator | Mathematically valid | Significant impact/exposition weakness |
| Gap \(E=\Omega(\eta^{28}g/t^{26})\) | Inverse polynomial | Structurally adequate, practically very poor |

## Submission gate

Proceed only if at least one of the following survives hostile comparison:

1. The finite-certificate theorem isolates assumptions and proves a degenerate-kernel transfer statement not obtainable by simply changing the last paragraph of King--Kohler.
2. The quotient construction resolves the normalized-persistence conjecture for a natural restricted class in a way not already present in Gyurik et al. or Lowe et al.
3. The common-copy argument upgrades the complete construction to an unweighted theorem with a clean filtration-level commuting diagram and polynomial gap/size bounds.

Downgrade to **LOW as a standalone theory paper** if King--Kohler's displayed inequalities plus the already-known single-gadget topology immediately imply the same degenerate-kernel theorem and if Gyurik et al. already supply a valid arbitrary-chain closure. Upgrade toward **HIGH** only after an unconditional unweighted theorem and either a broadly reusable degenerate-kernel transfer theorem or a source whose initial homology denominator is structurally intrinsic rather than dominated by idle padding.

## Evidence boundary

This pass targeted the six ledger sources and the nearby normalized persistent Betti algorithm literature. It checked the specific theorem/definition/proof locations summarized above. It did not exhaust later versions, citations, independent papers, conference proceedings, or unpublished work. Search nonappearance was not treated as evidence of novelty. The full reduction and local certificate family were not recertified during this source pass.
