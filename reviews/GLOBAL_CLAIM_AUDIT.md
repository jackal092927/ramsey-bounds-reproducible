# Adversarial audit of the unified manuscript's global claims

> **Later closure.** The claim audit below correctly described its snapshot.
> A later targeted proof removed S3 from the assumption ledger while retaining
> S1, S2, S4, and S5 as source assumptions; see
> `reviews/LOWER_S3_CLOSURE_2026-08-30.md`. Earlier S3 dispositions below are
> historical rather than current claim status.

Date: 2026-08-30  
Mode: read-only claim audit of the global manuscript layer; no paper, checker,
certificate, or materializer source was edited  
Audited global files:

- `papers/unified/main.tex`;
- `papers/unified/sections/00_abstract.tex`;
- `papers/unified/sections/01_introduction.tex`;
- `papers/unified/sections/02_evidence_taxonomy.tex`;
- `papers/unified/sections/90_unified_reproducibility.tex`; and
- `papers/unified/sections/91_conclusion.tex`.

The global statements were cross-checked against the current materialized
upper, lower, and finite Parts, the post-repair reviews, and the fresh
finite-heavy record.  At the audit snapshot the unified paper had been
rematerialized and compiled to a 78-page PDF; the unresolved-reference scan
passed.  This report audits claim scope, not typesetting quality and not the
underlying proofs a second time.

## Snapshot executive verdict

The **single-manuscript requirement is satisfied**.  There is one document
class, one abstract, one bibliography, one canonical PDF, and three Parts of
one article.  The sentence at
`papers/unified/sections/90_unified_reproducibility.tex:57-61` explicitly says
that the component trees are not separate publication outputs.  No split into
three papers is implied by the current architecture.

The global claim layer is nevertheless **not yet publication-safe without two
substantive wording repairs**:

1. the abstract, global introduction, evidence table, and conclusion do not
   consistently disclose that lower-interface item (S3) is an additional
   weighted-extension hypothesis and is not claimed as a theorem stated by
   HMS or Lin--Niu; and
2. the unified reproducibility section does not repeat the Part III statement
   that public GitHub and release-asset publication are still pending.

The numerical endpoints, limit order, exact-seven status, and global
non-implication for `R(3,18)` are mutually consistent.

## Proof-writer verdicts

| claim | verdict | audit reading |
|---|---|---|
| Conditional diagonal upper theorem | **PROVABLE AS STATED** | The condition consists of the three explicit Yang--Mao interfaces, the locally reproduced rate theorem, and Arb containment.  The positive-moment/tail argument is local, not imported. |
| Lower theorem as a standalone unconditional theorem | **HISTORICAL SNAPSHOT: PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION** | At this audit stage it required (S1)--(S5), with S3 treated as an additional weighted-extension hypothesis.  The later closure proves S3 locally but does not remove S1, S2, S4, or S5. |
| Lower theorem under explicit (S1)--(S5) | **HISTORICAL SNAPSHOT: PROVABLE AS STATED** | This was the status asserted in the then-repaired Part II.  The current theorem has the stronger four-item source boundary plus a local proof of S3. |
| Fixed-seed deletion barrier `rho(H) >= 7` | **PROVABLE AS STATED** | It is local to the fixed labelled vertex set and one-sided metric and is supported by six semantically reconstructed, checked DRAT refutations. |
| Existence or nonexistence of an exact-seven repair | **NOT CURRENTLY JUSTIFIED** | The paper correctly labels all three bounded runs `UNKNOWN` and asserts neither direction. |
| Anonymous public availability of the repository and twelve release assets | **NOT CURRENTLY JUSTIFIED** | The reviewed state is local pre-publication; public GitHub/release evidence has not yet been established. |

For the global prose at this audit snapshot, the lower-bound summary therefore
had status **PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION**.  This finding is
closed more strongly in the current manuscript: S3 is proved locally, while
S1, S2, S4, and S5 remain explicit source assumptions.

## Findings requiring correction

### G1 — HIGH: the global lower-bound summary blurs the provenance of (S3)

The repaired Part II is exact about the boundary:

- `papers/unified/sections/lower/02_setup.tex:322-326` says that (S1), (S2),
  (S4), and (S5) are version-pinned source items, while (S3) is an additional
  weighted-extension hypothesis not represented as a theorem stated verbatim
  in either source;
- `papers/unified/sections/lower/08_scope.tex:25-31` labels the theorem
  conditional on all five items.

The global layer weakens or loses this distinction:

- `00_abstract.tex:11-18` says only that the result is “within pinned Gaussian
  reverse-induction and exact-cumulant source interfaces”;
- `01_introduction.tex:37-54` attributes the surrounding interfaces to HMS and
  Lin--Niu and then displays the lower bound without naming the extra (S3)
  hypothesis;
- `02_evidence_taxonomy.tex:49-53` calls the result a written argument “inside
  pinned HMS/Lin--Niu interfaces”; and
- `91_conclusion.tex:7-14` summarizes the lower result and its limit order but
  omits the conditional interface.

An adversarial reader can reasonably read those sentences as saying that HMS
or Lin--Niu already stated the weighted nonexchangeable reverse-induction
extension.  The component paper expressly declines that attribution.

**Minimal repair.**  In every global summary, use one stable formulation:

> Assuming the version-pinned items (S1), (S2), (S4), and (S5), together with
> the separately stated weighted-extension hypothesis (S3), which is not
> attributed as a theorem stated by HMS or Lin--Niu, the local argument proves
> ...

The abstract may shorten this to “conditional on the four pinned source items
and the additional weighted-extension hypothesis (S3).”  The evidence table's
L0--L3 row should say that the arithmetic replay is only a witness and that
(S3) is an explicit additional hypothesis.  The conclusion needs at least one
sentence retaining that boundary.

