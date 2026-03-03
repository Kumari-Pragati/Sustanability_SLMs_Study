system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest
from HumanEval_99_code import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_closest_integer(self):
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("15.3"), 15)
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("-14.5"), -15)
        self.assertEqual(closest_integer("0"), 0)
        self.assertEqual(closest_integer("12.75"), 13)
        self.assertEqual(closest_integer("-12.75"), -13)
        self.assertEqual(closest_integer("10.5"), 11)
        self.assertEqual(closest_integer("-10.5"), -11)
        self.assertEqual(closest_integer("10.123"), 10)
        self.assertEqual(closest_integer("-10.123"), -10)
        self.assertEqual(closest_integer("10.999"), 11)
        self.assertEqual(closest_integer("-10.999"), -11)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover various scenarios as described in the docstring of `closest_integer`. It checks both positive and negative values, including those ending in `.5` which should be rounded away from zero.