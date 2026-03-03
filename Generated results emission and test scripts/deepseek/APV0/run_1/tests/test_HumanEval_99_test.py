You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_99_code import closest_integer

class TestClosestInteger(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(closest_integer("10"), 10)

    def test_positive_float(self):
        self.assertEqual(closest_integer("15.3"), 15)

    def test_positive_float_half(self):
        self.assertEqual(closest_integer("14.5"), 15)

    def test_negative_float_half(self):
        self.assertEqual(closest_integer("-14.5"), -15)

    def test_negative_float(self):
        self.assertEqual(closest_integer("-15.3"), -15)

    def test_negative_integer(self):
        self.assertEqual(closest_integer("-10"), -10)

    def test_zero(self):
        self.assertEqual(closest_integer("0"), 0)

    def test_positive_float_large(self):
        self.assertEqual(closest_integer("123456789.123456789"), 123456789)

    def test_negative_float_large(self):
        self.assertEqual(closest_integer("-123456789.123456789"), -123456789)

if __name__ == '__main__':
    unittest.main()


This script creates a test class `TestClosestInteger` that inherits from `unittest.TestCase`. It includes several test methods to test the `closest_integer` function with different types of input. Each method asserts that the output of `closest_integer` is as expected.

Please note that you need to have the `HumanEval_99_code` module with the `closest_integer` function defined in it for this script to work.