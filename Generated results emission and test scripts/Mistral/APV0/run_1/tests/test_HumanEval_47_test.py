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
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0

 Here is a unittest test script for the `median` function:


import unittest
from HumanEval_47_code import median

class TestMedian(unittest.TestCase):

    def test_median_odd_length(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)
        self.assertEqual(median([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(median([1, 3, 5, 7, 9]), 5.0)
        self.assertEqual(median([-5, -3, -1, 1, 3, 5]), 0.0)

    def test_median_even_length(self):
        self.assertEqual(median([2, 3, 4, 5]), 3.5)
        self.assertEqual(median([-10, -5, 0, 5, 10]), 0.0)
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        self.assertEqual(median([-1, 0, 1, 2]), 0.0)
        self.assertEqual(median([-5, -3, -1, 1, 3]), 0.0)

    def test_empty_list(self):
        self.assertIsNone(median([]))

    def test_single_element(self):
        for num in [-10, 0, 10, 1000]:
            self.assertEqual(median([num]), num)

    def test_extreme_values(self):
        self.assertEqual(median([-1000000, -1000000, -1000000]), -1000000)
        self.assertEqual(median([1000000, 1000000, 1000000]), 1000000)

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as odd and even length lists, empty lists, single-element lists, and extreme values. It also tests the edge case where the list contains only duplicate elements.