You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_88_code import sort_array

class TestSortArray(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(sort_array([]), [])

    def test_single_element_array(self):
        self.assertEqual(sort_array([5]), [5])

    def test_even_sum_of_first_and_last(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])

    def test_odd_sum_of_first_and_last(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])

    def test_same_elements(self):
        self.assertEqual(sort_array([1, 1, 1, 1]), [1, 1, 1, 1])

    def test_negative_numbers(self):
        self.assertEqual(sort_array([-1, -2, -3, -4]), [-4, -3, -2, -1])

    def test_mixed_numbers(self):
        self.assertEqual(sort_array([-1, 2, -3, 4]), [4, 2, -1, -3])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- An empty array
- An array with a single element
- An array where the sum of the first and last elements is even
- An array where the sum of the first and last elements is odd
- An array with all the same elements
- An array with negative numbers
- An array with a mix of positive and negative numbers

Each test checks that the function returns the correct sorted array for the given input.