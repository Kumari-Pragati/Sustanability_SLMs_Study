You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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
    return min_sum


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_114_code import minSubArraySum

class TestMinSubArraySum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)

    def test_negative_numbers(self):
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)

    def test_single_number(self):
        self.assertEqual(minSubArraySum([1]), 1)

    def test_zeroes(self):
        self.assertEqual(minSubArraySum([0, 0, 0]), 0)

    def test_empty_list(self):
        self.assertEqual(minSubArraySum([]), 0)

    def test_large_numbers(self):
        self.assertEqual(minSubArraySum([1000, 2000, 3000]), 1000)

    def test_negative_and_positive(self):
        self.assertEqual(minSubArraySum([-1, 2, -3, 4]), 1)

    def test_all_negative(self):
        self.assertEqual(minSubArraySum([-1, -2, -3, -4]), -1)

    def test_all_positive(self):
        self.assertEqual(minSubArraySum([1, 2, 3, 4]), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure the function is working correctly. It tests with positive numbers, negative numbers, a single number, zeroes, an empty list, large numbers, a mix of negative and positive numbers, all negative numbers, and all positive numbers.