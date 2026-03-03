You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_32_code import find_zero
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    begin, end = -1.0, 1.0
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2.0
        end *= 2.0
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(xs, center) * poly(xs, begin) > 0:
            begin = center
        else:
            end = center
    return begin

 import unittest
from HumanEval_32_code import find_zero
import math

class TestPolynomialFunctions(unittest.TestCase):

    def test_poly_with_simple_coefficients(self):
        # Test the poly function with simple coefficients
        self.assertAlmostEqual(poly([1, 2], 0), 1)
        self.assertAlmostEqual(poly([1, 2], 1), 3)
        self.assertAlmostEqual(poly([1, 2], -1), -1)

    def test_poly_with_negative_coefficients(self):
        # Test the poly function with negative coefficients
        self.assertAlmostEqual(poly([-1, 2], 0), -1)
        self.assertAlmostEqual(poly([-1, 2], 1), 1)
        self.assertAlmostEqual(poly([-1, 2], -1), -3)

    def test_poly_with_zero_coefficients(self):
        # Test the poly function with zero coefficients
        self.assertAlmostEqual(poly([0], 0), 0)

    def test_find_zero_with_simple_coefficients(self):
        # Test find_zero function with simple coefficients
        self.assertAlmostEqual(find_zero([1, 2]), -0.5)

    def test_find_zero_with_negative_coefficients(self):
        # Test find_zero function with negative coefficients
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0)

    def test_find_zero_with_even_number_of_coefficients(self):
        # Test find_zero function with an even number of coefficients
        self.assertAlmostEqual(find_zero([1, -1, 1, -1]), 0)

    def test_find_zero_with_non_zero_largest_coefficient(self):
        # Test find_zero function with the largest non-zero coefficient
        self.assertAlmostEqual(find_zero([1, 0, 0, -1]), 1.0)

    def test_find_zero_with_large_coefficients(self):
        # Test find_zero function with large coefficients
        self.assertAlmostEqual(find_zero([1000, 1000, -2000, 1]), 1.0)

    def test_find_zero_with_no_solution(self):
        # Test find_zero function with no solution
        with self.assertRaises(ValueError):
            find_zero([1, 1])

if __name__ == '__main__':
    unittest.main()