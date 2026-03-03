system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_63_code import fibfib
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)


assistant

import unittest

# Importing the fibfib function from the given code snippet
from HumanEval_63_code import fibfib

class TestFibfib(unittest.TestCase):

    def test_fibfib(self):
        # Test cases to verify the correctness of the fibfib function
        self.assertEqual(fibfib(1), 0)
        self.assertEqual(fibfib(5), 4)
        self.assertEqual(fibfib(8), 24)
        self.assertEqual(fibfib(9), 40)
        self.assertEqual(fibfib(10), 72)

if __name__ == '__main__':
    unittest.main()


This script imports the `fibfib` function from the provided code snippet and defines a class `TestFibfib` within a module named `unittest`. It contains a method `test_fibfib` which includes several assertions to check the correctness of the `fibfib` function against known values. The `unittest.main()` call at the end makes the tests executable when run directly.