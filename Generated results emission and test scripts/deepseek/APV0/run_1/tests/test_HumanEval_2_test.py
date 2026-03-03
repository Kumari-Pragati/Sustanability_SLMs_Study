You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


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


This script includes tests for positive floats, negative floats, integers, and zero. It uses the `assertAlmostEqual` method to compare the output of the `truncate_number` function with the expected result, allowing for a small margin of error due to floating point precision.

Please note that the `truncate_number` function is supposed to return the decimal part of the number, so the test cases are designed based on this assumption. If the function is supposed to return something different, the test cases should be adjusted accordingly.

Also, the `truncate_number` function is imported from the `HumanEval_2_code` module, which should be in the same directory as this test script or in a directory that's part of the Python path.