You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_3_code import below_zero

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that
    starts with zero balance. Your task is to detect if at any point the balance of
    account falls below zero, and at that point function should return True.
    Otherwise, it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False

 Here is a comprehensive unittest test suite for the `below_zero` function:


import unittest
from HumanEval_3_code import below_zero

class TestBelowZero(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(below_zero([]))

    def test_positive_list(self):
        self.assertFalse(below_zero([1, 2, 3]))
        self.assertFalse(below_zero([100, 200, 300]))

    def test_zero_list(self):
        self.assertFalse(below_zero([0]))

    def test_zero_and_positive_list(self):
        self.assertFalse(below_zero([0, 1, 2, 3]))

    def test_negative_list(self):
        self.assertFalse(below_zero([-1, -2, -3]))

    def test_mixed_list(self):
        self.assertTrue(below_zero([1, 2, -4, 5]))
        self.assertTrue(below_zero([100, 200, -300, 400]))
        self.assertTrue(below_zero([-1, 0, 1, -2, 0, 1]))

    def test_large_list(self):
        operations = list(range(-1000, 1001))
        self.assertTrue(below_zero(operations))

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty list, positive numbers only, negative numbers only, mixed numbers, and large lists. It also tests the edge case where the list contains only zeros.