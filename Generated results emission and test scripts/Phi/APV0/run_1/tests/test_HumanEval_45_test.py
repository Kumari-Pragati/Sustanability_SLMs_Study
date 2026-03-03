Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_45_code import triangle_area
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def triangle_area(a, h):
    """Given length of a side and height, return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    return a * h / 2.0

 import unittest
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_triangle_area_with_positive_numbers(self):
        self.assertAlmostEqual(triangle_area(5, 3), 7.5)

    def test_triangle_area_with_zero_height(self):
        with self.assertRaises(ZeroDivisionError):
            triangle_area(5, 0)

    def test_triangle_area_with_negative_numbers(self):
        with self.assertRaises(ValueError):
            triangle_area(-5, 3)
        with self.assertRaises(ValueError):
            triangle_area(5, -3)

    def test_triangle_area_with_zero_side_length(self):
        with self.assertRaises(ValueError):
            triangle_area(0, 3)

if __name__ == '__main__':
    unittest.main()