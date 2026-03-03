system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_51_code import remove_vowels

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def remove_vowels(text):
    """
    remove_vowels is a function that takes string and returns string without vowels.
    >>> remove_vowels('')
    ''
    >>> remove_vowels("abcdef\nghijklm")
    'bcdf\nghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    return "".join([s for s in text if s.lower() not in ["a", "e", "i", "o", "u"]])


assistant

import unittest
from HumanEval_51_code import remove_vowels

class TestRemoveVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_vowels(""), "")

    def test_single_char(self):
        self.assertEqual(remove_vowels("a"), "")
        self.assertEqual(remove_vowels("A"), "")

    def test_multiple_chars(self):
        self.assertEqual(remove_vowels("abcde"), "bcd")
        self.assertEqual(remove_vowels("hello world"), "hll wrld")

    def test_uppercase_letters(self):
        self.assertEqual(remove_vowels("HELLO WORLD"), "HLL WRLD")

    def test_lowercase_letters(self):
        self.assertEqual(remove_vowels("world"), "wrld")

    def test_numbers_and_punctuation(self):
        self.assertEqual(remove_vowels("Hello! World?"), "Hll! Wrld?")
        self.assertEqual(remove_vowels("1234567890"), "1234567890")

    def test_all_caps(self):
        self.assertEqual(remove_vowels("ALL CAPS"), "L CP")

    def test_all_lower(self):
        self.assertEqual(remove_vowels("all lower case"), "l l d c")

    def test_special_characters(self):
        self.assertEqual(remove_vowels("#$%&*+-=?@^_{}|~`"), "#$%&*+-=?@^_{}|~`")

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestRemoveVowels` class within the `unittest` framework, which contains several test cases to ensure the `remove_vowels` function behaves as expected across various scenarios. The tests cover empty strings, single characters, multiple characters including uppercase letters, numbers and punctuation, all caps, all lowercase, special characters, and more complex combinations of these elements.