### G2 — HIGH: the global artifact-publication language is ahead of external state

Part III is honest at
`papers/unified/sections/finite/07_reproducibility.tex:5-9`: public GitHub and
archival release publication remain pending, and the displayed commands are a
release contract rather than evidence of an anonymous download.

The global section is titled “Unified reproducibility and artifact
publication” and uses present-tense release language at
`90_unified_reproducibility.tex:4-5,44-65` without repeating that disclaimer.
Although it never gives a false URL, a reader can infer that the twelve assets
are already downloadable.  The bibliography and Part III say otherwise.

**Minimal pre-publication repair.**  Rename the section “Unified
reproducibility and planned artifact release” and insert after its opening
sentence:

> At the date of this draft, public GitHub and immutable release-asset
> publication remain pending.  The commands below specify the reviewed release
> contract; they do not assert that an anonymous download already exists.

Change “are release assets” to “are to be release assets” until publication.
After an authorized release, replace the disclaimer only after recording and
checking the public repository, commit, tag, exact twelve-asset name set, and
hashes.

### G3 — MEDIUM: the short finite statement omits the labelled-vertex-set quantifier

`01_introduction.tex:58-63` says that “every triangle-free graph with
independence number below 18 deletes at least seven seed edges.”  The exact
theorem quantifies over graphs on the same labelled set
`V={0,...,99}` and uses `d_H(F)=|E(H)\setminus E(F)|`.  The surrounding
sentence names `H`, but the domain should not be left implicit in a main-result
summary.

**Minimal repair.**  Replace that sentence by:

> For every graph `F` on the same labelled vertex set with `F` triangle-free
> and `alpha(F)<18`, one has `|E(H)\setminus E(F)| >= 7`, even when additions
> outside `E(H)` are free.

The abstract and evidence table may retain “fixed-seed one-sided deletion
radius” because that defined phrase already signals locality.

### G4 — MEDIUM: enumerate the upper interfaces rather than using an umbrella name

`00_abstract.tex:2-4` and `01_introduction.tex:22-25` use “retained-spine
interfaces” as shorthand.  The current upper theorem is more precise: it
assumes version-pinned regularization, parameterized-book, and
spine-compatibility interfaces; the correlation positive-moment/tail
implication is proved locally.

**Minimal repair.**  Enumerate those three imported interfaces once in the
abstract or introduction, and retain the sentence that the positive-moment and
tail step is local.  This prevents a future reader from treating that local
analytic lemma as a fourth imported Yang--Mao theorem.

### G5 — LOW: avoid an unsupported novelty/priority reading

`01_introduction.tex:13-18` says “three new results” and that the first two
“improve source-relative asymptotic ledgers.”  The Parts themselves explicitly
avoid unqualified priority and world-best claims.  “New” is unnecessary and
may be read as a literature-wide novelty assertion.

**Minimal repair.**  Use “three results developed here” and “give conditional,
source-relative refinements of two asymptotic ledgers.”

## Consistency checks that passed

1. **One paper.** `main.tex` includes all three Parts and all appendices in one
   document, and `90_unified_reproducibility.tex:57-61` denies separate
   publication outputs.  No mandatory structural correction is needed.
2. **Upper endpoint.** The safe base `3.780685290`, the strict unrounded upper
   endpoint below `3.780685288379640114`, and the predecessor value
   `exp(U(1))=3.780698427796...` agree with Part I.  No rounding-direction or
   endpoint mismatch was found.
3. **Upper quantifiers.** The global layer consistently calls the theorem
   asymptotic and source-relative and makes no effective finite-`k`, global
   optimum, priority, or world-best claim.
4. **Lower limit order.** The abstract, introduction, evidence table, and
   conclusion consistently fix sufficiently large `C`, then take
   `ell -> infinity`, and only afterward study `C -> infinity`.  The
   existential, non-effective `C_0` is preserved.
5. **Lower coefficient.** The global value
   `(1+o_{C->infinity}(1))/(64 log C)` agrees with Part II, and no
   cross-normalization strict comparison is claimed.
6. **Finite theorem.** The fixed seed, 100 vertices, 827 edges, free additions,
   one-sided deletion radius at least seven, and six checked refutations agree
   with Part III and the fresh finite-heavy record.
7. **Exact seven.** Every global occurrence says `UNKNOWN` or “remains open.”
   None turns the wall-limited runs into SAT, UNSAT, existence, or
   nonexistence.
8. **Global Ramsey non-implication.** The abstract, introduction, evidence
   table, and conclusion all state that the local theorem does not imply
   `R(3,18) >= 101`; this agrees with Part III.

## Per-file minimal correction list

| file | required minimum |
|---|---|
| `papers/unified/main.tex` | No claim-level change required.  Its single-document architecture satisfies the one-paper instruction. |
| `papers/unified/sections/00_abstract.tex` | Disclose the additional lower hypothesis (S3); enumerate the three imported upper interfaces. |
| `papers/unified/sections/01_introduction.tex` | Remove “new”; make the lower formula explicitly conditional on (S1)--(S5) and identify (S3); state the finite quantifier on the same labelled vertex set. |
| `papers/unified/sections/02_evidence_taxonomy.tex` | Rewrite L0--L3 to distinguish four pinned source items from extra hypothesis (S3). |
| `papers/unified/sections/90_unified_reproducibility.tex` | State that GitHub/release publication is pending and that the section is a release contract until public verification succeeds. |
| `papers/unified/sections/91_conclusion.tex` | Retain the conditional lower interface, including the non-source status of (S3). |

Once G1 and G3--G5 are repaired, G2 is resolved either by an honest
pre-publication disclaimer or by a verified public release, and the canonical
PDF is rebuilt, the global claim layer is suitable for another adversarial
pass.
