You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a simple unittest test suite for the `fibfib` function. I've included tests for the base cases (0, 1, and 2) and some additional tests to ensure the function correctly computes FibFib numbers for various inputs.


import unittest
from HumanEval_63_code import fibfib

class TestFibFib(unittest.TestCase):
    def test_base_cases(self):
        self.assertEqual(fibfib(0), 0)
        self.assertEqual(fibfib(1), 0)
        self.assertEqual(fibfib(2), 1)

    def test_small_numbers(self):
        self.assertEqual(fibfib(3), 1)
        self.assertEqual(fibfib(4), 2)
        self.assertEqual(fibfib(5), 4)

    def test_large_numbers(self):
        self.assertEqual(fibfib(8), 24)
        self.assertEqual(fibfib(13), 144)
        self.assertEqual(fibfib(20), 6724)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            fibfib(-1)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for base cases, small numbers, large numbers, and negative numbers. The `assertRaises` method is used to test for the expected ValueError when a negative number is passed to the function.