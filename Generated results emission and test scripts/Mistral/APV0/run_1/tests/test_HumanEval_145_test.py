Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

    return sorted(nums, key=digits_sum)

 Here is a unittest test script for the `order_by_points` function:


import unittest
from HumanEval_145_code import order_by_points

class TestOrderByPoints(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(order_by_points([]), [])

    def test_single_element(self):
        self.assertEqual(order_by_points([1]), [1])
        self.assertEqual(order_by_points([-1]), [-1])

    def test_multiple_elements(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([10, 11, 9]), [9, 10, 11])
        self.assertEqual(order_by_points([-10, -11, -9]), [-9, -10, -11])
        self.assertEqual(order_by_points([100, 11, 9, 1000]), [11, 9, 100, 1000])
        self.assertEqual(order_by_points([-100, -11, -9, -1000]), [-9, -11, -100, -1000])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as an empty list, a single element, and multiple elements with positive and negative numbers. The test cases are designed to ensure that the function correctly sorts the list based on the sum of their digits and maintains the original order for numbers with the same sum of digits.