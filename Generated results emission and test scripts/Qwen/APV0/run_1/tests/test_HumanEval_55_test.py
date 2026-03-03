system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return fib(n - 1) + fib(n - 2)


assistant

import unittest

# Importing the function to be tested
from HumanEval_55_code import fib

class TestFibonacci(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(8), 21)
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)

if __name__ == '__main__':
    unittest.main()


This script imports the `fib` function from the module `HumanEval_55_code`, defines a class `TestFibonacci` that inherits from `unittest.TestCase`, and includes methods to test the `fib` function with various inputs. The `assertEqual` method is used to check if the output of the `fib` function matches the expected values. Finally, the `unittest.main()` call runs all the tests in the `TestFibonacci` class.