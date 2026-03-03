### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_133_code import sum_squares
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
2. Include: from HumanEval_133_code import sum_squares
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i) ** 2
    return squared

 import unittest
from HumanEval_133_code import sum_squares

class TestSumSquares(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(sum_squares([1, 2, 3]), 14)

    def test_positive_mixed_numbers(self):
        self.assertEqual(sum_squares([1.4, 4.2, 0]), 29)

    def test_negative_integers(self):
        self.assertEqual(sum_squares([-2, -1]), 6)

    def test_mixed_integers(self):
        self.assertEqual(sum_squares([1, -2, 3]), 14)

    def test_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

    def test_single_element(self):
        self.assertEqual(sum_squares([5]), 25)

    def test_multiple_elements(self):
        self.assertEqual(sum_squares([1, 4, 9]), 98)

    def test_large_numbers(self):
        self.assertEqual(sum_squares([100, 200, 300]), 140000)

    def test_edge_case_with_zero(self):
        self.assertEqual(sum_squares([0]), 0)

    def test_edge_case_with_negative_zero(self):
        self.assertEqual(sum_squares([-0]), 0)

if __name__ == '__main__':
    unittest.main()