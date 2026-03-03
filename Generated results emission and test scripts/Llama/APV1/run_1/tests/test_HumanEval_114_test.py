user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_114_code import minSubArraySum

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    max_sum = 0
    s = 0
    for num in nums:
        s += -num
        if s < 0:
            s = 0
        max_sum = max(s, max_sum)
    if max_sum == 0:
        max_sum = max(-i for i in nums)
    min_sum = -max_sum
    return min_sumassistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_114_code import minSubArraySum

class TestMinSubArraySum(unittest.TestCase):

    def test_minSubArraySum(self):
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)
        self.assertEqual(minSubArraySum([1, 2, 3, 4, 5]), 1)
        self.assertEqual(minSubArraySum([-1, 0, 1, 2, -1]), -1)
        self.assertEqual(minSubArraySum([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(minSubArraySum([1, 2, 3, 4, 5, 6]), 1)
        self.assertEqual(minSubArraySum([-1, -2, -3, -4, -5, -6]), -6)
        self.assertEqual(minSubArraySum([1, 1, 1, 1, 1]), 1)
        self.assertEqual(minSubArraySum([-1, -1, -1, -1, -1]), -5)
        self.assertEqual(minSubArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)
        self.assertEqual(minSubArraySum([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), -10)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure the function is working correctly. It tests the function with both positive and negative numbers, as well as with single-digit and multi-digit numbers. It also tests the function with edge cases, such as an array with all the same numbers, or an array with all negative numbers.