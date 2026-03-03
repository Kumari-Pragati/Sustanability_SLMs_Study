user

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
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 *... * i).
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
    return retassistant

Here is the unittest test script for the function `f`:

import unittest
from HumanEval_106_code import f

class TestF(unittest.TestCase):
    def test_f_1(self):
        self.assertEqual(f(1), [1])

    def test_f_2(self):
        self.assertEqual(f(2), [1, 2])

    def test_f_3(self):
        self.assertEqual(f(3), [1, 2, 3])

    def test_f_4(self):
        self.assertEqual(f(4), [1, 2, 6, 24])

    def test_f_5(self):
        self.assertEqual(f(5), [1, 2, 6, 24, 15])

    def test_f_6(self):
        self.assertEqual(f(6), [1, 2, 6, 24, 30, 90])

    def test_f_7(self):
        self.assertEqual(f(7), [1, 2, 6, 24, 30, 90, 36])

    def test_f_8(self):
        self.assertEqual(f(8), [1, 2, 6, 24, 30, 90, 36, 120])

    def test_f_9(self):
        self.assertEqual(f(9), [1, 2, 6, 24, 30, 90, 36, 120, 45])

    def test_f_10(self):
        self.assertEqual(f(10), [1, 2, 6, 24, 30, 90, 36, 120, 45, 210])

if __name__ == '__main__':
    unittest.main()

This script defines a `TestF` class that contains 10 test methods, each testing the function `f` with a different input value. The `assertEqual` method is used to check that the output of the function matches the expected result.