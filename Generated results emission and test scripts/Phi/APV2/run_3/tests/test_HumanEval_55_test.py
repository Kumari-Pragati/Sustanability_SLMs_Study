You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

    def test_fib_edge_case(self):
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)

    def test_fib_negative_integers(self):
        with self.assertRaises(ValueError):
            fib(-1)

if __name__ == '__main__':
    unittest.main()