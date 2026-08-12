# Standalone proof of the GNNW book lemma

Date: 2026-08-12  
Source being repaired: Gupta--Ndiaye--Norin--Wei,
arXiv:2407.19026v1, Lemmas 7--11 and Theorem 12.

## Claim boundary

This note proves the combinatorial input used by the certified diagonal
Ramsey descent without invoking GNNW Lemma 11 or Theorem 12 as black boxes.
It retains their definitions of a candidate and of the rate region, and it
uses only elementary Ramsey recursion, convexity, averaging, and induction.

Let a **candidate** be a pair of nonempty disjoint vertex sets $(X,Y)$ in a
red--blue complete graph.  Its red cross-density is

$$
d(X,Y)=\frac{e_R(X,Y)}{|X||Y|}.
$$

It is $(k,\ell,t)$-good if $X\cup Y$ contains a red $K_k$, or $X$ contains
a blue $K_t$, or $Y$ contains a blue $K_\ell$.

Let $\mathcal R$ be the closure of the set of pairs $(x,y)\in(0,1)^2$ for
which, for all sufficiently large $k+\ell$,

$$
R(k,\ell)\le x^{-k}y^{-\ell},
$$

and let $\mathcal R_*$ be its interior.

### Theorem A (book induction)

Suppose $0<\mu_0,x_0,y_0,p<1$,

$$
x_0<p^{1/(1-\mu_0)}(1-\mu_0),
\qquad (x_0,y_0)\in\mathcal R_*.
\tag{A.1}
$$

There is $L_0$ such that, for all positive integers $k,\ell,t$ with
$\ell\ge L_0$, every candidate of density at least $p$ and satisfying

$$
|X||Y|\ge x_0^{-k}y_0^{-\ell}\mu_0^{-t}
\tag{A.2}
$$

is $(k,\ell,t)$-good.

### Corollary B (balanced-book bound)

Suppose $0<\mu,x,y,p<1$,

$$
x<p^{1/(1-\mu)}(1-\mu),
\qquad (x,y)\in\mathcal R_*.
\tag{B.1}
$$

For all sufficiently large $\ell$, every red--blue coloring of $K_N$ of
red density at least $p$, where

$$
N\ge x^{-k/2}(\mu y)^{-\ell/2},
\tag{B.2}
$$

contains a red $K_k$ or a blue $K_\ell$.

The statements hold for all $p,\mu\in(0,1)$; no relation $p>\mu$ is needed.

## Four elementary inputs

### Lemma 1 (an interior point gives its own eventual bound)

If $(u,v)\in\mathcal R_*$, then, for all sufficiently large $a+b$,

$$
R(a,b)\le u^{-a}v^{-b}.
\tag{1.1}
$$

**Proof.** Choose $\eta>0$ so that
$(u+2\eta,v+2\eta)\in\mathcal R$.  Since $\mathcal R$ is the closure of
the eventual-bound set, there is a point $(u',v')$ in that set with
$u'>u$ and $v'>v$.  Its defining bound is stronger than (1.1). $\square$

### Lemma 2 (density convexity)

For every candidate,

$$
\sum_{v\in X}d(X,N_R(v)\cap Y)|N_R(v)\cap Y|
\ge e_R(X,Y)d(X,Y),
\tag{2.1}
$$

where an empty-neighborhood summand is interpreted as zero.

**Proof.** Put $d_y=|N_R(y)\cap X|$.  Multiplying the left side by $|X|$
gives $\sum_{y\in Y}d_y^2$.  Cauchy--Schwarz bounds this below by
$|Y|^{-1}(\sum_y d_y)^2=e_R(X,Y)^2/|Y|$, which is $|X|$ times the
right side. $\square$

### Lemma 3 (blue-book extraction)

Let $0<\nu<1$, and let $b,k,m$ be positive integers with
$m\ge5\nu^{-1}b^2$ and $b\le m$.  Suppose $|X|\ge5m^2$ and at least
$R(k,m)$ vertices
$v\in X$ have blue degree at least $\nu|X|$ inside $X$.  Then $X$ contains
a red $K_k$, or it contains disjoint sets $S,T$ such that $S$ is a blue
clique, every edge from $S$ to $T$ is blue, and

