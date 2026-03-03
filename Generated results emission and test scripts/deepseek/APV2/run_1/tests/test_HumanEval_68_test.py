You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a unittest test suite for the given function:


import unittest
from HumanEval_68_code import pluck

class TestPluck(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(pluck([]), [])

    def test_no_even_values(self):
        self.assertEqual(pluck([1, 3, 5]), [])

    def test_single_even_value(self):
        self.assertEqual(pluck([4]), [4, 0])

    def test_multiple_even_values(self):
        self.assertEqual(pluck([4, 2, 3]), [2, 1])

    def test_even_values_with_different_indices(self):
        self.assertEqual(pluck([5, 0, 3, 0, 4, 2]), [0, 1])

    def test_even_values_with_same_smallest(self):
        self.assertEqual(pluck([2, 4, 6]), [2, 0])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for all the edge cases and normal scenarios. It checks if the function returns the correct result for an empty array, an array with no even values, an array with a single even value, an array with multiple even values, an array with even values at different indices, and an array with even values that have the same smallest value.