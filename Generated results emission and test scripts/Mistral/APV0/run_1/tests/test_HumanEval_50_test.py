Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `encode_shift` and `decode_shift` functions:


import unittest
from HumanEval_50_code import encode_shift, decode_shift

class TestShiftFunctions(unittest.TestCase):

    def test_encode_shift(self):
        self.assertEqual(encode_shift("abc"), "fgh")
        self.assertEqual(encode_shift("ABC"), "DEF")
        self.assertEqual(encode_shift("123"), "123")  # Non-alphabetic characters should remain the same
        self.assertEqual(encode_shift(""), "")
        self.assertEqual(encode_shift("Z"), "A")  # Handles wrapping around the alphabet
        self.assertEqual(encode_shift("aaa"), "def")  # Handles multiple occurrences of the same character

    def test_decode_shift(self):
        self.assertEqual(decode_shift("fgh"), "abc")
        self.assertEqual(decode_shift("DEF"), "ABC")
        self.assertEqual(decode_shift("123"), "123")  # Non-alphabetic characters should remain the same
        self.assertEqual(decode_shift(""), "")
        self.assertEqual(decode_shift("A"), "Z")  # Handles wrapping around the alphabet
        self.assertEqual(decode_shift("def"), "aaa")  # Handles multiple occurrences of the same character

if __name__ == '__main__':
    unittest.main()


This test script includes tests for edge cases, such as handling multiple occurrences of the same character, non-alphabetic characters, and wrapping around the alphabet. It also tests the functions with empty strings.