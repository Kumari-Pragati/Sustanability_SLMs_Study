system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Importing the function from the provided code snippet
from HumanEval_2_code import truncate_number

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5, places=5)
        self.assertAlmostEqual(truncate_number(7.9999), 0.9999, places=5)
        self.assertAlmostEqual(truncate_number(4.0), 0.0, places=5)
        self.assertAlmostEqual(truncate_number(1.1111), 0.1111, places=5)

if __name__ == '__main__':
    unittest.main()


This test suite includes several assertions to check the correctness of the `truncate_number` function across different scenarios. The use of `self.assertAlmostEqual` ensures that the comparison is accurate within a specified number of decimal places.