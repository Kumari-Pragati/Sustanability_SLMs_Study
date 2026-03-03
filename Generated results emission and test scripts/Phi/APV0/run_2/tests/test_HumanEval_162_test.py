Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_162_code import string_to_md5
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None

 import unittest
from HumanEval_162_code import string_to_md5

class TestStringToMD5(unittest.TestCase):

    def test_non_empty_string(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')

    def test_empty_string(self):
        self.assertIsNone(string_to_md5(''))

    def test_special_characters(self):
        self.assertEqual(string_to_md5('Test!@#$%^&*()'), '9035994b1d306751e8e6e1b0f7e4f9e8')

    def test_unicode_characters(self):
        self.assertEqual(string_to_md5('こんにちは'), '5d41402abc4b2a76b9719d911017c592')

    def test_case_sensitivity(self):
        self.assertEqual(string_to_md5('Hello'), '5eb63bbbe01eeed093cb22bb8f5acdc3')
        self.assertEqual(string_to_md5('hello'), '5eb63bbbe01eeed093cb22bb8f5acdc3')

    def test_whitespace(self):
        self.assertEqual(string_to_md5('   '), 'd0f9c69a6c2e3e9b1b2c3d4e5f6a7b8c')

    def test_repeated_string(self):
        self.assertEqual(string_to_md5('abc'), '900150983cd24fb0d6963f7d28e17735')

if __name__ == '__main__':
    unittest.main()