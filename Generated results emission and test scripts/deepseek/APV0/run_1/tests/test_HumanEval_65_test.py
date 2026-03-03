You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_65_code import circular_shift
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]


### Response:
Here is the unittest test script for the given Python function:


import unittest
from HumanEval_65_code import circular_shift

class TestCircularShift(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(circular_shift(1, 1), "1")

    def test_two_digits(self):
        self.assertEqual(circular_shift(12, 1), "21")
        self.assertEqual(circular_shift(12, 2), "12")

    def test_three_digits(self):
        self.assertEqual(circular_shift(123, 1), "312")
        self.assertEqual(circular_shift(123, 2), "231")
        self.assertEqual(circular_shift(123, 3), "123")

    def test_more_than_digits(self):
        self.assertEqual(circular_shift(123, 4), "321")

    def test_zero(self):
        self.assertEqual(circular_shift(0, 1), "0")

    def test_negative(self):
        self.assertEqual(circular_shift(-123, 1), "-321")

if __name__ == '__main__':
    unittest.main()


This script includes tests for single-digit numbers, two-digit numbers, three-digit numbers, numbers with more digits than the number of digits, zero, and negative numbers. It checks that the function returns the correct result for each of these cases.

Please note that the function `circular_shift` is assumed to be in a file named `HumanEval_65_code.py` in the same directory as the test script. If the function is in a different location, you will need to adjust the import statement accordingly.

Also, the function `circular_shift` is expected to handle negative numbers correctly, which means it should reverse the digits of the absolute value of the number and add a negative sign if the input number is negative. The test script includes a test for this case.