system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return min_sum


assistant

import unittest

# Function to be tested
from HumanEval_114_code import minSubArraySum

class TestMinSubArraySum(unittest.TestCase):

    def test_minSubArraySum(self):
        self.assertEqual(minSubArraySum([2, 3, 4, 1, 2, 4]), 1)
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)
        self.assertEqual(minSubArraySum([1, 2, 3, -6, 4]), -6)
        self.assertEqual(minSubArraySum([5, 8, 7, 9, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]), 1)

    def test_empty_array(self):
        self.assertEqual(minSubArraySum([]), None)  # or raise ValueError if you want to enforce this case

    def test_all_negative_numbers(self):
        self.assertEqual(minSubArraySum([-1, -2, -3]), -6)

    def test_all_positive_numbers(self):
        self.assertEqual(minSubArraySum([1, 2, 3, 4, 5]), 1)

    def test_large_numbers(self):
        self.assertEqual(minSubArraySum([1000, 2000, 3000, 4000, 5000]), 1000)

if __name__ == '__main__':
    unittest.main()


This script defines a `TestMinSubArraySum` class that inherits from `unittest.TestCase`. It includes several test cases to verify the correctness of the `minSubArraySum` function. The `test_empty_array`, `test_all_negative_numbers`, `test_all_positive_numbers`, and `test_large_numbers` methods cover various scenarios including empty arrays, all negative numbers, all positive numbers, and large numbers respectively. The `test_minSubArraySum` method tests the function against the provided examples. Finally, the `if __name__ == '__main__':` block runs the tests when the script is executed directly.