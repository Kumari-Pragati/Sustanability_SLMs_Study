system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_150_code import x_or_y
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def x_or_y(n, x, y):
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    for x_or_y(7, 34, 12) == 34
    for x_or_y(15, 8, 5) == 5
    
    """
    if n == 1:
        return y
    for i in range(2, n):
        if n % i == 0:
            return y
            break
    else:
        return x


assistant

import unittest

# Importing the function from the given code snippet
from HumanEval_150_code import x_or_y

class TestXOrY(unittest.TestCase):

    def test_prime_returns_x(self):
        self.assertEqual(x_or_y(7, 34, 12), 34)

    def test_non_prime_returns_y(self):
        self.assertEqual(x_or_y(15, 8, 5), 5)

    def test_one_returns_y(self):
        self.assertEqual(x_or_y(1, 9, 6), 6)

    def test_zero_returns_y(self):
        self.assertEqual(x_or_y(0, 10, 2), 2)

    def test_negative_number_returns_y(self):
        self.assertEqual(x_or_y(-5, -1, -3), -3)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various scenarios as described in the docstring of `x_or_y` function. It covers both prime numbers and non-prime numbers, as well as edge cases like one and zero/negative numbers.