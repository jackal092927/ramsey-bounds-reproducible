# Optimized retained-spine proof package

Date: 2026-08-12  
Arithmetic: 384-bit Arb author certificate; 448-bit high-precision replay

## Claim

Interpret the following terminating decimals exactly:

$$
\eta=0.02863,\quad p=0.47136,\quad \delta=0.000074,
\quad \lambda_0=12000,\quad \tau=0.0001473.
$$

Let $C_*$ be the two-dimensional maximum in the already refereed retained-
spine transfer theorem, with these parameters and the frozen $P_6$ rate $U$.
Then

$$
\boxed{U(1)-0.000000714\le C_*\le U(1)-0.0000007.}
\tag{1}
$$

In particular, conditional on the same Yang--Mao v1 and frozen local $P_6$
trust boundary,

$$
\boxed{
R(k,k)\le
\left(3.780695781309\right)^{k+o(k)}.}
\tag{2}
$$

The lower inequality in (1) only brackets the maximum for this fixed
parameter tuple.  It is not a Ramsey lower bound.

## Status

`PROVABLE AS STATED` within the declared local computer-assisted trust
boundary.  This package does not establish a finite-$k$ threshold, external
peer review, formal verification, global optimality of the five book
parameters, or novelty/priority relative to unexamined work.

## Assumptions

1. The transfer theorem in `RETAINED_SPINE_TRANSFER_ATTEMPT.md` and its
   resolved referee report are valid for every fixed tuple satisfying the
   displayed Yang--Mao parameter gates.
2. The exact frozen $P_6$ coefficient tuple in
   `certificate-higher-order-tetradecic-chain-v6.json` supplies the uniform
   off-diagonal rate $U$.
3. Arb containment in `python-flint==0.9.0` has its documented semantics.

All upstream artifacts are checked by SHA-256 before either numerical replay.

## Notation

Write $x=\sigma_R$, $y=\sigma_B$, and by symmetry restrict first to
$0\le x\le y\le1$.  Put

$$
c=\log\frac2{1+\eta},\qquad
A=U(1)-2c,\qquad E=U'(1)-c,
$$

and let $D,P_R,P_B,Q,B$ have exactly the meanings in the transfer theorem,
so $B=\max\{P_R,P_B,Q\}$ and
$C_*=\max\min\{D,B\}$.

Set the certified upper gap

$$
\Delta=7\cdot10^{-7},\qquad
G(x,y)=xA+(y-x)E.
$$

The checker verifies all book constants $\Pi,\Xi,q$ directly from the exact
parameter tuple rather than importing their old values.

## Proof strategy and dependency map

1. Verify every Yang--Mao scalar gate and re-prove $U''<0$ on $(0,1]$.
2. If $G(x,y)\ge\Delta$, use the direct branch.
3. The remaining weighted wedge $G(x,y)\le\Delta$ has a linear upper edge.
   Prove derivative signs that reduce $P_R,P_B,Q$ to explicit endpoints.
4. Apply symmetry for $y\le x$ and combine the branch bounds.
5. Evaluate one exact rational axis point to obtain the lower bracket.

## Proof

### Step 1: scalar gates and concavity

The 384-bit checker verifies

$$
0<p<\frac12-\eta,\quad
0<\delta\le\min\{p/4,1/4\},
$$

$$
\lambda_0\ge\max\{2,6\log(1/\delta)\},
\qquad 0<\tau<1,
$$

and reconstructs the Yang--Mao constants with
$\beta=1/48$, $C=8\log432$, and $\rho=\log96$.  It independently proves
$U''<0$ on $(0,1]$ using an analytic pole bound near zero followed by 16,384
closed Arb cells.  It obtains

$$
A=0.00007004028183732921899\ldots>0,
$$

$$
E=0.10092000828440347875\ldots>A.
\tag{3}
$$

### Step 2: exact domain cover

Concavity gives the refereed direct-branch estimate

$$
U(1)-D(x,y)\ge G(x,y)=xA+(y-x)E.
\tag{4}
$$

Thus $G\ge\Delta$ implies $D\le U(1)-\Delta$.

It remains to cover the closed wedge

$$
\mathcal W=\{0\le x\le y:\ xA+(y-x)E\le\Delta\}.
$$

Define

$$
r_d=\frac\Delta A=0.0099942487613880\ldots,
\qquad
r_a=\frac\Delta E=0.0000069361865094910\ldots.
\tag{5}
$$

Then $0\le x\le r_d$, $0\le y-x\le r_a<\tau$, and the upper edge is

$$
y=h(x)=r_a+x\left(1-\frac AE\right).
\tag{6}
$$

These inequalities cover all endpoints: the origin, both edge endpoints,
and the line $G=\Delta$.  No division by a vanishing homogeneous coordinate
is used inside $\mathcal W$, since $r_d<1$.

