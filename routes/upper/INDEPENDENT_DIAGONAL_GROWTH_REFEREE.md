# Independent adversarial referee: diagonal growth and retained spine

Date: 2026-08-12  
Runtime checked: `python-flint==0.9.0`, 512-bit Arb

## Claim under review

Put

$$
u_0=\frac{619}{250},\qquad L=u_0^3,\qquad a=e^{-u_0},
$$

$$
E(z)=\sum_{n\geq0}\frac{z^n}{(3n)!},\qquad
H(z)=1+aE(z)^2,\qquad
G(z)=\frac{H(z)-H(-z)}2,
$$

and

$$
F(x,y)=G(x)H(y)+G(y)H(x).
$$

The frozen candidate claims the parameterized correlation property

$$
\mathcal G_2^{(3)}\!\left(
\frac{3253}{5000},
4\frac{619}{250}\left(1+\frac{93}{125000}\right)
\right),
\tag{R1}
$$

where the second parameter is exactly

$$
C=\frac{77432567}{7812500}=9.911368576.
$$

Combined with the frozen degree-14 rate and retained-spine transfer, the
candidate then claims

$$
R(k,k)
\leq\exp\!\left((U(1)-0.000003469)k+o(k)\right)
\leq (3.780685320)^{k+o(k)}.
\tag{R2}
$$

## Verdict

**PASS.** The status is **PROVABLE AS STATED UNDER THE EXPLICIT PINNED
DEPENDENCIES**. I found no sign, boundary, strictness, interval-coverage,
max/min, or parameter-handoff gap. In particular:

1. the reduction from the complete two-dimensional good region to the
   nonnegative diagonal covers all three sign patterns and their boundaries;
2. the diagonal identity is the corrected identity
   $H(z)^2-H(z)H(-z)$, and the comparison with
   $H(z)^2-H(-z)^2$ has the required direction;
3. the compact interval, analytic half-line, exact expectation budget, full
   retained-spine wedge, and final decimal all have strict certified margins;
4. Yang--Mao's parameterized definition and book theorem explicitly permit
   every $0<\beta\leq1$, so the relatively large value
   $\beta=3253/5000$ is admissible.

This is a conditional asymptotic theorem. The verdict does not make it an
unconditional theorem, give a finite-$k$ threshold, prove global parameter
optimality, establish publication priority, or establish a current
world-best claim.

## Frozen identities

The four requested author/replay artifacts matched their frozen SHA-256
identities before and after the review:

```text
b6b7bfe049f138ae69e166502d932576924833f20daec8d63c4eac612d623916  DIAGONAL_GROWTH_SHARPENING_CANDIDATE.md
ff183fc15797504b7d17dab14e51ac6b49edaf46b1593794fde733e579880faa  check_diagonal_growth.py
c612e898b07c05b68c6fc54f6a8f8f684eba449676cd3bf90553360a9303ccf2  check_retained_spine_diagonal_growth.py
f134b943a778db159f8cd3a00706a9f4e00af052b3618372cd5793284ef94ec7  independent_check_diagonal_growth.py
```

The theorem-chain artifacts actually used by the non-importing replay also
matched:

```text
80b5ae4d663194623b4b6222181792d1bf71f5f73684133d84f936ed1807fefb  STRONG_SEPARATOR_GROWTH_SHARPENING.md
9ea998eeab45a839c0fd24428bf9ccc7e0123cfc1550aaacc45f9e64a1568ccd  check_strong_separator_growth.py
5aa5d6cb1ee1cc2d9f4d34b8564b6c57f78cfd7444a89abcfbb64542274e4aaa  RETAINED_SPINE_TRANSFER_ATTEMPT.md
6ba57fdbe13bf45255644ae94af5474b7a34afda3aefeda26415f3cc3f9b66db  INDEPENDENT_RETAINED_SPINE_REFEREE.md
8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8  certificate-higher-order-tetradecic-chain-v6.json
2f142a9371d29f07ffd68253c7dbb0981fe440f7f0b8284b4a81430f38395dbc  INDEPENDENT_PROOF_REPLAY.md
2881e8b1df310b449d0bffff5715b9176d9c191ba2a5d05bb376ab2843c58ccd  STAGE6_SEARCH.md
2bb40e6dc4f83203998adad57a0e922565bc8f6f07e1bdc810dd3ebfea481f5d  INDEPENDENT_STAGE6_REFEREE.md
e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe  verify_region_direct_arb.py
b10815b10cb3ab922aa079ee74289c52239ec90939ed41b93907bf06a60ee274  check_retained_spine_transfer.py
```

