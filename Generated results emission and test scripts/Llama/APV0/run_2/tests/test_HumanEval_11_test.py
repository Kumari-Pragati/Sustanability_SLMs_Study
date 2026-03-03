user

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

    return ''.join(xor(x, y) for x, y in zip(a, b))assistant

Here is the unittest test script for the `string_xor` function:

import unittest
from HumanEval_11_code import string_xor

class TestStringXOR(unittest.TestCase):
    def test_empty_strings(self):
        self.assertEqual(string_xor("", ""), "")

    def test_single_character_strings(self):
        self.assertEqual(string_xor("1", "0"), "1")
        self.assertEqual(string_xor("0", "1"), "1")
        self.assertEqual(string_xor("1", "1"), "0")
        self.assertEqual(string_xor("0", "0"), "0")

    def test_multiple_character_strings(self):
        self.assertEqual(string_xor("010", "110"), "100")
        self.assertEqual(string_xor("101", "010"), "111")
        self.assertEqual(string_xor("111", "111"), "000")
        self.assertEqual(string_xor("000", "000"), "000")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            string_xor("hello", "world")
        with self.assertRaises(TypeError):
            string_xor("101", "abc")

if __name__ == '__main__':
    unittest.main()

This script defines a `TestStringXOR` class with four test methods:

1. `test_empty_strings`: Tests that the function returns an empty string when both input strings are empty.
2. `test_single_character_strings`: Tests that the function returns the correct result for single-character input strings.
3. `test_multiple_character_strings`: Tests that the function returns the correct result for multiple-character input strings.
4. `test_invalid_input`: Tests that the function raises a `TypeError` when given invalid input (e.g., non-binary strings).

You can run this script directly to execute the tests.