user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_31_code import is_prime
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return Trueassistant

Here is the unittest test script for the `is_prime` function:

import unittest
from HumanEval_31_code import is_prime

class TestIsPrime(unittest.TestCase):
    def test_small_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))

    def test_large_primes(self):
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(13441))
        self.assertTrue(is_prime(61))

    def test_composite_numbers(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))

    def test_edge_cases(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-1))

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            is_prime("hello")
        with self.assertRaises(TypeError):
            is_prime(3.14)

if __name__ == '__main__':
    unittest.main()

This script defines a `TestIsPrime` class with five test methods:

1. `test_small_primes`: Tests the function with small prime numbers (2, 3, 5, 7).
2. `test_large_primes`: Tests the function with larger prime numbers (101, 13441, 61).
3. `test_composite_numbers`: Tests the function with composite numbers (4, 6, 8, 9).
4. `test_edge_cases`: Tests the function with edge cases (1, 0, -1).
5. `test_non_integer_input`: Tests the function with non-integer input (string, float) and checks that it raises a `TypeError`.

The `unittest.main()` call at the end runs all the test methods and reports the results.