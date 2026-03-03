You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

    def test_mean_absolute_deviation_with_zero_variation(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    def test_mean_absolute_deviation_with_negative_values(self):
        self.assertEqual(mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]), 1.0)

    def test_mean_absolute_deviation_with_positive_values(self):
        self.assertEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    def test_mean_absolute_deviation_with_single_value(self):
        self.assertEqual(mean_absolute_deviation([5.0]), 0.0)

    def test_mean_absolute_deviation_with_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

    def test_mean_absolute_deviation_with_non_numeric_values(self):
        with self.assertRaises(TypeError):
            mean_absolute_deviation(['a', 'b', 'c'])

    def test_mean_absolute_deviation_with_large_numbers(self):
        self.assertEqual(mean_absolute_deviation([1000000.0, 2000000.0, 3000000.0, 4000000.0]), 1000000.0)

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios for the `mean_absolute_deviation` function, including:

- A basic test with a simple list of numbers.
- Tests with negative values to ensure the function handles them correctly.
- A test with a list containing a single value to check the behavior when there is no variation.
- A test with an empty list to ensure the function returns 0.
- A test that expects a `TypeError` when non-numeric values are passed to the function.
- A test with a list of large numbers to ensure the function calculates the MAD correctly.

Each test case is designed to verify the correctness of the `mean_absolute_deviation` function under different conditions. The `unittest` framework is used to automate the test execution and report any failures.