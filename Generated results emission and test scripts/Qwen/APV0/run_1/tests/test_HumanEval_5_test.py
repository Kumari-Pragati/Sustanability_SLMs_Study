system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_5_code import intersperse
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result: List[int] = []
    for i, x in enumerate(numbers):
        result.append(x)
        if i != len(numbers) - 1:
            result.append(delimeter)
    return result


assistant

import unittest

# Importing the function to be tested
from HumanEval_5_code import intersperse

class TestIntersperse(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(intersperse([], 4), [])

    def test_single_element_list(self):
        self.assertEqual(intersperse([1, 2, 3], 4), [1, 4, 2, 4, 3])

    def test_multiple_elements_list(self):
        self.assertEqual(intersperse([10, 20, 30, 40], 5), [10, 5, 20, 5, 30, 5, 40])

if __name__ == '__main__':
    unittest.main()


This script imports the necessary module, defines a class `TestIntersperse` that inherits from `unittest.TestCase`, and includes three test methods (`test_empty_list`, `test_single_element_list`, and `test_multiple_elements_list`) to verify the functionality of the `intersperse` function using assertions. The `unittest.main()` call at the end makes the tests executable when run as a standalone script.