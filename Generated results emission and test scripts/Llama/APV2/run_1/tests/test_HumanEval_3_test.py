system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return Falseassistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_3_code import below_zero

class TestBelowZero(unittest.TestCase):

    def test_below_zero(self):
        self.assertTrue(below_zero([1, 2, -4, 5]))

    def test_not_below_zero(self):
        self.assertFalse(below_zero([1, 2, 3]))

    def test_zero_balance(self):
        self.assertFalse(below_zero([0]))

    def test_single_operation_below_zero(self):
        self.assertTrue(below_zero([-1]))

    def test_single_operation_above_zero(self):
        self.assertFalse(below_zero([1]))

    def test_multiple_operations_above_zero(self):
        self.assertFalse(below_zero([1, 2, 3]))

    def test_multiple_operations_below_zero(self):
        self.assertTrue(below_zero([1, 2, -4, -5]))

if __name__ == '__main__':
    unittest.main()