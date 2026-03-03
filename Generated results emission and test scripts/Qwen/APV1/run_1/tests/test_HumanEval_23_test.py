system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest
from HumanEval_23_code import strlen

class TestStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)
    
    def test_single_character_string(self):
        self.assertEqual(strlen("a"), 1)
    
    def test_multiple_characters_string(self):
        self.assertEqual(strlen("hello world"), 11)
    
    def test_whitespace_string(self):
        self.assertEqual(strlen("   "), 1)
    
    def test_special_characters_string(self):
        self.assertEqual(strlen("!@#$%^&*()"), 10)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestStringLength` class that inherits from `unittest.TestCase`. It contains several test methods to verify the correctness of the `strlen` function. Each method tests different scenarios such as empty strings, single-character strings, multiple-character strings, whitespace strings, and special characters. The `assertEqual` method is used to check if the output of the `strlen` function matches the expected result. Finally, the `unittest.main()` call runs all the test methods when the script is executed directly.