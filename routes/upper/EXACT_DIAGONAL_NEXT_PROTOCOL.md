# Exact-diagonal next-round protocol

Date: 2026-08-12

## Frozen objective

Starting from the candidate safe decimal

$$
 R(k,k)\le(3.780685300)^{k+o(k)},
$$

run exactly one bounded high-precision refinement round.  Replace the
previous sufficient diagonal envelope

$$H(z)^2-H(-z)^2$$

by the exact identity

$$
 F(z,z)=H(z)^2-H(z)H(-z).                                       \tag{P1}
$$

Jointly search $u_0$, the rigorous good-event prefactor $D$, the exact
tail parameters $(\beta,\varepsilon)$, and the retained-spine/P6 outer
tuple.  No canonical file may be edited in this round.

## Frozen acceptance gates

The round succeeds only if every item below passes without weakening.

1. The actual exponent gap must improve enough that the resulting actual
   base is at least $10^{-8}$ smaller than the current actual candidate
   base $3.7806852985874904\ldots$.
2. The outward-rounded safe decimal must be at most
   $3.780685290$.
3. Every critical outer margin, including the degree gate, red page, blue
   page, reservoir, and final decimal rounding, must be at least $10^{-9}$.
4. The exact rational inner tail-budget margin must be at least $10^{-5}$.
5. A single exact correlation constant $C=4u_0(1+\varepsilon)$ must be
   reconstructed independently by both the inner and outer checkers.
6. The bad-event ratio/separator, the full two-dimensional sign reduction,
   the compact exact-diagonal envelope, its analytic tail and asymptotic
   constant, and the complete outer wedge must all be proved, not sampled.
7. A successful package requires an author 512-bit Arb checker and a
   genuinely non-importing 512-bit replay which reconstructs all special
   functions, rate functions, exact constants, and proof reductions.

## Bounded search and freeze rule

- Exploratory floating-point search may be used only to locate a candidate.
- At most one candidate may be rationalized and subjected to the complete
  high-precision freeze/replay sequence.
- Once rationalization begins, no second high-precision candidate is
  allowed in this round.
- If any fixed gate fails, record the best bounded-search frontier and the
  failed gate.  Do not lower a margin, change the target safe decimal, or
  start another freeze.

## Method diagnostic fixed before search

The exact diagonal principally improves the compact enclosure, not the
asymptotic floor.  At $u_0=2.472$ and $u=20$, preliminary evaluation gives

$$
 \frac{H(u^3)^2-H(u^3)H(-u^3)}{e^{4w}}
 \approx 8.365826294619\cdot10^{-5},
$$

whereas the square-difference surrogate is approximately
$8.365826294739\cdot10^{-5}$.  Both converge to

$$
 D_\infty(u_0)=\frac{e^{-2u_0}}{81};                              \tag{P2}
$$

at $u_0=2.472$ this is approximately
$8.797576715275\cdot10^{-5}$.  Therefore the search must treat (P2) as the
binding inner floor and seek improvement mainly by increasing $u_0$ enough
to lower that floor while balancing the resulting increase in
$C=4u_0(1+\varepsilon)$.  No success may be attributed merely to replacing
the compact square-difference expression by (P1).

## Claim boundary

Even if all numerical gates pass, the result remains a conditional local
computer-assisted candidate until independent proof review.  This protocol
does not authorize a canonical bound change, a global optimality claim, a
finite-$k$ threshold, or a priority claim.
