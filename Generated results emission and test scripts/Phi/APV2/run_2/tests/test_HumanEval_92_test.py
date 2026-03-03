You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 
import unittest
from HumanEval_92_code import any_int

class TestAnyIntFunction(unittest.TestCase):

    def test_positive_integers(self):
        self.assertTrue(any_int(5, 2, 7))
        self.assertFalse(any_int(3, 2, 2))
        self.assertTrue(any_int(3, -2, 1))

    def test_non_integer_values(self):
        self.assertFalse(any_int(5, 2, 7.5))
        self.assertFalse(any_int(3, 2, "2"))
        self.assertFalse(any_int(3.6, -2.2, 2))

    def test_all_integers(self):
        self.assertTrue(any_int(1, 2, 3))
        self.assertFalse(any_int(-1, 0, 1))
        self.assertFalse(any_int(0, 0, 0))

    def test_no_sum_condition_met(self):
        self.assertFalse(any_int(1, 2, 4))
        self.assertFalse(any_int(10, 5, 15))
        self.assertFalse(any_int(0, 0, 1))

    def test_sum_condition_met(self):
        self.assertTrue(any_int(3, 4, 7))
        self.assertTrue(any_int(-1, 1, 0))
        self.assertTrue(any_int(5, -5, 0))

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios to ensure the `any_int` function behaves as expected. It includes tests for:

- Positive integers where the sum condition is met.
- Non-integer values to ensure the function returns `False`.
- Cases where all inputs are integers but the sum condition is not met.
- Cases where the sum condition is met.

Each test case is designed to verify a specific aspect of the function's behavior, ensuring comprehensive coverage.