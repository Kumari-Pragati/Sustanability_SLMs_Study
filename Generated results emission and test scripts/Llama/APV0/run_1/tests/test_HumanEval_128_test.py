user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return prod * sum([abs(i) for i in arr])assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_128_code import prod_signs

class TestProdSigns(unittest.TestCase):

    def test_prod_signs(self):
        self.assertIsNone(prod_signs([]))
        self.assertEqual(prod_signs([0, 1]), 0)
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)
        self.assertEqual(prod_signs([-1, -2, -3]), 6)
        self.assertEqual(prod_signs([1, 2, 3, 4]), 30)
        self.assertEqual(prod_signs([-1, 1, -1, 1]), 0)
        self.assertEqual(prod_signs([0, 0, 0]), 0)
        self.assertEqual(prod_signs([-1, 0, 1]), 0)
        self.assertEqual(prod_signs([1, -1, 1, -1]), 0)

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to cover different scenarios, such as an empty array, arrays with only positive numbers, arrays with only negative numbers, arrays with a mix of positive and negative numbers, and arrays with only zeros. The `assertIsNone` method is used to test the return value of the function when the input array is empty, and the `assertEqual` method is used to test the return value of the function for other input arrays.