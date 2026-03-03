You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given function:


import unittest
from HumanEval_93_code import encode

class TestEncode(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(encode('test'), 'TGST')
        self.assertEqual(encode('This is a message'), 'tHKS KS C MGSSCGG')
        self.assertEqual(encode('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 'abcDfgHiJklMnOpqRstUvwXyz')
        self.assertEqual(encode('abcdefghijklmnopqrstuvwxyz'), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.assertEqual(encode('AEIOUaeiou'), 'CgKqYcgkqy')
        self.assertEqual(encode('1234567890!@#$%^&*()'), '1234567890!@#$%^&*()')

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to ensure the function is working as expected. The first test case is a simple one, the second one checks if the function can handle spaces and capital letters, the third one checks if the function can handle all uppercase letters, the fourth one checks if the function can handle all lowercase letters, and the fifth one checks if the function can handle vowels. The last test case checks if the function can handle non-alphabet characters.