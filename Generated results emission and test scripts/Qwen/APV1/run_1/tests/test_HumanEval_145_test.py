system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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

    return sorted(nums, key=digits_sum)


assistant

import unittest

from HumanEval_145_code import order_by_points


class TestOrderByPoints(unittest.TestCase):

    def test_order_by_points(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([]), [])
        self.assertEqual(order_by_points([-1, -2, -3, -4, -5]), [-5, -4, -3, -2, -1])

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `unittest` test case class named `TestOrderByPoints`. It includes two test cases:

1. The first test case checks that the function correctly orders the list `[1, 11, -1, -11, -12]` as expected.
2. The second test case checks that the function returns an empty list when passed an empty input list.
3. The third test case checks that the function correctly orders the negative numbers in descending order.

The `assertEqual` method is used to compare the output of the `order_by_points` function with the expected results. If any of these tests fail, it will raise an assertion error and print out the failure message.