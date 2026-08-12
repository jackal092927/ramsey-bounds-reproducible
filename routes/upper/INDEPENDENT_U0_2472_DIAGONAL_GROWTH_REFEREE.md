# Independent adversarial referee: the `u0=309/125` diagonal-growth package

Date: 2026-08-12  
Reviewed runtime: `python-flint==0.9.0`, 512-bit Arb

## Verdict

**PASS.** The frozen package supports, under the explicit pinned dependencies,

$$
\mathcal G_2^{(3)}\!\left(
\frac{833}{1250},\frac{3092197917}{312500000}
\right)
\tag{R1}
$$

and the conditional local computer-assisted asymptotic bound

$$
R(k,k)\leq(3.780685300)^{k+o(k)}.
\tag{R2}
$$

The proof status is **PROVABLE AS STATED UNDER THE EXPLICIT PINNED
DEPENDENCIES**. I found no ratio-target, separator, sign-case, compact-tail,
asymptotic, rational-budget, parameter-handoff, retained-spine-wedge, or
rounding gap. The narrowest promotion margin is the final decimal-rounding
margin, approximately $1.41251\times10^{-9}$, which strictly exceeds the
pre-registered $10^{-9}$ gate.

This verdict is conditional and asymptotic. It establishes neither a
finite-$k$ threshold nor an unconditional theorem, global optimum,
publication priority, finite Ramsey number, or world-best claim.

## Frozen identities

The requested candidate and three checker identities are

```text
5900745028807c817fdb92dd0f6caf9df435df5106bfe2fd4309d8afe173a738  U0_2472_DIAGONAL_GROWTH_CANDIDATE.md
f10e9f43e6666e11e916fe4d9998fe3e9ff7fd4b9b42750e48b5fdd5c1d1f5d9  check_u0_2472_diagonal_growth.py
a04f44b931f27225ad7d75caa013d72176a185e94fb08aacb17643e2083fe682  check_retained_spine_u0_2472.py
67dbca5a88bdf942a8be4a2069488150f3e1ed85ff0e3931b01ec5ab41c69fe1  independent_check_u0_2472_diagonal_growth.py
```

All four matched before and after the review. The non-importing replay pins
the following immediate theorem-chain artifacts, which also matched:

```text
8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8  certificate-higher-order-tetradecic-chain-v6.json
5aa5d6cb1ee1cc2d9f4d34b8564b6c57f78cfd7444a89abcfbb64542274e4aaa  RETAINED_SPINE_TRANSFER_ATTEMPT.md
6ba57fdbe13bf45255644ae94af5474b7a34afda3aefeda26415f3cc3f9b66db  INDEPENDENT_RETAINED_SPINE_REFEREE.md
b10815b10cb3ab922aa079ee74289c52239ec90939ed41b93907bf06a60ee274  check_retained_spine_transfer.py
e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe  verify_region_direct_arb.py
4b29c692dd1fc96859491b25d61c9b0e1124a33cf57a45ef01abb5a2e49ed30d  HYBRID_CORRELATION_SHARPENING.md
80b5ae4d663194623b4b6222181792d1bf71f5f73684133d84f936ed1807fefb  STRONG_SEPARATOR_GROWTH_SHARPENING.md
```

For a source-boundary cross-check, I again used the Yang--Mao v1 TeX source
with identity

```text
155b7104ec5b6935a576ae9f2b161976a966b0b46bd2b69153c0934ca688da2a  main.tex
```

It defines $\mathcal G_r^{(d)}(\beta,C)$ and states the parameterized book
theorem for arbitrary $0<\beta\leq1$ and $C>0$. Thus the present
$\beta=833/1250$ lies inside the source theorem's domain.

## Exact claim and dependency boundary

The new inner constants are

$$
u_0=\frac{309}{125},\qquad L=u_0^3,\qquad a=e^{-u_0},
$$

$$
E(z)=\sum_{n\geq0}\frac{z^n}{(3n)!},\qquad
H(z)=1+aE(z)^2,
$$

$$
G(z)=\frac{H(z)-H(-z)}2,
\qquad
F(x,y)=G(x)H(y)+G(y)H(x).
\tag{1}
$$

