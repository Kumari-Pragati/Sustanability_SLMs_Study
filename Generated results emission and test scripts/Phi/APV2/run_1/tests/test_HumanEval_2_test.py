You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return number % 1.0

 import unittest
from HumanEval_2_code import truncate_number

class TestTruncateNumber(unittest.TestCase):

    def test_truncate_number_positive_float(self):
        self.assertEqual(truncate_number(3.5), 0.5)

    def test_truncate_number_zero(self):
        self.assertEqual(truncate_number(0.0), 0.0)

    def test_truncate_number_negative_float(self):
        with self.assertRaises(ValueError):
            truncate_number(-1.5)

    def test_truncate_number_whole_number(self):
        self.assertEqual(truncate_number(5.0), 0.0)

    def test_truncate_number_very_large_float(self):
        self.assertEqual(truncate_number(1000000.999), 0.999)

    def test_truncate_number_very_small_float(self):
        self.assertEqual(truncate_number(0.000001), 0.000001)

if __name__ == '__main__':
    unittest.main()