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
    return sum(abs(x - mean) for x in numbers) / len(numbers)

 import unittest
from HumanEval_4_code import mean_absolute_deviation

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_mean_absolute_deviation_zero(self):
        self.assertEqual(mean_absolute_deviation([0.0]), 0.0)

    def test_mean_absolute_deviation_single_number(self):
        self.assertEqual(mean_absolute_deviation([10.0]), 0.0)

    def test_mean_absolute_deviation_identical_numbers(self):
        self.assertEqual(mean_absolute_deviation([5.0, 5.0, 5.0]), 0.0)

    def test_mean_absolute_deviation_simple_list(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    def test_mean_absolute_deviation_negative_numbers(self):
        self.assertEqual(mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]), 1.0)

    def test_mean_absolute_deviation_mixed_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, -2.0, 3.0, -4.0]), 2.5)

    def test_mean_absolute_deviation_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            mean_absolute_deviation([])

    def test_mean_absolute_deviation_non_float_list(self):
        with self.assertRaises(TypeError):
            mean_absolute_deviation([1, 2, 3])

if __name__ == '__main__':
    unittest.main()