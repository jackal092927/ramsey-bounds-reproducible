"""Tiny exact check of the padded-bulk boundary convention, not a gap proof."""

from fractions import Fraction


def boundary(chain, weights):
    result = {}
    for simplex, coefficient in chain.items():
        for index, vertex in enumerate(simplex):
            face = simplex[:index] + simplex[index + 1:]
            term = coefficient * weights[vertex] * (-1) ** index
            result[face] = result.get(face, Fraction(0)) + term
    return {face: value for face, value in result.items() if value}


def bulk(chain):
    return {face: value for face, value in chain.items() if 0 in face}


def norm_squared(chain):
    return sum((coefficient * coefficient for coefficient in chain.values()), Fraction(0))


for lam in (Fraction(1, 2), Fraction(1, 16), Fraction(1, 256)):
    weights = {0: lam, 1: lam, 2: Fraction(1), 3: Fraction(1),
               4: Fraction(1), 5: Fraction(1)}
    # A local bulk edge [0,1] joined with one outside register edge [2,3].
    test = {(0, 1, 2, 3): Fraction(1)}
    projected = bulk(boundary(test, weights))
    assert norm_squared(projected) == 2 + lam * lam

    # The same local edge joined with a normalized outside four-cycle.
    outside_cycle = {(2, 3): Fraction(1, 2), (3, 4): Fraction(1, 2),
                     (4, 5): Fraction(1, 2), (2, 5): Fraction(-1, 2)}
    assert not boundary(outside_cycle, weights)
    joined = {(0, 1) + edge: value for edge, value in outside_cycle.items()}
    harmonic_projected = bulk(boundary(joined, weights))
    assert norm_squared(harmonic_projected) == lam * lam
    assert all(sum(vertex >= 2 for vertex in face) == 2 for face in harmonic_projected)
    print(f"lambda={lam}: arbitrary-edge bulk boundary squared={norm_squared(projected)}; "
          f"harmonic-outside squared={norm_squared(harmonic_projected)}")

print("PASS: unit-weight padded boundary survives for arbitrary inputs and cancels for the outside cycle.")
