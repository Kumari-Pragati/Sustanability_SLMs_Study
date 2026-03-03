system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Importing the function from the given module
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_triangle_area(self):
        # Test cases to verify the correctness of the triangle_area function
        self.assertAlmostEqual(triangle_area(5, 3), 7.5, msg="Expected 7.5, got {}".format(triangle_area(5, 3)))
        self.assertEqual(triangle_area(6, 4), 12.0, msg="Expected 12.0, got {}".format(triangle_area(6, 4)))
        self.assertEqual(triangle_area(8, 2), 8.0, msg="Expected 8.0, got {}".format(triangle_area(8, 2)))

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases that cover different scenarios to ensure the `triangle_area` function works as expected. The use of `assertAlmostEqual` allows for floating-point comparison, which is common in geometric calculations where exact values might not be perfectly representable due to precision limitations.