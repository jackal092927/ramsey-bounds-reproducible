# Quantum TDA and hyperbolic-navigation direction selection

Date: 2026-09-02 (America/Los_Angeles).

## Scope and status

This is an ongoing mathematical exploration, not a submitted paper or a correctness certificate for the full reduction. Current work focuses on true normalized persistence. The user has now requested a consolidated GitHub archive and Pro review followed by substantive proof development. Both earlier Pro responses have been completed and collected. The separate QuantumTDA and NaviGraph manuscripts were not changed by this consolidation.

Current entry point: [research dossier and Pro collaboration](collaboration/2026-09-02/README.md), with [milestones](collaboration/2026-09-02/MILESTONES.md), [audit corrections](collaboration/2026-09-02/AUDIT_CORRECTIONS.md), and [execution state](collaboration/2026-09-02/COLLABORATION_STATE.json). The [round-2 report](round2/IDEA_REPORT.md), [first-round decision](DECISION_2026-09-02.md), original prompts, and [first dispatch receipt](PRO_DISPATCH_2026-09-02.md) are retained as dated historical records; their old 'not sent/collected/pushed' statements describe their original preparation time. Current lifecycle claims come from the new execution receipt. Older 'verified source' labels report those prior reading passes, not a complete new literature audit by this consolidator.

Supporting material:

- [TDA literature map, native simplicial obstruction and candidate lemmas](tda_probe/PROBE_REPORT.md)
- [Conditional functorial unweighting corollary](tda_probe/UNWEIGHTING_FIRST_LEMMA.md)
- [AIDA exact update-rank obstruction](AIDA_UPDATE_TRIAGE.md)
- [Hyperbolic landmark proof and progress-density calculation](hyperbolic_probe/PROOF_PACKAGE.md)
- [Quantum hyperbolic LSH literature and full-cost comparison](lsh_probe/2026-09-02-quantum-hyperbolic-lsh-triage.md)
- [Sent TDA Pro payload](PRO_REVIEW_TDA_PREPARED.md)
- [Sent hyperbolic Pro payload](PRO_REVIEW_HYPERBOLIC_PREPARED.md)
- [Round 2 exact-kernel transfer lemma and open dependencies](round2/NORMALIZED_PERSISTENCE_PROBE.md)
- [Round 2 candidate generation and kill tests](round2/IDEA_GENERATION_54.md)
- [Explicit supported weighted-history palette and gap proofs](round2/UNARY_PALETTE_ADDENDUM.md)
- [Secondary quantum net and barcode query bounds](round2/QUANTUM_NET_PROOF.md)
- [Independent mathematical review and resolution](round2/REVIEW_RESOLUTION.md)

## Reproduction

The root independently reran the first-round probes and all four round-2 probes successfully. Tested environment: Python 3.11.15, NumPy 2.4.4, SciPy 1.17.1. The hyperbolic probe uses only the Python standard library. The Möbius probe uses rational arithmetic from `fractions` for the local exact certificate, plus NumPy/SciPy for numerical checks. The common-blow-up probe uses NumPy. Round-2 matrix probes use NumPy/SciPy; the padded-bulk and barcode-outlier checks use exact rational arithmetic.

From this directory:

```sh
python3 tda_probe/check_mobius_zigzag.py
python3 tda_probe/check_common_blowup.py
python3 hyperbolic_probe/probe.py
python3 round2/check_kernel_filtration.py
python3 round2/check_weighted_history.py
python3 round2/check_padded_bulk.py
python3 round2/check_barcode_outlier.py
```

All print their results explicitly; the matrix probes use JSON and the padded-bulk probe prints exact fractions. Expected key outputs:

- Möbius band: 12 vertices, 30 edges, 18 triangles, harmonic H1 dimension 1; exact `a_squared=41/86`, `b_squared=41/344`; exact boundary/filling ranks both 18.
- At 32 bands: generalized rank 1, D/B singular gaps approximately 0.21824/0.21831, projector cosine approximately 6.09612e-9.
- Hyperbolic checks: `status=PASS`; full-rank H2/H3 and a geodesic in H5; maximum observed score error approximately 1.78e-15.
- Common-multiplicity check: path-to-triangle filtration, seven copied vertices, multiplicities (4,1,2), common M=4; inclusion residuals zero and operator residuals at most 7.7e-16. Changing one vertex's multiplicity from one to two breaks inclusion compatibility, with residual approximately 0.76537.
- Independent filling: sixteen vertices; degree-three Betti counts `[4,2,1]`, successive map ranks `[2,1]`, for weights `1, 1/2, 1/4, 1/8`.
- Weighted history: kernel pairs `[4,1]` and `[4,3]`, fractions `0.25` and `0.75`; a separate twelve-dimensional fixture has initial nullity four, final nullity zero, and final minimum eigenvalue about `0.11808`.
- Padded bulk: at weight `1/256`, unrestricted squared boundary norm is `131073/65536`, while its outside-harmonic counterpart is `1/65536`.
- Barcode outlier: all `2080` singleton positions for sizes `1..64` pass the exact maximum-length separation; the appended-short-bar example has diagonal cost `1/2000` and refutes using maximum death coordinate of an arbitrary approximate barcode.

Floating-point last digits may differ across numerical-library builds. They are not used to prove the infinite-family statements. The reports give analytic proofs separately. These checks are not quantum circuit simulations and do not demonstrate an end-to-end runtime advantage.

No expensive remote computation is required for these checks; their purpose is to reject or support specific mathematical steps before scaling experiments.

The consolidation reran all seven listed checks and archived [their full output](collaboration/2026-09-02/REPRODUCTION_RESULTS.json). A new [persistent-domain check](collaboration/2026-09-02/check_persistent_laplacian.py) also passes for a four-cycle filled through a later diagonal; it supports the finite implementation in the [conditional persistent-Laplacian extension](collaboration/2026-09-02/PERSISTENT_LAPLACIAN_EXTENSION.md), not its priority or the imported general spectral theorem.
