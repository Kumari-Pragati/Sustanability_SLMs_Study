system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
        self.assertEqual(add_elements([1, 2, 3, 4, 5, 6, 7, 8, 9], 8), 36)
        self.assertEqual(add_elements([], 0), 0)
        self.assertEqual(add_elements([100, 200, 300], 2), 300)
        print("All tests passed!")

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestAddElements` class that inherits from `unittest.TestCase`. It contains a single method `test_add_elements`, which uses assertions to verify the correctness of the `add_elements` function. The `assertEqual` method checks if the output of `add_elements` matches the expected result for various input scenarios. If all tests pass, it prints "All tests passed!" to indicate successful execution.