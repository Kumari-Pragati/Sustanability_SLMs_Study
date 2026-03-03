system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_52_code import below_threshold
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for e in l:
        if e >= t:
            return False
    return True


assistant

import unittest

# Importing the function to be tested
from HumanEval_52_code import below_threshold

class TestBelowThreshold(unittest.TestCase):
    def test_below_threshold_true(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))

    def test_below_threshold_false(self):
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))

if __name__ == '__main__':
    unittest.main()


This script imports the `below_threshold` function from the `HumanEval_52_code` module and defines two test cases using the `unittest.TestCase` class. The first test case checks if the function returns `True` when all elements in the list are below the specified threshold, while the second test case checks if it returns `False`. Finally, the `unittest.main()` function runs all tests defined in the test suite.