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
   - Include from HumanEval_57_code import monotonic
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
2. Include: from HumanEval_57_code import monotonic
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False


assistant

import unittest

from HumanEval_57_code import monotonic

class TestMonotonicity(unittest.TestCase):
    def test_monotonic_increasing(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))

    def test_monotonic_decreasing(self):
        self.assertFalse(monotonic([1, 20, 4, 10]))

    def test_monotonic_neutral(self):
        self.assertTrue(monotonic([4, 1, 0, -10]))

    def test_equal_elements(self):
        self.assertTrue(monotonic([1, 2, 3, 4]))
        self.assertTrue(monotonic([-1, -2, -3]))
        self.assertTrue(monotonic([1, 2, 3, 4, 5]))

    def test_sorted_lists(self):
        self.assertTrue(monotonic(sorted([1, 2, 3])))
        self.assertTrue(monotonic(sorted([1, 2, 3], reverse=True)))
        self.assertTrue(monotonic(sorted([-1, -2, -3])))
        self.assertTrue(monotonic(sorted([-1, -2, -3], reverse=True)))

    def test_unsorted_lists(self):
        self.assertFalse(monotonic([1, 3, 2]))
        self.assertFalse(monotonic([1, 3, 2, 4]))
        self.assertFalse(monotonic([1, 3, 2, 4, 5]))

if __name__ == '__main__':
    unittest.main()