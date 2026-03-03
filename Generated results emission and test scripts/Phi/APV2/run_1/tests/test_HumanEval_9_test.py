You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
        self.assertEqual(rolling_max([1]), [1])

    def test_rolling_max_with_negative_numbers(self):
        self.assertEqual(rolling_max([-1, -2, -3, -2, -5]), [-1, -1, -1, -2, -5])

    def test_rolling_max_with_mixed_numbers(self):
        self.assertEqual(rolling_max([1, -2, 3, -2, 5]), [1, 1, 3, 3, 5])

    def test_rolling_max_with_all_negative_numbers(self):
        self.assertEqual(rolling_max([-1, -2, -3, -4, -5]), [-1, -2, -3, -4, -5])

    def test_rolling_max_with_all_positive_numbers(self):
        self.assertEqual(rolling_max([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_rolling_max_with_all_zeroes(self):
        self.assertEqual(rolling_max([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

    def test_rolling_max_with_repeated_numbers(self):
        self.assertEqual(rolling_max([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])

    def test_rolling_max_with_increasing_numbers(self):
        self.assertEqual(rolling_max([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_rolling_max_with_decreasing_numbers(self):
        self.assertEqual(rolling_max([5, 4, 3, 2, 1]), [5, 5, 5, 5, 5])

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of cases for the `rolling_max` function, including lists with positive and negative numbers, empty lists, single-element lists, mixed numbers, all negative numbers, all positive numbers, all zeroes, repeated numbers, increasing numbers, and decreasing numbers. Each test case uses the `assertEqual` method to verify that the output of the `rolling_max` function matches the expected result.