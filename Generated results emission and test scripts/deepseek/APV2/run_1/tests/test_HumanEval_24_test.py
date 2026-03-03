You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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
            return i


### Response:
Here is a complete unittest test suite for the given Python function:


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


This test suite includes tests for positive numbers, prime numbers, negative numbers, zero, and large numbers. The expected results are based on the function's docstring.

Please note that the function `largest_divisor(n: int) -> int` does not return `None` for negative numbers and zero, as the problem statement suggests. The function returns the largest number that divides `n` evenly, which is 1 for negative numbers and zero.

If you want the function to return `None` for negative numbers and zero, you should modify the function to return `None` in these cases.

Also, the function `largest_divisor(n: int) -> int` does not return `None` for large numbers. The largest divisor of a large number `n` is `1`, because `n` is a prime number.

If you want the function to return `None` for large numbers, you should modify the function to return `None` in this case.

Please let me know if you need a different behavior for these cases.