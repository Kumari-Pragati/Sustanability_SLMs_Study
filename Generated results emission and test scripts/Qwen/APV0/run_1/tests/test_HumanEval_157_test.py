system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b


assistant

import unittest

# Importing the function to be tested
from HumanEval_157_code import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):

    def test_right_angle_triangle(self):
        # Test case 1: Right-angled triangle (3, 4, 5)
        self.assertTrue(right_angle_triangle(3, 4, 5))
        
        # Test case 2: Not a right-angled triangle (1, 2, 3)
        self.assertFalse(right_angle_triangle(1, 2, 3))

        # Test case 3: Another right-angled triangle (5, 12, 13)
        self.assertTrue(right_angle_triangle(5, 12, 13))

        # Test case 4: Not a right-angled triangle (6, 8, 10)
        self.assertFalse(right_angle_triangle(6, 8, 10))

        # Test case 5: Another right-angled triangle (7, 24, 25)
        self.assertTrue(right_angle_triangle(7, 24, 25))

        # Test case 6: Not a right-angled triangle (8, 15, 17)
        self.assertFalse(right_angle_triangle(8, 15, 17))

        # Test case 7: Another right-angled triangle (9, 40, 41)
        self.assertTrue(right_angle_triangle(9, 40, 41))

        # Test case 8: Not a right-angled triangle (10, 24, 26)
        self.assertFalse(right_angle_triangle(10, 24, 26))

    def test_invalid_input(self):
        # Test case 9: Invalid input type (list instead of tuple)
        self.assertRaises(TypeError, right_angle_triangle, [3, 4, 5])

        # Test case 10: Invalid input length (less than 3 elements)
        self.assertRaises(ValueError, right_angle_triangle, 3)

        # Test case 11: Invalid input format (not all numbers)
        self.assertRaises(ValueError, right_angle_triangle, "a", "b", "c")

if __name__ == '__main__':
    unittest.main()


This script imports the `right_angle_triangle` function and creates a unit test class named `TestRightAngleTriangle`. It includes several test cases to verify the correctness of the function under different conditions, such as valid inputs forming a right-angled triangle and invalid inputs like lists or strings that do not represent valid side lengths. The `unittest.main()` call at the end makes the tests executable when run directly.