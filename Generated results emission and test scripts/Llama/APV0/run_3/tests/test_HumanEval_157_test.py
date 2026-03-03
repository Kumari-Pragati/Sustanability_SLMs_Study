user

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
    return a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * bassistant

Here is the unittest test script for the `right_angle_triangle` function:

import unittest
from HumanEval_157_code import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):
    def test_right_angle_triangle(self):
        # Test cases
        self.assertTrue(right_angle_triangle(3, 4, 5))  # Example from problem statement
        self.assertTrue(right_angle_triangle(5, 12, 13))  # Another example
        self.assertFalse(right_angle_triangle(1, 2, 3))  # Not a right-angled triangle
        self.assertFalse(right_angle_triangle(0, 0, 0))  # All sides are zero
        self.assertFalse(right_angle_triangle(1, 1, 1))  # All sides are equal
        self.assertTrue(right_angle_triangle(2, 3, 4))  # Another example
        self.assertTrue(right_angle_triangle(5, 6, 7))  # Another example
        self.assertFalse(right_angle_triangle(-1, 2, 3))  # Negative side
        self.assertFalse(right_angle_triangle(1, -2, 3))  # Negative side
        self.assertFalse(right_angle_triangle(1, 2, -3))  # Negative side

if __name__ == '__main__':
    unittest.main()

This script defines a `TestRightAngleTriangle` class with a single method `test_right_angle_triangle`, which contains a series of test cases to verify the correctness of the `right_angle_triangle` function. The test cases cover various scenarios, including:

* Valid right-angled triangles (e.g., 3-4-5, 5-12-13)
* Non-right-angled triangles (e.g., 1-2-3, 0-0-0)
* Edge cases (e.g., all sides equal, negative sides)
* Additional examples to ensure the function is robust

The `unittest.main()` call at the end of the script runs the test cases and reports any failures or errors.