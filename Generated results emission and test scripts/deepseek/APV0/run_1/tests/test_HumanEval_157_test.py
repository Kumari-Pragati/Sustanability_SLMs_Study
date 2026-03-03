You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_157_code import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):

    def test_right_angle(self):
        self.assertTrue(right_angle_triangle(3, 4, 5))
        self.assertTrue(right_angle_triangle(5, 12, 13))
        self.assertTrue(right_angle_triangle(8, 15, 17))

    def test_not_right_angle(self):
        self.assertFalse(right_angle_triangle(1, 2, 3))
        self.assertFalse(right_angle_triangle(6, 8, 10))
        self.assertFalse(right_angle_triangle(7, 24, 25))

if __name__ == '__main__':
    unittest.main()


This script includes two test methods: `test_right_angle` and `test_not_right_angle`. The first method tests the function with some right-angled triangles and asserts that the function returns True in these cases. The second method tests the function with some non-right-angled triangles and asserts that the function returns False in these cases.

Please note that you need to have the function `right_angle_triangle` in a file named `HumanEval_157_code.py` in the same directory as this test script for it to work.