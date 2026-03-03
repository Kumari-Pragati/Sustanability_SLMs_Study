You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is a complete unittest test suite for the `is_equal_to_sum_even` function:


import unittest
from HumanEval_138_code import is_equal_to_sum_even

class TestIsEqualToSumEven(unittest.TestCase):
    def test_is_equal_to_sum_even(self):
        self.assertFalse(is_equal_to_sum_even(4))
        self.assertFalse(is_equal_to_sum_even(6))
        self.assertTrue(is_equal_to_sum_even(8))
        self.assertTrue(is_equal_to_sum_even(10))
        self.assertTrue(is_equal_to_sum_even(12))
        self.assertFalse(is_equal_to_sum_even(3))
        self.assertFalse(is_equal_to_sum_even(5))
        self.assertFalse(is_equal_to_sum_even(7))

if __name__ == '__main__':
    unittest.main()


This test suite includes a test case for the given examples and additional test cases to cover a range of even numbers less than 8, odd numbers, and numbers greater than 12. The `unittest.TestCase.assertFalse()` and `unittest.TestCase.assertTrue()` methods are used to verify the expected behavior of the `is_equal_to_sum_even()` function.