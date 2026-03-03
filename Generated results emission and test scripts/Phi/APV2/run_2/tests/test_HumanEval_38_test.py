You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function.
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

 import unittest
from HumanEval_38_code import decode_cyclic, encode_cyclic

class TestCyclicEncoding(unittest.TestCase):

    def test_encode_cyclic_empty_string(self):
        self.assertEqual(encode_cyclic(''), '')

    def test_encode_cyclic_single_character(self):
        self.assertEqual(encode_cyclic('a'), 'a')

    def test_encode_cyclic_multiple_characters(self):
        self.assertEqual(encode_cyclic('abc'), 'bca')

    def test_encode_cyclic_longer_string(self):
        self.assertEqual(encode_cyclic('abcdef'), 'bcadef')

    def test_encode_cyclic_string_with_remainder(self):
        self.assertEqual(encode_cyclic('abcdefgh'), 'bcadefgh')

    def test_decode_cyclic_empty_string(self):
        self.assertEqual(decode_cyclic(''), '')

    def test_decode_cyclic_single_character(self):
        self.assertEqual(decode_cyclic('a'), 'a')

    def test_decode_cyclic_multiple_characters(self):
        self.assertEqual(decode_cyclic('bca'), 'abc')

    def test_decode_cyclic_longer_string(self):
        self.assertEqual(decode_cyclic('bcadef'), 'abcdef')

    def test_decode_cyclic_string_with_remainder(self):
        self.assertEqual(decode_cyclic('bcadefgh'), 'abcdefgh')

if __name__ == '__main__':
    unittest.main()