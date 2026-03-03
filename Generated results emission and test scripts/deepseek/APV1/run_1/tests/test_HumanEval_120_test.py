You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_120_code import maximum

class TestMaximum(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(maximum([], 3), [])

    def test_k_equals_zero(self):
        self.assertEqual(maximum([1, 2, 3], 0), [])

    def test_k_equals_length_of_array(self):
        self.assertEqual(maximum([1, 2, 3], 3), [1, 2, 3])

    def test_k_less_than_length_of_array(self):
        self.assertEqual(maximum([1, 2, 3, 4, 5], 3), [1, 2, 3])

    def test_negative_numbers(self):
        self.assertEqual(maximum([-3, -4, 5], 3), [-4, -3, 5])

    def test_positive_numbers(self):
        self.assertEqual(maximum([4, -4, 4], 2), [4, 4])

    def test_mixed_numbers(self):
        self.assertEqual(maximum([-3, 2, 1, 2, -1, -2, 1], 1), [2])

    def test_large_numbers(self):
        self.assertEqual(maximum([1000, -1000, 0], 2), [1000, 0])

    def test_large_array(self):
        arr = list(range(1000))
        self.assertEqual(maximum(arr, 100), list(range(1000, 900, -1)))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various edge cases, such as an empty array, k equals to zero, k equals to the length of the array, k less than the length of the array, negative numbers, positive numbers, mixed numbers, large numbers, and a large array.