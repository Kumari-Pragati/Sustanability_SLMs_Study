system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_42_code import incr_list

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    return [e + 1 for e in l]


assistant

import unittest

# Function to be tested
from HumanEval_42_code import incr_list

class TestIncrList(unittest.TestCase):

    def test_incr_list(self):
        self.assertEqual(incr_list([1, 2, 3]), [2, 3, 4], "Test case 1 failed")
        self.assertEqual(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]), [6, 4, 6, 3, 4, 4, 10, 1, 124], "Test case 2 failed")

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `unittest` test case class named `TestIncrList`. It includes two test cases that check if the `incr_list` function returns the expected results when called with different input lists. The `assertEqual` method is used to verify that the output of `incr_list` matches the expected values. If any of these tests fail, the corresponding assertion will raise an error message indicating which test case failed and what the expected result was.