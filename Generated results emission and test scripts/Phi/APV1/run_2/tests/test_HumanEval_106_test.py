You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_106_code import f

class TestF(unittest.TestCase):

    def test_f_even_index(self):
        # Test the function with even indices
        self.assertEqual(f(2), [1, 2])
        self.assertEqual(f(4), [1, 2, 6, 24])
        self.assertEqual(f(6), [1, 2, 6, 24, 120, 720])

    def test_f_odd_index(self):
        # Test the function with odd indices
        self.assertEqual(f(1), [0])
        self.assertEqual(f(3), [0, 1, 3])
        self.assertEqual(f(5), [1, 2, 6, 24, 15])

    def test_f_zero(self):
        # Test the function with n=0
        self.assertEqual(f(0), [])

    def test_f_negative(self):
        # Test the function with negative n
        with self.assertRaises(ValueError):
            f(-1)

    def test_f_large_n(self):
        # Test the function with a large value of n
        self.assertEqual(f(10), [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800])

if __name__ == '__main__':
    unittest.main()