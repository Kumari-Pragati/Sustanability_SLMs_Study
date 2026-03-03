Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `encode` function:


import unittest
from HumanEval_93_code import encode

class TestEncodeFunction(unittest.TestCase):

    def test_encode_single_word(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('Test'), 'tGST')
        self.assertEqual(encode('TesT'), 'TGst')

    def test_encode_multiple_words(self):
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')
        self.assertEqual(encode('This Is A Message'), 'tHKS KS C MGSSCGG')
        self.assertEqual(encode('THIS IS A MESSAGE'), 'tHKS KS C MGSSCGG')

    def test_encode_mixed_case(self):
        self.assertEqual(encode('This Is A MeSSage'), 'tHKS KS C MGSSCGG')
        self.assertEqual(encode('THIS IS A MESSAGE'), 'tHKS KS C MGSSCGG')
        self.assertEqual(encode('THiS iS A MeSSage'), 'tHKS KS C MGSSCGG')

    def test_encode_empty_string(self):
        self.assertEqual(encode(''), '')

    def test_encode_special_characters(self):
        self.assertEqual(encode('This123 is a message@#'), 'tHKS 123 KS C MGSSCGG@##')

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as single words, multiple words, mixed case, empty string, and special characters. It uses the `unittest.TestCase.assertEqual` method to compare the expected and actual outputs of the `encode` function.