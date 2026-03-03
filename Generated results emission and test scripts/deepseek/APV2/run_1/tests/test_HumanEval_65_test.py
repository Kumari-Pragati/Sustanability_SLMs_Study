You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
Here is a complete unittest test suite for the given function:


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

    def test_shift_greater_than_number_of_digits(self):
        self.assertEqual(circular_shift(123, 4), "321")

    def test_negative_numbers(self):
        self.assertEqual(circular_shift(-123, 1), "-312")
        self.assertEqual(circular_shift(-123, 2), "-231")
        self.assertEqual(circular_shift(-123, 3), "-123")
        self.assertEqual(circular_shift(-123, 4), "-321")

    def test_zero(self):
        self.assertEqual(circular_shift(0, 1), "0")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for single-digit, two-digit, and three-digit numbers, as well as negative numbers and zero. It also tests the case where the shift is greater than the number of digits.