You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the `closest_integer` function:


import unittest
from HumanEval_99_code import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("15"), 15)
        self.assertEqual(closest_integer("99"), 99)

    def test_negative_integer(self):
        self.assertEqual(closest_integer("-10"), -10)
        self.assertEqual(closest_integer("-15"), -15)
        self.assertEqual(closest_integer("-99"), -99)

    def test_float_up(self):
        self.assertEqual(closest_integer("15.3"), 15)
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("14.9"), 15)

    def test_float_down(self):
        self.assertEqual(closest_integer("15.7"), 15)
        self.assertEqual(closest_integer("14.1"), 14)
        self.assertEqual(closest_integer("14.05"), 14)

    def test_edge_cases(self):
        self.assertEqual(closest_integer("0"), 0)
        self.assertEqual(closest_integer("0.5"), 1)
        self.assertEqual(closest_integer("9.5"), 10)
        self.assertEqual(closest_integer("-0.5"), -1)
        self.assertEqual(closest_integer("-9.5"), -10)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as positive integers, negative integers, floating-point numbers, edge cases, and handling the .5 cases as per the function's rounding rule.