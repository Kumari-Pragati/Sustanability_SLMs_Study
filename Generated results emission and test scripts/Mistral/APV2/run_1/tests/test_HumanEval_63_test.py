You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is a complete unittest test suite for the `fibfib` function:


import unittest
from HumanEval_63_code import fibfib

class TestFibFib(unittest.TestCase):
    def test_fibfib_base_cases(self):
        self.assertEqual(fibfib(0), 0)
        self.assertEqual(fibfib(1), 0)
        self.assertEqual(fibfib(2), 1)

    def test_fibfib_small_values(self):
        self.assertEqual(fibfib(3), 1)
        self.assertEqual(fibfib(4), 2)
        self.assertEqual(fibfib(5), 4)

    def test_fibfib_large_values(self):
        self.assertEqual(fibfib(6), 7)
        self.assertEqual(fibfib(7), 13)
        self.assertEqual(fibfib(8), 24)
        self.assertEqual(fibfib(9), 44)
        self.assertEqual(fibfib(10), 81)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test methods:

1. `test_fibfib_base_cases`: Tests the base cases of the function (fibfib(0), fibfib(1), and fibfib(2)).
2. `test_fibfib_small_values`: Tests the function for small values (fibfib(3) to fibfib(5)).
3. `test_fibfib_large_values`: Tests the function for larger values (fibfib(6) to fibfib(10)).

You can run the test suite by executing the script. If the function is correct, all tests should pass. If any test fails, the test method and the expected and actual results will be displayed.