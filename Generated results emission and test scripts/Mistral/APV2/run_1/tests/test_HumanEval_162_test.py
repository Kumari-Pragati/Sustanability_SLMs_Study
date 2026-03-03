You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the `string_to_md5` function:


import unittest
from HumanEval_162_code import string_to_md5

class TestStringToMd5(unittest.TestCase):
    def test_empty_string(self):
        self.assertIsNone(string_to_md5(''))

    def test_normal_string(self):
        self.assertEqual(string_to_md5('Hello world'), '3e25960a79dbc69b674cd4ec67a72c62')

    def test_special_characters(self):
        self.assertEqual(string_to_md5('!@#$%^&*()_+-=[]{}|;:,.<>?'), '8c97e1546720204abf596c442e9a69e3')

    def test_long_string(self):
        long_text = '0' * 1000
        self.assertEqual(len(string_to_md5(long_text)), 32)

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases:

1. An empty string test case (`test_empty_string`)
2. A test case for a normal string (`test_normal_string`)
3. A test case for a string with special characters (`test_special_characters`)
4. A test case for a long string (`test_long_string`)

The test suite uses the `unittest.TestCase` class to define test methods and asserts that the expected output matches the actual output for each test case.