You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_52_code import below_threshold
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for e in l:
        if e >= t:
            return False
    return True


### Response:
Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_52_code import below_threshold

class TestBelowThreshold(unittest.TestCase):
    def test_all_below(self):
        self.assertTrue(below_threshold([1, 2, 4, 10], 100))

    def test_one_above(self):
        self.assertFalse(below_threshold([1, 20, 4, 10], 5))

    def test_empty_list(self):
        self.assertTrue(below_threshold([], 100))

    def test_all_above(self):
        self.assertFalse(below_threshold([101, 202, 404, 1000], 100))

    def test_negative_numbers(self):
        self.assertTrue(below_threshold([-1, -2, -4, -10], 0))

    def test_negative_threshold(self):
        with self.assertRaises(ValueError):
            below_threshold([1, 2, 3], -1)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- `test_all_below`: Tests when all numbers in the list are below the threshold.
- `test_one_above`: Tests when at least one number in the list is above the threshold.
- `test_empty_list`: Tests when the list is empty.
- `test_all_above`: Tests when all numbers in the list are above the threshold.
- `test_negative_numbers`: Tests when the list contains negative numbers.
- `test_negative_threshold`: Tests when the threshold is negative, which should raise a ValueError.

Please note that the `HumanEval_52_code` module should contain the `below_threshold` function for these tests to work.