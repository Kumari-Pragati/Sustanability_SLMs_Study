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
    return fib(n - 1) + fib(n - 2)

 import unittest
from HumanEval_55_code import fib

class TestFibonacciFunction(unittest.TestCase):

    def test_fib_base_cases(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(8), 21)

    def test_fib_positive_integers(self):
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(15), 610)
        self.assertEqual(fib(20), 6765)

    def test_fib_large_integers(self):
        self.assertEqual(fib(50), 12586269025)
        self.assertEqual(fib(100), 354224848179261915075)

    def test_fib_edge_cases(self):
        with self.assertRaises(ValueError):
            fib(-1)
        with self.assertRaises(TypeError):
            fib("string")

if __name__ == '__main__':
    unittest.main()