Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 import unittest
from HumanEval_30_code import get_positive

class TestGetPositive(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(get_positive([-1, 2, -4, 5, 6]), [2, 5, 6])

    def test_mixed_numbers(self):
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

    def test_all_positive(self):
        self.assertEqual(get_positive([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_no_positive(self):
        self.assertEqual(get_positive([-1, -2, -3, -4, -5]), [])

    def test_empty_list(self):
        self.assertEqual(get_positive([]), [])

    def test_single_positive(self):
        self.assertEqual(get_positive([1]), [1])

    def test_single_negative(self):
        self.assertEqual(get_positive([-1]), [])

if __name__ == '__main__':
    unittest.main()