system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_24_code import largest_divisor

class TestLargestDivisor(unittest.TestCase):

    def test_largest_divisor(self):
        self.assertEqual(largest_divisor(15), 5)
        self.assertEqual(largest_divisor(12), 6)
        self.assertEqual(largest_divisor(7), 1)
        self.assertEqual(largest_divisor(10), 5)
        self.assertEqual(largest_divisor(24), 12)
        self.assertEqual(largest_divisor(25), 1)
        self.assertEqual(largest_divisor(36), 18)
        self.assertEqual(largest_divisor(48), 24)
        self.assertEqual(largest_divisor(50), 25)
        self.assertEqual(largest_divisor(51), 1)
        self.assertEqual(largest_divisor(52), 26)
        self.assertEqual(largest_divisor(53), 1)
        self.assertEqual(largest_divisor(54), 18)
        self.assertEqual(largest_divisor(55), 5)
        self.assertEqual(largest_divisor(56), 28)
        self.assertEqual(largest_divisor(57), 1)
        self.assertEqual(largest_divisor(58), 29)
        self.assertEqual(largest_divisor(59), 1)
        self.assertEqual(largest_divisor(60), 30)

if __name__ == '__main__':
    unittest.main()