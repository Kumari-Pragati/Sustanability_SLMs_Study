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
   - Include from HumanEval_13_code import greatest_common_divisor
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
2. Include: from HumanEval_13_code import greatest_common_divisor
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a


assistant

import unittest

from HumanEval_13_code import greatest_common_divisor

class TestGCD(unittest.TestCase):
    def test_gcd_positive(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)

    def test_gcd_negative(self):
        self.assertEqual(greatest_common_divisor(-3, 5), 1)

    def test_gcd_zero(self):
        self.assertEqual(greatest_common_divisor(0, 5), 5)

    def test_gcd_large_numbers(self):
        self.assertEqual(greatest_common_divisor(97, 89), 1)

    def test_gcd_edge_cases(self):
        # Edge cases should result in zero as the GCD
        self.assertEqual(greatest_common_divisor(0, 0), 0)
        self.assertEqual(greatest_common_divisor(1, 1), 1)
        self.assertEqual(greatest_common_divisor(2, 2), 2)

    def test_gcd_large_numbers_with_zeros(self):
        # Large numbers where one number is zero
        self.assertEqual(greatest_common_divisor(100, 20), 20)
        self.assertEqual(greatest_common_divisor(100, 0), 100)
        self.assertEqual(greatest_common_divisor(0, 100), 100)

    def test_gcd_large_numbers_with_large_factors(self):
        # Numbers that have large factors but still share some common factor
        self.assertEqual(greatest_common_divisor(120, 180), 60)

if __name__ == '__main__':
    unittest.main()