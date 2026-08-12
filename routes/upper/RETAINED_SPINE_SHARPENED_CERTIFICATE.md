# Retained-spine certificate with a specialized correlation lemma

Date: 2026-08-12

## Claim

Conditional on the frozen local $P_6$ off-diagonal rate theorem, the repaired
BookCor interface, and the Yang--Mao combinatorial book construction with the
specialized correlation property proved in
`SPECIALIZED_CORRELATION_SHARPENING.md`,

$$
R(k,k)
\le \exp\!\left((U(1)-2.87\cdot10^{-6})k+o(k)\right)
\le (3.780687577208)^{k+o(k)}.
\tag{1}
$$

Here $U=F_6$ is the exact frozen degree-14 rate certified by the six-stage
Arb chain.  Its coefficients and all upstream hashes are unchanged.

## Status

**AUTHOR CHECKER PASS; pending independent referee replay.**

The 384-bit Arb checker covers the complete variational square and reports
strict positive margins.  The only new mathematical input relative to the
previous retained-spine certificate is the source-level property

$$
\mathcal G_2^{(3)}(0.000001,11.62088),
\tag{2}
$$

proved in the companion note.  Until (2) and this enclosure receive an
independent replay, (1) should be called a theorem-linked candidate rather
than promoted as the canonical result.

## Exact parameters

The retained-spine tuple is

$$
\eta=0.028681,\qquad
p=0.471309,\qquad
\delta=0.0000528,\qquad
\lambda_0=13520,\qquad
\tau=0.000572.
\tag{3}
$$

The correlation pair is the exact rational pair

$$
\beta=\frac{1}{1000000},
\qquad
C=\frac{145261}{12500}.
\tag{4}
$$

With

$$
\Pi=\frac{3\delta}{p}
 +\frac{6\log(1/\delta)\log(1/p)}{\lambda_0},
\quad q=\log(1/p)+\Pi,
\tag{5}
$$

and

$$
\rho=\log(2/\beta),
\quad
\Xi=2\rho+4C\lambda_0^{1/3}
 +\frac{12C\log(1/\delta)}{\lambda_0^{2/3}},
\tag{6}
$$

the checker obtains

$$
q=0.7558653742596826\ldots,
\qquad
\Xi=1138.8035215904428\ldots.
\tag{7}
$$

All Yang--Mao scalar gates are strict, including
$p<1/2-\eta$, $\delta\le p/4$,
$\lambda_0\ge6\log(1/\delta)$, and the positive minimum-degree slack.

## Complete-square enclosure

Let

$$
c_\eta=\log\frac2{1+\eta},
\qquad
A=U(1)-2c_\eta,
\qquad
E=U'(1)-c_\eta.
\tag{8}
$$

Strict concavity of $U$ gives the direct-branch tangent gain

$$
G(x,y)=\min(x,y)A+|x-y|E.
\tag{9}
$$

For $\Delta=2.87\cdot10^{-6}$, the region not already won by the direct
branch is $G(x,y)\le\Delta$.  By symmetry it is enough to take
$0\le x\le y$, where

$$
r_{\rm axis}=\frac\Delta E
=2.84244005467\ldots\cdot10^{-5},
\qquad
r_{\rm diag}=\frac\Delta A
=0.0169622908610\ldots.
\tag{10}
$$

The exact inequalities

$$
0<r_{\rm axis}<\tau<r_{\rm diag}<1
$$

hold.  On this weighted wedge, the analytic derivative signs from the
reviewed retained-spine reduction send the red-page branch to the axis
endpoint, the blue-page branch to the origin, and the reservoir branch to
the diagonal endpoint.  Thus no sampled two-dimensional grid is used.

The strict Arb lower margins are

| check | lower margin |
|---|---:|
| red-page endpoint | $2.33620592\cdot10^{-8}$ |
| blue-page/origin | $2.89428559\cdot10^{-6}$ |
| reservoir/diagonal | $4.55923388\cdot10^{-3}$ |
| final decimal rounding | $7.9347\cdot10^{-13}$ |

The proof-critical derivative enclosures are also strict:

$$
\partial_xP_R<-0.1011084,\qquad
\partial_yP_R>0.1008664,\qquad
\frac{d}{dx}P_R(x,h(x))<-1.3672\cdot10^{-4},
$$

and the blue diagonal derivative is below
$-1.5048\cdot10^{-4}$.

## Dependency boundary

The proof chain is:

1. the locally proved six-stage off-diagonal rate $U=F_6$;
2. the repaired BookCor and finite-net descent used by that rate;
3. Yang--Mao regularization and parameterized book lemmas;
4. the new specialized correlation proof (2);
5. the already refereed retained-spine max/min transfer;
6. the present complete-square Arb enclosure.

The earliest external mathematical dependency is the Yang--Mao
regularization/book construction.  The earliest numerical dependency is
`python-flint==0.9.0` and Arb containment semantics.

## Claim boundary

Equation (1) is asymptotic and conditional on the pinned proof chain.  It
does not establish a finite-$k$ threshold, optimality of the six parameters,
publication priority, or a globally best-known bound.  It is a strict local
improvement over the prior certified decimal `3.780695781309`, by
`0.000008204101` in the reported base.

## Reproduction

```text
.venv/bin/python routes/upper/check_specialized_correlation.py
.venv/bin/python routes/upper/check_retained_spine_sharpened.py
```

Both scripts require `python-flint==0.9.0`; the second pins all theorem and
source-lemma inputs by SHA-256.
