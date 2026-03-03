You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_24_code import largest_divisor

class TestLargestDivisor(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(largest_divisor(15), 5)
        self.assertEqual(largest_divisor(24), 6)
        self.assertEqual(largest_divisor(100), 50)

    def test_prime_numbers(self):
        self.assertEqual(largest_divisor(2), 1)
        self.assertEqual(largest_divisor(3), 1)
        self.assertEqual(largest_divisor(5), 1)

    def test_negative_numbers(self):
        self.assertEqual(largest_divisor(-15), None)
        self.assertEqual(largest_divisor(-24), None)
        self.assertEqual(largest_divisor(-100), None)

    def test_zero(self):
        self.assertEqual(largest_divisor(0), None)

    def test_large_numbers(self):
        self.assertEqual(largest_divisor(1000000), 1)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive numbers, prime numbers, negative numbers, zero, and large numbers. The `largest_divisor` function is expected to return `None` for negative numbers and zero, and 1 for the number 1 (since 1 is the largest divisor of any number).

Please note that the function `largest_divisor` is expected to return `None` for negative numbers and zero, and 1 for the number 1 (since 1 is the largest divisor of any number). If the function behaves differently, the test suite should be adjusted accordingly.