# Round 2 correction: orientation-union false positive

## Outcome

The independent theorem audit **rejected** both the HorizonMath
`3.6960839126332994` artifact and the local `3.695879961267919` delta as
Ramsey upper-bound candidates.

## Root cause

Let `a=-log x`, `b=-log y`, and let `U(mu)` certify a rate bound for
`0<mu<=1`.  Because the GNNW Ramsey region is defined by one pair `(x,y)` that
must bound `R(k,l)` for every sufficiently large ordered pair, symmetry of
`R(k,l)` imposes both

```text
a + mu*b >= U(mu),
b + mu*a >= U(mu)
```

for every `mu`.  HorizonMath's `B_of_a` returns `min(bu,bs)`, accepting either
orientation.  The required intersection uses `max(bu,bs)`.  The degree-5
candidate fails the omitted standard direction near `lambda=0.001` by roughly
`0.248`, far beyond interval-rounding uncertainty.

## Separate source typo

The displayed GNNW sufficient theorem writes `F'(lambda)<0`; its surrounding
derivation, the expression `1-exp(-F')`, and the induction proof require
`F'(lambda)>0`.  This is a source sign typo, distinct from the HorizonMath
orientation bug.

## Revised route

1. Treat the old degree-5 artifacts as negative regression cases.
2. Implement the Ramsey-region intersection independently with
   `python-flint`/Arb rather than porting `mpmath.iv` code.
3. Require the published GNNW cubic `3.7992` parameters to pass as a positive
   control.
4. Search the cubic family with both orientations.  A floating candidate near
   `3.7929` is under full interval verification; it has no claim status yet.
5. Promote a result only after complete interval coverage, positive margins,
   certificate provenance, and a human-readable theorem derivation.

## Claim correction

All earlier workspace language calling `3.695879961267919` a
“verifier-passing candidate” is superseded.  The accurate label is
“artifact accepted by a known-unsound verifier.”
