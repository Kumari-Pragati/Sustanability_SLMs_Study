user

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

    return sorted(nums, key=digits_sum)assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_145_code import order_by_points

class TestOrderByPoints(unittest.TestCase):

    def test_order_by_points(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([]), [])
        self.assertEqual(order_by_points([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(order_by_points([-1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1])
        self.assertEqual(order_by_points([10, 20, 30, 40, 50]), [10, 20, 30, 40, 50])
        self.assertEqual(order_by_points([-10, -20, -30, -40, -50]), [-50, -40, -30, -20, -10])
        self.assertEqual(order_by_points([100, 200, 300, 400, 500]), [100, 200, 300, 400, 500])
        self.assertEqual(order_by_points([-100, -200, -300, -400, -500]), [-500, -400, -300, -200, -100])

if __name__ == '__main__':
    unittest.main()


This script includes five test cases to cover different scenarios:

1. Test with a list of positive and negative numbers.
2. Test with an empty list.
3. Test with a list of positive numbers.
4. Test with a list of negative numbers.
5. Test with a list of large positive and negative numbers.

Each test case uses the `assertEqual` method to compare the output of the `order_by_points` function with the expected output.