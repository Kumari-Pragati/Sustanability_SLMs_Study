user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_60_code import sum_to_n
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return sum(range(n + 1))assistant

Here is the unittest test script for the `sum_to_n` function:

import unittest
from HumanEval_60_code import sum_to_n

class TestSumToN(unittest.TestCase):
    def test_sum_to_n(self):
        # Test cases
        self.assertEqual(sum_to_n(1), 1)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)

        # Edge cases
        self.assertEqual(sum_to_n(0), 0)  # Edge case: n = 0
        self.assertEqual(sum_to_n(-1), 0)  # Edge case: n = -1 (should return 0)

if __name__ == '__main__':
    unittest.main()

This script defines a `TestSumToN` class that contains a single test method `test_sum_to_n`. This method tests the `sum_to_n` function with a variety of input values, including some edge cases.

The `assertEqual` method is used to check that the output of the `sum_to_n` function matches the expected result for each test case. If the output does not match the expected result, the test will fail and an error message will be displayed.

You can run this script directly using Python, and it will execute the tests and report any failures.