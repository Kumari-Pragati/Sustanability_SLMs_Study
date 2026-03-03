Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

    def test_string_xor_same_length(self):
        self.assertEqual(string_xor('010', '110'), '100')

    def test_string_xor_different_lengths(self):
        self.assertEqual(string_xor('0101', '110'), '1011')

    def test_string_xor_empty_strings(self):
        self.assertEqual(string_xor('', '110'), '110')
        self.assertEqual(string_xor('010', ''), '010')

    def test_string_xor_all_zeros(self):
        self.assertEqual(string_xor('000', '000'), '000')

    def test_string_xor_all_ones(self):
        self.assertEqual(string_xor('111', '111'), '000')

    def test_string_xor_mixed_zeros_ones(self):
        self.assertEqual(string_xor('010101', '110011'), '101100')

    def test_string_xor_long_strings(self):
        self.assertEqual(string_xor('0101010101', '1100110011'), '1001100110')

if __name__ == '__main__':
    unittest.main()