user

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

    return power == xassistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_76_code import is_simple_power

class TestIsSimplePower(unittest.TestCase):

    def test_is_simple_power(self):
        # Test cases
        self.assertTrue(is_simple_power(1, 4))  # 1 is a simple power of 4
        self.assertTrue(is_simple_power(2, 2))  # 2 is a simple power of 2
        self.assertTrue(is_simple_power(8, 2))  # 8 is a simple power of 2
        self.assertFalse(is_simple_power(3, 2))  # 3 is not a simple power of 2
        self.assertFalse(is_simple_power(3, 1))  # 3 is not a simple power of 1
        self.assertFalse(is_simple_power(5, 3))  # 5 is not a simple power of 3
        self.assertTrue(is_simple_power(1, 1))  # 1 is a simple power of 1
        self.assertFalse(is_simple_power(2, 3))  # 2 is not a simple power of 3
        self.assertTrue(is_simple_power(4, 2))  # 4 is a simple power of 2
        self.assertFalse(is_simple_power(3, 4))  # 3 is not a simple power of 4
        self.assertTrue(is_simple_power(16, 4))  # 16 is a simple power of 4
        self.assertFalse(is_simple_power(5, 2))  # 5 is not a simple power of 2
        self.assertTrue(is_simple_power(1, 2))  # 1 is a simple power of 2
        self.assertFalse(is_simple_power(2, 4))  # 2 is not a simple power of 4
        self.assertTrue(is_simple_power(8, 4))  # 8 is a simple power of 4
        self.assertFalse(is_simple_power(3, 5))  # 3 is not a simple power of 5
        self.assertTrue(is_simple_power(1, 3))  # 1 is a simple power of 3
        self.assertFalse(is_simple_power(2, 6))  # 2 is not a simple power of 6
        self.assertTrue(is_simple_power(64, 4))  # 64 is a simple power of 4
        self.assertFalse(is_simple_power(3, 7))  # 3 is not a simple power of 7
        self.assertTrue(is_simple_power(1, 5))  # 1 is a simple power of 5
        self.assertFalse(is_simple_power(2, 8))  # 2 is not a simple power of 8
        self.assertTrue(is_simple_power(25, 5))  # 25 is a simple power of 5
        self.assertFalse(is_simple_power(3, 9))  # 3 is not a simple power of 9
        self.assertTrue(is_simple_power(1, 6))  # 1 is a simple power of 6
        self.assertFalse(is_simple_power(2, 10))  # 2 is not a simple power of 10
        self.assertTrue(is_simple_power(36, 6))  # 36 is a simple power of 6
        self.assertFalse(is_simple_power(3, 11))  # 3 is not a simple power of 11
        self.assertTrue(is_simple_power(1, 7))  # 1 is a simple power of 7
        self.assertFalse(is_simple_power(2, 12))  # 2 is not a simple power of 12
        self.assertTrue(is_simple_power(49, 7))  # 49 is a simple power of 7
        self.assertFalse(is_simple_power(3, 13))  # 3 is not a simple power of 13
        self.assertTrue(is_simple_power(1, 8))  # 1 is a simple power of 8
        self.assertFalse(is_simple_power(2, 14))  # 2 is not a simple power of 14
        self.assertTrue(is_simple_power(64, 8))  # 64 is a simple power of 8
        self.assertFalse(is_simple_power(3, 15))  # 3 is not a simple power of 15
        self.assertTrue(is_simple_power(1, 9))  # 1 is a simple power of 9
        self.assertFalse(is_simple_power(2, 16))  # 2 is not a simple power of 16
        self.assertTrue(is_simple_power(81, 9))  # 81 is a simple power of 9
        self.assertFalse(is_simple_power(3, 17))  # 3 is not