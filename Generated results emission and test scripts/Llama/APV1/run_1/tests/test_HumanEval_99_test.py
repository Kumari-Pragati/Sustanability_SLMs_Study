user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

    # Handle.5 cases — round away from zero
    if abs(num * 10) % 10 == 5:
        return ceil(num) if num > 0 else floor(num)
    else:
        return round(num)assistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_99_code import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_closest_integer(self):
        self.assertEqual(closest_integer("10"), 10)
        self.assertEqual(closest_integer("15.3"), 15)
        self.assertEqual(closest_integer("14.5"), 15)
        self.assertEqual(closest_integer("-14.5"), -15)
        self.assertEqual(closest_integer("0"), 0)
        self.assertEqual(closest_integer("0.5"), 1)
        self.assertEqual(closest_integer("-0.5"), -1)
        self.assertEqual(closest_integer("1.9"), 2)
        self.assertEqual(closest_integer("-1.9"), -2)
        self.assertEqual(closest_integer("2.5"), 3)
        self.assertEqual(closest_integer("-2.5"), -3)
        self.assertEqual(closest_integer("3.5"), 4)
        self.assertEqual(closest_integer("-3.5"), -4)
        self.assertEqual(closest_integer("4.5"), 5)
        self.assertEqual(closest_integer("-4.5"), -5)
        self.assertEqual(closest_integer("5.5"), 6)
        self.assertEqual(closest_integer("-5.5"), -6)
        self.assertEqual(closest_integer("6.5"), 7)
        self.assertEqual(closest_integer("-6.5"), -7)
        self.assertEqual(closest_integer("7.5"), 8)
        self.assertEqual(closest_integer("-7.5"), -8)
        self.assertEqual(closest_integer("8.5"), 9)
        self.assertEqual(closest_integer("-8.5"), -9)
        self.assertEqual(closest_integer("9.5"), 10)
        self.assertEqual(closest_integer("-9.5"), -10)

    def test_edge_cases(self):
        self.assertEqual(closest_integer("0.0"), 0)
        self.assertEqual(closest_integer("-0.0"), 0)
        self.assertEqual(closest_integer("1.0"), 1)
        self.assertEqual(closest_integer("-1.0"), -1)
        self.assertEqual(closest_integer("2.0"), 2)
        self.assertEqual(closest_integer("-2.0"), -2)
        self.assertEqual(closest_integer("3.0"), 3)
        self.assertEqual(closest_integer("-3.0"), -3)
        self.assertEqual(closest_integer("4.0"), 4)
        self.assertEqual(closest_integer("-4.0"), -4)
        self.assertEqual(closest_integer("5.0"), 5)
        self.assertEqual(closest_integer("-5.0"), -5)
        self.assertEqual(closest_integer("6.0"), 6)
        self.assertEqual(closest_integer("-6.0"), -6)
        self.assertEqual(closest_integer("7.0"), 7)
        self.assertEqual(closest_integer("-7.0"), -7)
        self.assertEqual(closest_integer("8.0"), 8)
        self.assertEqual(closest_integer("-8.0"), -8)
        self.assertEqual(closest_integer("9.0"), 9)
        self.assertEqual(closest_integer("-9.0"), -9)

if __name__ == '__main__':
    unittest.main()


This test suite includes two test cases: `test_closest_integer` and `test_edge_cases`. The `test_closest_integer` test case includes a variety of test cases to ensure that the function correctly rounds numbers to the closest integer. The `test_edge_cases` test case includes test cases to ensure that the function correctly handles edge cases, such as rounding 0.0 to 0, and rounding 1.0 to 1.