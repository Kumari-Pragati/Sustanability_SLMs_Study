system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    xs[0] + xs[1] * x + xs[2] * x^2 +....
    Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [(i * x) for i, x in enumerate(xs)][1:]assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_62_code import derivative

class TestDerivative(unittest.TestCase):

    def test_derivative(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])
        self.assertEqual(derivative([1, 2, 3]), [2, 6])
        self.assertEqual(derivative([1]), [0])
        self.assertEqual(derivative([1, 2]), [2])
        self.assertEqual(derivative([1, 2, 3, 4, 5, 6]), [2, 6, 12, 20, 30])

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            derivative([])

    def test_single_element_list(self):
        self.assertEqual(derivative([1]), [0])

if __name__ == '__main__':
    unittest.main()