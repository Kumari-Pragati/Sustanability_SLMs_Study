system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
from HumanEval_10_code import make_palindrome

class TestMakePalindrome(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(make_palindrome(""), "")

    def test_single_character(self):
        self.assertEqual(make_palindrome("a"), "a")

    def test_short_palindrome(self):
        self.assertEqual(make_palindrome("racecar"), "racecar")
        
    def test_medium_palindrome(self):
        self.assertEqual(make_palindrome("hello"), "olleh")
        
    def test_longer_palindrome(self):
        self.assertEqual(make_palindrome("level"), "leveldlevl")
        
    def test_non_palindrome(self):
        self.assertEqual(make_palindrome("world"), "dlrowo")
        
    def test_reverse_palindrome(self):
        self.assertEqual(make_palindrome("madam"), "madam")
        
    def test_middle_palindrome(self):
        self.assertEqual(make_palindrome("abba"), "abba")
        
    def test_large_input(self):
        large_string = "abcdefghijklmnopqrstuvwxyz"
        expected_output = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"
        self.assertEqual(make_palindrome(large_string), expected_output)
        
if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestMakePalindrome` class that inherits from `unittest.TestCase`. It contains several test methods to verify the correctness of the `make_palindrome` function using various inputs and edge cases. The `assertEqual` method checks whether the output of `make_palindrome` matches the expected result. If any test fails, it will raise an assertion error.