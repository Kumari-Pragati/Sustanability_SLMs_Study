You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_92_code import any_int

class TestAnyInt(unittest.TestCase):
    def test_any_int(self):
        self.assertEqual(any_int(5, 2, 7), True)
        self.assertEqual(any_int(3, 2, 2), False)
        self.assertEqual(any_int(3, -2, 1), True)
        self.assertEqual(any_int(3.6, -2.2, 2), False)
        self.assertEqual(any_int(3, 2, 5), False)
        self.assertEqual(any_int(3, 2.0, 2), False)
        self.assertEqual(any_int(3, -2, 1.0), False)
        self.assertEqual(any_int(3.0, -2.0, 2.0), False)
        self.assertEqual(any_int(3, 2, 2.0), False)
        self.assertEqual(any_int(3.0, 2.0, 2), False)
        self.assertEqual(any_int(3, 2.0, 2.0), False)
        self.assertEqual(any_int(3.0, 2, 2.0), False)
        self.assertEqual(any_int(3.0, 2.0, 2), False)
        self.assertEqual(any_int(3, 2, 2), False)
        self.assertEqual(any_int(3.0, -2.0, 1.0), False)
        self.assertEqual(any_int(3.0, -2, 1), False)
        self.assertEqual(any_int(3, -2.0, 1.0), False)
        self.assertEqual(any_int(3, -2.0, 1), False)
        self.assertEqual(any_int(3.0, -2, 1.0), False)
        self.assertEqual(any_int(3.0, -2, 1), False)

if __name__ == '__main__':
    unittest.main()


This script tests the function with various integer and non-integer inputs to ensure that it behaves as expected.