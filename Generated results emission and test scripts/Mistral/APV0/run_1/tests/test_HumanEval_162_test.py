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

 Here is a unittest test script for the `string_to_md5` function:


import unittest
from HumanEval_162_code import string_to_md5

class TestStringToMD5(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(string_to_md5(''), None)

    def test_normal_string(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')

    def test_special_characters(self):
        self.assertEqual(string_to_md5('!@#$%^&*()_+-=[]{}|;:,.<>?'), 'e10adc3949ba59abbe56e057f20f883e')

    def test_long_string(self):
        long_string = '0' * 100
        self.assertIsInstance(string_to_md5(long_string), str)

if __name__ == '__main__':
    unittest.main()


This test script includes four test cases:

1. An empty string should return `None`.
2. A normal string ('Hello world') should return the expected MD5 hash.
3. A string with special characters should return the expected MD5 hash.
4. A long string (100 characters) should return a string (since it's an MD5 hash).

You can run this script directly by saving it as a .py file and running it with Python:


python test_string_to_md5.py


This will execute the tests and display the results. If all tests pass, it means the `string_to_md5` function is working correctly.