user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_60_code import sum_to_n

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    return sum(range(n + 1))assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_60_code import sum_to_n

class TestSumToN(unittest.TestCase):

    def test_sum_to_n_positive_integer(self):
        self.assertEqual(sum_to_n(1), 1)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)

    def test_sum_to_n_zero(self):
        with self.assertRaises(ZeroDivisionError):
            sum_to_n(0)

    def test_sum_to_n_negative_integer(self):
        with self.assertRaises(ValueError):
            sum_to_n(-1)

    def test_sum_to_n_non_integer(self):
        with self.assertRaises(TypeError):
            sum_to_n('a')

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases:

1. `test_sum_to_n_positive_integer`: This test case checks the function with positive integers. It uses the `assertEqual` method to verify that the function returns the expected results.

2. `test_sum_to_n_zero`: This test case checks the function with zero. It uses the `assertRaises` method to verify that the function raises a `ZeroDivisionError` when called with zero.

3. `test_sum_to_n_negative_integer`: This test case checks the function with negative integers. It uses the `assertRaises` method to verify that the function raises a `ValueError` when called with a negative integer.

4. `test_sum_to_n_non_integer`: This test case checks the function with non-integer values. It uses the `assertRaises` method to verify that the function raises a `TypeError` when called with a non-integer value.