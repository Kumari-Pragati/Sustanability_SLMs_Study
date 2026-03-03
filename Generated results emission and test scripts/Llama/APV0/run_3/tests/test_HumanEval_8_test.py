user

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
    return sum_value, prod_valueassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_8_code import sum_product

class TestSumProduct(unittest.TestCase):

    def test_sum_product(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))
        self.assertEqual(sum_product([]), (0, 1))
        self.assertEqual(sum_product([-1, 0, 1]), (0, -1))
        self.assertEqual(sum_product([1, 1, 1, 1]), (4, 1))
        self.assertEqual(sum_product([-1, -1, -1, -1]), (-4, 1))
        self.assertEqual(sum_product([1, 2, 3, 4, 5]), (15, 120))
        self.assertEqual(sum_product([-1, 0, 1, 2, 3]), (4, -6))

if __name__ == '__main__':
    unittest.main()


This script includes five test cases to cover different scenarios:

1. Test with a list of positive numbers.
2. Test with an empty list.
3. Test with a list of negative numbers.
4. Test with a list of identical numbers.
5. Test with a list of mixed positive and negative numbers.

Each test case uses the `assertEqual` method to check if the output of the `sum_product` function matches the expected result. If the output does not match the expected result, the test will fail and an error message will be displayed.