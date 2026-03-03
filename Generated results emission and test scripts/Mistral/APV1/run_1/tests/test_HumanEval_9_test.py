You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_9_code import rolling_max

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """Return a list where each element is the maximum of all elements up to that index.
    >>> rolling_max([1, 2, 3, 2, 5])
    [1, 2, 3, 3, 5]
    >>> rolling_max([])
    []
    """
    result: List[int] = []
    running_max = None
    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)
        result.append(running_max)
    return result

 Here is a comprehensive unittest test suite for the given `rolling_max` function:


import unittest
from HumanEval_9_code import rolling_max

class TestRollingMax(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_single_element(self):
        self.assertEqual(rolling_max([1]), [1])

    def test_simple_list(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 5]), [1, 2, 3, 3, 5])

    def test_decreasing_list(self):
        self.assertEqual(rolling_max([5, 4, 3, 2, 1]), [5, 5, 5, 5, 1])

    def test_increasing_then_decreasing_list(self):
        self.assertEqual(rolling_max([1, 5, 4, 3, 2]), [1, 5, 5, 5, 3])

    def test_list_with_duplicates(self):
        self.assertEqual(rolling_max([3, 2, 3, 2, 3, 2]), [3, 3, 3, 3, 3, 3])

    def test_list_with_negative_numbers(self):
        self.assertEqual(rolling_max([-1, -2, -3, -2, -5]), [-1, -1, -1, -1, -5])

    def test_list_with_zero(self):
        self.assertEqual(rolling_max([0]), [0])
        self.assertEqual(rolling_max([0, 1, 2, 3, 0]), [0, 0, 1, 2, 3])

if __name__ == '__main__':
    unittest.main()


This test suite includes various edge cases and different types of input lists to ensure the `rolling_max` function works correctly.