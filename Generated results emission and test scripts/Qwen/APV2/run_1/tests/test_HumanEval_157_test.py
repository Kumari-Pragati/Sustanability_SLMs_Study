system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Importing the function from the given module
from HumanEval_157_code import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):

    def test_right_angle_triangle(self):
        # Test cases to verify the correctness of the right_angle_triangle function
        self.assertTrue(right_angle_triangle(3, 4, 5))
        self.assertFalse(right_angle_triangle(1, 2, 3))
        self.assertTrue(right_angle_triangle(5, 12, 13))

    def test_invalid_input(self):
        # Test invalid input scenarios
        self.assertRaises(ValueError, right_angle_triangle, -1, 2, 3)
        self.assertRaises(TypeError, right_angle_triangle, "a", 2, 3)

if __name__ == '__main__':
    unittest.main()


This test suite includes two main tests:

1. `test_right_angle_triangle` checks that the function correctly identifies right-angle triangles by verifying it returns `True` for valid inputs (e.g., 3, 4, 5).
2. `test_invalid_input` uses assertions to check that the function raises exceptions when provided with invalid types or values (e.g., non-numeric strings).

The `unittest.main()` call at the end runs all defined tests within the `TestRightAngleTriangle` class.