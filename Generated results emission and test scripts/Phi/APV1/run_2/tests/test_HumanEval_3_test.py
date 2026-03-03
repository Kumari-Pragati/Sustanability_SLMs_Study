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

 import unittest
from HumanEval_3_code import below_zero

class TestBelowZero(unittest.TestCase):
    def test_positive_operations(self):
        self.assertFalse(below_zero([1, 2, 3]), "The balance should not fall below zero with positive operations.")

    def test_negative_operations(self):
        self.assertTrue(below_zero([1, 2, -4, 5]), "The balance should fall below zero with negative operations.")

    def test_zero_operations(self):
        self.assertFalse(below_zero([0]), "The balance should not fall below zero with zero operations.")

    def test_single_negative_operation(self):
        self.assertTrue(below_zero([-1]), "The balance should fall below zero with a single negative operation.")

    def test_multiple_negative_operations(self):
        self.assertTrue(below_zero([1, -2, -3, -1]), "The balance should fall below zero with multiple negative operations.")

    def test_balance_remains_positive(self):
        self.assertFalse(below_zero([10, 5, 3]), "The balance should remain positive with all positive operations.")

    def test_balance_falls_below_zero_early(self):
        self.assertTrue(below_zero([1, -2, 1]), "The balance should fall below zero early in the sequence.")

    def test_balance_falls_below_zero_later(self):
        self.assertTrue(below_zero([1, 2, 3, -10, 1]), "The balance should fall below zero later in the sequence.")

    def test_balance_never_falls_below_zero(self):
        self.assertFalse(below_zero([1, 2, 3, 4, 5]), "The balance should never fall below zero with all positive operations.")

    def test_empty_list(self):
        self.assertFalse(below_zero([]), "The balance should not fall below zero with an empty list.")

    def test_single_element_list(self):
        self.assertFalse(below_zero([1]), "The balance should not fall below zero with a single element list.")

    def test_negative_balance_after_operations(self):
        self.assertTrue(below_zero([1, -2, -3]), "The balance should be negative after operations.")

if __name__ == '__main__':
    unittest.main()