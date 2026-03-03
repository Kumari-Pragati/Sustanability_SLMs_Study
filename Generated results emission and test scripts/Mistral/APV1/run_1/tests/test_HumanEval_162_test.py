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

 Here is a comprehensive unittest test suite for the given Python function `string_to_md5`:


import unittest
from HumanEval_162_code import string_to_md5

class TestStringToMD5(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(string_to_md5(''), None)

    def test_single_character_string(self):
        self.assertEqual(string_to_md5('a'), '0cc175b9c0f1b6a831c399e269772661')
        self.assertEqual(string_to_md5('A'), '0cc175b9c0f1b6a831c399e269772661')
        self.assertEqual(string_to_md5('z'), 'e10adc3949ba59abbe56e057f20f883e')

    def test_multiple_character_strings(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')
        self.assertEqual(string_to_md5('Python is awesome'), '900150983cd24fb0d6963f7d28e17f72')
        self.assertEqual(string_to_md5('Javascript is cool'), 'c3fcd3d76192e4007dfb496cca67e13b')

    def test_special_characters(self):
        self.assertEqual(string_to_md5('!@#$%^&*()_+-=[]{}|;:,.<>?'), '8c97e154ba79879255a257117fcc7129')
        self.assertEqual(string_to_md5('Hello, World!'), '098f6bcd4621d373cade4e832627b4f6')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for empty strings, single character strings, multiple character strings with spaces, and strings containing special characters. It uses the `assertEqual` method to compare the expected and actual outputs of the `string_to_md5` function.