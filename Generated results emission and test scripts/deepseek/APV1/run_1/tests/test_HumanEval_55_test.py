You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_55_code import fib

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(8), 21)
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(7), 13)
        self.assertEqual(fib(9), 34)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the first few Fibonacci numbers (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55) and also tests for the 10th Fibonacci number (55). The test suite also includes a test for the 0th Fibonacci number (0), which is a special case.

Please note that the function `fib(n)` is implemented using a recursive approach, which can be very slow for large values of `n`. For larger values of `n`, you might want to use an iterative approach or memoization to improve performance.