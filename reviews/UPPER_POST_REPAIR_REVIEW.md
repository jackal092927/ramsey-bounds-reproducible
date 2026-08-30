# Second post-repair adversarial review: diagonal upper-bound component

Date: 2026-08-30  
Review mode: read-only adversarial review of the mathematical manuscript,
version-pinned source interface, generated unified copy, and executable
certificate path.  No paper, checker, certificate, or generator source was
changed in this review.  This report is the only review artifact written by
the reviewer.

The proof-status vocabulary in this report is literal:

- **CLOSED**: the first-round defect is removed in the current source and its
  proof dependencies have been checked;
- **PARTIAL**: a material part is repaired but the printed implication still
  needs an additional lemma, hypothesis, or endpoint argument;
- **OPEN**: the claimed conclusion is not justified by the current package.

## Scope

The principal human-facing files reviewed were

- `papers/upper/sections/01_introduction.tex`;
- `papers/upper/sections/02_framework.tex`;
- `papers/upper/sections/03_rate.tex`;
- `papers/upper/sections/04_exact_diagonal.tex`;
- `papers/upper/sections/05_transfer.tex`;
- `papers/upper/sections/06_computation.tex`;
- `papers/upper/appendices/A_certificate_data.tex`; and
- `papers/upper/appendices/C_stage6_record.tex`.

I also reviewed the corresponding generated files under
`papers/unified/sections/upper` and `papers/unified/appendices/upper`, the
materialization rules in `scripts/materialize_unified_paper.py`, and the
proof-relevant programs under `routes/upper`, especially
`verify_arb.py`, `verify_chain_arb.py`, `verify_region_direct_arb.py`, the
four final exact-diagonal/retained-spine checkers, and `audit_tests.py`.

For the external interface I freshly obtained the Yang--Mao v1 TeX member.
Its SHA-256 was

```text
155b7104ec5b6935a576ae9f2b161976a966b0b46bd2b69153c0934ca688da2a
```

which agrees with Appendix A and the external-source manifest.  The source
line checks cited below are against that exact member, not a later arXiv
version.

## Executive verdict

The current standalone upper-bound source is **PROVABLE AS STATED under its explicit
conditional trust boundary**: the three named Yang--Mao v1 combinatorial
interfaces, the locally reproduced repaired BookCor induction, and Arb ball
containment through the pinned `python-flint` version.  It is not an
unconditional reproof of those imported interfaces, a proof-assistant
formalization, or an effective finite-\(k\) estimate.

| First-round item | Final verdict | Principal closing evidence |
|---|---|---|
| U1: usable Yang--Mao interface | **CLOSED** | The manuscript now states the complete regularization, book, and colour-dependent compatibility specialization; defines \(\mathcal G_2^{(3)}\) exactly; and proves the specialized positive-moment/tail implication locally. |
| U2: outer wedge absent or directionally incomplete | **CLOSED** | The direct region, exceptional wedge, red side, blue diagonal, reservoir endpoint, \(x=y=1\) case, and rate-function domain gate are all explicit and agree with three structured replays. |
| U3: unrounded decimal unsupported | **CLOSED** | A 512-bit outward endpoint strictly below `3.780685288379640114` is printed, and all outer replays reproduce it. |
| U4: rate certificate lacked a correctness theorem | **CLOSED** | Appendix C now proves the finite-net descent, density split, induction in \(\ell\), small-ratio interior argument, exact six-link induction, and canonical byte/tuple identity gate. |
| Endpoint and notation defects | **CLOSED after regeneration** | The standalone source repairs zero residuals, the uniform finite-order split, \(x=y=1\), \(r_d+\tau<1\), `\qquad`, and stable symbolic cross-references.  The unified copy was rematerialized, compared with an independent materialization, compiled, and checked for namespaced-label fidelity. |

I found no new circular dependency, sign reversal, uncovered continuum
interval, or numerical counterexample in the repaired component.

## Reproduction evidence

The following checks passed on the reviewed bytes:

1. all four final 512-bit exact-diagonal/retained-spine checkers;
2. the complete six-stage `verify_chain_arb.py` replay, including the
   elementary first prior and all five exact target-to-prior handoffs;
3. `verify_region_direct_arb.py` on the sixth certificate;
4. `audit_tests.py`; and
5. the new canonical identity precheck, which accepted the six filenames in
   order, all six SHA-256 values, and the exact fourteen-entry displayed
   \(P_6\) tuple.

The sixth-stage replay returned the following proof-critical quantities:

```text
target small slack / lambda       0.0037785734384423962376319094...
standard region margin            7.464714995786726e-05
swapped region margin             5.766703065384951e-05
large main slack                  4.818471567626107e-05
F6(1)                             1.3299087618219930723187812632...
exp(F6(1))                        3.7806984277961236987518816497...
```

