system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
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
    return number % 1.0assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_2_code import truncate_number

class TestTruncateNumber(unittest.TestCase):

    def test_truncate_number(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5)
        self.assertAlmostEqual(truncate_number(2.0), 0.0)
        self.assertAlmostEqual(truncate_number(1.0), 0.0)
        self.assertAlmostEqual(truncate_number(0.5), 0.5)
        self.assertAlmostEqual(truncate_number(0.0), 0.0)
        self.assertAlmostEqual(truncate_number(1.5), 0.5)
        self.assertAlmostEqual(truncate_number(2.5), 0.5)
        self.assertAlmostEqual(truncate_number(3.0), 0.0)
        self.assertAlmostEqual(truncate_number(4.5), 0.5)
        self.assertAlmostEqual(truncate_number(5.0), 0.0)

    def test_non_positive_number(self):
        with self.assertRaises(ValueError):
            truncate_number(-1.0)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            truncate_number('a')

if __name__ == '__main__':
    unittest.main()