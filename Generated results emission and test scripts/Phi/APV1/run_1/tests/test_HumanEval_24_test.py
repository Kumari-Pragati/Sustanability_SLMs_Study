You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
        self.assertIsNone(largest_divisor(-15))

    def test_largest_divisor_zero(self):
        self.assertIsNone(largest_divisor(0))

    def test_largest_divisor_prime_number(self):
        self.assertEqual(largest_divisor(7), None)

    def test_largest_divisor_even_number(self):
        self.assertEqual(largest_divisor(12), 6)

    def test_largest_divisor_multiple_of_two(self):
        self.assertEqual(largest_divisor(24), 12)

    def test_largest_divisor_multiple_of_three(self):
        self.assertEqual(largest_divisor(36), 18)

    def test_largest_divisor_multiple_of_four(self):
        self.assertEqual(largest_divisor(48), 24)

    def test_largest_divisor_multiple_of_five(self):
        self.assertEqual(largest_divisor(60), 30)

    def test_largest_divisor_multiple_of_six(self):
        self.assertEqual(largest_divisor(72), 36)

    def test_largest_divisor_multiple_of_seven(self):
        self.assertEqual(largest_divisor(49), None)

    def test_largest_divisor_multiple_of_eight(self):
        self.assertEqual(largest_divisor(96), 48)

    def test_largest_divisor_multiple_of_nine(self):
        self.assertEqual(largest_divisor(81), 27)

    def test_largest_divisor_multiple_of_ten(self):
        self.assertEqual(largest_divisor(100), 50)

if __name__ == '__main__':
    unittest.main()