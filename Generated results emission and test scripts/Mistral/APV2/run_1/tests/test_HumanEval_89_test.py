You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the `encrypt` function:


import unittest
from HumanEval_89_code import encrypt

class TestEncrypt(unittest.TestCase):

    def test_encrypt_single_char(self):
        self.assertEqual(encrypt('a'), 'd')
        self.assertEqual(encrypt('z'), 'c')

    def test_encrypt_multiple_chars(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')

    def test_encrypt_special_chars(self):
        self.assertEqual(encrypt('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), '!@#$%^&*()_+-=[]{}|;:'\'<>,.?/')
        self.assertEqual(encrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'DEFGHIJKLMNOPQRSTUVWXYZABC')
        self.assertEqual(encrypt('1234567890'), '3456789012')

    def test_encrypt_empty_string(self):
        self.assertEqual(encrypt(''), '')

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases:

1. `test_encrypt_single_char` checks the encryption of single characters.
2. `test_encrypt_multiple_chars` checks the encryption of multiple characters.
3. `test_encrypt_special_chars` checks the encryption of special characters, uppercase letters, numbers, and an empty string.
4. `test_encrypt_empty_string` checks the behavior of the function when an empty string is passed.