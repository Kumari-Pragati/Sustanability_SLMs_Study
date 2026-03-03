You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

    return power == x

 Here is a complete unittest test suite for the `is_simple_power` function:


import unittest
from HumanEval_76_code import is_simple_power

class TestIsSimplePower(unittest.TestCase):

    def test_simple_power(self):
        self.assertTrue(is_simple_power(1, 1))
        self.assertTrue(is_simple_power(1, 4))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(8, 3))

    def test_not_simple_power(self):
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(3, 1))
        self.assertFalse(is_simple_power(5, 3))
        self.assertFalse(is_simple_power(6, 2))
        self.assertFalse(is_simple_power(7, 2))
        self.assertFalse(is_simple_power(9, 2))
        self.assertFalse(is_simple_power(10, 2))
        self.assertFalse(is_simple_power(11, 2))
        self.assertFalse(is_simple_power(12, 2))
        self.assertFalse(is_simple_power(13, 2))
        self.assertFalse(is_simple_power(14, 2))
        self.assertFalse(is_simple_power(15, 2))
        self.assertFalse(is_simple_power(16, 2))
        self.assertFalse(is_simple_power(17, 2))
        self.assertFalse(is_simple_power(18, 2))
        self.assertFalse(is_simple_power(19, 2))
        self.assertFalse(is_simple_power(20, 2))

if __name__ == '__main__':
    unittest.main()


This test suite includes two test cases: `test_simple_power` and `test_not_simple_power`. The first one tests the cases where the input number is a simple power of the base, and the second one tests the cases where it is not. The test suite covers a wide range of inputs to ensure the function works correctly for various cases.