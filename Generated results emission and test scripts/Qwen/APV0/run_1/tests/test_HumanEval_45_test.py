system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return a * h / 2.0


assistant

import unittest

# Importing the function to be tested
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):

    def test_triangle_area(self):
        # Test case 1: Valid input (a=5, h=3)
        self.assertAlmostEqual(triangle_area(5, 3), 7.5)

        # Test case 2: Another valid input (a=6, h=4)
        self.assertAlmostEqual(triangle_area(6, 4), 12.0)

        # Test case 3: Invalid input (negative sides or zero height)
        try:
            triangle_area(-1, 3)
            self.fail("Expected ValueError")
        except ValueError:
            pass

        try:
            triangle_area(5, 0)
            self.fail("Expected ZeroDivisionError")
        except ZeroDivisionError:
            pass

        # Test case 4: Edge cases (a=0, h=0)
        self.assertEqual(triangle_area(0, 0), 0)

if __name__ == '__main__':
    unittest.main()


This script imports the `triangle_area` function and defines a class `TestTriangleArea` that inherits from `unittest.TestCase`. It contains several test methods to verify the correctness of the `triangle_area` function under different conditions. The `assertAlmostEqual` method is used to check if the output matches the expected value within a small tolerance, while the `try-except` blocks handle potential errors such as division by zero or negative inputs. Finally, the `unittest.main()` call runs all the tests when the script is executed directly.