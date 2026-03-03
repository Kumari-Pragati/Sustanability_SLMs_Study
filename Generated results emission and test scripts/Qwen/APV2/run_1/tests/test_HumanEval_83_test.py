system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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
    return 18 * (10 ** (n - 2))


assistant

import unittest

# Importing the function from the given module
from HumanEval_83_code import starts_one_ends

class TestStartsOneEnds(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(starts_one_ends(1), 1)

    def test_two_digits(self):
        self.assertEqual(starts_one_ends(2), 18)

    def test_three_digits(self):
        self.assertEqual(starts_one_ends(3), 180)

    def test_four_digits(self):
        self.assertEqual(starts_one_ends(4), 1800)

    def test_five_digits(self):
        self.assertEqual(starts_one_ends(5), 18000)

    def test_six_digits(self):
        self.assertEqual(starts_one_ends(6), 180000)

    def test_seven_digits(self):
        self.assertEqual(starts_one_ends(7), 1800000)

    def test_eight_digits(self):
        self.assertEqual(starts_one_ends(8), 18000000)

    def test_nine_digits(self):
        self.assertEqual(starts_one_ends(9), 180000000)

    def test_ten_digits(self):
        self.assertEqual(starts_one_ends(10), 1800000000)

if __name__ == '__main__':
    unittest.main()


This unittest test suite includes tests for various digit lengths up to ten digits, covering both cases where the number starts with one and ends with one. It ensures the function behaves as expected across different scenarios.