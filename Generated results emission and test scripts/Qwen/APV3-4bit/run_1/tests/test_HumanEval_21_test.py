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
    
    # Test case for positive numbers
    def test_positive_numbers(self):
        result = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(result, expected_result)
        
    # Test case for negative numbers
    def test_negative_numbers(self):
        result = rescale_to_unit([-1.0, -2.0, -3.0, -4.0, -5.0])
        expected_result = [-1.0, -0.25, -0.5, -0.75, -1.0]
        self.assertEqual(result, expected_result)
        
    # Test case for empty list
    def test_empty_list(self):
        result = rescale_to_unit([])
        expected_result = []
        self.assertEqual(result, expected_result)
        
    # Test case for mixed numbers
    def test_mixed_numbers(self):
        result = rescale_to_unit([0.0, 1.0, 2.0, 3.0, 4.0])
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(result, expected_result)
        
    # Test case for floating point numbers
    def test_floats(self):
        result = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0, 1.0]
        self.assertEqual(result, expected_result)
        
    # Test case for large numbers
    def test_large_numbers(self):
        result = rescale_to_unit([1e9, 2e8, 3e7, 4e6, 5e5])
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(result, expected_result)
        
    # Test case for small numbers
    def test_small_numbers(self):
        result = rescale_to_unit([1e-9, 2e-8, 3e-7, 4e-6, 5e-5])
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(result, expected_result)
        
    # Test case for zero
    def test_zero(self):
        result = rescale_to_unit([0.0])
        expected_result = [0.0]
        self.assertEqual(result, expected_result)
        
    # Test case for one element list
    def test_single_element_list(self):
        result = rescale_to_unit([1.0])
        expected_result = [0.0]
        self.assertEqual(result, expected_result)
        
    # Test case for duplicate values
    def test_duplicate_values(self):
        result = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0, 1.0])
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0, 0.0]
        self.assertEqual(result, expected_result)
        
    # Test case for very small numbers
    def test_vsmall_numbers(self):
        result = rescale_to_unit([1e-10, 2e-9, 3e-8, 4e-7, 5e-6])
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(result, expected_result)
        
    # Test case for very large numbers
    def test_vlarge_numbers(self):
        result = rescale_to_unit([1e+10, 2e+9, 3e+8, 4e+7, 5e+6])
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(result, expected_result)
        
    # Test case for non-float input
    def test_non_float_input(self):
        with self.assertRaises(TypeError):
            rescale_to_unit("abc")