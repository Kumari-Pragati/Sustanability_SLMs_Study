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
    return min_sum

 Here is a unittest test script for the provided function `minSubArraySum`. The test cases cover various scenarios such as empty list, positive numbers, negative numbers, and a mix of positive and negative numbers.


import unittest
from HumanEval_114_code import minSubArraySum

class TestMinSubArraySum(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(minSubArraySum([]), 0)

    def test_positive_numbers(self):
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)

    def test_negative_numbers(self):
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(minSubArraySum([-1, 2, -3, 4]), 1)

    def test_single_number(self):
        self.assertEqual(minSubArraySum([-1]), -1)

    def test_large_array(self):
        nums = [-100000, -99999, -99998, -99997, -99996, -99995, -99994, -99993, -99992, -99991]
        self.assertEqual(minSubArraySum(nums), -100000)

if __name__ == '__main__':
    unittest.main()


Save this script as `test_minSubArraySum.py` and run it using the command `python test_minSubArraySum.py`. The test cases will be executed, and you should see the output indicating whether the tests passed or failed.