The proof imports the following and no stronger interfaces.

1. Yang--Mao v1 supplies the positive tensor-moment fact, the parameterized
   tail-integration interface, preliminary-spine regularization,
   parameterized book theorem, and spine-compatibility statement.
2. The frozen local chain supplies the degree-14 off-diagonal rate $U=F_6$,
   its uniform asymptotic Ramsey interface, repaired BookCor descent, and the
   already reviewed retained-spine max/min transfer.
3. Arb outward-rounded interval containment is trusted at the pinned
   `python-flint==0.9.0` runtime.

The present review independently checks the new $u_0$, pointwise lemmas,
exact budget, retained-spine parameter substitution, complete wedge, and
reported decimal. It does not silently re-prove or strengthen the imported
source theorems.

## 1. Exact ratio target and separator

Define

$$
\sigma_0=\frac1{10000},\qquad
T=\frac{10001}{5000},\qquad
\sigma_*=\frac{5001}{10000}.
\tag{2}
$$

Exact rational arithmetic gives

$$
T=2+2\sigma_0,
\qquad
\sigma_*=\frac{1+2\sigma_0}{2}.
\tag{3}
$$

These two constants play different roles. The ratio target is $T$, not
$1+2\sigma_0$. The extra constant $1$ entering $\sigma_*$ comes from the
$-H(-y)$ term in the exact two-variable separator identity below.

For $u\geq0$, the cubic root filters and derivatives are

$$
P(u)=E(u^3)
=\frac{e^u+2e^{-u/2}\cos(\sqrt3u/2)}3,
$$

$$
N(u)=E(-u^3)
=\frac{e^{-u}+2e^{u/2}\cos(\sqrt3u/2)}3,
\tag{4}
$$

$$
P'(u)=\frac{e^u-e^{-u/2}\cos(\sqrt3u/2)
-\sqrt3e^{-u/2}\sin(\sqrt3u/2)}3,
$$

$$
N'(u)=\frac{-e^{-u}+e^{u/2}\cos(\sqrt3u/2)
-\sqrt3e^{u/2}\sin(\sqrt3u/2)}3.
\tag{5}
$$

Put

$$
R(u)=\frac{1+aP(u)^2}{1+aN(u)^2}.
$$

The denominator is positive, and $R'(u)$ has the sign of

$$
W(u)=PP'(1+aN^2)-NN'(1+aP^2).
\tag{6}
$$

Independent 512-bit evaluation gives

$$
R(u_0)-T
>1.5259655314585074\times10^{-5}.
\tag{7}
$$

The author checker covers $[u_0,2.9]$ with 32,768 exact rational cells and
obtains $W>10.3611$. The frozen non-importing checker uses 131,072 cells and
obtains $W>10.3613$.

I additionally reconstructed (4)--(6) in a scratch 512-bit program that did
not import either checker. Starting with the whole interval, adaptive dyadic
bisection resolved $W>0$ with three leaf intervals, maximum depth two. The
least coarse-cell lower bound remained above $1.027$. Hence the finite
interval sign is not dependent on either fixed grid.

## 2. Ratio tail and bad-event separator

For $u\geq2.9$ use

$$
P(u)\geq\frac{e^u-2e^{-u/2}}3,
\qquad
|N(u)|\leq\frac{2e^{u/2}+e^{-u}}3.
\tag{8}
$$

Let

$$
B_T(u)=e^{2u}-4Te^u-4e^{u/2}-4Te^{-u/2}
+4e^{-u}-Te^{-2u},
$$

$$
K(u)=aB_T(u)-9(T-1).
\tag{9}
$$

Expanding squares shows that $K(u)>0$ is precisely the cross-multiplied
version of the ratio inequality obtained from (8). At $u=2.9$, the separate
reconstruction gives

$$
K(2.9)>5.02614765083963.
\tag{10}
$$

Define

$$
D_0(u)=2e^u(e^u-2T)-2e^{u/2}-4e^{-u}.
\tag{11}
$$

Direct differentiation of (9) gives $B_T'(u)\geq D_0(u)$. At the switch,

