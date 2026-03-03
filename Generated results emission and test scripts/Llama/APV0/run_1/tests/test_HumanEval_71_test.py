user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_71_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.00)

    def test_invalid_triangle(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)

    def test_zero_side(self):
        self.assertEqual(triangle_area(0, 0, 0), -1)

    def test_negative_side(self):
        self.assertEqual(triangle_area(-1, 2, 3), -1)

    def test_equal_sides(self):
        self.assertEqual(triangle_area(1, 1, 2), 0.47)

    def test_zero_area(self):
        self.assertEqual(triangle_area(1, 1, 1), 0.00)

if __name__ == '__main__':
    unittest.main()


This script includes six test cases:

- `test_valid_triangle`: Tests the function with a valid triangle (3, 4, 5).
- `test_invalid_triangle`: Tests the function with an invalid triangle (1, 2, 10).
- `test_zero_side`: Tests the function with a triangle where one side is zero.
- `test_negative_side`: Tests the function with a triangle where one side is negative.
- `test_equal_sides`: Tests the function with a triangle where two sides are equal.
- `test_zero_area`: Tests the function with a triangle where the area is zero.