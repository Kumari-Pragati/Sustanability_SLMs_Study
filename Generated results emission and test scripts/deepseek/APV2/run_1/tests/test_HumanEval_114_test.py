You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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
    return min_sum


### Response:
Here is a unittest test suite for the given function:


import unittest
from HumanEval_114_code import minSubArraySum

class TestMinSubArraySum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)

    def test_negative_numbers(self):
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)

    def test_single_number(self):
        self.assertEqual(minSubArraySum([5]), 5)

    def test_empty_list(self):
        self.assertEqual(minSubArraySum([]), 0)

    def test_large_numbers(self):
        self.assertEqual(minSubArraySum([1000, 2000, 3000]), 1000)

    def test_all_negative_numbers(self):
        self.assertEqual(minSubArraySum([-1, -2, -3, -4]), -1)

    def test_all_positive_numbers(self):
        self.assertEqual(minSubArraySum([1, 2, 3, 4]), 1)

    def test_mixed_numbers(self):
        self.assertEqual(minSubArraySum([-1, 2, -3, 4]), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios such as positive numbers, negative numbers, single number, empty list, large numbers, all negative numbers, all positive numbers, and mixed numbers.