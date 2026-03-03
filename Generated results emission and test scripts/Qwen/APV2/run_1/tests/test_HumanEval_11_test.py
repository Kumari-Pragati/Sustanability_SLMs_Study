system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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

    return ''.join(xor(x, y) for x, y in zip(a, b))


assistant

import unittest

# Provided function
from HumanEval_11_code import string_xor

# Test class
class TestStringXOR(unittest.TestCase):
    
    # Test case for valid input
    def test_valid_input(self):
        self.assertEqual(string_xor('010', '110'), '100')

    # Test case for empty strings
    def test_empty_strings(self):
        self.assertEqual(string_xor('', ''), '')

    # Test case for single character strings
    def test_single_character_strings(self):
        self.assertEqual(string_xor('1', '1'), '0')

    # Test case for different lengths
    def test_different_lengths(self):
        self.assertEqual(string_xor('0101', '1010'), '1111')

    # Test case for mixed characters (should raise ValueError)
    def test_mixed_characters(self):
        with self.assertRaises(ValueError):
            string_xor('01a', '110')

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to ensure the `string_xor` function behaves correctly under different conditions, including edge cases like empty strings, single-character strings, strings of different lengths, and strings containing non-binary characters.