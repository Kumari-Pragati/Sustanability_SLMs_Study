Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `largest_prime_factor` function:


import unittest
from HumanEval_59_code import largest_prime_factor

class TestLargestPrimeFactor(unittest.TestCase):

    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)
        self.assertEqual(largest_prime_factor(60), 5)
        self.assertEqual(largest_prime_factor(10), 5)  # edge case: n is prime
        self.assertEqual(largest_prime_factor(1), 1)  # edge case: n is 1
        self.assertEqual(largest_prime_factor(4), 2)  # edge case: n is a power of 2
        self.assertEqual(largest_prime_factor(17), 17)  # edge case: n is prime
        self.assertEqual(largest_prime_factor(448), 2)  # edge case: n is a power of 2 with an additional factor
        self.assertEqual(largest_prime_factor(96480), 31)
        self.assertEqual(largest_prime_factor(640320), 2)  # edge case: n is a power of 2 with multiple factors

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to ensure the function works correctly for different inputs, including edge cases where the input is a prime number or a power of 2. The test cases cover a range of numbers from small to large to ensure the function handles large inputs correctly.