system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None


assistant

import unittest
from HumanEval_162_code import string_to_md5

class TestStringToMD5(unittest.TestCase):

    def test_string_to_md5(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')
        self.assertIsNone(string_to_md5(''))
        self.assertIsNone(string_to_md5(None))
        self.assertIsNone(string_to_md5(123))

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `unittest` test case class named `TestStringToMD5`. It includes two assertions to check that the `string_to_md5` function returns the correct MD5 hash for different inputs and handles edge cases such as an empty string, `None`, and non-string types. The `unittest.main()` call at the end runs all tests in this class.