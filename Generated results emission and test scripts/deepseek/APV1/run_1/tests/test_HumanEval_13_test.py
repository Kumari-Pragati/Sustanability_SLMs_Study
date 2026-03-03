You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


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
        self.assertEqual(greatest_common_divisor(-3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, -15), 5)

    def test_zero(self):
        self.assertEqual(greatest_common_divisor(0, 5), 5)
        self.assertEqual(greatest_common_divisor(25, 0), 25)
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_single_number(self):
        self.assertEqual(greatest_common_divisor(5, 0), 5)
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_equal_numbers(self):
        self.assertEqual(greatest_common_divisor(5, 5), 5)
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_non_integer_numbers(self):
        with self.assertRaises(TypeError):
            greatest_common_divisor(3.5, 5)
        with self.assertRaises(TypeError):
            greatest_common_divisor(3, 5.5)
        with self.assertRaises(TypeError):
            greatest_common_divisor(3.5, 5.5)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive numbers, negative numbers, mixed positive and negative numbers, zero, single number, equal numbers, and non-integer numbers. It uses the `unittest` module's `TestCase` class to create test cases and the `assertEqual` method to check if the function's output matches the expected result. The `assertRaises` method is used to check if the function raises a `TypeError` when it's given non-integer numbers.