$$
D_0(2.9)>506.445095636894,
$$

$$
D_0'(2.9)
=4e^{5.8}-4Te^{2.9}-e^{1.45}+4e^{-2.9}
>1171.74751573181.
\tag{12}
$$

For completeness, the claimed persistence follows without assuming that a
positive endpoint derivative stays positive. Write

$$
D_0'(u)=4e^u(e^u-T)-e^{u/2}+4e^{-u}.
$$

For $u\geq2.9$, $e^u>T+1$, and therefore

$$
4e^u(e^u-T)>4e^u>e^{u/2}.
$$

Thus $D_0'(u)>0$ on the complete half-line. Consequently $D_0(u)>0$,
$B_T'(u)>0$, and $K(u)>0$ throughout $[2.9,\infty)$. The envelope ratio
slack at the switch is

$$
0.3303154378849961\ldots>0.
$$

Together with (7), this proves

$$
R(u)>\frac{10001}{5000}
\qquad(u\geq u_0).
\tag{13}
$$

Now let $t\geq L$, put $A=H(-t)$ and
$R_t=H(t)/H(-t)$, and take arbitrary real $y$. Exact substitution gives

$$
F(-t,y)=\frac A2\bigl((2-R_t)H(y)-H(-y)\bigr).
\tag{14}
$$

Since $A,H(y),H(-y)\geq1$ and $R_t>2+2\sigma_0$,

$$
F(-t,y)
<\frac A2\bigl(-2\sigma_0H(y)-H(-y)\bigr)
\leq-\frac{1+2\sigma_0}{2}
=-\frac{5001}{10000}.
\tag{15}
$$

This is strict because (13) is strict. Equation (14) has no restriction on
$y$, so it includes the case where both coordinates are bad. Symmetry handles
which coordinate lies below $-L$.

## 3. Complete two-dimensional-to-diagonal reduction

The Taylor coefficients of $E(z)^2$, and hence of $H(z)$, are positive.
The odd part

$$
G(z)=a\sum_{\substack{n\geq0\\n\text{ odd}}}b_nz^n,
\qquad b_n>0,
\tag{16}
$$

is odd, nonnegative, and increasing on $[0,\infty)$. The same coefficient
argument makes $H$ increasing on that half-line and gives
$H(z)\geq H(-z)>0$ for $z\geq0$.

For $x=-v^3\in[-L,0]$, $0\leq v\leq u_0$, equation (4) gives

$$
|E(-v^3)|\leq\frac{e^{-v}+2e^{v/2}}3\leq e^{v/2}.
$$

Since $a=e^{-u_0}$,

$$
H(x)\leq1+e^{v-u_0}\leq2.
\tag{17}
$$

Let $x,y\geq-L$, set $m=\max\{x,y,0\}$, and by symmetry assume $x\leq y$.
There are exactly three sign cases.

1. If $x\leq y<0$, then $G(x),G(y)<0$ and $H(x),H(y)>0$, so
   $F(x,y)<0=F(0,0)$.
2. If $x<0\leq y$, then
   $$
   F(x,y)\leq G(y)H(x)\leq2G(y)
   \leq2G(y)H(y)=F(y,y).
   $$
3. If $0\leq x\leq y$, positive-axis monotonicity bounds both summands by
   $G(y)H(y)$, hence $F(x,y)\leq F(y,y)$.

The same weak inequalities include $x=-L$, $x=0$, $y=0$, and $x=y$.
Therefore

$$
F(x,y)\leq F(m,m)
\qquad(x,y\geq-L).
\tag{18}
$$

On the nonnegative diagonal, the exact identity is

$$
F(z,z)=2G(z)H(z)=H(z)^2-H(z)H(-z).
\tag{19}
$$

It is not $H(z)^2-H(-z)^2$. However, $H(z)\geq H(-z)>0$ gives

$$
F(z,z)\leq H(z)^2-H(-z)^2.
\tag{20}
$$

The direction is the one required for an upper envelope.

If $A_1,A_2\geq-1$, $M=\max(A_1,A_2)$, and $M\geq0$, then with

