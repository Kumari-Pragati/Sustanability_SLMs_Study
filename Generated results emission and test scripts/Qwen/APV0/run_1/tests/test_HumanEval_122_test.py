system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_122_code import add_elements
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add_elements(arr, k):
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

        Input: arr = [111, 21, 3, 4000, 5, 6, 7, 8, 9], k = 4
        Output: 24 # sum of 21 + 3

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """
    return sum(elem for elem in arr[:k] if len(str(elem)) <= 2)


assistant

import unittest

# Function to be tested
from HumanEval_122_code import add_elements

class TestAddElements(unittest.TestCase):
    def test_add_elements(self):
        self.assertEqual(add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4), 24)
        self.assertEqual(add_elements([10, 20, 30, 40, 50], 3), 60)
        self.assertEqual(add_elements([1, 2, 3, 4, 5], 5), 15)
        self.assertEqual(add_elements([], 2), 0)
        self.assertEqual(add_elements([100, 200, 300], 2), 300)
        self.assertEqual(add_elements([-1, -2, -3, -4, -5], 2), -3)

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a test case class `TestAddElements`. It includes several test cases that cover various scenarios as specified in the problem description. The `test_add_elements` method checks the correctness of the `add_elements` function using assertions. If any assertion fails, it will raise an error indicating which test failed.