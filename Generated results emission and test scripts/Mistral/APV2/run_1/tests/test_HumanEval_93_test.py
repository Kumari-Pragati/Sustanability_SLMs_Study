You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_93_code import encode
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """

    vowels = "aeiouAEIOU"
    vowels_replace = dict([(i, chr(ord(i) + 2)) for i in vowels])
    message = message.swapcase()
    return ''.join([vowels_replace[i] if i in vowels else i for i in message])

 Here is the complete unittest test suite for the provided `encode` function:


import unittest
from HumanEval_93_code import encode

class TestEncodeFunction(unittest.TestCase):

    def test_encode_single_word(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('Tset'), 'tGST')

    def test_encode_multiple_words(self):
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')
        self.assertEqual(encode('Hello World'), 'hLlO wOrLD')

    def test_encode_case_insensitive(self):
        self.assertEqual(encode('Test'), 'TGST')
        self.assertEqual(encode('tset'), 'tGST')

    def test_encode_vowels(self):
        self.assertEqual(encode('aeiou'), 'gHJKL')
        self.assertEqual(encode('AEIOU'), 'GHJKL')

    def test_encode_empty_string(self):
        self.assertEqual(encode(''), '')

    def test_encode_special_characters(self):
        self.assertRaises(TypeError, encode, 'test123')

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios such as single words, multiple words, case insensitivity, vowel replacement, empty string, and special characters. The test suite uses the `unittest.TestCase` class to define test methods and the `unittest.main()` function to run the tests.