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

 Here is a simple unittest test script for the provided function `right_angle_triangle`. The test cases cover the example provided in the function description and some additional edge cases.


import unittest
from HumanEval_157_code import right_angle_triangle

class TestRightAngleTriangle(unittest.TestCase):

    def test_right_angle_triangle(self):
        self.assertTrue(right_angle_triangle(3, 4, 5))
        self.assertFalse(right_angle_triangle(1, 2, 3))
        self.assertFalse(right_angle_triangle(0, 0, 0))
        self.assertFalse(right_angle_triangle(0, 0, 1))
        self.assertFalse(right_angle_triangle(1, 0, 0))
        self.assertFalse(right_angle_triangle(1, 1, 0))
        self.assertTrue(right_angle_triangle(5, 12, 13))  # Pythagorean triple
        self.assertTrue(right_angle_triangle(12, 16, 20))  # Pythagorean triple
        self.assertTrue(right_angle_triangle(20, 24, 28))  # Pythagorean triple

if __name__ == '__main__':
    unittest.main()


This test script defines a test case class `TestRightAngleTriangle` and includes a method `test_right_angle_triangle`. Inside this method, we have several assertions to test the function's behavior for different input combinations. If you run this script, it will execute the tests and print the results.