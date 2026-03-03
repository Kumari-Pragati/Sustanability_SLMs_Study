You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_13_code import greatest_common_divisor

class TestGreatestCommonDivisor(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(-3, -5), 1)
        self.assertEqual(greatest_common_divisor(-25, -15), 5)

    def test_mixed_positive_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(3, -5), 1)
        self.assertEqual(greatest_common_divisor(-25, 15), 5)

    def test_zero(self):
        self.assertEqual(greatest_common_divisor(0, 5), 5)
        self.assertEqual(greatest_common_divisor(25, 0), 25)

    def test_same_numbers(self):
        self.assertEqual(greatest_common_divisor(5, 5), 5)
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            greatest_common_divisor(3, "5")
        with self.assertRaises(TypeError):
            greatest_common_divisor("25", 15)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive numbers, negative numbers, mixed positive and negative numbers, zero, same numbers, and type error.