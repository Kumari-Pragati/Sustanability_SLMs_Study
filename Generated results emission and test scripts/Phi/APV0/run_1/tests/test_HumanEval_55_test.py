Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

    def test_fib_edge_cases(self):
        self.assertEqual(fib(-1), None)  # Assuming the function should handle negative inputs
        self.assertEqual(fib(21), 10946)

    def test_fib_large_numbers(self):
        # Testing with a larger number to ensure the function can handle it
        # Note: This may take a long time to compute
        self.assertEqual(fib(30), 832040)

if __name__ == '__main__':
    unittest.main()