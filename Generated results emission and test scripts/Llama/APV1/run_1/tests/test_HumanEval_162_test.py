user

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
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else Noneassistant

Here is the comprehensive unittest test suite for the given Python function:

Python
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

    def test_string_to_md5_empty_string(self):
        self.assertIsNone(string_to_md5(''))

    def test_string_to_md5_none(self):
        self.assertIsNone(string_to_md5(None))

    def test_string_to_md5_non_string(self):
        self.assertIsNone(string_to_md5(12345))
        self.assertIsNone(string_to_md5([1, 2, 3]))
        self.assertIsNone(string_to_md5({'a': 1, 'b': 2}))

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to ensure the function is working correctly:

- `test_string_to_md5`: This test case checks the function with different inputs, including a string, an empty string, None, an integer, a list, and a dictionary. It checks that the function returns the expected result for the string and None, and None for the other inputs.

- `test_string_to_md5_empty_string`: This test case checks that the function returns None for an empty string.

- `test_string_to_md5_none`: This test case checks that the function returns None for None.

- `test_string_to_md5_non_string`: This test case checks that the function returns None for non-string inputs.