Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_106_code import f
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """

    ret = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            x = 1
            for j in range(1, i + 1):
                x *= j
            ret += [x]
        else:
            x = 0
            for j in range(1, i + 1):
                x += j
            ret += [x]
    return ret

 Here is a unittest test script for the provided function `f(n)`. The test cases cover various edge cases and ensure the function works as expected.


import unittest
from HumanEval_106_code import f

class TestFunctionF(unittest.TestCase):

    def test_f_with_positive_integer(self):
        self.assertEqual(f(1), [1])
        self.assertEqual(f(2), [1, 1])
        self.assertEqual(f(3), [1, 2, 1])
        self.assertEqual(f(4), [1, 2, 6, 1])
        self.assertEqual(f(5), [1, 2, 6, 24, 15])
        self.assertEqual(f(6), [1, 2, 6, 24, 120, 72])
        self.assertEqual(f(7), [1, 2, 6, 24, 120, 720, 5041])

    def test_f_with_zero(self):
        self.assertEqual(f(0), [])

    def test_f_with_negative_integer(self):
        self.assertEqual(f(-1), [])
        self.assertEqual(f(-2), [])
        self.assertEqual(f(-3), [])

if __name__ == '__main__':
    unittest.main()


This test script includes three test cases:

1. `test_f_with_positive_integer` checks the function with positive integers from 1 to 7.
2. `test_f_with_zero` checks the function with zero.
3. `test_f_with_negative_integer` checks the function with negative integers.

You can run this test script directly by saving it as a .py file and executing it using the command `python filename.py`. The output should show the test results, indicating whether the tests passed or failed.