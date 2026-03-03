system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return sum_value, prod_valueassistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_8_code import sum_product

class TestSumProduct(unittest.TestCase):

    def test_sum_product_with_positive_numbers(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_sum_product_with_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-10, 24))

    def test_sum_product_with_zero(self):
        self.assertEqual(sum_product([0, 1, 2, 3]), (6, 6))

    def test_sum_product_with_mixed_numbers(self):
        self.assertEqual(sum_product([-1, 0, 1, 2]), (2, 2))

    def test_sum_product_with_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

if __name__ == '__main__':
    unittest.main()