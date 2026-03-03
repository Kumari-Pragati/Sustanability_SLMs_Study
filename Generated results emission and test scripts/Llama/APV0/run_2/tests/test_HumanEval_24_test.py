user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_24_code import largest_divisor
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def largest_divisor(n: int) -> int:
    """For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in reversed(range(n)):
        if n % i == 0:
            return iassistant

Here is the unittest test script for the `largest_divisor` function:

import unittest
from HumanEval_24_code import largest_divisor

class TestLargestDivisor(unittest.TestCase):
    def test_largest_divisor(self):
        # Test cases
        self.assertEqual(largest_divisor(15), 5)
        self.assertEqual(largest_divisor(12), 6)
        self.assertEqual(largest_divisor(24), 12)
        self.assertEqual(largest_divisor(37), 1)
        self.assertEqual(largest_divisor(48), 24)
        self.assertEqual(largest_divisor(99), 33)
        self.assertEqual(largest_divisor(100), 25)
        self.assertEqual(largest_divisor(101), 1)
        self.assertEqual(largest_divisor(102), 51)
        self.assertEqual(largest_divisor(103), 1)
        self.assertEqual(largest_divisor(104), 52)

    def test_edge_cases(self):
        # Edge cases
        self.assertEqual(largest_divisor(0), 0)
        self.assertEqual(largest_divisor(1), 1)
        self.assertEqual(largest_divisor(-1), 1)
        self.assertEqual(largest_divisor(-2), 1)
        self.assertEqual(largest_divisor(-3), 1)

if __name__ == '__main__':
    unittest.main()

This script defines a `TestLargestDivisor` class with two test methods:

* `test_largest_divisor`: This method tests the `largest_divisor` function with a variety of input values, including positive integers, negative integers, and edge cases.
* `test_edge_cases`: This method tests the `largest_divisor` function with edge cases, such as 0, 1, -1, -2, and -3.

The `assertEqual` method is used to verify that the output of the `largest_divisor` function matches the expected result for each test case.

To run the tests, simply execute the script using Python, for example: `python test_largest_divisor.py`.