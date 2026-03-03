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

 Here is a unittest test script for the `sort_array` function:


import unittest
from HumanEval_116_code import sort_array

class TestSortArray(unittest.TestCase):

    def test_sort_array(self):
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])
        self.assertEqual(sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 3, 4])
        self.assertEqual(sort_array([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])
        self.assertEqual(sort_array([10, 20, 100, 200, 1000]), [10, 20, 100, 200, 1000])
        self.assertEqual(sort_array([1, 7, 5, 10, 13]), [1, 5, 7, 10, 13])
        self.assertEqual(sort_array([10000, 10001, 100000, 100001]), [10000, 100001, 10001, 100000])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to ensure the function works correctly for various inputs. It checks the function's behavior for positive integers, negative integers, zero, and a mix of integers with different numbers of ones in their binary representation. The test cases are designed to cover edge cases and various input scenarios.