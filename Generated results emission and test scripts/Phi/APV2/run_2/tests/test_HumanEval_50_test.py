You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
        self.assertEqual(encode_shift('world'), 'btwqi')
        self.assertEqual(encode_shift('python'), 'udymts')
        self.assertEqual(encode_shift(''), '')

    def test_decode_shift(self):
        self.assertEqual(decode_shift('mjqqt'), 'hello')
        self.assertEqual(decode_shift('btwqi'), 'world')
        self.assertEqual(decode_shift('udymts'), 'python')
        self.assertEqual(decode_shift(''), '')

    def test_encode_shift_with_uppercase(self):
        self.assertEqual(encode_shift('Hello'), 'Mjqqt')
        self.assertEqual(encode_shift('WORLD'), 'BTWQI')
        self.assertEqual(encode_shift('PYTHON'), 'UDYMTS')
        self.assertEqual(encode_shift(''), '')

    def test_decode_shift_with_uppercase(self):
        self.assertEqual(decode_shift('Mjqqt'), 'Hello')
        self.assertEqual(decode_shift('BTWQI'), 'WORLD')
        self.assertEqual(decode_shift('UDYMTS'), 'PYTHON')
        self.assertEqual(decode_shift(''), '')

    def test_encode_shift_with_non_alphabet_characters(self):
        self.assertEqual(encode_shift('abc123!'), 'mjq178!')
        self.assertEqual(encode_shift('#$%'), '&^%')
        self.assertEqual(encode_shift('123'), '678')
        self.assertEqual(encode_shift(''), '')

    def test_decode_shift_with_non_alphabet_characters(self):
        self.assertEqual(decode_shift('mjq178!'), 'abc123!')
        self.assertEqual(decode_shift('&^%'), '#$%')
        self.assertEqual(decode_shift('678'), '123')
        self.assertEqual(decode_shift(''), '')

if __name__ == '__main__':
    unittest.main()


This test suite covers various cases for the `encode_shift` and `decode_shift` functions, including:

- Basic alphabetical characters
- Uppercase letters
- Non-alphabetical characters
- Empty string

Each test case ensures that the functions correctly encode and decode strings as expected. The test cases are designed to be comprehensive and cover different scenarios to validate the correctness of the functions.