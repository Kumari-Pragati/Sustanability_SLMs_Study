system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

# Provided function
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


This test suite includes tests for various cases including empty strings, single characters, even-length palindromes, odd-length palindromes, and non-palindromic strings. It uses the `unittest` framework to run these tests effectively.