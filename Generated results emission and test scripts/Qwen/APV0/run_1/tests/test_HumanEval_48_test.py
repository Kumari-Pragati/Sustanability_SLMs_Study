system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_48_code import is_palindrome
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    for i in range(len(text)):
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True


assistant

import unittest

# Importing the function to be tested
from HumanEval_48_code import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character(self):
        self.assertTrue(is_palindrome('a'))
    
    def test_even_length_palindrome(self):
        self.assertTrue(is_palindrome('abba'))
    
    def test_odd_length_palindrome(self):
        self.assertTrue(is_palindrome('abcba'))
    
    def test_non_palindrome(self):
        self.assertFalse(is_palindrome('abcd'))

if __name__ == '__main__':
    unittest.main()


This script imports the `is_palindrome` function and creates a test class named `TestIsPalindrome`. It includes several test cases that cover different scenarios including empty strings, single characters, even-length palindromes, odd-length palindromes, and non-palindromic strings. The `unittest.main()` call at the end makes the tests executable when run as a standalone script.