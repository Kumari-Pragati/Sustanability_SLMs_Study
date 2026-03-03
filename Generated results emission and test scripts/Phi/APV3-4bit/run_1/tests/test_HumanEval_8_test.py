### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_8_code import sum_product
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
2. Include: from HumanEval_8_code import sum_product
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """Return a pair (sum, product) for the given list of integers.
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    >>> sum_product([])
    (0, 1)
    """
    sum_value = 0
    prod_value = 1
    for n in numbers:
        sum_value += n
        prod_value *= n
    return sum_value, prod_value

 import unittest

from HumanEval_8_code import sum_product

class TestSumProduct(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(sum_product([1, 2, 3, 4]), (10, 24))

    def test_negative_numbers(self):
        self.assertEqual(sum_product([-1, -2, -3]), (-6, 6))

    def test_empty_list(self):
        self.assertEqual(sum_product([]), (0, 1))

    def test_single_number(self):
        self.assertEqual(sum_product([5]), (5, 5))

    def test_zero_list(self):
        self.assertEqual(sum_product([0, 0]), (0, 0))

    def test_all_zeros(self):
        self.assertEqual(sum_product([0, 0, 0]), (0, 0))

    def test_all_positive(self):
        self.assertEqual(sum_product([1, 2, 3, 4, 5]), (15, 120))

    def test_all_negative(self):
        self.assertEqual(sum_product([-1, -2, -3, -4]), (-10, 24))

    def test_all_mixed(self):
        self.assertEqual(sum_product([1, -2, 3, -4]), (2, -24))

    def test_all_zeros_and_one(self):
        self.assertEqual(sum_product([0, 1]), (1, 0))

    def test_all_ones(self):
        self0self.assertEqual(sum_product([1, 1, 1, 1]), (4, 1))

    def test_all_mixed_and_one(self):
        self.assertEqual(sum_product([1, -1, 1]), (1, -1))

    def test_all_mixed_and_zero(self):
        self.assertEqual(sum_product([0, -1, 1]), (0, 0))

    def test_all_mixed_and_negative(self):
        self.assertEqual(sum_product([-1, 1, -1]), (-3, -1))

    def test_all_mixed_and_positive(self):
        self.assertEqual(sum_product([1, -1, 1, 1]), (3, 1))

    def test_all_mixed_and_zero_list(self):
        self.assertEqual(sum_product([0, -1, 1, 0]), (0, 0))

    def test_all_mixed_and_negative_list(self):
        self.assertEqual(sum_product([-1, 1, -1, -1]), (-4, -1))

    def test_all_mixed_and_positive_list(self):
        self.assertEqual(sum_product([1, -1, 1, 1, -1]), (0, -1))

if __name__ == '__main__':
    unittest.main()