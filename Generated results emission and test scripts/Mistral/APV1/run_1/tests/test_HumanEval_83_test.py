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

 Here is a comprehensive unittest test suite for the `starts_one_ends` function:


import unittest
from HumanEval_83_code import starts_one_ends

class TestStartsOneEnds(unittest.TestCase):

    def test_starts_one_ends_1(self):
        self.assertEqual(starts_one_ends(1), 1)

    def test_starts_one_ends_2(self):
        self.assertEqual(starts_one_ends(2), 18)

    def test_starts_one_ends_3(self):
        self.assertEqual(starts_one_ends(3), 180)

    def test_starts_one_ends_4(self):
        self.assertEqual(starts_one_ends(4), 1680)

    def test_starts_one_ends_5(self):
        self.assertEqual(starts_one_ends(5), 15360)

    def test_starts_one_ends_6(self):
        self.assertEqual(starts_one_ends(6), 143360)

    def test_starts_one_ends_7(self):
        self.assertEqual(starts_one_ends(7), 1331200)

    def test_starts_one_ends_8(self):
        self.assertEqual(starts_one_ends(8), 12244800)

    def test_starts_one_ends_9(self):
        self.assertEqual(starts_one_ends(9), 111714400)

    def test_starts_one_ends_10(self):
        self.assertEqual(starts_one_ends(10), 1009600000)

if __name__ == '__main__':
    unittest.main()


This test suite includes unit tests for the function with different input values ranging from 1 to 10. The test cases are designed to cover the edge cases and a range of possible inputs.