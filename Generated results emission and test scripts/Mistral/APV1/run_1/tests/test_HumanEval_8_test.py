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

 Here is a comprehensive unittest test suite for the given Python function `sum_product`. The test cases cover various scenarios such as empty list, single element list, positive numbers, negative numbers, and a mix of positive and negative numbers.


import unittest
from HumanEval_8_code import sum_product

class TestSumProduct(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element(self):
        self.assertEqual(sum_product([1]), (1, 1))
        self.assertEqual(sum_product([-1]), (1, -1))

    def test_positive_numbers(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))
        self.assertEqual(sum_product([10, 20, 30, 40]), (100, 24000))

    def test_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-10, 24))
        self.assertEqual(sum_product([-10, -20, -30, -40]), (-100, 24000))

    def test_mix_of_positive_and_negative_numbers(self):
        self.assertEqual(sum_product([1, -2, 3, -4]), (3, -24))
        self.assertEqual(sum_product([-1, 2, -3, 4]), (3, 24))
        self.assertEqual(sum_product([10, -20, 30, -40]), (10, -24000))
        self.assertEqual(sum_product([-10, 20, -30, 40]), (10, 24000))

if __name__ == '__main__':
    unittest.main()


This test suite uses the built-in `unittest` module to create a test case class `TestSumProduct`. Inside this class, there are several test methods, each testing a specific scenario. The `assertEqual` method is used to compare the expected and actual results. If the results match, the test passes; otherwise, it fails. The `if __name__ == '__main__':` block at the end runs the unittest suite when the script is executed directly.