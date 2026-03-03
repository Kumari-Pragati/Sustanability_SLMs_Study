You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

class TestFindZero(unittest.TestCase):

    def test_find_zero_with_simple_polynomial(self):
        # Test with a simple linear polynomial
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=2)

    def test_find_zero_with_quadratic_polynomial(self):
        # Test with a quadratic polynomial
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=2)

    def test_find_zero_with_even_coefficients(self):
        # Test with a polynomial that has an even number of coefficients
        self.assertAlmostEqual(find_zero([1, -3, 2, -1]), 1.0, places=2)

    def test_find_zero_with_no_solution(self):
        # Test with a polynomial that has no real solution
        self.assertAlmostEqual(find_zero([1, 1, 1]), None, places=2)

    def test_find_zero_with_multiple_solutions(self):
        # Test with a polynomial that has multiple solutions
        self.assertAlmostEqual(find_zero([1, -3, 3, -1]), 1.0, places=2)

    def test_find_zero_with_large_coefficient(self):
        # Test with a polynomial that has a large non-zero coefficient
        self.assertAlmostEqual(find_zero([1000, -1000, 1000]), 1.0, places=2)

    def test_find_zero_with_negative_coefficients(self):
        # Test with a polynomial that has negative coefficients
        self.assertAlmostEqual(find_zero([-1, 2, -3, 1]), 1.0, places=2)

    def test_find_zero_with_zero_coefficients(self):
        # Test with a polynomial that has zero coefficients
        self.assertIsNone(find_zero([]))

    def test_find_zero_with_single_coefficient(self):
        # Test with a polynomial that has only one coefficient
        self.assertIsNone(find_zero([1]))

    def test_find_zero_with_invalid_input(self):
        # Test with invalid input (non-list or list with odd number of elements)
        with self.assertRaises(TypeError):
            find_zero("not a list")
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3])

if __name__ == '__main__':
    unittest.main()