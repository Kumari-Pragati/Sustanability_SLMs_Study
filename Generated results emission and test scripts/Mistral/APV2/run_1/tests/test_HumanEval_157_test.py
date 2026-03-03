You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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
    return a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b

 Here is a complete unittest test suite for the provided Python function `right_angle_triangle`. I've included several test cases to cover various scenarios.


import unittest
from HumanEval_157_code import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):

    def test_right_angle_triangle(self):
        self.assertTrue(right_angle_triangle(3, 4, 5))
        self.assertFalse(right_angle_triangle(1, 2, 3))
        self.assertFalse(right_angle_triangle(5, 121, 144))  # large numbers
        self.assertFalse(right_angle_triangle(2, 8, 10))  # not a right-angled triangle
        self.assertTrue(right_angle_triangle(12, 16, 20))  # another right-angled triangle
        self.assertFalse(right_angle_triangle(0, 0, 0))  # no sides
        self.assertFalse(right_angle_triangle(0, 0, 1))  # invalid side length
        self.assertFalse(right_angle_triangle(-3, 4, 5))  # negative side length

if __name__ == '__main__':
    unittest.main()


This test suite includes test cases for valid right-angled triangles, invalid triangles, large numbers, negative side lengths, and zero side lengths.