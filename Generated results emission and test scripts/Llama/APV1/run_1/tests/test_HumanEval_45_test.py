user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_triangle_area_positive_numbers(self):
        self.assertAlmostEqual(triangle_area(5, 3), 7.5)

    def test_triangle_area_zero_height(self):
        self.assertEqual(triangle_area(5, 0), 0)

    def test_triangle_area_zero_base(self):
        self.assertEqual(triangle_area(0, 3), 0)

    def test_triangle_area_negative_numbers(self):
        self.assertAlmostEqual(triangle_area(-5, -3), 7.5)

    def test_triangle_area_mixed_numbers(self):
        self.assertAlmostEqual(triangle_area(5, -3), 7.5)

    def test_triangle_area_non_numeric_input(self):
        with self.assertRaises(TypeError):
            triangle_area('a', 3)

    def test_triangle_area_non_numeric_input2(self):
        with self.assertRaises(TypeError):
            triangle_area(5, 'b')

    def test_triangle_area_non_numeric_input3(self):
        with self.assertRaises(TypeError):
            triangle_area('a', 'b')

if __name__ == '__main__':
    unittest.main()


This test suite includes the following test cases:

1. `test_triangle_area_positive_numbers`: Tests the function with positive numbers.
2. `test_triangle_area_zero_height`: Tests the function with a zero height.
3. `test_triangle_area_zero_base`: Tests the function with a zero base.
4. `test_triangle_area_negative_numbers`: Tests the function with negative numbers.
5. `test_triangle_area_mixed_numbers`: Tests the function with mixed positive and negative numbers.
6. `test_triangle_area_non_numeric_input`: Tests the function with non-numeric input (string).
7. `test_triangle_area_non_numeric_input2`: Tests the function with non-numeric input (string) for the base.
8. `test_triangle_area_non_numeric_input3`: Tests the function with non-numeric input (string) for both the base and height.

These test cases cover various scenarios to ensure the function works correctly and handles different types of input.