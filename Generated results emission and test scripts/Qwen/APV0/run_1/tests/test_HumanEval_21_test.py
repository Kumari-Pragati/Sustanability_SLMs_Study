system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_21_code import rescale_to_unit
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]


assistant

import unittest

# Importing the function from the given code snippet
from HumanEval_21_code import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):
    def test_rescale_to_unit(self):
        # Test case 1: Normal input
        result = rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(result, expected_result)

        # Test case 2: Single element input
        result = rescale_to_unit([10.0])
        expected_result = [0.0]
        self.assertEqual(result, expected_result)

        # Test case 3: Empty list input
        result = rescale_to_unit([])
        expected_result = []
        self.assertEqual(result, expected_result)

        # Test case 4: All elements equal
        result = rescale_to_unit([1.0] * 5)
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(result, expected_result)

        # Test case 5: Negative values
        result = rescale_to_unit([-1.0, 0.0, 1.0])
        expected_result = [-0.5, 0.0, 0.5]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()


This script defines a `TestRescaleToUnit` class within the `unittest` module, which contains several test cases to verify the correctness of the `rescale_to_unit` function. The tests cover various scenarios including normal inputs, single-element inputs, empty lists, all elements being equal, and negative values. If any of these test cases fail, an assertion error will be raised indicating what went wrong.