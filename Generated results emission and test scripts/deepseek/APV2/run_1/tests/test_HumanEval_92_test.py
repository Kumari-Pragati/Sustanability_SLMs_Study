You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_92_code import any_int

class TestAnyInt(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertTrue(any_int(3, -2, 1))

    def test_negative_numbers(self):
        self.assertTrue(any_int(-3, -2, -1))
        self.assertTrue(any_int(-3, -2, 1))

    def test_mixed_numbers(self):
        self.assertFalse(any_int(3.6, -2.2, 2))
        self.assertFalse(any_int(3, 2, 2))

    def test_non_integer_numbers(self):
        self.assertFalse(any_int(3, 2, 2.5))
        self.assertFalse(any_int(3.6, -2.2, 2))
        self.assertFalse(any_int(3, '2', 2))

    def test_single_integer(self):
        self.assertFalse(any_int(3, 2, 2))
        self.assertFalse(any_int(3, 2, 5))

    def test_two_integers(self):
        self.assertFalse(any_int(3, 2, 2.5))
        self.assertFalse(any_int(3.6, -2.2, 2))
        self.assertFalse(any_int(3, '2', 2))

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different scenarios:

- `test_positive_numbers`: Tests with positive integers.
- `test_negative_numbers`: Tests with negative integers.
- `test_mixed_numbers`: Tests with mixed integers and floats.
- `test_non_integer_numbers`: Tests with non-integer numbers.
- `test_single_integer`: Tests with a single integer.
- `test_two_integers`: Tests with two integers.

Each test case checks the function's output against the expected result. If the function's behavior deviates from the expected behavior in any of these scenarios, the test will fail.