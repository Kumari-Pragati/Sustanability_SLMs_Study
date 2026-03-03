You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a comprehensive unittest test suite for the `is_palindrome` function:


import unittest
from HumanEval_48_code import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character(self):
        for char in ['a', 'A', '0', '9', '_']:
            self.assertTrue(is_palindrome(char))

    def test_palindrome(self):
        for palindrome in ['aba', 'level', 'racecar', 'deified', 'rotor', 'madam', 'radar']:
            self.assertTrue(is_palindrome(palindrome))

    def test_non_palindrome(self):
        for non_palindrome in ['zbcd', 'hello', 'world', 'python', 'javascript']:
            self.assertFalse(is_palindrome(non_palindrome))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty string, single characters, palindromes, and non-palindromes. It uses the `unittest.TestCase` class to define test methods and the `self.assertTrue()` and `self.assertFalse()` methods to verify the expected results.