$$
u=u_0M^{1/3},\qquad
w=(u^3+u_0^3)^{1/3}=u_0(M+1)^{1/3},
\tag{21}
$$

equations (18)--(20) reduce the full good region to the claimed
one-dimensional envelope. If $M<0$, the first sign case gives the stronger
bound $F<0$.

## 4. Growth prefactor on the compact interval and half-line

The numerical target is exactly

$$
D=\frac{89}{10^6}.
\tag{22}
$$

For $u\geq0$, define

$$
Q(u)=\frac{H(u^3)^2-H(-u^3)^2}
{\exp(4(u^3+u_0^3)^{1/3})}.
\tag{23}
$$

The author checker covers $[0,20]$ with 65,536 exact rational cells and
certifies $D-Q(u)>5.23965\times10^{-6}$. The non-importing checker uses
131,072 cells and obtains $D-Q(u)>5.29070\times10^{-6}$.

My separate 512-bit implementation began from the whole interval and
recursively bisected only unresolved dyadic cells. It independently
reconstructed the root filters and built the cube-root range from monotone
endpoint images. It covered $[0,20]$ with 695 leaf cells, maximum depth 11.
Even under the intentionally coarser dependency enclosures, its least lower
bound was

$$
D-Q(u)>3.78519\times10^{-9}>0.
\tag{24}
$$

For $u\geq20$, put $q=e^{-3u/2}$. The elementary root-filter bound and
$w\geq u$ give

$$
Q(u)\leq T_1(u)+T_2(u),
\tag{25}
$$

where

$$
T_1(u)=\frac{2a}{9}e^{-2u}(1+2q)^2,
\qquad
T_2(u)=\frac{a^2}{81}(1+2q)^4.
$$

Both are strictly decreasing because

