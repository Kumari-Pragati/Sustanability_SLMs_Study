Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b

 import unittest
from HumanEval_157_code import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):

    def test_right_angle_triangle_true(self):
        self.assertTrue(right_angle_triangle(3, 4, 5))
        self.assertTrue(right_angle_triangle(5, 12, 13))
        self.assertTrue(right_angle_triangle(7, 24, 25))

    def test_right_angle_triangle_false(self):
        self.assertFalse(right_angle_triangle(1, 2, 3))
        self.assertFalse(right_angle_triangle(6, 8, 10))
        self.assertFalse(right_angle_triangle(8, 15, 17))

    def test_right_angle_triangle_invalid_input(self):
        with self.assertRaises(ValueError):
            right_angle_triangle(-1, 2, 3)
        with self.assertRaises(ValueError):
            right_angle_triangle(0, 2, 3)
        with self.assertRaises(ValueError):
            right_angle_triangle(2, 0, 3)

if __name__ == '__main__':
    unittest.main()