$$
|S|=b,\qquad |T|\ge\frac{\nu^b}{2}|X|.
\tag{3.1}
$$

**Proof.** The high-blue-degree vertices contain a red $K_k$ or a blue
$K_m$.  In the latter case call its vertex set $U$.  Put
$d_z=|N_B(z)\cap U|$ for $z\in X\setminus U$ and let $D$ be their average.
Counting ordered blue pairs from $U$ to $X\setminus U$ gives

$$
D\ge\frac{m(\nu|X|-m)}{|X|-m}
=\nu m-\frac{(1-\nu)m^2}{|X|-m}
>\nu m-\frac14,
\tag{3.2}
$$

where $|X|\ge5m^2$ and $m\ge1$ were used in the last inequality.  Let
$q=\lfloor D\rfloor$.  The discrete convexity of
$j\mapsto\binom jb$ on nonnegative integers (with value zero for $j<b$)
shows that a uniform $b$-subset $S$ of $U$ satisfies

$$
\mathbb E|N_B(S)\cap(X\setminus U)|
=\binom mb^{-1}\sum_{z\in X\setminus U}\binom{d_z}b
\ge\binom mb^{-1}\binom qb|X\setminus U|.
\tag{3.3}
$$

Since $q>D-1>\nu m-5/4$ and $m\ge5\nu^{-1}b^2$, every
$0\le i<b$ satisfies

$$
\frac{q-i}{m-i}
>\nu-\frac{(1-\nu)i+5/4}{m-i}
\ge\nu\left(1-\frac{b+1/4}{5b^2}\right).
$$

For the second inequality, the fraction being subtracted increases with
$i$, and at $i=b-1$ it is at most the claimed value because

$$
\frac{(1-\nu)(b-1)+5/4}{5b^2/\nu-(b-1)}
\le\frac{\nu(b+1/4)}{5b^2};
$$

after cross-multiplication, the difference between the right numerator and
the left numerator is
$\nu(b-1)(1-(b+1/4)/(5b^2))\ge0$.

(If $q<b$, the last strict lower bound would be positive at $i=q$, an
impossibility, so the binomial ratio is well-defined.)  Hence

$$
\frac{\binom qb}{\binom mb}
\ge\nu^b\left(1-\frac{b+1/4}{5b^2}\right)^b
\ge\frac34\nu^b.
\tag{3.4}
$$

The last elementary bound is weakest at $b=1$, where its left factor is
$3/4$; for $b\ge2$, Bernoulli's inequality gives at least
$1-(b+1/4)/(5b)>3/4$.  Finally
$|X\setminus U|\ge(4/5)|X|$, so (3.3)--(3.4) exceed
$3\nu^b|X|/5>\nu^b|X|/2$.  Some $S$ therefore has a common blue page $T$
satisfying (3.1). $\square$

### Lemma 4 (the limit needed to choose the moment)

For every $p,\mu\in(0,1)$,

$$
\lim_{r\to\infty}
(p^{1/r}-\mu)^r(1-\mu)^{1-r}
=p^{1/(1-\mu)}(1-\mu),
\tag{4.1}
$$

where $r$ runs through sufficiently large positive integers, for which the
base is positive.

**Proof.** Since $p^{1/r}\to1>\mu$, positivity is eventual, and

$$
r\log\left(1+\frac{p^{1/r}-1}{1-\mu}\right)
\longrightarrow\frac{\log p}{1-\mu}.
$$

Exponentiation and the remaining factor $1-\mu$ prove (4.1). $\square$

## Proof of Theorem A

The strict inequality in (A.1) implies $x_0+\mu_0<1$.  By Lemma 4 choose
an integer $r>1$ such that

$$
x_0<(p^{1/r}-\mu_0)^r(1-\mu_0)^{1-r}.
\tag{5.1}
$$

After fixing $r$, choose $\varepsilon>0$ sufficiently small that

