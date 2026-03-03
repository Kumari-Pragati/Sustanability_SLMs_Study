user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_145_code import order_by_points

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def digits_sum(n):
        neg = 1
        if n < 0:
            n, neg = -1 * n, -1
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)

    return sorted(nums, key=digits_sum)assistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_145_code import order_by_points

class TestOrderByPoints(unittest.TestCase):

    def test_order_by_points(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([]), [])
        self.assertEqual(order_by_points([1, 2, 3]), [1, 2, 3])
        self.assertEqual(order_by_points([-1, -2, -3]), [-3, -2, -1])
        self.assertEqual(order_by_points([10, 20, 30]), [10, 20, 30])
        self.assertEqual(order_by_points([-10, -20, -30]), [-30, -20, -10])
        self.assertEqual(order_by_points([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(order_by_points([-1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1])
        self.assertEqual(order_by_points([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(order_by_points([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1])

    def test_order_by_points_with_duplicates(self):
        self.assertEqual(order_by_points([1, 1, 2, 2, 3, 3]), [1, 1, 2, 2, 3, 3])
        self.assertEqual(order_by_points([-1, -1, -2, -2, -3, -3]), [-3, -3, -2, -2, -1, -1])
        self.assertEqual(order_by_points([1, 1, 1, 2, 2, 2, 3, 3, 3]), [1, 1, 1, 2, 2, 2, 3, 3, 3])
        self.assertEqual(order_by_points([-1, -1, -1, -2, -2, -2, -3, -3, -3]), [-3, -3, -3, -2, -2, -2, -1, -1, -1])

    def test_order_by_points_with_negative_numbers(self):
        self.assertEqual(order_by_points([-1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1])
        self.assertEqual(order_by_points([1, -1, 2, -2, 3, -3]), [-3, -2, -1, 1, 2, 3])
        self.assertEqual(order_by_points([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1])

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different scenarios, such as:

- Testing the function with a list of integers
- Testing the function with an empty list
- Testing the function with a list of positive integers
- Testing the function with a list of negative integers
- Testing the function with a list of mixed positive and negative integers
- Testing the function with a list of duplicate integers
- Testing the function with a list of negative integers with duplicates

Each test case checks if the output of the function matches the expected output.