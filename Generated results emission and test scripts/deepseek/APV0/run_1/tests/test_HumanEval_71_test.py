You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_71_code import triangle_area

class TestTriangleArea(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(triangle_area(3, 4, 5), 6.00)
        self.assertEqual(triangle_area(5, 12, 13), 30.00)
        self.assertEqual(triangle_area(8, 15, 17), 60.31)

    def test_invalid_triangle(self):
        self.assertEqual(triangle_area(1, 2, 10), -1)
        self.assertEqual(triangle_area(10, 10, 20), -1)
        self.assertEqual(triangle_area(1, 1, 1), -1)

    def test_non_positive_sides(self):
        self.assertEqual(triangle_area(0, 1, 1), -1)
        self.assertEqual(triangle_area(-1, 2, 3), -1)
        self.assertEqual(triangle_area(1, -2, 3), -1)
        self.assertEqual(triangle_area(1, 2, -3), -1)

    def test_non_numeric_input(self):
        self.assertEqual(triangle_area('a', 2, 3), -1)
        self.assertEqual(triangle_area(1, 'b', 3), -1)
        self.assertEqual(triangle_area(1, 2, 'c'), -1)

if __name__ == '__main__':
    unittest.main()


This script includes tests for valid triangles, invalid triangles, non-positive side lengths, and non-numeric input. It checks that the function returns the correct output for each of these cases.