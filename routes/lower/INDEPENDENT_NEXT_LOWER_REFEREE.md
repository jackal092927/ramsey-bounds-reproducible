# Independent referee report: next lower-bound obstruction

Date: 2026-08-12

## Verdict

**PASS AS AN OBSTRUCTION, WITH THE PROPOSED RECORD LEMMA STILL OPEN.**

The four requested checks are correct.  Proposition 4 gives an actual family
inside the forward-independent-tuple tree of $D^*(t,q)$, the small-layer
refinement has the corrected max-layer consequence, the surviving number of
singleton blocks is exactly $q-\lfloor M_0\rfloor$ under the stated
$q>M_0$ hypothesis, and the stated record-map lemma would conditionally give
the advertised one-logarithm improvement.  The report does not prove that
open record-map lemma and does not establish a new Ramsey lower bound.

## Checks

### 1. Proposition 4

The construction works over every finite field $\mathbb F_q$, including
characteristic two.  The initial points in $\mathcal A$ are distinct, every
pair $(a,e_1)$ is a vertex of $D^*$, and all consistency implications between
initial pairs hold because every first coordinate is orthogonal to $e_1$.
The equations defining $Z_0$ force $y_2\ne0$, permit normalization $y_2=1$,
and then force $y_j=0$ for $j\ge3$.  Hence

$$
Z_0=\{\langle xe_1+e_2\rangle:x\in\mathbb F_q\}.
$$

For a processed set $S$ and $z\notin S$, the candidate
$(a_z,y_z)$ satisfies $a_z\perp y_z$.  Every old-to-new consistency
antecedent is false: it has value $1$ for an initial first coordinate and
$z-x\ne0$ for a previously processed label $x$.  Moreover
$a_z\cdot y_x=x-z$, so exactly $y_z$ leaves $U_0$.  At that step
$r=\ell=0$, the candidate $b=y_z$ belongs to no current zero-dimensional
span and is therefore not popular, while exactly one point of $Z_0$ is
orthogonal to $a_z$ and

$$
1>|Z_0|/(8q).
$$

Thus the child is unmarked and its literal removal block is the singleton
$R_z=\{y_z\}$.  The $q$ blocks are distinct, each has rank one, and their
union is a $q$-point subset of the projective line on
$\langle e_1,e_2\rangle$ that spans this vector space, of dimension two.
Strictly, equation (8) omits the point $\langle e_1\rangle$; the main proof now
describes these as $q$ points on a projective line.  This wording correction
does not affect (5).  The
source explicitly allows loops in $G(t,q)$, so possible self-orthogonal
coincidences do not invalidate a $D^*$ vertex.

### 2. The $q-\lfloor M_0\rfloor$ count

Immediately before the successive singleton removals, the current sizes are
$q,q-1,\ldots,1$.  The added $r=0$ marking rule marks exactly those steps
whose current integer size $m$ satisfies $m\le M_0$.  If $q>M_0$, the number
with $m>M_0$ is therefore

$$
\#\{m\in\{1,\ldots,q\}:m>M_0\}=q-\lfloor M_0\rfloor.
$$

### 3. Corrected Lemma 5 consequence

For fixed $b\in Z_r$, the source bound gives at most $2q^{t-r}$ extending
choices of $a$.  A layer with $|Z_r|\le M_rq^r$ therefore contributes at most
$2M_rq^t$ newly marked children, and summing over $0\le r\le t$ gives (10).
If a child of rank type $r$ remains unmarked, then
$|Z_r|>M_rq^r$.  Since $\ell=\ell_r$ maximizes the layer size among
$Z_0,\ldots,Z_r$, the corrected inference is

$$
|Z_\ell|\ge |Z_r|>M_rq^r,
\qquad |R|>\frac{M_r}{16}q^{r-1}.
$$

The coefficient is correctly $M_r$, not $M_\ell$.  For fixed $M_r>0$ and
$r\ge2$, this eventually exceeds $[r-1]_q$, the maximum number of projective
points in vector rank at most $r-1$; hence
$\dim\operatorname{span}R\ge r$.  This remains a within-block statement and
does not supply transverse rank across steps.

### 4. Conditional record-map implication

Fixing a signature with $u$ unmarked positions and the local indices of its
marked children, the proposed lemma would bound the realizing paths by

$$
\exp(O_t(q\log q))(C_tq^t)^u.
$$

There are at most $2^k$ signatures and at most $h^{k-u}$ marked-index
sequences, where $h=O_t(q^t)$.  Consequently the total is bounded by

$$
2^k h^{k-u}(C_tq^t)^u\exp(O_t(q\log q)).
$$

When $k\ge c_tq\log q$, the last exponential is absorbed into a
constant-to-the-$k$ factor, uniformly in $u$, giving
$\overrightarrow{i_k}(D^*)\le(C'_tq^t)^k$.  Combining this with
$|V(D^*)|=\Omega_t(q^{2t-1})$, the existing sampling argument, and a prime
power $q=\Theta_t(k/\log k)$ yields conditionally

$$
r(s,k)=\Omega_s\!\left(
\frac{k^{s-1}}{(\log k)^{s-2}}
\right),\qquad t=s-1.
$$

This verifies only the implication from the proposed record lemma; the lemma
itself remains unproved.

## Reproduction and provenance

The checker passed with its default parameters and independently with
$t=2$ and $q\in\{2,3,5,7\}$.  Its coordinate replay covers prime fields; the
written proof of Proposition 4 uses field operations only and therefore
covers all prime powers.

- `NEXT_LOWER_BOUND.md`: SHA-256
  `b797f3c5b13f2755450048a012c50a881fe42729d4f4a4c3858006b342f0e429`
- `bradac_multiwitness_obstruction.py`: SHA-256
  `1af24973180241895958c6976f25e95eaa1ebd1f5e5d7d29d18605b6ca5c0370`
- Bradač arXiv:2605.28793v3 `main.tex`: SHA-256
  `90acf52f3766e780bc22114e08aa46b115cfe86e33d340e7f7eace01bb7fe39f`
