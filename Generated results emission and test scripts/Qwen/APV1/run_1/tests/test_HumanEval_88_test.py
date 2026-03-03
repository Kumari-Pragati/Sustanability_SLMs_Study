system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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

    return [] if len(array) == 0 else sorted(array, reverse=(array[0] + array[-1]) % 2 == 0)


assistant

import unittest
from HumanEval_88_code import sort_array

class TestSortArray(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(sort_array([]), [])

    def test_single_element(self):
        self.assertEqual(sort_array([5]), [5])

    def test_sorted_increasing(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])

    def test_sorted_decreasing(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])

    def test_mixed_values(self):
        self.assertEqual(sort_array([7, 1, 5, 3, 9, 2]), [1, 2, 3, 5, 7, 9])

    def test_odd_sum_first_last(self):
        self.assertEqual(sort_array([1, 2, 3, 4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_even_sum_first_last(self):
        self.assertEqual(sort_array([1, 2, 3, 4, 5, 6, 7]), [7, 6, 5, 4, 3, 2, 1])

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestSortArray` class that inherits from `unittest.TestCase`. It contains several test methods to verify the correctness of the `sort_array` function. Each method tests different scenarios and compares the output against expected results using assertions. The `if __name__ == '__main__':` block ensures that when this script is run directly, all the test cases are executed.