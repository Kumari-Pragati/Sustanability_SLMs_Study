user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

    return [n + 2*i for i in range(n)]assistant

Here is the unittest test script for the `make_a_pile` function:

import unittest
from HumanEval_100_code import make_a_pile

class TestMakeAPile(unittest.TestCase):
    def test_odd_input(self):
        self.assertEqual(make_a_pile(3), [3, 5, 7])
        self.assertEqual(make_a_pile(5), [5, 7, 9, 11, 13])
        self.assertEqual(make_a_pile(9), [9, 11, 13, 15, 17, 19, 21])

    def test_even_input(self):
        self.assertEqual(make_a_pile(4), [4, 6, 8, 10])
        self.assertEqual(make_a_pile(6), [6, 8, 10, 12, 14, 16])
        self.assertEqual(make_a_pile(8), [8, 10, 12, 14, 16, 18, 20])

    def test_edge_cases(self):
        self.assertEqual(make_a_pile(1), [1])
        self.assertEqual(make_a_pile(2), [2, 4])
        self.assertEqual(make_a_pile(0), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            make_a_pile("hello")
        with self.assertRaises(TypeError):
            make_a_pile(0.5)

if __name__ == '__main__':
    unittest.main()

This script defines a `TestMakeAPile` class with four test methods:

* `test_odd_input`: tests the function with odd input values
* `test_even_input`: tests the function with even input values
* `test_edge_cases`: tests the function with edge cases (e.g. input value 1, 2, 0)
* `test_invalid_input`: tests the function with invalid input values (e.g. string, float)

Each test method uses the `assertEqual` method to check that the output of the `make_a_pile` function matches the expected result. The `with self.assertRaises` block is used to test that the function raises a `TypeError` when given invalid input.

You can run this script directly to execute the tests.