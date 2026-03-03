You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

    def test_shift_right(self):
        self.assertEqual(circular_shift(1234, 1), "2341")
        self.assertEqual(circular_shift(1234, 2), "3412")
        self.assertEqual(circular_shift(1234, 3), "4123")
        self.assertEqual(circular_shift(1234, 4), "1234")

    def test_shift_left(self):
        self.assertEqual(circular_shift(1234, 1), "4123")
        self.assertEqual(circular_shift(1234, 2), "3412")
        self.assertEqual(circular_shift(1234, 3), "1234")
        self.assertEqual(circular_shift(1234, 4), "4123")

    def test_shift_zero(self):
        self.assertEqual(circular_shift(1234, 0), "1234")

    def test_shift_negative(self):
        self.assertEqual(circular_shift(1234, -1), "4123")
        self.assertEqual(circular_shift(1234, -2), "3412")
        self.assertEqual(circular_shift(1234, -3), "2341")
        self.assertEqual(circular_shift(1234, -4), "1234")

    def test_shift_greater_than_length(self):
        self.assertEqual(circular_shift(1234, 5), "4321")
        self.assertEqual(circular_shift(1234, 10), "4321")

    def test_shift_empty_string(self):
        self.assertEqual(circular_shift("", 1), "")

    def test_shift_single_digit(self):
        self.assertEqual(circular_shift(1, 1), "1")
        self.assertEqual(circular_shift(1, 2), "1")

    def test_shift_negative_shift(self):
        self.assertEqual(circular_shift(1234, -1), "4123")
        self.assertEqual(circular_shift(1234, -2), "3412")
        self.assertEqual(circular_shift(1234, -3), "2341")
        self.assertEqual(circular_shift(1234, -4), "1234")

if __name__ == '__main__':
    unittest.main()