$$
\frac{T_1'(u)}{T_1(u)}=-2-\frac{6q}{1+2q}<0,
\qquad
\frac{T_2'(u)}{T_2(u)}=-\frac{12q}{1+2q}<0.
\tag{26}
$$

Thus $u=20$ controls the complete tail. Independent 512-bit evaluation gives

$$
T_1(20)+T_2(20)
<8.797576715281706\times10^{-5},
$$

and therefore

$$
D-T_1(20)-T_2(20)
>1.024232847182941\times10^{-6}.
\tag{27}
$$

The limiting value is $a^2/81$, and its separate slack is

$$
D-\frac{a^2}{81}
>1.024232847248880\times10^{-6}.
\tag{28}
$$

Hence the compact certificate, tail monotonicity, and asymptotic constant are
mutually consistent. Equations (18)--(28) prove the good-event pointwise
bound with the exact prefactor (22).

## 5. Exact expectation-tail budget and correlation constant

The four exact parameters passed into the contradiction are

$$
D=\frac{89}{10^6},\qquad
\sigma_*=\frac{5001}{10000},
$$

$$
\beta=\frac{833}{1250},\qquad
\varepsilon=\frac{7113}{10^7}.
\tag{29}
$$

Under failure of $\mathcal G_2^{(3)}(\beta,C)$, the same positive-moment and
two-coordinate union-bound argument requires

$$
D\beta\left(1+\frac2\varepsilon\right)
<\sigma_*(1-\beta).
\tag{30}
$$

The exact left and right sides are

$$
D\beta\left(1+\frac2\varepsilon\right)
=\frac{1483267336481}{8891250000000},
$$

$$
\sigma_*(1-\beta)=\frac{2085417}{12500000}.
$$

Their exact difference is

$$
\frac{89775619}{8891250000000}
=1.0097075101926051\times10^{-5}>10^{-5}.
\tag{31}
$$

All pointwise and failure inequalities entering the contradiction are strict,
so threshold equality cannot erase the margin.

The correlation constant reconstructed independently in both inner and outer
calculations is exactly

$$
\begin{aligned}
C
&=4\frac{309}{125}left(1+\frac{7113}{10^7}\right)\\
&=\frac{3092197917}{312500000}\\
&=9.8950333344.
\end{aligned}
\tag{32}
$$

There is no decimal substitution or stale $u_0$ between (R1) and the outer
book parameters. Equations (15), (22)--(32), and the pinned source interface
prove (R1).

## 6. Independent retained-spine/P6 reconstruction

The outer tuple consists of exact terminating rationals:

$$
\eta=0.02868925,\quad p=0.47130784,
\quad\delta=0.000053934,
$$

$$
\lambda_0=13235,\quad\tau=0.00069374,
\quad\Delta=0.0000034727.
\tag{33}
$$

The rate is reconstructed from all fourteen frozen coefficients as

$$
U(z)=(1+z)\log(1+z)-z\log z+P_6(z)e^{-z}.
\tag{34}
$$

I independently rebuilt $U,U',U''$ without importing an author checker. A
512-bit adaptive proof treats the pole interval near zero analytically and
covers the rest of $(0,1]$ using 44 adaptive leaves, maximum depth eight.
Every enclosure satisfies $U''<0$; the deliberately coarse worst upper
endpoint is below $-0.0109$. The frozen non-importing fine-grid replay gives
the stronger worst upper endpoint $-0.3602795\ldots$. Both prove global
strict concavity.

Define

$$
c_\eta=\log\frac2{1+\eta},
$$

$$
q_p=\log(1/p)+\frac{3\delta}{p}
+\frac{6\log(1/\delta)\log(1/p)}{\lambda_0},
$$

$$
\rho=\log(2/\beta),
$$

$$
\Xi=2\rho+4C\lambda_0^{1/3}
+\frac{12C\log(1/\delta)}{\lambda_0^{2/3}}.
\tag{35}
$$

The independent enclosures give

$$
\rho=1.0990123686894494\ldots,
$$

$$
q_p=0.7559386206633876\ldots,
\qquad
\Xi=940.5194323347251\ldots.
\tag{36}
$$

All source-level scalar gates hold. The tight degree gate is exactly

$$
\tau(1/2-\eta-p)
=2.0187834\times10^{-9}>10^{-9}.
\tag{37}
$$

### Complete direct wedge

Put

$$
A=U(1)-2c_\eta
=0.0001852387373349502\ldots,
$$

$$
E=U'(1)-c_\eta
=0.1009776075121522892\ldots,
\qquad0<A<E.
\tag{38}
$$

In the ordered half-square $0\leq x\leq y$, concavity gives the direct gain

$$
U(1)-D_{\rm direct}(x,y)
\geq xA+(y-x)E.
\tag{39}
$$

It therefore suffices to control the complete closed wedge

$$
\mathcal W={0\leq x\leq y:\ xA+(y-x)E\leq\Delta\}.
\tag{40}
$$

Its intercepts and boundary slope are

$$
r_{\rm axis}=\frac\Delta E
=0.00003439079302390951\ldots,
$$

$$
r_{\rm diag}=\frac\Delta A
=0.0187471586664976839\ldots,
$$

$$
s=1-\frac AE\in(0,1).
\tag{41}
$$

The strict order

$$
0<r_{\rm axis}<\tau<r_{\rm diag}<1
\tag{42}
$$

identifies $\mathcal W$ exactly as the triangle with vertices
$(0,0)$, $(0,r_{\rm axis})$, and
$(r_{\rm diag},r_{\rm diag})$. Symmetry covers the opposite parameter order.
No part of the exceptional set is omitted.

### Red page

The red-page rate is

$$
P_R(x,y)=c_\eta(x+y)+\tau q_p
+(1-y)U\!\left(\frac{1-\tau-x}{1-y}\right).
\tag{43}
$$

Over the wedge, its $U$ argument lies in

$$
z_{\min}=1-\frac\tau{1-r_{\rm diag}}
=0.9992930058688469\ldots,
$$

$$
z_{\max}=\frac{1-\tau}{1-r_{\rm axis}}
=0.9993406281167019\ldots.
\tag{44}
$$

The coordinate derivatives are

$$
\partial_xP_R=c_\eta-U'(z)<0,
$$

$$
\partial_yP_R=c_\eta-U(z)+zU'(z)>0.
\tag{45}
$$

Concavity reduces both signs to endpoints. At $z_{\max}$ the independent
values are respectively below $-0.1012161$ and above $0.1010307$.
Consequently a maximum lies on the sloping boundary
$y=r_{\rm axis}+sx$.

Along that boundary the derivative is

$$
B(z)=c_\eta-U'(z)
+s\bigl(c_\eta-U(z)+zU'(z)\bigr).
$$

Since

$$
B'(z)=(sz-1)U''(z)>0,
\tag{46}
$$

its maximum occurs at $z_{\max}$. The independent 512-bit enclosure is

$$
B(z_{\max})
<-0.0003706536867499084.
$$

Thus the red-page maximum is the axis vertex $(0,r_{\rm axis})$, with

$$
U(1)-\Delta-P_R(0,r_{\rm axis})
>8.130784683526161\times10^{-9}>10^{-9}.
\tag{47}
$$

### Blue page and reservoir

The blue-page rate is

$$
P_B(x,y)=c_\eta(x+y)+\tau q_p
+(1-x)U\!\left(\frac{1-y-\tau}{1-x}\right).
\tag{48}
$$

Its $y$ derivative is negative throughout the wedge, reducing the maximum
to $y=x$. Along that diagonal, concavity makes the derivative attain its
maximum at the origin. The independent endpoint enclosures are

$$
\partial_yP_B(0,0)<-0.1012285,
$$

$$
\frac d{dx}P_B(x,x)\bigg|_{x=0}
<-0.0001853257970959558.
\tag{49}
$$

Therefore the blue-page maximum is $(0,0)$, and its margin is

$$
U(1)-\Delta-P_B(0,0)
>3.4828736313844327\times10^{-6}.
\tag{50}
$$

The reservoir rate is coordinatewise increasing. On the sloping boundary,
$x+y=r_{\rm axis}+(1+s)x$ is increasing, so the diagonal vertex maximizes
it. Its margin is

$$
U(1)-\Delta-2c_\eta r_{\rm diag}-2\tau\Xi
>2.4849276366241719\times10^{-5}.
\tag{51}
$$

Equations (39)--(51) cover the full ordered wedge, its symmetric copy, the
direct branch, both possible book colors, and the simultaneous reservoir
condition. The retained-spine max/min and inner maxima have the correct
directions.

### Base and promotion margins

Outward-rounded 512-bit evaluation gives

$$
\exp(U(1)-\Delta)
<3.7806852985874904057579978721\ldots
<3.780685300.
\tag{52}
$$

The decimal rounding margin is

$$
3.780685300-\exp(U(1)-\Delta)
>1.4125095942420021\times10^{-9}>10^{-9}.
\tag{53}
$$

The exact safe-decimal improvement over the previous reviewed value is

$$
3.780685320-3.780685300
=2\times10^{-8}\geq10^{-8}.
\tag{54}
$$

Thus every pre-registered inner and outer promotion gate passes, and the
conditional implication (R2) follows.

## Replay record

All three frozen commands returned `PASS`:

```text
.venv/bin/python routes/upper/check_u0_2472_diagonal_growth.py
.venv/bin/python routes/upper/check_retained_spine_u0_2472.py
.venv/bin/python routes/upper/independent_check_u0_2472_diagonal_growth.py
```

The third program imports no author checker. It independently reconstructs
the root filters, ratio, compact and tail growth estimates, exact rational
budget, rate and derivatives, global concavity, wedge endpoints, and final
exponential. The separate adaptive reconstructions described above use a
different interval decomposition and are additional checks rather than
copies of that replay.

## Remaining boundaries and risks

- The theorem is conditional on the pinned Yang--Mao v1 interfaces and the
  frozen local $P_6$/BookCor/retained-spine chain.
- The result is asymptotic and does not extract a finite-$k$ threshold.
- Arb supplies rigorous interval arithmetic, not proof-assistant
  formalization.
- The decimal-rounding margin is only about $1.41\times10^{-9}$, so the exact
  file hashes, runtime, and use of outward rounding are material.
- No global optimum, novelty, publication priority, finite Ramsey number, or
  world-best status follows from this review.

Within these explicit boundaries, the frozen package supports the safe base
**3.780685300**.
