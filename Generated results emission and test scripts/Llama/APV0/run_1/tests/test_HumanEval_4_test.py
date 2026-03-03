user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_4_code import mean_absolute_deviation
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a center point (mean in this case):
    MAD = average |x - x_mean|
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)assistant

Here is a unittest test script for the given Python function:

Python
import unittest
from HumanEval_4_code import mean_absolute_deviation

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_mean_absolute_deviation(self):
        # Test with a list of numbers
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, 0.0, 1.0, 2.0]), 0.5)
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 1.0, 1.0, 1.0]), 0.0)
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, -1.0, -1.0, -1.0]), 1.0)
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]), 1.25)
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0, -5.0]), 1.25)

        # Test with an empty list
        self.assertRaises(ZeroDivisionError, mean_absolute_deviation, [])

        # Test with a list containing non-numeric values
        self.assertRaises(TypeError, mean_absolute_deviation, [1, 2, 'a', 4, 5])

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to ensure the function works correctly for different types of input. It also includes tests for edge cases, such as an empty list and a list containing non-numeric values.