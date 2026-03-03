You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
    return True

 Here is a comprehensive unittest test suite for the given Python function `is_prime`.


import unittest
from HumanEval_31_code import is_prime

class TestIsPrime(unittest.TestCase):

    def test_is_prime_positive_numbers(self):
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(41))
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(13441))
        self.assertTrue(is_prime(61))

    def test_is_not_prime_positive_numbers(self):
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(20))
        self.assertFalse(is_prime(34))
        self.assertFalse(is_prime(40))
        self.assertFalse(is_prime(46))
        self.assertFalse(is_prime(50))

    def test_is_prime_zero(self):
        self.assertFalse(is_prime(0))

    def test_is_prime_negative_numbers(self):
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-3))
        self.assertFalse(is_prime(-4))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-6))
        self.assertFalse(is_prime(-7))

    def test_is_prime_one(self):
        self.assertFalse(is_prime(1))

if __name__ == '__main__':
    unittest.main()


This test suite includes positive test cases for prime numbers, negative test cases for non-prime numbers, edge cases like zero and one, and negative numbers. It uses the `unittest.TestCase.assertTrue()` and `unittest.TestCase.assertFalse()` methods to verify the correctness of the `is_prime()` function.