You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_8_code import sum_product

class TestSumProduct(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_element(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_multiple_elements(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_negative_elements(self):
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-10, -24))

    def test_zero_elements(self):
        self.assertEqual(sum_product([0, 0, 0, 0]), (0, 0))

if __name__ == '__main__':
    unittest.main()


This script creates a test class `TestSumProduct` that inherits from `unittest.TestCase`. It includes five test methods to test the function with different types of input: empty list, single element, multiple elements, negative elements, and zero elements. Each method uses the `assertEqual` method to check if the output of the function matches the expected result.

To run the tests, you can simply execute this script. The `unittest.main()` call at the end will run all the test methods in the `TestSumProduct` class.

Please note that you need to have the `HumanEval_8_code` module with the `sum_product` function defined in it for this script to work.