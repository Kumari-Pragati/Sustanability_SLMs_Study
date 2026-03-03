You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 
import unittest
from HumanEval_48_code import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_letter(self):
        self.assertTrue(is_palindrome('a'))

    def test_multiple_same_letters(self):
        self.assertTrue(is_palindrome('aaaaa'))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome('zbcd'))

    def test_palindrome_with_spaces(self):
        self.assertTrue(is_palindrome('racecar'))

    def test_palindrome_with_case_insensitivity(self):
        self.assertTrue(is_palindrome('Racecar'))

    def test_palindrome_with_special_characters(self):
        self.assertTrue(is_palindrome('A man, a plan, a canal: Panama'))

    def test_non_palindrome_with_special_characters(self):
        self.assertFalse(is_palindrome('A man, a plan, a canal: Panama!'))

if __name__ == '__main__':
    unittest.main()


This test suite covers various cases for the `is_palindrome` function, including empty strings, single letters, multiple same letters, non-palindromes, palindromes with spaces, palindromes with case insensitivity, and palindromes with special characters. It ensures that the function behaves as expected in different scenarios.