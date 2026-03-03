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

 Here is a comprehensive unittest test suite for the given Python function `largest_divisor`. I've added several test cases to cover different scenarios, including positive numbers, zero, and negative numbers.


import unittest
from HumanEval_24_code import largest_divisor

class TestLargestDivisor(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(largest_divisor(15), 5)
        self.assertEqual(largest_divisor(20), 4)
        self.assertEqual(largest_divisor(100), 25)
        self.assertEqual(largest_divisor(1), 1)

    def test_zero(self):
        self.assertEqual(largest_divisor(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(largest_divisor(-15), 1)
        self.assertEqual(largest_divisor(-20), 2)
        self.assertEqual(largest_divisor(-100), 2)
        self.assertEqual(largest_divisor(-1), 1)

    def test_edge_cases(self):
        self.assertEqual(largest_divisor(1), 1)
        self.assertEqual(largest_divisor(2), 2)
        self.assertEqual(largest_divisor(3), 3)
        self.assertEqual(largest_divisor(4), 2)
        self.assertEqual(largest_divisor(5), 5)
        self.assertEqual(largest_divisor(6), 2)
        self.assertEqual(largest_divisor(7), 7)
        self.assertEqual(largest_divisor(8), 4)
        self.assertEqual(largest_divisor(9), 3)

if __name__ == '__main__':
    unittest.main()


This test suite includes test cases for positive numbers, zero, negative numbers, and edge cases. It covers a wide range of inputs and ensures that the `largest_divisor` function behaves as expected.