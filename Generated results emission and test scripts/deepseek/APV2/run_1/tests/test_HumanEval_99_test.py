You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_99_code import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(closest_integer("10"), 10)

    def test_positive_decimal(self):
        self.assertEqual(closest_integer("15.3"), 15)

    def test_positive_decimal_half(self):
        self.assertEqual(closest_integer("14.5"), 15)

    def test_negative_decimal_half(self):
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_negative_decimal(self):
        self.assertEqual(closest_integer("-15.3"), -15)

    def test_negative_integer(self):
        self.assertEqual(closest_integer("-10"), -10)

    def test_zero(self):
        self.assertEqual(closest_integer("0"), 0)

    def test_positive_decimal_half_round_up(self):
        self.assertEqual(closest_integer("1.5"), 2)

    def test_negative_decimal_half_round_down(self):
        self.assertEqual(closest_integer("-1.5"), -2)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various cases, including positive integers, negative integers, decimals, and the case where the number is equidistant from two integers (in which case it should round away from zero).