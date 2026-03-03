You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return sum(range(n + 1))

 Here is a complete unittest test suite for the `sum_to_n` function:


import unittest
from HumanEval_60_code import sum_to_n

class TestSumToN(unittest.TestCase):
    def test_sum_to_n_with_positive_integer(self):
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(1), 1)

    def test_sum_to_n_with_zero(self):
        self.assertEqual(sum_to_n(0), 0)

    def test_sum_to_n_with_negative_integer(self):
        with self.assertRaises(ValueError):
            sum_to_n(-1)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_sum_to_n_with_positive_integer` checks the function's behavior with positive integers.
2. `test_sum_to_n_with_zero` checks the function's behavior with zero.
3. `test_sum_to_n_with_negative_integer` checks the function's behavior with negative integers.

The last test case uses the `assertRaises` method to check if the function raises a `ValueError` when given a negative integer.