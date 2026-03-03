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
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0

 import unittest
from HumanEval_47_code import median

class TestMedianFunction(unittest.TestCase):

    def test_median_odd_length(self):
        self.assertEqual(median([3, 1, 2, 4, 5]), 3)

    def test_median_even_length(self):
        self.assertAlmostEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

    def test_median_empty_list(self):
        with self.assertRaises(ValueError):
            median([])

    def test_median_single_element(self):
        self.assertEqual(median([5]), 5)

    def test_median_all_same_elements(self):
        self.assertEqual(median([10, 10, 10, 10]), 10)

    def test_median_negative_numbers(self):
        self.assertEqual(median([-10, -5, -3, -1]), -4.0)

    def test_median_large_numbers(self):
        self.assertEqual(median([1000000, 2000000, 3000000, 4000000]), 2500000.0)

    def test_median_non_integer_numbers(self):
        self.assertAlmostEqual(median([1.5, 2.5, 3.5, 4.5]), 3.0)

    def test_median_with_floats(self):
        self.assertAlmostEqual(median([1.0, 2.0, 3.0, 4.0]), 2.5)

    def test_median_with_decimals(self):
        self.assertAlmostEqual(median([1.2, 2.3, 3.4, 4.5]), 2.95)

if __name__ == '__main__':
    unittest.main()