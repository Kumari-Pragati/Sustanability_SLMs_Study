You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_39_code import prime_fib
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    import math

    def is_prime(p):
        if p < 2:
            return False
        for k in range(2, min(int(math.sqrt(p)) + 1, p - 1)):
            if p % k == 0:
                return False
        return True

    f = [0, 1]
    while True:
        f.append(f[-1] + f[-2])
        if is_prime(f[-1]):
            n -= 1
        if n == 0:
            return f[-1]

 Here is a comprehensive unittest test suite for the `prime_fib` function:


import unittest
from HumanEval_39_code import prime_fib

class TestPrimeFib(unittest.TestCase):

    def test_prime_fib_with_valid_inputs(self):
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 5)
        self.assertEqual(prime_fib(4), 13)
        self.assertEqual(prime_fib(5), 89)
        self.assertEqual(prime_fib(6), 233)
        self.assertEqual(prime_fib(7), 1597)
        self.assertEqual(prime_fib(8), 37793)
        self.assertEqual(prime_fib(9), 85084074)
        self.assertEqual(prime_fib(10), 23636400383)

    def test_prime_fib_with_zero(self):
        with self.assertRaises(ValueError):
            prime_fib(0)

    def test_prime_fib_with_negative_input(self):
        with self.assertRaises(ValueError):
            prime_fib(-1)

    def test_prime_fib_with_large_input(self):
        with self.assertRaises(OverflowError):
            prime_fib(1000000)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases for valid inputs, edge cases (zero and negative inputs), and a large input to test for potential overflow errors. The test cases are organized into separate methods for better readability and maintainability.