system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_47_code import median
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0


assistant

import unittest

# Importing the function to be tested
from HumanEval_47_code import median

class TestMedian(unittest.TestCase):

    def test_median(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

    def test_odd_length_list(self):
        self.assertEqual(median([1, 2, 3, 4, 5, 6]), 3.5)

    def test_even_length_list(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            median([])

if __name__ == '__main__':
    unittest.main()


This script imports the `median` function and defines several test cases using the `unittest` framework. It includes tests for both odd and even length lists as well as an empty list case to ensure robustness. The `assertEqual` method is used to check that the output matches the expected values, and the `with self.assertRaises(ValueError)` statement ensures that attempting to call the function on an empty list raises a ValueError.