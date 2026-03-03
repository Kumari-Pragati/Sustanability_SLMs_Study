user

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
    return Falseassistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_57_code import monotonic

class TestMonotonic(unittest.TestCase):

    def test_monotonic_increasing(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))
        self.assertTrue(monotonic([0, 1, 2, 3]))
        self.assertTrue(monotonic([-10, -5, 0, 5]))

    def test_monotonic_decreasing(self):
        self.assertTrue(monotonic([20, 10, 5, 1]))
        self.assertTrue(monotonic([5, 3, 1, 0]))
        self.assertTrue(monotonic([-5, -10, -20, -30]))

    def test_monotonic_mixed(self):
        self.assertFalse(monotonic([1, 20, 4, 10]))
        self.assertFalse(monotonic([5, 3, 8, 2]))
        self.assertFalse(monotonic([-10, 0, 5, -20]))

    def test_monotonic_single_element(self):
        self.assertTrue(monotonic([1]))
        self.assertTrue(monotonic([-1]))
        self.assertTrue(monotonic([0]))

    def test_monotonic_empty_list(self):
        self.assertTrue(monotonic([]))

    def test_monotonic_non_list_input(self):
        with self.assertRaises(TypeError):
            monotonic(123)
        with self.assertRaises(TypeError):
            monotonic("hello")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the following cases:

- Monotonic increasing lists
- Monotonic decreasing lists
- Mixed lists (not monotonic)
- Single-element lists
- Empty lists
- Non-list inputs (to test error handling)

Each test case uses the `assertTrue` or `assertFalse` methods to verify that the function returns the expected result. The `assertRaises` method is used to test that the function raises a `TypeError` when given a non-list input.