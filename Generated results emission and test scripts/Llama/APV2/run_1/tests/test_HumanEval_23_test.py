system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_23_code import strlen
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def strlen(string: str) -> int:
    """Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
    return len(string)assistant

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_23_code import strlen

class TestStrlen(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(strlen(""), 0)

    def test_single_character_string(self):
        self.assertEqual(strlen("a"), 1)

    def test_multiple_character_string(self):
        self.assertEqual(strlen("abc"), 3)

    def test_string_with_spaces(self):
        self.assertEqual(strlen("   "), 3)

    def test_string_with_punctuation(self):
        self.assertEqual(strlen("Hello, World!"), 12)

    def test_string_with_numbers(self):
        self.assertEqual(strlen("1234567890"), 10)

if __name__ == '__main__':
    unittest.main()