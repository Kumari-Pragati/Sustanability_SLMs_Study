user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_114_code import minSubArraySum

class TestMinSubArraySum(unittest.TestCase):

    def test_minSubArraySum(self):
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)
        self.assertEqual(minSubArraySum([1, 2, 3, 4, 5]), 1)
        self.assertEqual(minSubArraySum([-1, 0, 1, 2, -1]), -1)
        self.assertEqual(minSubArraySum([1, -2, 3, -4, 5]), -6)
        self.assertEqual(minSubArraySum([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(minSubArraySum([1, 1, 1, 1, 1]), 1)
        self.assertEqual(minSubArraySum([-1, -1, -1, -1, -1]), -1)
        self.assertEqual(minSubArraySum([0, 0, 0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()


This script includes 9 test cases to cover different scenarios. The `assertEqual` method is used to compare the output of the function with the expected output. If the output is not as expected, the test will fail and an error message will be displayed.