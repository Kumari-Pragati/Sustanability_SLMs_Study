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

 Here is a unittest test script for the `make_palindrome` function:


import unittest
from HumanEval_10_code import make_palindrome, is_palindrome

class TestMakePalindrome(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(make_palindrome(''), '')

    def test_single_char(self):
        self.assertEqual(make_palindrome('a'), 'a')
        self.assertEqual(make_palindrome('A'), 'A')
        self.assertEqual(make_palindrome('0'), '0')

    def test_simple_palindrome(self):
        self.assertEqual(make_palindrome('cat'), 'catac')
        self.assertEqual(make_palindrome('racecar'), 'racecar')
        self.assertEqual(make_palindrome('level'), 'levelle')

    def test_complex_palindrome(self):
        self.assertEqual(make_palindrome('cata'), 'catac')
        self.assertEqual(make_palindrome('kayak'), 'kayakayak')
        self.assertEqual(make_palindrome('amanaplanacanalpanama'), 'amanaplanacanalpanamanamanaplanacanalpanama')

    def test_non_palindrome(self):
        self.assertEqual(make_palindrome('hello'), 'elloholle')
        self.assertEqual(make_palindrome('world'), 'dlrowdlorw')
        self.assertEqual(make_palindrome('programming'), 'grammaringnorempap')

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome('racecar'))
        self.assertTrue(is_palindrome('level'))
        self.assertTrue(is_palindrome('catac'))
        self.assertTrue(is_palindrome(''))
        self.assertFalse(is_palindrome('hello'))
        self.assertFalse(is_palindrome('world'))
        self.assertFalse(is_palindrome('programming'))

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases for the `make_palindrome` function, as well as a test for the `is_palindrome` function that the `make_palindrome` function uses. To run the tests, simply execute the script. If all tests pass, the function is working correctly. If any tests fail, you'll need to debug the function to fix the issues.