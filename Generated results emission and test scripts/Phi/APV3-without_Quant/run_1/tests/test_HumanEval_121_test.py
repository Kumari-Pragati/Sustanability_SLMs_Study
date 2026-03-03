### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_121_code import solution
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
2. Include: from HumanEval_121_code import solution
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    
    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==> 0
    """
    return sum([x for idx, x in enumerate(lst) if idx % 2 == 0 and x % 2 == 1])

 import unittest
from HumanEval_121_code import solution

class TestSolution(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(solution([5, 8, 7, 1]), 12)
        self.assertEqual(solution([3, 3, 3, 3, 3]), 9)
        self.assertEqual(solution([30, 13, 24, 321]), 0)

    def test_empty_list(self):
        self.assertEqual(solution([]), 0)

    def test_single_element(self):
        self.assertEqual(solution([1]), 0)

    def test_all_odd_even_positions(self):
        self.assertEqual(solution([1, 3, 5, 7]), 1 + 5)

    def test_all_even_odd_positions(self):
        self.assertEqual(solution([2, 4, 6, 8]), 0)

    def test_all_odd_odd_positions(self):
        self.assertEqual(solution([1, 3, 5, 7, 9]), 1 + 9)

    def test_all_even_even_positions(self):
        self.assertEqual(solution([2, 4, 6, 8, 10]), 0)

    def test_mixed_odd_even_positions(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6]), 1 + 5)

    def test_mixed_odd_even_values(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7]), 1 + 7)

    def test_mixed_odd_even_values_with_zeros(self):
        self.assertEqual(solution([0, 2, 0, 4, 0, 6, 0, 8]), 0)

if __name__ == '__main__':
    unittest.main()