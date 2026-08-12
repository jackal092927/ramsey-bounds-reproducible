# Round 1 review

## External-review status

The research-refinement workflow called for a strict external Claude review.
That service was unavailable because its local client was not logged in.  No
external score was fabricated; this round is therefore recorded as **not
externally scored**.

## Internal adversarial audit

### Blocking concerns

1. Passing the HorizonMath validator does not by itself prove that the checked
   inequalities exactly instantiate the GNNW sufficient theorem.
2. The displayed GNNW theorem source appears to say `F'(lambda) < 0`, while its
   formula for `X` and the subsequent proof require the positive-derivative
   regime.  This looks like a typographical sign error, but it must be resolved
   explicitly.
3. The HorizonMath validator uses two admissibility mechanisms: Lemma 14 near
   zero and a numerical `R_0` inner region above `10^-3`.  Both mechanisms and
   their seam need a human proof audit.
4. The large-regime witnesses are piecewise constant.  The source theorem does
   not visibly require them to be smooth, but all quantifiers and endpoint
   conventions still need checking.

### Strengths

1. The proposal identifies a concrete live frontier and a finite certificate.
2. Baseline reproduction succeeded.
3. A tiny, interpretable coefficient change improves the implemented objective
   without exhausting the available margin.
4. The improvement is testable locally and does not depend on an opaque search
   model.

## Verdict

**REVISE.**  Freeze the candidate, move theorem auditing ahead of further
optimization, and do not state a Ramsey theorem until an independent checker
and the source-theorem derivation both pass.
