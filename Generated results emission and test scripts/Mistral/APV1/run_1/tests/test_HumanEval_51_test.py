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

 Here is a comprehensive unittest test suite for the `remove_vowels` function:


import unittest
from HumanEval_51_code import remove_vowels

class TestRemoveVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_no_vowels(self):
        self.assertEqual(remove_vowels("abcdef\nghijklm"), 'bcdf\nghjklm')

    def test_only_vowels(self):
        self.assertEqual(remove_vowels('aaaaa'), '')

    def test_mixed_case(self):
        self.assertEqual(remove_vowels('aaBAA'), 'B')

    def test_special_characters(self):
        self.assertEqual(remove_vowels('zbcd'), 'zbcd')

    def test_multiple_vowels(self):
        self.assertEqual(remove_vowels('aeiou'), '')

    def test_long_string(self):
        self.assertEqual(remove_vowels("abcdefghijklmnopqrstuvwxyz"), 'bcdfghjklmnpqrstvwxyz')

    def test_punctuation(self):
        self.assertEqual(remove_vowels("abcdef,ghijklm!"), 'bcdf\nghjklm')

if __name__ == '__main__':
    unittest.main()


This test suite covers various edge cases and scenarios, ensuring that the `remove_vowels` function works as expected.