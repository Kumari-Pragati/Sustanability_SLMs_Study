You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the provided Python function `f(n)`. I've created several test cases to cover different scenarios, including edge cases and common input values.


import unittest
from HumanEval_106_code import f

class TestFunctionF(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(f(0), [])

    def test_single_element(self):
        self.assertEqual(f(1), [1])

    def test_even_numbers(self):
        self.assertEqual(f(2), [1, 1])
        self.assertEqual(f(4), [1, 2, 24, 24])
        self.assertEqual(f(6), [1, 2, 6, 72, 90, 90])

    def test_odd_numbers(self):
        self.assertEqual(f(3), [1, 2, 3])
        self.assertEqual(f(5), [1, 2, 6, 15, 31])
        self.assertEqual(f(7), [1, 2, 6, 15, 28, 42, 56])

    def test_large_number(self):
        self.assertEqual(f(100), [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000, 2432902008176640000])

if __name__ == '__main__':
    unittest.main()


This test suite includes a test for an empty list, single-element lists, even numbers, odd numbers, and a large number. The test suite will run automatically when you run the script.