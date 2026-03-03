user

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
    return outassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_89_code import encrypt

class TestEncrypt(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')
        self.assertEqual(encrypt('abcdefghijklmnopqrstuvwxyz'),'stuvwxyzabcde')
        self.assertEqual(encrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'XYZABCDEF')
        self.assertEqual(encrypt('1234567890'), '1234567890')
        self.assertEqual(encrypt('!@#$%^&*()'), '!@#$%^&*()')

    def test_encrypt_empty_string(self):
        self.assertEqual(encrypt(''), '')

    def test_encrypt_non_string(self):
        with self.assertRaises(TypeError):
            encrypt(123)

if __name__ == '__main__':
    unittest.main()


This script includes two test cases: `test_encrypt` and `test_encrypt_empty_string`. The `test_encrypt` test case checks the function with various inputs, including strings of letters, uppercase letters, numbers, and special characters. The `test_encrypt_empty_string` test case checks the function with an empty string. The `test_encrypt_non_string` test case checks the function with a non-string input, which should raise a TypeError.