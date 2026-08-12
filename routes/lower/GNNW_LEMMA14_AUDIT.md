# Independent audit of GNNW Lemma 14

Date: 2026-08-12  
Paper: Gupta--Ndiaye--Norin--Wei, *Optimizing the CGMS upper bound on Ramsey
numbers*, [arXiv:2407.19026v1](https://arxiv.org/abs/2407.19026v1)  
Audited source: `RamseyArXiv.tex`, SHA-256
`9475bdc42aac1cb2c995fdfba1803f0ec4dc53ac0c5a838623cb31b5e19eaa2e`  
Audited notebook: `Ramsey12.nb`, SHA-256
`26fa33ead4584c995233368acd19853c7f55e550fcd4b6d7206c820f0aebc5b5`

## Claim and status

**Claim audited.** Source lines 445--464 claim that the one-sided estimate

$$
R(k,\ell)\leq \exp\{k h(\ell/k)-\alpha\ell+o(k)\},\qquad \ell\leq k,
\tag{A}
$$

where

$$
h(r)=(1+r)\log(1+r)-r\log r,
$$

puts both $(x,e^\alpha(1-x))$ (for $x<1/2$) and
$(x,1-xe^{-\alpha})$ (for every $x$) in the global Ramsey region
$\mathcal R$.

**Status: NOT CURRENTLY JUSTIFIED.** **[DERIVED]** The comparison on source
line 460 has the wrong direction whenever $k>\ell$ and
$x<e^\alpha(1-x)$. The inequality on line 463 is valid only in the
complementary range $x\leq e^\alpha(1-x)$; read with that intended range it
is correct, but it cannot repair line 460. Assumption (A), together with
symmetry and all ratios $k/\ell$, certifies instead the boundary

$$
Y_{\rm legal}(x)=\min\{e^\alpha(1-x),\,1-xe^{-\alpha}\}
=
\begin{cases}
1-xe^{-\alpha},&0<x\leq t_\alpha,\\
e^\alpha(1-x),&t_\alpha\leq x<1,
\end{cases}
\qquad
t_\alpha=\frac{e^\alpha}{1+e^\alpha}.
\tag{B}
$$

This verdict is about the implication proved in Lemma 14. It does **not**
prove that points above (B) are outside the true Ramsey region; such a
non-membership statement would require lower bounds on Ramsey numbers that
are not supplied by (A).

## Assumptions and notation

1. **[SOURCE]** Source lines 257--258 define $\mathcal R$ using one fixed pair
   $(x,y)$ whose estimate must hold for all sufficiently large $k+\ell$.
2. **[SOURCE]** Observation 9(4), lines 262--274, permits $o(k),o(\ell)$
   losses before passing to the closure $\mathcal R$.
3. **[STANDARD]** $R(k,\ell)=R(\ell,k)$.
4. Put $E=e^\alpha\geq1$, $a(x)=E(1-x)$ and
   $b(x)=1-x/E$.

The only asymptotic assumption in the derivation is (A). In particular, the
argument below does not import a conclusion from another audit route.

## Source-line-to-formula map

| Source | Source assertion | Independent formula | Verdict |
|---|---|---|---|
| 257--258 | one $(x,y)$ must work for all $k,\ell$ | both half-planes of ratios must be checked | **[SOURCE]** |
| 445--458 | for $\ell\leq k$, entropy gives a bound at $(x,E(1-x))$ | equation (C) below | **[DERIVED: correct]** |
| 460 | if $x\leq E(1-x)$, the $(k,\ell)$ exponents may be swapped with `\(\leq\)` | quotient is $(E(1-x)/x)^{k-\ell}\geq1$ | **[FAILED: reversed]** |
| 462--463 | use symmetry and $b(x)\leq a(x)$ | $b(x)\leq a(x)$ iff $x\leq t_\alpha$ | **[RANGE-DEPENDENT; cannot repair line 460]** |
| 473--476 | notebook/paper chooses $a(X)$ below $1/2$ and $b(X)$ above $1/2$ | (B) chooses $b(X)$ below $t_\alpha$ and $a(X)$ above it | **[MISMATCH for $\alpha>0$]** |
| 481 | initial pair $(\alpha_0,\beta_0)=(0,.08)$ uses $Y=1-X$ | $a=b=1-X$ at $\alpha=0$ | **[INDEPENDENT of Lemma 14]** |
| 487 | first positive-$\alpha$ step uses $(.09/e,.045)$ | corrected $Y$ makes condition (2) negative at $\lambda=1$ | **[CERTIFIED COUNTEREXAMPLE to this iteration]** |
| 489 | later values $.033,.03$ are reached recursively | recursion has not passed its first positive-$\alpha$ step | **[NOT ESTABLISHED by this chain]** |

## Dependency map

$$
\text{one-sided premise (A)}
\xrightarrow[\ell\leq k]{\text{entropy}}
(s,E(1-s))
\xrightarrow[k\leq\ell]{\text{symmetry}}
(E(1-s),s)
\xrightarrow{\text{all ratios}}
Y\leq\min\{a(X),b(X)\}.
$$

The paper instead uses the two larger outer branches, then feeds their
$Y_i$ values into Theorem 13's analytic inequality. Consequently Lemma 14 is
a genuine dependency of every positive-$\alpha$ iteration, but not of the
initial $\alpha_0=0$ computation.

## Proof of the corrected all-ratio envelope

### Step 1: the two oriented entropy estimates

For every $s\in(0,1)$ and $\ell\leq k$, the entropy expression in (A) is at
most the corresponding tangent expression. Thus

$$
\log R(k,\ell)
\leq-k\log s-\ell\log(E(1-s))+o(k).
\tag{C}
$$

This is exactly the valid calculation on source lines 453--458. By Ramsey
symmetry, for $k\leq\ell$ the same premise applied to $R(\ell,k)$ gives

$$
\log R(k,\ell)
\leq-k\log(E(1-s))-\ell\log s+o(\ell).
\tag{D}
$$

### Step 2: a fixed pair that works in both orientations

For $\ell\leq k$, take $s=x$ in (C). It is enough that

$$
y\leq E(1-x)=a(x).
\tag{E}
$$

For $k\leq\ell$, take $s=y$ in (D). It is enough that

$$
x\leq E(1-y),
\quad\text{equivalently}\quad
y\leq1-x/E=b(x).
\tag{F}
$$

Equations (E)--(F), Observation 9(4), and closure prove that every
$y\leq\min\{a(x),b(x)\}$ belongs to $\mathcal R$.

### Step 3: why checking only the two endpoints did not lose a ratio

For completeness, impose the exponent comparison furnished by (A) for
every ratio $r\in(0,1]$. The $\ell\leq k$ family is

$$
-\log x-r\log y\geq h(r)-\alpha r.
\tag{G}
$$

At fixed $x$, optimizing (G) over $r$ gives

$$
y\leq
\begin{cases}
E/(4x),&x\leq1/2,\\
E(1-x),&x\geq1/2.
\end{cases}
\tag{H}
$$

Indeed the derivative of
$\alpha-[h(r)+\log x]/r$ has the sign of
$\log(x(1+r))$. The symmetric $k\leq\ell$ family is

$$
-r\log x-\log y\geq h(r)-\alpha r,
\tag{I}
$$

and optimization gives

$$
y\leq
\begin{cases}
1-x/E,&x\leq E/2,\\
E/(4x),&x\geq E/2.
\end{cases}
\tag{J}
$$

The minimum of (H) and (J) is precisely
$\min\{a(x),b(x)\}$. For example,
$4x(1-x/E)\leq E$ is $(E-2x)^2\geq0$, and
$4x(1-x)\leq1$. Therefore (B) is not merely one convenient sufficient
choice: it is the maximal fixed-coordinate envelope certified by the two
all-ratio exponent families (G) and (I).

Finally,

$$
a(x)=b(x)\iff x=t_\alpha=\frac{E}{1+E}.
$$

This proves the piecewise form in (B). Notice that $t_\alpha>1/2$ whenever
$\alpha>0$.

## Explicit algebraic counterexample to source line 460

Ignoring the harmless $o(k)$ term, the quotient of the alleged left and
right sides is

$$
\frac{x^{-k}a(x)^{-\ell}}{x^{-\ell}a(x)^{-k}}
=\left(\frac{a(x)}x\right)^{k-\ell}.
\tag{K}
$$

Under the line's assumptions $a(x)\geq x$ and $k\geq\ell$, (K) is at least
one, not at most one. It is strictly larger away from equality. A rational
counterexample already occurs at $\alpha=0$, $x=2/5$, $k=2$, $\ell=1$:

$$
x^{-2}(1-x)^{-1}=\frac{125}{12}
>\frac{125}{18}=x^{-1}(1-x)^{-2}.
$$

Thus the displayed comparison itself is false, independently of any
asymptotic or numerical issue.

## Paper/Notebook branch versus the corrected branch

The source and `Ramsey12.nb` use

$$
Y_{\rm paper}(x)=
\begin{cases}
a(x),&x<1/2,\\
b(x),&x\geq1/2.
\end{cases}
$$

For $\alpha>0$, comparison with (B) is:

| range of $x$ | corrected value | paper value | result |
|---|---:|---:|---|
| $0<x<1/2$ | $b(x)$ | $a(x)$ | paper uses the strictly larger branch |
| $1/2\leq x\leq t_\alpha$ | $b(x)$ | $b(x)$ | branches agree |
| $t_\alpha<x<1$ | $a(x)$ | $b(x)$ | paper uses the strictly larger branch |

So “opposite branch” is exact on the two outer ranges; there is a middle
range where the notebook happens to agree with the corrected hull.

## Certified failure of the first positive-$\alpha$ iteration

Define, exactly as on source lines 473--480,

$$
F_\beta(\lambda)=h(\lambda)
+(-\tfrac14\lambda+\beta\lambda^2+\tfrac2{25}\lambda^3)e^{-\lambda},
\qquad M(\lambda)=\lambda e^{-\lambda},
$$

$$
X(\lambda)=
\bigl(1-e^{-F_\beta'(\lambda)}\bigr)^{1/(1-M(\lambda))}
(1-M(\lambda)),
$$

where the final juxtaposition is multiplication, as in the source formula:
$X=(1-e^{-F'})^{1/(1-M)}(1-M)$. The condition to verify is

$$
\psi(\lambda)=F_\beta(\lambda)
+\frac12\{\log X+\lambda\log M+\lambda\log Y\}>0.
\tag{L}
$$

At the first positive-$\alpha$ stage, take
$\alpha=9/(100e)$, $\beta=9/200$, and $\lambda=1$. Then

$$
F_\beta(1)=2\log2-\frac1{8e},\qquad
F_\beta'(1)=\log2+\frac{41}{200e},\qquad M(1)=e^{-1}.
$$

Using 200-bit Arb interval arithmetic and the legal branch
$Y=1-Xe^{-\alpha}$ gives

$$
\begin{aligned}
X&=0.2359152801196664307331922155\ldots,\\
t_\alpha&=0.5082765313681368034254873630\ldots,\\
Y_{\rm legal}&=0.7717677825268715065633772580\ldots,\\
\psi(1)&=-0.01136761652270750631625525636\ldots<0.
\end{aligned}
$$

The certified interval for the last quantity is

```text
[-0.0113676165227075063162552563600106865400367457004020437627
 +/- 4.64e-59]
```

By contrast, the larger paper branch $Y=E(1-X)$ gives
$\psi(1)=0.0001844423173285711\ldots>0$. Thus this is not merely a
possible loss of slack: after replacing Lemma 14 by the envelope actually
certified by its premise, the paper's stated $(\alpha_1,\beta_1)$ fails
condition (2) at a single explicit point. Nor can the `\(X\leq\)` freedom on
source line 473 rescue this point: for every allowed $0<X\leq
0.235916$, the legal branch is $Y=1-X/E$, and
$X(1-X/E)$ is strictly increasing because $X<E/2$. Hence the displayed
$X$ already maximizes the logarithmic $X Y$ contribution among all allowed
choices. The interval calculation is
reproduced by [gnnw_hull_counterexample.py](./gnnw_hull_counterexample.py).

Consequently, the recursive route to $\beta_2=.033$ and $\beta_3=.03$ does
not start as written. This audit does not rule out a different $F$, a smaller
positive improvement, or an independent Ramsey-region input.

## Why the initial $\beta=.08$ stage survives this audit

**[DERIVED: dependency verdict, not a fresh global numerical proof.]** Yes:
the initial stage is independent of Lemma 14.

1. Source line 481 explicitly obtains region membership from Observation
   9(1), the standard $(X,1-X)\in\mathcal R$ bound.
2. It sets $\alpha_0=0$, so $a(X)=b(X)=1-X$ and
   $t_0=1/2$. The paper branch and (B) are identical everywhere.
3. The notebook's first substitution is `a -> 0, b -> 0.08`; positive
   $\alpha$ enters only in the later iterations.

Therefore the branch-direction defect does not affect the initial
$\beta=.08$ construction. Its separate all-$\lambda$ numerical verification
remains whatever is supplied by the paper/Notebook; this audit establishes
independence, not a new certified proof of that global inequality.

## Failure modes and minimal repair target

- Reversing line 460's sign alone is not a repair: it removes the claimed
  implication instead of proving the desired larger branch.
- Replacing the cutoff $1/2$ by $t_\alpha$ while retaining the same two
  notebook branches is also insufficient; the branches themselves must be
  swapped as in (B).
- Downward closure cannot recover $Y_{\rm paper}$ because it is strictly
  larger than $Y_{\rm legal}$ on both outer ranges.
- There is also a secondary domain issue in the literal first conclusion:
  if $E(1-x)>1$, the claimed point is not even in the closure of
  $(0,1)^2$ used to define $\mathcal R$. The corrected envelope (B) always
  stays in the coordinate domain. This does not drive the numerical
  counterexample above.
- The minimal missing mathematical input for the preprint iteration is an
  independent lemma placing the particular curve
  $(X(\lambda),Y_{\rm paper}(X(\lambda)))$ in $\mathcal R$ wherever it lies
  above (B). Assumption (A), symmetry, and entropy alone do not provide it.
- A viable alternative is to re-optimize $F,\alpha,\beta$ using (B) and then
  certify (L) uniformly. The explicit negative value above shows that the
  preprint's first positive-$\alpha$ parameters cannot simply be reused.

## Final verdict

1. **Line 460: comparison direction is reversed.** The rational example
   $(\alpha,x,k,\ell)=(0,2/5,2,1)$ is a literal counterexample.
2. **The globally certified hull is (B),** with cutoff
   $t_\alpha=e^\alpha/(1+e^\alpha)$ and the smaller of the two branches.
3. **The $.03$ iterative conclusion is not proved by the displayed
   Lemma-14/Notebook chain.** The corrected hull already makes the $.045$
   stage fail at $\lambda=1$.
4. **The initial $.08$ stage does not depend on Lemma 14** and is unchanged
   by this particular defect.
