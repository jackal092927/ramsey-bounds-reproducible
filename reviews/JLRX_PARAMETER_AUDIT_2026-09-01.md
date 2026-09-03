# JLRX parameter audit for the quantum Ramsey submission

Date: 2026-09-01

## Verified publication status

Jain, Li, Robere, and Xun, *On Pigeonhole Principles and Ramsey in
TFNP*, is a peer-reviewed FOCS 2024 proceedings paper, pp. 406--428, DOI
`10.1109/FOCS61266.2024.00033`.  It is not merely an arXiv preprint.

## Exact claim locations

The proceedings version is the comparison source.

- Definition II.6 (proceedings p. 413) defines the graph size as
  `N = 2^n`.
- The convention following Definition II.7 on the same page uses
  `K = n/2` for the default RAMSEY relation.
- Lemma III.1 (p. 414) supplies the graph-hash reduction.
- The unnumbered paragraph “Query complexity of RAMSEY” (p. 415) states
  a quantum lower bound `N^{1-o(1)}` by combining Lemma III.1 with
  Liu--Zhandry.

The introductory shorthand on p. 406 uses a different normalization.  The
submission therefore compares against the formal definitions rather than the
introductory shorthand.

## Direct parameter substitution

Write `H` for the multicollision range size and `G` for the number of vertices
in the Ramsey instance.  The sufficient parameter condition in JLRX
Theorem I.3 is

```
G >= H^(4t) / 4^t.
```

For each fixed multiplicity `t`, Liu--Zhandry gives exponent

```
alpha_t = (2^(t-1) - 1) / (2^t - 1)
```

in `H`.  On the tight reduction boundary, this transfers exponent

```
beta_t = alpha_t / (4t)
       = (2^(t-1) - 1) / (4t(2^t - 1))
```

in `G`.  In particular, `beta_2 = 1/24`, `beta_3 = 1/28`, and the later
values are smaller.  The cited Liu--Zhandry theorem is stated only for
constant `t`, so it does not itself justify substituting a growing `t` to
obtain the printed conclusion; the displayed fixed-`t` exponent decreases in
any event.

Conclusion: the reported near-linear lower bound does not follow from the
cited parameter substitution.  This is narrower than saying that the paper's
main results are wrong.

## Impact on our theorem

The new upper bound is proved independently from capped quantum search, the
implicit-candidate-set invariant, adaptive concentration, and a survival
recurrence.  It does not invoke JLRX or Liu--Zhandry.  JLRX matters only to
model alignment, priority, and comparison with prior lower bounds.

The apparent conflict cannot be ignored: if the unnumbered JLRX consequence
is correct for exactly the formal default relation, it contradicts our upper
bound.  The current evidence points to a parameter mismatch in that side
consequence because the printed reduction and cited lower bound can be
substituted directly.  This audit does not affect the principal JLRX
black-box nonreducibility and TFNP separation theorems, which do not use the
query-complexity paragraph.

## Publication-safe wording

Use “does not follow from the cited parameter substitution” and “apparent
parameter mismatch.”  Do not call the JLRX paper or a numbered main theorem
false.  State explicitly that our proof does not rely on the disputed
consequence and that their principal TFNP separation results are outside the
scope of the audit.

## Author clarification lifecycle

The user reports sending the revised clarification email on 2026-09-01.
No author acknowledgment is incorporated into the manuscript. The historical
draft below was superseded in Gmail and is **not the final sent wording**;
in particular, its manuscript-preparation language was removed at the user's
request. Do not reuse it as a current draft.

## Historical proposed message (superseded)

Subject: Clarification request about the quantum query lower bound for RAMSEY

Dear Professors Jain, Li, Robere, and Xun,

We are preparing a manuscript on quantum query algorithms for the default
RAMSEY relation, and we would be grateful for clarification about the quantum
query lower-bound statement in the unnumbered “Query complexity of RAMSEY”
paragraph in Section III of your FOCS 2024 paper.

We may be overlooking an intended normalization or an additional ingredient.
Using `H` for the range size of the multicollision instance and `G` for the
Ramsey graph size, we read the sufficient parameter condition in Theorem I.3
as `G >= H^(4t)/4^t`.  Combining this with the fixed-`t` Liu--Zhandry exponent
`alpha_t = (2^(t-1)-1)/(2^t-1)` appears to transfer the exponent
`alpha_t/(4t)` to `G`; for `t >= 2`, its maximum is `1/24`.  We are using the
formal convention `G = 2^n`, `K = n/2` from Definitions II.6--II.7.

Our manuscript obtains an `O(sqrt(G) polylog(G))` upper bound for the same
apparently intended bounded-error query relation, so it is important for us to
align the models and parameters correctly.  Is there a different parameter
choice, normalization, reduction direction, or additional lower-bound
ingredient behind the near-linear statement?  We want to describe your result
accurately and would greatly appreciate any guidance or correction to our
calculation.  We would also be happy to share the relevant comparison section
of our draft if helpful.

Best regards,
Cheng Xin, Ph.D.
Assistant Professor of Computer Science
California State University, Fresno
