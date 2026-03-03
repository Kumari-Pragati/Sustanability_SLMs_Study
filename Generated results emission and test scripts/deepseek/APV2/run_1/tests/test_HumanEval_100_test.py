You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given function:


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

    def test_make_a_pile_large_number(self):
        with self.assertRaises(Exception):
            make_a_pile(1000000)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- Testing the function with an odd number.
- Testing the function with an even number.
- Testing the function with zero.
- Testing the function with a negative number.
- Testing the function with a non-integer.
- Testing the function with a large number.

The last three tests are to ensure that the function raises an exception when it's given invalid input.

Please note that the function `make_a_pile` should be in a file named `HumanEval_100_code.py` in the same directory as this test file.

Also, the function `make_a_pile` should handle the cases where it's given invalid input (like negative numbers, non-integers, or large numbers) appropriately. If it doesn't, the tests for those cases will fail.

The function `make_a_pile` is currently not handling these cases, so you would need to modify it to make these tests pass.