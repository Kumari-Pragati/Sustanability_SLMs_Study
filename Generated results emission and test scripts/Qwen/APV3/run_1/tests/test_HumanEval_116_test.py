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
   - Include from HumanEval_116_code import sort_array
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
2. Include: from HumanEval_116_code import sort_array
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))


assistant

import unittest

# Provided function
from HumanEval_116_code import sort_array

class TestSortArray(unittest.TestCase):
    def test_normal_input(self):
        self.assertListEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])

    def test_edge_case_with_zeros(self):
        self.assertListEqual(sort_array([0, 0, 0]), [0, 0, 0])

    def test_edge_case_with_single_element(self):
        self.assertListEqual(sort_array([1]), [1])

    def test_large_input(self):
        large_arr = [i for i in range(10**7)]
        expected_sorted = sorted(large_arr)
        self.assertListEqual(sort_array(large_arr), expected_sorted)

    def test_empty_array(self):
        self.assertListEqual(sort_array([]), [])

    def test_duplicate_values(self):
        arr = [1, 2, 2, 3, 3, 3]
        expected_sorted = [1, 2, 2, 3, 3, 3]
        self.assertListEqual(sort_array(arr), expected_sorted)

if __name__ == '__main__':
    unittest.main()