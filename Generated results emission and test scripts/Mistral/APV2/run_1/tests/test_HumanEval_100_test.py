You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_100_code import make_a_pile
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """

    return [n + 2*i for i in range(n)]

 Here is the complete unittest test suite for the `make_a_pile` function:


import unittest
from HumanEval_100_code import make_a_pile

class TestMakeAPile(unittest.TestCase):

    def test_make_a_pile(self):
        self.assertEqual(make_a_pile(1), [1])
        self.assertEqual(make_a_pile(2), [2, 4])
        self.assertEqual(make_a_pile(3), [3, 5, 7])
        self.assertEqual(make_a_pile(4), [4, 6, 8, 10])
        self.assertEqual(make_a_pile(5), [5, 7, 9, 11, 13])
        self.assertEqual(make_a_pile(6), [6, 8, 10, 12, 14, 16])
        self.assertEqual(make_a_pile(7), [7, 9, 11, 13, 15, 17, 19])
        self.assertEqual(make_a_pile(8), [8, 10, 12, 14, 16, 18, 20, 22])
        self.assertEqual(make_a_pile(9), [9, 11, 13, 15, 17, 19, 21, 23, 25])
        self.assertEqual(make_a_pile(10), [10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

if __name__ == '__main__':
    unittest.main()


This test suite includes a test function `test_make_a_pile` that checks the correctness of the `make_a_pile` function for various input values. The test suite uses the built-in `unittest.TestCase.assertEqual` method to compare the expected and actual outputs of the `make_a_pile` function.