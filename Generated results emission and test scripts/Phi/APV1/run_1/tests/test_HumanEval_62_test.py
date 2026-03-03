You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_62_code import derivative

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def derivative(xs: list):
    """xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [(i * x) for i, x in enumerate(xs)][1:]

 import unittest
from HumanEval_62_code import derivative

class TestDerivativeFunction(unittest.TestCase):

    def test_derivative_of_constant_polynomial(self):
        self.assertEqual(derivative([3]), [0])

    def test_derivative_of_linear_polynomial(self):
        self.assertEqual(derivative([1, 2]), [2])

    def test_derivative_of_quadratic_polynomial(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

    def test_derivative_of_cubic_polynomial(self):
        self.assertEqual(derivative([1, 2, 3, 4]), [2, 6, 12])

    def test_derivative_of_polynomial_with_zero_coefficient(self):
        self.assertEqual(derivative([0, 5]), [0])

    def test_derivative_of_polynomial_with_all_zero_coefficients(self):
        self.assertEqual(derivative([0, 0, 0]), [0])

    def test_derivative_of_polynomial_with_single_coefficient(self):
        self.assertEqual(derivative([5]), [0])

    def test_derivative_of_polynomial_with_negative_coefficients(self):
        self.assertEqual(derivative([-3, 1, -2]), [0, -2])

    def test_derivative_of_polynomial_with_mixed_coefficients(self):
        self.assertEqual(derivative([1, -2, 3, -4]), [0, -2, 12, -16])

    def test_derivative_of_polynomial_with_large_coefficients(self):
        self.assertEqual(derivative([1000, 100, 10, 1]), [0, 100, 40, 1])

    def test_derivative_of_polynomial_with_floating_point_coefficients(self):
        self.assertAlmostEqual(derivative([1.5, 2.3, 3.7]), [0, 2.3, 11.1])

if __name__ == '__main__':
    unittest.main()