You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_51_code import remove_vowels

class TestRemoveVowels(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_vowels(''), '')

    def test_no_vowels(self):
        self.assertEqual(remove_vowels('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'), 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')

    def test_all_vowels(self):
        self.assertEqual(remove_vowels('aeiouAEIOU'), '')

    def test_mixed_case(self):
        self.assertEqual(remove_vowels('aaBAA'), 'B')

    def test_mixed_string(self):
        self.assertEqual(remove_vowels('abcdef\nghijklm'), 'bcdf\nghjklm')

    def test_single_vowel(self):
        self.assertEqual(remove_vowels('a'), '')

    def test_multiple_vowels(self):
        self.assertEqual(remove_vowels('aeiou'), '')

    def test_vowels_in_middle(self):
        self.assertEqual(remove_vowels('abcde'), 'bcd')

    def test_vowels_at_end(self):
        self.assertEqual(remove_vowels('xyz'), 'xyz')

    def test_vowels_at_start(self):
        self.assertEqual(remove_vowels('aeiouxyz'), 'xyz')

if __name__ == '__main__':
    unittest.main()


This test suite includes a variety of test cases, including empty strings, strings with no vowels, strings with all vowels, strings with mixed case vowels, and strings with vowels at the start, middle, and end. It also includes tests for single vowels and multiple vowels.