You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_50_code import encode_shift, decode_shift

class TestShiftFunctions(unittest.TestCase):
    def test_encode_decode(self):
        test_string = "hello"
        encoded = encode_shift(test_string)
        self.assertEqual(decode_shift(encoded), test_string)

    def test_encode_shift(self):
        test_string = "hello"
        expected_output = "mjqqt"
        self.assertEqual(encode_shift(test_string), expected_output)

    def test_decode_shift(self):
        test_string = "mjqqt"
        expected_output = "hello"
        self.assertEqual(decode_shift(test_string), expected_output)

    def test_encode_decode_special_chars(self):
        test_string = "hel!lo"
        encoded = encode_shift(test_string)
        self.assertEqual(decode_shift(encoded), test_string)

    def test_encode_shift_special_chars(self):
        test_string = "hel!lo"
        expected_output = "mjqq!t"
        self.assertEqual(encode_shift(test_string), expected_output)

    def test_decode_shift_special_chars(self):
        test_string = "mjqq!t"
        expected_output = "hel!lo"
        self.assertEqual(decode_shift(test_string), expected_output)

    def test_encode_decode_upper_case(self):
        test_string = "Hello"
        encoded = encode_shift(test_string)
        self.assertEqual(decode_shift(encoded), test_string)

    def test_encode_shift_upper_case(self):
        test_string = "Hello"
        expected_output = "Mjqqt"
        self.assertEqual(encode_shift(test_string), expected_output)

    def test_decode_shift_upper_case(self):
        test_string = "Mjqqt"
        expected_output = "Hello"
        self.assertEqual(decode_shift(test_string), expected_output)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for both the encoding and decoding functions, with both lower-case and upper-case letters, and also with special characters.