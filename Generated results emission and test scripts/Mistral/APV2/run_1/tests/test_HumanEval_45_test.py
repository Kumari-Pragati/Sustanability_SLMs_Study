You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `triangle_area` function:


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

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different scenarios, such as positive and zero values for the base and height, as well as edge cases like a base of 0 or a height of 0. The test cases use the `assertEqual` method to compare the expected and actual results.