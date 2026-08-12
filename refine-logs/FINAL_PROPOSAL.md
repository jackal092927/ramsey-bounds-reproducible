# Superseded proposal: theorem-faithful certification of a diagonal Ramsey candidate

> **Superseded by `round-2-correction.md`.**  The frozen `3.6958799` artifact
> fails the corrected two-orientation Ramsey-region condition and is no longer
> an active candidate.  The active route is a corrected Arb verifier plus a
> cubic search against the published `3.7992` baseline.

## Objective

Determine whether the verifier-passing base
`c = 3.695879961267919` yields a rigorous bound

```text
R(k,k) <= c^(k+o(k)),
```

and, only after that question is settled, optimize it further.

## Frozen candidate

Use the HorizonMath arXiv v1 certificate unchanged except for

```text
a5: -0.0778 -> -0.07795.
```

The pinned public verifier accepts it with minimum reported slack
`0.00021556940670870104315`.

## Work packages and hard gates

### WP1: source-theorem audit

- Transcribe the exact sufficient theorem and define every variable.
- Resolve the apparent sign typo for `F'` using the proof, not intuition.
- Prove that the `R_0` support test used in code is a valid inner-region test.
- Verify the symmetric orientation logic.
- Verify piecewise-witness legality and all endpoint conventions.
- Prove overlapping validity across the `lambda=10^-3` split.

**Gate 1:** every program predicate has a numbered theorem/lemma derivation.

### WP2: independent interval verifier

- Reimplement formulas from the audited derivation, not from the existing code.
- Use an independently chosen interval library or exact rational enclosures.
- Validate the published `3.7992` parameters, the HorizonMath `3.6960839`
  certificate, and the `3.6958799` delta.
- Report interval coverage, outward-rounded `c`, and the location of each worst
  margin.

**Gate 2:** both verifiers agree and no interval is uncovered or inconclusive.

### WP3: constrained optimization

- Start with coefficient-only continuation around the frozen certificate.
- Then optimize piecewise `M,Y` witnesses with a minimum safety-margin target.
- Compile every candidate into the frozen certificate format.
- Reject improvements whose minimum certified slack is below a predeclared
  numerical safety floor.

**Gate 3:** a smaller outward-rounded base passes both verifiers.

### WP4: mathematical write-up

- State the result conditionally if any gate remains open.
- Include certificate provenance, hashes, verification commands, and complete
  proof obligations.
- Separate the optimizer from the proof artifact.

## Fallback

If Gate 1 fails because the validator checks a stronger-looking but unjustified
region or splice, document the obstruction and stop optimizing this ansatz.
The next project should be an explicit `R(4,t)` lower-bound graph search chosen
against the live AlphaEvolve certificate repository.  Every claimed improvement
must ship an adjacency certificate and two clique/independence checkers.

## Claim policy

- Now: “a smaller candidate accepted by the pinned public validator.”
- After Gate 1 only: “the implemented conditions have a theorem derivation.”
- After Gates 1 and 2: “independently certified candidate bound.”
- Only after complete mathematical review: “new Ramsey upper bound.”
