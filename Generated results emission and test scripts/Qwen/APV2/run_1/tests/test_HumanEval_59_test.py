system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_59_code import largest_prime_factor
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True

    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest


assistant

import unittest

# Function to check if a number is prime
def is_prime(k):
    if k < 2:
        return False
    for i in range(2, k - 1):
        if k % i == 0:
            return False
    return True

# Test class for the largest_prime_factor function
class TestLargestPrimeFactor(unittest.TestCase):

    # Test case for positive integer inputs
    def test_positive_integer(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)

    # Test case for edge cases (n=1 and n=prime numbers)
    def test_edge_cases(self):
        self.assertIsNone(largest_prime_factor(1))
        self.assertEqual(largest_prime_factor(2), 2)

    # Test case for large input values
    def test_large_input(self):
        self.assertEqual(largest_prime_factor(600851475143), 6857)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestLargestPrimeFactor` class that inherits from `unittest.TestCase`. It includes three test methods:

- `test_positive_integer`: Tests the function with typical positive integers.
- `test_edge_cases`: Checks the function's behavior with special cases like `n=1` and when `n` itself is a prime number.
- `test_large_input`: Verifies the function's performance with a very large input value.

The `unittest.main()` call at the end runs these tests when the script is executed directly.