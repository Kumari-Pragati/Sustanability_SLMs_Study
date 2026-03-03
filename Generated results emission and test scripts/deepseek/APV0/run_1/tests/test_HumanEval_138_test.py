You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_138_code import is_equal_to_sum_even
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n % 2 == 0 and n >= 8


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_138_code import is_equal_to_sum_even

class TestIsEqualToSumEven(unittest.TestCase):

    def test_is_equal_to_sum_even(self):
        self.assertFalse(is_equal_to_sum_even(4))
        self.assertFalse(is_equal_to_sum_even(6))
        self.assertTrue(is_equal_to_sum_even(8))
        self.assertFalse(is_equal_to_sum_even(10))
        self.assertTrue(is_equal_to_sum_even(12))
        self.assertFalse(is_equal_to_sum_even(14))
        self.assertTrue(is_equal_to_sum_even(16))
        self.assertFalse(is_equal_to_sum_even(18))
        self.assertTrue(is_equal_to_sum_even(20))
        self.assertFalse(is_equal_to_sum_even(22))
        self.assertTrue(is_equal_to_sum_even(24))
        self.assertFalse(is_equal_to_sum_even(26))
        self.assertTrue(is_equal_to_sum_even(28))
        self.assertFalse(is_equal_to_sum_even(30))
        self.assertTrue(is_equal_to_sum_even(32))
        self.assertFalse(is_equal_to_sum_even(34))
        self.assertTrue(is_equal_to_sum_even(36))
        self.assertFalse(is_equal_to_sum_even(38))
        self.assertTrue(is_equal_to_sum_even(40))

if __name__ == '__main__':
    unittest.main()


This script tests the function `is_equal_to_sum_even` with a range of input values, including both cases where the function should return `True` and where it should return `False`.

Please note that the function `is_equal_to_sum_even` is not defined in the provided code. You need to define it in the `HumanEval_138_code` module for the test script to work.

The function should be defined as follows:


def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n % 2 == 0 and n >= 8


This function checks if the input number `n` is even and greater than or equal to 8. If both conditions are met, it returns `True`, otherwise it returns `False`.