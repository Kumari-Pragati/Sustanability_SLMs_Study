You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 
import unittest
from HumanEval_93_code import encode

class TestEncodeFunction(unittest.TestCase):

    def test_swapcase(self):
        self.assertEqual(encode('test'), 'TGST')

    def test_vowel_replacement(self):
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')

    def test_no_change_for_non_vowels(self):
        self.assertEqual(encode('Hello World'), 'hELLO wORLD')

    def test_no_change_for_empty_string(self):
        self.assertEqual(encode(''), '')

    def test_single_character(self):
        self.assertEqual(encode('a'), 'c')

    def test_special_characters(self):
        self.assertEqual(encode('!@#$%^&*()'), '!@#$%^&*()')

    def test_uppercase_vowels(self):
        self.assertEqual(encode('AEIOU'), 'CEIOU')

    def test_lowercase_vowels(self):
        self.assertEqual(encode('aeiou'), 'ceio')

    def test_mixed_case_vowels(self):
        self.assertEqual(encode('AeIoU'), 'CEIOU')

    def test_vowels_at_end_of_string(self):
        self.assertEqual(encode('message'), 'MGSSCGG')

    def test_vowels_in_middle_of_string(self):
        self.assertEqual(encode('This is a test'), 'tHKS KS C TGST')

    def test_vowels_at_beginning_of_string(self):
        self.assertEqual(encode('Test message'), 'TGST MGSSCGG')

    def test_vowels_in_consecutive_order(self):
        self.assertEqual(encode('aeiou'), 'ceio')

    def test_vowels_in_reverse_order(self):
        self.assertEqual(encode('uoiea'), 'ceio')

    def test_vowels_with_spaces(self):
        self.assertEqual(encode('This is a test message'), 'tHKS KS C MGSSCGG')

    def test_vowels_with_numbers(self):
        self.assertEqual(encode('1234567890'), '1234567890')

    def test_vowels_with_special_characters(self):
        self.assertEqual(encode('!@#$%^&*123'), '!@#$%^&*123')

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios for the `encode` function, including different cases, positions of vowels, and the presence of non-alphabetic characters. It ensures that the function behaves as expected across a wide range of inputs.