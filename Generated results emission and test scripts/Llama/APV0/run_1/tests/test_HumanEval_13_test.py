user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_13_code import greatest_common_divisor
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return aassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_13_code import greatest_common_divisor

class TestGreatestCommonDivisor(unittest.TestCase):

    def test_greatest_common_divisor(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)
        self.assertEqual(greatest_common_divisor(12, 15), 3)
        self.assertEqual(greatest_common_divisor(24, 30), 6)
        self.assertEqual(greatest_common_divisor(7, 3), 1)
        self.assertEqual(greatest_common_divisor(10, 20), 10)
        self.assertEqual(greatest_common_divisor(9, 12), 3)
        self.assertEqual(greatest_common_divisor(15, 20), 5)
        self.assertEqual(greatest_common_divisor(24, 36), 12)

if __name__ == '__main__':
    unittest.main()


This script includes 9 test cases to cover different scenarios. The `assertEqual` method is used to compare the output of the function with the expected result. If the output matches the expected result, the test case passes; otherwise, it fails.