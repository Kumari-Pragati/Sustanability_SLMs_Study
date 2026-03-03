You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_11_code import string_xor
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i: str, j: str) -> str:
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))

 
import unittest
from HumanEval_11_code import string_xor

class TestStringXor(unittest.TestCase):

    def test_string_xor_equal_length(self):
        self.assertEqual(string_xor('010', '110'), '100')

    def test_string_xor_different_length(self):
        self.assertRaises(ValueError, string_xor, '010', '11')

    def test_string_xor_empty_strings(self):
        self.assertEqual(string_xor('', '110'), '110')
        self.assertEqual(string_xor('010', ''), '010')

    def test_string_xor_all_zeros(self):
        self.assertEqual(string_xor('000', '000'), '000')

    def test_string_xor_all_ones(self):
        self.assertEqual(string_xor('111', '111'), '000')

    def test_string_xor_mixed_zeros_ones(self):
        self.assertEqual(string_xor('0101', '1100'), '1011')

    def test_string_xor_long_strings(self):
        self.assertEqual(string_xor('0101010101', '1100110011'), '1001100110')

    def test_string_xor_non_binary_characters(self):
        with self.assertRaises(ValueError):
            string_xor('010a', '1100')

if __name__ == '__main__':
    unittest.main()


This test suite covers various cases for the `string_xor` function, including:

- Equal length strings
- Different length strings (should raise a `ValueError`)
- Empty strings
- Strings with all zeros
- Strings with all ones
- Mixed strings
- Long strings
- Non-binary characters (should raise a `ValueError`)

The `ValueError` is assumed to be raised by the `string_xor` function when the input strings contain characters other than '0' or '1'. If the `string_xor` function does not raise a `ValueError` for non-binary characters, the test case for non-binary characters should be adjusted accordingly.