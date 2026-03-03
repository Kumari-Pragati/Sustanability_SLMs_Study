You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the `triangle_area` function:


import unittest
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(triangle_area(5, 3), 7.5)
        self.assertEqual(triangle_area(3, 4), 6.0)
        self.assertEqual(triangle_area(6, 8), 24.0)
        self.assertEqual(triangle_area(1, 1), 0.5)
        self.assertEqual(triangle_area(0, 5), 0.0)
        self.assertEqual(triangle_area(10, 0), 0.0)
        self.assertAlmostEqual(triangle_area(5.5, 3.2), 10.2)
        self.assertRaises(ValueError, triangle_area, 0, 5)
        self.assertRaises(ValueError, triangle_area, 5, 0)
        self.assertRaises(TypeError, triangle_area, "a", 3)
        self.assertRaises(TypeError, triangle_area, 5, "h")

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases for different inputs, edge cases, and error handling scenarios. It uses the `assertEqual` method to check if the function returns the expected result, `assertAlmostEqual` to compare floating-point numbers, and `assertRaises` to check if the function raises the expected exceptions.