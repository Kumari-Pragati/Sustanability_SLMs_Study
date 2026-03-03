Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

    def test_derivative_of_polynomial(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

    def test_derivative_of_constant_polynomial(self):
        self.assertEqual(derivative([1]), [])

    def test_derivative_of_linear_polynomial(self):
        self.assertEqual(derivative([2, 3]), [3])

    def test_derivative_of_zero_polynomial(self):
        self.assertEqual(derivative([]), [])

    def test_derivative_with_negative_coefficients(self):
        self.assertEqual(derivative([-3, -1, -2]), [-1, -4])

    def test_derivative_with_single_term(self):
        self.assertEqual(derivative([5]), [])

    def test_derivative_with_multiple_terms(self):
        self.assertEqual(derivative([1, 0, -2, 3]), [0, -2, 9])

if __name__ == '__main__':
    unittest.main()