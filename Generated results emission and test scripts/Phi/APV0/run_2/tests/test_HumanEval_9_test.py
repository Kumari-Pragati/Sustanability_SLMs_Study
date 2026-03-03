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

 import unittest
from HumanEval_9_code import rolling_max

class TestRollingMax(unittest.TestCase):

    def test_rolling_max_with_positive_numbers(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 5]), [1, 2, 3, 3, 5])

    def test_rolling_max_with_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_rolling_max_with_single_element(self):
        self.assertEqual(rolling_max([10]), [10])

    def test_rolling_max_with_negative_numbers(self):
        self.assertEqual(rolling_max([-1, -2, -3, -2, -5]), [-1, -1, -1, -1, -5])

    def test_rolling_max_with_all_same_elements(self):
        self.assertEqual(rolling_max([5, 5, 5, 5, 5]), [5, 5, 5, 5, 5])

    def test_rolling_max_with_mixed_numbers(self):
        self.assertEqual(rolling_max([1, -2, 3, -4, 5]), [1, 1, 3, 3, 5])

    def test_rolling_max_with_large_numbers(self):
        self.assertEqual(rolling_max([1000000, 2000000, 3000000, 2000000, 5000000]),
                         [1000000, 2000000, 3000000, 3000000, 5000000])

if __name__ == '__main__':
    unittest.main()