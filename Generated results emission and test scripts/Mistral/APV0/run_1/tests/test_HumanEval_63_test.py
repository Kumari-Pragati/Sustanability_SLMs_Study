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

 Here is a unittest test script for the `fibfib` function:


import unittest
from HumanEval_63_code import fibfib

class TestFibFib(unittest.TestCase):
    def test_fibfib(self):
        self.assertEqual(fibfib(0), 0)
        self.assertEqual(fibfib(1), 0)
        self.assertEqual(fibfib(2), 1)
        self.assertEqual(fibfib(3), 1)
        self.assertEqual(fibfib(4), 2)
        self.assertEqual(fibfib(5), 4)
        self.assertEqual(fibfib(6), 7)
        self.assertEqual(fibfib(7), 13)
        self.assertEqual(fibfib(8), 24)
        self.assertEqual(fibfib(9), 44)
        self.assertEqual(fibfib(10), 81)
        self.assertEqual(fibfib(15), 610)
        self.assertEqual(fibfib(20), 10946)
        self.assertEqual(fibfib(30), 3648008)
        self.assertEqual(fibfib(40), 140733206368580428800)

if __name__ == '__main__':
    unittest.main()


This test script includes a test function `test_fibfib` that checks the function for various input values. The test function uses the `assertEqual` method to compare the expected output with the actual output of the `fibfib` function. The test script also includes the necessary imports and the line to run the tests when the script is executed directly.