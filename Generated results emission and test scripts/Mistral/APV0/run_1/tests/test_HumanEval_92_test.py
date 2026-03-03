Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `any_int` function:


import unittest
from HumanEval_92_code import any_int

class TestAnyInt(unittest.TestCase):
    def test_any_int(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertFalse(any_int(3, 2, 2))
        self.assertTrue(any_int(3, -2, 1))
        self.assertFalse(any_int(3.6, -2.2, 2))
        self.assertFalse(any_int(5, "2", 7))
        self.assertFalse(any_int(5, 2, "7"))
        self.assertFalse(any_int("5", 2, 7))
        self.assertFalse(any_int(5, 2, None))
        self.assertFalse(any_int([5], 2, 7))
        self.assertFalse(any_int(5, 2, (1, 2, 3)))

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the function's expected behavior, as well as edge cases where non-integer values are passed. The test case checks the function's return value against expected results using the `assertTrue` and `assertFalse` methods provided by unittest. The test script can be run directly using the command `python test_any_int.py`.