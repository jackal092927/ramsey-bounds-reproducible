# Literature and priority audit for the active Ramsey routes

Date of search: **2026-08-12** (America/Los_Angeles)  
Evidence cutoff: material publicly visible by the search time; the newest arXiv
submissions visible in the relevant search were dated **2026-08-11**.  
Purpose: determine what the present local bounds may safely be compared with.
This is a literature audit, not an amendment to any canonical theorem document.

## 1. Evidence policy and search scope

Only primary or first-party sources were used for technical conclusions:

- version-pinned arXiv abstract/source/HTML pages;
- the Electronic Journal of Combinatorics (EJC) dynamic survey itself;
- the authors' public Google Research certificate repository.

Secondary search results, blogs, citation aggregators, and AI summaries were not
used as technical evidence.  The following official searches were checked on
2026-08-12:

1. the [arXiv all-field search for `Ramsey`, newest first, first 100
   records](https://arxiv.org/search/?query=Ramsey&searchtype=all&abstracts=show&order=-announced_date_first&size=100);
2. the [complete August 2026 math.CO listing](https://arxiv.org/list/math.CO/2026-08?skip=0&show=2000);
3. exact-title/phrase searches around `diagonal Ramsey upper bound`, `GNNW`,
   `Yang Mao Ramsey`, `R(l,C l)`, `p_C`, `Gaussian random graphs Ramsey`,
   `truncated Gaussian Ramsey`, `1/log C Ramsey`, `history dependent Ramsey`,
   `R(3,18)`, `R(3, 18) >= 101`, and `100-vertex R(3,18)`;
4. version histories and full text for every directly relevant arXiv item listed
   below;
5. EJC DS1.18 and the first-party construction directory/history for the current
   finite lower bound.

This is a deliberately bounded public-source search.  It cannot exclude a
private manuscript, an unindexed repository, a result posted after the cutoff,
or a paper whose title and abstract conceal the relevant mechanism.  Therefore
“no exact analogue found” below is a search result, **not** a novelty proof.

## 2. Executive conclusions

| Route | Public-source finding at the cutoff | Safe conclusion for this workspace |
|---|---|---|
| Diagonal upper | GNNW v1 states the specialist two-colour theorem-level base $4e^{-0.14/e}=3.7992027396\ldots$. Yang--Mao v1 supplies no numerical $r=2$ base and explicitly says GNNW is stronger for $r=2$. HorizonMath v1 separately reports provisional values $3.7296$ and $3.6961$, expressly pending third-party verification. | $3.780685405$ is a numerical improvement over the **GNNW source-stated comparator** by about $0.4874\%$. It is not safe to call it first, world-best, or best publicly claimed. |
| Fixed-large-$C$ off-diagonal lower | Lin--Niu v2 already gives an explicit $1/(64\log C)$ correction beyond the HMS $e^{1/24}p_C^{-1/2}$ base. HMS and Lin--Niu both use history-conditioned reverse induction; Lin--Niu retains history-dependent conditional means before later coarsening them. | Do **not** claim the first $1/\log C$ correction or the first use of conditioning on exposure history. No exact counterpart of the local non-exchangeable triangular weighted-mean ledger was found in the checked sources, but this supports only a mechanism-level distinction, not priority. |
| Finite $R(3,18)$ | EJC DS1.18 gives $100\le R(3,18)\le120$. Nagda--Raghavan--Thakurta v5 states the improvement $99\to100$, and the authors publish the 99-vertex witness and verifier. | The current public/computational lower bound is $100$. No public $R(3,18)\ge101$ source was found. A local exclusion around one fixed near-miss, even if complete through six deletions, does not change the lower bound. |

## 3. Diagonal \(R(k,k)\): published and publicly posted comparators

### 3.1 GNNW: the numerical specialist comparator

Gupta, Ndiaye, Norin, and Wei, *Optimizing the CGMS upper bound on Ramsey
numbers*, [arXiv:2407.19026v1](https://arxiv.org/abs/2407.19026v1), was
submitted **2024-07-26** and still had only v1 at the cutoff.  The full-text
[Theorem 1](https://arxiv.org/html/2407.19026v1) states

\[
R(k,k)\le
\left(4e^{-0.14/e}\right)^{k+o(k)}
= (3.7992\ldots)^{k+o(k)}.
\]

The exact displayed expression evaluates to

\[
b_{\rm GNNW}=4e^{-0.14/e}
=3.799202739615937197176104356686\ldots .
\]

The local safe conditional base therefore satisfies

\[
3.780685405<b_{\rm GNNW},
\]

with absolute difference

\[
b_{\rm GNNW}-3.780685405
=0.018517334615937\ldots,
\]

relative base reduction \(0.4874005\ldots\%\), and log-rate reduction

\[
\log\!\frac{b_{\rm GNNW}}{3.780685405}
=0.0048859220\ldots .
\]

**Claim boundary.** This arithmetic proves a numerical comparison with the
formula printed in GNNW.  It does not itself validate every step of GNNW v1.
The workspace's separate theorem audit records a gap in the displayed proof of
GNNW Lemma 14.  Accordingly, the clean wording is “improves the numerical base
stated in GNNW v1,” not “improves an independently re-proved unconditional
published theorem.”

### 3.2 Yang--Mao v1 does not furnish a competing two-colour number

Yang and Mao, *New upper bound for multicolor Ramsey numbers*,
[arXiv:2608.01962v1](https://arxiv.org/abs/2608.01962v1), was submitted
**2026-08-03 09:30:23 UTC** and had no later version at the cutoff.  Its main
theorem is

\[
R_r(k)\le
\exp\!\left(-c\frac{k}{r^2\log^4(2r)}\right)r^{rk},
\qquad k\ge Kr^2\log^6(2r),
\]

for unspecified absolute constants \(c,K>0\).  The
[full text](https://arxiv.org/html/2608.01962v1) explicitly says that the paper
does not optimize a fixed small \(r\), and that GNNW is stronger at \(r=2\).
Thus Yang--Mao is important as a retained-spine/parameterized-book dependency,
but it gives **no source-stated numerical \(r=2\) base** against which
\(3.780685405\) can be directly ranked.

The newest-first arXiv and full August math.CO searches found no post-Yang--Mao
paper, through submissions dated 2026-08-11, that states another classical
two-colour diagonal asymptotic upper base.  For example, Tatarevic,
[arXiv:2608.06531v1](https://arxiv.org/abs/2608.06531v1), submitted
**2026-08-06**, is a constructive lower-bound increment and not an asymptotic
upper comparator.

This is only a cutoff-bounded search result; it is not evidence that no later,
private, or differently indexed result exists.

### 3.3 HorizonMath is a lower public numerical claim, but not an established comparator

Wang et al., *HorizonMath: Measuring AI Progress Toward Mathematical Discovery
with Automatic Verification*,
[arXiv:2603.15617v1](https://arxiv.org/abs/2603.15617v1), submitted
**2026-03-16**, publicly reports two candidate diagonal optimizations with bases
approximately \(3.7296\) and \(3.6961\).  Appendix A.2 of the
[official full text](https://arxiv.org/html/2603.15617v1) calls both
“pending third-party verification”; the paper also labels them “potentially
novel solutions” requiring expert inspection.

This source cannot be omitted from a priority audit because its public numbers
are smaller than \(3.780685405\).  It also cannot presently be treated as a
settled Ramsey upper theorem.  The workspace's independent theorem-to-code
audit found that the pinned HorizonMath validator accepts the union of two
one-sided rate conditions (`min`) where the cited all-orders Ramsey-region
definition requires both (`max`).  The advertised \\(3.6961\\) object passes the
former but is not certified by that route under the latter.  That is a local
audit finding, not a retraction by the authors.

Consequently the correct three-way distinction is:

1. **source-stated specialist theorem-level comparator:** GNNW,
   \(3.7992027396\ldots\);
2. **public provisional numerical claims:** HorizonMath, \(3.7296\) and
   \(3.6961\), pending third-party verification and locally challenged at the
   theorem-to-validator bridge;
3. **current local conditional proof package:** \(3.780685405\), numerically
   below (1), but above the raw numbers in (2).

### 3.4 Priority verdict for the local diagonal result

Supported wording:

> Conditional on the pinned local theorem chain, the base \(3.780685405\)
> strictly improves the numerical two-colour base
> \(4e^{-0.14/e}=3.7992027396\ldots\) stated in GNNW v1.  No later
> source-stated two-colour theorem-level base was found in the searched public
> primary sources through 2026-08-12.

Unsupported at present:

- “first improvement after GNNW”;
- “best published,” “best known,” or “world-best” upper base;
- “improves every public claim” (the provisional HorizonMath numbers are
  smaller);
- an unconditional statement, because the local result retains pinned
  Yang--Mao/P6/BookCor/computer-arithmetic dependencies and lacks external
  review/publication.

## 4. Fixed-large-\(C\) lower bounds and prior art for a history ledger

Write \(p_C\in(0,1/2)\) for the solution of

\[
C=\frac{\log p_C}{\log(1-p_C)}.
\]

### 4.1 Public rate progression and exact versions

1. **Ma--Shen--Xie.** *An exponential improvement for Ramsey lower bounds*,
   [arXiv:2507.12926v2](https://arxiv.org/abs/2507.12926v2): v1 submitted
   **2025-07-17**, current v2 revised **2026-04-26**.  It establishes, for each
   fixed \(C>1\), an exponential improvement over the classical
   \(p_C^{-1/2}\) base.

2. **Hunter--Milojević--Sudakov (HMS).** *Gaussian random graphs and Ramsey
   numbers*, [arXiv:2512.17718v2](https://arxiv.org/abs/2512.17718v2): v1
   submitted **2025-12-19**, current v2 revised **2026-05-18**.  Theorem B.1 in
   the [official full text](https://arxiv.org/html/2512.17718v2) states, for all
   sufficiently large fixed \(C\),

   \[
   R(\ell,C\ell)\ge
   \left(e^{1/24}p_C^{-1/2}\right)^\ell
   \quad(\ell\text{ sufficiently large}).
   \]

3. **Lin--Niu.** *Sharper Ramsey lower bounds from refined Gaussian estimates*,
   [arXiv:2605.25843v2](https://arxiv.org/abs/2605.25843v2): v1 submitted
   **2026-05-25**, current v2 revised **2026-07-02**.  Equations in the
   [official full text](https://arxiv.org/html/2605.25843v2) give, as
   \(C\to\infty\),

   \[
   \rho^{\rm new}(D)
   =-\frac12\log p_C+\frac1{24}
    +\frac1{64\log C}
    +o\!\left(\frac1{\log C}\right),
   \]

   equivalently

   \[
   e^{\rho^{\rm new}(D)}
   =e^{1/24}p_C^{-1/2}
   \left(1+\frac1{64\log C}
   +o\!\left(\frac1{\log C}\right)\right).
   \]

Therefore an explicit \(1/\log C\) correction is already public, with printed
leading coefficient \(1/64\) in the log-rate (and relative-base) expansion.
Any claim that the local route discovers the first correction of this order
would be false relative to Lin--Niu v2.

Exact arXiv searches around the three titles, \(p_C\), \(R(\ell,C\ell)\), and
truncated Gaussian refinements found no later direct fixed-\(C\) refinement
through the cutoff.  Again, this is not an exhaustive priority certificate.

### 4.2 How much “history dependence” is already present?

There is substantial prior-art overlap at the framework level:

- HMS uses a Bartlett/column exposure, conditions on previously exposed
  columns, and propagates a projection-dependent potential by reverse
  induction.
- Lin--Niu explicitly fixes the first \(s-1\) columns and the current diagonal
  entry, defines history-specific truncated means
  \(\mu_i=\mathbb E[X_i\mid\text{edge event, previous columns}]\), writes
  \(A_i=\sum_{j\ne i}\mu_j\), and applies a sharp upper-truncated cumulant
  generating-function estimate to
  \(\sum_i A_i\xi_i\).  It then bounds sums such as
  \(\sum_i A_i^2\) by a uniform Cauchy estimate and packages the result into a
  coarser reverse-induction remainder.

Thus neither “conditioning on the history” nor “keeping conditional means
before an exponential-moment bound” is new by itself.

Within the checked primary sources, however, no exact analogue was found for
the local package's more specific mechanism: a deterministic but
non-exchangeable triangular family of adapted weights, recursively carried
through the exposure, which changes the mean/connection potential and pays the
associated centered linear and weighted-quadratic costs before final
coarsening.  HMS and Lin--Niu expose the ingredients from which such a ledger
might be built, but the searched versions do not state the same recursive
weighted ledger or a separate term corresponding exactly to the local
\(H_*(C)\).

The safe novelty language is therefore:

> The local triangular weighted-mean ledger is mechanism-distinct from the
> coarsened HMS/Lin--Niu estimates in the versions checked here; no exact
> analogue was located in those sources.

It is **not** safe to say “the first history-dependent argument,” because the
source inductions are already conditioned on full exposure histories.

### 4.3 Comparison boundary for the local \(G_*+H_*\) package

The local source-relative expansion records

\[
G_*(C)\sim\frac1{32\log C},\qquad
H_*(C)\sim\frac1{96\log C},
\]

so its two added terms algebraically total

\[
G_*(C)+H_*(C)\sim\frac1{24\log C}.
\]

Lin--Niu prints \(1/(64\log C)\).  These numbers should **not yet** be promoted
to the public claim “coefficient \(1/24\) improves Lin--Niu's \(1/64\).”  The
local theorem is normalized against a frozen HMS/source ledger containing
\(B_R(C)/2\), and the workspace source audit has an unresolved alignment issue
between Lin--Niu's stated HMS comparator and the pre-Cauchy HMS coefficient.
An apples-to-apples derivation from one pinned public probability inequality is
needed before making that comparison.  At present the defensible claims are:

- the local package is a source-relative, internally reviewed conditional
  theorem package;
- it contains a positive additional \(H_*(C)\sim1/(96\log C)\) beyond its own
  frozen \(G_*(C)\) ledger;
- Lin--Niu already establishes the existence and explicit leading coefficient
  of a public \(1/\log C\) improvement;
- publication priority, exact superiority to Lin--Niu, and global optimality
  remain unknown.

## 5. Finite \(R(3,18)\)

### 5.1 Current published/computational interval

Radziszowski's EJC dynamic survey, *Small Ramsey Numbers*,
[DS1.18, revision 18](https://www.combinatorics.org/ojs/index.php/eljc/article/view/DS1),
dated **2026-04-24**, gives in Table IIa of the
[official PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS1/pdf/)

\[
\boxed{100\le R(3,18)\le120}.
\]

The table credits the lower bound to Nagda--Raghavan--Thakurta and the upper
bound to Backelin's \(e(3,k,n)\)-based work.

Nagda, Raghavan, and Thakurta, *Reinforced Generation of Combinatorial
Structures: Ramsey Numbers*,
[arXiv:2603.09172v5](https://arxiv.org/abs/2603.09172v5), was first submitted
**2026-03-10** and last revised **2026-04-21**.  It explicitly states the
improvement

\[
R(3,18):\quad 99\longrightarrow100.
\]

The authors' [Google Research `improved_bounds`
directory](https://github.com/google-research/google-research/tree/master/ramsey_number_bounds/improved_bounds)
publishes `R(3, 18) >= 100.txt`, a 99-vertex adjacency matrix, together with a
verification notebook.  The file history contains a single initial commit on
**2026-02-12**; the immutable witness is pinned at commit
[`62d471c0e73cbb808f5bd0341e1d5aa3a5a41ea0`](https://github.com/google-research/google-research/blob/62d471c0e73cbb808f5bd0341e1d5aa3a5a41ea0/ramsey_number_bounds/improved_bounds/R%283%2C%2018%29%20%3E%3D%20100.txt).

The graph has 99 vertices and excludes a triangle and an independent set of
size 18, so it certifies \(R(3,18)\ge100\).  A bound
\(R(3,18)\ge101\) would require a valid **100-vertex** graph with the same
avoidance properties.

### 5.2 Search result and local claim boundary

Exact searches for `R(3,18)>=101`, `R(3, 18) >= 101`, and a 100-vertex
\((3,18)\)-graph found no primary public certificate or paper.  The current
public lower bound at the cutoff is therefore \(100\), subject to the bounded
search caveat.

The local fixed near-miss starts from the published 99-vertex witness, adds one
vertex, and studies repairs of a 100-vertex graph with a triangle defect.  The
current local proof package now excludes every repair in its specified ball
using at most six input-edge deletions (with additions allowed), via the three
triangle-edge branches.  This is useful structural/computational information,
but it produces no 100-vertex triangle-free graph with independence number at
most 17.  It therefore proves neither \(R(3,18)\ge101\) nor any improvement of
the public lower bound.

## 6. Recommended claim language

The following language is supported by this audit:

> As of a primary-source search on 2026-08-12, the local conditional diagonal
> base \(3.780685405\) is numerically smaller than the
> \(3.7992027396\ldots\) base stated by GNNW.  Yang--Mao v1 does not give a
> numerical two-colour comparator and says GNNW remains stronger for \(r=2\).
> HorizonMath publicly reports smaller provisional numbers, but labels them
> pending third-party verification; the local audit identifies a
> theorem-to-validator gap.  We therefore make no first, best-known, priority,
> or world-best claim.
>
> For fixed large \(C\), Lin--Niu v2 already gives a
> \(1/(64\log C)\) improvement beyond the HMS asymptotic base.  The local
> weighted mean ledger appears mechanism-distinct from the coarsened formulas
> in the searched HMS/Lin--Niu versions, but conditioning on exposure history
> is already present there, and no priority claim is made.
>
> For the finite problem, the current public interval is
> \(100\le R(3,18)\le120\).  The local bounded-repair exclusions do not yield a
> 100-vertex witness and hence do not improve \(R(3,18)\ge100\).

## 7. Remaining unknowns before any priority statement

1. Repeat the arXiv/new-paper search immediately before public release; this
   audit freezes a rapidly changing 2026-08-12 snapshot.
2. Obtain external combinatorics review of the local diagonal transfer and
   interval certificate, including the repaired all-orders Ramsey-region
   condition.
3. Derive the local large-\(C\) coefficient and Lin--Niu's printed coefficient
   from a single common, version-pinned HMS normalization before claiming a
   strict quantitative improvement.
4. Search full journal databases and author repositories at submission time;
   the current primary-source search is strong enough for conservative wording
   but not for legalistic priority or exhaustive bibliographic claims.
5. For \(R(3,18)\), only an independently verified 100-vertex witness (or a
   different theorem implying one) can move the public lower bound to 101.
