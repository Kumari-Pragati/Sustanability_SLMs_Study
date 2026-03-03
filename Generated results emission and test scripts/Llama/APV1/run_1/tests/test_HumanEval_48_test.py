user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
        if text[i]!= text[len(text) - 1 - i]:
            return False
    return Trueassistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_48_code import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character(self):
        self.assertTrue(is_palindrome('a'))

    def test_palindrome_with_even_length(self):
        self.assertTrue(is_palindrome('aba'))

    def test_palindrome_with_odd_length(self):
        self.assertTrue(is_palindrome('aaaaa'))

    def test_non_palindrome_with_even_length(self):
        self.assertFalse(is_palindrome('abcd'))

    def test_non_palindrome_with_odd_length(self):
        self.assertFalse(is_palindrome('zbcd'))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome('a b a'))

    def test_palindrome_with_punctuation(self):
        self.assertTrue(is_palindrome('A man, a plan, a canal: Panama'))

    def test_non_palindrome_with_spaces(self):
        self.assertFalse(is_palindrome('a b c'))

    def test_non_palindrome_with_punctuation(self):
        self.assertFalse(is_palindrome('Hello, world!'))

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of test cases, including:

- Empty string
- Single character
- Palindromes with even and odd lengths
- Non-palindromes with even and odd lengths
- Palindromes with spaces and punctuation
- Non-palindromes with spaces and punctuation

These tests ensure that the `is_palindrome` function is working correctly for a wide range of input strings.