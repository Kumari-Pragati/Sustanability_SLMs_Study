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

 import unittest
from HumanEval_48_code import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character(self):
        self.assertTrue(is_palindrome('a'))

    def test_palindrome_with_single_repeated_characters(self):
        self.assertTrue(is_palindrome('aba'))
        self.assertTrue(is_palindrome('aaaaa'))

    def test_non_palindrome_with_mixed_characters(self):
        self.assertFalse(is_palindrome('zbcd'))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome('racecar'))

    def test_palindrome_with_uppercase_letters(self):
        self.assertTrue(is_palindrome('Racecar'))

    def test_palindrome_with_special_characters(self):
        self.assertTrue(is_palindrome('A man, a plan, a canal: Panama'))

    def test_palindrome_with_numbers(self):
        self.assertTrue(is_palindrome('12321'))

    def test_palindrome_with_mixed_case(self):
        self.assertTrue(is_palindrome('Able was I saw Elba'))

    def test_palindrome_with_whitespace(self):
        self.assertTrue(is_palindrome('A man a plan a canal Panama'))

    def test_palindrome_with_punctuation(self):
        self.assertTrue(is_palindrome('Madam, in Eden, I’m Adam'))

    def test_palindrome_with_numbers_and_letters(self):
        self.assertTrue(is_palindrome('12321a'))

    def test_palindrome_with_numbers_and_special_characters(self):
        self.assertTrue(is_palindrome('12321!'))

    def test_palindrome_with_numbers_and_mixed_case(self):
        self.assertTrue(is_palindrome('12321A'))

    def test_palindrome_with_numbers_and_mixed_case_and_spaces(self):
        self.assertTrue(is_palindrome('12321 A'))

    def test_palindrome_with_numbers_and_mixed_case_and_punctuation(self):
        self.assertTrue(is_palindrome('12321! A'))

if __name__ == '__main__':
    unittest.main()