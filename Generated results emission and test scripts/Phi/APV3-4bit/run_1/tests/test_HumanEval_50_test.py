### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_50_code import decode_shift
   - Define a single unittest.TestCase class
   - Include multiple test_ methods for normal, edge, and invalid inputs
   - End with if __name__ == '__main__': unittest.main()
4. Use only unittest assertions.
5. Do not include markdown, prose, or explanations.
6. Output must be runnable Python code.

### Example
#### Function:
def sum_of_elements(numbers: list) -> int:
    """Return the sum of all integers in a list."""
    return sum(numbers)

#### Test Script:
import unittest

class TestSumOfElements(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_of_elements([1, 2, 3, 4]), 10)

    def test_negative_numbers(self):
        self.assertEqual(sum_of_elements([-1, -2, -3]), -6)

    def test_empty_list(self):
        self.assertEqual(sum_of_elements([]), 0)

if __name__ == '__main__':
    unittest.main()
 ### Immediate Task
Write the complete unittest test suite for the following Python function.

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

 import unittest

from HumanEval_50_code import encode_shift, decode_shift

class TestShiftFunctions(unittest.TestCase):

    def test_encode_shift_normal(self):
        original_string = "hello"
        encoded_string = encode_shift(original_string)
        self.assertEqual(encoded_string, "mjqqt")

    def test_decode_shift_normal(self):
        encoded_string = "mjqqt"
        decoded_string = decode_shift(encoded_string)
        self.assertEqual(decoded_string, "hello")

    def test_encode_shift_edge(self):
        original_string = "z"
        encoded_string = encode_shift(original_string)
        self.assertEqual(encoded_string, "e")

    def test_decode_shift_edge(self):
        encoded_string = "e"
        decoded_string = decode_shift(encoded_string)
        self.assertEqual(decoded_string, "z")

    def test_encode_shift_invalid(self):
        with self.assertRaises(TypeError):
            encode_shift(123)

    def test_decode_shift_invalid(self):
        with self.assertRaises(TypeError):
            decode_shift(123)

if __name__ == '__main__':
    unittest.main()