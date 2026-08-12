# Fourth chained upper-bound descent

## Outcome

The fourth descent succeeded.  With exact decimal coefficients listed in
increasing powers of \(\lambda\), set

\[
\begin{aligned}
P_3={}&(-0.250000000000000,-0.003330465213687,
 0.091728978292451,0.040555948334794,\\
&-0.053458127305523,0.021783259992867),\\
P_4={}&(-0.250000000000000,0.006788512088209,
 0.038835297966515,0.110380487198675,\\
&-0.045883160603885,-0.048420977583689,
 0.038460877061037,-0.003292994769736).
\end{aligned}
\]

For

\[
F_j(\lambda)=H(\lambda)+P_j(\lambda)e^{-\lambda},
\]

the frozen certificate proves the exact link \(F_3\to F_4\).  Conditional on
the same audited GNNW Lemma 11 / repaired BookCor descent used by the first
three stages, the complete four-stage chain gives

\[
\boxed{
R(k,k)\leq
(3.7808931385024181222517908784987532\ldots)^{k+o(k)}.
}
\]

This is a **local computer-assisted theorem**, not yet a published or
externally reviewed result.  The numerical statement is proved by the frozen
Arb artifacts below; the remaining non-numerical dependencies and publication
caveats are unchanged from `HIGHER_ORDER_RESULT_TO_CLAIM.md`.

## Concavity gate before search

The exact stage-3 target was treated as the prospective stage-4 prior.  Before
optimizing a new target, the two existing 256-bit Arb implementations proved
strict concavity on all of \((0,1]\):

```text
verify_arb.prove_prior_concavity(P3): worst U'' upper = -0.3618584052687671
verify_region_direct_arb.prove_concavity(P3): worst U'' upper = -0.36219400575974847
```

The second implementation has a separate subdivision and derivative code.
As a continuation check, the same two routines also prove that the final
\(P_4\) target is strictly concave, with upper bounds
`-0.3551324549829281` and `-0.3559047458651924`, respectively.  Thus it is
eligible to serve as an exact prior in a later stage.

## Floating-point construction search

`search_chained_target.py` remains a constructor only.  It was extended with
an optional `--initial-coefficients` warm start so a coarse search can be
continued on a denser mesh.  This option checks both the requested degree and
the frozen universal linear coefficient.  It does not enter either proof
checker.

Representative constructor endpoints were:

| degree | requested mesh slack | constructed base |
|---:|---:|---:|
| 6 | \(2.5\times10^{-4}\) | 3.78123177264300 |
| 7 | \(2.5\times10^{-4}\) | 3.78119027125275 |
| 8 | \(2.5\times10^{-4}\) | 3.78117386606962 |
| 7 | \(1.8\times10^{-4}\) | 3.78091601937616 |
| 7 warm | \(1.75\times10^{-4}\) | 3.78089403864694 |
| 8 warm, final | \(1.75\times10^{-4}\) | 3.78089313850242 |

An independent dense floating scan of the final exact decimals found minimum
unbuffered slack `0.00017498495342138654` near
`lambda=0.93106`, with `min F'=0.7658686092917886`.  This was only a
preflight check.  It was not used as proof.

## Frozen fourth-stage certificate

```text
file: certificate-higher-order-octic-chain-v4.json
SHA-256: 09253d757516dc258396f82c09a442aaaf9d499640c1cc99b5767e6d51d35942
cells: 131072 on [0.005,1]
region buffer: 0.00008
constructor predicted worst buffered slack: 0.00013770259745871094
```

The first 65,536-cell trial already passed, but its rigorous main slack was
only `8.762467175372537e-05`.  Keeping the exact target fixed and doubling the
number of cells reduced interval dependency loss.  The final 131,072-cell
certificate has rigorous fourth-stage main slack above \(10^{-4}\).

## Final rigorous replay

`verify_chain_arb.py` passed the complete four-stage chain and reported for
stage 4:

```text
target small slack/lambda: 0.0038794631355425788456986812430578...
standard region margin:    7.473125335382186e-05
swapped region margin:     7.502455280615754e-05
large main slack:          1.1266755240590772e-04
F4(1):                     1.3299602617488617145808261929025859...
exp(F4(1)):                3.7808931385024181222517908784987532...
```

The separately written direct Ramsey-region verifier also passed all 131,072
cells:

```text
prior U'' worst certified upper:       -0.36219400575974847
worst standard direct exponent slack:   1.063861730808328e-06
worst swapped direct exponent slack:    7.502455280615754e-05
```

The standard direct margin exceeds the predeclared \(5\times10^{-7}\) target.
`audit_tests.py` also passed all derivative-sign, arbitrary-degree derivative,
and known union-gap regressions after the search-script change.

## Exact-link and reproduction commands

The chain checker confirmed exact `Decimal` equality between the stage-3
target tuple and the stage-4 prior tuple.  From `routes/upper`, replay with:

```text
.venv/bin/python verify_chain_arb.py \
  certificate-higher-order-quintic-v1.json \
  certificate-higher-order-quintic-chain-v2.json \
  certificate-higher-order-sextic-chain-v3.json \
  certificate-higher-order-octic-chain-v4.json

.venv/bin/python verify_region_direct_arb.py \
  certificate-higher-order-octic-chain-v4.json

.venv/bin/python audit_tests.py
```

## Open risks

1. The theorem still imports the audited GNNW combinatorial descent and
   repaired BookCor; the interval programs do not re-prove that combinatorial
   lemma.
2. The proof relies on the documented containment semantics of Arb through
   python-flint at 256-bit precision.
3. The certificate has not yet received independent external human review or
   public archival.
4. The successful fourth stage does not imply that an unrestricted infinite
   descent exists.  Any fifth stage must again freeze the exact \(P_4\) tuple,
   prove its prior properties, and pass both independent replays.
