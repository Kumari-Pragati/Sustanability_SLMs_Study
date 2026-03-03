You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_45_code import triangle_area

class TestTriangleArea(unittest.TestCase):
    def test_triangle_area(self):
        self.assertEqual(triangle_area(5, 3), 7.5)
        self.assertEqual(triangle_area(10, 2), 10.0)
        self.assertEqual(triangle_area(0, 5), 0)
        self.assertEqual(triangle_area(5, 0), 0)
        self.assertEqual(triangle_area(0, 0), 0)
        self.assertRaises(TypeError, triangle_area, "5", 3)
        self.assertRaises(TypeError, triangle_area, 5, "3")
        self.assertRaises(TypeError, triangle_area, "5", "3")

if __name__ == '__main__':
    unittest.main()


This script includes a test class `TestTriangleArea` that inherits from `unittest.TestCase`. Inside this class, there is a method `test_triangle_area` that tests the `triangle_area` function with various inputs. The `assertEqual` method is used to check if the output of the function matches the expected output. The `assertRaises` method is used to check if the function raises a `TypeError` when it is given inputs of the wrong type.

The script ends with `unittest.main()`, which runs all the tests when the script is run directly.

Please note that you need to have the `HumanEval_45_code` module and the `triangle_area` function in the same directory as this script, or you need to provide the correct path to the module.