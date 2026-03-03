You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
Here is a complete unittest test suite for the given function:


import unittest
from HumanEval_128_code import prod_signs

class TestProdSigns(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)

    def test_zero(self):
        self.assertEqual(prod_signs([0, 1]), 0)

    def test_empty_array(self):
        self.assertEqual(prod_signs([]), None)

    def test_negative_numbers(self):
        self.assertEqual(prod_signs([-1, -2, -2, 4]), 9)

    def test_mixed_numbers(self):
        self.assertEqual(prod_signs([1, -2, 2, -4]), -9)

    def test_single_number(self):
        self.assertEqual(prod_signs([5]), 5)

    def test_single_zero(self):
        self.assertEqual(prod_signs([0]), 0)

    def test_single_negative(self):
        self.assertEqual(prod_signs([-5]), -5)

    def test_large_numbers(self):
        self.assertEqual(prod_signs([1000, -2000, 2000, -4000]), 9000000)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the function is working correctly for different types of input. It tests with positive numbers, zero, negative numbers, and a variety of other scenarios.