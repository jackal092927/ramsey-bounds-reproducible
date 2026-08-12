# Sixth chained upper-bound descent: bounded search log

## Claim

Let

$$
H(\lambda)=(1+\lambda)\log(1+\lambda)-\lambda\log\lambda
$$

and interpret every displayed terminating decimal exactly.  Define

$$
\begin{aligned}
P_6(\lambda)={}&-0.250000000000000\lambda
+0.019891840059418\lambda^2
-0.012275954247190\lambda^3\\
&+0.144110816398083\lambda^4
+0.006277913420654\lambda^5
-0.066101623491668\lambda^6\\
&-0.002287675993602\lambda^7
-0.058238059505066\lambda^8
+0.030675864198693\lambda^9\\
&+0.052472201910597\lambda^{10}
+0.043300454861853\lambda^{11}
-0.042529975074653\lambda^{12}\\
&-0.055263639426635\lambda^{13}
+0.036695886931268\lambda^{14}.
\end{aligned}
$$

For $F_6(\lambda)=H(\lambda)+P_6(\lambda)e^{-\lambda}$, the exact six-stage
chain and the locally closed combinatorial descent prove the local
computer-assisted theorem

$$
\boxed{
R(k,k)\leq
\left(3.7806984277961236987518816497522162\ldots\right)^{k+o(k)}.
}
$$

The status is `PROVABLE AS STATED` under the same local proof boundary as the
fifth-stage theorem.  This is not a published result, an explicit finite-$k$
bound, or a proof-assistant formalization.  Independent external human review
of this sixth link remains pending.

## Frozen protocol (declared before target search)

This is a bounded attempt to add **one** descent after the frozen fifth-stage
certificate.  It will not continue to a seventh stage.

The only admissible prior is the exact ten-entry target tuple in
`certificate-higher-order-decic-chain-v5.json`, whose SHA-256 is
`4ec4dbbe190a08134efe68c3a76ce4b4fb3aabdad230af703c19a28a03ecf9a9`.
No rounded, refitted, or independently retyped prior is admissible.  Before
search, both existing 256-bit Arb implementations must prove this exact
prior strictly concave on all of `(0,1]`.

The construction search is limited to target degrees 10 through 14.  A
candidate will be frozen only if all of the following predeclared gates hold:

1. its base is at least `0.000001` below the frozen fifth-stage base;
2. dense floating replay plus local scalar refinement finds unbuffered
   continuous slack at least `0.000150000000000`;
3. the exact certificate has at most 131,072 cells and passes the complete
   six-stage `verify_chain_arb.py` replay;
4. the separately written `verify_region_direct_arb.py` gives both exact Arb
   exponent margins at least `0.0000005`;
5. exact `Decimal` comparison proves the P5 target tuple equals the P6 prior
   tuple entry by entry; and
6. `audit_tests.py` passes unchanged.

A certificate that merely has positive margins but misses one of these gates
will be reported as a frontier/FAIL, not as a new Ramsey bound.  Floating
optimization and interpolation are construction aids only and have no role in
the proof.

## Pre-search prior audit

The certificate hash was recomputed before optimization and equals the frozen
hash above.  On its exact target decimals the two independent 256-bit Arb
implementations returned

```text
verify_arb.prove_prior_concavity:          P5'' <= -0.35642515827888227
verify_region_direct_arb.prove_concavity:  P5'' <= -0.3574394324533535
```

Thus the strict-concavity gate passed before any sixth-stage search.  The
frozen prior base, computed in Arb rather than binary floating point, is

```text
3.7807566104095593763172345562324210302278058291660...
```

## Bounded degree-10--14 frontier

The first bounded pass used the exact P5 tuple above, a requested construction
margin of `0.00015`, and no target degree outside 10--14.  Its diagnostic
frontier was

| target degree | diagnostic base | sampled minimum slack | disposition |
|---:|---:|---:|:---|
| 10 | 3.78075661040956 | 0.000148091758 | no accepted feasible step |
| 11 | 3.78075661040956 | 0.000148091758 | no accepted feasible step |
| 12 | 3.78075661040956 | 0.000148091758 | no accepted feasible step |
| 13 | 3.78069741660317 | 0.000150109936 | frontier only |
| 14, raw | 3.78069363690183 | 0.000150096701 | rejected after dense leak |

The raw degree-14 point looked best on the construction mesh, but a denser
mesh found slack only

```text
0.00014795745008933103 near lambda = 0.3386221294,
```

