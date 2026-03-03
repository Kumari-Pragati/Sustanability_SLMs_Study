You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_62_code import derivative

class TestDerivative(unittest.TestCase):

    def test_positive_coefficients(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

    def test_negative_coefficients(self):
        self.assertEqual(derivative([-3, -1, -2, -4, -5]), [-1, -4, -12, -20])

    def test_single_term(self):
        self.assertEqual(derivative([3]), [])

    def test_empty_list(self):
        self.assertEqual(derivative([]), [])

    def test_large_list(self):
        self.assertEqual(derivative(list(range(1, 1001))), list(range(1, 1000)))

    def test_zero_coefficients(self):
        self.assertEqual(derivative([0, 0, 0, 0]), [0, 0])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive, negative, single term, empty list, large list, and zero coefficients. It checks if the derivative function is working correctly for all these cases.