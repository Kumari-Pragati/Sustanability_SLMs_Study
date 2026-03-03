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

 Here is a simple unittest test script for the `triangle_area` function:


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


This test script includes a test case for the `TestTriangleArea` class, which tests the `triangle_area` function with various inputs. If the function works correctly, all the assertions will pass, and the test will pass as well. If any assertion fails, the test will fail, and the error message will indicate the failed assertion and the expected and actual results.

You can run this test script directly by saving it as a .py file and running it using the command `python filename.py` in your terminal or command prompt.