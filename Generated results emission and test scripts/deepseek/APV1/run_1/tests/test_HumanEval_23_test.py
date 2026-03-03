You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_23_code import strlen

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def strlen(string: str) -> int:
    """Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)


### Response:
Here is a Python unittest test suite for the given function:


import unittest
from HumanEval_23_code import strlen

class TestStrlen(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(''), 0)

    def test_non_empty_string(self):
        self.assertEqual(strlen('abc'), 3)

    def test_string_with_spaces(self):
        self.assertEqual(strlen('hello world'), 10)

    def test_string_with_special_characters(self):
        self.assertEqual(strlen('!@#$%^&*()'), 10)

    def test_string_with_numbers(self):
        self.assertEqual(strlen('1234567890'), 10)

    def test_string_with_mixed_characters(self):
        self.assertEqual(strlen('a1b2c3d4e5'), 10)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different types of strings: empty string, non-empty string, string with spaces, string with special characters, string with numbers, and string with mixed characters. Each test checks if the length of the string is calculated correctly.