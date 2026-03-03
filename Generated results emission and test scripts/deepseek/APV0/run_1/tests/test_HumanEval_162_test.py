You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


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


This script includes 4 test cases:

1. `test_empty_string`: Tests the function with an empty string. The expected result is `None`.
2. `test_hello_world`: Tests the function with the string 'Hello world'. The expected result is the md5 hash of 'Hello world'.
3. `test_non_ascii_string`: Tests the function with a string that contains non-ASCII characters. The expected result is `None` because the function can't encode non-ASCII characters.
4. `test_none`: Tests the function with `None`. The expected result is `None`.

To run the test, you can use the command `python -m unittest test_script.py` in the terminal, where `test_script.py` is the name of the script containing the test cases.