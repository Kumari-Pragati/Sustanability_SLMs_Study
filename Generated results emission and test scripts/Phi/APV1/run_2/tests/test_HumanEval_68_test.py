You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_68_code import pluck

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def pluck(arr):
    """
    Given an array representing a branch of a tree that has non-negative integer nodes,
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found, return the node that has the smallest index.

    The plucked node should be returned in a list, [smallest_value, its index].
    If there are no even values or the given array is empty, return [].

    Example 1:
        Input: [4, 2, 3]
        Output: [2, 1]

    Example 2:
        Input: [1, 2, 3]
        Output: [2, 1]

    Example 3:
        Input: []
        Output: []

    Example 4:
        Input: [5, 0, 3, 0, 4, 2]
        Output: [0, 1]

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """
    if len(arr) == 0:
        return []
    evens = list(filter(lambda x: x % 2 == 0, arr))
    if evens == []:
        return []
    return [min(evens), arr.index(min(evens))]

 
import unittest
from HumanEval_68_code import pluck

class TestPluckFunction(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(pluck([]), [])

    def test_no_even_values(self):
        self.assertEqual(pluck([1, 3, 5]), [])

    def test_single_even_value(self):
        self.assertEqual(pluck([2]), [2, 0])

    def test_multiple_even_values_smallest_index(self):
        self.assertEqual(pluck([4, 2, 3]), [2, 1])

    def test_multiple_even_values_smallest_value(self):
        self.assertEqual(pluck([4, 2, 2]), [2, 1])

    def test_multiple_even_values_same_smallest_value_smallest_index(self):
        self.assertEqual(pluck([2, 2, 0]), [0, 2])

    def test_multiple_even_values_same_smallest_value_non_first_index(self):
        self.assertEqual(pluck([2, 0, 2]), [0, 1])

    def test_multiple_even_values_same_smallest_value_non_first_index_with_zeros(self):
        self.assertEqual(pluck([0, 2, 2]), [0, 0])

    def test_multiple_even_values_same_smallest_value_non_first_index_with_zeros_and_non_zero_elements(self):
        self.assertEqual(pluck([2, 0, 3]), [0, 1])

    def test_multiple_even_values_same_smallest_value_non_first_index_with_zeros_and_non_zero_elements_with_negative_values(self):
        self.assertEqual(pluck([-2, 0, 3]), [-2, 0])

    def test_multiple_even_values_same_smallest_value_non_first_index_with_zeros_and_non_zero_elements_with_negative_values_and_positive_values(self):
        self.assertEqual(pluck([-2, 0, 2]), [-2, 0])

    def test_multiple_even_values_same_smallest_value_non_first_index_with_zeros_and_non_zero_elements_with_negative_values_and_positive_values_with_large_numbers(self):
        self.assertEqual(pluck([-2, 0, 1000000]), [-2, 0])

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios for the `pluck` function, including empty arrays, arrays without even values, arrays with a single even value, arrays with multiple even values, and arrays with both even and odd values. It also tests the function's ability to return the correct index of the smallest even value. The tests are designed to ensure that the function behaves as expected under different conditions.