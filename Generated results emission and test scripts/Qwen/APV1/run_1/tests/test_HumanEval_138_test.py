system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to check if the given number can be expressed as the sum of four even numbers
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
    return n % 2 == 0 and n >= 8

class TestIsEqualToSumEven(unittest.TestCase):

    def test_is_equal_to_sum_even(self):
        # Test cases to verify the correctness of the function
        self.assertEqual(is_equal_to_sum_even(4), False)
        self.assertEqual(is_equal_to_sum_even(6), False)
        self.assertEqual(is_equal_to_sum_even(8), True)
        self.assertEqual(is_equal_to_sum_even(10), True)
        self.assertEqual(is_equal_to_sum_even(12), True)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestIsEqualToSumEven` class that inherits from `unittest.TestCase`. It contains a single method `test_is_equal_to_sum_even`, which tests the `is_equal_to_sum_even` function with various inputs to ensure it behaves as expected. The `assertEqual` methods compare the output of `is_equal_to_sum_even` against the expected results, using the `self.assertEqual` method. If any of these assertions fail, the test will raise an error indicating which assertion failed.