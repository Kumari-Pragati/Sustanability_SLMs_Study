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
   - Include from HumanEval_21_code import rescale_to_unit
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
2. Include: from HumanEval_21_code import rescale_to_unit
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]


assistant

import unittest

# Importing the function we want to test
from HumanEval_21_code import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):
    def test_normal_input(self):
        result = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(result, expected_result)

    def test_edge_case_min_max_equal(self):
        result = rescale_to_unit([1.0, 1.0, 1.0, 1.0, 1.0])
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(result, expected_result)

    def test_edge_case_one_element(self):
        result = rescale_to_unit([1.0])
        expected_result = [0.0]
        self.assertEqual(result, expected_result)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            rescale_to_unit("not a list")

if __name__ == '__main__':
    unittest.main()