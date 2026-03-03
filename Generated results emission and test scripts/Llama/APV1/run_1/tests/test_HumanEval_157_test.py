user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_157_code import right_angle_triangle

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    return a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * bassistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_157_code import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):

    def test_right_angle_triangle_true(self):
        self.assertTrue(right_angle_triangle(3, 4, 5))
        self.assertTrue(right_angle_triangle(5, 12, 13))
        self.assertTrue(right_angle_triangle(1, 2, 3))

    def test_right_angle_triangle_false(self):
        self.assertFalse(right_angle_triangle(1, 2, 3))
        self.assertFalse(right_angle_triangle(2, 3, 4))
        self.assertFalse(right_angle_triangle(3, 4, 5))

    def test_right_angle_triangle_edge_cases(self):
        self.assertTrue(right_angle_triangle(0, 0, 0))
        self.assertFalse(right_angle_triangle(0, 0, 1))

    def test_right_angle_triangle_invalid_input(self):
        with self.assertRaises(TypeError):
            right_angle_triangle('a', 4, 5)
        with self.assertRaises(TypeError):
            right_angle_triangle(3, 'b', 5)
        with self.assertRaises(TypeError):
            right_angle_triangle(3, 4, 'c')

if __name__ == '__main__':
    unittest.main()


This test suite includes the following test cases:

- `test_right_angle_triangle_true`: Tests the function with known right-angled triangles.
- `test_right_angle_triangle_false`: Tests the function with known non-right-angled triangles.
- `test_right_angle_triangle_edge_cases`: Tests the function with edge cases, such as a triangle with all sides of zero length.
- `test_right_angle_triangle_invalid_input`: Tests the function with invalid input, such as non-numeric values.