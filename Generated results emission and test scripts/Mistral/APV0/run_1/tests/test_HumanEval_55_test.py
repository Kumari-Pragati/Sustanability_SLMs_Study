Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_55_code import fib
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

 Here is a unittest test script for the provided `fib` function:


import unittest
from HumanEval_55_code import fib

class TestFibonacci(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(3), 2)
        self.assertEqual(fib(4), 3)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(6), 8)
        self.assertEqual(fib(7), 13)
        self.assertEqual(fib(8), 21)
        self.assertEqual(fib(9), 34)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(20), 6765)
        self.assertEqual(fib(30), 832040)
        self.assertEqual(fib(40), 102334155)
        self.assertEqual(fib(50), 354224848179261915075)
        self.assertEqual(fib(60), 51096022018834563162891891661)
        self.assertEqual(fib(70), 79788456980785627660447136816683778147)
        self.assertEqual(fib(80), 1258626902533572036856188327666049288206647093)
        self.assertEqual(fib(90), 1953667033441436021043901696347551188092586969)
        self.assertEqual(fib(100), 2971215073819619326617283064569204686403918981)

if __name__ == '__main__':
    unittest.main()


This test script includes a `TestFibonacci` class that contains a single method, `test_fib`, which tests the `fib` function for various input values. The test cases cover a range of small and large Fibonacci numbers to ensure the function works correctly for different cases. The script ends with the standard boilerplate for running the unittest tests.