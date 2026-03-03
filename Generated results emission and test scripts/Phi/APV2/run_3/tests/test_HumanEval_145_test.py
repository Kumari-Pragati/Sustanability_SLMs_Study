You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

    def test_same_digit_sum(self):
        self.assertEqual(order_by_points([11, 21, 31]), [11, 31, 21])

    def test_different_digit_sum(self):
        self.assertEqual(order_by_points([10, 20, 30]), [10, 20, 30])

    def test_mixed_numbers(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])

if __name__ == '__main__':
    unittest.main()