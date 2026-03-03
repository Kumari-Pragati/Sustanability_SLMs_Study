You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_46_code import fib4

class TestFib4(unittest.TestCase):
    def test_fib4_base_cases(self):
        self.assertEqual(fib4(0), 0)
        self.assertEqual(fib4(1), 0)
        self.assertEqual(fib4(2), 2)
        self.assertEqual(fib4(3), 0)

    def test_fib4_positive_numbers(self):
        self.assertEqual(fib4(5), 4)
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)
        self.assertEqual(fib4(8), 24)
        self.assertEqual(fib4(9), 40)

    def test_fib4_negative_number(self):
        with self.assertRaises(IndexError):
            fib4(-1)

    def test_fib4_large_number(self):
        self.assertEqual(fib4(10), 112)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the base cases, positive numbers, negative numbers, and large numbers. It checks that the function returns the correct values for these cases and that it raises an `IndexError` when given a negative number.

Please note that the function `fib4` is expected to be in a file named `HumanEval_46_code.py` in the same directory as the test file.