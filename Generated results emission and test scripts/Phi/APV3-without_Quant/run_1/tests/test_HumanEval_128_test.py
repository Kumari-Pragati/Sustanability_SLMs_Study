### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_128_code import prod_signs
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
2. Include: from HumanEval_128_code import prod_signs
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    if not arr:
        return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])

 import unittest

from HumanEval_128_code import prod_signs

class TestProdSigns(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(prod_signs([1, 2, 2, -4]), -9)

    def test_negative_numbers(self):
        self.assertEqual(prod_signs([-1, -2, -2, -4]), -8)

    def test_mixed_numbers(self):
        self.assertEqual(prod_signs([1, -2, 2, -4]), -14)

    def test_zero_numbers(self):
        self.assertEqual(prod_signs([0, 1]), 0)

    def test_all_negative_numbers(self):
        self.assertEqual(prod_signs([-1, -2, -3, -4]), -12)

    def test_all_positive_numbers(self):
        self.assertEqual(prod_signs([1, 2, 3, 4]), 20)

    def test_empty_list(self):
        self.assertIsNone(prod_signs([]))

    def test_single_zero(self):
        self.assertEqual(prod_signs([0]), 0)

    def test_single_negative(self):
        self.assertEqual(prod_signs([-1]), -1)

    def test_single_positive(self):
        self.assertEqual(prod_signs([1]), 1)

if __name__ == '__main__':
    unittest.main()