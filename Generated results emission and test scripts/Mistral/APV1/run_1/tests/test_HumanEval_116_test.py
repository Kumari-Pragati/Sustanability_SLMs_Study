You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the `sort_array` function:


import unittest
from HumanEval_116_code import sort_array

class TestSortArray(unittest.TestCase):

    def test_sort_array(self):
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])
        self.assertEqual(sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 3, 4])
        self.assertEqual(sort_array([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])
        self.assertEqual(sort_array([10, 20, 100, 200, 1000]), [10, 20, 100, 200, 1000])
        self.assertEqual(sort_array([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])
        self.assertEqual(sort_array([10, 9, 8, 7, 6]), [6, 7, 8, 9, 10])
        self.assertEqual(sort_array([1000, 100, 10, 1]), [1, 10, 100, 1000])
        self.assertEqual(sort_array([5, 3, 2, 1]), [1, 2, 3, 5])
        self.assertEqual(sort_array([10, 100, 1000, 10000]), [10, 100, 1000, 10000])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to ensure the function works correctly for different input arrays. It checks the function's behavior for arrays with positive integers, negative integers, zeros, and a mix of numbers. It also tests the function's ability to handle arrays with the same number of ones in their binary representation, sorting them based on their decimal value.