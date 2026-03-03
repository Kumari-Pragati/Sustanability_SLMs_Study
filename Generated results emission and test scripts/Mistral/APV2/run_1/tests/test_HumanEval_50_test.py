You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])

 Here is the complete unittest test suite for the `encode_shift` and `decode_shift` functions:


import unittest
from HumanEval_50_code import encode_shift, decode_shift

class TestShiftFunctions(unittest.TestCase):

    def test_encode_shift(self):
        self.assertEqual(encode_shift("hello"), "mjqqt")
        self.assertEqual(encode_shift("world"), "baef")
        self.assertEqual(encode_shift("Python"), "Zltom")
        self.assertEqual(encode_shift(""), "")
        self.assertEqual(encode_shift("A"), "F")
        self.assertEqual(encode_shift("Z"), "c")

    def test_decode_shift(self):
        self.assertEqual(decode_shift("mjqqt"), "hello")
        self.assertEqual(decode_shift("baef"), "world")
        self.assertEqual(decode_shift("Zltom"), "Python")
        self.assertEqual(decode_shift(""), "")
        self.assertEqual(decode_shift("F"), "A")
        self.assertEqual(decode_shift("c"), "Z")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for both functions, covering various edge cases and empty strings. The test cases are designed to be self-explanatory and easy to understand.