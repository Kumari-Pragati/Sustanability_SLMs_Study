You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `sort_array` function:


import unittest
from HumanEval_116_code import sort_array

class TestSortArray(unittest.TestCase):

    def test_sort_array(self):
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])
        self.assertEqual(sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 3, 4])
        self.assertEqual(sort_array([0, 0, 0, 0]), [0, 0, 0, 0])
        self.assertEqual(sort_array([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]), [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])
        self.assertEqual(sort_array([1, 3, 2, 1]), [1, 1, 2, 3])
        self.assertEqual(sort_array([1000000000, 10000000, 1000000, 100000, 10000, 1000, 100, 10, 1]), [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 1000000000])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to ensure the `sort_array` function works correctly for different input arrays. The test cases cover both positive and negative numbers, arrays with only zeros, and arrays with a mix of numbers having different numbers of ones in their binary representation.