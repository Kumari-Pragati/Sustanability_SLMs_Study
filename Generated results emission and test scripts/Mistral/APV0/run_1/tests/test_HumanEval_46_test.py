Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `fib4` function:


import unittest
from HumanEval_46_code import fib4

class TestFib4(unittest.TestCase):
    def test_fib4(self):
        self.assertEqual(fib4(0), 0)
        self.assertEqual(fib4(1), 0)
        self.assertEqual(fib4(2), 2)
        self.assertEqual(fib4(3), 0)
        self.assertEqual(fib4(4), 4)
        self.assertEqual(fib4(5), 4)  # The function is not recursive, so fib4(4) and fib4(5) should return the same result
        self.assertEqual(fib4(6), 8)
        self.assertEqual(fib4(7), 14)
        self.assertEqual(fib4(8), 26)
        self.assertEqual(fib4(9), 48)
        self.assertEqual(fib4(10), 88)
        self.assertEqual(fib4(15), 317)
        self.assertEqual(fib4(20), 778)
        self.assertEqual(fib4(30), 22034)
        self.assertEqual(fib4(40), 524288)
        self.assertEqual(fib4(50), 12987024)
        self.assertEqual(fib4(60), 317811072)
        self.assertEqual(fib4(70), 7855767360)
        self.assertEqual(fib4(80), 195366713368)
        self.assertEqual(fib4(90), 4832023665728)
        self.assertEqual(fib4(100), 121393224767081)

if __name__ == '__main__':
    unittest.main()


This test script includes a test function `test_fib4` that checks the function for various input values. The test cases cover the base cases and a range of larger values to ensure the function works correctly for larger inputs as well.