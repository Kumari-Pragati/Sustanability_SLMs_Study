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

 import unittest
from HumanEval_63_code import fibfib

class TestFibFib(unittest.TestCase):

    def test_fibfib_base_cases(self):
        self.assertEqual(fibfib(0), 0)
        self.assertEqual(fibfib(1), 0)
        self.assertEqual(fibfib(2), 1)

    def test_fibfib_positive_integers(self):
        self.assertEqual(fibfib(3), 2)
        self.assertEqual(fibfib(4), 4)
        self.assertEqual(fibfib(5), 4)
        self.assertEqual(fibfib(6), 7)
        self.assertEqual(fibfib(7), 13)
        self.assertEqual(fibfib(8), 24)
        self.assertEqual(fibfib(9), 44)
        self.assertEqual(fibfib(10), 81)

    def test_fibfib_large_integers(self):
        self.assertEqual(fibfib(11), 149)
        self.assertEqual(fibfib(12), 288)
        self.assertEqual(fibfib(13), 534)
        self.assertEqual(fibfib(14), 990)
        self.assertEqual(fibfib(15), 1754)

    def test_fibfib_edge_cases(self):
        self.assertEqual(fibfib(-1), 0)  # Assuming the function handles negative inputs gracefully
        self.assertEqual(fibfib(100), 1000000)  # Assuming the function can handle large inputs

if __name__ == '__main__':
    unittest.main()