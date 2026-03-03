You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_138_code import is_equal_to_sum_even

class TestIsEqualToSumEven(unittest.TestCase):

    def test_negative_numbers(self):
        self.assertFalse(is_equal_to_sum_even(-1))
        self.assertFalse(is_equal_to_sum_even(-2))
        self.assertFalse(is_equal_to_sum_even(-4))

    def test_odd_numbers(self):
        self.assertFalse(is_equal_to_sum_even(1))
        self.assertFalse(is_equal_to_sum_even(3))
        self.assertFalse(is_equal_to_sum_even(5))

    def test_numbers_less_than_8(self):
        self.assertFalse(is_equal_to_sum_even(4))
        self.assertFalse(is_equal_to_sum_even(6))
        self.assertFalse(is_equal_to_sum_even(7))

    def test_numbers_equal_to_8(self):
        self.assertTrue(is_equal_to_sum_even(8))

    def test_numbers_greater_than_8(self):
        self.assertTrue(is_equal_to_sum_even(10))
        self.assertTrue(is_equal_to_sum_even(12))
        self.assertTrue(is_equal_to_sum_even(14))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for negative numbers, odd numbers, numbers less than 8, numbers equal to 8, and numbers greater than 8. It checks whether the function returns the correct result for each of these cases.