You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `derivative` function:


import unittest
from HumanEval_62_code import derivative

class TestDerivative(unittest.TestCase):

    def test_derivative_simple_polynomial(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

    def test_derivative_small_polynomial(self):
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

    def test_derivative_zero_coefficients(self):
        self.assertEqual(derivative([]), [])

    def test_derivative_single_coefficient(self):
        self.assertEqual(derivative([1]), [0])

    def test_derivative_negative_coefficients(self):
        self.assertEqual(derivative([-3, 1, -2, 4, -5]), [-1, -4, 12, -20])

    def test_derivative_empty_input(self):
        with self.assertRaises(TypeError):
            derivative(None)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios such as simple polynomials, small polynomials, zero coefficients, single coefficient, negative coefficients, empty input, and edge cases. The test suite uses the `unittest.TestCase` class to define test methods and asserts the expected results against the actual results returned by the `derivative` function.