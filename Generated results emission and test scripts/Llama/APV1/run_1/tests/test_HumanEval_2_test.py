user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_2_code import truncate_number

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def truncate_number(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number % 1.0assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_2_code import truncate_number

class TestTruncateNumber(unittest.TestCase):

    def test_truncate_number_positive(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5)
        self.assertAlmostEqual(truncate_number(2.0), 0.0)
        self.assertAlmostEqual(truncate_number(1.0), 0.0)
        self.assertAlmostEqual(truncate_number(0.5), 0.5)
        self.assertAlmostEqual(truncate_number(0.0), 0.0)

    def test_truncate_number_negative(self):
        self.assertAlmostEqual(truncate_number(-3.5), -0.5)
        self.assertAlmostEqual(truncate_number(-2.0), -0.0)
        self.assertAlmostEqual(truncate_number(-1.0), -0.0)
        self.assertAlmostEqual(truncate_number(-0.5), -0.5)
        self.assertAlmostEqual(truncate_number(-0.0), -0.0)

    def test_truncate_number_zero(self):
        self.assertAlmostEqual(truncate_number(0.0), 0.0)
        self.assertAlmostEqual(truncate_number(-0.0), 0.0)

    def test_truncate_number_non_numeric(self):
        with self.assertRaises(TypeError):
            truncate_number('a')
        with self.assertRaises(TypeError):
            truncate_number([1, 2, 3])
        with self.assertRaises(TypeError):
            truncate_number({'a': 1, 'b': 2})

    def test_truncate_number_large(self):
        self.assertAlmostEqual(truncate_number(123456.789), 0.789)
        self.assertAlmostEqual(truncate_number(-123456.789), -0.789)

    def test_truncate_number_small(self):
        self.assertAlmostEqual(truncate_number(0.000001), 0.000001)
        self.assertAlmostEqual(truncate_number(-0.000001), -0.000001)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive and negative numbers, zero, non-numeric inputs, large and small numbers. It uses the `assertAlmostEqual` method to account for floating point precision issues.