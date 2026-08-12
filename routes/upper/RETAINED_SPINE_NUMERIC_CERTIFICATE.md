# Conservative numerical certificate for the retained-spine transfer

Date: 2026-08-12  
Precision: 256-bit Arb (`python-flint==0.9.0`)

## Verdict

```text
analytic two-region cover of [0,1]^2:       PASS
all page-branch derivative signs:           PASS
certified exponent improvement 1e-8:        PASS
certified decimal upper bound:               PASS
independent review of this numeric note:     PENDING
```

The already refereed transfer theorem defines

\[
 C_* = \max_{\sigma\in[0,1]^2}\min\{D(\sigma),B(\sigma)\}
\]

and proves

\[
 R(k,k)\leq \exp(C_*k+o(k)).
\]

The present certificate proves the deliberately conservative explicit bound

\[
 \boxed{C_*\leq U(1)-10^{-8}}.
\tag{1}
\]

Consequently, conditional on the same Yang--Mao v1 and frozen local P6 trust
boundary as the transfer theorem,

\[
 \boxed{
 R(k,k)
 \leq
 \exp\!\left((U(1)-10^{-8})k+o(k)\right)
 =
 \left(3.7806983899891396098255654219\ldots\right)^{k+o(k)}.}
\tag{2}
\]

In particular, the base in (2) is strictly less than the terminating decimal
`3.780698389989140`.  This improves the frozen P6 base
`3.7806984277961236987518816497...` by about
`3.7806984088926e-8` in the base.  No attempt is made to approximate the true
maximum in the definition of $C_*$.

## Frozen dependencies

The checker refuses to run if any of these upstream files changes:

```text
5aa5d6cb1ee1cc2d9f4d34b8564b6c57f78cfd7444a89abcfbb64542274e4aaa  RETAINED_SPINE_TRANSFER_ATTEMPT.md
6ba57fdbe13bf45255644ae94af5474b7a34afda3aefeda26415f3cc3f9b66db  INDEPENDENT_RETAINED_SPINE_REFEREE.md
b10815b10cb3ab922aa079ee74289c52239ec90939ed41b93907bf06a60ee274  check_retained_spine_transfer.py
8689e3f80f363ac4b2dada31d6d71d682288eac24ca5e128e22aecfffcd4bde8  certificate-higher-order-tetradecic-chain-v6.json
e0dfe25c7fa644e6549c1dd321518f523a4ba787312932b3190237fcca905abe  verify_region_direct_arb.py
```

