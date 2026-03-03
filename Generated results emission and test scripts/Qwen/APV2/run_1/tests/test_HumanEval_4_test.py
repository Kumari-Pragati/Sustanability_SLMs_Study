system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
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


assistant

import unittest

# Provided function
from HumanEval_4_code import mean_absolute_deviation

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

    def test_single_element(self):
        self.assertEqual(mean_absolute_deviation([5.0]), 0.0)

    def test_uniform_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 0.5)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 3.0, 5.0, 7.0]), 2.0)

    def test_all_negative(self):
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, -3.0, -5.0, -7.0]), 3.0)

    def test_random_numbers(self):
        random_numbers = [round(random.uniform(-10, 10), 2) for _ in range(10)]
        self.assertAlmostEqual(mean_absolute_deviation(random_numbers), round(sum(abs(num - sum(random_numbers)/len(random_numbers))) / len(random_numbers), 2))

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to ensure the `mean_absolute_deviation` function works correctly under different conditions, including edge cases like empty lists and single-element lists. It also tests uniform distributions, mixed distributions, all negative values, and more complex scenarios involving randomness.