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

    return sorted(nums, key=digits_sum)

 import unittest
from HumanEval_145_code import order_by_points

class TestOrderByPoints(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(order_by_points([]), [])

    def test_single_element_list(self):
        self.assertEqual(order_by_points([1]), [1])

    def test_negative_numbers(self):
        self.assertEqual(order_by_points([-1, -11, -12]), [-1, -11, -12])

    def test_positive_numbers(self):
        self.assertEqual(order_by_points([1, 11, 12]), [1, 11, 12])

    def test_same_sum_digits(self):
        self.assertEqual(order_by_points([10, 20, 30]), [10, 20, 30])

    def test_same_sum_digits_with_different_indices(self):
        self.assertEqual(order_by_points([100, 200, 300]), [100, 200, 300])

    def test_same_sum_digits_with_different_indices_and_negatives(self):
        self.assertEqual(order_by_points([-100, 200, -300]), [-100, 200, -300])

    def test_large_numbers(self):
        self.assertEqual(order_by_points([1000000, 2000000, 3000000]), [1000000, 2000000, 3000000])

    def test_large_numbers_with_negatives(self):
        self.assertEqual(order_by_points([-1000000, 2000000, -3000000]), [-1000000, 2000000, -3000000])

    def test_large_numbers_with_same_sum_digits(self):
        self.assertEqual(order_by_points([10000000, 20000000, 30000000]), [10000000, 20000000, 30000000])

    def test_large_numbers_with_same_sum_digits_and_different_indices(self):
        self.assertEqual(order_by_points([100000000, 200000000, 300000000]), [100000000, 200000000, 300000000])

if __name__ == '__main__':
    unittest.main()