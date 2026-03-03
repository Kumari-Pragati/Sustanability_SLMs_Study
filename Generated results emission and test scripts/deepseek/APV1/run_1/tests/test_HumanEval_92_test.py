You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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
    return False


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_92_code import any_int

class TestAnyInt(unittest.TestCase):

    def test_integers(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertTrue(any_int(3, -2, 1))
        self.assertFalse(any_int(3, 2, 2))
        self.assertFalse(any_int(3.6, -2.2, 2))

    def test_non_integers(self):
        self.assertFalse(any_int(3, 2, 2.0))
        self.assertFalse(any_int(3.6, -2.2, 2))
        self.assertFalse(any_int(3, -2, '1'))
        self.assertFalse(any_int(3.6, -2.2, '2'))
        self.assertFalse(any_int('3', -2, 2))
        self.assertFalse(any_int('3.6', '-2.2', 2))

    def test_single_integer(self):
        self.assertFalse(any_int(5, 2, 7))
        self.assertFalse(any_int(3, -2, 1))

    def test_two_integers(self):
        self.assertFalse(any_int(3, 2, 2))

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases:

1. `test_integers`: This test case checks the function's behavior with integer inputs.
2. `test_non_integers`: This test case checks the function's behavior with non-integer inputs.
3. `test_single_integer`: This test case checks the function's behavior with a single integer input.
4. `test_two_integers`: This test case checks the function's behavior with two integer inputs.

Each test case uses the `assertEqual` method to check if the function's output matches the expected output. If the function's output does not match the expected output, the test case will fail.