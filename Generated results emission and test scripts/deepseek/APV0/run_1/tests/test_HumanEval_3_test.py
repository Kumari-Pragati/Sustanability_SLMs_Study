You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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
    return False


### Response:
Here is a unittest script for the given function:


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

    def test_multiple_negative_operations(self):
        self.assertTrue(below_zero([-1, -2, -3]))

    def test_multiple_positive_operations(self):
        self.assertFalse(below_zero([1, 2, 3]))

    def test_mixed_operations(self):
        self.assertTrue(below_zero([1, -2, 3, -4]))

if __name__ == '__main__':
    unittest.main()


This script includes a series of test cases to cover different scenarios, including:
- No negative balance
- Negative balance
- Single negative operation
- Single positive operation
- Empty operations
- Multiple negative operations
- Multiple positive operations
- Mixed operations

Each test case checks the function's output against the expected result.

Please note that the above script assumes that the `below_zero` function is defined in a file named `HumanEval_3_code.py` in the same directory. If the function is defined in a different file, you will need to import it accordingly.