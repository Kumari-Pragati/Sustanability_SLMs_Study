You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_63_code import fibfib

class TestFibFib(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(fibfib(0), 0)

    def test_one(self):
        self.assertEqual(fibfib(1), 0)

    def test_two(self):
        self.assertEqual(fibfib(2), 1)

    def test_three(self):
        self.assertEqual(fibfib(3), 1)

    def test_four(self):
        self.assertEqual(fibfib(4), 2)

    def test_five(self):
        self.assertEqual(fibfib(5), 4)

    def test_six(self):
        self.assertEqual(fibfib(6), 7)

    def test_seven(self):
        self.assertEqual(fibfib(7), 13)

    def test_eight(self):
        self.assertEqual(fibfib(8), 24)

    def test_negative(self):
        with self.assertRaises(Exception):
            fibfib(-1)

    def test_non_integer(self):
        with self.assertRaises(Exception):
            fibfib(1.5)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the first few positive integers, as well as tests for negative numbers and non-integers. It uses the `unittest` framework's `assertRaises` method to check that the function raises an exception when given invalid input.

Please note that the function `fibfib` is not optimized for large inputs, and so the tests for larger inputs (e.g., 7, 8) may take a long time to run.

Also, the function `fibfib` is not designed to handle floating-point numbers, so the test for `test_non_integer` will fail if the function is given a floating-point number.

If you want to optimize the function for larger inputs, you could use a technique called memoization to store the results of previous computations, which would significantly speed up the function for larger inputs.