The separately written direct-region replay returned lower margins
`1.0628096485437162e-6` and `5.766703065384951e-5` for the two orientations.
The final outer replays reproduced

```text
q                                  0.755936928669275184934248156704747...
Xi                                 940.301459730178940085277235574944...
degree gate                        1.5056762e-9
red page margin                    5.1006707822905727e-9
blue page margin                   3.4825658438202073e-6
reservoir margin                   6.0468779601096050e-6
base upper enclosure               3.7806852883796401133523716774...
safe-decimal margin                1.6203598866476283e-9
```

These are continuum certificates under Arb containment semantics, not mesh
samples.  Floating scans described in the search record select candidates but
do not enter the accepted proof.

## U1: Yang--Mao interface and the local correlation implication

### Source fidelity

The revised `ass:yang-mao` is now a usable theorem interface rather than a
reference by informal name.

1. **Regularization.**  Yang--Mao v1 lines 318--332 give pairwise disjoint
   \(S_R,S_B,W\), the exact reservoir-size lower bound, the minimum degree in
   every colour, the fact that each \(S_i\) is a colour-\(i\) clique, and the
   fact that every \(S_i\)--\(W\) edge has colour \(i\).  All of these
   conclusions, including the quantification over a colouring of \(K_N\),
   now appear in item (a).
