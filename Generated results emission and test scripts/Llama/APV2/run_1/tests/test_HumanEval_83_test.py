system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

Here is the complete unittest test suite for the given Python function:

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

if __name__ == '__main__':
    unittest.main()