Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

    def test_positive_fraction(self):
        self.assertEqual(closest_integer("15.3"), 15)

    def test_positive_half(self):
        self.assertEqual(closest_integer("14.5"), 15)

    def test_negative_half(self):
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_negative_integer(self):
        self.assertEqual(closest_integer("-10"), -10)

    def test_zero(self):
        self.assertEqual(closest_integer("0"), 0)

    def test_fraction_less_than_half(self):
        self.assertEqual(closest_integer("14.4"), 14)

    def test_fraction_greater_than_half(self):
        self.assertEqual(closest_integer("14.6"), 15)

    def test_equidistant_from_two_integers(self):
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_non_numeric_string(self):
        with self.assertRaises(ValueError):
            closest_integer("abc")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            closest_integer("")

if __name__ == '__main__':
    unittest.main()