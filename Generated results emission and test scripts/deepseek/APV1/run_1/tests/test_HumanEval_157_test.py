You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_157_code import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):

    def test_right_angle(self):
        self.assertTrue(right_angle_triangle(3, 4, 5))
        self.assertTrue(right_angle_triangle(5, 12, 13))
        self.assertTrue(right_angle_triangle(6, 8, 10))

    def test_not_right_angle(self):
        self.assertFalse(right_angle_triangle(1, 2, 3))
        self.assertFalse(right_angle_triangle(2, 3, 4))
        self.assertFalse(right_angle_triangle(7, 8, 9))

    def test_negative_values(self):
        self.assertFalse(right_angle_triangle(-1, 2, 3))
        self.assertFalse(right_angle_triangle(2, -3, 4))
        self.assertFalse(right_angle_triangle(-7, 8, -9))

    def test_zero_values(self):
        self.assertFalse(right_angle_triangle(0, 2, 3))
        self.assertFalse(right_angle_triangle(2, 0, 4))
        self.assertFalse(right_angle_triangle(0, 8, 0))

    def test_non_integer_values(self):
        self.assertFalse(right_angle_triangle(1.5, 2, 3))
        self.assertFalse(right_angle_triangle(2, 3.5, 4))
        self.assertFalse(right_angle_triangle(7, 8, 9.5))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for a right-angled triangle, a non-right-angled triangle, negative values, zero values, and non-integer values. It uses the `assertTrue` and `assertFalse` methods to check if the function returns the expected results.