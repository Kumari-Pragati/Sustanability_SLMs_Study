You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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
    return False

 Here is a comprehensive unittest test suite for the `monotonic` function:


import unittest
from HumanEval_57_code import monotonic

class TestMonotonic(unittest.TestCase):

    def test_monotonic_increasing(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))
        self.assertTrue(monotonic([0, 1, 2, 3, 4]))
        self.assertTrue(monotonic([-10, -5, -2, -1, 0]))

    def test_monotonic_decreasing(self):
        self.assertTrue(monotonic([4, 3, 2, 1]))
        self.assertTrue(monotonic([10, 9, 8, 7]))
        self.assertTrue(monotonic([0, -1, -2, -5, -10]))

    def test_non_monotonic(self):
        self.assertFalse(monotonic([1, 20, 4, 10]))
        self.assertFalse(monotonic([4, 1, 0, -10, 5]))
        self.assertFalse(monotonic([1, 2, 3, 2, 1]))

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_monotonic_increasing` checks that the function correctly identifies monotonically increasing lists.
2. `test_monotonic_decreasing` checks that the function correctly identifies monotonically decreasing lists.
3. `test_non_monotonic` checks that the function correctly identifies non-monotonic lists.

Each test case uses the `assertTrue` and `assertFalse` methods to verify the expected behavior of the `monotonic` function.