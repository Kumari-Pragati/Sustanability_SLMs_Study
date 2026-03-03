You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_55_code import fib
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

 Here is a complete unittest test suite for the provided `fib` function:


import unittest
from HumanEval_55_code import fib

class TestFibonacci(unittest.TestCase):
    def test_fib_with_positive_numbers(self):
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(7), 13)
        self.assertEqual(fib(8), 21)
        self.assertEqual(fib(9), 34)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(20), 6765)
        self.assertEqual(fib(30), 832040)
        self.assertEqual(fib(40), 102334155)
        self.assertEqual(fib(50), 354224848179261915075)

    def test_fib_with_zero(self):
        self.assertEqual(fib(0), 0)

    def test_fib_with_negative_numbers(self):
        with self.assertRaises(ValueError):
            fib(-1)
        with self.assertRaises(ValueError):
            fib(-2)
        with self.assertRaises(ValueError):
            fib(-3)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_fib_with_positive_numbers` checks the function's output for positive numbers up to 50.
2. `test_fib_with_zero` checks the function's output for the zero input.
3. `test_fib_with_negative_numbers` checks if the function raises a `ValueError` for negative inputs.