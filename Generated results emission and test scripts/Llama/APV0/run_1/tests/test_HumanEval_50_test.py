user

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
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])assistant

Here is a unittest test script for the `decode_shift` function:

Python
import unittest
from HumanEval_50_code import decode_shift

class TestDecodeShift(unittest.TestCase):

    def test_decode_shift_lowercase(self):
        self.assertEqual(decode_shift("y"), "a")
        self.assertEqual(decode_shift("z"), "e")
        self.assertEqual(decode_shift("a"), "f")
        self.assertEqual(decode_shift("b"), "g")
        self.assertEqual(decode_shift("c"), "h")
        self.assertEqual(decode_shift("d"), "i")

    def test_decode_shift_uppercase(self):
        self.assertEqual(decode_shift("Y"), "F")
        self.assertEqual(decode_shift("Z"), "E")
        self.assertEqual(decode_shift("A"), "F")
        self.assertEqual(decode_shift("B"), "G")
        self.assertEqual(decode_shift("C"), "H")
        self.assertEqual(decode_shift("D"), "I")

    def test_decode_shift_punctuation(self):
        self.assertEqual(decode_shift("Hello, World!"), "Hello, World!")

    def test_decode_shift_numbers(self):
        self.assertEqual(decode_shift("123"), "123")

    def test_decode_shift_empty_string(self):
        self.assertEqual(decode_shift(""), "")

    def test_decode_shift_non_alphabetic_characters(self):
        self.assertEqual(decode_shift("abc!@#"), "fhi!@#")

if __name__ == '__main__':
    unittest.main()


This script includes six test cases:

1. `test_decode_shift_lowercase`: Tests the decoding of lowercase letters.
2. `test_decode_shift_uppercase`: Tests the decoding of uppercase letters.
3. `test_decode_shift_punctuation`: Tests the decoding of punctuation characters.
4. `test_decode_shift_numbers`: Tests the decoding of numbers.
5. `test_decode_shift_empty_string`: Tests the decoding of an empty string.
6. `test_decode_shift_non_alphabetic_characters`: Tests the decoding of non-alphabetic characters.

Each test case uses the `assertEqual` method to check if the output of the `decode_shift` function matches the expected output.