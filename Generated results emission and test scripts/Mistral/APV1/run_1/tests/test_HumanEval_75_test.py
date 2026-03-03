You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_75_code import is_multiply_prime

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less than 100. 
    Example:
        is_multiply_prime(30) == True
        30 = 2 * 3 * 5
    """

    def is_prime(n):
        for j in range(2, n):
            if n % j == 0:
                return False
        return True

    for i in range(2, 101):
        if not is_prime(i):
            continue
        for j in range(2, 101):
            if not is_prime(j):
                continue
            for k in range(2, 101):
                if not is_prime(k):
                    continue
                if i * j * k == a:
                    return True
    return False

 Here is a comprehensive unittest test suite for the given Python function `is_multiply_prime`. The test cases cover the edge cases and a range of numbers to ensure the function works as expected.


import unittest
from HumanEval_75_code import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_edge_cases(self):
        self.assertFalse(is_multiply_prime(1))
        self.assertFalse(is_multiply_prime(0))
        self.assertFalse(is_multiply_prime(2))
        self.assertTrue(is_multiply_prime(3))
        self.assertTrue(is_multiply_prime(5))
        self.assertTrue(is_multiply_prime(7))

    def test_small_numbers(self):
        self.assertTrue(is_multiply_prime(6))
        self.assertTrue(is_multiply_prime(10))
        self.assertTrue(is_multiply_prime(15))
        self.assertTrue(is_multiply_prime(21))
        self.assertTrue(is_multiply_prime(30))
        self.assertTrue(is_multiply_prime(33))
        self.assertTrue(is_multiply_prime(35))
        self.assertTrue(is_multiply_prime(42))
        self.assertTrue(is_multiply_prime(56))
        self.assertTrue(is_multiply_prime(70))

    def test_large_numbers(self):
        self.assertTrue(is_multiply_prime(90))
        self.assertTrue(is_multiply_prime(91))
        self.assertTrue(is_multiply_prime(94))
        self.assertTrue(is_multiply_prime(105))
        self.assertTrue(is_multiply_prime(126))
        self.assertTrue(is_multiply_prime(153))
        self.assertTrue(is_multiply_prime(180))
        self.assertTrue(is_multiply_prime(210))
        self.assertTrue(is_multiply_prime(252))
        self.assertTrue(is_multiply_prime(300))

    def test_non_multiply_prime(self):
        self.assertFalse(is_multiply_prime(4))
        self.assertFalse(is_multiply_prime(8))
        self.assertFalse(is_multiply_prime(12))
        self.assertFalse(is_multiply_prime(16))
        self.assertFalse(is_multiply_prime(24))
        self.assertFalse(is_multiply_prime(36))
        self.assertFalse(is_multiply_prime(48))
        self.assertFalse(is_multiply_prime(60))
        self.assertFalse(is_multiply_prime(72))
        self.assertFalse(is_multiply_prime(96))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for edge cases, small numbers, large numbers, and non-multiply prime numbers. It ensures that the function works correctly for the given range of numbers (less than 100).