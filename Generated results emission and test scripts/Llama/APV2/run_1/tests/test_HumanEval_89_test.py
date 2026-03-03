system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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
    return outassistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_89_code import encrypt

class TestEncrypt(unittest.TestCase):

    def test_encrypt_hi(self):
        self.assertEqual(encrypt('hi'), 'lm')

    def test_encrypt_asdfghjkl(self):
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')

    def test_encrypt_gf(self):
        self.assertEqual(encrypt('gf'), 'kj')

    def test_encrypt_et(self):
        self.assertEqual(encrypt('et'), 'ix')

    def test_encrypt_all_lowercase(self):
        self.assertEqual(encrypt('abcdefghijklmnopqrstuvwxyz'), 'nopqrstuvwxyzabc')

    def test_encrypt_all_uppercase(self):
        self.assertEqual(encrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'wxyzabcdefg')

    def test_encrypt_mixed_case(self):
        self.assertEqual(encrypt('AbcDeFgHiJkLmNoPqRsTuVwXyZ'), 'wxyzabcdefg')

    def test_encrypt_non_alphabetic_characters(self):
        self.assertEqual(encrypt('hello123'), 'khoor456')

    def test_encrypt_empty_string(self):
        self.assertEqual(encrypt(''), '')

if __name__ == '__main__':
    unittest.main()