### Step 3: first page branch

Because $y-x<\tau$, the larger homogeneous coordinate is $1-y$ and

$$
P_R(x,y)=c(x+y)+\tau q+(1-y)U(z),
\qquad z=\frac{1-\tau-x}{1-y}.
$$

Across the complete wedge, monotonicity of this ratio gives

$$
1-\frac\tau{1-r_d}\le z\le\frac{1-\tau}{1-r_a}<1.
$$

Differentiation gives

$$
\partial_xP_R=c-U'(z),
\qquad
\partial_yP_R=c-U(z)+zU'(z).
$$

Arb proves on the entire displayed $z$ interval

$$
\partial_xP_R<-0.1009580419,
\qquad
\partial_yP_R>0.1008719865,
$$

and, along (6),

$$
\frac d{dx}P_R(x,h(x))
=\partial_xP_R+\left(1-\frac AE\right)\partial_yP_R
<-0.0000955985.
\tag{7}
$$

For fixed $x$, $P_R$ increases with $y$, so its wedge maximum lies on
$y=h(x)$.  Equation (7) moves that maximum to $(0,r_a)$.  Direct evaluation
there proves

$$
U(1)-\Delta-P_R(0,r_a)
>2.6716427596\cdot10^{-8}.
\tag{8}
$$

### Step 4: second page and reservoir branches

For $P_B$, put $w=(1-y-\tau)/(1-x)$.  Its $y$ derivative is
$c-U'(w)$.  Since $x\le y$, one has
$0<w\le1-\tau<z_+:=(1-\tau)/(1-r_a)$.  Strict concavity makes $U'$
decreasing, and Arb proves $c-U'(z_+)<0$.  Hence
$P_B(x,y)\le P_B(x,x)$.  On $0\le x\le r_d$, its diagonal derivative is

$$
2c-U\!\left(1-\frac\tau{1-x}\right)
-\frac\tau{1-x}U'\!\left(1-\frac\tau{1-x}\right)<0,
$$

with certified upper endpoint below $-0.0000672161$.  Thus its maximum is
at the origin, where

$$
U(1)-\Delta-P_B(0,0)
>7.2659130694\cdot10^{-7}.
\tag{9}
$$

The reservoir branch $Q=c(x+y)+2\tau\Xi$ is coordinatewise increasing.
The wedge lies in $[0,r_d]^2$, so the deliberately looser square-corner
bound gives

$$
U(1)-\Delta-Q(r_d,r_d)>0.0010713840814.
\tag{10}
$$

Equations (8)--(10) bound every constituent of $B$ by
$U(1)-\Delta$ on $\mathcal W$.  Equation (4) bounds $D$ on its complement.
Symmetry supplies the triangle $y\le x$.  Therefore

$$
C_*\le U(1)-7\cdot10^{-7}.
\tag{11}
$$

### Step 5: lower bracket for this variational maximum

At the exact point

$$
(x,y)=(0,0.000007069),
$$

the checker evaluates $D$ and $P_R$ directly and proves each is larger than
$U(1)-0.000000714$, by margins respectively

$$
5.8742850169\cdot10^{-10},\qquad
6.8454546509\cdot10^{-10}.
$$

Since $B\ge P_R$, this proves
$\min\{D,B\}>U(1)-0.000000714$, completing (1).

Finally, Arb gives

$$
\exp(U(1)-7\cdot10^{-7})
=3.78069578130815051236\ldots
<3.780695781309,
$$

and the retained-spine transfer theorem gives (2). $\square$

## Machine reproduction

From the repository root:

```text
routes/upper/.venv/bin/python routes/upper/check_retained_spine_optimized.py
routes/upper/.venv/bin/python routes/upper/independent_check_retained_spine_optimized.py
```

The high-precision replay uses 448-bit precision, an analytic split at
$1/32768$, and 32,768 subsequent concavity cells.  It separately recomputes
every proof-critical expression but shares the author's formulas and control
flow; it is not an implementation-independent checker.

## Corrections or missing assumptions

- The old numerical certificate used a different, more conservative fixed
  parameter tuple.  It remains frozen and is not modified by this package.
- The transfer theorem's fixed-decimal presentation is instantiated here
  with a new exact tuple; its proof is parameter-generic once the source
  gates and scalar inequalities are checked.  The present scripts check all
  gates actually used in the transfer proof.

## Open risks

- Both scripts share Python, python-flint, the same mathematical reduction,
  and substantially the same control flow; the second is a high-precision
  replay, not an implementation-independent or formally verified checker.
- The five-dimensional parameter tuple is feasible and stronger, but no
  global parameter optimum is claimed.
- External specialist review and archival novelty checking remain open.
