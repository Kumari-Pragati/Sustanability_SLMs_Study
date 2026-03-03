### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_116_code import sort_array
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
2. Include: from HumanEval_116_code import sort_array
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))

 import unittest

from HumanEval_116_code import sort_array

class TestSortArray(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])

    def test_negative_integers(self):
        self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])

    def test_zero_integers(self):
        self.assertEqual(sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 3, 4])

    def test_edge_case_single_element(self):
        self.assertEqual(sort_array([5]), [5])

    def test_edge_case_empty_list(self):
        self.assertEqual(sort_array([]), [])

    def test_edge_case_single_negative(self):
        self.assertEqual(sort_array([-1]), [-1])

    def test_edge_case_single_positive(self):
        self.assertEqual(sort_array([1]), [1])

    def test_edge_case_all_zeros(self):
        self.assertEqual(sort_array([0]), [0])

    def test_edge_case_all_ones(self):
        self.assertEqual(sort_array([1]), [1])

    def test_edge_case_all_twos(self):
        self.assertEqual(sort_array([2]), [2])

    def test_edge_case_all_fives(self):
        self.assertEqual(sort_array([5]), [5])

    def test_edge_case_all_sevens(self):
        self.assertEqual(sort_array([7]), [7])

    def test_edge_case_all_threes(self):
        self.assertEqual(sort_array([3]), [3])

    def test_edge_case_all_nines(self):
        self.assertEqual(sort_array([9]), [9])

    def test_edge_case_all_eights(self):
        self.assertEqual(sort_array([8]), [8])

    def test_edge_case_all_ten_twos(self):
        self.assertEqual(sort_array([2, 2, 2, 2, 2, 2, 2, 2, 2, 2]), [2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

    def test_edge_case_all_ten_fives(self):
        self.assertEqual(sort_array([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]), [5, 5, 5, 5, 5, 5, 5, 5, 5, 5])

if __name__ == '__main__0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000