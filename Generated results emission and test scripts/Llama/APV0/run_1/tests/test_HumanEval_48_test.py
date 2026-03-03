user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_48_code import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_palindrome(''))

    def test_single_character(self):
        self.assertTrue(is_palindrome('a'))

    def test_palindrome(self):
        self.assertTrue(is_palindrome('aba'))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome('zbcd'))

    def test_long_palindrome(self):
        self.assertTrue(is_palindrome('aaaaa'))

    def test_long_non_palindrome(self):
        self.assertFalse(is_palindrome('zyxwv'))

if __name__ == '__main__':
    unittest.main()


This script includes tests for the following cases:
- An empty string
- A single character
- A palindrome
- A non-palindrome
- A long palindrome
- A long non-palindrome

Each test case uses the `assertTrue` or `assertFalse` method to check if the result of the `is_palindrome` function matches the expected result.