You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 
import unittest
from HumanEval_89_code import encrypt

class TestEncryptFunction(unittest.TestCase):

    def test_encrypt_single_characters(self):
        self.assertEqual(encrypt('h'), 'j')
        self.assertEqual(encrypt('a'), 'c')
        self.assertEqual(encrypt('z'), 'b')

    def test_encrypt_two_characters(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('as'), 'cx')
        self.assertEqual(encrypt('gh'), 'jk')
        self.assertEqual(encrypt('jk'), 'nl')

    def test_encrypt_three_characters(self):
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')
        self.assertEqual(encrypt('xyz'), 'b{')

    def test_encrypt_non_alphabetic_characters(self):
        self.assertEqual(encrypt('123'), '123')
        self.assertEqual(encrypt('!@#'), '!@#')
        self.assertEqual(encrypt('$%^'), '$%^')

    def test_encrypt_empty_string(self):
        self.assertEqual(encrypt(''), '')

    def test_encrypt_whitespace(self):
        self.assertEqual(encrypt(' '), ' ')

    def test_encrypt_case_sensitive(self):
        self.assertEqual(encrypt('Hi'), 'Jk')
        self.assertEqual(encrypt('HI'), 'JK')

if __name__ == '__main__':
    unittest.main()


This test suite covers various cases for the `encrypt` function, including single characters, two characters, three characters, non-alphabetic characters, empty strings, whitespace, and case sensitivity. Each test case checks if the output of the `encrypt` function matches the expected encrypted string.