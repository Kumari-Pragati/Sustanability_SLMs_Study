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
   - Include from HumanEval_52_code import below_threshold
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
2. Include: from HumanEval_52_code import below_threshold
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for e in l:
        if e >= t:
            return False
    return True


assistant

import unittest

from HumanEval_52_code import below_threshold

class TestBelowThreshold(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))

    def test_negative_numbers(self):
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))

    def test_single_element(self):
        self.assertTrue(below_threshold([1], 100))

    def test_empty_list(self):
        self.assertTrue(below_threshold([], 100))

    def test_all_above_threshold(self):
        self.assertFalse(below_threshold([100, 99, 98, 97], 100))

    def test_mixed_values(self):
        self.assertTrue(below_threshold([1, 2, 3, 4], 10))
        self.assertFalse(below_threshold([1, 2, 3, 4], 100))

if __name__ == '__main__':
    unittest.main()