$$
\begin{gathered}
p\ge2\varepsilon,\qquad
(1+\varepsilon)(\mu_0+\varepsilon)\le1,\qquad
x_0+\mu_0+2\varepsilon<1,\\
(x_0+2\varepsilon,y_0+2\varepsilon)\in\mathcal R_*,\\
\mu_0+2\varepsilon
\le\frac{\mu_0+\varepsilon}
{(\mu_0+\varepsilon)+(x_0+\varepsilon)},\qquad
(p-\varepsilon)^{1/r}>\mu_0+3\varepsilon,\\
x_0\le
\big((p-\varepsilon)^{1/r}-\mu_0-3\varepsilon\big)^r
(1-\mu_0-\varepsilon)^{1-r}-\varepsilon.
\tag{5.2}
\end{gathered}
$$

All requirements follow by openness, continuity, (5.1), and the strict
inequality $x_0+\mu_0<1$.  Set

$$
x=x_0+\varepsilon,\qquad y=y_0+\varepsilon,\qquad
\mu=\mu_0+\varepsilon,\qquad \delta_n=\frac\varepsilon n.
\tag{5.3}
$$

We prove the following stronger assertion by induction on $n=k+t$, with
$\ell\ge L_0$ fixed.  If

$$
d(X,Y)\ge p-\delta_n
\tag{5.4}
$$

and

$$
(d(X,Y)+\delta_n-p)^r|X||Y|
\ge x^{-k}y^{-\ell}\mu^{-t},
\tag{5.5}
$$

then $(X,Y)$ is $(k,\ell,t)$-good.  The cases $k=1$ or $t=1$ are
immediate.

First note that (A.2) and $d(X,Y)\ge p$ imply (5.5): because
$x_0\le x/(1+\varepsilon)$, $y_0\le y/(1+\varepsilon)$, and
$\mu_0\le\mu/(1+\varepsilon)$, it is enough that

$$
\frac{\varepsilon^r}{n^r}(1+\varepsilon)^{n+\ell}\ge1.
\tag{5.6}
$$

A single sufficiently large $L_0$ makes (5.6) true for every $n\ge2$.

### Regularization and the size of $X$

Delete from $X$ any vertex having fewer than
$(p-\delta_n)|Y|$ red neighbors in $Y$.  Both the nonnegative excess

$$
e_R(X,Y)-(p-\delta_n)|X||Y|
$$

and its normalization by $|X||Y|$ do not decrease, so the left side of
(5.5) does not decrease.  The positive right side prevents deletion of all
vertices.  We may consequently assume

