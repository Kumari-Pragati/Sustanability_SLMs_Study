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

 import unittest
from HumanEval_47_code import median

class TestMedianFunction(unittest.TestCase):

    def test_odd_length_list(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)

    def test_even_length_list(self):
        self.assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            median([])

    def test_single_element_list(self):
        self.assertEqual(median([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(median([-10, -5, -3, -1]), -4.0)

    def test_large_numbers(self):
        self.assertEqual(median([1000000, 2000000, 3000000, 4000000]), 2500000.0)

    def test_already_sorted_list(self):
        self.assertEqual(median([1, 2, 3, 4, 5]), 3)

    def test_duplicate_elements(self):
        self.assertEqual(median([1, 2, 2, 3, 4]), 2)

if __name__ == '__main__':
    unittest.main()