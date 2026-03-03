system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
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

    return ''.join(xor(x, y) for x, y in zip(a, b))assistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_11_code import string_xor

class TestStringXOR(unittest.TestCase):

    def test_string_xor(self):
        self.assertEqual(string_xor('010', '110'), '100')
        self.assertEqual(string_xor('111', '000'), '111')
        self.assertEqual(string_xor('101', '010'), '111')
        self.assertEqual(string_xor('000', '111'), '011')
        self.assertEqual(string_xor('1010', '1010'), '0')
        self.assertEqual(string_xor('1111', '0000'), '1111')
        self.assertEqual(string_xor('101010', '101010'), '0')
        self.assertEqual(string_xor('111111', '000000'), '111111')

    def test_string_xor_empty(self):
        self.assertEqual(string_xor('', ''), '')
        self.assertEqual(string_xor('1', ''), '')
        self.assertEqual(string_xor('', '1'), '')
        self.assertEqual(string_xor('1', '1'), '')
        self.assertEqual(string_xor('0', '0'), '')

    def test_string_xor_length_mismatch(self):
        with self.assertRaises(IndexError):
            string_xor('1010', '10101')
        with self.assertRaises(IndexError):
            string_xor('10101', '1010')

if __name__ == '__main__':
    unittest.main()