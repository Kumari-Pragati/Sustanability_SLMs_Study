user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
            return f[-1]assistant

Here is the unittest test script for the `prime_fib` function:

import unittest
from HumanEval_39_code import prime_fib

class TestPrimeFib(unittest.TestCase):
    def test_prime_fib(self):
        # Test cases from the docstring
        self.assertEqual(prime_fib(1), 2)
        self.assertEqual(prime_fib(2), 3)
        self.assertEqual(prime_fib(3), 5)
        self.assertEqual(prime_fib(4), 13)
        self.assertEqual(prime_fib(5), 89)

        # Additional test cases
        self.assertEqual(prime_fib(6), 233)
        self.assertEqual(prime_fib(7), 1597)
        self.assertEqual(prime_fib(8), 28657)
        self.assertEqual(prime_fib(9), 43398)

        # Edge cases
        self.assertEqual(prime_fib(0), 0)  # Should return 0 for n=0
        self.assertEqual(prime_fib(-1), 0)  # Should return 0 for n<0

    def test_is_prime(self):
        # Test cases for the is_prime function
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(6))

if __name__ == '__main__':
    unittest.main()

This script defines a `TestPrimeFib` class with two test methods: `test_prime_fib` and `test_is_prime`. The `test_prime_fib` method tests the `prime_fib` function with various input values, including the test cases from the docstring and additional test cases. The `test_is_prime` method tests the `is_prime` function with various input values.

You can run this script directly to execute the tests. If all tests pass, you should see an output like:

....
----------------------------------------------------------------------
Ran 6 tests in 0.000s

OK

If any tests fail, you will see an error message indicating which test failed and why.