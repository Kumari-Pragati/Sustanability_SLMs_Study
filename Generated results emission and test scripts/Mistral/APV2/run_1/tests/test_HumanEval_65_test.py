You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the `circular_shift` function:


import unittest
from HumanEval_65_code import circular_shift

class TestCircularShift(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(circular_shift(12, 1), "21")
        self.assertEqual(circular_shift(123, 2), "312")
        self.assertEqual(circular_shift(1024, 3), "4201")
        self.assertEqual(circular_shift(999, 4), "999")

    def test_zero(self):
        self.assertEqual(circular_shift(0, 1), "0")
        self.assertEqual(circular_shift(0, 2), "0")

    def test_negative(self):
        self.assertEqual(circular_shift(-12, 1), "-21")
        self.assertEqual(circular_shift(-123, 2), "-312")
        self.assertEqual(circular_shift(-1024, 3), "-4201")
        self.assertEqual(circular_shift(-999, 4), "-999")

    def test_shift_greater_than_digits(self):
        self.assertEqual(circular_shift(12, 5), "123")
        self.assertEqual(circular_shift(123, 5), "231")
        self.assertEqual(circular_shift(1024, 5), "4201")
        self.assertEqual(circular_shift(999, 5), "999")

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different scenarios such as basic shifts, zero values, negative values, and shifts greater than the number of digits.