You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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
    return prod * sum([abs(i) for i in arr])


### Response:
Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_128_code import prod_signs

class TestProdSigns(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(prod_signs([1, 2, 2, 4]), 15)

    def test_negative_numbers(self):
        self.assertEqual(prod_signs([-1, -2, -2, -4]), -15)

    def test_mixed_numbers(self):
        self.assertEqual(prod_signs([1, -2, 2, -4]), -9)

    def test_zero(self):
        self.assertEqual(prod_signs([0, 1]), 0)

    def test_empty_array(self):
        self.assertIsNone(prod_signs([]))

    def test_single_number(self):
        self.assertEqual(prod_signs([5]), 5)

    def test_negative_single_number(self):
        self.assertEqual(prod_signs([-5]), -5)

    def test_zero_and_positive_numbers(self):
        self.assertEqual(prod_signs([0, 1, 2, 3]), 6)

    def test_zero_and_negative_numbers(self):
        self.assertEqual(prod_signs([0, -1, -2, -3]), -6)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various scenarios including positive numbers, negative numbers, mixed numbers, zero, empty array, single number, and combinations of zero and positive/negative numbers.