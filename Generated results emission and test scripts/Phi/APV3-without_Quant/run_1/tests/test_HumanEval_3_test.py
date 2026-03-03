### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_3_code import below_zero
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()
 ### Immediate Task
Write the complete unittest test suite for the following Python function.

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
    def test_balance_never_below_zero(self):
        self.assertFalse(below_zero([1, 2, 3]))

    def test_balance_falls_below_zero(self):
        self.assertTrue(below_zero([1, 2, -4, 5]))

    def test_balance_falls_below_zero_early(self):
        self.assertTrue(below_zero([1, -5, 2]))

    def test_balance_falls_below_zero_multiple_times(self):
        self.assertTrue(below_zero([1, -3, 2, -4, 5]))

    def test_balance_never_below_zero_with_large_numbers(self):
        self.assertFalse(below_zero([1000000, 2000000, 3000000]))

    def test_balance_falls_below_zero_with_large_numbers(self):
        self.assertTrue(below_zero([1000000, -2000000, 3000000]))

    def test_balance_falls_below_zero_with_zero_operations(self):
        self.assertFalse(below_zero([]))

    def test_balance_falls_below_zero_with_negative_operations(self):
        self.assertTrue(below_zero([-1, -2, -3]))

    def test_balance_falls_below_zero_with_negative_operations_early(self):
        self.assertTrue(below_zero([-1, -5, -2]))

if __name__ == '__main__':
    unittest.main()