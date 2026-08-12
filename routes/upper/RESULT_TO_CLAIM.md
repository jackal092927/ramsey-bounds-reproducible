# Result-to-claim judgment

- `claim_supported`: **yes**
- `supports`:
  - The frozen beta-0.0299 certificate, replayed with 256-bit Arb balls,
    supports the asymptotic claim
    $$R(k,k)\leq(3.7990629773286618741\ldots)^{k+o(k)}.$$
  - The proof first establishes the exact-decimal beta-0.08 elementary prior
    without GNNW Lemma 14, then proves both rate-envelope orientations needed
    for all ordered pairs $(k,\ell)$.
  - Strict two-sided margins on $[5\cdot10^{-3},1]$ supply the missing
    $\mathcal R_*$ interior condition. The elementary witness supplies it on
    $(0,5\cdot10^{-3}]$ after the finite-net parameter strictly shrinks $X$.
  - The analytic small-$\lambda$ proof covers the entire open tail, and the
    Arb checker covers every point of every exact-decimal large-regime cell,
    not merely a sampled net.
  - A candidate-specific repaired finite-net descent closes the bridge to
    GNNW Theorem 12 despite the defects in the printed Theorem 13.
  - A second, independently written Arb program checks the two exponent
    slacks directly rather than reusing the scalar-envelope reduction.
- `does_not_support`:
  - It does not validate GNNW Theorem 13 in its literal arbitrary-witness
    generality; the printed $F'<0$, $\mathcal R$ versus $\mathcal R_*$, and
    missing uniformity must be repaired.
  - It does not support the withdrawn `3.792918524...` route or any route using
    beta 0.03 itself as an unproved prior.
  - It does not elevate the beta-0.0298 numerical frontier to the recommended
    claim.
  - It does not provide explicit finite-$k$ thresholds or exact finite Ramsey
    bounds.
  - The formerly imported GNNW Lemma 11/Theorem 12 combinatorial content is now
    re-proved in `LEMMA11_STANDALONE_PROOF.md` and independently accepted in
    `INDEPENDENT_LEMMA11_REFEREE.md`; this does not substitute for external
    community review.
- `missing_evidence`:
  - No further local mathematical evidence is needed for the stated asymptotic
    implication under Arb's enclosure semantics.
  - Optional trust reduction would consist of a proof-assistant replay or an
    additional independent interval-arithmetic implementation.
- `suggested_claim`:
  - “Using GNNW Theorem 12 with a repaired, candidate-specific finite-net
    bridge and an Arb-certified two-sided Ramsey-region witness, we obtain
    $R(k,k)\leq(3.799062977328662)^{k+o(k)}$.”
  - Do not state that the result follows from GNNW Theorem 13 as printed.
- `next_checks`:
  - Archive the certificate, verifier, requirements lock, hashes, and full
    stdout together.
  - Obtain an external combinatorics review focused on the repaired BookCor
    application and the uniform-epsilon quantifiers.
  - If publication-grade independent numerical redundancy is desired, replay
    the inequalities with a second ball-arithmetic implementation.
- `confidence`: **high**

## Independent replay evidence

Recommended split-0.005 certificate SHA-256:

```text
f7344d74bb2e5f033e14dbe9e943af7b90e52937d86610eb9f2dc548605aa11e
```

Observed decisive margins:

```text
prior elementary [0.005,1] slack:       3.1150059697914928e-08
target analytic slack/lambda:            0.00369567987777145...
standard region margin:                  5.8529290109470086e-05
swapped region margin:                   6.074652597491317e-05
target large-regime main slack:          4.942496275865115e-06
direct standard exponent slack:          8.346513629711325e-07
direct swapped exponent slack:           6.074652597491317e-05
growth base:                              3.7990629773286618741...
```

Reproduction from the repository root:

```bash
.venv/bin/python -m pip install -r routes/upper/requirements-verify.txt
.venv/bin/python routes/upper/verify_arb.py \
  routes/upper/certificate-recommended-beta00299-split005.json
.venv/bin/python routes/upper/verify_region_direct_arb.py \
  routes/upper/certificate-recommended-beta00299-split005.json
.venv/bin/python routes/upper/audit_tests.py
```
