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
   - Include from HumanEval_83_code import starts_one_ends
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
    unittest.main()user

### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_83_code import starts_one_ends
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 1
    return 18 * (10 ** (n - 2))assistant

import unittest
from HumanEval_83_code import starts_one_ends

class TestStartsOneEnds(unittest.TestCase):
    def test_n_1(self):
        self.assertEqual(starts_one_ends(1), 1)

    def test_n_2(self):
        self.assertEqual(starts_one_ends(2), 18)

    def test_n_3(self):
        self.assertEqual(starts_one_ends(3), 1800)

    def test_n_4(self):
        self.assertEqual(starts_one_ends(4), 180000)

    def test_n_5(self):
        self.assertEqual(starts_one_ends(5), 18000000)

    def test_n_6(self):
        self.assertEqual(starts_one_ends(6), 180000000)

    def test_n_7(self):
        self.assertEqual(starts_one_ends(7), 18000000000)

    def test_n_8(self):
        self.assertEqual(starts_one_ends(8), 180000000000)

    def test_n_9(self):
        self.assertEqual(starts_one_ends(9), 1800000000000)

    def test_n_10(self):
        self.assertEqual(starts_one_ends(10), 18000000000000)

if __name__ == '__main__':
    unittest.main()