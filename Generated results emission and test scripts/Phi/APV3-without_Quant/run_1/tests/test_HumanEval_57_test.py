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

 import unittest
from HumanEval_57_code import monotonic

class TestMonotonic(unittest.TestCase):
    def test_increasing_order(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))

    def test_decreasing_order(self):
        self.assertTrue(monotonic([20, 4, 1, 0, -10]))

    def test_mixed_order(self):
        self.assertFalse(monotonic([1, 20, 4, 10]))

    def test_empty_list(self):
        self.assertTrue(monotonic([]))

    def test_single_element(self):
        self.assertTrue(monotonic([5]))

    def test_duplicate_elements(self):
        self.assertTrue(monotonic([3, 3, 3]))

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            monotonic([1, 'a', 3])

if __name__ == '__main__':
    unittest.main()