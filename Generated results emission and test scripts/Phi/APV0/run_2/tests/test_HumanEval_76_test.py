Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 import unittest
from HumanEval_76_code import is_simple_power

class TestIsSimplePower(unittest.TestCase):

    def test_is_simple_power_true(self):
        self.assertTrue(is_simple_power(1, 4))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(8, 2))

    def test_is_simple_power_false_with_n_one(self):
        self.assertFalse(is_simple_power(3, 1))

    def test_is_simple_power_false_with_n_non_one(self):
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(5, 3))

    def test_is_simple_power_false_with_x_not_power_of_n(self):
        self.assertFalse(is_simple_power(9, 2))
        self.assertFalse(is_simple_power(10, 3))

    def test_is_simple_power_true_with_x_equal_to_n(self):
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(4, 2))
        self.assertTrue(is_simple_power(8, 2))

if __name__ == '__main__':
    unittest.main()