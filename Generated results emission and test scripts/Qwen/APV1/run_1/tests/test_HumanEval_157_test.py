system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return a * a == b * b + c * c or b * b == a * a + c * c or c * c == a * a + b * b


assistant

import unittest

# Function to be tested
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

    def test_invalid_input(self):
        # Test case 6: Invalid input type (list instead of tuple)
        try:
            right_angle_triangle([3, 4, 5])
            self.fail("Expected TypeError")
        except TypeError as e:
            self.assertIsInstance(e, TypeError)

        # Test case 7: Invalid input length (tuple with less than 3 elements)
        try:
            right_angle_triangle((3, 4))
            self.fail("Expected ValueError")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)

        # Test case 8: Invalid input value (negative number)
        try:
            right_angle_triangle(-3, -4, -5)
            self.fail("Expected ValueError")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestRightAngleTriangle` class that inherits from `unittest.TestCase`. It contains two methods: `test_right_angle_triangle`, which tests various cases including valid and invalid inputs, and `test_invalid_input`, which checks for potential errors when passing incorrect types or values to the function. The `unittest.main()` call at the end runs all the defined tests.