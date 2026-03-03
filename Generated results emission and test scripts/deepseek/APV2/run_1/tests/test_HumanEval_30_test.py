You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_30_code import get_positive

class TestGetPositive(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

    def test_negative_numbers(self):
        self.assertEqual(get_positive([-1, -2, -4, -5, -6]), [])
        self.assertEqual(get_positive([-5, -3, -5, -2, -3, -9, -123, -1]), [])

    def test_mixed_numbers(self):
        self.assertEqual(get_positive([-1, 0, 2, -4, 5, 6]), [2, 5, 6])
        self.assertEqual(get_positive([-5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [3, 2, 3, 9, 123, 1])

    def test_empty_list(self):
        self.assertEqual(get_positive([]), [])

    def test_single_positive_number(self):
        self.assertEqual(get_positive([5]), [5])

    def test_single_negative_number(self):
        self.assertEqual(get_positive([-5]), [])

    def test_single_zero(self):
        self.assertEqual(get_positive([0]), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- All positive numbers
- All negative numbers
- Mixed positive and negative numbers
- Empty list
- Single positive number
- Single negative number
- Single zero

Each test checks that the function returns the correct list of positive numbers for a given input list.