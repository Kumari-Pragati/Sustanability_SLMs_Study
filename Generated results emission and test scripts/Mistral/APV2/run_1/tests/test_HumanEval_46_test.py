You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

    return results[-1]

 Here is the complete unittest test suite for the `fib4` function:


import unittest
from HumanEval_46_code import fib4

class TestFib4(unittest.TestCase):

    def test_fib4_with_small_values(self):
        self.assertEqual(fib4(0), 0)
        self.assertEqual(fib4(1), 0)
        self.assertEqual(fib4(2), 2)
        self.assertEqual(fib4(3), 0)

    def test_fib4_with_positive_values(self):
        self.assertEqual(fib4(4), 4)
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)
        self.assertEqual(fib4(8), 26)
        self.assertEqual(fib4(9), 46)
        self.assertEqual(fib4(10), 80)

    def test_fib4_with_negative_values(self):
        self.assertRaises(ValueError, fib4, -1)
        self.assertRaises(ValueError, fib4, -2)
        self.assertRaises(ValueError, fib4, -3)
        self.assertRaises(ValueError, fib4, -4)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_fib4_with_small_values`: Tests the function with small values (0 to 3) to ensure it returns the expected values.
2. `test_fib4_with_positive_values`: Tests the function with positive values greater than 3 to ensure it returns the expected values.
3. `test_fib4_with_negative_values`: Tests the function with negative values to ensure it raises a `ValueError` exception.