2. **Correlation property.**  The definition printed before the assumption
   matches source lines 989--1009.  In particular, it quantifies over every
   finite \(\mathcal X\), independent copies \(U,U'\), arbitrary real Hilbert
   maps, a selected coordinate, and every other coordinate's \(-1\) gate.
3. **Parameterized book.**  Source lines 1146--1190 quantify positive integers
   \(t,m\), require the pointwise degree condition, and use
   \[
   \Pi=\frac{3\delta}{p}
       +\frac{6\log(1/\delta)\log(1/p)}{\lambda_0},
   \qquad
   \Xi=2\log(2/\beta)+4C\lambda_0^{1/3}
       +\frac{12C\log(1/\delta)}{\lambda_0^{2/3}}.
   \]
   Taking \(r=2,d=3\) and \(X=Y_R=Y_B=W\) changes the source reservoir
   requirement \(2rt\exp(rt\Xi)\) into exactly
   \(4t\exp(2t\Xi)\).  Yang--Mao themselves make the coincident-set choice at
   lines 2258--2265; disjointness of these book-theorem input sets is not a
   hidden hypothesis.
4. **Compatibility.**  The two colour-dependent residual orders now match
   source lines 1571--1618: the selected book colour reduces its order by
   \(s_i+t\), while the other colour reduces only by its preliminary spine
   \(s_j\).  Nonpositive residual orders are treated as immediate completion,
   rather than passed to an undefined Ramsey number.

The scalar domains and gates are also complete: \(\delta\), \(\lambda_0\),
the eventual integer \(t\), the pointwise two-colour degree hypothesis, and
the strict gap \(p<1/2-\eta\) are all present.  The displayed numerical
values of \(q\) and \(\Xi\) agree with exact substitution into the source
formulas.

### Positive moments and the tail transfer

The former circular-looking phrase “positive-moment/tail interface” has been
removed from the imported assumptions.  The relevant implication is now
proved in Section 4.

- Every bivariate Taylor coefficient of
  \(F(x,y)=G(x)H(y)+G(y)H(x)\) is nonnegative.
- For every pair of nonnegative exponents, tensorization writes the mixed
  moment as a squared Hilbert norm.  Finiteness of \(\mathcal X\) makes the
  random pair bounded, so the entire series may be averaged term by term.
- On \(\mathcal E=\{Z_1,Z_2\ge-1\}\), the exact-diagonal envelope gives the
  exponential upper bound; on \(\mathcal E^c\), the separator gives the
  negative contribution \(-\sigma_*\).
- If \(\mathbb P(\mathcal E)\ge\beta\), choosing \(\lambda=-1\) proves the
  correlation conclusion immediately.  Otherwise, failure of the claimed
  conclusion at \(\lambda=v^3-1\), followed by a union bound, gives the
  printed tail for \(Y=((\max(Z_1,Z_2)+1)_+)^{1/3}\).
- Layer cake integrates this tail to
  \(\beta(1+2/\varepsilon)\).  The exact positive rational budget in (4.15)
  then contradicts the nonnegative expectation.

The final identity
\(4u_0(1+\varepsilon)=12366348252219/1250000000000\) matches the exact
\(C\) consumed by the book theorem.  Thus the correlation input is produced
locally before the imported book interface consumes it; there is no logical
cycle.

Appendix A now distinguishes the three genuinely imported combinatorial
conclusions from analytic source lineage that is reproved locally.  Its line
map includes the actual positive-moment source lines 370--418 and no longer
attributes that lemma to the wrong range.

**U1 verdict: CLOSED.**

## U2: retained-spine transfer and outer wedge

Let \(x=\sigma_R\le y=\sigma_B\),
\(A=U(1)-2c_\eta\), and \(E=U'(1)-c_\eta\).  The repaired proof correctly
uses concavity at one to obtain

\[
U(1)-D(x,y)\ge xA+(y-x)E.
\]

The endpoint \(x=y=1\), where the raw expression \(aU(b/a)\) would contain
\(0/0\), is now separated first and discharged by
\(U(1)-D(1,1)=A>\Delta\).  Everywhere else the homogeneous expression is
defined.

The exceptional region has vertices
\((0,0),(0,r_a),(r_d,r_d)\), where
\(r_a=\Delta/E\), \(r_d=\Delta/A\), and its sloping edge is
\(y=r_a+sx\), \(s=1-A/E\).  The exact checker proves and the manuscript now
states both

\[
0<r_a<\tau<r_d<1,
\qquad r_d+\tau<1,
\qquad 0<s<1.
\]

The second inequality ensures that every argument
\(1-\tau/(1-x)\) used in the blue-page derivative lies in \((0,1)\) on the
whole certified interval.

For the red page,

\[
\partial_xP_R=c_\eta-U'(z)<0,
\qquad
\partial_yP_R=c_\eta-U(z)+zU'(z)>0.
\]

It is therefore enough to follow the sloping edge.  There
\(\mathcal B'(z)=(sz-1)U''(z)>0\), while \(z\) decreases from the axis
endpoint.  Since the enclosure at that largest \(z\) is already negative,
the derivative along the full side is negative and the maximum is at
\((0,r_a)\).  Both the sign and the endpoint direction are correct.

For the blue page, its negative \(y\)-derivative first reduces the maximum to
the diagonal.  With \(v=\tau/(1-x)\),
\(\Gamma'(v)=vU''(1-v)<0\), and \(v\) increases with \(x\).  Hence the
negative enclosure at \(v=\tau\) controls the entire diagonal and the maximum
is at \(x=0\).  Finally, \(Q\) is coordinatewise increasing, so its maximum
is \((r_d,r_d)\).  The symmetric triangle merely exchanges colours.

The proof therefore covers the full square, including its exceptional
endpoint, and the three independently structured outer replays agree with
all page and reservoir margins.

**U2 verdict: CLOSED.**

## U3: certified decimal

The proof now prints the strict chain

\[
e^{U(1)-\Delta}
 <3.7806852883796401133524
 <3.780685288379640114
 <3.780685290.
\]

The first displayed decimal is an outward-rounded upper endpoint, and the
primary, non-importing, and adaptive replays enclose the same value.  The
stronger decimal in the theorem is therefore implied by a displayed certified
inequality rather than by an unstated console result.

**U3 verdict: CLOSED.**

## U4: theorem-to-certificate correctness

Appendix C now states the complete semantic obligations of a
`corrected-two-sided-ramsey-v1` record and proves their implication to a
uniform Ramsey rate.

### Finite-net descent

The proof correctly separates the small-ratio and compact-ratio regimes.

1. Classical Erd\H{o}s--Szekeres recursion plus Stirling handles
   \(\ell/k\to0\).  Since every target differs from entropy by
   \(O(\lambda)\), a fixed sufficiently small \(\rho\) absorbs that
   difference into the requested \(\epsilon k\).
2. On \([\rho,1]\), the perturbation
   \[
   p_{\lambda,\delta}=1-e^{-G'(\lambda)+2\delta},
   \qquad
   x_{\lambda,\delta}=e^{-\delta}(1-M)
      p_{\lambda,\delta}^{1/(1-M)}
   \]
   is uniformly smaller than the unperturbed \(X\).  Compactness and the
   finite certificate records permit one \(\delta\), one finite descending
   grid, and one finite maximum of the BookCor thresholds.
3. In the high-red-density branch, the comparison
   \(G'(\lambda_j)\le G'(r)+\delta\) makes the actual red density at least
   \(p_{\lambda_j,\delta}\).  The main certificate slack, the
   \(e^{-\epsilon}X\) perturbation, \(\lambda_j\ge r\), and
   \(\log(MY)<0\) give the balanced-book size threshold with the correct
   inequality directions.
4. In the complementary branch, the average blue degree is greater than
   \(e^{-G'(r)+\delta}(N-1)\).  A vertex of at least the printed exponential
   degree exists.  The mean-value identity
   \(k(G(r)-G(r-1/k))=G'(\xi)\), together with bounded \(G''\) on
   \([\rho/2,1]\), shows that this degree reaches the induction threshold for
   \(\ell-1\).  A blue \(K_{\ell-1}\) extends with the selected vertex; a
   red \(K_k\) already finishes.  The previously settled small-ratio range is
   a valid base for this induction.

This closes exactly the finite-grid, density-dichotomy, and \(\ell\)-induction
steps absent in the first-round manuscript.

### Interior points and the first prior

On a closed certificate record, both strict prior-rate orientations imply an
interior Ramsey-region point after a small enlargement of \(X,Y\); decreasing
the first coordinate to \(x_{\lambda,\delta}\) preserves interior membership.
On \((0,\lambda_*]\), the elementary witness has \(Y=1-X\).  Choosing
\(x_{\lambda,\delta}<z<X\) places \((z,1-z)\) in the elementary Ramsey
region and strictly dominates the perturbed point in both coordinates.  This
supplies the required interior point without importing the rate being proved.

The first certificate's prior is established by this elementary witness.
Each later prior is the exact decimal tuple of the preceding accepted target,
so ordinary finite induction proves all six targets.  There is no
target-as-own-prior cycle.

### Byte and statement identity

`verify_chain_arb.py --require-paper-chain` now performs, before any interval
work:

- exact filename and order comparison;
- SHA-256 comparison for all six JSON files; and
- exact `Decimal` comparison of the final target against the fourteen
  terminating decimals printed for \(P_6\).

`reproduce.py full` invokes that mode.  A direct invocation of the identity
gate passed on the reviewed bytes.  Thus a successful replay of a different
six-file chain can no longer masquerade as the manuscript theorem.

**U4 verdict: CLOSED.**

## Endpoint, notation, and generated-copy audit

The earlier endpoint and notation defects are closed individually.

1. The residual convention gives cost zero when either residual order is
   nonpositive.
2. The homogeneous-extension lemma assumes \(U\ge0\) and splits at a fixed
   rate threshold \(K_0\).  Ratios with larger order at least \(K_0\) use the
   uniform rate; the finitely many remaining Ramsey numbers contribute
   \(O_{K_0}(1)=o(k)\).  Floored zero coordinates use the residual convention.
3. The \(x=y=1\) point is handled before division by the homogeneous scale.
4. The blue-page domain gate \(r_d+\tau<1\) is explicit.
5. The malformed literal `qquad` is replaced by `\qquad`.
6. The correlation handoff and rate theorem now use symbolic `\eqref` labels
   rather than stale literal numbers.
7. **Generated-copy gate closed.**  A fresh materialization reproduced all
   ten upper source and appendix files in the unified tree byte for byte.
   The audit counted 106 labels, 116 references, and 85 handwritten tags,
   with no unnamespaced or duplicate labels, unresolved references, or
   malformed visible tags.  The compiled unified log contains no undefined
   or multiply defined reference and no duplicate PDF destination.

**Endpoint/notation verdict: CLOSED in both the standalone source and the
generated unified copy.**

## Dependency and trust-boundary audit

The final dependency order is acyclic:

1. elementary Ramsey recursion proves the initial rate prior and the
   small-ratio interior witness;
2. repaired BookCor plus six exact, linked certificates proves \(F_6\);
3. local analytic lemmas plus the local tensor-moment/tail proof establish
   \(\mathcal G_2^{(3)}(\beta,C)\);
4. Yang--Mao regularization and parameterized book/compatibility consume the
   established rate and correlation property; and
5. the outer wedge turns the max--min transfer into the final base.

The surviving qualifications are declared limitations rather than defects:

- the theorem is conditional on the pinned Yang--Mao v1 regularization,
  parameterized-book, and compatibility conclusions;
- the local rate proof relies on the repaired BookCor proof reproduced in the
  paper and on Arb containment semantics;
- the several replays are independently structured but share the same Arb
  library and exact mathematical specification;
- asymptotic \(o(k)\) terms are non-effective, so no explicit finite
  threshold or finite-\(k\) inequality follows; and
- neither the combinatorial proof nor the interval proof has been formalized
  in a proof assistant.

## Final recommendation

No U1--U4 mathematical blocker remains in the reviewed standalone upper-bound
source.  Subject to the explicitly printed conditional boundary, the upper
theorem may be presented as **PROVABLE AS STATED**.  The repaired source has
been rematerialized into the unified manuscript, its generated-copy fidelity
gate has passed, and the unified PDF has compiled without unresolved or
multiply defined references.  Publication should retain the source digest,
exact certificate hashes,
`--require-paper-chain` reproduction mode, and the non-effective-asymptotic
disclaimer.
