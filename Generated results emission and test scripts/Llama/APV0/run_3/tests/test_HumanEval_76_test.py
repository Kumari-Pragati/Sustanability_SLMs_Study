user

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

    return power == xassistant

Here is a unittest test script for the given Python function:

Python
import unittest
from HumanEval_76_code import is_simple_power

class TestIsSimplePower(unittest.TestCase):

    def test_is_simple_power(self):
        self.assertTrue(is_simple_power(1, 4))  # 1 is a simple power of 4
        self.assertTrue(is_simple_power(2, 2))  # 2 is a simple power of 2
        self.assertTrue(is_simple_power(8, 2))  # 8 is a simple power of 2
        self.assertFalse(is_simple_power(3, 2))  # 3 is not a simple power of 2
        self.assertFalse(is_simple_power(3, 1))  # 3 is not a simple power of 1
        self.assertFalse(is_simple_power(5, 3))  # 5 is not a simple power of 3
        self.assertTrue(is_simple_power(1, 1))  # 1 is a simple power of 1
        self.assertFalse(is_simple_power(2, 3))  # 2 is not a simple power of 3
        self.assertFalse(is_simple_power(4, 2))  # 4 is not a simple power of 2
        self.assertTrue(is_simple_power(16, 4))  # 16 is a simple power of 4
        self.assertFalse(is_simple_power(3, 4))  # 3 is not a simple power of 4

if __name__ == '__main__':
    unittest.main()


This script includes a variety of test cases to ensure the function is working correctly. The `assertTrue` method is used to check if the function returns `True` for expected inputs, and the `assertFalse` method is used to check if the function returns `False` for unexpected inputs.