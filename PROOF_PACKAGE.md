# Proof Package

## Claim

Let \(H\) be the fixed graph on vertex set \(V\), let

\[
\mathcal F=\{F\text{ on }V:F\text{ is triangle-free and }\alpha(F)<18\},
\]

and let \(d_H(F)=|E(H)\setminus E(F)|\). Assume the already certified theorem

\[
\rho(H):=\inf_{F\in\mathcal F}d_H(F)\ge 7.
\]

Fix a seed edge \(f\in E(H)\), and define the exact-seven branch

\[
\mathcal B_f=\{F\in\mathcal F:d_H(F)=7,\ f\notin E(F)\}.
\]

The claims under adversarial review are:

1. If \(\mathcal B_f\ne\varnothing\), then some \(F^*\in\mathcal B_f\) is
   maximal triangle-free. More strongly, \(F^*\) can be obtained from any
   \(F\in\mathcal B_f\) by adding only pairs outside \(E(H)\); in particular,
   the full seven-edge deletion support and the fixed branch edge are
   preserved.
2. For a primary graph \(G\), the all-pair selector clauses used in the paper
   have an auxiliary satisfying assignment if and only if \(G\) is maximal
   triangle-free, provided the triangle clauses are also imposed.
3. Consequently, every genuine exact-seven branch-1 repair extends to a model
   of the frozen maximal-union CNF. Therefore a checked UNSAT proof for that
   CNF would close branch 1. A SAT result for the finite-bank CNF need not be a
   repair, and an UNKNOWN result implies neither existence nor nonexistence.

## Status

**PROVABLE AS STATED.**

The claims survive unchanged. The first and third claims depend on the already
certified premise \(\rho(H)\ge7\); they are not independent alternative proofs
of that premise.

## Assumptions

- \(H\) and \(F\) are finite simple graphs on the same finite labelled vertex
  set \(V\).
- Additions of pairs outside \(E(H)\) do not change \(d_H\).
- Adding an edge to a graph cannot increase its independence number.
- The theorem \(\rho(H)\ge7\) has already been established independently of
  the maximality argument by the budget-five and exact-six proof packages.
- The branch-1 common CNF is a sound relaxation: every genuine branch-1 target
  extends to a model of it.
- Each of the four positive retention units is a proved consequence of that
  common CNF.
- Every installed mask is an actual 18-vertex subset, and its positive
  pair-hitting clause is therefore necessary for \(\alpha(F)<18\).

## Notation

- \(N_G(v)\) is the open neighbourhood of \(v\) in \(G\).
- A missing pair \(uv\notin E(G)\) is *safe* if
  \(N_G(u)\cap N_G(v)=\varnothing\). Equivalently, adding \(uv\) creates no
  triangle.
- A triangle-free graph is *maximal triangle-free* if adding any missing pair
  creates a triangle.
- \(x_{uv}\) is the primary variable saying that \(uv\in E(G)\).
- \(y_{uv,w}\) is an existential auxiliary variable selecting \(w\) as a
  common neighbour of the missing pair \(uv\).

## Proof Strategy

First saturate a target using only safe additions of original nonedges. The
certified radius lower bound then shows that every still-deleted seed edge is
already triangle-blocked: otherwise restoring it would produce a target at
distance six. This proves the maximal-triangle-free normal form without
altering the branch. Next prove the selector encoding by direct projection on
the primary variables. Finally compose the normal form with the soundness of
the common relaxation, retention entailments, and mask clauses.

## Dependency Map

1. The maximality normal form depends on the safe-edge lemma, finite
   termination, and \(\rho(H)\ge7\).
2. The safe-edge lemma depends only on the definition of a triangle and the
   monotonicity of independence number under edge addition.
3. The selector projection is a direct Boolean equivalence and does not depend
   on \(\rho(H)\ge7\).
4. The maximal-union implication depends on the normal form, common-CNF
   soundness, the four singleton entailments, mask validity, and selector
   projection.
5. The implication from formula UNSAT to branch nonexistence is the
   contrapositive of item 4. No reverse target-to-SAT equivalence is claimed for
   arbitrary SAT models because the independent-set bank is finite.

## Proof

### Step 1. Safe additions preserve the target conditions

Let \(G\in\mathcal F\), and suppose \(uv\notin E(G)\) satisfies

\[
N_G(u)\cap N_G(v)=\varnothing.
\]

Any triangle newly created by adding \(uv\) would have a third vertex \(w\)
adjacent to both \(u\) and \(v\) before the addition. This contradicts the
displayed condition. Hence \(G+uv\) remains triangle-free.

Every independent set of \(G+uv\) is also an independent set of \(G\), because
\(G+uv\) has all edges of \(G\) and one additional edge. Therefore

\[
\alpha(G+uv)\le\alpha(G)<18.
\]

If additionally \(uv\notin E(H)\), then

\[
E(H)\setminus E(G+uv)=E(H)\setminus E(G),
\]

so both the deletion distance and the complete deletion support are unchanged.

### Step 2. Saturate only original nonedges

Take \(F\in\mathcal B_f\). While there is a safe pair

\[
uv\notin E(H)\cup E(F),
\]

add it. The finite set \(\binom{V}{2}\) guarantees termination. By Step 1,
every intermediate graph remains in \(\mathcal B_f\), and the final graph
\(F_0\) satisfies

