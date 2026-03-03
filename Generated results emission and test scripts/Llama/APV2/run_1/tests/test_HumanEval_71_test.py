system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

Here is the complete unittest test suite for the given Python function:


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

    def test_non_integer_sides(self):
        self.assertEqual(triangle_area(3.5, 4.2, 5.1), 6.00)

if __name__ == '__main__':
    unittest.main()