You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return a

 Here is a complete unittest test suite for the `greatest_common_divisor` function:


import unittest
from HumanEval_13_code import greatest_common_divisor

class TestGCD(unittest.TestCase):

    def test_gcd_basic(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)
        self.assertEqual(greatest_common_divisor(48, 18), 6)
        self.assertEqual(greatest_common_divisor(12, 36), 12)
        self.assertEqual(greatest_common_divisor(10, 20), 10)

    def test_gcd_negative(self):
        self.assertEqual(greatest_common_divisor(-3, 5), 1)
        self.assertEqual(greatest_common_divisor(-25, -15), 5)
        self.assertEqual(greatest_common_divisor(-48, -18), 6)
        self.assertEqual(greatest_common_divisor(-12, -36), 12)
        self.assertEqual(greatest_common_divisor(-10, -20), 10)

    def test_gcd_zero(self):
        self.assertEqual(greatest_common_divisor(0, 5), 0)
        self.assertEqual(greatest_common_divisor(5, 0), 0)
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_gcd_large_numbers(self):
        self.assertEqual(greatest_common_divisor(123456789, 987654321), 72576543)
        self.assertEqual(greatest_common_divisor(1234567890, 9876543210), 10)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases for different scenarios such as basic cases, negative numbers, zero, and large numbers. It uses the `assertEqual` method to compare the expected and actual results.