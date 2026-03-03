You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_79_code import decimal_to_binary

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def decimal_to_binary(decimal):
    """You will be given a number in decimal form and your task is to convert it to
    binary format. The function should return a string, with each character representing a binary
    number. Each character in the string will be '0' or '1'.

    There will be an extra couple of characters 'db' at the beginning and at the end of the string.
    The extra characters are there to help with the format.

    Examples:
        decimal_to_binary(15)   # returns "db1111db"
        decimal_to_binary(32)   # returns "db100000db"
    """

    return "db" + bin(decimal)[2:] + "db"

 import unittest
from HumanEval_79_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_decimal_to_binary_with_zero(self):
        self.assertEqual(decimal_to_binary(0), "db0db")

    def test_decimal_to_binary_with_one(self):
        self.assertEqual(decimal_to_binary(1), "db1db")

    def test_decimal_to_binary_with_small_number(self):
        self.assertEqual(decimal_to_binary(5), "db101db")

    def test_decimal_to_binary_with_large_number(self):
        self.assertEqual(decimal_to_binary(15), "db1111db")

    def test_decimal_to_binary_with_power_of_two(self):
        self.assertEqual(decimal_to_binary(32), "db100000db")

    def test_decimal_to_binary_with_negative_number(self):
        with self.assertRaises(ValueError):
            decimal_to_binary(-1)

    def test_decimal_to_binary_with_non_integer(self):
        with self.assertRaises(TypeError):
            decimal_to_binary(1.5)

if __name__ == '__main__':
    unittest.main()