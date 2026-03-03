You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_99_code import closest_integer
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples:
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15
    >>> closest_integer("14.5")
    15
    >>> closest_integer("-14.5")
    -15
    '''

    from math import floor, ceil

    # Clean up string
    value = value.strip()
    num = float(value)

    # Handle .5 cases — round away from zero
    if abs(num * 10) % 10 == 5:
        return ceil(num) if num > 0 else floor(num)
    else:
        return round(num)

 import unittest
from HumanEval_99_code import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(closest_integer("10"), 10)

    def test_positive_float_less_than_half(self):
        self.assertEqual(closest_integer("15.3"), 15)

    def test_positive_float_equal_half(self):
        self.assertEqual(closest_integer("14.5"), 15)

    def test_negative_float_equal_half(self):
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_negative_integer(self):
        self.assertEqual(closest_integer("-10"), -10)

    def test_zero(self):
        self.assertEqual(closest_integer("0"), 0)

    def test_float_greater_than_half(self):
        self.assertEqual(closest_integer("15.6"), 16)

    def test_float_less_than_half_and_negative(self):
        self.assertEqual(closest_integer("-15.4"), -15)

    def test_string_with_leading_or_trailing_spaces(self):
        self.assertEqual(closest_integer(" 10 "), 10)

    def test_string_with_trailing_period(self):
        self.assertEqual(closest_integer("10."), 10)

    def test_string_with_leading_period(self):
        self.assertEqual(closest_integer(".10"), 1)

    def test_string_with_multiple_periods(self):
        self.assertEqual(closest_integer("10..1"), 10)

    def test_string_with_non_numeric_characters(self):
        with self.assertRaises(ValueError):
            closest_integer("abc")

if __name__ == '__main__':
    unittest.main()