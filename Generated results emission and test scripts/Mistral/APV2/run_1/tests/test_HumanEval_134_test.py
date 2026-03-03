You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is a comprehensive unittest test suite for the provided function `check_if_last_char_is_a_letter`. I've created several test cases to cover various scenarios.


import unittest
from HumanEval_134_code import check_if_last_char_is_a_letter

class TestCheckIfLastCharIsALetter(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(check_if_last_char_is_a_letter(""))

    def test_single_word(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple"))
        self.assertFalse(check_if_last_char_is_a_letter("pie"))

    def test_multiple_words(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple pie"))
        self.assertTrue(check_if_last_char_is_a_letter("apple pi e"))
        self.assertFalse(check_if_last_char_is_a_letter("apple pi e "))

    def test_special_characters(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple#"))
        self.assertFalse(check_if_last_char_is_a_letter("apple%"))
        self.assertFalse(check_if_last_char_is_a_letter("apple!"))

    def test_punctuation_marks(self):
        self.assertFalse(check_if_last_char_is_a_letter("apple."))
        self.assertFalse(check_if_last_char_is_a_letter("apple,"))
        self.assertFalse(check_if_last_char_is_a_letter("apple?"))
        self.assertFalse(check_if_last_char_is_a_letter("apple!"))

if __name__ == '__main__':
    unittest.main()


This test suite includes test cases for an empty string, single words, multiple words, special characters, and punctuation marks. It covers various scenarios and ensures that the function behaves as expected.