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

 import unittest
from HumanEval_21_code import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):
    def test_normal_input(self):
        input_numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

    def test_empty_list(self):
        self.assertEqual(rescale_to_unit([]), [])

    def test_single_element_list(self):
        input_numbers = [1.0]
        expected_output = [0.0]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

    def test_all_elements_same(self):
        input_numbers = [1.0, 1.0, 1.0, 1.0]
        expected_output = [0.0, 0.0, 0.0, 0.0]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

    def test_all_elements_zero(self):
        input_numbers = [0.0, 0.0, 0.0, 0.0]
        expected_output = [0.0, 0.0, 0.0, 0.0]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

    def test_all_elements_one(self):
        input_numbers = [1.0, 1.0, 1.0, 1.0]
        expected_output = [1.0, 1.0, 1.0, 1.0]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

    def test_all_elements_negative(self):
        input_numbers = [-1.0, -2.0, -3.0, -4.0]
        expected_output = [0.0, 0.25, 0.5, 0.75]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

    def test_all_elements_positive(self):
        input_numbers = [1.0, 2.0, 3.0, 4.0]
        expected_output = [0.0, 0.25, 0.5, 0.75]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

    def test_all_elements_float(self):
        input_numbers = [1.0, 2.5, 3.7, 4.2]
        expected_output = [0.0, 0.25, 0.5, 0.75]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

if __name__ == '__main__':
    unittest.main()