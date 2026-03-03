system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Importing the function to be tested
from HumanEval_138_code import is_equal_to_sum_even

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


This script imports the `is_equal_to_sum_even` function and creates a test class named `TestIsEqualToSumEven`. It includes several test cases using the `assertEqual` method to check if the function returns the expected results for different inputs. The `unittest.main()` call at the end makes the tests executable when run directly.