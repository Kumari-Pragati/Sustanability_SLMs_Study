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

 import unittest
from HumanEval_106_code import f

class TestF(unittest.TestCase):

    def test_factorial_of_even_numbers(self):
        self.assertEqual(f(2), [1, 2])
        self.assertEqual(f(4), [1, 2, 6, 24])
        self.assertEqual(f(6), [1, 2, 6, 24, 120, 720])

    def test_sum_of_numbers_for_odd_numbers(self):
        self.assertEqual(f(1), [1])
        self.assertEqual(f(3), [1, 3, 6])
        self.assertEqual(f(5), [1, 2, 6, 24, 15])

    def test_empty_list(self):
        self.assertEqual(f(0), [])

    def test_single_element_list(self):
        self.assertEqual(f(1), [1])

    def test_large_number(self):
        self.assertEqual(f(10), [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800])

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            f(-1)

if __name__ == '__main__':
    unittest.main()