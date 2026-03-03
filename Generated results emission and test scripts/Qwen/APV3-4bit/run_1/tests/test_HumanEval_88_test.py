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
   - Include from HumanEval_88_code import sort_array
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
2. Include: from HumanEval_88_code import sort_array
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting.
    You will sort the given array in ascending order if the sum(first index value, last index value) is odd,
    or sort it in descending order if the sum(first index value, last index value) is even.

    Note:
    * Don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """

    return [] if len(array) == 0 else sorted(array, reverse=(array[0] + array[-1]) % 2 == 0)


assistant

import unittest

# Importing the function we want to test
from HumanEval_88_code import sort_array

class TestSortArray(unittest.TestCase):
    
    # Test case for empty array
    def test_sort_array_empty(self):
        result = sort_array([])
        expected_result = []
        self.assertEqual(result, expected_result)
        
    # Test case for single element array
    def test_sort_array_single_element(self):
        result = sort_array([5])
        expected_result = [5]
        self.assertEqual(result, expected_result)
        
    # Test case for two elements array
    def test_sort_array_two_elements(self):
        result = sort_array([2, 4, 3, 0, 1, 5])
        expected_result = [0, 1, 2, 3, 4, 5]
        self.assertEqual(result, expected_result)
        
    # Test case for three elements array
    def test_sort_array_three_elements(self):
        result = sort_array([2, 4, 3, 0, 1, 5, 6])
        expected_result = [6, 5, 4, 3, 2, 1, 0]
        self.assertEqual(result, expected_result)
        
    # Test case for four elements array
    def test_sort_array_four_elements(self):
        result = sort_array([1, 2, 3, 4])
        expected_result = [1, 2, 3, 4]
        self.assertEqual(result, expected_result)
        
    # Test case for five elements array
    def test_sort_array_five_elements(self):
        result = sort_array([5, 4, 3, 2, 1])
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected_result)
        
    # Test case for six elements array
    def test_sort_array_six_elements(self):
        result = sort_array([1, 2, 3, 4, 5, 6])
        expected_result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(result, expected_result)
        
    # Test case for seven elements array
    def test_sort_array_seven_elements(self):
        result = sort_array([7, 6, 5, 4, 3, 2, 1])
        expected_result = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(result, expected_result)
        
    # Test case for eight elements array
    def test_sort_array_eight_elements(self):
        result = sort_array([8, 7, 6, 5, 4, 3, 2, 1])
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(result, expected_result)
        
    # Test case for nine elements array
    def test_sort_array_nine_elements(self):
        result = sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1])
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(result, expected_result)
        
    # Test case for ten elements array
    def test_sort_array_ten_elements(self):
        result = sort_array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(result, expected_result)
        
    # Test case for eleven elements array
    def test_sort_array_eleven_elements(self):
        result = sort_array([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.assertEqual(result, expected_result)
        
    # Test case for twelve elements array
    def test_sort_array_twelve_elements(self):
        result = sort_array([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,