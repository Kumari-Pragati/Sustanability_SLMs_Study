You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
from typing import List


class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_mean_absolute_deviation_with_zeros(self):
        self.assertEqual(mean_absolute_deviation([0.0, 0.0, 0.0, 0.0]), 0.0)

    def test_mean_absolute_deviation_with_single_number(self):
        self.assertEqual(mean_absolute_deviation([1.0]), 0.0)

    def test_mean_absolute_deviation_with_even_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    def test_mean_absolute_deviation_with_odd_numbers(self):
        self.assertEqual(mean_absolute_deviation([1.0, 3.0, 5.0, 7.0]), 2.0)

    def test_mean_absolute_deviation_with_negative_numbers(self):
        self.assertEqual(mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]), 1.0)

    def test_mean_absolute_deviation_with_mixed_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, -2.0, 3.0, -4.0]), 2.5)

    def test_mean_absolute_deviation_with_large_numbers(self):
        self.assertEqual(mean_absolute_deviation([1000.0, 2000.0, 3000.0, 4000.0]), 1000.0)

    def test_mean_absolute_deviation_with_floats(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]), 1.0)

    def test_mean_absolute_deviation_with_empty_list(self):
        with self.assertRaises(ZeroDivisionError):
            mean_absolute_deviation([])

    def test_mean_absolute_deviation_with_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            mean_absolute_deviation(['a', 'b', 'c'])

if __name__ == '__main__':
    unittest.main()