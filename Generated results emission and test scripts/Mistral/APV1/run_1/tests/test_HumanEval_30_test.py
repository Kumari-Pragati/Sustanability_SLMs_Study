You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_30_code import get_positive

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [e for e in l if e > 0]

 Here is a comprehensive unittest test suite for the given Python function `get_positive`:


import unittest
from HumanEval_30_code import get_positive

class TestGetPositive(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(get_positive([]), [])

    def test_all_positive(self):
        self.assertListEqual(get_positive([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_all_negative(self):
        self.assertListEqual(get_positive([-1, -2, -3, -4, -5]), [])

    def test_mixed_numbers(self):
        self.assertListEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
        self.assertListEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

    def test_zero(self):
        self.assertListEqual(get_positive([0]), [])
        self.assertListEqual(get_positive([0, 5]), [5])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty list, all positive numbers, all negative numbers, mixed numbers, and handling zero values. The `assertListEqual` function is used to compare the expected output with the actual output of the `get_positive` function.