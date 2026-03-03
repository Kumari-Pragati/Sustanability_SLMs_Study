user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_88_code import sort_array

class TestSortArray(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(sort_array([]), [])

    def test_single_element_array(self):
        self.assertEqual(sort_array([5]), [5])

    def test_even_sum_array(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])

    def test_odd_sum_array(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])

    def test_array_with_duplicates(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 5]), [0, 1, 2, 3, 4, 5, 5])

    def test_array_with_negative_numbers(self):
        with self.assertRaises(TypeError):
            sort_array([-1, 0, 1])

    def test_array_with_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            sort_array([1.5, 2.5, 3.5])

    def test_array_with_mixed_types(self):
        with self.assertRaises(TypeError):
            sort_array([1, 2, 'a', 3, 4])

if __name__ == '__main__':
    unittest.main()


This test suite covers the following scenarios:

1.  An empty array
2.  A single-element array
3.  An array with an even sum of the first and last elements
4.  An array with an odd sum of the first and last elements
5.  An array with duplicate elements
6.  An array with negative numbers
7.  An array with non-integer numbers
8.  An array with mixed types