The first referee's final verdict is `PASS AFTER MINOR CORRECTIONS
(RESOLVED)`.  Thus the requested promotion gate for using the transfer lemma
is satisfied locally.  The new numerical enclosure itself has not yet had a
separate adversarial referee replay.

The numerical checker is

```text
fa19734aa1a29ea14c643cc98ae964ae8c99e6d2bcd0386c88888933c25e427a  check_retained_spine_numeric.py
```

## Two-region proof

Write $x=\sigma_R$, $y=\sigma_B$, and set

\[
 r_0=1.6\cdot10^{-6},\qquad \Delta=10^{-8},
\]

\[
 A=U(1)-2c_\eta,
 \qquad
 E=U'(1)-c_\eta.
\]

The exact transfer parameters and the P6 rate $U$ are those in the frozen
transfer note.

### Region I: outside the tiny square

Suppose $\max\{x,y\}\geq r_0$.  If $x\leq y$, the transfer note's equation
(18) gives

\[
 U(1)-D(x,y)\geq xA+(y-x)E.
\tag{3}
\]

The opposite order is symmetric.  Arb proves $E\geq A>0$, so the right side
of (3) is at least

\[
 yA\geq r_0A.
\]

The endpoint $(1,1)$, at which the ratio used to derive (3) is undefined, is
handled by the exact identity $U(1)-D(1,1)=A\geq r_0A$.  The one-zero
remainder boundaries follow by continuity, exactly as in the refereed
transfer note.  The certified values are

\[
 r_0A
 =1.0578775713351096985\ldots\times10^{-8},
\]

\[
 r_0A-\Delta
 =5.78775713351096985\ldots\times10^{-10}>0.
\tag{4}
\]

Therefore $D(x,y)\leq U(1)-\Delta$ throughout Region I.

### Region II: the square $[0,r_0]^2$

For the first page branch, $\tau=5\cdot10^{-5}>r_0$ implies

\[
 1-y>1-x-\tau>0.
\]

Consequently its homogeneous-rate expression has the single smooth form

\[
 P_R(x,y)
 =c_\eta(x+y)+\tau q+(1-y)U(z),
 \qquad
 z=\frac{1-\tau-x}{1-y}.
\tag{5}
\]

On the whole square,

\[
 z\in
 \left[1-\tau-r_0,\frac{1-\tau}{1-r_0}\right]
 =[0.9999484,\,0.999951599922559876\ldots].
\tag{6}
\]

Differentiating (5) gives

\[
 \frac{\partial P_R}{\partial x}=c_\eta-U'(z),
 \qquad
 \frac{\partial P_R}{\partial y}
 =c_\eta-U(z)+zU'(z).
\tag{7}
\]

Direct interval evaluation of (7) over the complete interval (6) proves

```text
dP_R/dx in [-0.1042 +/- 3.78e-5] < 0
dP_R/dy in [ 0.0976 +/- 4.02e-5] > 0
```

Thus $P_R$ is maximized at $(0,r_0)$.  The second page branch is its transpose
and is maximized at $(r_0,0)$; symmetry gives the same endpoint value.  Hence
the maximum $P=\max\{P_R,P_B\}$ over the whole square is bounded by

\[
 P_{\rm axis}
 =c_\eta r_0+\tau q
 +(1-r_0)U\!\left(\frac{1-\tau}{1-r_0}\right).
\]

Arb certifies

\[
 P_{\rm axis}
 =1.3299086990817350190386668588\ldots,
\]

\[
 U(1)-\Delta-P_{\rm axis}
 =5.27402580532801144\ldots\times10^{-8}>0.
\tag{8}
\]

The reservoir branch

\[
 Q(x,y)=c_\eta(x+y)+2\tau\Xi
\]

is coordinatewise increasing.  Its square maximum is therefore

\[
 Q(r_0,r_0)=0.5695133408104064790\ldots,
\]

and Arb gives the much larger margin

\[
 U(1)-\Delta-Q(r_0,r_0)
 =0.7603954110115865932\ldots>0.
\tag{9}
\]

Equations (8)--(9) prove

\[
 B(x,y)=\max\{P(x,y),Q(x,y)\}
 \leq U(1)-\Delta
\]

throughout Region II.  Combining the book bound in Region II with the direct
bound in Region I covers the entire square and proves (1).

## Independent formula checks performed by the script

The checker does not import the existing rate-evaluation routines.  It
reimplements $U,U',U''$ from the fourteen exact decimal P6 coefficients and:

1. independently proves $U''<0$ on $(0,1]$, using an analytic pole bound near
   zero and 8,192 closed Arb cells on $[10^{-4},1]$;
2. verifies every frozen upstream SHA-256 before calculation;
3. verifies `python-flint==0.9.0` and sets 256-bit precision;
4. proves the direct-region comparison $E\geq A>0$ and (4);
5. proves the branch ordering, the full derivative signs in (7), and the
   endpoint bounds (8)--(9);
6. proves
   $\exp(U(1)-10^{-8})<3.780698389989140$ by an Arb comparison.

## Reproduction

From `routes/upper` run

```text
../../.venv/bin/python check_retained_spine_numeric.py
```

The proof-critical output is

```text
PASS: retained-spine numerical maximum certificate
outer_direct_gain: 1.0578775713351096985...e-8
outer_margin_over_target: 5.78775713351096985...e-10
page_margin_below_target: 5.27402580532801144...e-8
reservoir_margin_below_target: 0.7603954110115865932...
certified_exponent: 1.3299087518219930723187812632...
certified_base: 3.7806983899891396098255654219...
certified_decimal_upper: 3.780698389989140
```

## Claim boundary

This is a computer-assisted asymptotic upper bound, conditional on the exact
upstream transfer theorem, Yang--Mao v1 inputs, frozen local P6 theorem, and
Arb containment semantics.  It is not an externally peer-reviewed or
published result, gives no practical finite-$k$ threshold, and makes no
global novelty claim.  The conservative value in (2) is a proved upper bound
for $e^{C_*}$, not a numerical approximation to the actual optimizer of
$C_*$.
