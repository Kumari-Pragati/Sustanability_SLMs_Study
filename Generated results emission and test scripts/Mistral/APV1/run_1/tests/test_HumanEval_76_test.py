You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_76_code import is_simple_power

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int = x
    For example:
        is_simple_power(1, 4) => True
        is_simple_power(2, 2) => True
        is_simple_power(8, 2) => True
        is_simple_power(3, 2) => False
        is_simple_power(3, 1) => False
        is_simple_power(5, 3) => False
    """

    if n == 1:
        return x == 1

    power = 1
    while power < x:
        power *= n

    return power == x

 Here is a comprehensive unittest test suite for the given Python function `is_simple_power`. The test cases cover a range of positive and negative numbers for both `x` and `n`.


import unittest
from HumanEval_76_code import is_simple_power

class TestIsSimplePower(unittest.TestCase):

    def test_simple_power(self):
        self.assertTrue(is_simple_power(1, 1))
        self.assertTrue(is_simple_power(1, 4))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(8, 3))

    def test_non_simple_power(self):
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(3, 1))
        self.assertFalse(is_simple_power(5, 3))
        self.assertFalse(is_simple_power(7, 2))
        self.assertFalse(is_simple_power(9, 2))

    def test_negative_numbers(self):
        self.assertFalse(is_simple_power(-1, 1))
        self.assertFalse(is_simple_power(-2, 2))
        self.assertFalse(is_simple_power(-8, 3))

    def test_zero(self):
        self.assertFalse(is_simple_power(0, 0))
        self.assertFalse(is_simple_power(0, 1))
        self.assertFalse(is_simple_power(0, 2))
        self.assertFalse(is_simple_power(0, n) for n in range(3, 10))

if __name__ == '__main__':
    unittest.main()


This test suite includes test cases for positive and negative numbers, as well as edge cases like zero and non-integer powers. It uses the `unittest.TestCase.assertTrue()` and `unittest.TestCase.assertFalse()` methods to verify the expected behavior of the `is_simple_power()` function.