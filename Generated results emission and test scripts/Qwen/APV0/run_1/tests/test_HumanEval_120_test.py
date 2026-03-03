system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


assistant

import unittest

# Function to be tested
from HumanEval_120_code import maximum

class TestMaximum(unittest.TestCase):
    def test_maximum(self):
        # Test case 1
        self.assertEqual(maximum([-3, -4, 5], 3), [-4, -3, 5])
        
        # Test case 2
        self.assertEqual(maximum([4, -4, 4], 2), [4, 4])
        
        # Test case 3
        self.assertEqual(maximum([-3, 2, 1, 2, -1, -2, 1], 1), [2])

    def test_empty_array(self):
        self.assertEqual(maximum([], 3), [])

    def test_k_zero(self):
        self.assertEqual(maximum([1, 2, 3], 0), [])

    def test_large_input(self):
        large_arr = [i for i in range(-1000, 1001)]
        self.assertEqual(maximum(large_arr, 1000), large_arr[:1000])

if __name__ == '__main__':
    unittest.main()


This script defines a `TestMaximum` class that inherits from `unittest.TestCase`. It contains several test methods to verify the correctness of the `maximum` function. Each method calls the `maximum` function with different inputs and checks if the output matches the expected result using assertions. The `if __name__ == '__main__':` block ensures that the tests can be run directly when the script is executed.