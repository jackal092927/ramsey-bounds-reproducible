"""Exact finite checks of the 1D OR/barcode reduction, not quantum simulation."""

from fractions import Fraction
import json


def largest_gap(points):
    ordered = sorted(points)
    return max(b - a for a, b in zip(ordered, ordered[1:]))


def main():
    count = 0
    min_zero = Fraction(1)
    max_one = Fraction(0)
    # Includes n=1, non-power-of-two sizes and the last-point outlier.
    for n in range(1, 65):
        denominator = 1 << ((n - 1).bit_length() + 10)
        original = [Fraction(i, denominator) for i in range(1, n + 1)]
        zero = largest_gap(original + [Fraction(1)])
        assert zero >= Fraction(1023, 1024)
        min_zero = min(min_zero, zero)
        for j in range(n):
            moved = original.copy()
            moved[j] += Fraction(1, 2)
            one = largest_gap(moved + [Fraction(1)])
            assert one <= Fraction(1, 2) + Fraction(1, 1024)
            # A bottleneck error below .1 changes max finite length by <.2.
            assert zero - Fraction(1, 5) > Fraction(3, 4)
            assert one + Fraction(1, 5) < Fraction(3, 4)
            max_one = max(max_one, one)
            count += 1

    # Why maximum death is the wrong output statistic: the extra short bar
    # matches to the diagonal at cost 1/2000 but has arbitrarily large death.
    extra = (Fraction(100), Fraction(100001, 1000))
    assert (extra[1] - extra[0]) / 2 == Fraction(1, 2000)
    assert extra[1] > 100
    assert extra[1] - extra[0] < min_zero
    print(json.dumps({"status": "PASS", "kind": "exact rational barcode fixture",
                      "sizes_tested": 64, "singleton_cases": count,
                      "minimum_zero_case_max_length": str(min_zero),
                      "maximum_one_case_max_length": str(max_one),
                      "spurious_bar_diagonal_cost": "1/2000"}, indent=2))


if __name__ == "__main__":
    main()
