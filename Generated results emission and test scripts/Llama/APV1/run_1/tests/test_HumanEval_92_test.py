user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_92_code import any_int

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    any_int(3, 2, 2) ➞ False
    any_int(3, -2, 1) ➞ True
    any_int(3.6, -2.2, 2) ➞ False
    '''

    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        if (x + y == z) or (x + z == y) or (y + z == x):
            return True
        return False
    return Falseassistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_92_code import any_int

class TestAnyInt(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertTrue(any_int(3, -2, 1))
        self.assertTrue(any_int(1, 2, 3))

    def test_negative_numbers(self):
        self.assertTrue(any_int(-5, 2, 3))
        self.assertTrue(any_int(-3, 2, 1))
        self.assertTrue(any_int(-1, 2, 1))

    def test_zero_numbers(self):
        self.assertTrue(any_int(0, 0, 0))
        self.assertTrue(any_int(0, 1, 1))
        self.assertTrue(any_int(1, 0, 1))

    def test_non_integer_numbers(self):
        self.assertFalse(any_int(5.5, 2, 7))
        self.assertFalse(any_int(3, -2.2, 1))
        self.assertFalse(any_int(3.6, -2, 2))

    def test_non_equal_numbers(self):
        self.assertFalse(any_int(3, 2, 2))
        self.assertFalse(any_int(1, 1, 1))
        self.assertFalse(any_int(2, 2, 2))

    def test_edge_cases(self):
        self.assertFalse(any_int(1, 2, 'a'))
        self.assertFalse(any_int(1, 'a', 2))
        self.assertFalse(any_int('a', 2, 3))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive numbers, negative numbers, zero numbers, non-integer numbers, non-equal numbers, and edge cases. Each test method starts with the prefix `test_` to indicate that it is a test method. The `assertTrue` and `assertFalse` methods are used to verify the expected output of the `any_int` function.