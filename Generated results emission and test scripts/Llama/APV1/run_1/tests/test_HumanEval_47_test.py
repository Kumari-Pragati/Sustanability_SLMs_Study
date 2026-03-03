user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_47_code import median

class TestMedian(unittest.TestCase):

    def test_median_odd_length(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)

    def test_median_even_length(self):
        self.assertAlmostEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

    def test_median_empty_list(self):
        with self.assertRaises(ValueError):
            median([])

    def test_median_single_element(self):
        self.assertEqual(median([5]), 5)

    def test_median_all_equal(self):
        self.assertEqual(median([1, 1, 1, 1, 1]), 1)

    def test_median_negative_numbers(self):
        self.assertAlmostEqual(median([-10, -5, 0, 5, 10]), 0)

    def test_median_mixed_numbers(self):
        self.assertAlmostEqual(median([-10, 4, 6, 1000, 10, 20, 30]), 15.0)

    def test_median_non_numeric(self):
        with self.assertRaises(TypeError):
            median([1, 2, 'a', 4, 5])

    def test_median_non_list(self):
        with self.assertRaises(TypeError):
            median(123)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the following scenarios:

- A list with an odd number of elements
- A list with an even number of elements
- An empty list
- A list with a single element
- A list with all elements equal
- A list with negative numbers
- A list with mixed numbers
- A list with non-numeric elements
- A non-list input