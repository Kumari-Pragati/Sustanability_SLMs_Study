system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_22_code import filter_integers
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """Filter given list of any Python values only for integers.
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [x for x in values if isinstance(x, int)]


assistant

import unittest

# Importing the function to be tested
from HumanEval_22_code import filter_integers

class TestFilterIntegers(unittest.TestCase):
    def test_filter_integers(self):
        # Test case 1: Filter out non-integer values
        self.assertEqual(filter_integers(['a', 3.14, 5]), [5])

        # Test case 2: Filter out mixed types
        self.assertEqual(filter_integers([1, 2, 3, 'abc', {}, []]), [1, 2, 3])

        # Test case 3: Empty list
        self.assertEqual(filter_integers([]), [])

        # Test case 4: Single integer value
        self.assertEqual(filter_integers([7]), [7])

        # Test case 5: Mixed types including strings
        self.assertEqual(filter_integers(['hello', 99, True, None, [], {}]), [99])

if __name__ == '__main__':
    unittest.main()


This script imports the `filter_integers` function and defines a test class `TestFilterIntegers` that contains several test cases using the `assertEqual` method to verify the correctness of the function. The `unittest.main()` call at the end makes the tests executable when run as a standalone script.