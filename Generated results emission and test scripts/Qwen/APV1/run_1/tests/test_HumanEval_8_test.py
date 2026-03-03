system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return sum_value, prod_value


assistant

import unittest
from HumanEval_8_code import sum_product

class TestSumProduct(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))
        self.assertEqual(sum_product([]), (0, 1))

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-10, 24))

    def test_large_numbers(self):
        self.assertEqual(sum_product([10**6, 10**7, 10**8, 10**9]), ((10**15 + 10**9), 10**15))

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestSumProduct` class that inherits from `unittest.TestCase`. It contains several test methods to verify different scenarios of the `sum_product` function:

- The `test_sum` method tests the function with a typical input and an empty list.
- The `test_empty_list` method checks if the function returns correct values when the input list is empty.
- The `test_single_element` method verifies the function's behavior with a single-element list.
- The `test_negative_numbers` method ensures the function works correctly with negative numbers.
- The `test_large_numbers` method tests the function with large positive numbers to check its performance and accuracy.

The `unittest.main()` call at the end runs all the test cases defined within the `TestSumProduct` class.