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
    return [(x - min_number) / (max_number - min_number) for x in numbers]assistant

Here is the unittest test script for the `rescale_to_unit` function:

import unittest
from HumanEval_21_code import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):
    def test_rescale_to_unit(self):
        # Test with a simple list of numbers
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

        # Test with a list of negative numbers
        numbers = [-1.0, -2.0, -3.0, -4.0, -5.0]
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

        # Test with a list of mixed positive and negative numbers
        numbers = [-1.0, 0.0, 1.0, 2.0, 3.0]
        expected_result = [0.0, 0.5, 1.0, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

        # Test with a list of identical numbers
        numbers = [1.0, 1.0, 1.0, 1.0, 1.0]
        expected_result = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

        # Test with an empty list
        numbers = []
        with self.assertRaises(ValueError):
            rescale_to_unit(numbers)

        # Test with a list with only one element
        numbers = [1.0]
        with self.assertRaises(ValueError):
            rescale_to_unit(numbers)

if __name__ == '__main__':
    unittest.main()

This test script covers the following scenarios:

1. A simple list of numbers
2. A list of negative numbers
3. A list of mixed positive and negative numbers
4. A list of identical numbers
5. An empty list
6. A list with only one element

The `assertEqual` method is used to check if the output of the `rescale_to_unit` function matches the expected result. The `assertRaises` method is used to check if the function raises a `ValueError` when given an empty or single-element list.