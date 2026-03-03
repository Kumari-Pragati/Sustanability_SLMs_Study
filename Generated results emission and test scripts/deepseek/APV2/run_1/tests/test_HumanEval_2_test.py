You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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
    return number % 1.0


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_2_code import truncate_number

class TestTruncateNumber(unittest.TestCase):

    def test_positive_floats(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5)
        self.assertAlmostEqual(truncate_number(1.234), 0.234)
        self.assertAlmostEqual(truncate_number(0.001), 0.001)

    def test_negative_floats(self):
        self.assertAlmostEqual(truncate_number(-3.5), 0.5)
        self.assertAlmostEqual(truncate_number(-1.234), 0.766)
        self.assertAlmostEqual(truncate_number(-0.001), 0.999)

    def test_integers(self):
        self.assertAlmostEqual(truncate_number(3), 0)
        self.assertAlmostEqual(truncate_number(0), 0)
        self.assertAlmostEqual(truncate_number(-3), 0)

    def test_zero(self):
        self.assertAlmostEqual(truncate_number(0.0), 0.0)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive floats, negative floats, integers, and zero. The `assertAlmostEqual` method is used to compare the result of the `truncate_number` function with the expected result, allowing for a small margin of error due to floating point precision.