system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


This script imports `unittest` to create a test case class named `TestStringToMD5`. It then defines a method `test_string_to_md5` that uses assertions to check the correctness of the `string_to_md5` function. The `assertEqual` assertion checks if the output of `string_to_md5` matches the expected result. The `assertIsNone` assertions check if the function returns `None` when given specific inputs (an empty string, `None`, or an integer). Finally, it runs all tests using `unittest.main()`.