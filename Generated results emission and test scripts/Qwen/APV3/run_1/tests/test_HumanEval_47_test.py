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
   - Include from HumanEval_47_code import median
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
2. Include: from HumanEval_47_code import median
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0


assistant

import unittest

from HumanEval_47_code import median

class TestMedian(unittest.TestCase):
    def test_normal_input(self):
        self.assertAlmostEqual(median([3, 1, 2, 4, 5]), 3)
        self.assertAlmostEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

    def test_edge_case_odd_length(self):
        self.assertAlmostEqual(median([1, 2, 3, 4, 5]), 3)

    def test_edge_case_even_length(self):
        self.assertAlmostEqual(median([1, 2, 3, 4]), 2.5)

    def test_empty_list(self):
        self.assertIsNone(median([]))

    def test_single_element(self):
        self.assertAlmostEqual(median([5]), 5)

    def test_sorted_list(self):
        self.assertAlmostEqual(median([1, 2, 3, 4, 5]), 3)

    def test_repeated_values(self):
        self.assertAlmostEqual(median([1, 1, 1, 1, 1]), 1)

    def test_large_number(self):
        self.assertAlmostEqual(median([1e9, 2e9, 3e9, 4e9, 5e9]), 3e9)

    def test_floats(self):
        self.assertAlmostEqual(median([1.5, 2.5, 3.5, 4.5, 5.5]), 3.5)

    def test_mixed_types(self):
        self.assertAlmostEqual(median([1, 'a', 3, True, False]), None)

if __name__ == '__main__':
    unittest.main()