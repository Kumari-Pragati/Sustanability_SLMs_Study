Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
        self.assertTrue(monotonic([1, 2, 4, 20]))

    def test_decreasing(self):
        self.assertTrue(monotonic([20, 4, 1, 0]))

    def test_non_monotonic(self):
        self.assertFalse(monotonic([1, 20, 4, 10]))

    def test_empty_list(self):
        self.assertTrue(monotonic([]))

    def test_single_element_list(self):
        self.assertTrue(monotonic([1]))

    def test_duplicate_elements(self):
        self.assertTrue(monotonic([1, 1, 1, 1]))

    def test_mixed_elements(self):
        self.assertFalse(monotonic([1, 3, 2, 4]))

if __name__ == '__main__':
    unittest.main()