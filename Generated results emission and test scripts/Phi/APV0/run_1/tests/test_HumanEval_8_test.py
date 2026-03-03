Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_8_code import sum_product
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """Return a pair (sum, product) for the given list of integers.
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    >>> sum_product([])
    (0, 1)
    """
    sum_value = 0
    prod_value = 1
    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value

 import unittest
from HumanEval_8_code import sum_product

class TestSumProduct(unittest.TestCase):

    def test_sum_product_with_positive_numbers(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_sum_product_with_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_sum_product_with_single_number(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_sum_product_with_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, -3]), (-6, -6))

    def test_sum_product_with_mixed_numbers(self):
        self.assertEqual(sum_product([1, -2, 3, -4]), (0, -8))

    def test_sum_product_with_zero(self):
        self.assertEqual(sum_product([0]), (0, 0))

    def test_sum_product_with_large_numbers(self):
        self.assertEqual(sum_product([1000, 2000, 3000]), (6000, 6000000))

if __name__ == '__main__':
    unittest.main()