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

 Here is a unittest test script for the `rescale_to_unit` function:


import unittest
from HumanEval_21_code import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):
    def test_rescale_to_unit(self):
        self.assertEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
        self.assertEqual(rescale_to_unit([0.0, 1.0, 2.0, 3.0, 4.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
        self.assertEqual(rescale_to_unit([-1.0, 0.0, 1.0, 2.0, 3.0]), [-1.0, 0.0, 0.33333333333333336, 0.6666666666666667, 1.0])
        self.assertEqual(rescale_to_unit([1.0]), [0.0])
        self.assertEqual(rescale_to_unit([5.0]), [1.0])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to ensure the function works correctly for different input scenarios. The test cases cover the following cases:

1. A list with positive numbers in increasing order.
2. A list with positive numbers in decreasing order.
3. A list with both positive and negative numbers.
4. A list with only one number.
5. A list with only the maximum number.

You can run this script directly by saving it as a .py file and running it using the command `python filename.py` in your terminal.