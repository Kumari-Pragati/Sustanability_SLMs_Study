system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
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
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])assistant

Here is the complete unittest test suite for the `decode_shift` function:


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
        self.assertEqual(decode_shift("Y"), "A")
        self.assertEqual(decode_shift("Z"), "E")
        self.assertEqual(decode_shift("A"), "F")
        self.assertEqual(decode_shift("B"), "G")
        self.assertEqual(decode_shift("C"), "H")
        self.assertEqual(decode_shift("D"), "I")

    def test_decode_shift_mixedcase(self):
        self.assertEqual(decode_shift("yY"), "aA")
        self.assertEqual(decode_shift("zZ"), "eE")
        self.assertEqual(decode_shift("aA"), "fF")
        self.assertEqual(decode_shift("bB"), "gG")
        self.assertEqual(decode_shift("cC"), "hH")
        self.assertEqual(decode_shift("dD"), "iI")

    def test_decode_shift_punctuation(self):
        self.assertEqual(decode_shift("hello world!"), "hello world!")
        self.assertEqual(decode_shift("This is a test."), "This is a test.")
        self.assertEqual(decode_shift("Hello, World!"), "Hello, World!")

    def test_decode_shift_numbers(self):
        self.assertEqual(decode_shift("123"), "123")
        self.assertEqual(decode_shift("456"), "456")
        self.assertEqual(decode_shift("789"), "789")

    def test_decode_shift_empty_string(self):
        self.assertEqual(decode_shift(""), "")

if __name__ == '__main__':
    unittest.main()