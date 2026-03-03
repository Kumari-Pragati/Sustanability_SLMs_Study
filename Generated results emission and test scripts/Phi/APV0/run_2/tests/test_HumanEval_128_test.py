Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return prod * sum([abs(i) for i in arr])

 import unittest
from HumanEval_128_code import prod_signs

class TestProdSigns(unittest.TestCase):

    def test_prod_signs_with_positive_numbers(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)

    def test_prod_signs_with_zero(self):
        self.assertEqual(prod_signs([0, 1]), 0)

    def test_prod_signs_with_negative_numbers(self):
        self.assertEqual(prod_signs([-1, -2, -2, 4]), -8)

    def test_prod_signs_with_mixed_numbers(self):
        self.assertEqual(prod_signs([1, -1, 2, -2]), -6)

    def test_prod_signs_with_empty_array(self):
        self.assertIsNone(prod_signs([]))

    def test_prod_signs_with_single_element(self):
        self.assertEqual(prod_signs([5]), 5)

    def test_prod_signs_with_all_negative_numbers(self):
        self.assertEqual(prod_signs([-1, -2, -3, -4]), -12)

    def test_prod_signs_with_all_positive_numbers(self):
        self.assertEqual(prod_signs([1, 2, 3, 4]), 10)

    def test_prod_signs_with_all_zeros(self):
        self.assertEqual(prod_signs([0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()