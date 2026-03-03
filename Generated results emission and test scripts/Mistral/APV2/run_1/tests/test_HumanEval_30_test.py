You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `get_positive` function:


import unittest
from HumanEval_30_code import get_positive

class TestGetPositive(unittest.TestCase):

    def test_get_positive_empty_list(self):
        self.assertListEqual(get_positive([]), [])

    def test_get_positive_all_negative(self):
        self.assertListEqual(get_positive([-1, -2, -3]), [])

    def test_get_positive_all_positive(self):
        self.assertListEqual(get_positive([1, 2, 3]), [1, 2, 3])

    def test_get_positive_mixed_numbers(self):
        self.assertListEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
        self.assertListEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases to cover different scenarios: an empty list, a list with all negative numbers, a list with all positive numbers, and a list with mixed numbers. The `assertListEqual` function is used to compare the expected output with the actual output of the `get_positive` function.