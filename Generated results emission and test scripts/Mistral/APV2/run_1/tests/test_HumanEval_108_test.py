You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_108_code import count_nums
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    def digits_sum(n):
        neg = 1
        if n < 0:
            n, neg = -1 * n, -1
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)

    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))

 Here is the complete unittest test suite for the `count_nums` function:


import unittest
from HumanEval_108_code import count_nums

class TestCountNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_nums([]), 0)

    def test_negative_and_positive_numbers(self):
        self.assertEqual(count_nums([-1, 11, -11]), 1)

    def test_positive_numbers(self):
        self.assertEqual(count_nums([1, 1, 2]), 3)

    def test_single_digit_numbers(self):
        self.assertEqual(count_nums([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), 10)

    def test_multi_digit_numbers(self):
        self.assertEqual(count_nums([12, 111, 123, 1234]), 4)

    def test_negative_multi_digit_numbers(self):
        self.assertEqual(count_nums([-12, -111, -123, -1234]), 4)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios such as an empty list, negative and positive numbers, single-digit numbers, multi-digit numbers, and negative multi-digit numbers. It uses the `unittest.TestCase.assertEqual` method to verify the expected and actual results.