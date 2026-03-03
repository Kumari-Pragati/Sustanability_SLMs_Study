You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a complete unittest test suite for the `largest_prime_factor` function:


import unittest
from HumanEval_59_code import largest_prime_factor

class TestLargestPrimeFactor(unittest.TestCase):

    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)
        self.assertEqual(largest_prime_factor(60), 5)
        self.assertEqual(largest_prime_factor(10), 5)
        self.assertEqual(largest_prime_factor(1), 1)
        self.assertEqual(largest_prime_factor(2), 2)
        self.assertEqual(largest_prime_factor(3), 3)
        self.assertEqual(largest_prime_factor(4), 2)
        self.assertEqual(largest_prime_factor(5), 5)
        self.assertEqual(largest_prime_factor(6), 3)
        self.assertEqual(largest_prime_factor(7), 7)
        self.assertEqual(largest_prime_factor(8), 2)
        self.assertEqual(largest_prime_factor(9), 3)
        self.assertEqual(largest_prime_factor(100), 5)
        self.assertEqual(largest_prime_factor(1000), 2)
        self.assertEqual(largest_prime_factor(10000), 5)
        self.assertEqual(largest_prime_factor(100000), 5)
        self.assertEqual(largest_prime_factor(1000000), 2)
        self.assertEqual(largest_prime_factor(123456789), 1093)

if __name__ == '__main__':
    unittest.main()


This test suite includes a test function `test_largest_prime_factor` that tests the `largest_prime_factor` function with various input values. The test function uses the `assertEqual` method from the `unittest.TestCase` class to check if the expected and actual results match. The test suite also includes the standard boilerplate code to run the tests when the script is executed directly.