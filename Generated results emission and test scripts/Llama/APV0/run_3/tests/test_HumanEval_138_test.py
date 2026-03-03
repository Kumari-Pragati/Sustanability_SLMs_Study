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
    return n % 2 == 0 and n >= 8assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_138_code import is_equal_to_sum_even

class TestIsEqualToSumEven(unittest.TestCase):

    def test_is_equal_to_sum_even(self):
        self.assertFalse(is_equal_to_sum_even(4))
        self.assertFalse(is_equal_to_sum_even(6))
        self.assertTrue(is_equal_to_sum_even(8))
        self.assertFalse(is_equal_to_sum_even(7))
        self.assertTrue(is_equal_to_sum_even(10))
        self.assertFalse(is_equal_to_sum_even(5))
        self.assertTrue(is_equal_to_sum_even(12))
        self.assertFalse(is_equal_to_sum_even(3))

if __name__ == '__main__':
    unittest.main()


This script includes 8 test cases to cover different scenarios. The `is_equal_to_sum_even` function is tested with numbers 4, 6, 8, 7, 10, 5, 12, and 3. The expected results are also provided.