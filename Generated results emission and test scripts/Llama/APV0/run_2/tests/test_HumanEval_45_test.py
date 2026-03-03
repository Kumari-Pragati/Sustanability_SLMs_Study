user

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
    return a * h / 2.0assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_triangle_area(self):
        # Test case 1: Positive values
        self.assertAlmostEqual(triangle_area(5, 3), 7.5)
        self.assertAlmostEqual(triangle_area(10, 6), 30.0)
        self.assertAlmostEqual(triangle_area(2, 1), 1.0)

        # Test case 2: Zero values
        self.assertAlmostEqual(triangle_area(0, 3), 0.0)
        self.assertAlmostEqual(triangle_area(5, 0), 0.0)
        self.assertAlmostEqual(triangle_area(0, 0), 0.0)

        # Test case 3: Negative values
        self.assertAlmostEqual(triangle_area(-5, 3), 7.5)
        self.assertAlmostEqual(triangle_area(5, -3), 7.5)
        self.assertAlmostEqual(triangle_area(-5, -3), 7.5)

        # Test case 4: Non-numeric values
        with self.assertRaises(TypeError):
            triangle_area('a', 3)
        with self.assertRaises(TypeError):
            triangle_area(5, 'b')
        with self.assertRaises(TypeError):
            triangle_area('a', 'b')

if __name__ == '__main__':
    unittest.main()


This script includes four test cases:

1. Test case 1: Positive values: This test case checks the function with positive values.
2. Test case 2: Zero values: This test case checks the function with zero values.
3. Test case 3: Negative values: This test case checks the function with negative values.
4. Test case 4: Non-numeric values: This test case checks the function with non-numeric values and verifies that it raises a TypeError.