so it failed the predeclared gate and was not certified.  No degree was added
and no search range was enlarged.  A single guarded degree-14 point was then
selected within the already declared range.  A broad 20,001-point scan
(geometric near the splice and linear thereafter), followed by bounded scalar
refinement around every sampled local minimum, returned

```text
minimum unbuffered floating slack:
0.00015473769852614172 at lambda ~= 0.33943703594667307

next three refined local minima:
0.00015519556902354736 at lambda ~= 0.9859202132743512
0.00015519607550973370 at lambda ~= 0.6439420227559093
0.00015519870501323751 at lambda ~= 0.8750494757168542

minimum sampled F6:   0.030260793830868504 at lambda = 0.005
minimum sampled F6':  0.7658393690544814 at lambda = 1
floating base:        3.780698427796123
```

Thus the unique frozen candidate cleared both the `0.00015` continuous
construction floor and the `0.000001` base-improvement floor.  The eventual
exact Arb base improvement over P5 is

```text
0.0000581826134356775653529064802047549...
```

These floating data only selected the candidate.  In particular, they are not
used to cover the continuum in the proof.

## Exact replay and claim boundary

### Frozen certificate and exact handoff

Only the guarded degree-14 target displayed in the Claim was frozen:

```text
file: certificate-higher-order-tetradecic-chain-v6.json
SHA-256: 8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8
cells: 131072
stored left endpoint: 0.0050000000000000001
stored right endpoint: 1
region buffer: 0.000080000000000000007
constructor predicted worst buffered slack: 0.00011568648667514836
```

The certificate's ten-entry prior tuple was compared with the P5 target tuple
using arbitrary-precision `Decimal`, not binary floating point:

```text
P5 target == P6 prior: True
```

Thus the sixth link has no rounded or refitted handoff.

### Complete six-stage 256-bit Arb replay

`verify_chain_arb.py` replayed the elementary prior and all six exact links and
returned

```text
PASS: verified 6-stage Ramsey-rate certificate chain
```

The new stage's strict lower margins and endpoint value were

```text
target small slack/lambda:
0.0037785734384423962376319094335140413...

standard Ramsey-region margin:
7.464714995786726e-05 at cell 8

swapped Ramsey-region margin:
5.766703065384951e-05 at cell 131071

large-regime main slack:
4.818471567626107e-05 at cell 131071

F6(1):
1.3299087618219930723187812632036105226...

exp(F6(1)):
3.7806984277961236987518816497522162752...
```

Every proof-critical margin is strictly positive.  The analytic small regime
and the 131,072 exact cells cover all $0<\lambda\leq1$.

### Separately written direct region replay

`verify_region_direct_arb.py` does not import the primary verifier and directly
minimizes both continuous exponent slacks over the complete prior-ratio
interval.  It returned

```text
PASS: independent direct two-sided Ramsey-region replay
prior P5'' worst certified upper:       -0.35743943245335352
worst standard direct exponent slack:    1.0628096485437162e-06 at cell 0
worst swapped direct exponent slack:     5.766703065384951e-05 at cell 131071
```

Both independently replayed margins exceed the predeclared `5e-7` floor.
`audit_tests.py` also passed the derivative-sign regression, arbitrary-degree
polynomial-derivative regression, and known Horizon union-gap regression.

Consequently every predeclared gate passed and the boxed local asymptotic
bound follows.  The search stops here: no seventh-stage search was performed.

## Reproduction commands

Run from `routes/upper` with the repository environment that supplies
`python-flint`:

```text
../../.venv/bin/python verify_chain_arb.py \
  certificate-higher-order-quintic-v1.json \
  certificate-higher-order-quintic-chain-v2.json \
  certificate-higher-order-sextic-chain-v3.json \
  certificate-higher-order-octic-chain-v4.json \
  certificate-higher-order-decic-chain-v5.json \
  certificate-higher-order-tetradecic-chain-v6.json

../../.venv/bin/python verify_region_direct_arb.py \
  certificate-higher-order-tetradecic-chain-v6.json

../../.venv/bin/python audit_tests.py
```

## Claim boundary

1. The sixth certificate proves one finite descent only; it supplies no
   convergence theorem for an infinite chain.
2. The inherited asymptotic descent has non-effective $o(k)$ terms, so this is
   not an explicit finite-$k$ inequality.
3. The numerical proof imports Arb containment semantics through
   `python-flint` at 256-bit precision.
4. The local combinatorial proof and interval replay have not been formalized
   in a proof assistant, and this sixth link has not yet received independent
   external human review or public archival.
