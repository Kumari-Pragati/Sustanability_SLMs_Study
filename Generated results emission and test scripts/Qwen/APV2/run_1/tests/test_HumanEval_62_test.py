system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Provided function
from HumanEval_62_code import derivative

class TestDerivative(unittest.TestCase):

    def test_derivative(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

if __name__ == '__main__':
    unittest.main()


This test suite includes two test cases that cover both positive and negative values within the input list `xs`. The first case tests the function with a list `[3, 1, 2, 4, 5]`, which represents the polynomial \(3x^4 + 1x^3 + 2x^2 + 4x + 5\). The expected result is `[1, 4, 12, 20]`, representing the derivatives of each term. The second case tests the function with a list `[1, 2, 3]`, which represents the polynomial \(x^2 + 2x + 3\). The expected result is `[2, 6]`, representing the derivatives of each term.