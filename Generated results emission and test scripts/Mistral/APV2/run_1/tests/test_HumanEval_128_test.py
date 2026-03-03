You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the `prod_signs` function:


import unittest
from HumanEval_128_code import prod_signs

class TestProdSigns(unittest.TestCase):

    def test_empty_array(self):
        self.assertIsNone(prod_signs([]))

    def test_single_element(self):
        self.assertEqual(prod_signs([0]), 0)
        self.assertEqual(prod_signs([1]), 1)
        self.assertEqual(prod_signs([-1]), -1)

    def test_multiple_elements(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)
        self.assertEqual(prod_signs([0, 1]), 0)
        self.assertEqual(prod_signs([-1, -2, -3]), 6)
        self.assertEqual(prod_signs([1, -1, 1, -1]), 0)
        self.assertEqual(prod_signs([-1, 1, -1, 1]), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty array, single elements, and multiple elements with different combinations of positive, negative, and zero numbers. The `assertIsNone` function is used to test the expected behavior of returning `None` for an empty array. The `assertEqual` function is used to compare the expected and actual results for other test cases.