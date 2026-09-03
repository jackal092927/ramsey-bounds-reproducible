# Quantum submission readiness and JLRX comparison

Date: 2026-09-01 (Pacific time)

## Disposition

**Submission candidate after the scoped corrections below.** No fatal defect
in the main quantum-query upper bound was found in this pass. This is an
author-side mathematical assessment, not a formal verification or a human
peer-review verdict. Novelty and ITCS significance remain judgment calls.

An answer from the JLRX authors is desirable but is **not a prerequisite for
submission**. The appropriate requirement is an independently supported
proof, explicit model alignment, and accurate disclosure of the discrepancy.
The user reports having sent the clarification email. No author reply or
acknowledgment is incorporated into the present manuscript.

## Primary-source comparison checked

The comparison is pinned to the FOCS 2024 proceedings version:

- Definition II.6 and the convention following II.7, p. 413: graph size
  `N=2^n`, default target `K=n/2`.
- Lemma III.1, p. 414, and Theorem I.3: with range size `H` and graph size
  `G`, the displayed sufficient condition is `G >= H^(4t)/4^t`.
- The unnumbered query-complexity paragraph, p. 415: the printed quantum
  consequence is `N^(1-o(1))`.
- Liu--Zhandry, *On Finding Quantum Multi-collisions*, arXiv:1811.05385v2:
  the constant-multiplicity exponent is
  `alpha_t=(2^(t-1)-1)/(2^t-1)` in the range size.

At `G=Theta_t(H^(4t))`, the direct transferred exponent is
`alpha_t/(4t)`. It is `1/24` at `t=2`; for `t>=3`,
`alpha_t/(4t)<1/(8t)<=1/24`. This is a statement about the direct use of
these ingredients, not an upper bound on every possible lower-bound method.
The fixed-`t` theorem cannot simply be substituted at growing `t`.

The graph-hash product has a symmetric, zero-diagonal implementation using
a constant number of coherent value-oracle queries. The arbitrary-encoding
corollary and the stronger output size of our algorithm address the other
obvious model differences. The main algorithm does not invoke either JLRX or
Liu--Zhandry. Their principal TFNP separation theorems are outside this audit.

Primary sources:

- [JLRX proceedings PDF](https://ieee-focs.org/FOCS-2024-Papers/pdfs/FOCS2024-1oojWxXs5YAKfs3z3lBRMF/167400a406/167400a406.pdf)
- [Liu--Zhandry](https://arxiv.org/abs/1811.05385)
- [Random-Painter comparison, Theorem 16 and its weight argument](https://arxiv.org/html/1806.09726v2)

## Mathematical and presentation corrections made

1. **Classical baseline.** The earlier `<2M` claim omitted the truncation
   needed to force geometric set sizes. Retaining a whole majority class on
   a monochromatic graph can take `Theta(KM)` queries. The paper now retains
   exactly `s_i/2` vertices at each classical level, proving `<2M` explicitly.
   This repairs the baseline description, not the quantum upper theorem.
2. **Conditional concentration.** The displayed Hoeffding probability now
   conditions explicitly on batch success and then bounds the joint event
   of batch success and inaccuracy. Batch failures are charged separately.
3. **Oracle costs.** The arbitrary-circuit reduction now uses `O(1)` queries
   including uncomputation. The graph oracle is explicitly symmetric and
   zero on the diagonal. The unsupported wording charging one edge-oracle
   gate cost for the entire run is removed: that cost occurs on every call.
   The paper consistently claims a query bound, not an end-to-end gate bound.
4. **Abort semantics.** A density violation is not magically detected. The
   algorithm aborts when a capped search/batch fails to return the required
   verified samples; it always respects the predetermined query cap.
5. **JLRX positioning.** The introduction has a short disclosure, and Section 6
   supplies the source locations, model check, and calculation. The discrepancy
   is no longer listed as a fourth algorithmic contribution or as the first
   algorithmic open problem. No claim of author acknowledgment is made.

The main recurrence, density constants, witness extraction, batch-uniformity
argument, and `O(2^K K log(K/eta))` query sum are unchanged. The randomized
lower bound remains below the quantum upper exponent; no separation from the
best randomized classical algorithm is claimed.

## Pro review lifecycle

The earlier complete quantum review remains recorded in
`CHATGPT_PRO_QUANTUM_REVIEW_DISPOSITION_2026-08-31.md`.

The registered conversation was reopened. Its latest differential-review
request is present, followed by interim analysis and a visible **network
error**, not a final report. The visible profile is Jackal Xin / Pro and the
account panel shows username `@xin.job2025`; the updated account panel did
not expose its email in this check. No final verdict was collected, no new
prompt was transmitted, and the partial response is not counted as proof or
as a completed review. The local channel status is recorded as blocked by
the network failure rather than running.

## Verification and remaining actions

The page and diagnostic details in this section describe the earlier AMS
layout. A subsequent layout-only migration to the official LIPIcs anonymous
template preserves the mathematical content, uses an ITCS-specific 11pt
adapter, and still produces 16 pages. In that current layout the main quantum
upper-bound proof ends on page 8, appendices start on page 12, and the
standalone build has no warnings. See `papers/quantum/SUBMISSION_CHECKLIST.md`
for the current PDF hash and `papers/quantum/TEMPLATE.md` for template details.

- The standalone and generated archival manuscripts compile successfully.
- The quantum self-check reports `QUANTUM_RAMSEY_AUDIT_PASS`.
- The existing repository quick reproduction completed with
  `QUICK_REPRODUCTION_PASS`. This is regression evidence, not a proof of
  the asymptotic quantum theorem.
- The standalone PDF remains 16 pages. Main upper-bound proofs finish on
  page 9; Section 6 begins on page 9 and its detailed comparison continues
  onto page 11. The introduction presents the merits and literature issue
  within the recommended first ten pages. Section 7 ends on page 11 and
  appendices begin on page 12.
- All fonts are embedded; no unresolved references/citations or overfull
  boxes occur. One nonfatal pdfTeX font-expansion warning remains. The
  generated archival PDF retains underfull-spacing diagnostics.
- Pages 10--11 containing the changed comparison and conclusion were
  rendered and visually checked for clipping and formula legibility.
- Existing 5,000 ideal-sampler runs and the isolated 16-state calculation
  remain proof-of-concept checks, not full coherent simulations or speedup
  measurements. No new simulation data were generated in this pass.
- Final human reading, acceptance of authorship responsibility, COI
  declaration, PDF upload, and final submission action remain to be done.
  The last saved HotCRP record is registered draft #193 with no PDF uploaded;
  a live server-state refresh could not be completed in this pass.

Readiness does not mean acceptance is likely or that no undiscovered error
exists. The strongest remaining scientific risk is whether the implicit-set
implementation and survival analysis are sufficiently novel and significant
for ITCS. Neither an extra AI verdict nor author silence should be confused
with a mathematical prerequisite.
