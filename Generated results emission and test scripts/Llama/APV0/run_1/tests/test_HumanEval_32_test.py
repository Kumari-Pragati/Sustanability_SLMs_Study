user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return xs[0] + xs[1] * x + xs[2] * x^2 +.... + xs[n] * x^n
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
    return beginassistant

Here is the unittest test script for the `find_zero` function:

import unittest
from HumanEval_32_code import find_zero

class TestFindZero(unittest.TestCase):
    def test_find_zero(self):
        # Test 1: Simple polynomial
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=2)
        # Test 2: Quadratic polynomial
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=2)
        # Test 3: Cubic polynomial
        self.assertAlmostEqual(find_zero([1, -3, 3, -1]), 1.0, places=2)
        # Test 4: Polynomial with multiple zeros
        self.assertAlmostEqual(find_zero([1, -2, 1, -1]), 0.5, places=2)
        # Test 5: Edge case: single coefficient
        self.assertAlmostEqual(find_zero([1]), 0.0, places=2)
        # Test 6: Edge case: zero coefficients
        with self.assertRaises(ZeroDivisionError):
            find_zero([])

    def test_find_zero_invalid_input(self):
        # Test 7: Invalid input: odd number of coefficients
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3])
        # Test 8: Invalid input: non-numeric coefficients
        with self.assertRaises(TypeError):
            find_zero([1, 'a', 3])

if __name__ == '__main__':
    unittest.main()

This script defines two test methods: `test_find_zero` and `test_find_zero_invalid_input`. The first method tests the `find_zero` function with various input polynomials and checks that the output is close to the expected value using the `assertAlmostEqual` method. The second method tests the function with invalid input, such as odd number of coefficients or non-numeric coefficients, and checks that the function raises the expected exception using the `assertRaises` method.

You can run this script directly to execute the tests.