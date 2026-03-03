system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    return a * h / 2.0assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_triangle_area(self):
        self.assertAlmostEqual(triangle_area(5, 3), 7.5)
        self.assertAlmostEqual(triangle_area(10, 6), 30.0)
        self.assertAlmostEqual(triangle_area(2, 1), 1.0)
        self.assertAlmostEqual(triangle_area(0, 0), 0.0)
        self.assertAlmostEqual(triangle_area(5, 0), 0.0)
        self.assertAlmostEqual(triangle_area(0, 3), 0.0)

if __name__ == '__main__':
    unittest.main()