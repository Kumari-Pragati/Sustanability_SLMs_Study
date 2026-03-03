You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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
    return False


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_3_code import below_zero

class TestBelowZero(unittest.TestCase):

    def test_no_negative_balance(self):
        self.assertFalse(below_zero([1, 2, 3]))

    def test_negative_balance(self):
        self.assertTrue(below_zero([1, 2, -4, 5]))

    def test_single_negative_operation(self):
        self.assertTrue(below_zero([-1]))

    def test_single_positive_operation(self):
        self.assertFalse(below_zero([1]))

    def test_empty_operations(self):
        self.assertFalse(below_zero([]))

    def test_mixed_operations(self):
        self.assertTrue(below_zero([1, -2, 3, -4]))

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different scenarios:

- `test_no_negative_balance`: Tests when the balance never goes below zero.
- `test_negative_balance`: Tests when the balance goes below zero at some point.
- `test_single_negative_operation`: Tests when there's only one negative operation.
- `test_single_positive_operation`: Tests when there's only one positive operation.
- `test_empty_operations`: Tests when there are no operations (balance remains at zero).
- `test_mixed_operations`: Tests when there are both positive and negative operations.

Each test case checks the function's output against the expected result.