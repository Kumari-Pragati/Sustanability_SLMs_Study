system
### Task Context
You are an expert Python programmer. Your only task is to write complete unittest test suites.

### Tone Context
Maintain a professional, precise, and methodical tone.

### Detailed Task Description & Rules
1. Analyze the provided Python function.
2. Generate a self-contained unittest test suite.
3. The output must:
   - Begin with import unittest
   - Include from HumanEval_162_code import string_to_md5
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

user
### Immediate Task
Write the complete unittest test suite for the following Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_162_code import string_to_md5
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None


assistant

import unittest
from HumanEval_162_code import string_to_md5

class TestStringToMD5(unittest.TestCase):
    def test_normal_input(self):
        result = string_to_md5("Hello world")
        expected = "3e25960a79dbc69b674cd4ec67a72c62"
        self.assertEqual(result, expected)

    def test_empty_string(self):
        result = string_to_md5("")
        self.assertIsNone(result)

    def test_single_character(self):
        result = string_to_md5("a")
        expected = "098f6bcd4621d373cade62dd31a2ff00"
        self.assertEqual(result, expected)

    def test_whitespace(self):
        result = string_to_md5(" ")
        expected = "20329ffdb5929eaedce6ab9e1056b0d3"
        self.assertEqual(result, expected)

    def test_multiple_characters(self):
        result = string_to_md5("Test")
        expected = "105ebcc5ad924968"
        self.assertEqual(result, expected)

    def test_all_uppercase(self):
        result = string_to_md5("TEST")
        expected = "D0E8A5C4"
        self.assertEqual(result, expected)

    def test_all_lowercase(self):
        result = string_to_md5("test")
        expected = "D0E8A5C4"
        self.assertEqual(result, expected)

    def test_mixed_case(self):
        result = string_to_md5("Test")
        expected = "D0E8A5C4"
        self.assertEqual(result, expected)

    def test_non_ascii(self):
        result = string_to_md5("你好")
        expected = "50efbeed0b61db110615bc8dedcfe1ca"
        self.assertEqual(result, expected)

    def test_unicode(self):
        result = string_to_md5(u"Unicode")
        expected = "160a02674550656e657420616e20616d732061676520616c6f206164617420616e617a6f67206167697320616e20616d6520616c6520616e617a6f67206167697320616e20616d6520616c6520616e617a6f67206167697320616e20616d6520616c6520616e617a6f67206167697320616e20616d6520616c6520616e617a6f67206167697320616e20616d6520616c6520616e617a6f67206167697320616e20616d6520616c6520616e617a6f67206167697320616e20616d6520616c6520616e617a6f67206167697320616e20616d6520616c6520616e617a6f67206167697320616e20616d6520616c6520616e617a6f67206167697320616e20616d6520616c6520616e617a6f67206167697320616e20616d6520616c6520616e617a6f672