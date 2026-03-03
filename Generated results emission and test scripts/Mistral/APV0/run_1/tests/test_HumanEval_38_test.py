Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_38_code import decode_cyclic
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def encode_cyclic(s: str):
    """
    Returns encoded string by cycling groups of three characters.
    """
    # Split string into groups, each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # Cycle elements in each group, unless the group has fewer than 3 elements.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    Takes as input a string encoded with the encode_cyclic function.
    Returns decoded string.
    """
    return encode_cyclic(encode_cyclic(s))

 Here is a unittest test script for the `encode_cyclic` and `decode_cyclic` functions:


import unittest
from HumanEval_38_code import encode_cyclic, decode_cyclic

class TestCyclicEncoding(unittest.TestCase):

    def test_encode_cyclic(self):
        self.assertEqual(encode_cyclic("abc"), "bca")
        self.assertEqual(encode_cyclic("abcdef"), "defabc")
        self.assertEqual(encode_cyclic("abcdefgh"), "ghabcdef")
        self.assertEqual(encode_cyclic("a"), "a")
        self.assertEqual(encode_cyclic("abcde"), "cdeab")
        self.assertEqual(encode_cyclic(""), "")

    def test_decode_cyclic(self):
        self.assertEqual(decode_cyclic("bca"), "abc")
        self.assertEqual(decode_cyclic("defabc"), "abcdef")
        self.assertEqual(decode_cyclic("ghabcdef"), "abcdefgh")
        self.assertEqual(decode_cyclic("a"), "a")
        self.assertEqual(decode_cyclic("cdeab"), "abcde")
        self.assertEqual(decode_cyclic(""), "")

if __name__ == '__main__':
    unittest.main()


This test script includes tests for the edge cases and various input scenarios. It uses the `assertEqual` method to compare the expected output with the actual output produced by the functions. You can run this script directly to test your functions.