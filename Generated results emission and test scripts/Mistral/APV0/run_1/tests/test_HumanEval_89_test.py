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

 Here is a unittest test script for the provided `encrypt` function:


import unittest
from HumanEval_89_code import encrypt

class TestEncryptFunction(unittest.TestCase):

    def test_encrypt_single_char(self):
        self.assertEqual(encrypt('a'), 'd')
        self.assertEqual(encrypt('z'), 'c')
        self.assertEqual(encrypt('x'), 'w')

    def test_encrypt_multiple_chars(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')
        self.assertEqual(encrypt('abcdefghijklmnopqrstuvwxyz'), 'ehgfijklmnopqrstuvwxyzabcd')

    def test_encrypt_special_chars(self):
        self.assertEqual(encrypt('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), '!@#$%^&*()_+-=[]{}|;:'\'<>,.?/')
        self.assertEqual(encrypt('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.assertEqual(encrypt('1234567890'), '1234567890')

if __name__ == '__main__':
    unittest.main()


This test script includes three test cases:

1. `test_encrypt_single_char` tests the function with single character strings.
2. `test_encrypt_multiple_chars` tests the function with multiple character strings.
3. `test_encrypt_special_chars` tests the function with special characters, uppercase letters, and numbers.

You can run the test script by saving it as a .py file and running it using the command `python filename.py`. If all tests pass, the function is working correctly. If any tests fail, you'll see an error message indicating which test failed and the expected and actual results.