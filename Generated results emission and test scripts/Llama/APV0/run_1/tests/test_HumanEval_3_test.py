user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

Here is the unittest test script for the `below_zero` function:

import unittest
from HumanEval_3_code import below_zero

class TestBelowZero(unittest.TestCase):
    def test_positive_balance(self):
        self.assertFalse(below_zero([1, 2, 3]))

    def test_negative_balance(self):
        self.assertTrue(below_zero([1, 2, -4, 5]))

    def test_zero_balance(self):
        self.assertFalse(below_zero([0, 0, 0]))

    def test_single_negative_operation(self):
        self.assertTrue(below_zero([-1]))

    def test_multiple_negative_operations(self):
        self.assertTrue(below_zero([-1, -2, -3]))

    def test_positive_operations_only(self):
        self.assertFalse(below_zero([1, 2, 3, 4]))

    def test_mixed_operations(self):
        self.assertTrue(below_zero([1, -2, 3, -4]))

if __name__ == '__main__':
    unittest.main()

This script defines a `TestBelowZero` class with seven test methods, each testing a different scenario:

1. `test_positive_balance`: Tests that the function returns `False` when the balance remains positive.
2. `test_negative_balance`: Tests that the function returns `True` when the balance falls below zero.
3. `test_zero_balance`: Tests that the function returns `False` when the balance remains zero.
4. `test_single_negative_operation`: Tests that the function returns `True` when there is a single negative operation.
5. `test_multiple_negative_operations`: Tests that the function returns `True` when there are multiple negative operations.
6. `test_positive_operations_only`: Tests that the function returns `False` when there are only positive operations.
7. `test_mixed_operations`: Tests that the function returns `True` when there are both positive and negative operations.

You can run this script directly to execute the tests.