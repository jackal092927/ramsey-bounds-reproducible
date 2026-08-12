# Result-to-claim gate: six-stage diagonal upper bound

## Verdict

```text
claim_supported = yes
confidence = high
```

## Supported local theorem

The exact-linked quintic/quintic/sextic/octic/decic/tetradecic chain recorded
in `HIGHER_ORDER_SEARCH.md`, `STAGE4_SEARCH.md`, `STAGE5_SEARCH.md`, and
`STAGE6_SEARCH.md` supports

$$
R(k,k)\le
\left(3.7806984277961236987518816497522163\ldots\right)^{k+o(k)}.
$$

This is the recommended local computer-assisted theorem.  It improves the
independently reviewed five-stage predecessor
`3.7807566104095593763...`; it is not yet a published result.

## Evidence alignment

* **Safe base rate:** stage zero is the exact elementary `beta=.08` rate, with
  no use of the flawed Lemma 14 iteration.
* **Exact provenance:** every prior list is compared to the preceding target
  as an arbitrary-precision `Decimal` tuple.  In particular, the P5 target and
  P6 prior are exactly equal.
* **Continuous coverage:** stages 1--3 have 65,536 cells; stages 4--6 have
  131,072 exact-decimal cells on `[0.0050000000000000001,1]`; an analytic
  coefficient bound covers the entire open small-lambda tail.
* **Correct region:** both ordered-pair Ramsey-envelope orientations are
  strict.  The sixth-stage primary margins are `7.464715e-5` and
  `5.766703e-5`, with main slack `4.818472e-5`.
* **Independent numerical structure:** a separate direct-exponent Arb checker
  gives sixth-stage standard slack `1.0628096485437162e-6` and swapped slack
  `5.766703065384951e-5`.
* **Combinatorial closure:** `LEMMA11_STANDALONE_PROOF.md` proves the formerly
  imported GNNW Lemma 11/Theorem 12 core; `INDEPENDENT_LEMMA11_REFEREE.md`
  accepted it after two local repairs already present in the frozen hash.
* **Regression coverage:** derivative signs, arbitrary polynomial degree, and
  the known one-sided-union false positive all pass.
* **Independent final replay:** `INDEPENDENT_STAGE6_REFEREE.md` reruns the full
  chain, direct checker, exact link, dense gate and coverage audit and reports
  PASS.

## Frozen identifiers

```text
stage 1  2664bc421cd0cb7489289caa283a3a3f22830580f7c21bf0e6cbe092910bc277
stage 2  b5b595b4dcc9d1bdc2b5714f68fef99ec1c566bbd612d35ca19100d173d41c4d
stage 3  2052952c3af98074d5442fb736c7a2952146e92051a43fab84e75f099d9e00d7
stage 4  09253d757516dc258396f82c09a442aaaf9d499640c1cc99b5767e6d51d35942
stage 5  4ec4dbbe190a08134efe68c3a76ce4b4fb3aabdad230af703c19a28a03ecf9a9
stage 6  8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8
```

## Claims not supported

The evidence does not establish an explicit finite-k threshold, convergence
of an infinite descent, correctness of arbitrary fitted targets, proof-
assistant formalization, publication, or external community review.  The
machine trust boundary still includes Arb/python-flint containment semantics.

## Recommended wording

> A six-stage exact-linked computer-assisted descent, starting from an
> elementary certified rate, gives the local theorem
> $R(k,k)\le(3.7806984277961236988\ldots)^{k+o(k)}$.  Two differently
> structured Arb checks verify the continuous two-sided inequalities, and the
> combinatorial book lemma has a standalone independently reviewed proof.  The
> result remains pending public archival and external human review.
