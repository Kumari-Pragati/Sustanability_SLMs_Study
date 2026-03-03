user

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
    return Falseassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_57_code import monotonic

class TestMonotonic(unittest.TestCase):

    def test_monotonic_increasing(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))

    def test_monotonic_decreasing(self):
        self.assertTrue(monotonic([4, 1, 0, -10]))

    def test_monotonic_mixed(self):
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

if __name__ == '__main__':
    unittest.main()


This script includes 7 test cases to cover different scenarios:

- `test_monotonic_increasing`: Test a list that is monotonically increasing.
- `test_monotonic_decreasing`: Test a list that is monotonically decreasing.
- `test_monotonic_mixed`: Test a list that is not monotonically increasing or decreasing.
- `test_monotonic_single_element`: Test a list with a single element.
- `test_monotonic_empty_list`: Test an empty list.
- `test_monotonic_single_element_decreasing`: Test a list with a single decreasing element.
- `test_monotonic_all_equal`: Test a list with all equal elements.
- `test_monotonic_all_equal_decreasing`: Test a list with all equal decreasing elements.

Each test case uses the `assertTrue` or `assertFalse` method to check if the function returns the expected result.