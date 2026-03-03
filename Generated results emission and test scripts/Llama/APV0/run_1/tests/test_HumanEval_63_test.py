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
    return fibfib(n - 1) + fibfib(n - 2) + fibfib(n - 3)assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_63_code import fibfib

class TestFibFib(unittest.TestCase):

    def test_fibfib_zero(self):
        self.assertEqual(fibfib(0), 0)

    def test_fibfib_one(self):
        self.assertEqual(fibfib(1), 0)

    def test_fibfib_two(self):
        self.assertEqual(fibfib(2), 1)

    def test_fibfib_three(self):
        self.assertEqual(fibfib(3), 2)

    def test_fibfib_five(self):
        self.assertEqual(fibfib(5), 4)

    def test_fibfib_eight(self):
        self.assertEqual(fibfib(8), 24)

    def test_fibfib_negative(self):
        with self.assertRaises(ValueError):
            fibfib(-1)

    def test_fibfib_non_integer(self):
        with self.assertRaises(TypeError):
            fibfib('a')

if __name__ == '__main__':
    unittest.main()


This script includes tests for the base cases (0, 1, 2), a few larger cases (3, 5, 8), and also tests for invalid inputs (negative number and non-integer).