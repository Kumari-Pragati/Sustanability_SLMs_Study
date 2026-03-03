You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is a complete unittest test suite for the `encode_cyclic` and `decode_cyclic` functions:


import unittest
from HumanEval_38_code import encode_cyclic, decode_cyclic

class TestCyclicEncoding(unittest.TestCase):

    def test_encode_cyclic(self):
        self.assertEqual(encode_cyclic("abc"), "bca")
        self.assertEqual(encode_cyclic("abcd"), "cdab")
        self.assertEqual(encode_cyclic("abcde"), "cdeab")
        self.assertEqual(encode_cyclic("abcdef"), "defabc")
        self.assertEqual(encode_cyclic(""), "")
        self.assertEqual(encode_cyclic("a"), "a")
        self.assertEqual(encode_cyclic("ab"), "ba")
        self.assertEqual(encode_cyclic("abc"), "bca")
        self.assertEqual(encode_cyclic("abcdefghij"), "jhigfedcba")

    def test_decode_cyclic(self):
        self.assertEqual(decode_cyclic("bca"), "abc")
        self.assertEqual(decode_cyclic("cdab"), "abcd")
        self.assertEqual(decode_cyclic("cdeab"), "abcde")
        self.assertEqual(decode_cyclic("defabc"), "abcdef")
        self.assertEqual(decode_cyclic(""), "")
        self.assertEqual(decode_cyclic("a"), "a")
        self.assertEqual(decode_cyclic("ba"), "ab")
        self.assertEqual(decode_cyclic("bca"), "abc")
        self.assertEqual(decode_cyclic("jhigfedcba"), "abcdefghij")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for edge cases, such as an empty string and a single character string, as well as tests for various input lengths. The test suite uses the `assertEqual` method to compare the expected output with the actual output of the functions.