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
   - Include from HumanEval_71_code import triangle_area
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

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_71_code import triangle_area
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1.
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.

    Example:
        triangle_area(3, 4, 5) == 6.00
        triangle_area(1, 2, 10) == -1
    '''
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area


assistant

import unittest

from HumanEval_71_code import triangle_area

class TestTriangleArea(unittest.TestCase):
    
    def test_valid_triangle(self):
        # Valid triangle case
        result = triangle_area(3, 4, 5)
        self.assertAlmostEqual(result, 6.00, places=2)
        
    def test_invalid_triangle(self):
        # Invalid triangle case
        result = triangle_area(1, 2, 10)
        self.assertAlmostEqual(result, -1, places=2)
        
    def test_zero_sides(self):
        # Case where one or more sides are zero
        result = triangle_area(0, 4, 5)
        self.assertAlmostEqual(result, -1, places=2)
        
    def test_one_side_zero(self):
        # Case where one side is zero
        result = triangle_area(3, 0, 5)
        self.assertAlmostEqual(result, -1, places=2)
        
    def test_two_sides_zero(self):
        # Case where two sides are zero
        result = triangle_area(3, 4, 0)
        self.assertAlmostEqual(result, -1, places=2)
        
    def test_all_negative(self):
        # Case where all sides are negative
        result = triangle_area(-3, -4, -5)
        self.assertAlmostEqual(result, -1, places=2)
        
    def test_all_positive(self):
        # Case where all sides are positive
        result = triangle_area(3, 4, 5)
        self.assertAlmostEqual(result, 6.00, places=2)
        
    def test_float_input(self):
        # Case where input values are floats
        result = triangle_area(3.0, 4.0, 5.0)
        self.assertAlmostEqual(result, 6.00, places=2)
        
    def test_string_input(self):
        # Case where input values are strings
        result = triangle_area("3", "4", "5")
        self.assertAlmostEqual(result, -1, places=2)
        
    def test_none_input(self):
        # Case where input values are None
        result = triangle_area(None, None, None)
        self.assertAlmostEqual(result, -1, places=2)
        
    def test_mixed_input(self):
        # Case where input values are mixed types
        result = triangle_area(3, "4", 5)
        self.assertAlmostEqual(result, -1, places=2)
        
    def test_large_input(self):
        # Case where input values are large numbers
        result = triangle_area(1e9, 1e9, 2e9)
        self.assertAlmostEqual(result, 6.00, places=2)
        
    def test_small_input(self):
        # Case where input values are small numbers
        result = triangle_area(1e-9, 1e-9, 2e-9)
        self.assertAlmostEqual(result, -1, places=2)
        
    def test_complex_input(self):
        # Case where input values are complex numbers
        result = triangle_area(3+4j, 4+5j, 5+6j)
        self.assertAlmostEqual(result, -1, places=2)
        
    def test_nan_input(self):
        # Case where input values are NaN
        result = triangle_area(float('nan'), float('nan'), float('nan'))
        self.assertAlmostEqual(result, -1, places=2)
        
    def test_inf_input(self):
        # Case where input values are infinity
        result = triangle_area(float('inf'), float('inf'), float('inf'))
        self.assertAlmostEqual(result, -1, places=2)
        
    def test_neg_inf_input(self):
        # Case where input values are negative infinity
        result = triangle_area(float('-inf'), float('-inf'), float('-inf'))
        self.assertAlmostEqual(result, -1, places=2)
        
    def test_infinite_input(self):
        # Case where input value is infinite
        result = triangle_area(float('inf'), float('inf'), float('nan'))
        self.assertAlmostEqual(result, -1, places=2)
        
    def test_non_numeric_input(self):
        # Case where input values are non-numeric
        result = triangle_area("3", "4", "5")
        self.assertAlmostEqual(result, -1, places=2)
        
    def test_empty_tuple_input(self):
        # Case where input values are empty tuple
        result = triangle_area(())
        self.assertAlmostEqual(result, -1, places=2)
        
    def test_single_element_tuple_input(self):
        # Case where input values are single element tuple
        result = triangle_area((1,))
        self.assertAlmostEqual(result, -1, places=2)
        
    def test_multiple_elements_tuple_input(self):
        # Case where input values are multiple elements tuple
        result = triangle_area((1, 2))
        self.assertAlmostEqual(result, -1, places=