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
    return a

 import unittest
from HumanEval_13_code import greatest_common_divisor

class TestGreatestCommonDivisor(unittest.TestCase):

    def test_greatest_common_divisor_with_positive_integers(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)
        self.assertEqual(greatest_common_divisor(100, 20), 20)
        self.assertEqual(greatest_common_divisor(0, 5), 5)
        self.assertEqual(greatest_common_divisor(5, 0), 5)

    def test_greatest_common_divisor_with_negative_integers(self):
        self.assertEqual(greatest_common_divisor(-3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, -15), 5)
        self.assertEqual(greatest_common_divisor(-100, 20), 20)
        self.assertEqual(greatest_common_divisor(5, -0), 5)
        self.assertEqual(greatest_common_divisor(-5, 0), 5)

    def test_greatest_common_divisor_with_zero(self):
        self.assertEqual(greatest_common_divisor(0, 5), 5)
        self.assertEqual(greatest_common_divisor(5, 0), 5)

    def test_greatest_common_divisor_with_one(self):
        self.assertEqual(greatest_common_divisor(1, 5), 1)
        self.assertEqual(greatest_common_divisor(5, 1), 1)

    def test_greatest_common_divisor_with_same_numbers(self):
        self.assertEqual(greatest_common_divisor(10, 10), 10)
        self.assertEqual(greatest_common_divisor(0, 0), 0)

if __name__ == '__main__':
    unittest.main()