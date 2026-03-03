You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_162_code import string_to_md5

class TestStringToMD5(unittest.TestCase):
    def test_empty_string(self):
        self.assertIsNone(string_to_md5(''))

    def test_hello_world(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')

    def test_non_ascii_string(self):
        self.assertIsNone(string_to_md5('非ASCII字符串'))

    def test_none(self):
        self.assertIsNone(string_to_md5(None))

if __name__ == '__main__':
    unittest.main()


This test suite includes 4 test cases:

1. `test_empty_string`: Tests the function with an empty string. The expected result is `None`.
2. `test_hello_world`: Tests the function with the string 'Hello world'. The expected result is the md5 hash of 'Hello world'.
3. `test_non_ascii_string`: Tests the function with a string that contains non-ASCII characters. The expected result is `None` because the function only accepts strings in ASCII.
4. `test_none`: Tests the function with `None`. The expected result is `None`.

Please note that the function `string_to_md5` only accepts strings in ASCII. If you pass a string that contains non-ASCII characters, it will return `None`.