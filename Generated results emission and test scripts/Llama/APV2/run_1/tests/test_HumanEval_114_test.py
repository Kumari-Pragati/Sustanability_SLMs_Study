system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_114_code import minSubArraySum

class TestMinSubArraySum(unittest.TestCase):

    def test_minSubArraySum(self):
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)
        self.assertEqual(minSubArraySum([1, 2, 3, 4, 5]), 1)
        self.assertEqual(minSubArraySum([-1, 0, 1, 2, -3]), -1)
        self.assertEqual(minSubArraySum([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(minSubArraySum([1, 2, 3, 4, 5, 6]), 1)
        self.assertEqual(minSubArraySum([-1, -2, -3, -4, -5, -6]), -6)

if __name__ == '__main__':
    unittest.main()