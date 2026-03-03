You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_114_code import minSubArraySum

class TestMinSubArraySum(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)

    def test_negative_numbers(self):
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)

    def test_single_number(self):
        self.assertEqual(minSubArraySum([5]), 5)

    def test_empty_array(self):
        self.assertEqual(minSubArraySum([]), 0)

    def test_all_negative_numbers(self):
        self.assertEqual(minSubArraySum([-1, -2, -3, -4]), -1)

    def test_all_positive_numbers(self):
        self.assertEqual(minSubArraySum([1, 2, 3, 4]), 1)

    def test_mixed_numbers(self):
        self.assertEqual(minSubArraySum([-2, 1, -3, 4]), 1)

if __name__ == '__main__':
    unittest.main()


This script includes a series of test cases to cover different scenarios, such as positive numbers, negative numbers, single number, empty array, all negative numbers, all positive numbers, and mixed numbers. Each test case checks if the function returns the correct minimum sum of any non-empty sub-array of the given array.