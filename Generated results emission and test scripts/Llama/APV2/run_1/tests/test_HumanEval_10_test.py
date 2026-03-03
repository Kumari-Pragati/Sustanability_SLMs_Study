system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

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

    return string + string[:beginning_of_suffix][::-1]assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_10_code import make_palindrome

class TestMakePalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(make_palindrome(''), '')

    def test_single_character_string(self):
        self.assertEqual(make_palindrome('a'), 'a')

    def test_non_palindrome_string(self):
        self.assertEqual(make_palindrome('cat'), 'catac')

    def test_palindrome_string(self):
        self.assertEqual(make_palindrome('cata'), 'catac')

    def test_long_palindrome_string(self):
        self.assertEqual(make_palindrome('abcdefgfedcba'), 'abcdefgfedcba')

    def test_string_with_spaces(self):
        self.assertEqual(make_palindrome('hello world'), 'hello worldolleh')

    def test_string_with_punctuation(self):
        self.assertEqual(make_palindrome('Hello, World!'), 'Hello, World!olleH')

    def test_string_with_numbers(self):
        self.assertEqual(make_palindrome('1234567654321'), '1234567654321')

    def test_string_with_special_characters(self):
        self.assertEqual(make_palindrome('!@#$%^&*()'), '!@#$%^&*()!@#$%^&*')

if __name__ == '__main__':
    unittest.main()