system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return "".join([chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s])


assistant

import unittest

# Function to be tested
from HumanEval_50_code import encode_shift, decode_shift

class TestEncodeDecodeShift(unittest.TestCase):

    def setUp(self):
        self.test_string = "HelloWorld"

    def test_encode_decode(self):
        # Encoding test
        encoded_str = encode_shift(self.test_string)
        decoded_str = decode_shift(encoded_str)

        self.assertEqual(decoded_str, self.test_string)

    def test_empty_string(self):
        empty_str = ""
        encoded_empty = encode_shift(empty_str)
        decoded_empty = decode_shift(encoded_empty)

        self.assertEqual(decoded_empty, empty_str)

    def test_single_char(self):
        single_char = "A"
        encoded_single = encode_shift(single_char)
        decoded_single = decode_shift(encoded_single)

        self.assertEqual(decoded_single, single_char)

    def test_uppercase(self):
        uppercase_str = "HELLO WORLD"
        encoded_uppercase = encode_shift(uppercase_str)
        decoded_uppercase = decode_shift(encoded_uppercase)

        self.assertEqual(decoded_uppercase, uppercase_str)

    def test_lowercase(self):
        lowercase_str = "hello world"
        encoded_lowercase = encode_shift(lowercase_str)
        decoded_lowercase = decode_shift(encoded_lowercase)

        self.assertEqual(decoded_lowercase, lowercase_str)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()


This script includes all necessary imports at the beginning, defines the `encode_shift` and `decode_shift` functions, and sets up a test class with various test cases to ensure the correctness of both encoding and decoding functions. The `unittest.main()` call at the end makes the tests executable when run directly.