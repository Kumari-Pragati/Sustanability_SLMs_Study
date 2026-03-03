You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return False

 Here is the complete unittest test suite for the `any_int` function:


import unittest
from HumanEval_92_code import any_int

class TestAnyInt(unittest.TestCase):

    def test_any_int(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertFalse(any_int(3, 2, 2))
        self.assertTrue(any_int(3, -2, 1))
        self.assertFalse(any_int(3.6, -2.2, 2))
        self.assertFalse(any_int(5, '2', 7))
        self.assertFalse(any_int(5, 2, '7'))
        self.assertFalse(any_int('5', 2, 7))
        self.assertFalse(any_int(5, 2, None))
        self.assertFalse(any_int(None, 2, 7))
        self.assertFalse(any_int(5, None, 7))

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover the edge cases and invalid inputs. It uses the `assertTrue` and `assertFalse` methods from unittest to verify the expected behavior of the `any_int` function.