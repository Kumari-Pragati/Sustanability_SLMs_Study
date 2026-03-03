You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False

 import unittest
from HumanEval_134_code import check_if_last_char_is_a_letter

class TestCheckIfLastCharIsALetter(unittest.TestCase):

    def test_last_char_is_letter(self):
        self.assertTrue(check_if_last_char_is_a_letter("apple pi e"))

    def test_last_char_is_not_letter(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple pie"))

    def test_last_char_is_space(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple pi e "))

    def test_empty_string(self):
        self.assertFalse(check_if_last_char_is_a_letter(""))

    def test_single_char_string(self):
        self.assertTrue(check_if_last_char_is_a_letter("a"))

    def test_non_alphabet_characters(self):
        self.assertFalse(check_if_last_char_is_a_letter("123"))
        self.assertFalse(check_if_last_char_is_a_letter("!@#"))
        self.assertFalse(check_if_last_char_is_a_letter("$%^&*"))

    def test_uppercase_characters(self):
        self.assertTrue(check_if_last_char_is_a_letter("A"))
        self.assertTrue(check_if_last_char_is_a_letter("Z"))

    def test_special_characters(self):
        self.assertFalse(check_if_last_char_is_a_letter("!"))
        self.assertFalse(check_if_last_char_is_a_letter("@"))
        self.assertFalse(check_if_last_char_is_a_letter("$"))

if __name__ == '__main__':
    unittest.main()