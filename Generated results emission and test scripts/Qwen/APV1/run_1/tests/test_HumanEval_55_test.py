system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return fib(n - 1) + fib(n - 2)


assistant

import unittest

# Function to be tested
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


This code snippet defines a `TestFibonacci` class that inherits from `unittest.TestCase`. It contains a single method `test_fib`, which tests the `fib` function using assertions. The `assertEqual` methods check if the output of `fib` matches the expected values for different inputs. If any assertion fails, it will raise an error indicating which input caused the failure.