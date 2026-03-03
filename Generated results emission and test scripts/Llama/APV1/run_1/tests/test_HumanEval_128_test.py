user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_128_code import prod_signs

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if not arr:
        return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_128_code import prod_signs

class TestProdSigns(unittest.TestCase):

    def test_empty_array(self):
        self.assertIsNone(prod_signs([]))

    def test_single_positive(self):
        self.assertEqual(prod_signs([1]), 1)

    def test_single_negative(self):
        self.assertEqual(prod_signs([-1]), -1)

    def test_single_zero(self):
        self.assertEqual(prod_signs([0]), 0)

    def test_multiple_positive(self):
        self.assertEqual(prod_signs([1, 2, 3]), 6)

    def test_multiple_negative(self):
        self.assertEqual(prod_signs([-1, -2, -3]), 6)

    def test_multiple_mixed(self):
        self.assertEqual(prod_signs([1, -2, 3]), 8)

    def test_multiple_zero(self):
        self.assertEqual(prod_signs([0, 0, 0]), 0)

    def test_multiple_mixed_zero(self):
        self.assertEqual(prod_signs([1, -2, 0, 3]), 6)

    def test_edge_case(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)

    def test_edge_case_zero(self):
        self.assertEqual(prod_signs([0, 1]), 0)

if __name__ == '__main__':
    unittest.main()


This test suite covers all the edge cases and scenarios mentioned in the problem statement. It tests the function with empty array, single positive, single negative, single zero, multiple positive, multiple negative, multiple mixed, multiple zero, multiple mixed zero, and edge cases.