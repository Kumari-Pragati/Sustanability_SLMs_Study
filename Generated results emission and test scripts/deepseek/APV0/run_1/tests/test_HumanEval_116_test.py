You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_116_code import sort_array
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_116_code import sort_array

class TestSortArray(unittest.TestCase):
    def test_sort_array(self):
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])
        self.assertEqual(sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 3, 4])
        self.assertEqual(sort_array([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])
        self.assertEqual(sort_array([10, 20, 30, 40, 50]), [10, 20, 30, 40, 50])
        self.assertEqual(sort_array([100, 200, 300, 400, 500]), [100, 200, 300, 400, 500])
        self.assertEqual(sort_array([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_array([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_array([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])
        self.assertEqual(sort_array([-1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1])

if __name__ == '__main__':
    unittest.main()


This script includes a test class `TestSortArray` that inherits from `unittest.TestCase`. Inside this class, there is a method `test_sort_array` that contains a series of `assertEqual` calls to test the `sort_array` function with different inputs.

The `assertEqual` method is used to check if the output of the `sort_array` function matches the expected output. If the output does not match the expected output, the test will fail.

The `unittest.main()` call at the end of the script runs the test cases when the script is executed directly.