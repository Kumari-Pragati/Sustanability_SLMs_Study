system
### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_32_code import find_zero
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

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


assistant

import unittest
from HumanEval_32_code import find_zero

class TestFindZero(unittest.TestCase):
    def test_positive_coefficients(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5)
    
    def test_even_number_of_coefficients(self):
        self.assertAlmostEqual(find_zero([1, 2, 3, 4]), -0.5)
    
    def test_odd_number_of_coefficients(self):
        self.assertRaises(ValueError, lambda: find_zero([1, 2, 3]))
    
    def test_non_zero_coefficient(self):
        self.assertAlmostEqual(find_zero([1, 2, 3, 4, 5]), -0.5)
    
    def test_large_coefficients(self):
        self.assertAlmostEqual(find_zero([1000000, 999999, 999988, 999977, 999966, 999955, 999944, 999933, 999922, 999911, 999900]), -0.5)
    
    def test_small_coefficients(self):
        self.assertAlmostEqual(find_zero([0.000001, 0.000002, 0.000003, 0.000004, 0.000005]), -0.5)
    
    def test_float_precision(self):
        self.assertAlmostEqual(find_zero([1.000001, 2.000002, 3.000003, 4.000004, 5.000005]), -0.5)
    
    def test_edge_case(self):
        self.assertAlmostEqual(find_zero([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), -0.5)
    
    def test_complex_function(self):
        self.assertAlmostEqual(find_zero([-1, 0, 1]), 0.0)
    
    def test_infinite_loop(self):
        self.assertRaises(RecursionError, lambda: find_zero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

if __name__ == '__main__':
    unittest.main()