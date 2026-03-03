user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

Here is the comprehensive unittest test suite for the given Python function:

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
        self.assertEqual(greatest_common_divisor(15, 21), 3)
        self.assertEqual(greatest_common_divisor(48, 18), 6)

    def test_greatest_common_divisor_zero(self):
        with self.assertRaises(ZeroDivisionError):
            greatest_common_divisor(0, 5)
        with self.assertRaises(ZeroDivisionError):
            greatest_common_divisor(5, 0)

    def test_greatest_common_divisor_negative(self):
        self.assertEqual(greatest_common_divisor(-3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, -15), 5)
        self.assertEqual(greatest_common_divisor(-12, 15), 3)
        self.assertEqual(greatest_common_divisor(24, -30), 6)
        self.assertEqual(greatest_common_divisor(-7, 3), 1)
        self.assertEqual(greatest_common_divisor(10, -20), 10)
        self.assertEqual(greatest_common_divisor(-9, 12), 3)
        self.assertEqual(greatest_common_divisor(15, -21), 3)
        self.assertEqual(greatest_common_divisor(-48, 18), 6)

if __name__ == '__main__':
    unittest.main()


This test suite includes two test methods: `test_greatest_common_divisor` and `test_greatest_common_divisor_zero`. The `test_greatest_common_divisor` method tests the function with various inputs, including positive and negative numbers. The `test_greatest_common_divisor_zero` method tests the function with zero inputs, which should raise a `ZeroDivisionError`.