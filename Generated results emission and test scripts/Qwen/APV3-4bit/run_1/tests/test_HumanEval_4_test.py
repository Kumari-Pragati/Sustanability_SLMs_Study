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
   - Include from HumanEval_4_code import mean_absolute_deviation
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
2. Include: from HumanEval_4_code import mean_absolute_deviation
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a center point (mean in this case):
    MAD = average |x - x_mean|
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)


assistant

import unittest

# Importing the function we want to test
from HumanEval_4_code import mean_absolute_deviation

class TestMeanAbsoluteDeviation(unittest.TestCase):
    
    # Test cases for different scenarios
    def test_normal_input(self):
        result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        expected_result = 1.0
        self.assertAlmostEqual(result, expected_result, places=2)
        
    def test_edge_case(self):
        # Edge case where all elements are equal
        result = mean_absolute_deviation([1.0, 1.0, 1.0, 1.0])
        expected_result = 0.0
        self.assertAlmostEqual(result, expected_result, places=2)
        
    def test_empty_list(self):
        # Testing with an empty list
        result = mean_absolute_deviation([])
        expected_result = 0.0
        self.assertAlmostEqual(result, expected_result, places=2)
        
    def test_single_element(self):
        # Testing with a single-element list
        result = mean_absolute_deviation([1.0])
        expected_result = 0.0
        self.assertAlmostEqual(result, expected_result, places=2)
        
    def test_mixed_types(self):
        # Testing with mixed types (integers and floats)
        result = mean_absolute_deviation([1.0, 2.0, '3', 4.0])
        expected_result = 1.0
        self.assertAlmostEqual(result, expected_result, places=2)
        
    def test_large_values(self):
        # Testing with large values
        result = mean_absolute_deviation([1e9, 2e9, 3e9, 4e9])
        expected_result = 1.0 * 1e9
        self.assertAlmostEqual(result, expected_result, places=2)
        
    def test_negative_values(self):
        # Testing with negative values
        result = mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0])
        expected_result = 1.0 * 1.0
        self.assertAlmostEqual(result, expected_result, places=2)
        
    def test_zero_division(self):
        # Testing with zero division
        result = mean_absolute_deviation([0.0, 0.0, 0.0, 0.0])
        expected_result = 0.0
        self.assertAlmostEqual(result, expected_result, places=2)
        
    def test_infinitesimal_values(self):
        # Testing with infinitesimally small values
        result = mean_absolute_deviation([1e-18, 2e-18, 3e-18, 4e-18])
        expected_result = 0.0
        self.assertAlmostEqual(result, expected_result, places=2)
        
    def test_complex_numbers(self):
        # Testing with complex numbers
        result = mean_absolute_deviation([1+2j, 2+3j, 3+4j, 4+5j])
        expected_result = 1.0 * 1.0
        self.assertAlmostEqual(result, expected_result, places=2)
        
    def test_string_input(self):
        # Testing with string input
        result = mean_absolute_deviation("abc")
        expected_result = 0.0
        self.assertAlmostEqual(result, expected_result, places=2)
        
    def test_none_input(self):
        # Testing with None as input
        result = mean_absolute_deviation(None)
        expected_result = 0.0
        self.assertAlmostEqual(result, expected_result, places=2)
        
    def test_floats_only(self):
        # Testing with floats only
        result = mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        expected_result = 1.0
        self.assertAlmostEqual(result, expected_result, places=2)
        
    def test_integers_only(self):
        # Testing with integers only
        result = mean_absolute_deviation([1, 2, 3, 4])
        expected_result = 1.0
        self.assertAlmostEqual(result, expected_result, places=2)
        
    def test_all_zeros(self):
        # Testing with all zeros
        result = mean_absolute_deviation([0.0, 0.0, 0.0, 0.0])
        expected_result = 0.0
        self.assertAlmostEqual(result, expected_result, places=2)
        
    def test_all_negatives(self):
        # Testing with all negatives
        result = mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0])
        expected_result = 1.0 * 1.0
        self.assertAlmostEqual(result, expected_result, places=2)