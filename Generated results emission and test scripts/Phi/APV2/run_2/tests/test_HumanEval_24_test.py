You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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
            return i

 import unittest
from HumanEval_24_code import largest_divisor

class TestLargestDivisor(unittest.TestCase):

    def test_largest_divisor_positive_number(self):
        self.assertEqual(largest_divisor(15), 5)

    def test_largest_divisor_one(self):
        self.assertEqual(largest_divisor(1), None)

    def test_largest_divisor_negative_number(self):
        with self.assertRaises(ValueError):
            largest_divisor(-1)

    def test_largest_divisor_zero(self):
        with self.assertRaises(ValueError):
            largest_divisor(0)

    def test_largest_divisor_even_number(self):
        self.assertEqual(largest_divisor(8), 4)

    def test_largest_divisor_prime_number(self):
        self.assertEqual(largest_divisor(7), None)

if __name__ == '__main__':
    unittest.main()