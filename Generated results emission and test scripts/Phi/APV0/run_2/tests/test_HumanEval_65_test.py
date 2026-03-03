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

 import unittest
from HumanEval_65_code import circular_shift

class TestCircularShift(unittest.TestCase):

    def test_shift_right_one_digit(self):
        self.assertEqual(circular_shift(12, 1), "21")

    def test_shift_right_two_digits(self):
        self.assertEqual(circular_shift(12, 2), "12")

    def test_shift_right_more_than_digits(self):
        self.assertEqual(circular_shift(123, 4), "321")

    def test_shift_right_zero_digits(self):
        self.assertEqual(circular_shift(123, 0), "123")

    def test_shift_right_negative_digits(self):
        self.assertEqual(circular_shift(123, -1), "321")

    def test_shift_right_negative_greater_than_digits(self):
        self.assertEqual(circular_shift(123, -4), "321")

    def test_shift_right_negative_greater_than_or_equal_to_digits(self):
        self.assertEqual(circular_shift(123, -3), "231")

    def test_shift_right_empty_string(self):
        self.assertEqual(circular_shift("", 1), "")

    def test_shift_right_non_integer(self):
        with self.assertRaises(TypeError):
            circular_shift("12", 1)

    def test_shift_right_non_positive_integer(self):
        with self.assertRaises(ValueError):
            circular_shift(12, -1)

if __name__ == '__main__':
    unittest.main()