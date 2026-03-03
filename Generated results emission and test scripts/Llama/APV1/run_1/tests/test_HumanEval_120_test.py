user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_120_code import maximum

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

        Input: arr = [-3, -4, 5], k = 3
        Output: [-4, -3, 5]

    Example 2:

        Input: arr = [4, -4, 4], k = 2
        Output: [4, 4]

    Example 3:

        Input: arr = [-3, 2, 1, 2, -1, -2, 1], k = 1
        Output: [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """
    if k == 0:
        return []
    arr.sort()
    ans = arr[-k:]
    return ansassistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_120_code import maximum

class TestMaximum(unittest.TestCase):

    def test_example1(self):
        arr = [-3, -4, 5]
        k = 3
        self.assertEqual(maximum(arr, k), [-4, -3, 5])

    def test_example2(self):
        arr = [4, -4, 4]
        k = 2
        self.assertEqual(maximum(arr, k), [4, 4])

    def test_example3(self):
        arr = [-3, 2, 1, 2, -1, -2, 1]
        k = 1
        self.assertEqual(maximum(arr, k), [2])

    def test_k_zero(self):
        arr = [1, 2, 3]
        k = 0
        self.assertEqual(maximum(arr, k), [])

    def test_k_greater_than_length(self):
        arr = [1, 2, 3]
        k = 5
        self.assertEqual(maximum(arr, k), [3, 2, 1])

    def test_k_equal_to_length(self):
        arr = [1, 2, 3]
        k = 3
        self.assertEqual(maximum(arr, k), [3, 2, 1])

    def test_negative_numbers(self):
        arr = [-10, -5, 0, 5, 10]
        k = 3
        self.assertEqual(maximum(arr, k), [10, 5, 0])

    def test_zero(self):
        arr = [0, 0, 0]
        k = 2
        self.assertEqual(maximum(arr, k), [0, 0])

    def test_all_negative(self):
        arr = [-10, -5, -3, -2, -1]
        k = 3
        self.assertEqual(maximum(arr, k), [-1, -2, -3])

    def test_all_positive(self):
        arr = [10, 5, 3, 2, 1]
        k = 3
        self.assertEqual(maximum(arr, k), [10, 5, 3])

if __name__ == '__main__':
    unittest.main()


This test suite covers various edge cases and scenarios, including:

- Example inputs from the problem statement
- Edge cases such as k = 0, k = length of array, and k = length of array + 1
- Test cases with negative numbers, zero, and all positive numbers
- Test cases with arrays of varying lengths

Each test case checks if the output of the `maximum` function matches the expected output.