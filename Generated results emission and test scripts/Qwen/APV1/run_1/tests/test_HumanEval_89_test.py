system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_89_code import encrypt

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """

    d = 'abcdefghijklmnopqrstuvwxyz'
    out = ''
    for c in s:
        if c in d:
            out += d[(d.index(c) + 4) % 26]
        else:
            out += c
    return out


assistant

import unittest

# Function to be tested
from HumanEval_89_code import encrypt

# Test class
class TestEncrypt(unittest.TestCase):

    def test_encrypt(self):
        # Test cases
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')

    def test_non_alpha(self):
        # Test case with non-alphabetic characters
        self.assertEqual(encrypt('hello!'), 'lmpm!')

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestEncrypt` class within the `unittest` framework, which contains two test methods: `test_encrypt` and `test_non_alpha`. The `test_encrypt` method tests various inputs against the expected outputs of the `encrypt` function, while the `test_non_alpha` method checks that the function correctly handles strings containing non-alphabetic characters. The `unittest.main()` call at the end runs all the defined tests when this script is executed directly.