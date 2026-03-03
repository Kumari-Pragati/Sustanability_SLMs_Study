You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_positive_values(self):
        self.assertAlmostEqual(triangle_area(5, 3), 7.5)
        self.assertAlmostEqual(triangle_area(10, 2), 10.0)
        self.assertAlmostEqual(triangle_area(7, 4), 14.0)

    def test_zero_height(self):
        self.assertEqual(triangle_area(5, 0), 0)

    def test_zero_side(self):
        self.assertEqual(triangle_area(0, 3), 0)

    def test_negative_values(self):
        self.assertEqual(triangle_area(-5, 3), -7.5)
        self.assertEqual(triangle_area(10, -2), -10.0)
        self.assertEqual(triangle_area(-7, -4), 14.0)

    def test_non_numeric_values(self):
        with self.assertRaises(TypeError):
            triangle_area("5", 3)
        with self.assertRaises(TypeError):
            triangle_area(5, "3")
        with self.assertRaises(TypeError):
            triangle_area("5", "3")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive, zero, and negative values for both the side length and height. It also includes a test for non-numeric values. The `assertAlmostEqual` method is used for floating point comparisons, and the `assertRaises` method is used to check that a `TypeError` is raised when non-numeric values are passed to the function.