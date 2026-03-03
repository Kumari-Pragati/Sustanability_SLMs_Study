### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_40_code import triples_sum_to_zero
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
2. Include: from HumanEval_40_code import triples_sum_to_zero
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    It returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            for k in range(j + 1, len(l)):
                if l[i] + l[j] + l[k] == 0:
                    return True
    return False

 import unittest

from HumanEval_40_code import triples_sum_to_zero

class TestTriplesSumToZero(unittest.TestCase):

    def test_normal_case(self):
        self.assertFalse(triples_sum_to_zero([1, 3, 5, 0]), "Should return False for a list without three elements summing to zero")
        self.assertTrue(triples_sum_to_zero([1, 3, -2, 1]), "Should return True for a list with three elements summing to zero")
        self.assertFalse(triples_sum_to_zero([1, 2, 3, 7]), "Should return False for a list without three elements summing to zero")
        self.assertTrue(triples_sum_to_zero([2, 4, -5, 3, 9, 7]), "Should return True for a list with three elements summing to zero")
        self.assertFalse(triples_sum_to_zero([1]), "Should return False for a list with less than three elements")

    def test_edge_case_with_duplicates(self):
        self.assertFalse(triples_sum_to_zero([0, 0, 0]), "Should return False for a list with all elements being zero")

    def test_edge_case_with_all_positive(self):
        self.assertFalse(triples_sum_to_zero([1, 2, 3, 4]), "Should return False for a list with all positive numbers")

    def test_edge_case_with_all_negative(self):
        self.assertFalse(triples_sum_to_zero([-1, -2, -3]), "Should return False for a list with all negative numbers")

    def test_edge_case_with_zero(self):
        self.assertFalse(triples_sum_to_zero([0]), "Should return False for a list with a single zero")

if __name__ == '__main__0':
    unittest.main()