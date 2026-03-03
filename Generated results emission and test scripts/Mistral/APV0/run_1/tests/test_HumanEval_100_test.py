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

    return [n + 2*i for i in range(n)]

 Here is a unittest test script for the `make_a_pile` function:


import unittest
from HumanEval_100_code import make_a_pile

class TestMakeAPile(unittest.TestCase):

    def test_make_a_pile(self):
        test_cases = [
            (3, [3, 5, 7]),
            (4, [4, 6, 8, 10]),
            (5, [5, 7, 9, 11, 13]),
            (6, [6, 8, 10, 12, 14, 16]),
            (7, [7, 9, 11, 13, 15, 17, 19]),
            (8, [8, 10, 12, 14, 16, 18, 20, 22]),
            (9, [9, 11, 13, 15, 17, 19, 21, 23, 25]),
            (10, [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]),
            (11, [11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]),
            (12, [12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34]),
            (13, [13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]),
            (14, [14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]),
            (15, [15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43]),
            (16, [16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46]),
            (17, [17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]),
            (18, [18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52]),
            (19, [19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55]),
            (20, [20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58]),
            (21, [21, 23, 25, 27, 29, 31,