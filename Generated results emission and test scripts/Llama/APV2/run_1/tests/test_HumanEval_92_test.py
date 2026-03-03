system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    return Falseassistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_92_code import any_int

class TestAnyInt(unittest.TestCase):

    def test_any_int_true(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertTrue(any_int(3, -2, 1))
        self.assertTrue(any_int(1, 2, 3))

    def test_any_int_false(self):
        self.assertFalse(any_int(3, 2, 2))
        self.assertFalse(any_int(3.6, -2.2, 2))
        self.assertFalse(any_int(1, 2, 4))

    def test_any_int_non_integer(self):
        self.assertFalse(any_int(3, 2, 2.5))
        self.assertFalse(any_int(3.6, -2.2, 2.5))

    def test_any_int_edge_cases(self):
        self.assertTrue(any_int(0, 0, 0))
        self.assertFalse(any_int(0, 0, 1))

if __name__ == '__main__':
    unittest.main()