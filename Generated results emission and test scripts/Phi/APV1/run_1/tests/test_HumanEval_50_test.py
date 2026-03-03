You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_50_code import decode_shift

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def encode_shift(s: str):
    """
    Returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input a string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

 import unittest
from HumanEval_50_code import encode_shift, decode_shift

class TestShiftFunctions(unittest.TestCase):

    def test_encode_shift(self):
        self.assertEqual(encode_shift('hello'), 'mjqqt')
        self.assertEqual(encode_shift('world'), 'adzsi')
        self.assertEqual(encode_shift('python'), 'ufytdq')
        self.assertEqual(encode_shift(''), '')
        self.assertEqual(encode_shift('a'), 'f')
        self.assertEqual(encode_shift('z'), 'e')
        self.assertEqual(encode_shift('abcdefghijklmnopqrstuvwxyz'), 'fghijklmnopqrstuvwxyzabcde')

    def test_decode_shift(self):
        self.assertEqual(decode_shift('mjqqt'), 'hello')
        self.assertEqual(decode_shift('adzsi'), 'world')
        self.assertEqual(decode_shift('ufytdq'), 'python')
        self.assertEqual(decode_shift(''), '')
        self.assertEqual(decode_shift('f'), 'a')
        self.assertEqual(decode_shift('e'), 'z')
        self.assertEqual(decode_shift('fghijklmnopqrstuvwxyzabcde'), 'abcdefghijklmnopqrstuvwxyz')

if __name__ == '__main__':
    unittest.main()