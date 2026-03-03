system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return Falseassistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_57_code import monotonic

class TestMonotonic(unittest.TestCase):

    def test_monotonic_increasing(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))

    def test_monotonic_decreasing(self):
        self.assertTrue(monotonic([4, 1, 0, -10]))

    def test_monotonic_neither(self):
        self.assertFalse(monotonic([1, 20, 4, 10]))

    def test_monotonic_single_element(self):
        self.assertTrue(monotonic([1]))

    def test_monotonic_empty_list(self):
        self.assertTrue(monotonic([]))

    def test_monotonic_single_element_decreasing(self):
        self.assertTrue(monotonic([-1]))

    def test_monotonic_all_equal(self):
        self.assertTrue(monotonic([1, 1, 1, 1]))

    def test_monotonic_all_equal_decreasing(self):
        self.assertTrue(monotonic([-1, -1, -1, -1]))

    def test_monotonic_mixed(self):
        self.assertFalse(monotonic([1, 2, 3, 4, 5, 0]))

    def test_monotonic_mixed_decreasing(self):
        self.assertFalse(monotonic([5, 4, 3, 2, 1, 0]))

if __name__ == '__main__':
    unittest.main()