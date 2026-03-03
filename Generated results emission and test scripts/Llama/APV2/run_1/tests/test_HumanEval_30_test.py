system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    return [e for e in l if e > 0]assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_30_code import get_positive

class TestGetPositive(unittest.TestCase):

    def test_get_positive(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

    def test_get_positive_empty_list(self):
        self.assertEqual(get_positive([]), [])

    def test_get_positive_single_element(self):
        self.assertEqual(get_positive([5]), [5])

    def test_get_positive_negative_numbers(self):
        self.assertEqual(get_positive([-1, -2, -3]), [])

    def test_get_positive_zero(self):
        self.assertEqual(get_positive([0]), [])

    def test_get_positive_mixed(self):
        self.assertEqual(get_positive([1, -2, 3, 0, -4, 5]), [1, 3, 5])

if __name__ == '__main__':
    unittest.main()