system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_46_code import fib4
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence. Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """
    results = [0, 0, 2, 0]
    if n < 4:
        return results[n]

    for _ in range(4, n + 1):
        results.append(results[-1] + results[-2] + results[-3] + results[-4])
        results.pop(0)

    return results[-1]assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_46_code import fib4

class TestFib4(unittest.TestCase):

    def test_fib4_0(self):
        self.assertEqual(fib4(0), 0)

    def test_fib4_1(self):
        self.assertEqual(fib4(1), 0)

    def test_fib4_2(self):
        self.assertEqual(fib4(2), 2)

    def test_fib4_3(self):
        self.assertEqual(fib4(3), 0)

    def test_fib4_4(self):
        self.assertEqual(fib4(4), 2)

    def test_fib4_5(self):
        self.assertEqual(fib4(5), 4)

    def test_fib4_6(self):
        self.assertEqual(fib4(6), 8)

    def test_fib4_7(self):
        self.assertEqual(fib4(7), 14)

    def test_fib4_8(self):
        self.assertEqual(fib4(8), 26)

    def test_fib4_9(self):
        self.assertEqual(fib4(9), 44)

    def test_fib4_10(self):
        self.assertEqual(fib4(10), 72)

    def test_fib4_negative(self):
        with self.assertRaises(ValueError):
            fib4(-1)

    def test_fib4_non_integer(self):
        with self.assertRaises(TypeError):
            fib4('a')

if __name__ == '__main__':
    unittest.main()