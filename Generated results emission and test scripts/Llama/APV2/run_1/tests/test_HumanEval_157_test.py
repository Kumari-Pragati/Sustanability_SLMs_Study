system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_157_code import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):

    def test_right_angle_triangle_true(self):
        self.assertTrue(right_angle_triangle(3, 4, 5))

    def test_right_angle_triangle_false(self):
        self.assertFalse(right_angle_triangle(1, 2, 3))

    def test_right_angle_triangle_edge_case1(self):
        self.assertTrue(right_angle_triangle(0, 0, 0))

    def test_right_angle_triangle_edge_case2(self):
        self.assertFalse(right_angle_triangle(0, 0, 1))

    def test_right_angle_triangle_edge_case3(self):
        self.assertTrue(right_angle_triangle(0, 0, 0))

    def test_right_angle_triangle_edge_case4(self):
        self.assertFalse(right_angle_triangle(0, 0, 1))

    def test_right_angle_triangle_edge_case5(self):
        self.assertTrue(right_angle_triangle(0, 0, 0))

    def test_right_angle_triangle_edge_case6(self):
        self.assertFalse(right_angle_triangle(0, 0, 1))

if __name__ == '__main__':
    unittest.main()