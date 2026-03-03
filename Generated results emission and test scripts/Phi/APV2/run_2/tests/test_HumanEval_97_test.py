You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

    return abs(a % 10) * abs(b % 10)

 import unittest
from HumanEval_97_code import multiply

class TestMultiplyFunction(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(148, 412), 16)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(19, -15), 20)

    def test_multiply_zero(self):
        self.assertEqual(multiply(2020, 1851), 0)

    def test_multiply_large_numbers(self):
        self.assertEqual(multiply(1999, 2001), 9999)

    def test_multiply_single_digit_numbers(self):
        self.assertEqual(multiply(1, 1), 1)
        self.assertEqual(multiply(9, 9), 81)

    def test_multiply_unit_digit_one(self):
        self.assertEqual(multiply(10, 10), 0)
        self.assertEqual(multiply(11, 11), 1)

    def test_multiply_unit_digit_two(self):
        self.assertEqual(multiply(22, 22), 4)
        self.assertEqual(multiply(23, 23), 9)

    def test_multiply_unit_digit_three(self):
        self.assertEqual(multiply(33, 33), 9)
        self.assertEqual(multiply(34, 34), 16)

    def test_multiply_unit_digit_four(self):
        self.assertEqual(multiply(44, 44), 16)
        self.assertEqual(multiply(45, 45), 25)

    def test_multiply_unit_digit_five(self):
        self.assertEqual(multiply(55, 55), 25)
        self.assertEqual(multiply(56, 56), 36)

    def test_multiply_unit_digit_six(self):
        self.assertEqual(multiply(66, 66), 36)
        self.assertEqual(multiply(67, 67), 49)

    def test_multiply_unit_digit_seven(self):
        self.assertEqual(multiply(77, 77), 49)
        self.assertEqual(multiply(78, 78), 64)

    def test_multiply_unit_digit_eight(self):
        self.assertEqual(multiply(88, 88), 64)
        self.assertEqual(multiply(89, 89), 81)

    def test_multiply_unit_digit_nine(self):
        self.assertEqual(multiply(99, 99), 81)
        self.assertEqual(multiply(100, 100), 0)

if __name__ == '__main__':
    unittest.main()