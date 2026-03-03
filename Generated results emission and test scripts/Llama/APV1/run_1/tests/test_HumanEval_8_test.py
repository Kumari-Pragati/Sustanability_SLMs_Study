user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_8_code import sum_product

class TestSumProduct(unittest.TestCase):

    def test_sum_product_with_positive_numbers(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_sum_product_with_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-10, 24))

    def test_sum_product_with_mixed_numbers(self):
        self.assertEqual(sum_product([1, -2, 3, -4]), (0, -24))

    def test_sum_product_with_zero(self):
        self.assertEqual(sum_product([0, 1, 2, 3]), (6, 0))

    def test_sum_product_with_single_number(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_sum_product_with_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_sum_product_with_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            sum_product([1, 2, 3.4, 4])

    def test_sum_product_with_non_list_input(self):
        with self.assertRaises(TypeError):
            sum_product(123)

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of scenarios, including:

- Testing with positive numbers
- Testing with negative numbers
- Testing with mixed numbers (both positive and negative)
- Testing with zero
- Testing with a single number
- Testing with an empty list
- Testing with non-integer numbers
- Testing with non-list input

Each test case uses the `assertEqual` method to check if the output of the `sum_product` function matches the expected result. The `assertRaises` method is used to test for specific error types.