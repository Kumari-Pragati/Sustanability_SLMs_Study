You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
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

 Here is the complete unittest test suite for the `decimal_to_binary` function:


import unittest
from HumanEval_79_code import decimal_to_binary

class TestDecimalToBinary(unittest.TestCase):

    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(1), "db000001db")
        self.assertEqual(decimal_to_binary(2), "db000010db")
        self.assertEqual(decimal_to_binary(3), "db000011db")
        self.assertEqual(decimal_to_binary(4), "db000100db")
        self.assertEqual(decimal_to_binary(5), "db000101db")
        self.assertEqual(decimal_to_binary(6), "db000110db")
        self.assertEqual(decimal_to_binary(7), "db000111db")
        self.assertEqual(decimal_to_binary(8), "db001000db")
        self.assertEqual(decimal_to_binary(9), "db001001db")
        self.assertEqual(decimal_to_binary(10), "db001010db")
        self.assertEqual(decimal_to_binary(11), "db001011db")
        self.assertEqual(decimal_to_binary(12), "db001100db")
        self.assertEqual(decimal_to_binary(13), "db001101db")
        self.assertEqual(decimal_to_binary(14), "db001110db")
        self.assertEqual(decimal_to_binary(15), "db001111db")
        self.assertEqual(decimal_to_binary(16), "db010000db")
        self.assertEqual(decimal_to_binary(31), "db011111db")
        self.assertEqual(decimal_to_binary(32), "db100000db")
        self.assertEqual(decimal_to_binary(127), "db1111111db")
        self.assertEqual(decimal_to_binary(128), "db1000000db")
        self.assertEqual(decimal_to_binary(255), "db11111111db")
        self.assertEqual(decimal_to_binary(256), "db10000000db")
        self.assertEqual(decimal_to_binary(511), "db111111111db")
        self.assertEqual(decimal_to_binary(512), "db100000000db")
        self.assertEqual(decimal_to_binary(1023), "db1111111111db")
        self.assertEqual(decimal_to_binary(1024), "db1000000000db")
        self.assertEqual(decimal_to_binary(2047), "db11111111111db")
        self.assertEqual(decimal_to_binary(2048), "db10000000000db")
        self.assertEqual(decimal_to_binary(4095), "db111111111111db")
        self.assertEqual(decimal_to_binary(4096), "db100000000000db")
        self.assertEqual(decimal_to_binary(8191), "db1111111111111db")
        self.assertEqual(decimal_to_binary(8192), "db1000000000000db")
        self.assertEqual(decimal_to_binary(16383), "db11111111111111db")
        self.assertEqual(decimal_to_binary(1