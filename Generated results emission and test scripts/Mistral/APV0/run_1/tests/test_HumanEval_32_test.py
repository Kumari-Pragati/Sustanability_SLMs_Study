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

 Here is a unittest test script for the `find_zero` function:


import unittest
from HumanEval_32_code import find_zero

class TestFindZero(unittest.TestCase):

    def test_find_zero(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, delta=0.01)
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, delta=0.01)
        self.assertAlmostEqual(find_zero([-1, 2, -1]), -0.618033988749895, delta=0.01)
        self.assertAlmostEqual(find_zero([0, 0, 1]), 0.0, delta=0.01)
        self.assertAlmostEqual(find_zero([-1, 2, 1]), -0.414213562373095, delta=0.01)
        self.assertAlmostEqual(find_zero([-1, 0, 1]), 0.0, delta=0.01)
        self.assertAlmostEqual(find_zero([1, -3, 2]), -1.0, delta=0.01)
        self.assertAlmostEqual(find_zero([-1, 2, -1, 0]), -0.618033988749895, delta=0.01)
        self.assertAlmostEqual(find_zero([-1, 0, 0, 1]), 0.0, delta=0.01)
        self.assertAlmostEqual(find_zero([1, -2, 1, -6]), -1.0, delta=0.01)
        self.assertAlmostEqual(find_zero([-1, 2, -1, 0, 1]), -0.618033988749895, delta=0.01)
        self.assertAlmostEqual(find_zero([-1, 0, 0, 0, 1]), 0.0, delta=0.01)
        self.assertAlmostEqual(find_zero([1, -2, 1, -6, 4]), -1.0, delta=0.01)
        self.assertAlmostEqual(find_zero([-1, 2, -1, 0, 1, 0]), -0.618033988749895, delta=0.01)
        self.assertAlmostEqual(find_zero([-1, 0, 0, 0, 0, 1]), 0.0, delta=0.01)
        self.assertAlmostEqual(find_zero([1, -2, 1, -6, 4, 0]), -1.0, delta=0.01)

if __name__ == '__main__':
    unittest.main()


This test script includes multiple test cases for the `find_zero` function, ensuring that it works correctly for various input polynomials. The test cases cover both simple and complex polynomials, including those with negative coefficients and those with multiple terms. The test cases also check the edge cases where the polynomial has a zero at x=0 or x=1.