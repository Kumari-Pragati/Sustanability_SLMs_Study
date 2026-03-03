You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

    def test_decimal_to_binary_positive_numbers(self):
        self.assertEqual(decimal_to_binary(15), "db1111db")
        self.assertEqual(decimal_to_binary(32), "db100000db")

    def test_decimal_to_binary_zero(self):
        self.assertEqual(decimal_to_binary(0), "db0db")

    def test_decimal_to_binary_negative_numbers(self):
        with self.assertRaises(ValueError):
            decimal_to_binary(-1)

    def test_decimal_to_binary_large_numbers(self):
        self.assertEqual(decimal_to_binary(10000000000000000), "db111001011000010000000000000000db")

    def test_decimal_to_binary_edge_case(self):
        self.assertEqual(decimal_to_binary(255), "db11111111db")

if __name__ == '__main__':
    unittest.main()