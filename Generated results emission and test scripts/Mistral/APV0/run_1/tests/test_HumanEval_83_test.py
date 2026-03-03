Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `starts_one_ends` function:


import unittest
from HumanEval_83_code import starts_one_ends

class TestStartsOneEnds(unittest.TestCase):
    def test_starts_one_ends(self):
        self.assertEqual(starts_one_ends(1), 1)
        self.assertEqual(starts_one_ends(2), 18)
        self.assertEqual(starts_one_ends(3), 180)
        self.assertEqual(starts_one_ends(4), 1680)
        self.assertEqual(starts_one_ends(5), 15744)
        self.assertEqual(starts_one_ends(6), 148336)
        self.assertEqual(starts_one_ends(7), 1407040)
        self.assertEqual(starts_one_ends(8), 13441440)
        self.assertEqual(starts_one_ends(9), 128767360)
        self.assertEqual(starts_one_ends(10), 1239534880)
        self.assertEqual(starts_one_ends(11), 11982581120)
        self.assertEqual(starts_one_ends(12), 116356160000)
        self.assertEqual(starts_one_ends(13), 1134890560000)
        self.assertEqual(starts_one_ends(14), 1109984000000)
        self.assertEqual(starts_one_ends(15), 10884160000000)
        self.assertEqual(starts_one_ends(16), 106995200000000)
        self.assertEqual(starts_one_ends(17), 1054496000000000)
        self.assertEqual(starts_one_ends(18), 1041712000000000)
        self.assertEqual(starts_one_ends(19), 1031408000000000)
        self.assertEqual(starts_one_ends(20), 1023200000000000)

if __name__ == '__main__':
    unittest.main()


This test script includes a test function `test_starts_one_ends` that tests the `starts_one_ends` function for various input values. The test function uses the `assertEqual` method from the `unittest.TestCase` class to check if the expected and actual outputs match. If the function passes all the tests, the test script will run successfully.