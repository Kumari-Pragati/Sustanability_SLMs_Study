system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest
from HumanEval_128_code import prod_signs

class TestProdSigns(unittest.TestCase):
    def test_prod_signs(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)
        self.assertEqual(prod_signs([0, 1]), 0)
        self.assertEqual(prod_signs([]), None)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `unittest` test case class named `TestProdSigns`. It includes two test cases that cover different scenarios:

1. The first test case checks if the function returns `-9` when the input list `[1, 2, 2, -4]` is passed to it.
2. The second test case verifies that the function correctly handles an empty list by returning `None`.
3. The third test case ensures that the function works as expected with a single negative number (`[0, 1]`) by checking if it returns `0`.

The `unittest.main()` call at the end runs these tests when the script is executed directly.