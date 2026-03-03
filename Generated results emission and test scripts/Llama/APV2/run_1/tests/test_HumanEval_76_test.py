system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

    return power == xassistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_76_code import is_simple_power

class TestIsSimplePower(unittest.TestCase):

    def test_is_simple_power(self):
        self.assertTrue(is_simple_power(1, 4))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(8, 2))
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(3, 1))
        self.assertFalse(is_simple_power(5, 3))
        self.assertTrue(is_simple_power(1, 1))
        self.assertFalse(is_simple_power(2, 3))
        self.assertTrue(is_simple_power(4, 2))
        self.assertFalse(is_simple_power(3, 4))
        self.assertTrue(is_simple_power(1, 2))
        self.assertFalse(is_simple_power(5, 2))
        self.assertTrue(is_simple_power(8, 3))
        self.assertFalse(is_simple_power(9, 3))
        self.assertTrue(is_simple_power(27, 3))
        self.assertFalse(is_simple_power(10, 2))
        self.assertTrue(is_simple_power(16, 4))
        self.assertFalse(is_simple_power(11, 2))
        self.assertTrue(is_simple_power(25, 5))
        self.assertFalse(is_simple_power(12, 3))
        self.assertTrue(is_simple_power(36, 4))
        self.assertFalse(is_simple_power(13, 2))
        self.assertTrue(is_simple_power(49, 7))
        self.assertFalse(is_simple_power(14, 3))
        self.assertTrue(is_simple_power(64, 4))
        self.assertFalse(is_simple_power(15, 2))
        self.assertTrue(is_simple_power(81, 4))
        self.assertFalse(is_simple_power(16, 3))
        self.assertTrue(is_simple_power(100, 4))
        self.assertFalse(is_simple_power(17, 2))
        self.assertTrue(is_simple_power(121, 11))
        self.assertFalse(is_simple_power(18, 3))
        self.assertTrue(is_simple_power(144, 12))
        self.assertFalse(is_simple_power(19, 2))
        self.assertTrue(is_simple_power(169, 13))
        self.assertFalse(is_simple_power(20, 3))
        self.assertTrue(is_simple_power(196, 14))
        self.assertFalse(is_simple_power(21, 2))
        self.assertTrue(is_simple_power(225, 15))
        self.assertFalse(is_simple_power(22, 3))
        self.assertTrue(is_simple_power(256, 16))
        self.assertFalse(is_simple_power(23, 2))
        self.assertTrue(is_simple_power(289, 17))
        self.assertFalse(is_simple_power(24, 3))
        self.assertTrue(is_simple_power(324, 18))
        self.assertFalse(is_simple_power(25, 2))
        self.assertTrue(is_simple_power(361, 19))
        self.assertFalse(is_simple_power(26, 3))
        self.assertTrue(is_simple_power(400, 20))
        self.assertFalse(is_simple_power(27, 2))
        self.assertTrue(is_simple_power(441, 21))
        self.assertFalse(is_simple_power(28, 3))
        self.assertTrue(is_simple_power(484, 22))
        self.assertFalse(is_simple_power(29, 2))
        self.assertTrue(is_simple_power(529, 23))
        self.assertFalse(is_simple_power(30, 3))
        self.assertTrue(is_simple_power(576, 24))
        self.assertFalse(is_simple_power(31, 2))
        self.assertTrue(is_simple_power(625, 25))
        self.assertFalse(is_simple_power(32, 3))
        self.assertTrue(is_simple_power(676, 26))
        self.assertFalse(is_simple_power(33, 2))
        self.assertTrue(is_simple_power(729, 27))
        self.assertFalse(is_simple_power(34, 3))
        self.assertTrue(is_simple_power(784, 28))
        self.assertFalse(is_simple_power(35, 2))
        self.assertTrue(is_simple_power(841, 29))
        self.assertFalse(is_simple_power(36, 3))
        self.assertTrue(is_simple_power(900, 30))
        self.assertFalse(is_simple_power(37, 2))
        self.assertTrue(is_simple_power(961, 31))
        self.assertFalse(is_simple_power(38, 3))
        self.assertTrue(is_simple_power(1024, 32))
        self.assertFalse(is_simple_power(39, 2))
        self.assertTrue(is_simple_power(1089, 33))
        self.assertFalse(is_simple_power(40, 3))
        self.assertTrue(is_simple_power(1296, 36))
        self.assertFalse(is_simple_power(41, 2))
        self.assertTrue(is_simple_power(1369, 37))
        self.assertFalse(is_simple_power(42, 3))
        self.assertTrue(is_simple_power(1444, 38))