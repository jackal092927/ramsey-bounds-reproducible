#!/usr/bin/env python3

from __future__ import annotations

import math
import unittest

from dual_truncation_sensitivity import coefficients, solve_p


class DualTruncationSensitivityTests(unittest.TestCase):
    def test_p_equation(self) -> None:
        for C in (1.0, 1.1, 2.0, 10.0, 100.0):
            p = solve_p(C)
            self.assertAlmostEqual(math.log(p) / math.log1p(-p), C, places=11)

    def test_c_equals_one_symmetry(self) -> None:
        result = coefficients(1.0)
        self.assertAlmostEqual(result["p_C"], 0.5, places=15)
        self.assertAlmostEqual(result["beta_red"], result["beta_blue"], places=14)
        self.assertAlmostEqual(result["lambda_red"], 0.5, places=15)
        self.assertAlmostEqual(
            result["red_coefficient_of_D_minus_2"],
            result["conditional_blue_coefficient_of_D_minus_2"],
            places=14,
        )

    def test_c_two_closed_form(self) -> None:
        expected = (3 - math.sqrt(5)) / 2
        self.assertAlmostEqual(solve_p(2.0), expected, places=14)

    def test_coefficients_are_positive(self) -> None:
        for C in (1.01, 1.1, 2.0, 5.0, 100.0):
            result = coefficients(C)
            for key in (
                "gamma_red_upper_truncation",
                "gamma_blue_lower_truncation",
                "beta_red",
                "beta_blue",
                "red_coefficient_of_D_minus_2",
                "conditional_blue_coefficient_of_D_minus_2",
            ):
                self.assertGreater(result[key], 0.0)

    def test_two_shift_transverse_derivative(self) -> None:
        # Numerically check the implicit crossing formula using constant shifts.
        C = 2.0
        result = coefficients(C)
        p0 = result["p_C"]
        dr = result["beta_red"]
        db = C**3 * result["beta_blue"]

        def red(p: float) -> float:
            return -0.5 * math.log(p)

        def blue(p: float) -> float:
            return -0.5 * C * math.log1p(-p)

        for epsilon in (1e-4, 1e-5, 1e-6):
            lo, hi = p0 / 2, (1 + p0) / 2
            for _ in range(160):
                mid = (lo + hi) / 2
                # red decreases and blue increases with p.
                if red(mid) + epsilon * dr > blue(mid) + epsilon * db:
                    lo = mid
                else:
                    hi = mid
            p_star = (lo + hi) / 2
            rho_star = min(red(p_star) + epsilon * dr, blue(p_star) + epsilon * db)
            observed = (rho_star - red(p0)) / epsilon
            predicted = (
                result["red_coefficient_of_D_minus_2"]
                + result["conditional_blue_coefficient_of_D_minus_2"]
            )
            self.assertAlmostEqual(observed, predicted, delta=3 * epsilon)


if __name__ == "__main__":
    unittest.main()
