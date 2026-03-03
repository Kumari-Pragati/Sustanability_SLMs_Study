You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return ans

 Here is the complete unittest test suite for the provided `maximum` function:


import unittest
from HumanEval_120_code import maximum

class TestMaximum(unittest.TestCase):

    def test_example_1(self):
        self.assertListEqual(maximum([-3, -4, 5], 3), [-4, -3, 5])

    def test_example_2(self):
        self.assertListEqual(maximum([4, -4, 4], 2), [4, 4])

    def test_example_3(self):
        self.assertListEqual(maximum([-3, 2, 1, 2, -1, -2, 1], 1), [2])

    def test_empty_array(self):
        self.assertListEqual(maximum([], 3), [])

    def test_single_element(self):
        self.assertListEqual(maximum([1], 1), [1])

    def test_k_greater_than_array_length(self):
        self.assertListEqual(maximum([1, 2, 3], 4), [3, 2, 1])

    def test_negative_k(self):
        with self.assertRaises(ValueError):
            maximum([1, 2, 3], -1)

    def test_negative_numbers(self):
        self.assertListEqual(maximum([-1, -2, -3], 3), [-1, -2, -3])

    def test_positive_numbers(self):
        self.assertListEqual(maximum([1, 2, 3], 3), [3, 2, 1])

    def test_mixed_numbers(self):
        self.assertListEqual(maximum([-1, 2, 3], 2), [3, 2])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as empty arrays, single-element arrays, k greater than array length, negative k, negative numbers, positive numbers, and mixed numbers. It also tests the correctness of the sorted list returned by the function.