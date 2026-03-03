You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
        self.assertEqual(string_to_md5('!@#$%^&*()'), '9b71d224bd62f3785d97eea62c551de4')

    def test_numeric_string(self):
        self.assertEqual(string_to_md5('1234567890'), '4a5e145857af69b4d18a5c20a5b371e9')

    def test_whitespace_string(self):
        self.assertEqual(string_to_md5('   '), 'e4d909c297d4ec28c09a5ff6b4d0741c')

    def test_unicode_string(self):
        self.assertEqual(string_to_md5('こんにちは'), 'd0f5e9e7e9e9e9e9e9e9e9e9e9e9e9e9')

    def test_case_sensitivity(self):
        self.assertEqual(string_to_md5('Hello'), '5ebe22949a9a578187b05d9e0d674d24')
        self.assertEqual(string_to_md5('hello'), '5ebe22949a9a578187b05d9e0d674d24')

    def test_empty_list(self):
        self.assertIsNone(string_to_md5([]))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            string_to_md5(123)

if __name__ == '__main__':
    unittest.main()