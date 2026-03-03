You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_10_code import make_palindrome
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if not string:
        return ''

    beginning_of_suffix = 0

    while not is_palindrome(string[beginning_of_suffix:]):
        beginning_of_suffix += 1

    return string + string[:beginning_of_suffix][::-1]

 Here is the complete unittest test suite for the `make_palindrome` function:


import unittest
from HumanEval_10_code import make_palindrome, is_palindrome

class TestMakePalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(make_palindrome(''), '')

    def test_single_char_string(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(make_palindrome(char), char + char)

    def test_palindrome(self):
        self.assertEqual(make_palindrome('racecar'), 'racecar')

    def test_non_palindrome(self):
        self.assertEqual(make_palindrome('cat'), 'catac')
        self.assertEqual(make_palindrome('cata'), 'catac')
        self.assertEqual(make_palindrome('hello'), 'olleh')
        self.assertEqual(make_palindrome('world'), 'dlrow')

    def test_palindrome_with_prefix(self):
        self.assertEqual(make_palindrome('catat'), 'catac')
        self.assertEqual(make_palindrome('worldd'), 'dlrow')

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('racecar'))
        self.assertFalse(is_palindrome('cat'))
        self.assertFalse(is_palindrome('hello'))
        self.assertTrue(is_palindrome('olleh'))
        self.assertTrue(is_palindrome('dlrow'))
        self.assertTrue(is_palindrome(''))

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases for the `make_palindrome` function, including empty strings, single character strings, palindromes, non-palindromes, and palindromes with prefixes. It also includes a test for the `is_palindrome` function to ensure it works correctly.