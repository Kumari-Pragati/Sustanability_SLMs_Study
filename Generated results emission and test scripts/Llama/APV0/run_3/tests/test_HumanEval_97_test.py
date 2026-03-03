user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_97_code import multiply
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.

    Examples:
    multiply(148, 412) ➞ 16
    multiply(19, 28) ➞ 72
    multiply(2020, 1851) ➞ 0
    multiply(14, -15) ➞ 20
    """

    return abs(a % 10) * abs(b % 10)assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_97_code import multiply

class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)
        self.assertEqual(multiply(14, -15), 20)
        self.assertEqual(multiply(-14, 15), 20)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(0, 1), 0)
        self.assertEqual(multiply(1, 0), 0)
        self.assertEqual(multiply(1, 1), 1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(-1, 1), 1)
        self.assertEqual(multiply(1, -1), 1)

if __name__ == '__main__':
    unittest.main()


This script includes a variety of test cases to ensure the function is working correctly. It tests the function with positive and negative numbers, as well as with zero. It also tests the function with different combinations of unit digits.