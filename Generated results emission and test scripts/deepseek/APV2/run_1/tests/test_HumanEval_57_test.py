You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_57_code import monotonic

class TestMonotonic(unittest.TestCase):

    def test_increasing(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))

    def test_decreasing(self):
        self.assertTrue(monotonic([20, 10, 4, 1]))

    def test_mixed(self):
        self.assertFalse(monotonic([1, 20, 4, 10]))

    def test_constant(self):
        self.assertTrue(monotonic([1, 1, 1, 1]))

    def test_single_element(self):
        self.assertTrue(monotonic([1]))

    def test_empty_list(self):
        self.assertTrue(monotonic([]))

    def test_negative_numbers(self):
        self.assertTrue(monotonic([4, 1, 0, -10]))

    def test_negative_and_positive_numbers(self):
        self.assertFalse(monotonic([4, -1, 0, 10]))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- Increasing lists
- Decreasing lists
- Lists that are neither increasing nor decreasing (mixed)
- Constant lists
- Lists with a single element
- Empty lists
- Lists with negative numbers
- Lists with both positive and negative numbers

Each test case uses the `assertTrue` method to check if the `monotonic` function returns the expected result.