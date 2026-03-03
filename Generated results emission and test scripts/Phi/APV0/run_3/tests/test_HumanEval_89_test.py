Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
        self.assertEqual(encrypt('i'), 'k')
        self.assertEqual(encrypt('a'), 'c')
        self.assertEqual(encrypt('b'), 'd')
        # Add more tests for other single characters

    def test_encrypt_two_characters(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('as'), 'cx')
        self.assertEqual(encrypt('df'), 'gh')
        self.assertEqual(encrypt('gh'), 'jk')
        # Add more tests for other two-character combinations

    def test_encrypt_three_characters(self):
        self.assertEqual(encrypt('abc'), 'def')
        self.assertEqual(encrypt('def'), 'ghi')
        self.assertEqual(encrypt('ghi'), 'jkl')
        # Add more tests for other three-character combinations

    def test_encrypt_special_characters(self):
        self.assertEqual(encrypt(' '), ' ')
        self.assertEqual(encrypt('!'), '!')
        self.assertEqual(encrypt('$'), '$')
        # Add more tests for other special characters

    def test_encrypt_uppercase_letters(self):
        self.assertEqual(encrypt('H'), 'J')
        self.assertEqual(encrypt('I'), 'K')
        self.assertEqual(encrypt('A'), 'C')
        self.assertEqual(encrypt('B'), 'D')
        # Add more tests for other uppercase letters

    def test_encrypt_non_alphabetic_characters(self):
        self.assertEqual(encrypt('1'), '1')
        self.assertEqual(encrypt('@'), '@')
        self.assertEqual(encrypt('#'), '#')
        # Add more tests for other non-alphabetic characters

    def test_encrypt_empty_string(self):
        self.assertEqual(encrypt(''), '')

    def test_encrypt_long_string(self):
        self.assertEqual(encrypt('abcdefghijklmnopqrstuvwxyz'), 'defghijklmnopqrstuvwxyz')
        self.assertEqual(encrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'CDEFGHIJKLMNOPQRSTUVWXYZ')
        # Add more tests for longer strings

if __name__ == '__main__':
    unittest.main()