I downloaded the Yang--Mao v1 TeX source again from
`https://export.arxiv.org/e-print/2608.01962v1`. Its `main.tex` identity was

```text
155b7104ec5b6935a576ae9f2b161976a966b0b46bd2b69153c0934ca688da2a  main.tex
```

which is the source identity used by the prior local audits.

## Dependency map

The reviewed implication has the following exact boundary.

1. The new two-variable growth estimate depends on coefficient signs of the
   explicit entire functions, the elementary two-to-one dimensional
   reduction proved below, a compact Arb enclosure, and an elementary
   half-line envelope.
2. The bad-event estimate depends on the previously derived ratio
   $H(s)/H(-s)>1001/500$ for $s\geq L$. The non-importing replay independently
   rechecks its endpoint, finite interval, and analytic tail.
3. The passage from the pointwise estimates to (R1) imports only the
   positive tensor-moment lemma and parameterized tail-integration interface
   from the pinned Yang--Mao v1 source.
4. The passage from (R1) to (R2) imports Yang--Mao's preliminary-spine
   regularization, parameterized book theorem, and spine compatibility, plus
   the frozen local off-diagonal $P_6$ rate and the already reviewed
   retained-spine max/min transfer.
5. The numerical proof assumes Arb outward-rounded containment semantics in
   `python-flint==0.9.0`.

The present report proves the new links and audits their handoffs. It does not
silently reclassify any imported source theorem as proved from first
principles here.

## 1. Coefficient signs and positive-axis monotonicity

Write

$$
e_n=\frac1{(3n)!},\qquad
b_n=\sum_{j=0}^n e_je_{n-j}.
$$

Every $e_n$ and $b_n$ is positive, and

$$
E(z)^2=\sum_{n\geq0}b_nz^n,
\qquad
H(z)=1+a\sum_{n\geq0}b_nz^n.
\tag{1}
$$

It follows term by term that $H$ is strictly increasing on $[0,\infty)$.
Moreover,

$$
G(z)=a\sum_{\substack{n\geq0\\n\text{ odd}}}b_nz^n.
\tag{2}
$$

Thus $G$ is odd, $G(z)>0$ for $z>0$, and $G$ is strictly increasing on
$[0,\infty)$. In particular, for $z\geq0$,

$$
H(z)-H(-z)=2G(z)\geq0.
\tag{3}
$$

Both products in

$$
F(x,y)=G(x)H(y)+G(y)H(x)
$$

also have nonnegative bivariate Taylor coefficients. This is exactly the
coefficient property required when the positive tensor moments are applied;
no alternating coefficient has been introduced by the sharpening.

## 2. Complete two-dimensional reduction

Let $x,y\geq-L$ and, by symmetry, suppose $x\leq y$. Define

$$
m=\max\{x,y,0\}.
$$

The target reduction is

$$
F(x,y)\leq F(m,m).
\tag{4}
$$

All sign patterns are as follows.

### Case 1: $x\leq y<0$

Equations (1)--(2) give $G(x),G(y)<0$ and $H(x),H(y)>0$. Hence

$$
F(x,y)<0=F(0,0)=F(m,m).
\tag{5}
$$

There is no missing two-negative-coordinate exception.

### Case 2: $x<0\leq y$

Write $x=-v^3$ with $0<v\leq u_0$. The cubic root filter gives

$$
E(-v^3)=\frac{e^{-v}+2e^{v/2}\cos(\sqrt3v/2)}3.
$$

Therefore

$$
|E(-v^3)|
\leq\frac{e^{-v}+2e^{v/2}}3
\leq e^{v/2},
$$

and, since $a=e^{-u_0}$,

$$
H(x)=1+aE(-v^3)^2\leq1+e^{v-u_0}\leq2.
\tag{6}
$$

The first summand in $F(x,y)$ is nonpositive. Using (6), $G(y)\geq0$,
and $H(y)\geq1$ gives