\[
uv\notin E(H)\cup E(F_0)
\quad\Longrightarrow\quad
N_{F_0}(u)\cap N_{F_0}(v)\ne\varnothing.
\]

No seed edge was added in this process, so \(E(H)\setminus E(F_0)\) is exactly
the deletion support of \(F\), including the fixed edge \(f\).

### Step 3. Every deleted seed edge is triangle-blocked

Let \(e\in E(H)\setminus E(F_0)\). Suppose for contradiction that \(e\) is
safe in \(F_0\). By Step 1, \(F_0+e\) is triangle-free and has independence
number below 18. Restoring one seed edge changes the one-sided distance by
exactly one, so

\[
d_H(F_0+e)=d_H(F_0)-1=6.
\]

Thus \(F_0+e\in\mathcal F\), contradicting \(\rho(H)\ge7\). Therefore every
deleted seed edge has a common neighbour in \(F_0\).

This includes the fixed branch edge. In the concrete branch
\(f=(97,99)\), if both other edges of the seed triangle were present,
restoring \(f\) would not be safe because it would create that triangle. If
restoring \(f\) were safe, then at least one other triangle edge would remain
absent, and the resulting distance-six graph would still fall under the
previously certified global three-branch exclusion. No assumption that the
restored graph remains in branch 1 is used.

Combining Steps 2 and 3, every missing pair of \(F_0\) has a common neighbour.
For a triangle-free graph this is equivalent to maximal triangle-freeness:
adding a missing pair creates a triangle exactly when its endpoints already
have a common neighbour. Set \(F^*=F_0\). This proves Claim 1.

### Step 4. Project the selector clauses exactly

For each unordered pair \(uv\), introduce \(y_{uv,w}\) for all
\(w\in V\setminus\{u,v\}\) and impose

\[
x_{uv}\vee\bigvee_{w\notin\{u,v\}}y_{uv,w},
\]

\[
\neg y_{uv,w}\vee x_{uw},
\qquad
\neg y_{uv,w}\vee x_{vw}.
\]

Fix an assignment of the primary variables. If the selector clauses have an
auxiliary satisfying assignment and \(x_{uv}=0\), the long clause forces some
\(y_{uv,w}=1\). The two binary clauses then force
\(x_{uw}=x_{vw}=1\), so \(w\) is a common neighbour of \(u\) and \(v\).

Conversely, if \(x_{uv}=1\), assign all \(y_{uv,w}=0\). If \(x_{uv}=0\) and
\(u,v\) have a common neighbour \(w\), assign \(y_{uv,w}=1\) and all other
selectors for that pair to zero. In either case all displayed clauses for the
pair are satisfied. The auxiliary blocks for distinct pairs are disjoint, so
these pairwise extensions combine into one global extension.

Therefore the selector block projects exactly to the condition that every
missing pair has a common neighbour. Together with the triangle clauses, this
is exactly maximal triangle-freeness. This proves Claim 2. Reverse Tseitin
implications are unnecessary because the \(y\)-variables are existential
witnesses rather than definitions required to be unique.

### Step 5. Compose the normal form with the maximal-union CNF

Assume a genuine branch-1 exact-seven repair exists. By Claim 1, there is such
a repair \(F^*\) that is maximal triangle-free and has the same seven deleted
seed edges. Its primary assignment satisfies the common branch-1 relaxation.
Because the four positive units are consequences of that relaxation, it
satisfies those units. Since \(\alpha(F^*)<18\), every installed 18-set has at
least one present pair, so every installed hitting clause is satisfied.
Finally, Claim 2 supplies an auxiliary assignment for all maximality selectors.
Thus \(F^*\) extends to a model of the maximal-union CNF.

Taking the contrapositive, if that exact CNF is UNSAT, no genuine branch-1
exact-seven repair exists. This proves the first implication in Claim 3.

The reverse implication from an arbitrary CNF model to a target is not valid:
the finite mask bank need not contain every independent 18-set. A model must
undergo a complete independence-number check before it can be called a repair.
Likewise, a timeout or UNKNOWN result supplies neither a model nor a
refutation and therefore implies nothing about branch existence. This proves
the remaining claim boundaries in Claim 3. \(\square\)

## Corrections or Missing Assumptions

- No correction to the maximality proposition is required.
- The paper should keep the phrase “a feasible branch-1 repair exists if and
  only if one exists that is maximal triangle-free.” It must not say that every
  raw repair is already maximal.
- The use of \(\rho(H)\ge7\) must remain explicit. Omitting it would prove only
  saturation on original nonedges, not blocking of deleted seed edges.
- An UNSAT result for branch 1 would not close the other two triangle-edge
  branches. The certified trivial seed automorphism group prevents a symmetry
  transfer.

## Open Risks

- The mathematical implication is conditional on the independently certified
  computational theorem \(\rho(H)\ge7\) and on the authenticated singleton
  entailments. This is a proof-carrying trust boundary, not a gap in the
  graph-theoretic argument.
- The current maximal-union endpoint is UNKNOWN. Its conflict count, memory
  use, elapsed time, and deleted incomplete proof prefix have no mathematical
  evidentiary value.
- No current result proves \(\rho(H)=7\), \(\rho(H)\ge8\), the existence of a
  100-vertex \((3,18)\)-Ramsey graph, or \(R(3,18)\ge101\).
