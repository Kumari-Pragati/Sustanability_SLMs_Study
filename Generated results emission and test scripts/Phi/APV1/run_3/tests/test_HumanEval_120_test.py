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
    return ans

 import unittest
from HumanEval_120_code import maximum

class TestMaximumFunction(unittest.TestCase):

    def test_maximum_with_negative_numbers(self):
        self.assertEqual(maximum([-3, -4, 5], 3), [-4, -3, 5])

    def test_maximum_with_positive_numbers(self):
        self.assertEqual(maximum([4, -4, 4], 2), [4, 4])

    def test_maximum_with_single_element(self):
        self.assertEqual(maximum([-3, 2, 1, 2, -1, -2, 1], 1), [2])

    def test_maximum_with_empty_array(self):
        self.assertEqual(maximum([], 0), [])

    def test_maximum_with_k_greater_than_array_length(self):
        self.assertEqual(maximum([1, 2, 3], 5), [3, 2, 1])

    def test_maximum_with_k_equal_to_array_length(self):
        self.assertEqual(maximum([1, 2, 3], 3), [3, 2, 1])

    def test_maximum_with_k_less_than_one(self):
        self.assertEqual(maximum([1, 2, 3], 0), [])

    def test_maximum_with_all_negative_numbers(self):
        self.assertEqual(maximum([-1000, -999, -998], 3), [-998, -999, -1000])

    def test_maximum_with_all_positive_numbers(self):
        self.assertEqual(maximum([1000, 999, 998], 3), [1000, 999, 998])

    def test_maximum_with_mixed_numbers(self):
        self.assertEqual(maximum([-1000, 1000, -999, 999], 2), [999, 1000])

if __name__ == '__main__':
    unittest.main()