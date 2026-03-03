system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Function to be tested
from HumanEval_50_code import encode_shift, decode_shift

class TestEncodeDecode(unittest.TestCase):

    def test_encode_decode(self):
        # Test case 1: Encodes "abc" to "fgh"
        self.assertEqual(encode_shift("abc"), "fgh")
        
        # Test case 2: Decodes "fgh" back to "abc"
        self.assertEqual(decode_shift("fgh"), "abc")

        # Test case 3: Encodes "xyz" to "efg"
        self.assertEqual(encode_shift("xyz"), "efg")
        
        # Test case 4: Decodes "efg" back to "xyz"
        self.assertEqual(decode_shift("efg"), "xyz")

        # Test case 5: Encodes "Hello World!" to "Mjqqt Bm!"
        self.assertEqual(encode_shift("Hello World!"), "Mjqqt Bm!")
        
        # Test case 6: Decodes "Mjqqt Bm!" back to "Hello World!"
        self.assertEqual(decode_shift("Mjqqt Bm!"), "Hello World!")

if __name__ == '__main__':
    unittest.main()


This unittest test suite includes two functions `encode_shift` and `decode_shift`, along with several test cases to ensure they work correctly. The `test_encode_decode` method contains assertions that check if the encoding and decoding processes produce expected results.