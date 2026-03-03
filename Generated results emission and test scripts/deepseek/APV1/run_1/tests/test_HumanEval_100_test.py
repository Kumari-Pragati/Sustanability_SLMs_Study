You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_100_code import make_a_pile

class TestMakeAPile(unittest.TestCase):

    def test_make_a_pile_odd(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])

    def test_make_a_pile_even(self):
        self.assertEqual(make_a_pile(4), [4, 6, 8, 10])

    def test_make_a_pile_zero(self):
        self.assertEqual(make_a_pile(0), [])

    def test_make_a_pile_negative(self):
        with self.assertRaises(Exception):
            make_a_pile(-1)

    def test_make_a_pile_non_integer(self):
        with self.assertRaises(Exception):
            make_a_pile(1.5)

    def test_make_a_pile_large(self):
        self.assertEqual(make_a_pile(1000), list(range(3, 1003, 2)))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- Testing the function with an odd number.
- Testing the function with an even number.
- Testing the function with zero.
- Testing the function with a negative number.
- Testing the function with a non-integer.
- Testing the function with a large number.

The last test is to check if the function works correctly with a large number. The function should return a list of numbers from 3 to 1003 with a step of 2, which is the sequence of odd numbers starting from 3.

Please note that the function `make_a_pile` should be defined in the file `HumanEval_100_code.py` for the test to work.