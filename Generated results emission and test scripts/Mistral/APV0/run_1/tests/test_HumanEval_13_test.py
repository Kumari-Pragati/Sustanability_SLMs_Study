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
    return a

 Here is a unittest test script for the `greatest_common_divisor` function:


import unittest
from HumanEval_13_code import greatest_common_divisor

class TestGCD(unittest.TestCase):

    def test_gcd_basic(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)
        self.assertEqual(greatest_common_divisor(20, 16), 4)
        self.assertEqual(greatest_common_divisor(48, 18), 6)
        self.assertEqual(greatest_common_divisor(12, 36), 12)

    def test_gcd_negative(self):
        self.assertEqual(greatest_common_divisor(-3, 5), 1)
        self.assertEqual(greatest_common_divisor(-25, -15), 5)
        self.assertEqual(greatest_common_divisor(-20, -16), 4)
        self.assertEqual(greatest_common_divisor(-48, -18), 6)
        self.assertEqual(greatest_common_divisor(-12, -36), 12)

    def test_gcd_zero(self):
        self.assertEqual(greatest_common_divisor(0, 5), 0)
        self.assertEqual(greatest_common_divisor(5, 0), 0)
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_gcd_large(self):
        self.assertEqual(greatest_common_divisor(1000000007, 999999997), 1)
        self.assertEqual(greatest_common_divisor(999999997, 1000000007), 1)

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases for different inputs, including positive, negative, zero, and large numbers. It also tests the function's behavior when the input numbers are swapped.