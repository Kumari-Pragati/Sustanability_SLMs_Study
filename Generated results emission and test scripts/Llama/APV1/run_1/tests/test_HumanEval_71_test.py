user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
    return areaassistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_71_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.00)

    def test_invalid_triangle(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)

    def test_zero_side(self):
        self.assertEqual(triangle_area(0, 4, 5), -1)

    def test_negative_side(self):
        self.assertEqual(triangle_area(-1, 4, 5), -1)

    def test_equal_sides(self):
        self.assertEqual(triangle_area(3, 3, 5), -1)

    def test_zero_area(self):
        self.assertEqual(triangle_area(3, 3, 3), 0.00)

    def test_rounding(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.00)
        self.assertEqual(triangle_area(1, 2, 3), 0.47)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            triangle_area('a', 4, 5)

        with self.assertRaises(TypeError):
            triangle_area(3, 'b', 5)

        with self.assertRaises(TypeError):
            triangle_area(3, 4, 'c')

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            triangle_area(-1, 4, 5)

        with self.assertRaises(ValueError):
            triangle_area(1, 2, 0)

        with self.assertRaises(ValueError):
            triangle_area(1, 2, -1)

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios, including valid and invalid triangles, zero and negative sides, equal sides, zero area, rounding, invalid input types, and invalid input values.