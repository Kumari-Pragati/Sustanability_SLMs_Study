You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
        self.assertAlmostEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            median([])

    def test_single_element_list(self):
        self.assertEqual(median([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(median([-10, -5, -3]), -5)

    def test_large_numbers(self):
        self.assertEqual(median([1000000, 2000000, 3000000]), 2000000)

    def test_non_integer_numbers(self):
        self.assertEqual(median([1.5, 2.5, 3.5]), 2.5)

    def test_duplicate_elements(self):
        self.assertEqual(median([2, 2, 2, 2, 2]), 2)

if __name__ == '__main__':
    unittest.main()