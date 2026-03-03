user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_134_code import check_if_last_char_is_a_letter
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else Falseassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_134_code import check_if_last_char_is_a_letter

class TestCheckIfLastCharIsALetter(unittest.TestCase):

    def test_last_char_is_a_letter(self):
        self.assertTrue(check_if_last_char_is_a_letter("apple pi e"))
        self.assertTrue(check_if_last_char_is_a_letter("banana e"))
        self.assertTrue(check_if_last_char_is_a_letter("cherry e "))

    def test_last_char_is_not_a_letter(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple pie"))
        self.assertFalse(check_if_last_char_is_a_letter("banana 123"))
        self.assertFalse(check_if_last_char_is_a_letter("cherry 456 "))

    def test_empty_string(self):
        self.assertFalse(check_if_last_char_is_a_letter(""))

    def test_last_char_is_space(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple pi e "))
        self.assertFalse(check_if_last_char_is_a_letter("banana e "))
        self.assertFalse(check_if_last_char_is_a_letter("cherry e  "))

if __name__ == '__main__':
    unittest.main()


This script includes four test cases:

- `test_last_char_is_a_letter`: Tests the function with strings that have a single alphabetical character at the end.
- `test_last_char_is_not_a_letter`: Tests the function with strings that do not have a single alphabetical character at the end.
- `test_empty_string`: Tests the function with an empty string.
- `test_last_char_is_space`: Tests the function with strings that have a space as the last character.