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
    return sum(range(n + 1))

 Here is a simple unittest test suite for the `sum_to_n` function. I've included a variety of test cases to ensure the function works correctly for different input values.


import unittest
from HumanEval_60_code import sum_to_n

class TestSumToN(unittest.TestCase):
    def test_sum_to_n_positive_numbers(self):
        self.assertEqual(sum_to_n(1), 1)
        self.assertEqual(sum_to_n(5), 15)
        self.assertEqual(sum_to_n(10), 55)
        self.assertEqual(sum_to_n(30), 465)
        self.assertEqual(sum_to_n(100), 5050)
        self.assertEqual(sum_to_n(1000), 500050)

    def test_sum_to_n_zero(self):
        self.assertEqual(sum_to_n(0), 0)

    def test_sum_to_n_negative_numbers(self):
        self.assertEqual(sum_to_n(-1), 0)
        self.assertEqual(sum_to_n(-5), 0)
        self.assertEqual(sum_to_n(-10), 0)
        self.assertEqual(sum_to_n(-30), 0)
        self.assertEqual(sum_to_n(-100), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive numbers, zero, and negative numbers. It uses the `assertEqual` method to check if the output of the `sum_to_n` function matches the expected result for each test case.