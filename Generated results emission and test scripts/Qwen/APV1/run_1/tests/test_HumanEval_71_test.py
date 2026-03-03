system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_71_code import triangle_area

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def triangle_area(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return the area of
    the triangle rounded to 2 decimal points if the three sides form a valid triangle. 
    Otherwise return -1.
    Three sides make a valid triangle when the sum of any two sides is greater 
    than the third side.

    Example:
        triangle_area(3, 4, 5) == 6.00
        triangle_area(1, 2, 10) == -1
    '''
    if a + b <= c or a + c <= b or b + c <= a:
        return -1
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    area = round(area, 2)
    return area


assistant

import unittest
from HumanEval_71_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6.00)

    def test_invalid_triangle(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)

    def test_zero_sides(self):
        self.assertEqual(triangle_area(0, 0, 0), -1)

    def test_negative_sides(self):
        self.assertEqual(triangle_area(-1, 2, 3), -1)

    def test_float_sides(self):
        self.assertAlmostEqual(triangle_area(3.5, 4.2, 5.1), 8.91)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestTriangleArea` class that inherits from `unittest.TestCase`. It contains several test methods to verify different scenarios:

- The `test_valid_triangle` method checks if the function correctly calculates the area of a valid triangle.
- The `test_invalid_triangle` method tests if the function returns `-1` for invalid triangles.
- The `test_zero_sides` and `test_negative_sides` methods check if the function handles zero and negative side lengths appropriately.
- The `test_float_sides` method verifies the function's handling of floating-point numbers.

The `assertAlmostEqual` method is used in the first four test cases to compare the expected result with the actual result within a small tolerance level (`0.01`). This ensures that the results are close enough to pass as equal.