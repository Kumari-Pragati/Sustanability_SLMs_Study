You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_145_code import order_by_points

class TestOrderByPoints(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(order_by_points([]), [])

    def test_positive_numbers(self):
        self.assertEqual(order_by_points([1, 11, 123]), [1, 11, 123])

    def test_negative_numbers(self):
        self.assertEqual(order_by_points([-1, -11, -123]), [-123, -11, -1])

    def test_mixed_numbers(self):
        self.assertEqual(order_by_points([1, -11, 123, -123]), [-123, -11, 1, 123])

    def test_same_digit_sum(self):
        self.assertEqual(order_by_points([1, 11, 12, 21]), [1, 11, 12, 21])

    def test_large_numbers(self):
        self.assertEqual(order_by_points([100, 200, 300, 400]), [100, 200, 300, 400])

    def test_large_negative_numbers(self):
        self.assertEqual(order_by_points([-100, -200, -300, -400]), [-400, -300, -200, -100])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios:

- An empty list
- Positive numbers
- Negative numbers
- Mixed numbers (positive and negative)
- Numbers with the same digit sum
- Large numbers
- Large negative numbers

Each test checks if the function returns the expected result for a given input.