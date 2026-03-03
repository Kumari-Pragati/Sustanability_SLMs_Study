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

 Here is a comprehensive unittest test suite for the given Python function `monotonic`. The test cases cover various scenarios including monotonically increasing, monotonically decreasing, and non-monotonic lists.


import unittest
from HumanEval_57_code import monotonic

class TestMonotonic(unittest.TestCase):

    def test_monotonic_increasing(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))
        self.assertTrue(monotonic([1, 2, 3, 4, 5]))
        self.assertTrue(monotonic([10, 20, 30, 40, 50]))

    def test_monotonic_decreasing(self):
        self.assertTrue(monotonic([4, 3, 2, 1]))
        self.assertTrue(monotonic([10, 9, 8, 7]))
        self.assertTrue(monotonic([50, 40, 30, 20]))

    def test_non_monotonic(self):
        self.assertFalse(monotonic([1, 20, 4, 10]))
        self.assertFalse(monotonic([4, 1, 0, -10]))
        self.assertFalse(monotonic([2, 1, 3, 2, 1]))

    def test_empty_list(self):
        self.assertTrue(monotonic([]))

    def test_single_element_list(self):
        self.assertTrue(monotonic([1]))
        self.assertTrue(monotonic([-1]))

    def test_duplicate_elements(self):
        self.assertTrue(monotonic([1, 1, 2, 3]))
        self.assertTrue(monotonic([-1, -1, -2, -3]))

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to ensure the function `monotonic` works as expected for different input scenarios.