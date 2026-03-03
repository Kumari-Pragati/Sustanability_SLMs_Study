user

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
    return resultassistant

Here is the unittest test script for the `rolling_max` function:

import unittest
from HumanEval_9_code import rolling_max

class TestRollingMax(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_single_element_list(self):
        self.assertEqual(rolling_max([1]), [1])

    def test_small_list(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 5]), [1, 2, 3, 3, 5])

    def test_large_list(self):
        self.assertEqual(rolling_max([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_list_with_duplicates(self):
        self.assertEqual(rolling_max([1, 2, 2, 3, 3, 3, 4, 5]), [1, 2, 2, 3, 3, 3, 4, 5])

    def test_list_with_negative_numbers(self):
        self.assertEqual(rolling_max([-1, -2, -3, -2, -5]), [-1, -2, -3, -3, -5])

    def test_list_with_mixed_numbers(self):
        self.assertEqual(rolling_max([1, -2, 3, -4, 5]), [1, -2, 3, 3, 5])

if __name__ == '__main__':
    unittest.main()

This script includes 6 test cases to cover different scenarios:

1. An empty list
2. A list with a single element
3. A small list with a few elements
4. A large list with many elements
5. A list with duplicate elements
6. A list with negative numbers and mixed numbers

Each test case uses the `assertEqual` method to check that the output of the `rolling_max` function matches the expected result.