$$
F(x,y)
\leq G(y)H(x)
\leq2G(y)
\leq2G(y)H(y)
=F(y,y)=F(m,m).
\tag{7}
$$

The endpoint $x=-L$ is included in (6). The boundary $y=0$ is included in
(7), with $G(0)=0$.

### Case 3: $0\leq x\leq y$

Positive-axis monotonicity of both $G$ and $H$ gives

$$
F(x,y)
\leq G(y)H(y)+G(y)H(y)
=F(y,y)=F(m,m).
\tag{8}
$$

This includes $x=0$ and $x=y$. Equations (5), (7), and (8) prove (4) on
the full closed region $[-L,\infty)^2$.

For the candidate variables $x=LA_1$, $y=LA_2$, if
$M=\max(A_1,A_2)<0$, (5) already gives $F(x,y)<0$. If $M\geq0$, put

$$
u=u_0M^{1/3},\qquad z=LM=u^3.
$$

Then

$$
(u^3+u_0^3)^{1/3}=u_0(M+1)^{1/3}.
\tag{9}
$$

Thus (4) reduces the entire good event, not merely a sampled subset, to the
one-dimensional nonnegative diagonal.

## 3. Correct diagonal identity and square-difference comparison

For every $z\geq0$, direct substitution, without an approximation, gives

$$
\begin{aligned}
F(z,z)
&=2G(z)H(z)\\
&=(H(z)-H(-z))H(z)\\
&=H(z)^2-H(z)H(-z).
\end{aligned}
\tag{10}
$$

It is not $H(z)^2-H(-z)^2$. However, (3) and $H(-z)>0$ imply

$$
H(z)H(-z)\geq H(-z)^2.
$$

Consequently,

$$
F(z,z)
\leq H(z)^2-H(-z)^2.
\tag{11}
$$

The inequality direction is the one needed for an upper envelope. At $z=0$
both sides are zero; for $z>0$ the comparison is strict.

## 4. Independent compact and half-line verification

For $u\geq0$, set

$$
P(u)=E(u^3)
=\frac{e^u+2e^{-u/2}\cos(\sqrt3u/2)}3,
$$

$$
N(u)=E(-u^3)
=\frac{e^{-u}+2e^{u/2}\cos(\sqrt3u/2)}3.
\tag{12}
$$

The numerical statement required after (11) is

$$
\frac{(1+aP(u)^2)^2-(1+aN(u)^2)^2}
{\exp(4(u^3+u_0^3)^{1/3})}<10^{-4}
\qquad(u\geq0).
\tag{13}
$$

### Compact interval

The author checker covers $[0,20]$ with 65,536 exact rational cells at
512-bit precision and obtains a least certified lower endpoint for the slack
of

$$
1.69273769438204\ldots\times10^{-5}.
$$

The frozen non-importing checker reconstructs (12), uses 131,072 cells, and
obtains

$$
1.69780056717526\ldots\times10^{-5}.
$$

I also performed a separate scratch replay that did not call either checker:
it began with the single interval $[0,20]$, bisected only unresolved dyadic
cells, constructed the cube-root range from monotone endpoint values, and
recomputed (12) at 512 bits. It resolved the complete interval with 315 leaf
cells, maximum depth 9. Its least interval lower bound was

$$
2.13641268464925\ldots\times10^{-7}>0.
$$

The smaller number is dependency inflation from deliberately coarse adaptive
cells, not a different target; its strict positivity gives a third complete
coverage check.

### Analytic half-line

For $u\geq20$, put $q=e^{-3u/2}$. Equation (12) gives

$$
|P(u)|\leq\frac{e^u}{3}(1+2q).
\tag{14}
$$

Also $H(-u^3)^2\geq1$ and
$w=(u^3+u_0^3)^{1/3}\geq u$. Expanding $H(u^3)^2-1$ and applying (14)
therefore gives

$$
\frac{H(u^3)^2-H(-u^3)^2}{e^{4w}}
\leq T_1(u)+T_2(u),
\tag{15}
$$

where

$$
T_1(u)=\frac{2a}{9}e^{-2u}(1+2q)^2,
\qquad
T_2(u)=\frac{a^2}{81}(1+2q)^4.
$$

