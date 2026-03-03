system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
        if text[i] != text[len(text) - 1 - i]:
            return False
    return True


assistant

import unittest

from HumanEval_48_code import is_palindrome


class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character(self):
        self.assertTrue(is_palindrome('a'))
        self.assertFalse(is_palindrome('b'))

    def test_even_length_palindrome(self):
        self.assertTrue(is_palindrome('racecar'))

    def test_odd_length_palindrome(self):
        self.assertTrue(is_palindrome('kayak'))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome('hello'))

    def test_mixed_case(self):
        self.assertTrue(is_palindrome('A man, a plan, a canal, Panama!'))

    def test_multiple_spaces(self):
        self.assertTrue(is_palindrome('The quick brown fox jumps over the lazy dog.'))

    def test_unicode_characters(self):
        self.assertTrue(is_palindrome('äöüß'))

    def test_numbers(self):
        self.assertTrue(is_palindrome('12321'))
        self.assertFalse(is_palindrome('12345'))

    def test_special_chars(self):
        self.assertTrue(is_palindrome('¡Hola, mundo!'))
        self.assertFalse(is_palindrome('¡Hola, Mundo!'))


if __name__ == '__main__':
    unittest.main()


This code snippet defines a comprehensive unittest test suite for the `is_palindrome` function. It includes tests for various edge cases and scenarios, ensuring that the function behaves as expected under different conditions.