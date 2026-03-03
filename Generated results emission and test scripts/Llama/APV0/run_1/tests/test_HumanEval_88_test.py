user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

    return [] if len(array) == 0 else sorted(array, reverse=(array[0] + array[-1]) % 2 == 0)assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_88_code import sort_array

class TestSortArray(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(sort_array([]), [])

    def test_single_element_array(self):
        self.assertEqual(sort_array([5]), [5])

    def test_even_sum(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])

    def test_odd_sum(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])

    def test_array_with_duplicates(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 5]), [0, 1, 2, 3, 4, 5, 5])

    def test_array_with_negative_numbers(self):
        self.assertEqual(sort_array([-2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])

    def test_array_with_zero(self):
        self.assertEqual(sort_array([0, 1, 2, 3, 4, 5]), [0, 1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()


This script includes 6 test cases to cover different scenarios:

- An empty array
- A single-element array
- An array with an even sum
- An array with an odd sum
- An array with duplicates
- An array with negative numbers

Each test case checks if the output of the `sort_array` function matches the expected output.