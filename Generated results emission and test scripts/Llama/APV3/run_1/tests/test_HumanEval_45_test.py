system

### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_45_code import triangle_area
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
    unittest.main()user

### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_45_code import triangle_area
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def triangle_area(a, h):
    """Given length of a side and height, return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return a * h / 2.0assistant

import unittest
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):
    def test_valid_input(self):
        self.assertAlmostEqual(triangle_area(5, 3), 7.5)

    def test_zero_height(self):
        self.assertEqual(triangle_area(5, 0), 0)

    def test_zero_base(self):
        self.assertEqual(triangle_area(0, 3), 0)

    def test_negative_base(self):
        self.assertEqual(triangle_area(-5, 3), 0)

    def test_negative_height(self):
        self.assertEqual(triangle_area(5, -3), 0)

    def test_non_numeric_base(self):
        with self.assertRaises(TypeError):
            triangle_area('a', 3)

    def test_non_numeric_height(self):
        with self.assertRaises(TypeError):
            triangle_area(5, 'b')

if __name__ == '__main__':
    unittest.main()