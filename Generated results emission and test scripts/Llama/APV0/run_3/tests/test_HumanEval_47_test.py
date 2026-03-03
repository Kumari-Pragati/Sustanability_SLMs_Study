user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_47_code import median
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_47_code import median

class TestMedian(unittest.TestCase):

    def test_median_even_length(self):
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

    def test_median_odd_length(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)

    def test_median_empty_list(self):
        with self.assertRaises(ValueError):
            median([])

    def test_median_single_element(self):
        self.assertEqual(median([5]), 5)

    def test_median_multiple_duplicates(self):
        self.assertEqual(median([1, 2, 2, 3, 3, 3]), 2.5)

    def test_median_negative_numbers(self):
        self.assertEqual(median([-10, -5, 0, 5, 10]), 0)

    def test_median_mixed_types(self):
        with self.assertRaises(TypeError):
            median([1, 2, 'a', 4, 5])

if __name__ == '__main__':
    unittest.main()


This script includes tests for the following cases:
- Even length list
- Odd length list
- Empty list
- Single element list
- List with multiple duplicates
- List with negative numbers
- List with mixed types (to test for type error)

Each test case uses the `assertEqual` method to check if the output of the `median` function matches the expected result. For the edge case of an empty list, the `assertRaises` method is used to check if a `ValueError` is raised. For the mixed types case, the `assertRaises` method is used to check if a `TypeError` is raised.