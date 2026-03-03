user

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
    return fib(n - 1) + fib(n - 2)assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_55_code import fib

class TestFibonacci(unittest.TestCase):

    def test_fibonacci(self):
        self.assertEqual(fib(0), 0)
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
        self.assertEqual(fib(11), 89)
        self.assertEqual(fib(12), 144)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            fib(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            fib('a')

if __name__ == '__main__':
    unittest.main()


This script includes three test cases:

1. `test_fibonacci`: This test case checks the function with different inputs and verifies that the output is as expected.

2. `test_negative_input`: This test case checks that the function raises a `ValueError` when given a negative input.

3. `test_non_integer_input`: This test case checks that the function raises a `TypeError` when given a non-integer input.