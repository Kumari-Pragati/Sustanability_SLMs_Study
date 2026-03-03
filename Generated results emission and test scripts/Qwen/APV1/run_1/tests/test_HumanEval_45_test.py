system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_triangle_area(self):
        self.assertAlmostEqual(triangle_area(5, 3), 7.5, places=2)

    def test_zero_side_length(self):
        with self.assertRaises(ValueError):
            triangle_area(0, 3)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            triangle_area(5, -3)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            triangle_area('a', 3)

if __name__ == '__main__':
    unittest.main()


This code snippet creates a comprehensive unittest test suite for the `triangle_area` function. It includes tests for positive cases (valid inputs), edge cases (side length of zero or negative height), and invalid types of input. The use of `assertAlmostEqual` ensures that floating-point comparisons are accurate within a specified number of decimal places.