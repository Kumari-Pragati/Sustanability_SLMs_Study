You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


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

    def test_empty(self):
        self.assertTrue(monotonic([]))

    def test_negative_numbers(self):
        self.assertTrue(monotonic([4, 1, 0, -10]))

    def test_negative_and_positive(self):
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

Each test checks if the function returns the expected result for a given input.