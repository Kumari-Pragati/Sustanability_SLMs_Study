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

 Here is a simple unittest test suite for the given Python function `is_equal_to_sum_even`. The test cases cover a range of even numbers from 0 to 16.


import unittest
from HumanEval_138_code import is_equal_to_sum_even

class TestIsEqualToSumEven(unittest.TestCase):

    def test_is_equal_to_sum_even(self):
        self.assertFalse(is_equal_to_sum_even(0))
        self.assertFalse(is_equal_to_sum_even(2))
        self.assertFalse(is_equal_to_sum_even(4))
        self.assertFalse(is_equal_to_sum_even(6))
        self.assertTrue(is_equal_to_sum_even(8))
        self.assertTrue(is_equal_to_sum_even(10))
        self.assertFalse(is_equal_to_sum_even(12))
        self.assertTrue(is_equal_to_sum_even(14))
        self.assertFalse(is_equal_to_sum_even(16))

if __name__ == '__main__':
    unittest.main()


This test suite includes a test function `test_is_equal_to_sum_even` that tests the `is_equal_to_sum_even` function with a range of even numbers. The `assertFalse` and `assertTrue` functions are used to verify the expected output of the function. If the function returns the correct output for the given test cases, the test will pass; otherwise, it will fail.