Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `rolling_max` function:


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
        self.assertEqual(rolling_max([1, 5, 4, 3, 2]), [1, 5, 5, 5, 2])

    def test_negative_numbers(self):
        self.assertEqual(rolling_max([-1, -2, -3, -2, -5]), [-1, -1, -1, -1, -5])

    def test_mixed_numbers(self):
        self.assertEqual(rolling_max([1, -2, 3, -4, 5]), [1, -2, 3, 3, 5])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios such as an empty list, single-element list, simple lists, decreasing lists, increasing-then-decreasing lists, negative numbers, and mixed numbers. You can run this script directly to test the `rolling_max` function.