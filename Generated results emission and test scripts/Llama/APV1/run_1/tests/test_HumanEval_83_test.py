user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_83_code import starts_one_ends

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 1
    return 18 * (10 ** (n - 2))assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_83_code import starts_one_ends

class TestStartsOneEnds(unittest.TestCase):

    def test_start_one_ends(self):
        self.assertEqual(starts_one_ends(1), 1)
        self.assertEqual(starts_one_ends(2), 18)
        self.assertEqual(starts_one_ends(3), 180)
        self.assertEqual(starts_one_ends(4), 1800)
        self.assertEqual(starts_one_ends(5), 18000)
        self.assertEqual(starts_one_ends(6), 180000)
        self.assertEqual(starts_one_ends(7), 1800000)
        self.assertEqual(starts_one_ends(8), 18000000)
        self.assertEqual(starts_one_ends(9), 180000000)
        self.assertEqual(starts_one_ends(10), 1800000000)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            starts_one_ends(-1)
        with self.assertRaises(TypeError):
            starts_one_ends(0)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            starts_one_ends('a')

if __name__ == '__main__':
    unittest.main()


This test suite includes two test methods: `test_start_one_ends` and `test_invalid_input`. 

- `test_start_one_ends` tests the function with valid inputs (positive integers) and checks if the function returns the expected results. It also includes some edge cases like n=1.

- `test_invalid_input` tests the function with invalid inputs (negative integer, 0, non-integer) and checks if the function raises the expected exceptions (TypeError).