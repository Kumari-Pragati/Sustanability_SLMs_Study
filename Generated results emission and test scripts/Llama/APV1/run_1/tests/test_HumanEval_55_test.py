user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
    return fib(n - 1) + fib(n - 2)assistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_55_code import fib

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_base_cases(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)

    def test_fibonacci_small_values(self):
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(7), 13)
        self.assertEqual(fib(8), 21)
        self.assertEqual(fib(9), 34)
        self.assertEqual(fib(10), 55)

    def test_fibonacci_large_values(self):
        self.assertEqual(fib(11), 89)
        self.assertEqual(fib(12), 144)
        self.assertEqual(fib(13), 233)
        self.assertEqual(fib(14), 377)
        self.assertEqual(fib(15), 610)
        self.assertEqual(fib(16), 987)
        self.assertEqual(fib(17), 1597)
        self.assertEqual(fib(18), 2584)
        self.assertEqual(fib(19), 4181)
        self.assertEqual(fib(20), 6765)

    def test_fibonacci_invalid_input(self):
        with self.assertRaises(TypeError):
            fib('a')
        with self.assertRaises(TypeError):
            fib(None)
        with self.assertRaises(TypeError):
            fib(1.5)

if __name__ == '__main__':
    unittest.main()


This test suite includes the following test cases:

- `test_fibonacci_base_cases`: Tests the base cases of the Fibonacci function, i.e., when n is 0 or 1.
- `test_fibonacci_small_values`: Tests the Fibonacci function for small values of n.
- `test_fibonacci_large_values`: Tests the Fibonacci function for large values of n.
- `test_fibonacci_invalid_input`: Tests the Fibonacci function with invalid input, such as strings, None, and non-integer values.