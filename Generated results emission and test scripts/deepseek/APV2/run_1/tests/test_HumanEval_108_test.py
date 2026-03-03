You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_108_code import count_nums

class TestCountNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_nums([]), 0)

    def test_positive_numbers(self):
        self.assertEqual(count_nums([1, 1, 2]), 3)

    def test_negative_numbers(self):
        self.assertEqual(count_nums([-1, 11, -11]), 1)

    def test_mixed_numbers(self):
        self.assertEqual(count_nums([1, -1, 11, -11, 0]), 2)

    def test_large_numbers(self):
        self.assertEqual(count_nums([123, -456, 789, -1011]), 2)

    def test_single_digit_numbers(self):
        self.assertEqual(count_nums([1, -2, 3, -4, 5, -6]), 3)

    def test_zero(self):
        self.assertEqual(count_nums([0]), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases to ensure that the `count_nums` function is working correctly. It tests with empty lists, lists of positive numbers, lists of negative numbers, and a mix of positive and negative numbers. It also tests with large numbers and single-digit numbers, as well as a list with a single zero.