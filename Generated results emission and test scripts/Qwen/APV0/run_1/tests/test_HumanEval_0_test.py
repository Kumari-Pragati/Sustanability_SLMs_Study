system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_0_code import has_close_elements
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True
    return False


assistant

import unittest

# Importing the function from the provided code snippet
from HumanEval_0_code import has_close_elements

class TestHasCloseElements(unittest.TestCase):
    def test_case_1(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0], 0.5))

    def test_case_2(self):
        self.assertTrue(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))

    def test_case_3(self):
        self.assertFalse(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.6))

    def test_case_4(self):
        self.assertTrue(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.1))

if __name__ == '__main__':
    unittest.main()


This script imports the `has_close_elements` function from the provided code snippet and defines several test cases using the `unittest` framework. Each test case checks whether the function returns the expected boolean value based on the input parameters. The `unittest.main()` call at the end makes the tests executable when run as a standalone script.