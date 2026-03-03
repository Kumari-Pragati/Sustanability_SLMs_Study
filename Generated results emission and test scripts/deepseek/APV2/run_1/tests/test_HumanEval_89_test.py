You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_89_code import encrypt
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """

    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c) + 4) % 26]
        else:
            out += c
    return out


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_89_code import encrypt

class TestEncrypt(unittest.TestCase):

    def test_lowercase_letters(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')

    def test_uppercase_letters(self):
        self.assertEqual(encrypt('HI'), 'LM')
        self.assertEqual(encrypt('ASDFGHJKL'), 'EWHJKLNOP')
        self.assertEqual(encrypt('GF'), 'KJ')
        self.assertEqual(encrypt('ET'), 'IX')

    def test_special_characters(self):
        self.assertEqual(encrypt('!@#$%^&*()'), '!@#$%^&*()')
        self.assertEqual(encrypt('1234567890'), '1234567890')
        self.assertEqual(encrypt(' '), ' ')

    def test_empty_string(self):
        self.assertEqual(encrypt(''), '')

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases:

1. `test_lowercase_letters`: Tests the function with lowercase letters.
2. `test_uppercase_letters`: Tests the function with uppercase letters.
3. `test_special_characters`: Tests the function with special characters.
4. `test_empty_string`: Tests the function with an empty string.

Each test case checks if the function's output matches the expected result. If the function's output does not match the expected result, the test case will fail.

Please note that the function `encrypt` is assumed to be in a file named `HumanEval_89_code.py` in the same directory as the test file. If the function is in a different file, you will need to adjust the import statement accordingly.