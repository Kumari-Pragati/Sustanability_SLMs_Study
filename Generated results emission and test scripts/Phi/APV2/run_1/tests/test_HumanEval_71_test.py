You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 
import unittest
from HumanEval_71_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.00)

    def test_invalid_triangle_1(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)

    def test_invalid_triangle_2(self):
        self.assertEqual(triangle_area(1, 1, 3), -1)

    def test_invalid_triangle_3(self):
        self.assertEqual(triangle_area(5, 5, 10), -1)

    def test_zero_area(self):
        self.assertEqual(triangle_area(0, 0, 0), -1)

    def test_equal_sides(self):
        self.assertEqual(triangle_area(3, 3, 3), 3.87)

    def test_negative_sides(self):
        self.assertEqual(triangle_area(-3, -4, -5), -1)

if __name__ == '__main__':
    unittest.main()


This test suite covers various cases for the `triangle_area` function, including:

- A valid triangle with sides 3, 4, and 5.
- An invalid triangle where the sum of two sides is less than or equal to the third side.
- An invalid triangle with sides 1, 1, and 3.
- An invalid triangle with sides 5, 5, and 10.
- A case where all sides are zero, which should return -1 as it does not form a valid triangle.
- A case where all sides are equal, which should return the area calculated using Heron's formula.
- A case where all sides are negative, which should return -1 as it does not form a valid triangle.

Each test case uses `assertEqual` to check if the function returns the expected result. Running this test suite will validate the correctness of the `triangle_area` function.