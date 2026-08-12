# Adversarial full-chain review

## Verdict

**PASS WITH IMPORTED DEPENDENCY.**

Conditional on the imported GNNW Lemma 11 / repaired BookCor combinatorial
core and Arb semantics, the reviewed package supports
$$R(k,k)\le(3.7814656158401685107\ldots)^{k+o(k)}.$$

## Scope actually checked

- GNNW v1 TeX was pinned at SHA-256 `9475bdc...eaa2e`.
- BookCor has the needed all-positive-$k,\ell$ quantifiers once $\ell\ge L_0$.
- No extra relation $p>M$ is needed.
- The descent uses $F'>0$, an actual $\mathcal R_*$ input, $\inf F'>0$, and $\sup M<1$.
- Standard and swapped prior-rate inequalities are both required for every ratio.
- Strict margins plus compactness give the all-$k,\ell$ $\mathcal R_*$ interior point.
- The finite net yields one finite BookCor threshold on each compact ratio interval.
- The analytic small-$\lambda$ witness covers the open tail to zero.
- Both stage handoffs agree as exact Decimal tuples; no rounded prior enters.
- The full three-stage Arb chain and all three direct-region replays passed.
- Prior concavity is used for envelopes; target concavity is not assumed by descent.

## Earliest unclosed boundary

The earliest item not independently re-proved from first principles in this
adversarial pass is **GNNW Lemma 11 together with the locally repaired BookCor
combinatorial proof**. It is an imported dependency, not a numerical-certificate
obligation. I found no insufficiency in the statement needed by the descent,
but this report does not certify that imported proof as a standalone theorem.

No fatal downstream gap was found. The $\mathcal R$/$\mathcal R_*$ bridge,
derivative sign, finite-net uniformity, two orientations, small-$\lambda$ tail,
and exact chain induction are discharged candidate-specifically.

## Residual risks

This remains a local conditional computer-assisted theorem: both replays trust
python-flint/Arb, there is no explicit finite-$k$ threshold, and external human
combinatorics review remains pending.