$$
d(X',Y)\ge p-\delta_n
\quad\text{for every nonempty }X'\subseteq X.
\tag{5.7}
$$

Lemma 1 and the interior condition in (5.2) imply, for sufficiently large
$L_0$, that if

$$
|Y|\ge(x+\varepsilon)^{-k}(y+\varepsilon)^{-\ell},
$$

then $Y$ already contains a red $K_k$ or a blue $K_\ell$.  Otherwise,
using $d+\delta_n-p\le1$ in (5.5),

$$
|X|
\ge\left(\frac{x+\varepsilon}{x}\right)^k
\left(\frac{y+\varepsilon}{y}\right)^\ell\mu^{-t}
\ge(1+\varepsilon)^{n+\ell}.
\tag{5.8}
$$

### The big-blue branch

Put

$$
b=\left\lceil
\frac{2r\log n-r\log\varepsilon+\log2}{\log(1+\varepsilon)}
\right\rceil,\qquad
m=\lceil5\mu^{-1}b^2\rceil,\qquad w=R(k,m).
\tag{5.9}
$$

Here $m=O_{r,\varepsilon}(\log^2n)$, $m\ge b$, and
$w=R(k,m)\le\binom{k+m-2}{m-1}\le(k+m)^m
\le\exp(O_{r,\varepsilon}(\log^3n))$.  Since (5.8) is
exponential in $n+\ell$, increasing $L_0$ once makes, uniformly for every
$n$,

$$
|X|\ge5m^2,\qquad
w\le\frac{\varepsilon(p-\varepsilon)}{n^3}|X|.
\tag{5.10}
$$

Let

$$
W=\{v\in X:|N_B(v)\cap X|\ge(\mu+\varepsilon)|X|\}.
$$

If $|W|\ge w$, Lemma 3, with $\nu=\mu+\varepsilon$, produces a red
$K_k$ or a blue book with base $S$ of size $b$ and page
$T$ of size at least $(\mu+\varepsilon)^b|X|/2$.  If $b\ge t$, its base
already contains a blue $K_t$.  Suppose $b<t$.  From (5.7),
$d(T,Y)\ge p-\delta_n$, and hence

$$
d(T,Y)+\delta_{n-b}-p
\ge\delta_{n-1}-\delta_n\ge\frac\varepsilon{n^2}.
$$

Using (5.5), $d+\delta_n-p\le1$, and the definition of $b$ gives

$$
\begin{aligned}
&(d(T,Y)+\delta_{n-b}-p)^r|T||Y|\\
&\quad\ge
\frac12\left(\frac\varepsilon{n^2}\right)^r
(\mu+\varepsilon)^b|X||Y|\\
&\quad\ge
\frac12\left(\frac\varepsilon{n^2}\right)^r
\left(\frac{\mu+\varepsilon}{\mu}\right)^b
x^{-k}y^{-\ell}\mu^{-t+b}\\
&\quad\ge x^{-k}y^{-\ell}\mu^{-t+b}.
\end{aligned}
\tag{5.11}
$$

Induction applied to $(T,Y)$ with parameter $t-b$ finishes this branch:
a blue $K_{t-b}$ in $T$ joins the blue base $S$.

We may therefore assume

$$
|W|<w.
\tag{5.12}
$$

### The red-step/density-increment branch

Lemma 2 and (5.10)--(5.12) show that the contribution from $W$ is at most

$$
w|Y|\le\frac\varepsilon{n^3}e_R(X,Y).
$$

Consequently some $v\in X\setminus W$ satisfies

$$
d(X,N_R(v)\cap Y)
\ge d(X,Y)-\frac\varepsilon{n^3}.
\tag{5.13}
$$

Write

$$
X_R=N_R(v)\cap X,\quad X_B=N_B(v)\cap X,\quad
Y'=N_R(v)\cap Y,\quad p'=p-\delta_{n-1},
$$

and

$$
\alpha=d(X,Y')-p',\quad
\alpha_R=d(X_R,Y')-p',\quad
\alpha_B=d(X_B,Y')-p'.
$$

An empty $X_R$ or $X_B$ is assigned zero weighted contribution and its
induction branch is skipped; its corresponding $\alpha_R$ or $\alpha_B$ need
not be defined.  By (5.7), $|Y'|\ge(p-\varepsilon)|Y|$.
Also, (5.4) and (5.13) give

$$
\alpha\ge
\delta_{n-1}-\delta_n-\frac\varepsilon{n^3}
\ge\frac\varepsilon{n^2}>0.
\tag{5.14}
$$

Since all edges from $v$ to $Y'$ are red,

$$
\frac{\alpha_R}{\alpha}\frac{|X_R|}{|X|}
+\frac{\alpha_B}{\alpha}\frac{|X_B|}{|X|}
+\frac1{\alpha|X|}\ge1.
\tag{5.15}
$$

If $\alpha_R\ge0$ and

$$
\alpha_R^r|X_R|
\ge\frac{x\alpha^r|X|}{p-\varepsilon},
\tag{5.16}
$$

then, using $|Y'|\ge(p-\varepsilon)|Y|$, (5.13), and

$$
d(X,Y')-p'\ge d(X,Y)+\delta_n-p,
$$

condition (5.16) and (5.5) show that $(X_R,Y')$ satisfies the inductive
moment inequality for
$(k-1,\ell,t)$.  Its goodness implies that of $(X,Y)$ because $v$ is red
to $X_R\cup Y'$.  The analogous condition, including its necessary sign
hypothesis, is

$$
\alpha_B\ge0,
\qquad
\alpha_B^r|X_B|
\ge\frac{\mu\alpha^r|X|}{p-\varepsilon}
\tag{5.17}
$$

gives the inductive branch $(k,\ell,t-1)$, since $v$ is blue to $X_B$.

Assume both branches fail.  Set

$$
a=|X_R|/|X|,\qquad c=|X_B|/|X|,\qquad q=1-1/r.
$$

Using the strict failures of (5.16)--(5.17) in (5.15) gives

$$
x^{1/r}a^q+\mu^{1/r}c^q
+\frac{(p-\varepsilon)^{1/r}}{\alpha|X|}
>(p-\varepsilon)^{1/r}.
\tag{5.18}
$$

Now $a+c=1-|X|^{-1}<1$ and $c\le\mu+\varepsilon$.  The function

$$
f(z)=x^{1/r}(1-z)^q+\mu^{1/r}z^q
$$

is increasing on $0\le z\le\mu/(\mu+x)$.  The special smallness condition
in (5.2) is exactly

$$
\mu+\varepsilon\le\frac\mu{\mu+x}.
$$

Therefore

$$
x^{1/r}a^q+\mu^{1/r}c^q
\le f(c)\le f(\mu+\varepsilon)
\le x^{1/r}(1-\mu)^q+\mu+\varepsilon.
\tag{5.19}
$$

Equations (5.8) and (5.14), after one final uniform increase of $L_0$, give

$$
\frac{(p-\varepsilon)^{1/r}}{\alpha|X|}
\le\frac{n^2}{\varepsilon(1+\varepsilon)^{n+\ell}}
\le\varepsilon.
\tag{5.20}
$$

Substituting (5.19)--(5.20) into the strict inequality (5.18) yields

$$
x^{1/r}(1-\mu)^{1-1/r}+\mu+2\varepsilon
>(p-\varepsilon)^{1/r}.
$$

The positivity condition in (5.2) allows the rearrangement

$$
x>
\big((p-\varepsilon)^{1/r}-\mu-2\varepsilon\big)^r
(1-\mu)^{1-r}.
\tag{5.21}
$$

But $x=x_0+\varepsilon$ and $\mu=\mu_0+\varepsilon$, so (5.21) strictly
contradicts the final inequality of (5.2).  The induction, and hence
Theorem A, is complete. $\square$

## Proof of Corollary B

By openness choose $y_0>y$ with $(x,y_0)\in\mathcal R_*$.  Take a uniformly
random equitable bipartition of the $N$ vertices.  Each edge has the same
probability of crossing, so some partition $(X,Y)$ has cross-red density at
least the global red density $p$.

For all sufficiently large $\ell$,

$$
(y_0/y)^{\ell/2}\ge3.
$$

Thus (B.2) makes both equitable parts at least
$x^{-k/2}(\mu y_0)^{-\ell/2}$, and hence

$$
|X||Y|\ge x^{-k}y_0^{-\ell}\mu^{-\ell}.
$$

Apply Theorem A with $t=\ell$.  A red $K_k$ in $X\cup Y$, a blue
$K_\ell$ in $X$, or a blue $K_\ell$ in $Y$ gives the desired conclusion.
$\square$

## Source defects neutralized by this proof

The standalone proof explicitly repairs all of the following source-level
issues rather than silently importing them:

1. Lemma 10 does not require $p>\mu$.
2. The moment order $r$ is chosen before $\varepsilon$.
3. The northeast rate point is chosen in $\mathcal R_*$, and Lemma 1
   supplies the exact eventual bound used later.
4. The printed comparison for $y_0$ uses $x$ in place of $y$.
5. The case $b\ge t$ and empty $X_R,X_B$ are treated separately.
6. The normalized sizes satisfy $a+c<1$, not the dimensionally false
   printed inequality.
7. The concavity calculation supplies an upper bound in (5.19), and the
   strictness in (5.18) is preserved to obtain a genuine contradiction.

The only non-symbolic dependency left in the diagonal descent is the stated
semantics of the Arb interval implementation used to certify its numerical
inequalities.  A separate adversarial replay of this standalone proof is
still required before changing the public claim label.