Their logarithmic derivatives are

$$
\frac{T_1'(u)}{T_1(u)}
=-2-\frac{6q}{1+2q}<0,
\qquad
\frac{T_2'(u)}{T_2(u)}
=-\frac{12q}{1+2q}<0.
\tag{16}
$$

Thus the complete half-line is bounded at $u=20$, with no eventual
monotonicity assumption left unchecked. Independent 512-bit evaluation gives

$$
T_1(20)<7.93770716261259\times10^{-20},
$$

$$
T_2(20)<8.727476874786841\times10^{-5},
$$

and hence

$$
T_1(20)+T_2(20)
<8.727476874786849\times10^{-5}.
$$

The half-line slack is therefore greater than

$$
1.272523125213151\times10^{-5}.
$$

Equations (4), (9), (11), (13), and (15) prove the claimed good-event
estimate, with the strict constant $D=10^{-4}$.

## 5. Bad-event separator and exact expectation budget

The imported ratio statement is

$$
\frac{H(s)}{H(-s)}>\frac{1001}{500}
\qquad(s\geq L).
\tag{17}
$$

The non-importing checker independently reconstructs its root filters and
obtains the following strict gates:

```text
ratio endpoint slack over 1001/500:       0.0002005988217396235...
finite derivative-numerator lower bound:  10.447265302158649...
analytic-tail cross-multiplied slack:      0.5492003812612323...
```

For completeness, if $s\geq L$, write

$$
A=H(-s),\qquad R=\frac{H(s)}{H(-s)}.
$$

For every real $y$, exact algebra gives

$$
F(-s,y)=\frac A2\bigl((2-R)H(y)-H(-y)\bigr).
\tag{18}
$$

Since $R>2+1/500$ and $A,H(y),H(-y)\geq1$,

$$
F(-s,y)<-\frac{501}{1000}.
\tag{19}
$$

Equation (18) places no restriction on $y$, so (19) includes the case in
which both coordinates are bad. Symmetry handles which coordinate is below
$-L$.

The pointwise constants passed to the moment/tail argument are exactly

$$
\sigma=\frac{501}{1000},\qquad
D=\frac1{10000},\qquad
\beta=\frac{3253}{5000},\qquad
\varepsilon=\frac{93}{125000},
$$

$$
c=4u_0,\qquad C=(1+\varepsilon)c.
\tag{20}
$$

If $\mathcal G_2^{(3)}(\beta,C)$ failed, failure at threshold $-1$ would
give $\mathbb P(\mathcal E)<\beta$. Coefficient positivity and tensor-moment
positivity, together with the strict pointwise bounds, would give

$$
D\,\mathbb E[e^{cY}\mathbf1_{\mathcal E}]
>\sigma(1-\beta).
\tag{21}
$$

The two-coordinate union bound and tail integration give

$$
\mathbb E[e^{cY}\mathbf1_{\mathcal E}]
<\beta\left(1+\frac2\varepsilon\right).
\tag{22}
$$

The two exact rational sides are

$$
D\beta\left(1+\frac2\varepsilon\right)
=\frac{813552529}{4650000000},
$$

$$
\sigma(1-\beta)=\frac{875247}{5000000}.
$$

Their exact difference is

$$
\frac{427181}{4650000000}
=0.0000918668817204301\ldots>10^{-5}.
\tag{23}
$$

Thus (21)--(22) contradict (23), proving (R1).

I separately checked the potentially nonstandard large-$\beta$ handoff in
the primary source. Yang--Mao v1 defines
$\mathcal G_r^{(d)}(\beta,C)$ for arbitrary $0<\beta\leq1$, and its
parameterized book theorem repeats exactly that range. Therefore
$\beta=0.6506$ is legal. The proof does not import the much smaller printed
choice $\beta_r$ from their general correlation theorem.

## 6. Complete retained-spine wedge

The outer replay reconstructs

$$
U(z)=(1+z)\log(1+z)-z\log z+P_6(z)e^{-z}
\tag{24}
$$

from all fourteen frozen decimal coefficients, interpreted as exact
rationals. The exact retained-spine tuple is

$$
\eta=0.0286892,\quad p=0.4713079,\quad
\delta=0.00005393,
$$

$$
\lambda_0=13236,\quad \tau=0.00069255,
\quad\Delta=0.000003469.
\tag{25}
$$

Put

$$
c_\eta=\log\frac2{1+\eta},
$$

$$
q=\log(1/p)+\frac{3\delta}{p}
+\frac{6\log(1/\delta)\log(1/p)}{\lambda_0},
$$

$$
\rho=\log(2/\beta),
$$

$$
\Xi=2\rho+4C\lambda_0^{1/3}
+\frac{12C\log(1/\delta)}{\lambda_0^{2/3}}.
\tag{26}
$$

Independent high-precision reconstruction gives

$$
\begin{aligned}
U(1)&=1.3299087618219930723187812632\ldots,\\
U'(1)&=0.7658393690544813503003599036\ldots,\\
c_\eta&=0.6648618101478736559224509346\ldots,\\
q&=0.7559382393657864516208300868\ldots,\\
\rho&=1.1230074455028312804909893328\ldots,\\
\Xi&=942.1399815018999028741442299\ldots.
\end{aligned}
\tag{27}
$$

All source scalar gates are strict. In particular,

$$
\tau\left(\frac12-\eta-p\right)
=2.008395\times10^{-9}>10^{-9}.
\tag{28}
$$

### Concavity and direct complement

Differentiation of (24) gives

$$
U''(z)=-\frac1{z(1+z)}
+\bigl(P_6''(z)-2P_6'(z)+P_6(z)\bigr)e^{-z}.
\tag{29}
$$

The independent checker treats the pole interval near zero analytically and
then covers the remainder of $(0,1]$ with 65,536 cells. Its worst certified
upper endpoint is below

$$
-0.3602795262399473<0.
$$

Thus $U$ is strictly concave on the complete interval.

Set

$$
A=U(1)-2c_\eta
=0.00018514152624576047\ldots,
$$

$$
E=U'(1)-c_\eta
=0.10097755890660769437\ldots,
\qquad 0<A<E.
\tag{30}
$$

In the ordered half-square $0\leq x\leq y$, concavity gives the direct-branch
gain

$$
U(1)-D(x,y)\geq xA+(y-x)E.
\tag{31}
$$

Consequently the direct branch controls every point outside the closed wedge

$$
\mathcal W={0\leq x\leq y: xA+(y-x)E\leq\Delta\}.
\tag{32}
$$

Its intercepts and boundary slope are

$$
r_{\rm axis}=\frac\Delta E
=0.00003435416777314269\ldots,
$$

$$
r_{\rm diag}=\frac\Delta A
=0.01873701740686301636\ldots,
$$

$$
s=1-\frac AE=0.99816650819993584415\ldots.
\tag{33}
$$

The strict ordering

$$
0<r_{\rm axis}<\tau<r_{\rm diag}<1
\tag{34}
$$

shows that $\mathcal W$ is exactly the triangle with vertices
$(0,0)$, $(0,r_{\rm axis})$, and
$(r_{\rm diag},r_{\rm diag})$. The symmetric half-square supplies its
mirror. No rectangle, sampled subset, or open boundary is substituted for
the complete exceptional set.

### Red page

On $\mathcal W$, the red-page rate is

$$
P_R(x,y)=c_\eta(x+y)+\tau q
+(1-y)U\!\left(\frac{1-\tau-x}{1-y}\right).
\tag{35}
$$

Writing $z=(1-\tau-x)/(1-y)$, the complete $z$ range is contained in

$$
z_{\min}=1-\frac\tau{1-r_{\rm diag}}
=0.99929422589837249228\ldots,
$$

$$
z_{\max}=\frac{1-\tau}{1-r_{\rm axis}}
=0.99934178155522625955\ldots.
\tag{36}
$$

The coordinate derivatives are

$$
\partial_xP_R=c_\eta-U'(z),
$$

$$
\partial_yP_R=c_\eta-U(z)+zU'(z).
\tag{37}
$$

Concavity makes the first expression increasing in $z$ and the second
decreasing in $z$. At $z=z_{\max}$ their independently recomputed values are

$$
-0.1012156449406722\ldots<0,
\qquad
0.1010304250447415\ldots>0.
$$

Thus a maximum lies on the sloping upper boundary
$y=r_{\rm axis}+sx$. Along this boundary the derivative is

$$
B(z)=c_\eta-U'(z)
+s\bigl(c_\eta-U(z)+zU'(z)\bigr).
$$

Its derivative is

$$
B'(z)=(sz-1)U''(z)>0,
\tag{38}
$$

because $sz<1$ and $U''(z)<0$. Hence $B(z)\leq B(z_{\max})$, and the
independent enclosure gives

$$
B(z_{\max})
<-0.0003704583518071982.
$$

The red-page maximum is therefore the axis vertex
$(0,r_{\rm axis})$, including all boundaries of the wedge. Its certified
margin is

$$
U(1)-\Delta-P_R(0,r_{\rm axis})
>3.7279917102833308\times10^{-9}>10^{-9}.
\tag{39}
$$

### Blue page

The blue-page rate is

$$
P_B(x,y)=c_\eta(x+y)+\tau q
+(1-x)U\!\left(\frac{1-y-\tau}{1-x}\right).
\tag{40}
$$

Its $y$ derivative is negative throughout the wedge, so its maximum first
moves to $y=x$. On that diagonal, with
$z=1-\tau/(1-x)$, the derivative is

$$
D_B(z)=2c_\eta-U(z)-(1-z)U'(z).
\tag{41}
$$

Since

$$
D_B'(z)=-(1-z)U''(z)>0
$$

and $z$ decreases as $x$ increases, the diagonal derivative is maximized at
$x=0$. The independent endpoint values are

$$
\partial_yP_B(0,0)
<-0.1012280697928693,
$$

$$
D_B(1-\tau)<-0.0001852282874817042.
$$

Thus the blue-page maximum is $(0,0)$, and

$$
U(1)-\Delta-P_B(0,0)
>3.4747574442423597\times10^{-6}.
\tag{42}
$$

### Reservoir and final base

The reservoir rate is coordinatewise increasing. On the sloping boundary,
$x+y=r_{\rm axis}+(1+s)x$ is increasing, so the maximum is the diagonal
vertex. Its margin is

$$
U(1)-\Delta-2c_\eta r_{\rm diag}-2\tau\Xi
>3.2149823913191351\times10^{-5}.
\tag{43}
$$

Equations (31)--(43) cover the complete ordered wedge, and symmetry covers
the other order. They also cover both possible book colors and the direct
branch, so the max/min direction from the retained-spine transfer is not
reversed.

Finally, outward-rounded 512-bit evaluation gives

$$
\exp(U(1)-\Delta)
<3.7806853125760260364105032741\ldots
<3.780685320.
\tag{44}
$$

The safe-decimal rounding margin is

$$
7.4239739635894967\times10^{-9}>10^{-9},
$$

and the exact improvement over the preceding safe decimal
$3.780685405$ is

$$
3.780685405-3.780685320=8.5\times10^{-8}
\geq5\times10^{-8}.
\tag{45}
$$

This proves (R2) under the dependency boundary stated above.

## Replay summary

All three frozen commands returned `PASS`:

```text
.venv/bin/python routes/upper/check_diagonal_growth.py
.venv/bin/python routes/upper/check_retained_spine_diagonal_growth.py
.venv/bin/python routes/upper/independent_check_diagonal_growth.py
```

The non-importing replay imports no author checker, reconstructs the root
filters, exact rational budget, degree-14 rate and derivatives, global
concavity, complete wedge, and final exponential at 512 bits. The symbolic
review and separate adaptive compact calculation above are additional to,
not substitutes for, that replay.

## Open risks and non-claims

- The result is asymptotic; no explicit sufficiently-large-$k$ threshold is
  extracted.
- The theorem remains conditional on the pinned Yang--Mao v1 interfaces and
  frozen local $P_6$/BookCor theorem chain.
- Arb is a rigorous interval library, but this is not a proof-assistant
  formalization.
- The smallest critical outer margin is the red-page margin
  $3.72799\times10^{-9}$; it exceeds the pre-registered $10^{-9}$ gate but
  makes exact file and environment pinning important.
- No global optimality, novelty, priority, finite-Ramsey-number, or
  world-record claim is supported by this review.

Subject to these explicit boundaries, the frozen package supports the safe
base **3.780685320**.
