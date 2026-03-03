system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


assistant

import unittest

# Importing the function we want to test
from HumanEval_10_code import make_palindrome

class TestMakePalindrome(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(make_palindrome(""), "")

    def test_single_character(self):
        self.assertEqual(make_palindrome("a"), "a")

    def test_short_palindrome(self):
        self.assertEqual(make_palindrome("racecar"), "racecar")
        
    def test_medium_palindrome(self):
        self.assertEqual(make_palindrome("level"), "leveldell")

    def test_longer_palindrome(self):
        self.assertEqual(make_palindrome("madamimadam"), "madamimadamadima")

    def test_non_palindrome(self):
        self.assertEqual(make_palindrome("hello"), "olleh")

if __name__ == '__main__':
    unittest.main()


This script imports the `make_palindrome` function and defines several test cases using the `unittest` framework. Each test case checks different scenarios to ensure the function behaves as expected. The `assertEqual` method is used to compare the output of `make_palindrome` against the expected results. If any test fails, an error message will be printed indicating which test failed and what the expected result was.