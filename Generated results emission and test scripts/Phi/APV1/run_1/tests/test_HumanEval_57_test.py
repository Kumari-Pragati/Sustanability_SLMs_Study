You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_57_code import monotonic

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False

 import unittest
from HumanEval_57_code import monotonic

class TestMonotonic(unittest.TestCase):

    def test_increasing(self):
        self.assertTrue(monotonic([1, 2, 4, 20]), "The list [1, 2, 4, 20] should be monotonically increasing")

    def test_decreasing(self):
        self.assertTrue(monotonic([20, 4, 1, 0]), "The list [20, 4, 1, 0] should be monotonically decreasing")

    def test_not_monotonic(self):
        self.assertFalse(monotonic([1, 20, 4, 10]), "The list [1, 20, 4, 10] should not be monotonically increasing or decreasing")

    def test_empty_list(self):
        self.assertTrue(monotonic([]), "An empty list should be considered monotonically increasing")

    def test_single_element_list(self):
        self.assertTrue(monotonic([1]), "A single element list should be considered monotonically increasing")

    def test_duplicate_elements(self):
        self.assertTrue(monotonic([1, 1, 1]), "A list with duplicate elements should be considered monotonically increasing")

    def test_mixed_elements(self):
        self.assertTrue(monotonic([1, 2, 1, 3]), "A list with mixed elements should be considered monotonically increasing")

if __name__ == '__main__':
    unittest.main()