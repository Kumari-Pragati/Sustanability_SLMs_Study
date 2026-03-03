You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the `starts_one_ends` function:


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

if __name__ == '__main__':
    unittest.main()


This test suite includes five test cases for the `starts_one_ends` function, covering different input values from 1 to 5. The test cases use the `assertEqual` method to compare the expected output with the actual output of the function.