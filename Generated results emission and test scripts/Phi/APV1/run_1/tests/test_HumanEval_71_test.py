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

 import unittest
from HumanEval_71_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_valid_triangle(self):
        self.assertAlmostEqual(triangle_area(3, 4, 5), 6.00)

    def test_invalid_triangle_with_zero(self):
        self.assertEqual(triangle_area(1, 2, 0), -1)

    def test_invalid_triangle_with_negative(self):
        self.assertEqual(triangle_area(-1, 2, 3), -1)

    def test_invalid_triangle_with_non_positive(self):
        self.assertEqual(triangle_area(0, 0, 0), -1)

    def test_invalid_triangle_with_equal_sides(self):
        self.assertEqual(triangle_area(1, 1, 1), -1)

    def test_invalid_triangle_with_large_numbers(self):
        self.assertEqual(triangle_area(1000000, 1000000, 1000000), -1)

    def test_invalid_triangle_with_small_numbers(self):
        self.assertEqual(triangle_area(0.0001, 0.0001, 0.0001), -1)

    def test_invalid_triangle_with_large_small_numbers(self):
        self.assertEqual(triangle_area(1000000, 0.0001, 0.0001), -1)

    def test_invalid_triangle_with_equal_large_numbers(self):
        self.assertEqual(triangle_area(1000000, 1000000, 1000000), -1)

if __name__ == '__main__':
    unittest.main()