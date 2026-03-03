user

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
    return Trueassistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_31_code import is_prime

class TestIsPrime(unittest.TestCase):

    def test_is_prime_positive_numbers(self):
        self.assertFalse(is_prime(6))
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13441))
        self.assertTrue(is_prime(61))

    def test_is_prime_negative_numbers(self):
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-3))

    def test_is_prime_zero(self):
        self.assertFalse(is_prime(0))

    def test_is_prime_one(self):
        self.assertFalse(is_prime(1))

    def test_is_prime_two(self):
        self.assertTrue(is_prime(2))

    def test_is_prime_even_numbers(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(10))

    def test_is_prime_large_numbers(self):
        self.assertTrue(is_prime(1000003))
        self.assertTrue(is_prime(1000007))
        self.assertTrue(is_prime(1000013))

    def test_is_prime_edge_cases(self):
        self.assertFalse(is_prime(1.5))
        self.assertFalse(is_prime('a'))
        self.assertFalse(is_prime([1, 2, 3]))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various edge cases, including:

- Positive numbers
- Negative numbers
- Zero
- One
- Two
- Even numbers
- Large numbers
- Edge cases (non-integer inputs)

Each test method in the test suite is designed to test a specific aspect of the `is_prime` function. The `assert` statements in each test method are used to verify that the function behaves as expected.