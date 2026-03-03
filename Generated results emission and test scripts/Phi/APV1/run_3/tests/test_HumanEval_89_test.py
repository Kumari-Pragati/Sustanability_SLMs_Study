You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_89_code import encrypt

class TestEncryptFunction(unittest.TestCase):

    def test_encrypt_single_characters(self):
        self.assertEqual(encrypt('h'), 'j')
        self.assertEqual(encrypt('g'), 'i')
        self.assertEqual(encrypt('f'), 'h')
        self.assertEqual(encrypt('e'), 'g')
        self.assertEqual(encrypt('d'), 'f')
        self.assertEqual(encrypt('c'), 'e')
        self.assertEqual(encrypt('b'), 'd')
        self.assertEqual(encrypt('a'), 'c')

    def test_encrypt_two_characters(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')

    def test_encrypt_empty_string(self):
        self.assertEqual(encrypt(''), '')

    def test_encrypt_non_alphabetic_characters(self):
        self.assertEqual(encrypt('!@#'), '!@#')
        self.assertEqual(encrypt('1234'), '1234')
        self.assertEqual(encrypt('abc123'), 'cde123')

    def test_encrypt_uppercase_letters(self):
        self.assertEqual(encrypt('H'), 'J')
        self.assertEqual(encrypt('G'), 'I')
        self.assertEqual(encrypt('F'), 'H')
        self.assertEqual(encrypt('E'), 'G')
        self.assertEqual(encrypt('D'), 'F')
        self.assertEqual(encrypt('C'), 'E')
        self.assertEqual(encrypt('B'), 'D')
        self.assertEqual(encrypt('A'), 'C')

    def test_encrypt_mixed_case_letters(self):
        self.assertEqual(encrypt('Ha'), 'Jc')
        self.assertEqual(encrypt('AbC'), 'Edf')
        self.assertEqual(encrypt('XYZ'), 'ZAB')

if __name__ == '__main__':
    unittest.main()