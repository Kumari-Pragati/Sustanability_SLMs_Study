Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `truncate_number` function:


import unittest
from HumanEval_2_code import truncate_number

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5)
        self.assertAlmostEqual(truncate_number(0.0), 0.0)
        self.assertAlmostEqual(truncate_number(1.0), 0.0)
        self.assertAlmostEqual(truncate_number(2.0), 0.0)
        self.assertAlmostEqual(truncate_number(3.0), 0.0)
        self.assertAlmostEqual(truncate_number(4.0), 0.0)
        self.assertAlmostEqual(truncate_number(5.0), 0.0)
        self.assertAlmostEqual(truncate_number(6.0), 0.0)
        self.assertAlmostEqual(truncate_number(7.0), 0.0)
        self.assertAlmostEqual(truncate_number(8.0), 0.0)
        self.assertAlmostEqual(truncate_number(9.0), 0.0)
        self.assertAlmostEqual(truncate_number(10.0), 0.0)
        self.assertAlmostEqual(truncate_number(11.0), 0.1)
        self.assertAlmostEqual(truncate_number(12.0), 0.0)
        self.assertAlmostEqual(truncate_number(13.0), 0.3)
        self.assertAlmostEqual(truncate_number(14.0), 0.0)
        self.assertAlmostEqual(truncate_number(15.0), 0.0)
        self.assertAlmostEqual(truncate_number(16.0), 0.0)
        self.assertAlmostEqual(truncate_number(17.0), 0.0)
        self.assertAlmostEqual(truncate_number(18.0), 0.0)
        self.assertAlmostEqual(truncate_number(19.0), 0.0)
        self.assertAlmostEqual(truncate_number(20.0), 0.0)

if __name__ == '__main__':
    unittest.main()


This test script includes a test function `test_truncate_number` that checks the function's behavior for a range of positive floating point numbers. The `assertAlmostEqual` function is used to compare the expected and actual results with a small tolerance (0.00001 by default).