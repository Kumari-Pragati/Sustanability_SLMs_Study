You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 
import unittest
from HumanEval_65_code import circular_shift

class TestCircularShift(unittest.TestCase):

    def test_shift_right_one(self):
        self.assertEqual(circular_shift(12, 1), "21")

    def test_shift_right_two(self):
        self.assertEqual(circular_shift(12, 2), "12")

    def test_shift_right_greater_than_digits(self):
        self.assertEqual(circular_shift(123, 4), "321")

    def test_shift_right_zero(self):
        self.assertEqual(circular_shift(123, 0), "123")

    def test_shift_right_negative(self):
        self.assertEqual(circular_shift(123, -1), "321")

    def test_shift_right_negative_greater_than_digits(self):
        self.assertEqual(circular_shift(123, -4), "321")

    def test_shift_right_negative_greater_than_twice_digits(self):
        self.assertEqual(circular_shift(123, -3), "321")

    def test_shift_right_empty_string(self):
        self.assertEqual(circular_shift("", 1), "")

    def test_shift_right_non_integer(self):
        with self.assertRaises(TypeError):
            circular_shift("12", 1)

    def test_shift_right_negative_integer(self):
        with self.assertRaises(ValueError):
            circular_shift(12, -1)

if __name__ == '__main__':
    unittest.main()


This test suite covers various cases for the `circular_shift` function, including shifting by one, two, and more than the number of digits, as well as handling edge cases such as shifting by zero, negative shifts, and non-integer inputs. It also tests for the expected behavior when the input is an empty string and when a `TypeError` should be raised for non-integer inputs.