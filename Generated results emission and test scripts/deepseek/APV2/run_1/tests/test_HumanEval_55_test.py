You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


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
        self.assertEqual(fib(13), 233)
        self.assertEqual(fib(14), 377)
        self.assertEqual(fib(15), 610)
        self.assertEqual(fib(16), 987)
        self.assertEqual(fib(17), 1597)
        self.assertEqual(fib(18), 2584)
        self.assertEqual(fib(19), 4181)
        self.assertEqual(fib(20), 6765)

if __name__ == '__main__':
    unittest.main()


This test suite includes a single test case, `test_fibonacci`, which tests the `fib` function for a range of input values. Each test case checks that the output of the `fib` function matches the expected result.

Please note that the `fib` function is implemented using a recursive approach, which is not efficient for large input values. The time complexity of the `fib` function is O(2^n), which makes it impractical to test the function for large input values.

If you want to test the function for large input values, you should consider implementing an iterative approach or using memoization to improve the efficiency of the function.