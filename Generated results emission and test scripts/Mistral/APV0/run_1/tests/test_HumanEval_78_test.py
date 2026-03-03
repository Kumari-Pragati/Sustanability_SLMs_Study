Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_78_code import hex_key
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def hex_key(num):
    """You have been tasked to write a function that receives 
    a hexadecimal number as a string and counts the number of hexadecimal 
    digits that are primes (prime number, or a prime, is a natural number 
    greater than 1 that is not a product of two smaller natural numbers).
    Hexadecimal digits are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F.
    Prime numbers are 2, 3, 5, 7, 11, 13, 17,...
    So you have to determine a number of the following digits: 2, 3, 5, 7, 
    B (=decimal 11), D (=decimal 13).
    Note: you may assume the input is always correct or empty string, 
    and symbols A,B,C,D,E,F are always uppercase.
    Examples:
        For num = "AB" the output should be 1.
        For num = "1077E" the output should be 2.
        For num = "ABED1A33" the output should be 4.
        For num = "123456789ABCDEF0" the output should be 6.
        For num = "2020" the output should be 2.
    """

    primes = ('2', '3', '5', '7', 'B', 'D')
    total = 0
    for i in range(len(num)):
        if num[i] in primes:
            total += 1
    return total

 Here is a unittest test script for the `hex_key` function:


import unittest
from HumanEval_78_code import hex_key

class TestHexKey(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(hex_key(""), 0)

    def test_single_digit(self):
        self.assertEqual(hex_key("2"), 1)
        self.assertEqual(hex_key("A"), 1)
        self.assertEqual(hex_key("F"), 1)
        self.assertEqual(hex_key("0"), 0)
        self.assertEqual(hex_key("9"), 0)

    def test_multiple_digits(self):
        self.assertEqual(hex_key("AB"), 1)
        self.assertEqual(hex_key("1077E"), 2)
        self.assertEqual(hex_key("ABED1A33"), 4)
        self.assertEqual(hex_key("123456789ABCDEF0"), 6)
        self.assertEqual(hex_key("2020"), 2)

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover the edge cases and common cases of the `hex_key` function. It tests the function with an empty string, single digits, and multiple digits containing prime numbers. The test cases are organized in a class called `TestHexKey`, and the test suite is run using `unittest.main()`.