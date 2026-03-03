system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else Noneassistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_162_code import string_to_md5

class TestStringToMd5(unittest.TestCase):

    def test_string_to_md5(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')
        self.assertIsNone(string_to_md5(''))
        self.assertIsNone(string_to_md5(None))
        self.assertIsNone(string_to_md5(12345))
        self.assertIsNone(string_to_md5([1, 2, 3]))
        self.assertIsNone(string_to_md5({'a': 1, 'b': 2}))

    def test_string_to_md5_non_ascii(self):
        self.assertEqual(string_to_md5('Hello world!'), '3e25960a79dbc69b674cd4ec67a72c62')
        self.assertEqual(string_to_md5('Hello world!@#'), '3e25960a79dbc69b674cd4ec67a72c62')

    def test_string_to_md5_empty_string(self):
        self.assertIsNone(string_to_md5(''))

    def test_string_to_md5_none(self):
        self.assertIsNone(string_to_md5(None))

    def test_string_to_md5_integer(self):
        self.assertIsNone(string_to_md5(12345))

    def test_string_to_md5_list(self):
        self.assertIsNone(string_to_md5([1, 2, 3]))

    def test_string_to_md5_dict(self):
        self.assertIsNone(string_to_md5({'a': 1, 'b': 2}))

if __name__ == '__main__':
    unittest.main()