You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_50_code import encode_shift, decode_shift

class TestShift(unittest.TestCase):
    def test_encode_decode(self):
        s = "hello"
        encoded = encode_shift(s)
        self.assertEqual(decode_shift(encoded), s)

    def test_encode_shift(self):
        s = "abc"
        expected = "fgh"
        self.assertEqual(encode_shift(s), expected)

    def test_decode_shift(self):
        s = "fgh"
        expected = "abc"
        self.assertEqual(decode_shift(s), expected)

    def test_encode_shift_special_chars(self):
        s = "hel!o"
        expected = "mjQ!t"
        self.assertEqual(encode_shift(s), expected)

    def test_decode_shift_special_chars(self):
        s = "mjQ!t"
        expected = "hel!o"
        self.assertEqual(decode_shift(s), expected)

    def test_encode_shift_empty_string(self):
        s = ""
        expected = ""
        self.assertEqual(encode_shift(s), expected)

    def test_decode_shift_empty_string(self):
        s = ""
        expected = ""
        self.assertEqual(decode_shift(s), expected)

if __name__ == '__main__':
    unittest.main()


This script includes a class `TestShift` that inherits from `unittest.TestCase`. The class includes several methods that test different aspects of the `encode_shift` and `decode_shift` functions. Each method asserts that the output of the function matches the expected result.

Please note that the `HumanEval_50_code` module should contain the `encode_shift` and `decode_shift` functions for the tests to pass.

To run the tests, you can save the script to a file (e.g., `test_shift.py`) and run it using Python. The `unittest` module will automatically discover and run the test methods.