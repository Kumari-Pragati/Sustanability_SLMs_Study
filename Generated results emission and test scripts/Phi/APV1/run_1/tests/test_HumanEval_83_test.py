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
    return 18 * (10 ** (n - 2))

 import unittest
from HumanEval_83_code import starts_one_ends

class TestStartsOneEnds(unittest.TestCase):

    def test_single_digit(self):
        self.assertEqual(starts_one_ends(1), 1)

    def test_two_digit(self):
        self.assertEqual(starts_one_ends(2), 18)

    def test_three_digit(self):
        self.assertEqual(starts_one_ends(3), 180)

    def test_four_digit(self):
        self.assertEqual(starts_one_ends(4), 1800)

    def test_five_digit(self):
        self.assertEqual(starts_one_ends(5), 18000)

    def test_six_digit(self):
        self.assertEqual(starts_one_ends(6), 180000)

    def test_seven_digit(self):
        self.assertEqual(starts_one_ends(7), 1800000)

    def test_eight_digit(self):
        self.assertEqual(starts_one_ends(8), 18000000)

    def test_nine_digit(self):
        self.assertEqual(starts_one_ends(9), 180000000)

    def test_zero_digit(self):
        with self.assertRaises(ValueError):
            starts_one_ends(0)

if __name__ == '__main__':
    unittest.main()